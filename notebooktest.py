import urllib.request, sys, os

dest_dir = "/databricks/driver/testing_usecase"
os.makedirs(dest_dir, exist_ok=True)

url = "https://raw.githubusercontent.com/nxumam/testing_usecase/main/mypackage.py"
urllib.request.urlretrieve(url, os.path.join(dest_dir, "mypackage.py"))

sys.path.append(dest_dir)
from mypackage import greet, add   # now resolves — mypackage.py is on the path

greet("Databricks")
