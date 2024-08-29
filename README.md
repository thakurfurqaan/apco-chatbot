
## Run locally
1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Unix or MacOS: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
6. Run the application: `uvicorn app.main:app --reload`



### NOTES:
- I committed the `.env` file to git only for ease of setup at your end.
- You can find the question in the `question` directory.
