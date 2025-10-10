# Clone repo

```bash
git clone https://github.com/vllm-project/vllm.git
```

# Dev ENV

```bash
docker pull vllm/vllm-openai
```

# Run vllm openai server in Container

```bash
bash run-vllm-server-in-docker.sh 
```

# Debug Offline Inference / Online Server

Then debug module `vllm.entrypoints.openai.api_server` or script `offline.py` using your favorite IDE.

Don't forget to set env `TORCH_COMPILE_DISABLE=1`.

# Benchmark

Download tools:

```bash
wget https://github.com/Yoosu-L/llmapibenchmark/releases/download/v1.0.2/llmapibenchmark_linux_amd64
chmod +x llmapibenchmark_linux_amd64
```

Run tools:

```bash
bash run-bench.sh
```
