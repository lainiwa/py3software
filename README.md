
# This package fails to execute entrypoint
```sh
git clone https://github.com/lainiwa/py3software.git
cd py3software/py3software
dpkg-buildpackage --unsigned-source --unsigned-changes --build=binary
# Installs the package and then tries to execute the entrypoint
docker build -t test ..  # `RUN sayhello` fails
# ELF load command address/offset not properly aligned
```
