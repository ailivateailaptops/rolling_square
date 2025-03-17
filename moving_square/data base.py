from gpt4all import GPT4All
model_path="/Users/Yagnanarayana.d/Downloads/falcon.70.instruct.Q4_0."
model=GPT4All(model_path)
prompt1=f"""Ask me a Grammer MCQ with 4 options to test my knowledge on tenses"""

question =model.generate(prompt1)
print(question)