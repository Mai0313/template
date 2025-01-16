from pydantic import Field, BaseModel, ConfigDict, AliasChoices


class Response(BaseModel):
    model_config = ConfigDict(use_attribute_docstrings=True)
    name: str = Field(
        ...,
        title="Name",
        description="The name of the response.",
        validation_alias=AliasChoices("name", "Name"),
        frozen=False,
        deprecated=False,
    )
    content: str = Field(
        ...,
        title="Content",
        description="The content of the response.",
        validation_alias=AliasChoices("content", "Content"),
        frozen=False,
        deprecated=False,
    )


def hello_fn() -> Response:
    """Generates a greeting response.

    This function creates a Response object with a predefined name and content.
    The name is set to "Wei" and the content is set to "Hello, World!".

    Returns:
        Response: An object containing the name and content.
    """
    name = "Wei"
    content = "Hello, World!"
    template_model = Response(name=name, content=content)
    return template_model


async def a_hello_fn() -> Response:
    """Asynchronous function that creates a Response object with a greeting message.

    Returns:
        Response: An object containing the name and greeting message.
    """
    name = "Wei"
    content = "Hello, World!"
    template_model = Response(name=name, content=content)
    return template_model


if __name__ == "__main__":
    result = hello_fn()
