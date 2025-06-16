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
bash run-vllm-server.sh 
```

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

# A

Download the `api_server.py` script:

```bash
wget https://github.com/vllm-project/vllm/blob/main/vllm/entrypoints/openai/api_server.py
```

Then debug this script using your favorite IDE. Don't forget to set env `TORCH_COMPILE_DISABLE=1`.