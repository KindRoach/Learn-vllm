#!/bin/bash

model="/models/Qwen3-4B"

vllm serve ${model} \
        --kv-transfer-config \
        '{"kv_connector":"SharedStorageConnector","kv_role":"kv_both","kv_connector_extra_config": {"shared_storage_path": "local_storage"}}'
