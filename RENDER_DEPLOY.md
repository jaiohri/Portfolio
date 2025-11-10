# Deploy to Render - Step by Step Guide

## Prerequisites
- GitHub account
- Code pushed to GitHub repository
- Render account (sign up at https://render.com)

## Quick Setup with render.yaml (Recommended)

**Option 1: Use render.yaml (Easiest - Enables PR Previews & Auto-Deploy)**

1. **Push `render.yaml` to your repository** (already included in repo)
2. **Go to Render Dashboard:** https://dashboard.render.com
3. **Click "New +"** → **"Blueprint"**
4. **Connect your GitHub repository**
5. **Render will detect `render.yaml` automatically**
6. **Review configuration and click "Apply"**
7. **Render creates both database and web service automatically**
8. **Update environment variables:**
   - Go to Web Service → Environment
   - Set `SECRET_KEY` (generate a new one!)
   - Update `ALLOWED_HOSTS` with your actual service URL
9. **Deploy and run migrations** (see Step 6 below)

**Benefits:**
- ✅ PR Previews (test changes before merging)
- ✅ Auto-deploy on every push
- ✅ Infrastructure as code
- ✅ Automatic database linking

---

## Manual Setup (Alternative)

---

## Step 1: Create PostgreSQL Database

1. **Go to Render Dashboard:** https://dashboard.render.com
2. **Click "New +"** → **"PostgreSQL"**
3. **Configure Database:**
   - **Name:** `personalwebsite-db` (or any name you prefer)
   - **Database:** `personalwebsite`
   - **User:** `personalwebsite` (or leave default)
   - **Region:** Choose closest to you
   - **PostgreSQL Version:** 15 (or latest)
   - **Plan:** Free (or paid if you prefer)
4. **Click "Create Database"**
5. **Wait for database to be ready** (takes 1-2 minutes)
6. **Copy these values** (you'll need them later):
   - Internal Database URL (or individual values)
   - Host
   - Port
   - Database name
   - User
   - Password

---

## Step 2: Create Web Service

1. **In Render Dashboard, click "New +"** → **"Web Service"**
2. **Connect Repository:**
   - Click "Connect account" if not connected
   - Select your GitHub account
   - Choose your repository: `PersonalWebsite` (or your repo name)
   - Click "Connect"

3. **Configure Service:**
   - **Name:** `personalwebsite` (or your preferred name)
   - **Region:** Same as database
   - **Branch:** `main` (or your default branch)
   - **Root Directory:** Leave empty (or `.` if needed)
   - **Runtime:** `Python 3`
   - **Build Command:**
     ```
     pip install -r requirements.txt && python manage.py collectstatic --noinput
     ```
   - **Start Command:**
     ```
     gunicorn --bind 0.0.0.0:$PORT --workers 3 personalwebsite.wsgi:application
     ```
   - **Plan:** Free (or paid)

4. **Click "Advanced"** to add environment variables

---

## Step 3: Set Environment Variables

In the Web Service settings, add these environment variables:

### Required Variables:

```
DEBUG=False
```

```
SECRET_KEY=<generate-a-new-secret-key>
```
**To generate:** Run this in Python:
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

```
ALLOWED_HOSTS=your-app-name.onrender.com
```
*(Replace `your-app-name` with your actual service name)*

### Database Variables:

Get these from your PostgreSQL database service:

```
DB_ENGINE=django.db.backends.postgresql
```

```
DB_NAME=personalwebsite
```
*(From your database settings)*

```
DB_USER=personalwebsite
```
*(From your database settings)*

```
DB_PASSWORD=<your-database-password>
```
*(From your database settings - click "Show" to reveal)*

```
DB_HOST=<your-database-host>
```
*(From your database settings - looks like: `dpg-xxxxx-a.oregon-postgres.render.com`)*

```
DB_PORT=5432
```
*(Usually 5432 for PostgreSQL)*

---

## Step 4: Link Database to Web Service

1. **In your Web Service settings**
2. **Scroll to "Connections" section**
3. **Click "Link Database"**
4. **Select your PostgreSQL database**
5. **Render will automatically add database environment variables** (you can still add them manually if needed)

---

## Step 5: Deploy

1. **Click "Create Web Service"** at the bottom
2. **Render will start building** (takes 3-5 minutes)
3. **Watch the build logs** to see progress
4. **Wait for "Your service is live"** message

---

## Step 6: Run Migrations

After deployment:

### Option A: Using Render Shell
1. **Go to your Web Service**
2. **Click "Shell" tab**
3. **Run:**
   ```bash
   python manage.py migrate
   ```

### Option B: Using Render CLI
1. **Install Render CLI:**
   ```bash
   npm install -g render-cli
   ```
2. **Login:**
   ```bash
   render login
   ```
3. **Run migrations:**
   ```bash
   render exec -s <your-service-name> -- python manage.py migrate
   ```

---

## Step 7: Create Admin User

1. **Open Render Shell** (from Step 6)
2. **Run:**
   ```bash
   python manage.py createsuperuser
   ```
3. **Follow prompts** to create admin account
4. **Note:** The `createsuperuser` command is blocked in your code, so you'll need to create the user via Django shell:
   ```python
   python manage.py shell
   ```
   Then:
   ```python
   from django.contrib.auth.models import User
   User.objects.create_superuser('admin', 'admin@example.com', 'your-password')
   ```

---

## Step 8: Access Your Site

1. **Your site URL:** `https://your-app-name.onrender.com`
2. **Admin Panel:** `https://your-app-name.onrender.com/admin`
3. **Test the site** to make sure everything works

---

## Troubleshooting

### Build Fails
- Check build logs for errors
- Ensure `requirements.txt` has all dependencies
- Verify Python version compatibility

### Database Connection Issues
- Double-check all database environment variables
- Ensure database is in same region as web service
- Verify database is "Available" (not paused)

### Static Files Not Loading
- Check that `collectstatic` ran successfully in build logs
- Verify WhiteNoise is in `MIDDLEWARE`
- Check `STATIC_ROOT` is set correctly

### 502 Bad Gateway
- Check service logs
- Verify `gunicorn` start command is correct
- Ensure `$PORT` environment variable is used (Render provides this)

### Media Files Not Working
- Free tier has limited storage
- Consider using cloud storage (AWS S3, Cloudinary) for production
- Media files are stored in `media/` folder (may be ephemeral on free tier)

---

## Important Notes

- **Free Tier Limitations:**
  - Service spins down after 15 minutes of inactivity
  - First request after spin-down takes ~30 seconds
  - 750 hours/month free (usually enough)
  - Limited storage for media files

- **Custom Domain:**
  - Free tier supports custom domains
  - Add domain in service settings → "Custom Domains"
  - Update `ALLOWED_HOSTS` to include your domain

- **Auto-Deploy:**
  - Render auto-deploys on every push to your branch
  - You can disable this in service settings

---

## Next Steps

1. ✅ Test all functionality
2. ✅ Set up custom domain (optional)
3. ✅ Configure media file storage (AWS S3 recommended)
4. ✅ Set up monitoring/alerts (optional)
5. ✅ Backup database regularly

---

## Quick Reference

**Your URLs:**
- Website: `https://your-app-name.onrender.com`
- Admin: `https://your-app-name.onrender.com/admin`
- API: `https://your-app-name.onrender.com/api/` (if you add API endpoints)

**Useful Commands:**
```bash
# View logs
# (In Render dashboard → Service → Logs)

# Run migrations
python manage.py migrate

# Create superuser (via shell)
python manage.py shell
# Then: User.objects.create_superuser('admin', 'email', 'password')

# Check service status
# (In Render dashboard)
```

