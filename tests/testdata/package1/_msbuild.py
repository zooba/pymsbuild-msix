from pymsbuild import *
from pymsbuild.entrypoint import Entrypoint
from pymsbuild_msix import *

METADATA = {
    "Name": "package1",
    "Version": "1.0",
}

PACKAGE = Package(
    "test-package1",
    AppxManifest("appxmanifest.xml"),
    ResourcesXml("resources.xml"),
    File("logo44.png"),
    File("logo150.png"),
    Entrypoint("package1", "main", "main"),
)
