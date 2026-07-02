import urllib.request, sys, os

dbutils.widgets.text("git_base_url",
    "https://raw.githubusercontent.com/nxumam/testing_usecase/main",
    "Raw GitHub base URL")
dbutils.widgets.text("files", "mypackage.py", "comma-separated files to pull")
dbutils.widgets.text("dest_dir", "/databricks/driver/testing_usecase", "Driver dest dir")

# --- Read widget values ---
git_base_url = dbutils.widgets.get("git_base_url").rstrip("/")
dest_dir     = dbutils.widgets.get("dest_dir")
files        = [f.strip() for f in dbutils.widgets.get("files").split(",") if f.strip()]

# --- Download each file from the git URL ---
os.makedirs(dest_dir, exist_ok=True)
for rel_path in files:
    url        = f"{git_base_url}/{rel_path}"
    local_path = os.path.join(dest_dir, rel_path)
    os.makedirs(os.path.dirname(local_path), exist_ok=True)   # handle nested paths
    urllib.request.urlretrieve(url, local_path)
    print(f"downloaded {rel_path} -> {local_path}")

# --- Make the files importable ---
sys.path.append(dest_dir)
from mypackage import greet, add   # now resolves — mypackage.py is on the path

greet("Databricks")
