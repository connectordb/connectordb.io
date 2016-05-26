---
layout: docs
---
## Creating a Database

ConnectorDB will be holding your personal data, so it is important to take some basic security precautions.
If you will be providing your own encryption, or just want to play around, feel free to skip the setup of an encrypted folder.

#### Setting up an encrypted folder
While the database itself does not support on-disk encryption out of the box, we provided a basic python2 script called [cryptify](https://github.com/connectordb/cryptify),
with which you can set up an encrypted password-protected container for your ConnectorDB database.

{% highlight bash %}
apt-get install python-subprocess32 cryptsetup
wget -O cryptify https://raw.githubusercontent.com/connectordb/cryptify/master/cryptify
chmod +x cryptify
{% endhighlight %}

With this script, you can create a 10GB container for your database, saved as `mydatabase.crypt`, and mounted in folder `mydatabase` with the following command:

~~~~~~~~~~~~
./cryptify -i mydatabase.crypt -o mydatabase -s 10000 create
~~~~~~~~~~~~

On future reboots, you can run `./cryptify -i mydatabase.crypt -o mydatabase open`
to mount your folder, and `./cryptify -i mydatabase.crypt -o mydatabase close`
to dismount.


#### Create Your Database

Now it is time to create your first ConnectorDB database:

~~~~~~~~~~~
connectordb create mydatabase/db
~~~~~~~~~~~

This will create your own personal ConnectorDB database.

Next, in order for the server to work, you need to start the Postgres, redis, and NATS servers which are used internally.
ConnectorDB provides the `start` command for exactly this purpose.

~~~~~~~~~~~
connectordb start mydatabase/db
~~~~~~~~~~~


#### Add your user

Finally, we are ready for you to add your first user:

~~~~~~~~~~~
connectordb run mydatabase/db --join
~~~~~~~~~~~

The above command runs ConnectorDB at `localhost:8000`, and with free join permissions, meaning that anyone can add themselves as a user. You can set fine-grained configuration
details in `mydatabase/db/connectordb.conf`. If running on a server, you will need to set up the site name in connectordb.conf before adding users.

Now, using your browser, navigate to `http://localhost:8000/join`, where you will be prompted to create your user.

Once all of the users you want are added, you can `ctrl+c` on the running database.

If you want to create users in the future, you should designate a user as administrator, so that this user can always access the `join` page. For security,
you cannot make a user an admin from the web app. You need to manually run the connectordb shell:

~~~~~~~~~~~
connectordb shell mydatabase/db
> mkadmin username
> exit
~~~~~~~~~~~

Once finished, you can run connectordb without free join permissions:

~~~~~~~~~~~
connectordb run mydatabase/db
~~~~~~~~~~~

Once you are done, you can exit the running connectordb process, and run `connectordb stop mydatabase/db` to stop the underlying postgres/redis/nats servers.


<a href="/docs/config.html" class="button alt">Configuring ConnectorDB <i class="fa fa-arrow-right"></i></a>
