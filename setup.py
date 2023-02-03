import os
import sys
from glob import glob
from setuptools import setup, Extension

PACKAGE_NAME = "pysqlite3-wheels"
VERSION = "0.5.0"


def quote_argument(arg):
    is_cibuildwheel = os.environ.get("CIBUILDWHEEL", "0") == "1"

    if sys.platform == "win32" and (
        (is_cibuildwheel and sys.version_info < (3, 7))
        or (not is_cibuildwheel and sys.version_info < (3, 9))
    ):
        q = '\\"'
    else:
        q = '"'

    return q + arg + q


sources = glob("src/*.c") + ["sqlite3.c"]

include_dirs = ["."]

define_macros = [
    ("MODULE_NAME", quote_argument("pysqlite3.dbapi2")),
    # Always use memory for temp store.
    ("SQLITE_TEMP_STORE", "3"),
    # Increase the maximum number of "host parameters" which SQLite will accept
    ("SQLITE_MAX_VARIABLE_NUMBER", "250000"),
    # Increase maximum allowed memory-map size to 1TB
    ("SQLITE_MAX_MMAP_SIZE", str(2**40)),
    ("SQLITE_ALLOW_COVERING_INDEX_SCAN", "1"),
    ("SQLITE_ENABLE_FTS3", "1"),
    ("SQLITE_ENABLE_FTS3_PARENTHESIS", "1"),
    ("SQLITE_ENABLE_FTS4", "1"),
    ("SQLITE_ENABLE_FTS5", "1"),
    ("SQLITE_ENABLE_JSON1", "1"),
    ("SQLITE_ENABLE_LOAD_EXTENSION", "1"),
    ("ENABLE_MATH_FUNCTIONS", "1"),
    ("SQLITE_ENABLE_RTREE", "1"),
    ("SQLITE_ENABLE_STAT4", "1"),
    ("SQLITE_ENABLE_UPDATE_DELETE_LIMIT", "1"),
    ("SQLITE_SOUNDEX", "1"),
    ("SQLITE_USE_URI", "1"),
]

if sys.platform == "darwin":
    # Work around clang raising hard error for unused arguments
    extra_compile_args = ["-Qunused-arguments"]
else:
    extra_compile_args = []

if sys.platform != "win32":
    # Include math library, required for fts5.
    extra_link_args = ["-lm"]
else:
    extra_link_args = []

module = Extension(
    name="pysqlite3._sqlite3",
    sources=sources,
    include_dirs=include_dirs,
    define_macros=define_macros,
    extra_compile_args=extra_compile_args,
    extra_link_args=extra_link_args,
    language="c",
)

with open("README.md", "r", encoding="utf-8") as fr:
    long_description = fr.read()

if __name__ == "__main__":
    setup(
        name=PACKAGE_NAME,
        version=VERSION,
        description="DB-API 2.0 interface for Sqlite 3.x",
        long_description=long_description,
        long_description_content_type="text/markdown",
        author="Charles Leifer",
        author_email="coleifer@gmail.com",
        license="zlib/libpng",
        platforms="ALL",
        url="https://github.com/coleifer/pysqlite3",
        classifiers=[
            "Development Status :: 4 - Beta",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: zlib/libpng License",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
            "Operating System :: POSIX",
            "Programming Language :: C",
            "Programming Language :: Python",
            "Topic :: Database :: Database Engines/Servers",
            "Topic :: Software Development :: Libraries :: Python Modules",
        ],
        packages=["pysqlite3"],
        ext_modules=[module],
    )
