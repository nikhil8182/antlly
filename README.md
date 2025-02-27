# Antlly.ai

A digital companion web application built with Flask.

## Deployment on Render

This application is configured for deployment on Render.

### Setup Instructions

1. Create a new Web Service on Render
2. Connect your GitHub repository
3. Use the following settings:
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Plan**: Free or Standard

### Environment Variables

No special environment variables are needed for basic deployment.

## Local Development

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `python app.py`
4. Visit http://localhost:5000 in your browser