__aesc__ (pronounced like "[ash][]") is a little http server written in Python and built on [Twisted Web][]. It's meant to effortlessly serve static files and wsgi applications.

[ash]: http://en.wiktionary.org/wiki/%C3%A6sc#Old_English
[Twisted Web]: http://cherrypy.org/

## Using It:

Configuration is done in json; your file should look like this:

````json
{
    "port": 80,
    "static": {
        "static.example.com":"/home/example/public/static"
    },
    "wsgi": {
        "dynamic.example.com":"wsgimodule.app"
    }
}
````

To start aesc, given a configuration file `config.json`, run `aesc config.json`.
