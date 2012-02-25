from distutils.core import setup
import graven

setup(
    name = "aesc",
    version = "0.00.0dev",
    author = "startling",
    author_email = "tdixon51793@gmail.com",
    description = "a twisted.web wrapper for serving static files and wsgi",
    scripts = ['aesc'],
    install_requires = ["twisted", "argent"]
)
