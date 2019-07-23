# the import section
import webapp2
import jinja2
import os

# this initializes the jinja2 environment
# this will be the same in every app that uses the jinja2 templating library 
the_jinja_env = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
  extensions=['jinja2.ext.autoescape'],
  autoescape=True)

# other functions should go above the handlers or in a separate file

# the handler section
class MainHandler(webapp2.RequestHandler):
  def get(self):  # for a get request
    results_template = the_jinja_env.get_template('templates/game-start.html')  # path to index.html
    self.response.write(results_template.render()) # render index.html


# the app configuration section	
app = webapp2.WSGIApplication([
  ('/', MainHandler),
  ], debug=True)