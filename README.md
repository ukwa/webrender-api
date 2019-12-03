webrender-api
=============

A standalone web-rendering service, for rendering the live web during crawls, and rendering the archived web afterwards.  During crawls, it should be deployed behind warcprox, which ensures all the required resources are packaged as WARC records.  When used after crawls, it can be used to compare pre/post-crawl results and for access screenshot and thumbnail generation.



API
---

### /render?url={URL}

Renders the given URL in the browser, extracts the relevant links, and passes a summary back to the caller as a JSON object.

This is done using a PhantomJS script based on one provided with PhantomJS.

e.g. an `&` needs to be encoded as %26
 
Additional query parameters: `warc-prefix`, `selectors` and `include-rendered`

Running the application
-----------------------

For development purposes, install [Flask](http://flask.pocoo.org/) and run

    $ FLASK_APP=webrender/wrengine.py flask run

and go to http://127.0.0.1:5000/

For production deployment, an example [gunicorn](http://docs.gunicorn.org/en/latest/install.html) configuration is included:

    $ gunicorn -c gunicorn.ini webrender.wrengine:app


