# ConnectorDB Website & Documentation

This repository contains the full website of the ConnectorDB open source project, as well as its documentation.


## Building

To build the docs and website, you will need [jekyll](https://jekyllrb.com/) and [sphinx](http://www.sphinx-doc.org/en/1.4.8/). You will also need to install [recommonmark](https://recommonmark.readthedocs.io/en/latest/):

```bash
git clone https://github.com/connectordb/connectordb.github.io
cd connectordb.github.io

apt-get install jekyll python-sphinx
pip install recommonmark
```

Then, to build the full website, including docs, you can run `_build`

```bash
./_build
```

This will create a copy of the website in the `_site` subdirectory.

To run the website while editing, you can serve jekyll:
```
jekyll serve --watch
```

## Documentation

The documentation is in `./_docs`. Note that the `pipescript/transforms` docs are auto-generated from pipescript - please do not edit them manually.

When editing the docs, you can run `make` in the `_docs` directory to run sphinx and generate documentation. Each time you run `make`, your changes should
be immediately available in the browser if running jekyll in watch mode.

## Contributing

All contributions are welcome - if something in the docs is confusing, ask about it on [gitter](https://gitter.im/connectordb/connectordb), and send a PR with an explanation that would work for you!

Feel free to add/fix anything in the docs! PRs are *very* warmly received.
