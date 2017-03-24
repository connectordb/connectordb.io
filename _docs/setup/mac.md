# Mac

```eval_rst
.. centered:: Click `here </download/connectordb_desktop_current_darwin_amd64.tar.gz>`_ to download ConnectorDB for Mac.
```
<!-- This code ensures that the download starts if coming from download page -->
<script type="text/javascript">if (/[?&]dl=1/.test(window.location.search)) setTimeout(function() {window.location.href="/download/connectordb_desktop_current_darwin_amd64.tar.gz";},0);</script>


```eval_rst
.. warning:: The Mac version of ConnectorDB does not gather data from your desktop yet. It will only manage a local ConnectorDB server for you. For more information on the progress of data-gathering in macs, click `here <https://github.com/connectordb/connectordb/issues/318>`_.
```

To start off, you will need to install a couple dependencies of ConnectorDB, since the Mac version does not yet have an installer.

```
brew install redis
brew install pyqt5
pip3 install connectordb apsw
```

Once these two are installed, you should double-click on the .tar.gz file you downloaded to extract it. 

Then, double-click on the `connectordb-desktop` file. You will get a terminal window pop up, and after a couple seconds, this screen will pop up:

<img src="/assets/docs/img/mac-desktop.png"/>

Type in your chosen username and password, and click `create`. After a couple seconds of work, ConnectorDB will appear in the top corner of your screen:

<img src="/assets/docs/img/mac-icon.png"/>

While the click-menu suggests that data is being gathered, Macs do not yet support desktop data-gathering.


```eval_rst
.. warning:: You will notice that ConnectorDB's app will open your browser upon being clicked. You will need to use Chrome or Firefox as your browser. Safari is not supported at this time.
```

Finally, you will want to run ConnectorDB on login, so it is always started in the background. 
[Please follow these instructions](http://stackoverflow.com/questions/6442364/running-script-upon-login-mac/13372744#13372744) to start ConnectorDB on login.
