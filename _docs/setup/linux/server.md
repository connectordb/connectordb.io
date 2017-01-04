# Server

If you want to set up an internet-connected server, [DigitalOcean is highly recommended](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-16-04).
This tutorial assumes that you have already set up a server.

## Dependencies

To start off, you need to make sure that you have all of the necessary dependencies.  Be warned that Debian jessie packages are not sufficient; specifically ConnectorDB requires Redis >= 3, golang >= 1.6, and node-js >= 4.  Debian stretch will provide sufficient versions of Redis and golang only.  Node for Debian may be downloaded at https://github.com/nodesource/distributions .

ConnectorDB needs recent versions of both Postgres and Redis installed:

```bash
sudo apt-get install postgresql redis-server
```

The servers are managed by ConnectorDB, so you do not need them to be run on startup:

```bash
sudo systemctl disable postgresql.service
sudo systemctl stop postgresql.service
sudo systemctl disable redis-server.service
sudo systemctl stop redis-server.service
```

The API tests will require a couple python packageS:

```bash
sudo apt-get install python-coverage python-websocket python-jsonschema
# or simply
pip install connectordb
```

Next, download the ConnectorDB binaries. Only 64 bit linux is supported at this time.

```bash
wget https://github.com/connectordb/connectordb/releases/download/v0.3.0a1/connectordb0.3.0b1.tar.gz
tar -zxvf connectordb0.3.0b1.tar.gz

```

Finally, make sure that connectordb is working:

```bash
test@connectordb.com $ cd ./bin
test@connectordb.com $ ./connectordb --version
ConnectorDB 0.3.0b1

arch: linux/amd64
go: go1.7
git: 209f1335b95aa115c57642c06f896e03b68d637c
build: 2016-09-06_07:29:26AM
```

Usually, processes can't access lower ports (such as 443 or 80).
To let ConnectorDB access these ports, you will need to run the following command:
```
sudo setcap cap_net_bind_service=+ep connectordb
```


All of the files in the binary folder are required for proper operation.
You should move this folder somewhere where it won't bother you, and add it to your PATH.

```bash
mv ./bin ~/.connectordb
```

Add the following to your .bashrc:

```bash
export PATH=$PATH:~/.connectordb
```


## Setting up an Encrypted Folder

ConnectorDB will be holding very personal data, so it is important to take some basic
security precautions. If you will be providing your own encryption, or just want to play around, feel free to skip this step.

ConnectorDB does not come with built-in encryption support, but you can use a basic python2 script called [cryptify](https://github.com/connectordb/cryptify),
with which you can set up an encrypted password-protected container for your ConnectorDB database.

```bash
apt-get install python-subprocess32 cryptsetup
wget -O cryptify https://raw.githubusercontent.com/connectordb/cryptify/master/cryptify
chmod +x cryptify
```

With this script, you can create a 10GB container for your database, saved as `mydatabase.crypt`, and mounted in folder `mydatabase` with the following command:

```bash
./cryptify -i mydatabase.crypt -o mydatabase -s 10000 create
```

On future reboots, you can run `./cryptify -i mydatabase.crypt -o mydatabase open`
to mount your folder, and `./cryptify -i mydatabase.crypt -o mydatabase close`
to dismount.

## Creating a Database

Now it is time to create a ConnectorDB database:

```
connectordb create mydatabase/db
```

The above command will create all the files necessary to run your ConnectorDB server in `mydatabase/db`.

## Configuring ConnectorDB

When starting or running, connectordb loads all of the necessary information from a JSON-formatted configuration file.

To see the file, you can navigate to your database directory, and open `connectordb.conf`

```bash
vim mydatabase/db/connectordb.conf
```

Before you can successfully run ConnectorDB on your server, you will need to edit a couple options. Only the options that need editing are shown below:

```javascript
{
  // This option needs to be set for ConnectorDB to work on the internet. If you don't
  // have a domain name (such as when running on a local Raspberry Pi), you can use
  // the IP address instead: http://192.168.1.123
  "siteurl": "https://cdb.mysite.com",

  // When running behind a reverse proxy (such as caddy or nginx), you can leave this
  // value at the default. If you want ConnectorDB to be secure, make sure to run
  // it on port 443 (if running without a domain name, you will either have to use port 80 or
  // generate your own https certificates)
  "port": 443,
  // Since we're running on port 443 (https), we redirect port 80 (http).
  "redirect80": true,

  // Make sure that ConnectorDB is exposed to the internet
  "hostname": "0.0.0.0",

  // ConnectorDB can generate its own Let's Encrypt TLS certificates, so that nobody
  // can snoop on your data. Change the following values to enable Let's Encrypt support.
  "tls": {
    "enabled": true,
    "acme": {
      "enabled": true,
      "domains": [
        "cdb.mysite.com"
      ],
      // You must agree to the Let's Encrypt terms of service
      "tos_agree": true
    }
  },
}
```

## Creating a User

With ConnectorDB all set up, you can add all of your users by running with `join` enabled:

```
connectordb start mydatabase/db --join
```

You can now use your browser to add as many users as you want by navigating to `https://cdb.mysite.com/join`.

Once all users are added, you should stop ConnectorDB to disable join mode:

```
connectordb stop mydatabase/db
```

## Running ConnectorDB

#### Start

```
connectordb start mydatabase/db
```

#### Stop

```
connectordb stop mydatabase/db
```

#### Encrypted folder

Remember that you will have to decrypt your database folder each time you restart:
```
./cryptify -i mydatabase.crypt -o mydatabase open
```
