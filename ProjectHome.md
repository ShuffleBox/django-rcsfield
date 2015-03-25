### Looking for a new maintainer ###

**I'm looking for a new maintainer for django-rcsfield. If you are interested in taking over the project please send me an e-mail to arne -at- rcs4u.de**

### Versionize Content of Django Model-Fields ###


`django-rcsfield` is a field (like `models.TextField`) for the Django web framework which - under the hood - versionizes its content. The 'rcs' in the name is short for **revision control system**.

The current implementation works with:

  * [Bazaar](http://www.bazaar-vcs.org)
  * Git (via GitPython)
  * SVN
  * Mercurial (hg)

An abstration layer makes implementing additional backends very easy.

Currently it handles the following: On running `manage.py syncdb` it checks out or creates (depending on the backend) an initial working copy. If a model has an `RcsTextField`  contents of this field are versionized in the repository.

To make it possible to fetch older versions a djangonic API is available. Plese look at the QuickStart Page for an example how the lookup API is implemented.

### Documentation ###

Please read the README file at: http://django-rcsfield.googlecode.com/svn/trunk/README

### News ###
| [r90](https://code.google.com/p/django-rcsfield/source/detail?r=90) | added a backend for mercurial (hg) |
|:--------------------------------------------------------------------|:-----------------------------------|
| [r80](https://code.google.com/p/django-rcsfield/source/detail?r=80) | added an example wiki which shows how to use rcsfield and improved documentation. |
| [r76](https://code.google.com/p/django-rcsfield/source/detail?r=76) | We now have some basic unittests :) |
| [r64](https://code.google.com/p/django-rcsfield/source/detail?r=64) | The output of the historytrail templatetag can now be changed in the template `rcsfield/includes/historytrail.html` |
| [r62](https://code.google.com/p/django-rcsfield/source/detail?r=62) | Added a RcsJsonField to store and versionize arbitrary data structures in json format (as long as they are handled by the default simplejson encoder.) |
| [r58](https://code.google.com/p/django-rcsfield/source/detail?r=58) | We now have a GIT backend (thanks to Jannis Leidel). |

### ohloh stats ###

&lt;wiki:gadget url="http://www.ohloh.net/p/11444/widgets/project\_basic\_stats.xml" height="220"  border="1" /&gt;