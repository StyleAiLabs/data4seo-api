#!/bin/bash
"""
Fast API Deployment Script
Deploys the optimized AI Visibility API for SaaS integration
"""

echo "🚀 Deploying Fast AI Visibility API for SaaS Integration"
echo "=================================================="

# Check if running in correct directory
if [ ! -f "fast_api_service.py" ]; then
    echo "❌ Error: fast_api_service.py not found"
    echo "Please run this script from the project root directory"
    exit 1
fi

# Check Python environment
if [ ! -d ".venv" ]; then
    echo "🔧 Setting up Python virtual environment..."
    python3 -m venv .venv
fi

# Activate virtual environment
source .venv/bin/activate

# Install dependencies
echo "📦 Installing dependencies..."
pip install fastapi uvicorn requests aiohttp python-multipart

# Check environment variables
echo "🔑 Checking environment configuration..."
if [ -z "$DATAFORSEO_LOGIN" ] || [ -z "$DATAFORSEO_PASSWORD" ]; then
    echo "⚠️  Warning: DataForSEO credentials not found in environment"
    echo "Make sure to set DATAFORSEO_LOGIN and DATAFORSEO_PASSWORD"
    
    if [ -f ".env" ]; then
        echo "✅ Found .env file - credentials will be loaded from file"
    else
        echo "❌ No .env file found"
        echo "Create .env file with:"
        echo "DATAFORSEO_LOGIN=your_login"
        echo "DATAFORSEO_PASSWORD=your_password"
    fi
fi

# Set port
PORT=${PORT:-8001}
echo "🌐 API will run on port $PORT"

# Start the fast API service
echo "🚀 Starting Fast AI Visibility API..."
echo "📍 Endpoints available at:"
echo "   - Health Check: http://localhost:$PORT/health"
echo "   - API Docs: http://localhost:$PORT/docs"
echo "   - Onboarding Analysis: http://localhost:$PORT/api/v2/onboarding-analysis"
echo "   - Fast Analysis: http://localhost:$PORT/api/v2/fast-analysis"
echo ""
echo "⚡ Performance Targets:"
echo "   - Onboarding Analysis: < 30 seconds"
echo "   - Fast Analysis: < 45 seconds"
echo "   - 79x faster than standard analysis"
echo ""
echo "🎯 Perfect for SaaS user onboarding flows!"
echo ""

# Start the service
python fast_api_service.py
