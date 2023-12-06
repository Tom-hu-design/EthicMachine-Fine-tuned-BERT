
# EthicMachine-Fine-tuned-BERT: Fine-tuning BERT-based classifier to identify idealized cultural behavior through GPT-generated data.
Expectation: The model will be able to learn and identify whether an input aligns with Shannon Vallor’s 12 technomoral values. The primary objective of the model will be giving out a yes or no response of whether an input is a technomoral value. If this is achieved, the next step would be classifying which of the 12 technomoral values that the input would be grouped to.
### Model Input: The inputs to the model will be short, tweet-styled descriptions of one’s action. (Less than 25 words)
### Model Output: The output of the model will be whether this action is included in the 12 technomoral values. (Outputting a Yes/No answer)
Training dataset: The training dataset will be generated solely by Chat GPT 3.5 (or other alternative models). The dataset would be first manually reviewed to ensure that the labeling is correct and accurate. The expected size of the training dataset would be around ~1000 individual inputs labeled.

Chat GPT would be given a specific prompt and persona so that it would give examples of actions that fit in one of the technomoral values. (Acceptable behavior) Then, the model would be asked to give a counter-example to the previous example. (Unacceptable behavior) Chat GPT would give its initial labels to the two, and such classification will then be re-examined by a human to ensure its accuracy. The data will then be cleaned and fed into the untrained network for the pre-training process. The training goal would be classifying between acceptable behavior and unacceptable behavior through the 12 technomoral values.
## Project Objectives:
#### 1. The primary objective of this project would be to examine whether AI-generated datasets can be a reliable source of training data for training other AI models.
#### 2. The secondary objective of this project would be to examine whether AI can classify actions based on values rather than pre-assigned goals.
#### 3. The final objective of this project would be to test out if the AI can be used to provide AI feedback and fine-tune another model. (RLAIF)
