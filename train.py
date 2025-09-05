from datasets import load_dataset
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, TrainingArguments, Trainer, DataCollatorForSeq2Seq

model_name = "google/flan-t5-small"
dataset = load_dataset("json", data_files="recipes.jsonl")

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def preprocess(examples):
    inputs = ["Ingredients: " + ing for ing in examples["ingredients"]]
    targets = examples["recipe"]
    model_inputs = tokenizer(inputs, max_length=64, truncation=True)
    labels = tokenizer(targets, max_length=128, truncation=True)
    model_inputs["labels"] = labels["input_ids"]
    return model_inputs

tokenized = dataset.map(preprocess, batched=True)

training_args = TrainingArguments(
    output_dir="./recipe-llm",
    per_device_train_batch_size=4,
    num_train_epochs=3,
    save_total_limit=2,        
    logging_dir="./logs",
    logging_steps=50,
    do_train=True,
    do_eval=False                
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized["train"],
    tokenizer=tokenizer,
    data_collator=DataCollatorForSeq2Seq(tokenizer, model=model),
)

trainer.train()
trainer.save_model("./recipe-llm")
tokenizer.save_pretrained("./recipe-llm")
