![StuffDB](https://raw.github.com/lrvick/stuffdb/master/static/img/stuffdbbanner.png)

# StuffDB #

<http://github.com/lrvick/stuffdb>

## About ##

A tool to make it trivial to use a web browser on a smart phone, tablet, or
PC to digitally attach special instructions, considerations, safety concerns,
notes, or tips about any object in a lab/shop/office environment. Access
to object pages is made available by printable QR code labels.

## Current Features ##

  * Accessible by smart-phones, tablets, or computer browsers
  * Home page takes a user directly to “add a new item” form
  * Upon saving the user is taken to the objects newly created page
  * From a page any user can edit, print, view/restore revisions, or share via email.
  * Labels contain name, QR Code, any safety icons, and a plain-text URL to the object page.

## Requirements ##

  * Python 2.6 - 2.7
  * pip

## Usage / Installation ##

1. Clone stuffdb and modules

    ```bash
    git clone https://github.com/lrvick/stuffdb/
    git submodule update --init
    ```

2. Modify settings.py to your liking

    ```bash
    cd stuffdb
    vim settings.py
    ```

4. Create admin user and initialize database

    ```bash
    python manage.py syndb
    ```

3.  Start StuffDB

    ```bash
    python manage.py runserver 0.0.0.0:8080

    ```

You should now be able to access stuffdb via <http://localhost:8080> to
create your first item.

The admin panel should be accessable with the admin user you just
created via <http://localhost:8080/admin>


## Notes ##

The runserver should only be used for testing/development. For deployment
use please consider using a production-ready server like cherokee or nginx.

This is by no means production-ready code. Do not actually use it in
production unless you wish to be eaten by a grue.

Questions/Comments? Please check us out on IRC via irc://udderweb.com/#uw
