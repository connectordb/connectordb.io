# Installing ConnectorDB

If you want to set up an internet-connected server, [DigitalOcean is highly recommended](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-16-04).
This tutorial assumes that you have already set up a server.

To start off, you need to make sure that you have all of the necessary dependencies. ConnectorDB needs recent versions of both Postgres and Redis installed:

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

Next, download the ConnectorDB binaries. Only 64 bit linux is supported at this time.

```bash
wget https://github.com/connectordb/connectordb/releases/download/v0.3.0a1/connectordb0.3.0a1.tar.gz
tar -zxvf connectordb0.3.0a1.tar.gz

```

Finally, make sure that connectordb is working:

```bash
cd bin
./connectordb --version
```

You should see something like the following:

~~~~~~~~~~~~~~~
ConnectorDB version 0.3.0a1
~~~~~~~~~~~~~~~

This means that you're ready to use ConnectorDB. All of the files in the binary folder are required for proper operation.
You should move this folder somewhere where it won't bother you, and add it to your PATH.

 All further instructions assume that the `connectordb` executable is in your PATH.

 Your next task is creating a ConnectorDB database:

<a href="/docs/creating.html" class="button alt">Creating a Database <i class="fa fa-arrow-right"></i></a>
