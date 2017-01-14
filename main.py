import os
import jinja2
import webapp2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                                autoescape = True)

def rot13(input_data):
	output_data = ""
	for char in input_data:
		ascii_val = ord(char)
		if ascii_val == 13 or  32 <= ascii_val <= 64:
			output_data += char
		elif 97 <= ascii_val <= 122:
			if ascii_val + 13 <= 122:
				output_data += chr(ascii_val + 13)
			else:
				output_data += chr(ascii_val + 13 - 26)
		elif 65 <= ascii_val <= 90:
			if ascii_val + 13 <= 90:
				output_data += chr(ascii_val + 13)
			else:
				output_data += chr(ascii_val + 13 - 26)
	return output_data





class Handler(webapp2.RequestHandler):
    """docstring for Handler"""
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class MainPage(Handler):
    def get(self):
        self.render("app.html")

    def post(self):
    	input_data = self.request.get("text")
    	self.render("app.html", input_data = rot13(input_data))

        
        


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ], debug=True)
