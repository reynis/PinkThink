import os
import urllib
import cgi

from google.appengine.api import users
from google.appengine.ext import ndb

import jinja2
import webapp2


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        # Checks for active Google account session
        user = users.get_current_user()

        if user:
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

        template_values = {
            'user' : user,
            'url' : url,
            'url_linktext': url_linktext
        }

        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))

codeList = list()

class CreatePage(webapp2.RequestHandler):
    def get(self, codeid):
        # Checks for active Google account session
        user = users.get_current_user()
        if codeid == "clear":
            if codeList:
                codeList.pop()
        else:
            codeList.append(codeid);

        if user:
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

        template_values = {
            'user' : user,
            'url' : url,
            'url_linktext': url_linktext,
            'codeList' : codeList
        }

        template = JINJA_ENVIRONMENT.get_template('html/create.html')
        self.response.write(template.render(template_values))

class ProjectsPage(webapp2.RequestHandler):
    def get(self):
        # Checks for active Google account session
        user = users.get_current_user()

        if user:
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

        template_values = {
            'user' : user,
            'url' : url,
            'url_linktext': url_linktext
        }

        template = JINJA_ENVIRONMENT.get_template('html/myprojects.html')
        self.response.write(template.render(template_values))

class ExplorePage(webapp2.RequestHandler):
    def get(self):
        # Checks for active Google account session
        user = users.get_current_user()

        if user:
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

        template_values = {
            'user' : user,
            'url' : url,
            'url_linktext': url_linktext
        }

        template = JINJA_ENVIRONMENT.get_template('html/explore.html')
        self.response.write(template.render(template_values))

class SubmitPage(webapp2.RequestHandler):
    def get(self):
        # Checks for active Google account session
        user = users.get_current_user()

        if user:
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

        template_values = {
            'user' : user,
            'url' : url,
            'url_linktext': url_linktext,
            'codeList' : codeList
        }

        template = JINJA_ENVIRONMENT.get_template('html/submit.html')
        self.response.write(template.render(template_values))



app = webapp2.WSGIApplication([
    ('/create/(.*)', CreatePage),
    ('/submitcode', SubmitPage),
    ('/myprojects', ProjectsPage),
    ('/explore', ExplorePage),
    (r'/.*', MainPage),
], debug=True)
