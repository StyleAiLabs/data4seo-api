#!/bin/bash

echo "🚀 Deploying AI Visibility Monitor to Render..."
echo "=================================================="

# Check if we're in a git repository
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    echo "❌ Not in a git repository. Initializing..."
    git init
    git add .
    git commit -m "Initial commit: AI Visibility Monitor API"
fi

# Check for uncommitted changes
if ! git diff-index --quiet HEAD --; then
    echo "📝 Committing changes..."
    git add .
    git commit -m "Add API service for Render deployment"
fi

# Check if remote exists
if ! git remote get-url origin > /dev/null 2>&1; then
    echo "❌ No git remote 'origin' found."
    echo "Please add your GitHub repository:"
    echo "git remote add origin https://github.com/yourusername/your-repo.git"
    echo "git push -u origin main"
    exit 1
fi

# Push to GitHub
echo "📤 Pushing to GitHub..."
git push origin main

echo ""
echo "✅ Code pushed to GitHub!"
echo ""
echo "🎯 Next Steps for Render Deployment:"
echo "====================================="
echo "1. Go to https://render.com"
echo "2. Click 'New Web Service'"
echo "3. Connect your GitHub repository"
echo "4. Render will auto-detect render.yaml"
echo "5. Set environment variables:"
echo "   - DATAFORSEO_LOGIN=your_login"
echo "   - DATAFORSEO_PASSWORD=your_password"
echo "6. Click 'Create Web Service'"
echo ""
echo "📚 API Documentation: /API_DEPLOYMENT.md"
echo "🔗 Interactive Docs: https://your-service.onrender.com/docs"
echo ""
echo "🎉 Your API will be available at: https://your-service-name.onrender.com"
