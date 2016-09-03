
# Creating a Database

ConnectorDB will be holding your personal data, so it is important to take some basic security precautions.
If you will be providing your own encryption, or just want to play around, feel free to skip the setup of an encrypted folder.

#### Setting up an encrypted folder
While the database itself does not support on-disk encryption out of the box, we provided a basic python2 script called [cryptify](https://github.com/connectordb/cryptify),
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


#### Create Your Database

Now it is time to create your first ConnectorDB database:

~~~~~~~~~~~
connectordb create mydatabase/db
~~~~~~~~~~~

This will create all of the necessary files in mydatabase/db

Next, in order for the server to work, you need to start the Postgres, Redis, and NATS servers which are used internally.
ConnectorDB provides the `start` command for exactly this purpose.

~~~~~~~~~~~
connectordb start mydatabase/db
~~~~~~~~~~~



[Configuring ConnectorDB](./config.html)
