
## Try it out
- Go to [APCO Chatbot Demo](https://tinyurl.com/apco-furqaan) to try out the chatbot.

## Run locally
1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Unix or MacOS: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
6. Run the application: `fastapi dev app/main.py` or `uvicorn app.main:app --reload`


### NOTES:
- You can find the question in the `question.py` file.
- I have committed ChromaDB vector store to git for ease of setup at your end.