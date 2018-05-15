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
LINKSBKG='img/splash.jpg'

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

Running `sudo pip install` is insanely dangerous. It is equivalent to giving a complete stranger root access on your machine.  
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

Third, **malicious packages**. People do evil shit, especially when money's involved.

![some men just wanna watch the world burn](img/burn.gif)

<br />
<br />

**How do I change my mindset?**

To install Python packages (even through pip), you must run a setup.py file, at some point in the process.

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

    # 
    # 
    # On The Web
    # 
    # 

    descr += "<h3>Paradise Lost Bot Flock On The Web</h3>"

    # items format:     [ button text,    href url,    fa-icon ]
    items  = [
                ["git.charlesreid1.com/bots/b-ginsberg",  "https://git.charlesreid1.com/bots/b-ginsberg",   "code-fork"],
                ["github.com/charlesreid1/ginsberg",      "https://github.com/charlesreid1/ginsberg",       "github"],
                ["pages.charlesreid1.com/b-ginsberg",     "https://pages.charlesreid1.com/b-ginsberg",      "globe"],
            ]

    for item in items:
        button_text = item[0]
        button_link = item[1]
        button_icon = item[2]

        descr += "<p><a class=\"btn btn-default btn-lg\" href=\"%s\">"%(button_link)
        descr += "<i class=\"fa fa-fw fa-2x fa-%s\"></i> %s"%(button_icon, button_text)
        descr += "</a></p>\n"

    descr += "\n"

    # 
    # 
    # On The Twitter
    # 
    # 

    descr += "<h3>Ginsberg Bot Flock On Twitter</h3>"

    poems = ["america",
             "auntrose",
             "chicago",
             "cosmo",
             "dc",
             "deathfame",
             "deathfronts",
             "ecologue",
             "elegy",
             "fiveam",
             "greyhound",
             "hospital",
             "howl",
             "kaddish",
             "lion",
             "money",
             "organ",
             "sunflower",
             "supermarket"]

    for poem in poems:
        handle = "gbf_%s"%(poem)
        button_text = "@%s"%(handle)
        button_link = "https://twitter.com/%s"%(handle)
        button_icon = "twitter"

        descr += "<p><a class=\"btn btn-default btn-lg\" href=\"%s\">"%(button_link)
        descr += "<i class=\"fa fa-fw fa-2x fa-%s\"></i> %s"%(button_icon, button_text)
        descr += "</a></p>\n"

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

ATTRIBUTION = """
<p style="font-size: 12px;">Header image credit: <a href="https://commons.wikimedia.org/wiki/File:Allen_ginsberg_675.jpg">Wikimedia Commons</a>, photo released under the <a href="https://creativecommons.org/licenses/by-sa/3.0/deed.en">CC BY-SA 3.0</a>

<p style="font-size: 12px;">Links image credit: <a href="https://www.flickr.com/photos/ig_gallery/albums/72157627207393728">John Hopkins</a>, photo &copy; 2018 <a href="https://hoppyx.com/about-hoppy/">Estate of John Hopkins</a>
"""


# --------------8<---------------------

DISPLAY_PAGES_ON_MENU = False
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
DEFAULT_PAGINATION = False
