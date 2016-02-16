---
layout: docs
---
## Configuration

When starting or running, connectordb loads all of the necessary information from a JSON-formatted configuration file.

To see the file, you can navigate to your database directory, and open connectordb.conf

```bash
connectordb create mydatabase
vim mydatabase/connectordb.conf
```

You will notice that the configuration file permits usage of javascript-style comments (both /\*\*/ and //).

As of version 0.3.0 of ConnectorDB, several configuration options in connectordb.conf support live-reload,
meaning that they automatically take into effect once you modify the configuration file. To disable live reload, you can set the `watch` option to false. Other options do not support live reload (such as ssl certificates), and will silently fail to update.

You can run connectordb from a configuration file as follows:

```
connectordb run myconfig.conf
```

You can also run ConnectorDB by giving it a path to your database folder

```
connectordb run mydatabase
```

If connectordb is run using a database folder path, it will source its configuration from the `connectordb.pid` file which is created when starting the backend servers. This means that
any changes made to connectordb.conf will not take into effect until stop/start of the backend servers.
It also means that any changes made to `connectordb.pid`, will be lost after connectordb is stopped.

### Setting Up HTTPS

In your `connectordb.conf`, you should find the `tls_key` and `tls_cert` configuration options (empty by default).
You can input the path to your key and certificate, and they will be loaded on connectordb start.

It is up to you to keep certificates up to date. Due to the necessity of restart each time TLS keys are changed, it is recommended that you run connectordb on `hostname: localhost` and put it behind an NGINX proxy. With this setup, you can use standard tutorials to obtain a free [let's encrypt SSL certificate for NGINX](https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-14-04).


### Sitename & Hostname

Another important property in ConnectorDB is the sitename & Hostname.

While you can leave them at the default values
when playing around with the database, be aware that by default ConnectorDB accepts connections from everyhere, including other computers (if you want it only to accept connections from your computer, set hostname to `localhost`).

If running connectordb on your own web-facing server (as you probably want to, in order for your phone to be able to sync), make sure to set `sitename` to the exact url at which connectordb is running. That is, if you
run connectordb at `connectordb.myname.com` with https enabled, sitename should be `https://connectordb.myname.com`.

### Permissions

By default, Connectordb uses its builtin permissions (`default`). If you want to be able to change what users and devices are and are not permitted to do, and the specific fine-grained access levels of each, make sure to check out the [permissions docs](./permissions.html).

For most people, the default permissions should work fine, and should not need to be changed.
