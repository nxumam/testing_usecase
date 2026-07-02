import sys
sys.path.append("/databricks/driver/testing_usecase")  # or wherever it cloned

from mypackage import greet, add
greet("Databricks")   # 'Hello, Databricks!'
