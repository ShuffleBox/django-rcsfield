# Quick start how-to for django-rcsfield #

Additionally to this page please read the Blog post of Will Larson about setting up django-rcsfield: http://lethain.com/entry/2008/oct/15/setting-up-django-rcsfield/
It describes the available settings variable etc.

In your models.py import the field and optionaly the manager:

```
from rcsfield.fields import RcsTextField
from rcsfield.manager import RevisionManager
```

Then use it in your Model instead of the builtin TextField. Example:

```
class Entry(models.Model):
    title = models.CharField(max_length=50)
    content = RcsTextField()

    objects = RevisionManager()

    class Admin:
        pass
```

Then start the dev server and add some Data via the admin interface. Make multiple edits on your to generate some revisions to play with.

# Some API examples #
```
>>> from example.models import Entry
>>> Entry.objects.get(pk=1)
<Entry: foo>
>>> Entry.objects.get(pk=1).text
'lorem ipsum dolor sit'
>>> Entry.objects.rev(1).get(pk=1).text
''
>>> Entry.objects.rev(2).get(pk=1).text
'test test test'
>>> e = Entry.objects.get(pk=1)
>>> f = Entry.objects.get(pk=2)
>>> e.get_content_revisions()
[8, 7, 6, 4, 2]
>>> f.get_content_revisions()
[5, 3]
```

# An example for the templatetag #

```
{% load historytrail %}

<p>{{ object.content }}</p>

{% historytrail object %}
```