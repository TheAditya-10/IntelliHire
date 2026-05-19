# Render Deployment Guide (IntelliHire)

## 1) Prepare Neon PostgreSQL

1. Create a new project in Neon.
2. Create a database (or use the default database).
3. Copy the connection string (DATABASE_URL).
4. Keep SSL enabled. Neon URLs already include `sslmode=require`.

## 2) Connect GitHub Repo in Render

1. Go to Render Dashboard and click "New" -> "Web Service".
2. Connect your GitHub account and select the IntelliHire repository.
3. Choose the `master` branch (or your deployment branch).
4. Select the "Free" plan.

## 3) Configure Build and Start

Render uses these settings from render.yaml:

- Build command:
  - `pip install --upgrade pip`
  - `pip install -r requirements.txt`
- Start command:
  - `gunicorn app:app`

## 4) Set Environment Variables in Render

Add these environment variables in Render -> Service -> Environment:

- `DATABASE_URL` = Neon PostgreSQL connection string
- `GOOGLE_API_KEY` = your Gemini API key
- `SECRET_KEY` = a long random string

Optional (already defined in render.yaml):

- `FLASK_ENV` = `production`
- `FLASK_APP` = `app.py`
- `PYTHON_VERSION` = `3.12.3`

## 5) Deploy

1. Click "Deploy" in Render.
2. Wait for the build to finish and the service to start.
3. Open the public URL shown in the Render dashboard.

## 6) Check Logs

- Render -> Service -> Logs
- Look for startup errors or missing environment variables.

## 7) Common Issues and Fixes

- **Python version mismatch**: Make sure Render shows Python 3.12.3 in logs.
- **Missing DATABASE_URL**: Set it in Render and redeploy.
- **pydantic_core build failures**: Usually caused by Python 3.14+ without wheels.
- **Static files not loading**: Verify `static/` is in the repo and paths are correct.
- **Secret key errors**: Ensure `SECRET_KEY` is set in Render.
