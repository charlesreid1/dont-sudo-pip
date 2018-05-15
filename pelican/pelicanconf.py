import markdown

AUTHOR = 'charlesreid1'
SITENAME = 'dont-sudo-pip'
SITEURL = 'dont-sudo-pip'
PATH = 'content'
TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = 'en'

# --------------8<---------------------

THEME = 'scurvy-knave-theme'

LICENSE_URL = "https://opensource.org/licenses/MIT"
LICENSE_NAME = "MIT License"

# Pelican is designed for files => pages.
# Use variables (below) to set pieces of pages.

# crimson and rust and dull red
INTROCOLOR  = "#fff"
ACOLOR      = "#8c000f"
AHOVERCOLOR = "#a83c09"
BRIGHTCOLOR = "#bb3f3f"
TEMPLATE_PAGES = {
    'custom.css' : 'custom.css'
}

INTROBKG='img/black.jpg'
LINKSBKG='img/moon.jpg'

# img/ should be in content/
# available at <url>/img
STATIC_PATHS = ['img']

# ---

# description appears between <p> tags, so don't include them

SITE_TITLE = "don't sudo pip"
SITE_DESCRIPTION = "it's insanely dangerous. don't believe me? try it:<br /><br /><code>sudo pip install russian_roulette</code><br /><br /><img src='img/output.gif' /><br /><br />"
GITEA_URL = "https://git.charlesreid1.com/charlesreid1/dont-sudo-pip"

# ---

about_md = markdown.Markdown(extensions=['extra','codehilite'],
                             output_format='html4')

ABOUT_SHORT = "why not?"

ABOUT_TITLE = "don't sudo pip install, ever"

ABOUT_TEXT = """

<br />
<br />

**You're paranoid. What's the big deal?**

Running `sudo pip install package-x` is insanely dangerous. It is equivalent to giving a complete stranger root access on your machine.  
You run pip as sudo, and pip runs setup.py as sudo, and setup.py can run system commands.

...in case you're wondering, that's bad.

![happy to sad](img/happy2sad.gif)

<br />
<br />

**What could possibly go wrong?**

A couple of things.

First, **typosquatting**. You could make a typo or spelling mistake when installing a package,
and a malicious typosquatting package could be installed instead. Imagine running
`sudo pip install uincode` and installing a malicious package `uincode`, 
instead of `sudo pip install unicode` like you wanted.

Second, **unintentional vulnerabilities**. Developers of a package may unintentionally expose 
a security hole that, when run as root, turns a minor security risk into a major one.
Say hello to bad dudes cruising the internet.

Third, **you could squash your system python**. Many modern operating systems
come with a system python that should be updated infrequently. Tacking on a sudo 
command could install packages that break your system.

Last, **malicious packages**. People do evil shit, especially when money's involved.

![some men just wanna watch the world burn](img/burn.gif)

<br />
<br />

**What should I do instead?**

Use [pyenv](https://github.com/pyenv/pyenv) to maintain separate, side-by-side versions of Python.

Use [virtualenv](https://virtualenv.pypa.io/en/stable/) to install software into an isolated Python environment.

Add the `--user` flag to install to your home directory, obviating the need for sudo: `pip install --user package-x`

(At the very least, set up your Python so it doesn't require sudo access each time it installs things.)

<br />
<br />

**How do I adjust my mindset?**

So just remind yourself of this, each time you type pip: 

***`setup.py` can run system commands.***

***`setup.py` can run system commands.***

***`setup.py` can run system commands.***

Never forget. Don't be a sheep. Trust no one.

<br />
<br />

<img src="img/defcon.png" />

"""

ABOUT_DESCRIPTION = about_md.convert(ABOUT_TEXT)



# -----------



def make_pages():
    descr = ""



    #############################
    # links around the web

    descr += "<h3>Links</h3>"

    # items format:     [ button text,    href url,    fa-icon ]
    items  = [
                ["python security",                       "https://www.python.org/news/security/",                       "globe"],
                ["pyto squatting project",                "https://www.pytosquatting.org/",                              "globe"],
                ["pypi hit by typosquatting sneak attack","https://tinyurl.com/y7gdjjne",                                "globe"],
                ["typosquatting package managers",        "https://tinyurl.com/zdsk8ok",                                 "globe"],
                ["measures taken by python security team","https://tinyurl.com/ydeynzjn",                                "globe"],
                ["fedora wiki: making sudo pip safe",     "https://fedoraproject.org/wiki/Changes/Making_sudo_pip_safe", "globe"],
                ["stack overflow: use a virtual env",    "https://stackoverflow.com/a/15028735",                         "globe"],
            ]

    for item in items:
        button_text = item[0]
        button_link = item[1]
        button_icon = item[2]

        descr += "<p><a class=\"btn btn-default btn-lg\" href=\"%s\">"%(button_link)
        descr += "<i class=\"fa fa-fw fa-2x fa-%s\"></i> %s"%(button_icon, button_text)
        descr += "</a></p>\n"

    descr += "\n"




    #############################
    # software 

    descr += "<h3>Software</h3>"

    # items format:     [ button text,    href url,    fa-icon ]
    items  = [
                ["virtualenv documentation",              "https://virtualenv.pypa.io/en/stable/",                       "globe"],
                ["pyenv documentation",                   "https://github.com/pyenv/pyenv",                              "globe"],
                ["pyenv installer",                       "https://github.com/pyenv/pyenv-installer",                    "globe"],
            ]

    for item in items:
        button_text = item[0]
        button_link = item[1]
        button_icon = item[2]

        descr += "<p><a class=\"btn btn-default btn-lg\" href=\"%s\">"%(button_link)
        descr += "<i class=\"fa fa-fw fa-2x fa-%s\"></i> %s"%(button_icon, button_text)
        descr += "</a></p>\n"

    descr += "\n"


    #############################
    # links to source/page

    descr += "<h3>Source</h3>"

    # items format:     [ button text,    href url,    fa-icon ]
    items  = [
                ["git.charlesreid1.com/charlesreid1/dont-sudo-pip",     "https://git.charlesreid1.com/charlesreid1/dont-sudo-pip", "code-fork"],
                ["github.com/charlesreid1/dont-sudo-pip",               "https://github.com/charlesreid1/dont-sudo-pip",           "github"],
                ["pages.charlesreid1.com/dont-sudo-pip (you are here)", "https://pages.charlesreid1.com/dont-sudo-pip",            "globe"],
            ]

    for item in items:
        button_text = item[0]
        button_link = item[1]
        button_icon = item[2]

        descr += "<p><a class=\"btn btn-default btn-lg\" href=\"%s\">"%(button_link)
        descr += "<i class=\"fa fa-fw fa-2x fa-%s\"></i> %s"%(button_icon, button_text)
        descr += "</a></p>\n"

    descr += "\n"

    descr += "\n"

    return descr



LINKS_TITLE = ""

LINKS_DESCRIPTION = make_pages()



# ---


CONTACT_TITLE = "Contact charlesreid1"

CONTACT_DESCRIPTION = """<p>@charlesreid1 is a full-time data engineer and part-time bot-wrangler working on bioinformatics problems at UC Davis.</p>
<p>Get in touch:</p>
<p><a href="mailto:twitter@charlesreid1.com">twitter (at) charlesreid1.com</a></p>
"""

ATTRIBUTION = ""


# --------------8<---------------------

DISPLAY_PAGES_ON_MENU = False
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
DEFAULT_PAGINATION = False
