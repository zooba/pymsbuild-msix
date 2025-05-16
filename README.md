# pymsbuild-msix

This is a [pymsbuild](https://pypi.org/project/pymsbuild) extension for
compiling packages to MSIX.

# Quick Start

In your `_msbuild.py`, import `AppxManifest` from `pymsbuild_msix` (using
`import *` is okay, and there are more names you may need).


```python
from pymsbuild import *
from pymsbuild_msix import *

METADATA = {...}

PACKAGE = Package(
    'package',
    PyFile("__init__.py"),
    AppxManifest("appxmanifest.xml"),
)
```

The extension adds a new `msix` command to build the MSIX. It behaves like the
`wheel` and `sdist` commands, including with the `--layout-dir` option followed
by the `pack` command.

```powershell
$> python -m pymsbuild msix

# Or

$> python -m pymsbuild msix --layout-dir $DIR
# Modify (e.g. sign) the files in $DIR
$> python -m pymsbuild pack --layout-dir $DIR --add @additional_files.txt
```

Additional types that can be used in the package definition include
`ResourcesXml`, to identify a file to run with `makepri.exe` as part of build,
and `AppInstaller`. The latter currently does nothing special.
