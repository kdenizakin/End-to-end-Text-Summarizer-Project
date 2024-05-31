from textSummarizer.config.configuration import ConfigurationManager
from transformers import AutoTokenizer
from transformers import pipeline


class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_config_model_evaluation()

    def predicts(self, given_text):
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        model_path = self.config.model_path
        pipeline_obj = pipeline("summarization", model=model_path,tokenizer=tokenizer)


        gen_kwargs = {"length_penalty": 0.8, "num_beams":8, "max_length": 200}

        print("Given input:")
        print(given_text)


        print("\Model Summary:")
        model_predcition = pipeline_obj(given_text, **gen_kwargs)[0]["summary_text"]
        print(model_predcition)

        return model_predcition

