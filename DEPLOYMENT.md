# Deployment Guide - Free Hosting Options

## All Free Hosting Options

### **Platform-as-a-Service (PaaS) - Easiest**

#### Option 1: Render ⭐ (Recommended)

**Free Tier:** Available (with limitations)

### Steps:

1. **Sign up:** https://render.com

2. **Create PostgreSQL Database:**
   - New → PostgreSQL
   - Note connection details

3. **Create Web Service:**
   - New → Web Service
   - Connect GitHub repo
   - Settings:
     - **Build Command:** `pip install -r requirements.txt && python manage.py collectstatic --noinput`
     - **Start Command:** `gunicorn --bind 0.0.0.0:$PORT --workers 3 personalwebsite.wsgi:application`

4. **Environment Variables:**
   ```
   DEBUG=False
   SECRET_KEY=your-secret-key
   ALLOWED_HOSTS=your-app.onrender.com
   DB_ENGINE=django.db.backends.postgresql
   DB_NAME=<from database>
   DB_USER=<from database>
   DB_PASSWORD=<from database>
   DB_HOST=<from database>
   DB_PORT=5432
   ```

5. **Deploy & Migrate:**
   - Render auto-deploys
   - Run migrations via shell or dashboard

---

#### Option 2: Fly.io

**Free Tier:** 3 shared VMs

### Steps:

1. **Install Fly CLI:**
   ```bash
   curl -L https://fly.io/install.sh | sh
   ```

2. **Login:**
   ```bash
   fly auth login
   ```

3. **Initialize:**
   ```bash
   fly launch
   ```

4. **Add PostgreSQL:**
   ```bash
   fly postgres create
   fly postgres attach <db-name>
   ```

5. **Set Secrets:**
   ```bash
   fly secrets set SECRET_KEY=your-key DEBUG=False ALLOWED_HOSTS=your-app.fly.dev
   ```

6. **Deploy:**
   ```bash
   fly deploy
   ```

---

#### Option 3: PythonAnywhere

**Free Tier:** Limited (1 web app, 512MB storage)

**Pros:**
- Python-focused, Django-friendly
- Simple web interface
- Free tier available

**Cons:**
- Limited free tier
- No Docker support
- Manual setup required

**Setup:**
1. Sign up: https://www.pythonanywhere.com
2. Upload code via web interface or Git
3. Configure web app manually
4. Use their PostgreSQL add-on

---

#### Option 4: Heroku (Limited Free Tier)

**Free Tier:** Discontinued, but has low-cost options ($5-7/month)

**Pros:**
- Well-documented
- Easy deployment
- Add-ons marketplace

**Cons:**
- No longer free
- More expensive than alternatives

---

#### Option 5: DigitalOcean App Platform

**Free Tier:** $5 credit/month (usually enough)

**Pros:**
- Reliable infrastructure
- Good documentation
- Docker support

**Cons:**
- Credit expires monthly
- May need to pay after credit runs out

---

### **VPS/Cloud Providers - More Control**

#### Option 6: Oracle Cloud (Always Free)

**Free Tier:** 2 VMs with 1GB RAM each (permanent free tier!)

**Pros:**
- Truly free forever
- Full control
- Good for learning

**Cons:**
- Requires server management
- More setup work
- Need to configure everything yourself

**Setup:**
- Create Ubuntu VM
- Install Docker
- Deploy your app
- Configure nginx, SSL, etc.

---

#### Option 7: Google Cloud Run

**Free Tier:** 2 million requests/month

**Pros:**
- Pay-per-use pricing
- Serverless
- Auto-scaling

**Cons:**
- Can get expensive with traffic
- More complex setup

---

#### Option 8: AWS Free Tier

**Free Tier:** EC2 t2.micro (12 months), RDS (12 months)

**Pros:**
- Industry standard
- Many services
- Good for learning AWS

**Cons:**
- Complex setup
- Free tier expires after 12 months
- Can get expensive if you exceed limits

---

#### Option 9: Azure App Service

**Free Tier:** Limited free tier available

**Pros:**
- Microsoft ecosystem
- Good integration
- Docker support

**Cons:**
- More complex than PaaS
- Free tier limitations

---

### **Static + API Split Approach**

#### Option 10: Vercel/Netlify (Frontend) + Backend API

**Free Tier:** Generous free tiers

**Approach:**
- Deploy Django as API only
- Use Vercel/Netlify for frontend
- Connect via API calls

**Pros:**
- Excellent free tiers
- Fast CDN
- Easy deployment

**Cons:**
- Need to restructure app
- More complex architecture

---

## Comparison Table

| Platform | Free Tier | Docker | Ease | Best For |
|----------|-----------|--------|------|----------|
| **Render** | Limited free | ✅ | ⭐⭐⭐⭐⭐ | Simple setup |
| **Fly.io** | 3 shared VMs | ✅ | ⭐⭐⭐ | Docker apps |
| **PythonAnywhere** | Limited | ❌ | ⭐⭐⭐ | Python-focused |
| **Oracle Cloud** | Always free VMs | ✅ | ⭐⭐ | Learning/Control |
| **Google Cloud Run** | 2M requests | ✅ | ⭐⭐⭐ | Serverless |
| **DigitalOcean** | $5 credit | ✅ | ⭐⭐⭐⭐ | Reliability |

---

## Important Notes:

- **Media Files:** For free tiers, consider using cloud storage (AWS S3, Cloudinary) for uploaded images
- **Static Files:** Already configured with WhiteNoise
- **Domain:** Free tiers usually provide subdomains (e.g., `yourapp.onrender.com`)
- **SSL:** Automatically handled by platforms

## Generate Secret Key:

```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

