#!/bin/bash

./llmapibenchmark_linux_amd64 \
    -base_url http://127.0.0.1:8000/v1 \
    -numWords 1024 \
    -max_tokens 512
