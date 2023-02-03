pysqlite3
=========

This library takes the SQLite module from Python 3 and packages it as a
separately-installable module.

This may be useful for creating SQLite modules capable of working with other
versions of SQLite (via the amalgamation option).

Additional features:

* User-defined window functions (requires SQLite >= 3.25)
* Flags and VFS an be specified when opening connection
* Incremental BLOB I/O, [bpo-24905](https://github.com/python/cpython/pull/271)
* Improved error messages, [bpo-16379](https://github.com/python/cpython/pull/1108)
* Simplified detection of DML statements via `sqlite3_stmt_readonly`.
* Sqlite native backup API (also present in standard library 3.7 and newer).

pysqlite3-wheels
================

A completely self-contained binary package (wheel) is available for versions 0.4.6 and newer as `pysqlite3-wheels` for all platforms. This package is linked against a recent release of SQLite compiled with numerous extensions, and requires no external dependencies.

```
$ pip install pysqlite3-wheels
```
