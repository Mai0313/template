import shutil
from pathlib import Path

from pydantic import Field, BaseModel, ConfigDict, computed_field
from rich.progress import Progress


class DocsGenerator(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    source: str = Field(..., frozen=True)
    output: str = Field(..., frozen=True)
    exclude: str = Field(
        default=".venv",
        description="Exclude the folder or file, it should be separated by comma.",
        examples=[".venv,.git,.idea"],
    )

    @computed_field
    @property
    def _source_path(self) -> Path:
        return Path(self.source)

    @computed_field
    @property
    def _output_path(self) -> Path:
        return Path(self.output)

    @staticmethod
    def __gen_single_docs(docs_path: Path, file: Path) -> str:
        _output_docs_path = Path(docs_path / file.with_suffix(".md").name)
        _output_docs_path.parent.mkdir(parents=True, exist_ok=True)
        _output_docs_path.unlink(missing_ok=True)
        _note_content = f"::: {file.as_posix().removesuffix('.py').replace('/', '.')}\n"
        _output_docs_path.write_text(data=_note_content, encoding="utf-8")
        return _output_docs_path.as_posix()

    def __remove_existing_folder(self) -> None:
        if self._output_path.exists():
            shutil.rmtree(self._output_path.absolute())
            self._output_path.mkdir(parents=True, exist_ok=True)

    def gen_docs(self) -> None:
        with Progress() as progress:
            task = progress.add_task("[green]Generating docs...")
            if self._source_path.is_dir():
                self.__remove_existing_folder()

                need_to_exclude = [*self.exclude.split(","), "__init__.py"]
                files = self._source_path.glob("**/*.py")
                all_files = [
                    file for file in files if not any(f in file.parts for f in need_to_exclude)
                ]

                progress.update(
                    task_id=task, description="[cyan]Files Found...", total=len(all_files)
                )

                for file in all_files:
                    docs_path = Path(
                        f"{self._output_path}/{file.parent.relative_to(self._source_path)}"
                    )
                    processed_file = self.__gen_single_docs(docs_path=docs_path, file=file)
                    progress.update(
                        task_id=task,
                        advance=1,
                        description=f"[cyan]Processing {processed_file}...",
                        refresh=True,
                    )

            elif self._source_path.is_file():
                progress.update(task_id=task, description="[cyan]Files Found...", total=1)
                processed_file = self.__gen_single_docs(self._output_path, self._source_path)
                progress.update(
                    task_id=task,
                    advance=1,
                    description=f"[cyan]Processing {processed_file}...",
                    refresh=True,
                )
            else:
                raise ValueError("Invalid source path")


if __name__ == "__main__":
    import fire

    fire.Fire(DocsGenerator)

    # pair_list = {
    #     "./app": "./docs/API",
    #     "./src": "./docs/Dashboard",
    #     "./pages": "./docs/Page",
    #     "./api.py": "./docs/API",
    # }
    # for key, value in pair_list.items():
    #     docs_generator = DocsGenerator(source_path=key, docs_path=value)
    #     docs_generator.gen_docs()
