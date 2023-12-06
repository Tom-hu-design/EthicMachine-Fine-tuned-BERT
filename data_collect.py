import os
from openai import OpenAI
import pandas as pd
import json

df_master = pd.DataFrame()

client = OpenAI(
    api_key="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",
)

for x in range(12*12):
    response = client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    response_format={ "type": "json_object" },
    messages=[
        {"role": "system", "content": "You are a helpful assistant designed to output JSON.You are an ethical story writer guiding individuals on expressing technomoral values in their real world actions. Present neutral scenarios, or scenarios that are irrelevant. Create contexts of the story according to what the prompt asks, make sure that you only output JSON responses with the format { 'Neutral': […]}"},
        # {"role": "system", "content": "You are a helpful assistant designed to output JSON.You are an ethical story writer guiding individuals on expressing technomoral values in their real world actions. Present diverse scenarios, values representation, and make sure that your descriptions follows Shannon Vallor's 12 technomoral values. Prioritize clarity and brevity in the generated examples. Your outputs should be in the form {Boolean: content}. Make sure that you are not repeating over the same content in your. Follow the following JSON structure { 'Positive': […],'Negative': […]}. inside each parameter should be content only."},
        {"role": "user", "content": "Describe a real world scenario of now, or a story like description of the near future where an individual is in a more technologically complex society. You will be writing and describing the characteristics of 'Ethic neutral: actions, behaviors, or situations that do not inherently carry a moral judgment or value.the action itself is not inherently moral or immoral. Ethical neutrality is exemplified by decisions that lack inherent moral judgment' You should come up an description of the context + person's action, shorter than 280 charaters. Give 10 examples that adheres to this character, or neutral statements that are not related to this topic."}
        # {"role": "user", "content": "Describe a real world scenario of now, or a story like description of the near future where an individual is in a more technologically complex society. You will be writing and describing the characteristics of 'Ethic neutral: a habitual choice of inclining to increase the welfare of others through action. New media systems disconnect ones from each other, leading to narcissism; Technology shares information in a way that overloads emotions and wears down empathy.' You should come up an description of the context + person's action, shorter than 280 charaters. Give 10 positive examples that adheres to this character, and gives 10 negative examples that violates this character"}
    ]
    )

    GPT_response_raw = response.choices[0].message.content
    df_raw = pd.read_json(GPT_response_raw)

    print(df_raw)
    df_master = pd.concat([df_master,df_raw])
df_master.to_csv('Neutral.csv')


