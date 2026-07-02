import urllib.request, sys, os

# ============================================================
# STEP 1: Define widgets
# ============================================================
try:
    dbutils.widgets.text("git_base_url",
        "https://raw.githubusercontent.com/nxumam/testing_usecase/main",
        "Raw GitHub base URL")
    dbutils.widgets.text("files", "mypackage.py", "comma-separated files to pull")
    dbutils.widgets.text("dest_dir", "/databricks/driver/testing_usecase", "Driver dest dir")
    print("✅ STEP 1: widgets defined")
except Exception as e:
    print(f"❌ STEP 1 FAILED: could not define widgets -> {e}")
    raise

# ============================================================
# STEP 2: Read widget values
# ============================================================
try:
    git_base_url = dbutils.widgets.get("git_base_url").rstrip("/")
    dest_dir     = dbutils.widgets.get("dest_dir")
    files        = [f.strip() for f in dbutils.widgets.get("files").split(",") if f.strip()]
    assert files, "no files listed in the 'files' widget"
    print(f"✅ STEP 2: read widgets — base_url={git_base_url}, dest_dir={dest_dir}, files={files}")
except Exception as e:
    print(f"❌ STEP 2 FAILED: could not read widget values -> {e}")
    raise

# ============================================================
# STEP 3: Download each file from the git URL
# ============================================================
try:
    os.makedirs(dest_dir, exist_ok=True)
    for rel_path in files:
        url        = f"{git_base_url}/{rel_path}"
        local_path = os.path.join(dest_dir, rel_path)
        os.makedirs(os.path.dirname(local_path), exist_ok=True)   # handle nested paths
        urllib.request.urlretrieve(url, local_path)
        print(f"   downloaded {rel_path} -> {local_path}")
    print("✅ STEP 3: all files downloaded")
except Exception as e:
    print(f"❌ STEP 3 FAILED: download error -> {e}")
    raise

# ============================================================
# STEP 4: Make files importable and import
# ============================================================
try:
    if dest_dir not in sys.path:
        sys.path.append(dest_dir)
    from mypackage import greet, add
    print("✅ STEP 4: mypackage imported successfully")
except Exception as e:
    print(f"❌ STEP 4 FAILED: import error -> {e}")
    raise

# ============================================================
# STEP 5: Run and verify the code works
# ============================================================
try:
    greet("Databricks")
    print("✅ STEP 5: code ran successfully — job confirmed working")
except Exception as e:
    print(f"❌ STEP 5 FAILED: execution error -> {e}")
    raise
