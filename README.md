Schoolr Software for Schools
=========================

What is Schoolr
------------

Schoolr is a Virtual Learning Environment (VLE). Now, there's some pretty good
examples of those out there, but Schoolr is different. We wanted to integrate
every aspect of a school into Schoolr: the website for non-students, parents or
teachers; the schedules for teachers, students, classes and classrooms; the
environment for putting assignments online as well as ways to learn or study on
the web and other tools, like a students-only forum and a project
management system.

Features
--------

### Current features

* News

### Planned features

TODO: Need to make a list.


Installation
------------

### Dependencies

* Python 2.7
* Django 1.3+
* Requests
* BeautifulSoup 4

### Development

To install the Schoolr software on a development server you pretty much just have
to set up Python, Django and edit the `personalsettings.py.ORG` accordingly.
You'll want to copy it and rename the copy to `personalsettings.py`. After that 
you have to edit the following options:

* `ADMINS`
* `URL_ROOT`
* `ROOT_DIR`

Finally, run the following command in the terminal:

    python manage.py syncdb

This will ask you if you want to generate a ton of information, for testing
purposes. The default option will be Yes. If you don't want to generate
anything just type anything else than y and press enter.

Now you can simply start up the server with this command:

    python manage.py runserver

Also, please read BRANCHINGMODEL.md for details on how to work with our branches,
is quite important.

### Production

To set up Schoolr for a production server (like for your school), you're going to
have to edit all the settings in the `personalsettings.py` file. Change your
database settings and set `DEBUG` and `STATIC` to `False`. Also mash some keys
into the `SECRET_KEY` option. Now run the `syncdb` command.

Now for the hard part. Seeing as Django's built-in development server (run from
the `runserver` command) isn't very stable or fast, you'll want to run it with
a *real* HTTP server, like [lighttpd](http://www.lighttpd.net/) or
[Apache](http://httpd.apache.org/) or any other server that supports FastCGI. I
recommend reading the Django docs on
[this subject](https://docs.djangoproject.com/en/dev/howto/deployment/fastcgi/)

