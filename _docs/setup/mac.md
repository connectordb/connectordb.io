# Mac

```eval_rst
.. centered:: Click `here </download/connectordb_server_current_mac_amd64.tar.gz>`_ to download ConnectorDB Server for Mac.
```
<!-- This code ensures that the download starts if coming from download page -->
<script type="text/javascript">if (/[?&]dl=1/.test(window.location.search)) window.location.href="/download/connectordb_server_current_mac_amd64.tar.gz";</script>


Unfortunately, there is no mac desktop version of ConnectorDB at this time. That means that you cannot yet gather data on your laptop use, nor can you have
an automatically managed ConnectorDB server.

However, experimental builds are available of the ConnectorDB server itself. On mac, it is recommended that you use the sqlite backend, rather than postgres:


```
connectordb create mydatabase --sqlbackend=sqlite3
connectordb start mydatabase --join
```

Going to `http://localhost:3124/join` will allow you to add users to your database. When done, run: 

```
connectordb stop mydatabase
```

This will disable free join mode.

Finally, to run ConnectorDB, you simply run:

```
connectordb start mydatabase
```
