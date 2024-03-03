#!/bin/bash
current_dir_name=$(basename "$(pwd)")
docker build -t $current_dir_name -f docker/Dockerfile .
