#!/bin/bash

echo "🤖 RankAled Phase 1: AI Visibility Monitor Setup"
echo "=============================================="

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Make scripts executable
chmod +x ai_visibility_monitor.py
chmod +x quick_test.py

echo "✅ Setup complete!"
echo ""
echo "📋 Next steps:"
echo "1. Set your DataForSEO credentials (choose one method):"
echo ""
echo "   Method A - Environment variables:"
echo "   export DATAFORSEO_LOGIN='your_login'"
echo "   export DATAFORSEO_PASSWORD='your_password'"
echo ""
echo "   Method B - Edit .env file:"
echo "   nano .env"
echo "   (Replace 'your_actual_login' and 'your_actual_password' with real credentials)"
echo ""
echo "2. Test connection:"
echo "   python3 quick_test.py"
echo ""
echo "3. Run AI visibility analysis:"
echo "   python3 ai_visibility_monitor.py"
