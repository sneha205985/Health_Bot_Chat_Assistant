# 🚀 Deployment Guide - Update Your Streamlit App

## Step 1: Find Your GitHub Repository

Since you already have a deployed app at `https://healthbot-chat-assistant-tg.streamlit.app`, you must have a GitHub repository connected to it.

**Option A: Check Streamlit Cloud**
1. Go to [Streamlit Cloud](https://share.streamlit.io/)
2. Sign in and find your app
3. Click on your app → Settings
4. You'll see the GitHub repository URL there

**Option B: Check Your GitHub**
1. Go to [GitHub.com](https://github.com)
2. Look for a repository named something like:
   - `HealthBot-chatassistant`
   - `healthbot-chat-assistant`
   - `HealthBot`
   - Or similar

## Step 2: Connect Local Repository to GitHub

Once you have your GitHub repository URL (it will look like: `https://github.com/yourusername/repo-name.git`), run:

```bash
cd /Users/snehagupta/Desktop/Health
git remote add origin https://github.com/yourusername/your-repo-name.git
```

Replace `yourusername` and `your-repo-name` with your actual GitHub username and repository name.

## Step 3: Push Your Updated Code

```bash
# Push to main branch (or master if that's what your repo uses)
git push -u origin main

# If your default branch is 'master', use:
# git push -u origin master
```

## Step 4: Update API Key in Streamlit Cloud

1. Go to [Streamlit Cloud](https://share.streamlit.io/)
2. Click on your app
3. Go to **Settings** → **Secrets**
4. Add or update the secret:
   ```
   GEMINI_API_KEY=AIzaSyDdWhrqF21dwf7BWddKewqFoE6IJRuO_YM
   ```
   (Or use `GOOGLE_API_KEY` if you prefer)

## Step 5: Automatic Deployment

Streamlit Cloud will automatically detect the push and redeploy your app with the new code. This usually takes 1-2 minutes.

## Alternative: If You Don't Have a GitHub Repo Yet

If you need to create a new repository:

1. Go to GitHub and create a new repository
2. Don't initialize it with README (since we already have files)
3. Copy the repository URL
4. Run the commands in Step 2 and Step 3 above

## Troubleshooting

- **If push is rejected**: You might need to pull first: `git pull origin main --allow-unrelated-histories`
- **If branch name differs**: Check your repo's default branch name (main vs master)
- **If API key doesn't work**: Make sure it's set correctly in Streamlit Cloud Secrets

