# Thorgate's Django template (Bootstrap 4 variant)

[![Build status](https://gitlab.com/thorgate-public/django-project-template/badges/master/pipeline.svg)](https://gitlab.com/thorgate-public/django-project-template/commits/master)

[Django](https://www.djangoproject.com/) project template that we use at [Thorgate](https://thorgate.eu).

Best suited for medium-sized and bigger apps that use JavaScript and React for frontend.

See also the [Single-Page Application](https://gitlab.com/thorgate-public/django-project-template/tree/spa)
and [Bootstrap 3](https://gitlab.com/thorgate-public/django-project-template/tree/legacy-docker-bootstrap3) variants.

_(note that the primary repo is in [Gitlab](https://gitlab.com/thorgate-public/django-project-template), with mirror in [Github](https://github.com/thorgate/django-project-template))_


## Features

- Django-based backend

    - [Django](https://www.djangoproject.com/)
    - Separate settings for different environments (local/staging/production)
    - Python 3.6 or later
    - loguru

- Frontend app(webapp) with JavaScript (ES2015), javascript and Sass

    - Latest JavaScript features from [ES2015](https://babeljs.io/docs/learn-es2015/) and beyond, transpiled with
      [Babel](https://babeljs.io/)
    - [Sass](http://sass-lang.com/), [PostCSS](http://postcss.org/) and
      [Autoprefixer](https://github.com/postcss/autoprefixer) for more convenient styling


## Usage

To use this template, first ensure that you have
[Pipenv](https://pipenv.readthedocs.io/en/latest/) `2020.6.2` available.

After that, you should:

1. Install the requirements of the project template by running
    ```
    virtualenv instagram
    ```
2. Activate the virtualenv created by pipenv:
    ```
    source instagram/bin/activate
    ```
3. Navigate to the directory where you'd like to create your project:
    ```
    cd core
    ```

4. Run project:
    ```
    python manage.py  runserver
    ```


See README.md in the generated project for instructions on how to set up your development environment.

