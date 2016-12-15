# domain
*Returns the domain name/host that is used in the given url*

The domain transform is run on URLs, and returns the domain.

For example:
```json
[
  "https://golang.org/pkg/net/url/#URL.EscapedPath",
  "https://connectordb.io",
  "https://github.com/connectordb/connectordb"
]
```
gives:
```json
[
  "golang.org",
  "connectordb.io",
  "github.com"
]
```


---

#### Transform Details
<table class='pipescriptargs'><thead><tr><th>One-To-One</th><th>Stateless</th><th>Peek</th><th>Input Schema</th><th>Output Schema</th></tr></thead><tr><td>True</td><td>True</td><td>False</td><td></td><td>{"type": "string"}</td></tr></table>

