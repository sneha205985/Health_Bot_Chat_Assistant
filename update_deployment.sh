#!/bin/bash

# Script to update your Streamlit Cloud deployment
# Usage: ./update_deployment.sh YOUR_GITHUB_REPO_URL

echo "🚀 HealthBot Deployment Update Script"
echo "======================================"
echo ""

if [ -z "$1" ]; then
    echo "❌ Error: Please provide your GitHub repository URL"
    echo ""
    echo "Usage: ./update_deployment.sh https://github.com/yourusername/repo-name.git"
    echo ""
    echo "To find your GitHub repo:"
    echo "1. Go to https://share.streamlit.io/"
    echo "2. Sign in and click on your app"
    echo "3. Go to Settings → you'll see the GitHub repository URL"
    echo ""
    exit 1
fi

REPO_URL=$1

echo "📦 Step 1: Adding remote repository..."
git remote remove origin 2>/dev/null
git remote add origin $REPO_URL

echo "✅ Remote added: $REPO_URL"
echo ""

echo "📤 Step 2: Pushing code to GitHub..."
echo "This will update your Streamlit Cloud deployment automatically."
echo ""

# Try to push to main first, if that fails try master
if git push -u origin main 2>/dev/null; then
    echo "✅ Successfully pushed to 'main' branch!"
elif git push -u origin master 2>/dev/null; then
    echo "✅ Successfully pushed to 'master' branch!"
else
    echo "⚠️  Push failed. You may need to:"
    echo "   1. Pull existing code first: git pull origin main --allow-unrelated-histories"
    echo "   2. Or check if you have the correct permissions"
    echo "   3. Or verify the repository URL is correct"
    exit 1
fi

echo ""
echo "🎉 Code pushed successfully!"
echo ""
echo "📋 Next Steps:"
echo "1. Go to https://share.streamlit.io/ and check your app"
echo "2. Streamlit will automatically redeploy (takes 1-2 minutes)"
echo "3. Make sure your API key is set in Streamlit Cloud Secrets:"
echo "   - Go to your app → Settings → Secrets"
echo "   - Add: GEMINI_API_KEY=AIzaSyDdWhrqF21dwf7BWddKewqFoE6IJRuO_YM"
echo ""
echo "✨ Your app will be updated at: https://healthbot-chat-assistant-tg.streamlit.app"

