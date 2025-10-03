from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

# Allow CORS so Flutter web can call the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # in production, replace with your Flutter web URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Backend is running"}

@app.post("/summarize")
async def summarize(request: Request):
    data = await request.json()
    text = data.get("text", "")

    # Simple dummy summary for now (replace with real LLM later)
    if not text.strip():
        return {"summary": "No text provided to summarize."}

    summary = text[:150] + "..." if len(text) > 150 else text
    return {"summary": summary}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
