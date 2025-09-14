from fastapi import FastAPI, Request
from app.github import fetch_pr_diff, post_comment
from app.review import generate_review

app = FastAPI()

@app.post("/webhook")
async def github_webhook(request: Request):
    payload = await request.json()

    if "pull_request" in payload:
        pr = payload["pull_request"]
        repo = payload["repository"]["full_name"]
        pr_number = pr["number"]

        # Fetch PR diff
        diff = await fetch_pr_diff(repo, pr_number)

        # Generate AI review
        review = await generate_review(diff)

        # Post review as comment
        await post_comment(repo, pr_number, review)

    return {"status": "ok"}
