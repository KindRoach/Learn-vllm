from vllm import SamplingParams, LLM
from vllm.config import KVTransferConfig

if __name__ == '__main__':

    model_name = "/models/Qwen3-4B"

    prompts = [
        "Hello, my name is",
        "The president of the United States is",
        "The capital of France is",
        "The future of AI is",
    ]

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

    sampling_params = SamplingParams(temperature=0.8, top_p=0.95)
    outputs = llm.generate(prompts, sampling_params)

    for output in outputs:
        prompt = output.prompt
        generated_text = output.outputs[0].text
        print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")
