# <img src="/_logos/atlas_orange.svg" alt="aTLAS orange" width="3%" height="3%"> TrustLab

Laboratory of Trust. Latest online version: [http://vsr-dem0.informatik.tu-chemnitz.de/trustlab/](http://vsr-dem0.informatik.tu-chemnitz.de/trustlab/)

## Information
1. Python 3
2. Django v2
3. Python virtual environment
4. Microsoft SQL Server with ODBC Driver 17

## Local Installation
1. Install Microsoft ODBC Driver 17 (Windows/Linux/MacOS)

    [https://docs.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-2017](https://docs.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-2017)
2. Clone Git Repository, including all submodules. (https://git-scm.com/book/en/v2/Git-Tools-Submodules)

3. Configure merge driver for dealing with ``.gitattributes`` or rather the merge strategy:
    ```bash
    git config merge.ours.driver true
    ```

4. Setup pipenv in project root:
    ```bash
    pipenv install
    ```
   ODBC on MAC:
    - If you installed this formula with the registration option (default), you'll need to manually remove
    ``[ODBC Driver 17 for SQL Server]`` section from odbcinst.ini after the formula is uninstalled.
    This can be done by executing:
        ```bash
        odbcinst -u -d -n "ODBC Driver 17 for SQL Server"
        ```
        
5. Modify ``Additional Options`` of your django configuration (for no auto-reload after editing scenario files) with:
    ```bash
    --noreload
    ```

## Run

1. Run aTLAS:
    ```bash
    python manage.py runserver 8000 --noreload
    ```

2. Run at least on supervisor with the included submodule and connect it to aTLAS. (https://github.com/N0omB/aTLAS_host)

## Notes

- The ``settings.py`` is via ``.gitattributes`` under merge strategy to have always different versions in develop and master branch. To hold this construction, **always** merge without fast-forward. Thus, always create a new commit, when you merge the two branches.

- djtrustlab is the main Django project with settings.py, trustlab is the subproject with all the code

- All deploy-configs for daphne and nginx (and depricated gunicorn) are in ``deploy-configs/``

## How To Scenario

- Scenario configurations can be placed in ``trustlab/lab/scenarios``.

- Every scenario configuration file has to end with ``_scenario.py``.

- All scenario parameters require to be the upperCase version of the respective ``Scenario.__init__`` arguments.

- Possible scenario arguments derive from ``Scenario.__init__`` arguments list, where parameters without default value are mandatory for scenario configuration file as well.

- Scenario files require ending with two new line feeds instead of one as described in the python style guide.

## Deploy

- Project is deployed at master branch via a CI gitlabrunner by ``.gitlab-ci.yml``.

- Password of the db user for the database is provided to ``settings.py`` at the deploy process via the script at ``/var/www/trustlab/dbkey.sh``.

- The deploy script is exchanging following strings in ``settings.py``
DB NAME, DB USER, DB PASSWORD, STATIC URL & ROOT, MEDIA URL & ROOT

## Links To Know

* NVD3: Re-usable chart for d3.js \
http://nvd3.org/
* Links for deploy \
https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04
* DEPRICATED mdl-selectfield \
 https://github.com/meyvn/mdl-selectfield
* DEPRICATED Dark MDL CSS Style from CreativeIT \
https://github.com/CreativeIT/material-dashboard-lite http://creativeit.io/material-dashboard-lite/

## For Later

- pip install markdown \- Markdown support for the browsable API.

- pip install pygments \- Add syntax highlighting (to Markdown processing).

- pip install django-filter \- Filtering support in Request via parameter and in REST Framework

- NetworkX for graph structure in backend: https://networkx.github.io/

- NVD3 for graphs and diagrams in frontend: http://nvd3.org/

<!-- Identifiers, in alphabetical order -->
[atlas-logo-orange]: /_logos/atlas_orange.svg


