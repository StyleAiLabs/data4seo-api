# 📄 Scripts

This folder contains deployment and setup scripts for the AI Visibility Monitor API.

## 📂 **Contents**

### **🚀 Deployment Scripts**
- `deploy.sh` - Main deployment script for production
- `deploy_fast_api.sh` - Fast API specific deployment (legacy)
- `build.sh` - Build script for the application

### **⚙️ Setup Scripts**
- `setup.sh` - Environment setup and dependency installation

## 🎯 **Usage**

### **Setup Development Environment**
```bash
./scripts/setup.sh
```

### **Deploy to Production**
```bash
./scripts/deploy.sh
```

### **Build Application**
```bash
./scripts/build.sh
```

## 🔧 **Script Details**

| Script | Purpose | When to Use |
|--------|---------|-------------|
| `setup.sh` | Install dependencies, configure environment | Development setup |
| `build.sh` | Build and prepare application | Before deployment |
| `deploy.sh` | Deploy to production (Render) | Production deployment |
| `deploy_fast_api.sh` | Legacy fast API deployment | Deprecated |

## ⚠️ **Prerequisites**

- Python 3.8+
- pip/poetry for dependency management
- Git for version control
- DataForSEO API credentials (in .env file)

## 🔒 **Security Note**

Ensure `.env` file is properly configured with your DataForSEO credentials before running deployment scripts.
