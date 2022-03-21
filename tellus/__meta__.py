# `name` is the name of the package as used for `pip install package`
name = "tellus"
# `path` is the name of the package for `import package`
path = name.lower().replace("-", "_").replace(" ", "_")
# Your version number should follow https://python.org/dev/peps/pep-0440 and
# https://semver.org
version = "0.1.dev0"
author = "Kota Yuhara"
author_email = "hotwater1367@gmail.com"
description = "Python client for Tellus API"  # One-liner
url = "https://github.com/wakame1367/tellus_client"  # your project homepage
license = "MIT"  # See https://choosealicense.com
