__aesc__ (pronounced like "[ash][]") is a little http server written in Python and built on [Twisted Web][]. It's meant to effortlessly serve static files and wsgi applications.

[ash]: http://en.wiktionary.org/wiki/%C3%A6sc#Old_English
[Twisted Web]: http://cherrypy.org/


There's an example in the `example` directory; you can use `aesc example/configuration.json` and point your browser to localhost:8888.

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

## Todo:

* match domains based on regular expressions so we can do things like `.*?\.example.com`
