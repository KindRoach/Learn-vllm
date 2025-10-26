#!/bin/bash

model_name="/models/Qwen3-4B"

vllm bench serve \
  --model "${model_name}" \
  --dataset-name random \
  --num-prompts 1024 \
  --max-concurrency 16 \
  --random-input-len 512 \
  --random-output-len 128 \
  --ignore-eos
