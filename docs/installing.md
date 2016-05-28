---
layout: docs
---
## Installing ConnectorDB

To start off, you need to make sure that you have all of the necessary dependencies. ConnectorDB needs recent versions of both Postgres and Redis installed:

{% highlight bash %}
apt-get install postgresql redis-server
{% endhighlight %}

The servers are managed by ConnectorDB, so you do not need them to be run on startup:

{% highlight bash %}
systemctl disable postrgresql.service
systemctl stop postgresql.service
systemctl disable redis-server.service
systemctl stop redis-server.service
{% endhighlight %}

Next, download the ConnectorDB binaries. Only 64 bit linux is supported at this time.

{% highlight bash %}
wget https://connectordb.github.io/dist/connectordb0.3.0a1.tar.gz
tar -zxvf connectordb0.3.0a1.tar.gz

{% endhighlight %}

Finally, make sure that connectordb is working:

{% highlight bash %}
cd connectordb
./connectordb --version
{% endhighlight %}

You should see something like the following:

~~~~~~~~~~~~~~~
ConnectorDB version 0.3.0a1
~~~~~~~~~~~~~~~

This means that you're ready to use ConnectorDB. All of the files in the binary folder are required for proper operation.
You should move this folder somewhere where it won't bother you, and add it to your PATH.

 All further instructions assume that the `connectordb` executable is in your PATH.

 Your next task is creating a ConnectorDB database:

<a href="/docs/creating.html" class="button alt">Creating a Database <i class="fa fa-arrow-right"></i></a>
