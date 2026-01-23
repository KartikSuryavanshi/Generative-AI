# sqlite-gemini-assistant

Streamlit app that turns natural language questions into SQL for a local SQLite database, using Google Gemini.

## Quick start

1) Clone and enter the project
```
git clone https://github.com/KartikSuryavanshi/sqlite-gemini-assistant.git
cd sqlite-gemini-assistant
```
2) Create and activate a venv (optional but recommended)
```
python3 -m venv .venv
source .venv/bin/activate
```
3) Install dependencies
```
pip install -r requirements.txt
```
4) Set your API key in .env
```
GOOGLE_API_KEY="your-key"
```
5) Seed the SQLite database (creates students.db)
```
python sqlite.py
```
6) Run the app
```
streamlit run sql.py
```
The app will start at http://localhost:8502.

## How it works
- `sql.py` loads your question, asks Gemini to produce SQL, executes it against `students.db`, and shows the rows.
- `sqlite.py` creates the `STUDENT` table and inserts sample data.

## Sample questions to try
- "How many entries of records are present?"
- "Tell me all the students studying in DS class"
- "Show me students in section A"

## Notes
- Gemini free tier has strict quotas; enable billing if you see 429 quota errors.
- Keep `.env` and `students.db` out of Git (already in `.gitignore`).