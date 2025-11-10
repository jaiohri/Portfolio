# Render PostgreSQL Setup - Step by Step

## Step 1: Create PostgreSQL Database

1. **Go to Render Dashboard:** https://dashboard.render.com
2. **Click "New +"** (top right corner)
3. **Select "PostgreSQL"** from the dropdown menu
4. **Fill in the database details:**
   - **Name:** `personalwebsite-db` (or any name you prefer)
   - **Database:** `personalwebsite` (or leave default)
   - **User:** `personalwebsite` (or leave default)
   - **Region:** Choose the same region as your web service (important for performance)
   - **PostgreSQL Version:** 15 (or latest available)
   - **Plan:** Free (or paid if you prefer)
5. **Click "Create Database"**
6. **Wait 1-2 minutes** for the database to be provisioned

---

## Step 2: Get Database Connection Details

Once the database is created:

1. **Click on your database** (`personalwebsite-db`) in the dashboard
2. **Scroll to "Connections" section**
3. **Copy these values** (you'll need them):
   - **Internal Database URL** (looks like: `postgres://user:password@host:port/dbname`)
   - **Host** (looks like: `dpg-xxxxx-a.oregon-postgres.render.com`)
   - **Port** (usually `5432`)
   - **Database name** (usually `personalwebsite`)
   - **User** (usually `personalwebsite`)
   - **Password** (click "Show" to reveal)

**Note:** Keep these safe! You'll need them if you want to connect manually.

---

## Step 3: Link Database to Web Service

**Option A: Using DATABASE_URL (Easiest - Recommended)**

1. **Go to your PostgreSQL Database** (`personalwebsite-db`) in the dashboard
2. **Find the "Connections" section** on the database page
3. **Copy the "Internal Database URL"** (looks like: `postgres://user:password@host:port/dbname`)
4. **Go to your Web Service** (`personalwebsite`) in the dashboard
5. **Click on the "Environment" tab**
6. **Click "Add Environment Variable"**
7. **Add:**
   - **Key:** `DATABASE_URL`
   - **Value:** Paste the Internal Database URL you copied
8. **Click "Save Changes"**
9. **Render will automatically redeploy** your service

**Option B: Using Individual Environment Variables**

If you can't find the Internal Database URL, use individual variables:

1. **From your Database service**, note these values:
   - **Host** (e.g., `dpg-xxxxx-a.oregon-postgres.render.com`)
   - **Port** (usually `5432`)
   - **Database name** (usually `personalwebsite`)
   - **User** (usually `personalwebsite`)
   - **Password** (click "Show" to reveal)

2. **Go to your Web Service** → **Environment** tab
3. **Add these environment variables:**

   ```
   DB_ENGINE=django.db.backends.postgresql
   DB_NAME=personalwebsite
   DB_USER=personalwebsite
   DB_PASSWORD=<your-database-password>
   DB_HOST=<your-database-host>
   DB_PORT=5432
   ```

   *(Replace `<your-database-password>` and `<your-database-host>` with actual values)*

4. **Click "Save Changes"** and redeploy

**Option C: Automatic Linking via Dashboard (If available)**

Some Render dashboards have a "Connections" section in the web service:

1. **Go to your Web Service** (`personalwebsite`) in the dashboard
2. **Scroll down to "Connections" section** (if visible)
3. **Click "Link Database"** or "Add Database"
4. **Select** `personalwebsite-db` from the dropdown
5. **Click "Link"**
6. **Render automatically sets `DATABASE_URL`** - no manual configuration needed!

---

## Step 4: Verify Database Connection

1. **Go to your Web Service** → **Logs** tab
2. **Check for any database connection errors**
3. **If you see connection errors**, verify:
   - Database is running (status should be "Available")
   - Database is linked to web service
   - Environment variables are set correctly

---

## Step 5: Run Database Migrations

After the database is linked and your app is deployed:

1. **Go to your Web Service** → **Shell** tab (or use Render Shell)
2. **Run migrations:**
   ```bash
   python manage.py migrate
   ```
3. **Create admin user (if needed):**
   ```bash
   python manage.py createsuperuser
   ```
   *(Note: Your custom command blocks this - you'll need to create admin via Django admin panel or another method)*

---

## Troubleshooting

### Database Connection Refused
- **Check:** Database is running and status is "Available"
- **Check:** Database is linked to web service
- **Check:** `DATABASE_URL` is set in environment variables

### DATABASE_URL Not Set
- **Solution:** Manually link database in "Connections" section
- **Alternative:** Add database connection variables manually (see Option B above)

### Migration Errors
- **Check:** Database is accessible
- **Check:** User has proper permissions
- **Run:** `python manage.py migrate` in Render Shell

---

## Quick Checklist

- [ ] PostgreSQL database created
- [ ] Database is running (status: "Available")
- [ ] Database linked to web service
- [ ] `DATABASE_URL` appears in environment variables (or manual DB_* vars set)
- [ ] Web service redeployed after linking
- [ ] Migrations run successfully
- [ ] No connection errors in logs

---

## Next Steps

After database is set up:
1. Run migrations: `python manage.py migrate`
2. Create initial data (if needed)
3. Test your application
4. Set up admin user (via Django admin or custom method)

