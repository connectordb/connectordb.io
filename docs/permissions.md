---
layout: docs
---
## Permissions

**WARNING:** *Permissions are the most complicated configuration of ConnectorDB. It is imperative that you know what you are doing when changing permissions, as you can create security issues and information leaks. You can also cause many errors, including making your entire database unusable when you change the wrong options.*

By default, ConnectorDB uses its built-in permissions structure, which creates a private server, where only users who are logged in have access to any data whatsoever. Using the optional `permissions.conf`, it is possible to modify this behavior to make connectordb more github-like (as is done with connectordb.com), and to enforce limits on specific roles.

To start playing around with permissions, you will need to add a permissions configuration file to your database.

```bash
connectordb create mydatabase
connectordb permissions mydatabase/mypermissions.conf
```

The connectordb `permissions` command generates a configuration file pre-populated with the default permissions used in ConnectorDB.

We now tell connectordb to use this configuration file instead of the default. In our database's connectordb.conf, we set `"permissions": "mypermissions.conf"`. Note that ALL permissions support auto-reload, meaning that the moment you change permissions, they are reloaded into ConnectorDB. To stop this behavior, set `watch: false` in permissions.conf.

And we are ready to begin experimenting...

### Permissions Structure
