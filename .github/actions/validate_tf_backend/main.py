

import hcl2
import os

# ./project1/app1/main.tf

state_bucket = os.environ.get("STATE_BUCKET")
path = os.environ.get("FILE_PATH")
# state_bucket = "tf-state-prod"
# path = "./project1/app1/main.tf"


print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(state_bucket)
print(path)
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

# with open(path, 'r') as f:
#     dict = hcl2.load(f)

#     # Normalize the path
#     base = os.path.dirname(path)
#     base = base.removeprefix('./')

#     prefix = dict['terraform'][0]['backend'][0]['gcs']['prefix']
#     prefix = prefix.removeprefix('/')
#     prefix = prefix.removesuffix('/')

#     if base == prefix:
#         print("Prefix is correct")

#     if state_bucket == dict['terraform'][0]['backend'][0]['gcs']['bucket']:
#         print("Bucket name is correct")

