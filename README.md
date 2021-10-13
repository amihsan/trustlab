# <img src="/_logos/atlas_orange.svg" alt="aTLAS orange" width="3%" height="3%"> TrustLab

Laboratory of Trust. Latest online version: [http://vsr-dem0.informatik.tu-chemnitz.de/trustlab/](http://vsr-dem0.informatik.tu-chemnitz.de/trustlab/)

## Information
1. Python 3.7
2. Django v2
3. Local Redis
4. Pipenv or Python virtual environment

## Setup
1. Install Redis https://redis.io/topics/quickstart

2. Clone Git Repository, including all submodules. (https://git-scm.com/book/en/v2/Git-Tools-Submodules)

3. Setup pipenv in project root:
    ```bash
    pipenv install
    ```
        
4. Modify ``Additional Options`` of your django configuration (for no auto-reload after editing scenario files) with:
    ```bash
    --noreload
    ```

6. Install also at least one supervisor. (https://gitlab.hrz.tu-chemnitz.de/vsr/phd/siegert/trustlab_host)

   
## Run

1. Run local Redis server

2. Run aTLAS:
    ```bash
    python manage.py runserver 8000 --noreload
    ```

3. Run at least on supervisor with the included submodule and connect it to aTLAS. (https://github.com/N0omB/aTLAS_host)

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

## Links To Know

* aTLAS Project page \
https://vsr.informatik.tu-chemnitz.de/projects/2020/atlas/

* Latest online prototype \
https://vsr.informatik.tu-chemnitz.de/projects/2020/atlas/demo/

* Host Library Repository and Submodule at `trustlab_host` \
https://gitlab.hrz.tu-chemnitz.de/vsr/phd/siegert/trustlab_host

