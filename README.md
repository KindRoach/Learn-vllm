# Prepare Models
Create a dir `/models` and move model files there, or change the path 
in [devcontainer.json](.devcontainer/devcontainer.json) to your model dir.

# Run vllm openai server

```bash
bash run-vllm-server.sh 
```

# Debug Offline Inference / Online Server

Then debug module `vllm.entrypoints.openai.api_server` (don't forget to use args `--enforce_eager` to disable torch compile)
or script `offline.py` using your favorite IDE.

# Benchmark

```bash
bash run-bench.sh
```
