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

Most options should be fairly self-explanatory, but the core permissions structure is complicated. It can be summarized with the following:

```javascript
{
	...
	"user_roles": {
		"myrole": {
			...
			"private_access_level": "level1",
			"public_access_level": "level2",
			"user_access_level": "level3",
			"self_access_level": "level4"
		},
		"user": {...},
		"nobody": {...}
	},
	"device_roles": {
		"myrole": {
			...
			"private_access_level": "level1",
			"public_access_level": "level2",
			"user_access_level": "level3",
			"self_access_level": "level4"
		},
		"user": {...},
		"nobody": {...},
		...
	},
	"access_levels": {
		"level1": {
			"read_access": "rwaccess1",
			"write_access": "rwaccess2"
		},
		...
	},
	"rw_access": {
		"rwaccess1": {
			...
			"user_...": true,
			"device_...": false,
			"stream_...": false
		}
	}

}
```

#### Roles

The first thing you will notice is that there are `user_roles` and `device_roles`. These are the possible roles given to every single user and device. They are visibly to querying by default.

Of special note is the required "nobody" user role. This is the role a random visitor to the server takes when they are not logged in. Any permissions given to the nobody role will be granted to anonymous visitors.

The `none` device role is given to devices which do not have a role set. This is the default for newly created devices.

Next, within each role (both user and device), we have 4 particularly important fields:

* private_access_level: This is the access level given to this device when attempting to query users/devices which have their public flag set to false, meaning that they are "private"
* public_access_level: This is the access level given to this device when attempting to query users/devices which have their public flag set to true.
* user_access_level: This is the access level given to this device when attempting to query its own user or its user's devices/streams
* self_access_level: This is the access level given to this device when attempting to query itself, meaning its own device and its own streams.

Note that a device can have *up to* its user's permissions. That is, if user "bob" does not have read access to private users, then none of Bob's devices will have such access, no matter what their permissions.

#### Access Levels

Each access level specifies its read and write access.

#### RW Access

This is a boolean permissions matrix. each property starting with user_ is a part of each user's structure (same with device and stream). If the access is for read, a value of true means that the property will be read (accessible to the querying device). If the access is for write, it means that the property can be written by its querying device.


### Why so complex?

The split into roles/accesslevels/rw_access was in an attempt to avoid repetition, as many roles and access levels use the same rw_access, etc.

The complexity of the permissions file is necessary to allow total control of ALL permissions that ConnectorDB exposes. It allows reconfiguring the database to be a private repository for a single user or database (the default configuration), or to be
a fully public github-style location for IoT data, and everything in between.
