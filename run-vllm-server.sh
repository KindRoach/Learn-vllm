#!/bin/bash

vllm serve /models/Qwen3-4B \
    --disable-log-requests \
    --no-enable-prefix-caching
