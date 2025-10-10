from vllm import SamplingParams, LLM
from vllm.config import KVTransferConfig


def test_kv_transfer(llm: LLM):
    doc = """
    vLLM is a fast and easy-to-use library for LLM inference and serving.

    Originally developed in the Sky Computing Lab at UC Berkeley, vLLM has evolved into a community-driven project with contributions from both academia and industry.

    vLLM is fast with:

    State-of-the-art serving throughput
    Efficient management of attention key and value memory with PagedAttention
    Continuous batching of incoming requests
    Fast model execution with CUDA/HIP graph
    Quantizations: GPTQ, AWQ, AutoRound, INT4, INT8, and FP8
    Optimized CUDA kernels, including integration with FlashAttention and FlashInfer
    Speculative decoding
    Chunked prefill
    vLLM is flexible and easy to use with:

    Seamless integration with popular Hugging Face models
    High-throughput serving with various decoding algorithms, including parallel sampling, beam search, and more
    Tensor, pipeline, data and expert parallelism support for distributed inference
    Streaming outputs
    OpenAI-compatible API server
    Support for NVIDIA GPUs, AMD CPUs and GPUs, Intel CPUs and GPUs, PowerPC CPUs, and TPU. Additionally, support for diverse hardware plugins such as Intel Gaudi, IBM Spyre and Huawei Ascend.
    Prefix caching support
    Multi-LoRA support
    vLLM seamlessly supports most popular open-source models on HuggingFace, including:

    Transformer-like LLMs (e.g., Llama)
    Mixture-of-Expert LLMs (e.g., Mixtral, Deepseek-V2 and V3)
    Embedding Models (e.g., E5-Mistral)
    Multi-modal LLMs (e.g., LLaVA)
    """

    sampling_params = SamplingParams(temperature=0.8, top_p=0.95)

    # the first call save cache to disk
    llm.generate([doc, ], sampling_params)

    # the second call load cache from disk
    llm.generate([doc, ], sampling_params)


if __name__ == '__main__':
    model_name = "/models/Qwen3-4B"
    kv_transfer_config = KVTransferConfig(
        kv_connector="SharedStorageConnector",
        kv_role="kv_both",
        kv_connector_extra_config={"shared_storage_path": "local_storage"}
    )

    llm = LLM(
        model=model_name,
        distributed_executor_backend="mp",
        kv_transfer_config=kv_transfer_config,
    )

    test_kv_transfer(llm)
