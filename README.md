
# 🍳 Local LLM Recipe Chatbot

This project is a **recipe suggestion chatbot** that runs entirely locally using a lightweight **language model (LLM)**. Users provide a list of ingredients, and the system returns recipe suggestions based on the input. The system integrates a **FastAPI backend** for serving the model and a **Streamlit frontend** for an interactive user interface.

---

## 📌 Project Overview

The project consists of three main components:

1. **Dataset Preparation:** A JSONL file containing ingredients and corresponding recipes is used to fine-tune the LLM. Each record represents a mapping from ingredients to a recipe.

2. **Local LLM Fine-Tuning:** A CPU-friendly open-source LLM (e.g., Flan-T5 Small) is fine-tuned on the recipe dataset. Fine-tuning allows the model to learn patterns between ingredients and recipes and produce relevant suggestions when given new inputs.

3. **API Serving with FastAPI:** The fine-tuned model is served locally through a REST API using FastAPI. The API accepts ingredient inputs from the user, passes them to the model, and returns recipe suggestions in JSON format.

4. **Interactive Chatbot UI:** A Streamlit web application provides a friendly interface for the user to input ingredients. The frontend sends requests to the API and displays the returned recipe suggestions in a conversational format.



## ⚙️ Workflow Description

### Step 1: Dataset Preparation

* Collect a diverse set of recipes and their ingredients.
* Organize the dataset in a structured JSONL format where each entry contains:

  * `ingredients`: A comma-separated list of ingredients.
  * `recipe`: The corresponding recipe or cooking instructions.
* This dataset acts as the knowledge base for fine-tuning the LLM.

### Step 2: Fine-Tuning the Local LLM

* Select a **lightweight, CPU-friendly model** suitable for instruction-based tasks.
* Train the model using the prepared dataset so that it can generate recipes based on ingredients.
* Save the fine-tuned model locally for future inference.

### Step 3: Deploying FastAPI Backend

* The fine-tuned model is loaded in a FastAPI server.
* The API exposes an endpoint that accepts JSON requests containing ingredients.
* The server processes the input, queries the model, and returns a JSON response with the recommended recipe.
* This step allows for easy integration with any frontend application.

### Step 4: Interactive Chatbot via Streamlit

* The Streamlit frontend provides a simple web interface for users.
* Users input ingredients into a text box.
* The frontend sends a request to the FastAPI backend and receives a recipe in response.
* The recipe is displayed on the web interface, enabling an interactive conversation-like experience.

### Step 5: User Interaction Flow

1. User enters ingredients (e.g., “Egg, Onion”) into the Streamlit UI.
2. The frontend sends the input to the FastAPI API.
3. The API queries the fine-tuned LLM and generates a recipe.
4. The response is returned to the frontend.
5. The recipe is displayed to the user.

### Workflow

run python train.py

Start FastAPI server:

uvicorn main:app --reload


Start Streamlit UI:

streamlit run app.py


Open the browser → http://localhost:8501

Enter ingredients like Egg, Onion

Get the recipe suggestion from the model!
## ✅ Benefits of this Workflow

* **Lightweight and CPU-friendly:** Can run on a personal computer without GPU.
* **Customizable recipes:** Fine-tuning allows adapting the model to any dataset of ingredients and recipes.
* **Interactive experience:** Streamlit frontend enables real-time suggestions in a browser.
* **Scalable design:** The API can be extended or integrated into mobile or web applications.

