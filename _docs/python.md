## Python

The ConnectorDB Python client's full documentation is at ReadTheDocs. The ConnectorDB API allows you total access to your data and ConnectorDB's dataset generation capabilities.

<a href="https://connectordb-python.readthedocs.io/en/latest/tutorial.html" class="button alt"><i class="fa fa-external-link"></i> View Python Tutorial</a>

#### tl;dr:

```bash
pip install connectordb
```

```python
import connectordb
cdb = connectordb.ConnectorDB("apikey",url="https://cdb.mysite.com")
cdb["mystream"].insert("hi!")
```

If you have a favorite language, or you don't want to work in python, you can look at the REST API to interface with ConnectorDB directly:

<a href="/docs/restapi.html" class="button alt">REST API <i class="fa fa-arrow-right"></i></a>
