---
layout: docs
---
## Configuration

When starting or running, connectordb loads all of the necessary information from a JSON-formatted configuration file.

To see the file, you can navigate to your database directory, and open connectordb.conf

```bash
connectordb create mydatabase/db
vim mydatabase/db/connectordb.conf
```

You will notice that the configuration file permits usage of javascript-style comments (both /\*\*/ and //).

As of version 0.3.0 of ConnectorDB, several configuration options in connectordb.conf support live-reload,
meaning that they automatically take into effect once you modify the configuration file even when ConnectorDB is running. To disable live reload, you can set the `watch` option to false. Other options do not support live reload (such as ssl certificates), and will silently fail to update.

### SiteUrl

The most important value in ConnectorDB's config is the site url. ConnectorDB expects to be set up using a domain or specific IP.

If you have ConnectorDB set up at an IP, set the `siteurl` property to the IP. It is recommended that you run it with a domain name, since this allows use of HTTPS, and
enables the android app to sync from the internet (NEVER have ConnectorDB accessible from the internet if it is not using https).

Suppose you have ConnectorDB set up to run at `cdb.mysite.com`. You then set `"siteurl": "https://cdb.mysite.com"`.

You must also set up the port on which connectordb will be hosted. By default, this is set to 8000, which is a good value when running connectordb behind a reverse proxy.


### Setting Up HTTPS

ConnectorDB can run its own https stack, but it is preferable to have it behind an nginx or caddy proxy.

Nevertheless, you can set up https using Let's Encrypt by setting `tls.enabled` to true, `tls.acme.enabled` to true, `tls.acme.domains` to `["cdb.mysite.com"]`, and finally `tls.acme.tos_agree` to true (meaning that you agree to the Let's Encrypt terms of service).


This is how your tls configuration should look after setting it up:

```
{
	"enabled": true,
	"key": "tls_key.key",
	"cert": "tls_cert.crt",
	"acme": {
		"enabled": true,
		"server": "https://acme-v01.api.letsencrypt.org/directory",
		"private_key": "acme_privatekey.pem",
		"registration": "acme_registration.json",
		"domains": ["cdb.mysite.com"],
		"tos_agree": true
	}
}
```

You must also set `port` to 443, so that ConnectorDB can correctly perform validation. Using acme does not work behind a reverse proxy.

Normally, user processes can't access lower ports (such as 443). This can be fixed by running
the following on the connectordb executable:

```
sudo setcap cap_net_bind_service=+ep connectordb
```

You can run ConnectorDB now, but you will notice that while https://cdb.mysite.com is functional,
the http version gives you nothing. Usually you'd want port 80 to redirect to https. This is what the redirect80 option does. Setting redirect80 to true in the configuration will have ConnectorDB
redirect traffic from http to your server's URL.


## That's It!

After doing the above two configuration steps, your ConnectorDB database is ready for use!

There are also some more interesting properties, which are optional.

### Running from Configuration file
Sometimes the database itself is distributed over multiple machines. In those cases, you can run ConnectorDB using only a configuration file

```
connectordb run myconfig.conf
```


### Permissions

By default, Connectordb uses its builtin permissions (`default`). If you want to be able to change what users and devices are and are not permitted to do, and the specific fine-grained access levels of each, make sure to check out the [permissions docs](./permissions.html).

For most people, the default permissions should work fine, and should not need to be changed.


<a href="/docs/users.html" class="button alt">Add Users <i class="fa fa-arrow-right"></i></a>
