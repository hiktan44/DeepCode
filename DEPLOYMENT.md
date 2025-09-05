# DeepCode Streamlit Cloud Deployment Guide

## 🚀 Quick Deploy to Streamlit Cloud

### Prerequisites
1. GitHub account
2. Streamlit Cloud account (free at share.streamlit.io)
3. API keys (OpenAI, Anthropic)

### Deployment Steps

#### 1. Fork/Clone Repository
```bash
git clone https://github.com/HKUDS/DeepCode.git
cd DeepCode
```

#### 2. Push to Your GitHub
```bash
git remote set-url origin https://github.com/YOUR_USERNAME/DeepCode.git
git push origin main
```

#### 3. Deploy on Streamlit Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click "New app"
3. Connect your GitHub repository
4. Set main file: `streamlit_app.py`
5. Set Python version: 3.9+

#### 4. Configure Secrets
In Streamlit Cloud dashboard, add these secrets:

```toml
[openai]
api_key = "sk-your-openai-key"
base_url = ""

[anthropic]
api_key = "sk-ant-your-anthropic-key"
```

#### 5. Advanced Configuration (Optional)
- Use `requirements_cloud.txt` for lighter deployment
- Configure `packages.txt` for system dependencies
- Adjust `.streamlit/config.toml` for custom settings

### 🔧 Troubleshooting

**Memory Issues:**
- Comment out heavy dependencies in requirements
- Use lighter alternatives
- Enable resource optimization

**Build Failures:**
- Check Python version compatibility
- Verify all dependencies are available
- Use `packages.txt` for system packages

**API Issues:**
- Verify secrets are properly configured
- Check API key formats
- Test API connectivity

### 📊 Performance Tips
- Use caching with `@st.cache_data`
- Optimize imports
- Minimize heavy computations
- Use session state efficiently

## 🌐 Live Demo
Once deployed, your app will be available at:
`https://your-app-name.streamlit.app`