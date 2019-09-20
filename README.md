# ContentTrustLab

Laboratory of Content Trust

## Information
1. Python 3
2. Django v2
3. Python virtual environment
4. Microsoft SQL Server with ODBC Driver 17

## Local Installation
1. Install Microsoft ODBC Driver 17 (Windows/Linux/MacOS)

	[https://docs.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-2017](https://docs.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-2017)
2. Clone Git Repository with git client or per terminal
3. Open terminal and go to project directory
4. Configure merge driver for dealing with ``.gitattributes`` or rather the merge strategy:

        git config merge.ours.driver true

5. Install (if needed), and then create, activate Python virtual environment

    [https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

6. Run pip to install all necessary python packages:

        pip3 install -r requirements.pip --exists-action w

7. Get to work! 

## Notes

- The ``settings.py`` is via ``.gitattributes`` under merge strategy to have always different versions in develop and master branch. To hold this construction, **always** merge without fast-forward. Thus, always create a new commit, when you merge the two branches.

- Add all new python packages to ``requirements.pip`` 

- djtrustlab is the main Django project with settings.py, contenttrustlab is the subproject with all the code

- All deploy-configs for gunicorn and nginx are in ``deploy-configs/``

## Deploy

- Project is deployed at master branch via a CI gitlabrunner by ``.gitlab-ci.yml``.

- Password of the db user for the database is provided to ``settings.py`` at the deploy process via the script at ``/var/www/cotenttrustlab/dbkey.sh``.

- The deploy script is exchanging following strings in ``settings.py``
DB NAME, DB USER, DB PASSWORD, STATIC URL & ROOT, MEDIA URL & ROOT

## Links To Know
* Links for deploy
https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04