#### Add your user

We are ready for you to add your first user:

~~~~~~~~~~~
connectordb run mydatabase/db --join
~~~~~~~~~~~

The above command runs ConnectorDB with free join permissions, meaning that anyone can add themselves as a user. You can set fine-grained configuration
details in `mydatabase/db/connectordb.conf`. If running on a server, you will need to set up the site name in connectordb.conf before adding users.

Now, using your browser, navigate to `http://localhost:8000/join` (or whatever url ConnectorDB is set up on), where you will be prompted to create your user.

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

You can exit the running connectordb process, and run `connectordb stop mydatabase/db` to stop the underlying postgres/redis/nats servers.


<a href="/docs/howitworks.html" class="button alt">How ConnectorDB Works <i class="fa fa-arrow-right"></i></a>
