# django-ban

Django app that adds bans and warnings to the user system.

## Requirements

- [Django messages framework](https://docs.djangoproject.com/en/1.9/ref/contrib/messages/) (optional)

## Installation

- Add `ban` folder to Python path.
- Add `"ban"` to your `INSTALLED_APPS`.
- Add `ban.middleware.BanAuthenticationMiddleware` to `MIDDLEWARE_CLASSES` in your `settings.py`. Make sure you place it AFTER:
    - `django.contrib.auth.middleware.AuthenticationMiddleware`
    - `django.contrib.auth.middleware.SessionAuthenticationMiddleware`
    - `django.contrib.messages.middleware.MessageMiddleware` (if you use it)
    
    Example:
    

    ```
    MIDDLEWARE_CLASSES = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
    
        'ban.middleware.BanAuthenticationMiddleware',
    
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]
    ```

## Usage

### Banning and warning users

You can easily ban or warn users from Django admin panel (auth/user section). You can ban a user permanently or for some period of time (day, week or month).

### Auto-ban for users with many warns

You can also specify a number of warns which is enough to ban a user permanently. To do that, simply add to your settings the following line:


    WARNS_THRESHOLD = 10

### Cleaning up inactive bans

In order to keep your database free from old bans, make sure to run the following command from time to time:


    $  python manage.py clean_inactive_bans

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
