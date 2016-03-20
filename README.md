# django-ban

Django app that...

## Installation

- Add `ban` folder to Python path.
- Add `"ban"` to your `INSTALLED_APPS`.

## Usage

...

## Demo

`django-ban` provides a simple demo with example usage. To install it from the console, execute `fab install` command. To run it, type ``fab runserver``.

Of course, to do that you need to have `fabric` installed on your computer.

## Tests

Tests assume that Selenium's ChromeDriver can be found at:
> /usr/bin/chromedriver

It also needs correct permissions. Make sure to run:

    $ sudo chmod a+x /usr/bin/chromedriver

To run all the tests simply type:

    $ fab install
    $ fab testall

## Notes

This package was tested with Python 3.4 and Django 1.8.

## License

MIT

