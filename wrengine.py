from phantomjs import phantomjs
import logging
import json
import flask

# Flash application context
app = flask.Flask(__name__)

# Setup logging
logging.getLogger().setLevel(logging.DEBUG)


@app.route('/')
def welcome():
    """
    :return: The Wrender homepage
    """
    return 'Wrender'


@app.route('/render')
def render():
    """
    Tries to retrieve the HAR with rendered images, returning a 500 if timing out.
    If data is POST'd it expects a string-representation of a list of selectors, e.g.:
    "[\":root\"]"
    """
    url = flask.request.args.get('url')
    app.logger.debug("Got URL: %s" % url)
    #
    selectors = flask.request.args.get('selectors', ':root')
    app.logger.debug("Got selectors: %s" % selectors)
    #
    warc_prefix = flask.request.args.get('warc_prefix', 'wrender')
    app.logger.debug("Got WARC prefix: %s" % warc_prefix)
    #
    include_rendered = flask.request.args.get('include_rendered', False)
    app.logger.debug("Got include_rendered: %s" % include_rendered)
    #
    return flask.jsonify(phantomjs.get_har_with_image(url, selectors, warc_prefix=warc_prefix, include_rendered=include_rendered))
