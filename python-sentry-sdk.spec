# Excluded extras/integrations
# Lines below are in `code: comment` format, where `code` is used for
# easier navigation in text editors and linking

# no_ariadne: ariadne not packaged yet
# no_arq: arq not packaged yet
# no_beam: beam not packaged yet
# no_chalice: chalice not packaged yet
# no_clickhouse_driver: clickhouse_driver not packaged yet
# no_gql: gql not packaged yet
# no_huey: huey not packaged yet
# no_loguru: loguru not packaged yet
# no_pyspark: pyspark not packaged yet
# no_quart: quart not packaged yet
# no_sanic: sanic not packaged yet
# no_starlite: starlite not packaged yet
# no_strawberry: strawberry not packaged yet
# no_trytond: trytond not packaged yet

# Conditionally excluded extras
# opentelemetry-experimental requires opentelemetry-contrib libraries of 0.40b0 version
%bcond opentelemetry_experimental %[%{?fedora} >= 40]

%bcond network_tests 0

# TODO:
# sqlalchemy installed during tests causes many failures.
# It is used by sentry_sdk/db/explain_plan/sqlalchemy.py and is optional, drop it.
%bcond sqlalchemy_during_tests 0

%global forgeurl https://github.com/getsentry/sentry-python
Version:        1.39.1
%global tag %{version}
%forgemeta

Name:           python-sentry-sdk
Release:        %autorelease
Summary:        The new Python SDK for Sentry.io
License:        MIT
URL:            https://sentry.io/for/python/
Source0:        %{forgesource}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(botocore)
BuildRequires:  python3dist(certifi)
BuildRequires:  python3dist(djangorestframework)
BuildRequires:  python3dist(gevent)
BuildRequires:  python3dist(graphene)
BuildRequires:  python3dist(jsonschema)
BuildRequires:  python3dist(protobuf)
BuildRequires:  python3dist(psycopg)
BuildRequires:  python3dist(pyramid)
BuildRequires:  python3dist(pysocks)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-aiohttp)
BuildRequires:  python3dist(pytest-asyncio)
BuildRequires:  python3dist(pytest-django)
BuildRequires:  python3dist(pytest-forked)
BuildRequires:  python3dist(pytest-localserver)
BuildRequires:  python3dist(python-multipart)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(responses)
BuildRequires:  python3dist(wheel)
%if %{with network_tests}
BuildRequires:  python3dist(boto3)
BuildRequires:  python3dist(httpx)
BuildRequires:  python3dist(pytest-httpx)
%endif

# For re-generating protobuf bindings
BuildRequires:  protobuf-compiler

%global _description %{expand:
Python Error and Performance Monitoring. Actionable insights to resolve Python
performance bottlenecks and errors. See the full picture of any Python exception
so you can diagnose, fix, and optimize performance in the Python debugging
process.}

%description %_description

%package -n python3-sentry-sdk
Summary:        %{summary}

%description -n python3-sentry-sdk %_description

%global extras_excluded %{shrink:
  arq
  beam
  chalice
  clickhouse-driver
  huey
  loguru
  %{!?with_opentelemetry_experimental:opentelemetry-experimental}
  pyspark
  quart
  sanic
  starlite
  %{nil}}

%global extras %{shrink:
  aiohttp
  asyncpg
  bottle
  celery
  django
  falcon
  fastapi
  flask
  grpcio
  httpx
  opentelemetry
  %{?with_opentelemetry_experimental:opentelemetry-experimental}
  pure_eval
  pymongo
  rq
  sqlalchemy
  starlette
  tornado
  %{nil}}

%define extras_csv %{expand:%(echo %{extras} | sed "s/ /,/g")}

%pyproject_extras_subpkg -n python3-sentry-sdk %{extras}


%prep
%forgeautosetup

# Verify all extras defined against setup.py
defined_extra=$(echo "%extras_excluded" "%extras" | xargs -n1 | sort -u)
setup_py_extra=$(cat setup.py | sed -n '/extras_require/,/}/p' | sed 's/    //g' | sed '$ s/.$/\nprint("\\n".join(extras_require))/' | python3 -)
diff <(echo "$defined_extra") <(echo "$setup_py_extra")

%generate_buildrequires
%pyproject_buildrequires -x %{extras_csv}


%build
# Re-generate the protobuf bindings for compatibility with the packaged
# protobuf version.
pushd tests/integrations/grpc/protos/
protoc --python_out="${PWD}" grpc_test_service.proto
popd

%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files sentry_sdk


%check
# Import check
skip_import_check="${skip_import_check-} -e sentry_sdk.integrations.ariadne"  # no_ariadne
skip_import_check="${skip_import_check-} -e sentry_sdk.integrations.arq"  # no_arq
skip_import_check="${skip_import_check-} -e sentry_sdk.integrations.chalice"  # no_chalice
skip_import_check="${skip_import_check-} -e sentry_sdk.integrations.clickhouse_driver"  # no_clickhouse_driver
skip_import_check="${skip_import_check-} -e sentry_sdk.integrations.gql"  # no_gql
skip_import_check="${skip_import_check-} -e sentry_sdk.integrations.huey"  # no_huey
skip_import_check="${skip_import_check-} -e sentry_sdk.integrations.loguru"  # no_loguru
skip_import_check="${skip_import_check-} -e sentry_sdk.integrations.quart"  # no_quart
skip_import_check="${skip_import_check-} -e sentry_sdk.integrations.sanic"  # no_sanic
skip_import_check="${skip_import_check-} -e sentry_sdk.integrations.starlite"  # no_starlite
skip_import_check="${skip_import_check-} -e sentry_sdk.integrations.strawberry"  # no_strawberry
skip_import_check="${skip_import_check-} -e sentry_sdk.integrations.trytond"  # no_trytond

%{!?with_opentelemetry_experimental:skip_import_check="${skip_import_check-} -e sentry_sdk.integrations.opentelemetry.integration"}

%pyproject_check_import ${skip_import_check}


# Tests

# Deselect/ignore:

# not in tox.ini, probably broken
ignore="${ignore-} --ignore=tests/integrations/wsgi"

# python 2 only
deselect="${deselect-} --deselect=tests/integrations/threading/test_threading.py::test_wrapper_attributes_no_qualname"

# python 3.7 only
ignore="${ignore-} --ignore=tests/integrations/gcp"

# require network
%if %{without network_tests}
deselect="${deselect-} --deselect=tests/integrations/requests/test_requests.py::test_omit_url_data_if_parsing_fails"
deselect="${deselect-} --deselect=tests/integrations/requests/test_requests.py::test_crumb_capture"
ignore="${ignore-} --ignore=tests/integrations/boto3"
ignore="${ignore-} --ignore=tests/integrations/httpx"
ignore="${ignore-} --ignore=tests/integrations/socket"
%endif
# TODO: investigate
ignore="${ignore-} --ignore=tests/integrations/fastapi"
ignore="${ignore-} --ignore=tests/integrations/httpx"
# require credentials
ignore="${ignore-} --ignore=tests/integrations/aws_lambda/"

# require a local PostgreSQL instance running
ignore="${ignore-} --ignore=tests/integrations/asyncpg"

# testing suite relies on the test to be executed in clean env
deselect="${deselect-} --deselect=tests/test_basics.py::test_auto_enabling_integrations_catches_import_error"

# currently will always fail: there is no env vars or git repository
deselect="${deselect-} --deselect=tests/test_utils.py::test_default_release"

# tests cannot be run during Fedora build because of the version of pytest:
#    https://github.com/pytest-dev/pytest/issues/9621
#    https://github.com/pytest-dev/pytest-forked/issues/67
deselect="${deselect-} --deselect=tests/utils/test_contextvars.py"

# TODO: relies on django testing, incompatible with pytest macro (see above)
deselect="${deselect-} --deselect=tests/test_transport.py::test_transport_works"
ignore="${ignore-} --ignore=tests/integrations/django"

# async_asgi_testclient is unpackaged yet
ignore="${ignore-} --ignore=tests/integrations/asgi"

# fakeredis is unpackaged yet
deselect="${deselect-} --deselect=tests/test_basics.py::test_redis_disabled_when_not_installed"
ignore="${ignore-} --ignore=tests/integrations/redis"
ignore="${ignore-} --ignore=tests/integrations/rq"

# graphene is too old (min version: 3.3)
ignore="${ignore-} --ignore=tests/integrations/graphene"

# mockupdb is unpackaged because it appears unmaintained
ignore="${ignore-} --ignore=tests/integrations/pymongo"

# protobuf is too old
ignore="${ignore-} --ignore=tests/integrations/grpc"

# werkzeug is too new (version < 2.1.0)
ignore="${ignore-} --ignore=tests/integrations/pyramid"

# newrelic is unpackaged yet
deselect="${deselect-} --deselect=tests/integrations/celery/test_celery.py::test_newrelic_interference"

# rediscluster is unpackaged yet
ignore="${ignore-} --ignore=tests/integrations/rediscluster"

# werkzeug in Fedora 38 is too new, see: https://github.com/getsentry/sentry-python/issues/1398
ignore="${ignore-} --ignore=tests/integrations/bottle"
ignore="${ignore-} --ignore=tests/integrations/flask"

# disabled extras/integrations
ignore="${ignore-} --ignore=tests/integrations/ariadne"  # no_ariadne
ignore="${ignore-} --ignore=tests/integrations/arq"  # no_arq
ignore="${ignore-} --ignore=tests/integrations/beam"  # no_beam
ignore="${ignore-} --ignore=tests/integrations/chalice"  # no_chalice
ignore="${ignore-} --ignore=tests/integrations/clickhouse_driver"  # no_clickhouse_driver
ignore="${ignore-} --ignore=tests/integrations/gql"  # no_gql
ignore="${ignore-} --ignore=tests/integrations/huey"  # no_huey
ignore="${ignore-} --ignore=tests/integrations/loguru"  # no_loguru
ignore="${ignore-} --ignore=tests/integrations/spark"  # no_pyspark
ignore="${ignore-} --ignore=tests/integrations/quart"  # no_quart
ignore="${ignore-} --ignore=tests/integrations/sanic"  # no_sanic
ignore="${ignore-} --ignore=tests/integrations/starlite"  # no_starlite
ignore="${ignore-} --ignore=tests/integrations/strawberry"  # no_strawberry
ignore="${ignore-} --ignore=tests/integrations/trytond"  # no_trytond

ignore="${ignore-} %{!?with_opentelemetry_experimental:--ignore=tests/integrations/opentelemetry/test_experimental.py}"

# Make django testing separate:
# pytest-django cannot find manage.py, since the layout is custom:
# https://github.com/getsentry/sentry-python/blob/1.39.1/tests/integrations/django/myapp/manage.py
# is too deep inside, so it expects manual setting of PYTHONPATH:
# https://pytest-django.readthedocs.io/en/latest/managing_python_path.html
# If we add . to PYTHONPATH for all tests, how can we be sure that packaged library works fine (we are testing sources)?
sed -i 's/\[pytest\]/[pytest]\ndjango_find_project = false/' pytest.ini
PYTHONPATH=. pytest -rsx -s --durations=5 tests/integrations/django
sed -i '/django_find_project =/D' pytest.ini
sed -i '/DJANGO_SETTINGS_MODULE =/D' pytest.ini

%if %{without sqlalchemy_during_tests}
# Test sqlalchemy separately
%pytest -rsx -s --durations=5 tests/integrations/sqlalchemy

# Make `import sqlalchemy` fail
echo "raise ImportError()" > sqlalchemy.py

ignore="${ignore-} --ignore=tests/integrations/sqlalchemy"
%endif

%pytest -rsx -s --durations=5 tests/ ${deselect-} ${ignore-}

%files -n python3-sentry-sdk -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
