#!/bin/bash

MODEL_DIR=/models

docker run --rm -it \
    -v $MODEL_DIR:/models:ro \
    --network host \
    vllm/vllm-openai \
    --host 0.0.0.0 \
    --port 8000 \
    --model /models/Qwen3-4B
    --dtype auto
