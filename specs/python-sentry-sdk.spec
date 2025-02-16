# Excluded extras/integrations
# The lines below are in `code: comment` format, where `code` is used for
# easier navigation in text editors and for linking.

# no_anthropic: anthropic is not packaged.
# no_ariadne: ariadne is not packaged.
# no_arq: arq is not packaged.
# no_beam: beam is not packaged.
# no_celery_redbeat: celery-redbeat is not packaged.
# no_chalice: chalice is not packaged.
# no_clickhouse_driver: clickhouse_driver is not packaged.
# no_cohere: cohere is not packaged.
# no_dramatiq: dramatiq is not packaged.
# no_fakeredis: fakeredis is not packaged.
# no_gql: gql is not packaged.
# no_httpcore_http2: httpcore[http2] is not packaged.
# no_huey: huey is not packaged.
# no_huggingface_hub: huggingface_hub is not packaged.
# no_langchain: langchain is not packaged.
# no_launchdarkly: launchdarkly is not packaged.
# no_litestar: litestar is not packaged.
# no_loguru: loguru is not packaged.
# no_mockupdb: mockupdb is not packaged. It is unmaintained: https://github.com/mongodb-labs/mongo-mockup-db.
# no_newrelic: newrelic is not packaged.
# no_openai: openai is not packaged.
# no_openfeature: openfeature is not packaged.
# no_opentelemetry: opentelemetry-distro is not packaged anymore.
# no_potel: opentelemetry-experimental is not packaged.
# no_pyspark: pyspark is not packaged.
# no_quart: quart is not packaged.
# no_ray: ray is not packaged.
# no_sanic: sanic is not packaged.
# no_starlite: starlite is not packaged.
# no_strawberry: strawberry is not packaged.
# no_trytond: trytond is not packaged.
# no_unleash: UnleashClient is not packaged.

# old_graphene: graphene in Fedora 41 is too old (Sentry SDK wants 3.3, Fedora 41 has 3.0b6).
# new_werkzeug: werkzeug in Fedora 41 is too new (Sentry SDK wants < 2.1.0, Fedora 41 has 3.0.3).
#   https://github.com/getsentry/sentry-python/issues/1398

%bcond tests 1
%bcond network_tests 0

%global forgeurl https://github.com/getsentry/sentry-python
Version:        2.21.0
%global tag %{version}
%forgemeta

Name:           python-sentry-sdk
Release:        %autorelease
Summary:        The new Python SDK for Sentry.io
License:        MIT
URL:            https://sentry.io/for/python/
Source0:        %{forgesource}
# Downstream-only: unpin virtualenv
#
# Upstream wants a old virtualenv to allow an old pip for compatibility
# with old celery and httpx, but we must work with what we have.
Patch0:         0001-Downstream-only-unpin-virtualenv.patch

# Downstream-only: add django.contrib.admin to INSTALLED_APPS
#
# In contrast with upstream, tox environment pyX.XX-gevent is executed
# with django and djangorestframework installed. djangorestframework
# imports django.contrib.admindocs which in turn imports
# django.contrib.admin:
# https://github.com/encode/django-rest-framework/blob/c7a7eae551528b6887614df816c8a26df70272d6/rest_framework/schemas/generators.py#L10C6-L10C30
# https://github.com/django/django/blame/2d4add11fd57b05f7ea48e8b3e89e743c9871aa3/django/contrib/admindocs/views.py#L7
# Then, when gevent.monkey.patch_all is called, DefaultAdminSite._setup
# tries to get config for admin app, which is not present in sentry's
# testing suite app:
# https://github.com/django/django/blob/2d4add11fd57b05f7ea48e8b3e89e743c9871aa3/django/contrib/admin/sites.py#L605
# The easiest option is to add it there.
Patch1:         0002-Add-django.contrib.admin-to-INSTALLED_APPS-to-fix-te.patch

# Downstream-only: remove `propagate_traces` deprecation warning from celery
# integration, as it causes many tests to fail (celery is pre-installed 
# because of presence in tox env, while testing in upstream for all tox envs,
# except one, is celery-free).
Patch2:         0003-Remove-propagate_traces-deprecation-warning.patch

BuildArch:      noarch
BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  postgresql-test-rpm-macros
BuildRequires:  python3dist(botocore)
BuildRequires:  python3dist(certifi)
BuildRequires:  python3dist(djangorestframework)
BuildRequires:  python3dist(gevent)
BuildRequires:  python3dist(graphene)
BuildRequires:  python3dist(jsonschema)
BuildRequires:  python3dist(protobuf)
BuildRequires:  python3dist(psycopg2)
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
BuildRequires:  python3dist(typer)
BuildRequires:  python3dist(wheel)
%if %{with network_tests}
BuildRequires:  python3dist(boto3)
BuildRequires:  python3dist(httpx)
BuildRequires:  python3dist(pytest-httpx)
%endif
BuildRequires:  redis
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

%global default_toxenv py%{python3_version}

# List of names of extras & toxenvs included
%global components %{shrink:
  aiohttp
  asyncpg
  celery
  django
  fastapi
  falcon
  pure_eval
  sqlalchemy
  starlette
  tornado
  %{nil}}

# List of names of extras & toxenvs excluded
# anthropic: no_anthropic
# arq: no_arq
# beam: no_beam
# chalice: no_chalice
# huey: no_huey
# huggingface_hub: no_huggingface_hub
# langchain: no_langchain
# launchdarkly: no_launchdarkly
# litestar: no_litestar
# loguru: no_loguru
# openai: no_openai
# openfeature: no_openfeature
# opentelemetry: no_opentelemetry
# quart: no_quart
# sanic: no_sanic
# starlite: no_starlite
# unleash: no_unleash
%global components_excluded %{shrink:
  anthropic
  arq
  beam
  chalice
  huey
  huggingface_hub
  langchain
  launchdarkly
  loguru
  litestar
  openai
  openfeature
  opentelemetry
  quart
  sanic
  starlite
  unleash
  %{nil}}

# List of names of extras included (if not present in components)
%global extras %{shrink:
  %{components}
  bottle
  flask
  grpcio
  httpx
  pymongo
  rq
  %{nil}}

# List of names of extras excluded (if not present in components_excluded)
# celery-redbeat: no_celery_redbeat
# clickhouse-driver: no_clickhouse_driver
# http2: no_httpcore_http2
# pyspark: no_pyspark
# opentelemetry-experimental: no_opentelemetry
%global extras_excluded %{shrink:
  %{components_excluded}
  celery-redbeat
  clickhouse-driver
  http2
  pyspark
  opentelemetry-experimental
  %{nil}}

%define toxenvs_by_components %{expand:%(echo %{components} | sed "s/^/%{toxenv}-/;s/ / %{toxenv}-/g")}

# List of names of toxenvs included (if not present in components)
%global toxenvs %{shrink:
  %{toxenvs_by_components}
  %{toxenv}-common
  %{toxenv}-cloud_resource_context
  %{toxenv}-gevent
  %{toxenv}-grpc
  %{toxenv}-typer
  %{nil}
}

%define toxenvs_excluded_by_components %{expand:%(echo %{components_excluded} | sed "s/^/%{toxenv}-/;s/ / %{toxenv}-/g")}

# List of names of toxenvs excluded (if not present in components_excluded)
# ariadne: no_ariadne
# asgi: async_asgi_testclient is unpackaged yet
# aws_lambda: aws_lambda requires credentials
# boto3: require network
# bottle: new_werkzeug
# clickhouse_driver: no_clickhouse_driver
# cohere: no_cohere
# dramatiq: no_dramatiq
# flask: new_werkzeug
# gcp: python 3.7 only
# gql: no_gql
# graphene: old_graphene
# httpx: require network
# potel: no_potel
# pymongo: no_mockupdb
# pyramid: new_werkzeug
# ray: no_ray
# redis: no_fakeredis
# redis_py_cluster_legacy: no_fakeredis
# requests: require network
# rq: no_fakeredis
# socket: require network
# spark: no_pyspark
# starberry: no_strawberry
# trytond: no_trytond
%global toxenvs_excluded %{shrink:
  %{toxenvs_excluded_by_components}
  %{toxenv}-ariadne
  %{toxenv}-asgi
  %{toxenv}-aws_lambda
  %{toxenv}-boto3
  %{toxenv}-bottle
  %{toxenv}-clickhouse_driver
  %{toxenv}-cohere
  %{toxenv}-dramatiq
  %{toxenv}-flask
  %{toxenv}-gcp
  %{toxenv}-gql
  %{toxenv}-graphene
  %{toxenv}-httpx
  %{toxenv}-potel
  %{toxenv}-pymongo
  %{toxenv}-pyramid
  %{toxenv}-ray
  %{toxenv}-redis
  %{toxenv}-redis_py_cluster_legacy
  %{toxenv}-rq
  %{toxenv}-requests
  %{toxenv}-socket
  %{toxenv}-spark
  %{toxenv}-strawberry
  %{toxenv}-trytond
  %{nil}}

%define toxenvs_csv %{expand:%(echo %{toxenvs} | sed "s/ /,/g")}

%define extras_csv %{expand:%(echo %{extras} | sed "s/ /,/g")}

%pyproject_extras_subpkg -n python3-sentry-sdk %{extras}


%prep
%forgeautosetup -p1

# Verify that all extras are defined against setup.py.
defined_extra=$(echo "%extras_excluded" "%extras" | xargs -n1 | sort -u)
setup_py_extra=$(cat setup.py | sed -n '/extras_require/,/}/p' | sed 's/    //g' | sed '$ s/.$/\nprint("\\n".join(extras_require))/' | python3 -)
diff <(echo "$defined_extra" | sed "s/_/-/g") <(echo "$setup_py_extra" | sed "s/_/-/g")

sed -r -i 's/psycopg2-binary/psycopg2/' tox.ini

# Unpin all test dependencies to make the installation happen.
sed -r -i 's/(pytest)<7.*/\1/' tox.ini
sed -r -i 's/(Werkzeug)<2\.1\.0/\1/' tox.ini
sed -r -i 's/(gevent)>=22\.10\.0, <22\.11\.0/\1/' tox.ini
sed -r -i 's/(anyio)<4\.0\.0/\1/' tox.ini

# no_newrelic
sed -r -i '/(newrelic)/d' tox.ini

# These Python packages needed for linting are not packaged.
sed -r -i '/(mypy-protobuf)/d' tox.ini
sed -r -i '/(types-protobuf)/d' tox.ini

# no_httpcore_http2
sed -r -i '/(httpcore\[http2\])/d' requirements-testing.txt

%generate_buildrequires
%pyproject_buildrequires -x %{extras_csv} -e %{toxenvs_csv}


%build
# Re-generate the protobuf bindings for compatibility with the packaged
# protobuf version.
pushd tests/integrations/grpc/protos/
protoc --python_out="${PWD}/.." grpc_test_service.proto
popd

%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files sentry_sdk


%check
# Check imports.
skip_import_check="${skip_import_check-} -e sentry_sdk.integrations.anthropic"  # no_anthropic
skip_import_check="${skip_import_check-} -e sentry_sdk.integrations.ariadne"  # no_ariadne
skip_import_check="${skip_import_check-} -e sentry_sdk.integrations.arq"  # no_arq
skip_import_check="${skip_import_check-} -e sentry_sdk.integrations.celery_redbeat"  # no_celery_redbeat
skip_import_check="${skip_import_check-} -e sentry_sdk.integrations.chalice"  # no_chalice
skip_import_check="${skip_import_check-} -e sentry_sdk.integrations.clickhouse_driver"  # no_clickhouse_driver
skip_import_check="${skip_import_check-} -e sentry_sdk.integrations.cohere"  # no_cohere
skip_import_check="${skip_import_check-} -e sentry_sdk.integrations.dramatiq"  # no_dramatiq
skip_import_check="${skip_import_check-} -e sentry_sdk.integrations.gql"  # no_gql
skip_import_check="${skip_import_check-} -e sentry_sdk.integrations.huey"  # no_huey
skip_import_check="${skip_import_check-} -e sentry_sdk.integrations.huggingface_hub"  # no_huggingface_hub
skip_import_check="${skip_import_check-} -e sentry_sdk.integrations.langchain"  # no_langchain
skip_import_check="${skip_import_check-} -e sentry_sdk.integrations.launchdarkly"  # no_launchdarkly
skip_import_check="${skip_import_check-} -e sentry_sdk.integrations.litestar"  # no_litestar
skip_import_check="${skip_import_check-} -e sentry_sdk.integrations.loguru"  # no_loguru
skip_import_check="${skip_import_check-} -e sentry_sdk.integrations.openai"  # no_openai
skip_import_check="${skip_import_check-} -e sentry_sdk.integrations.openfeature"  # no_openfeature
skip_import_check="${skip_import_check-} -e sentry_sdk.integrations.opentelemetry*"  # no_opentelemetry
skip_import_check="${skip_import_check-} -e sentry_sdk.integrations.quart"  # no_quart
skip_import_check="${skip_import_check-} -e sentry_sdk.integrations.ray"  # no_ray
skip_import_check="${skip_import_check-} -e sentry_sdk.integrations.sanic"  # no_sanic
skip_import_check="${skip_import_check-} -e sentry_sdk.integrations.starlite"  # no_starlite
skip_import_check="${skip_import_check-} -e sentry_sdk.integrations.strawberry"  # no_strawberry
skip_import_check="${skip_import_check-} -e sentry_sdk.integrations.trytond"  # no_trytond
skip_import_check="${skip_import_check-} -e sentry_sdk.integrations.unleash"  # no_unleash

%if %{without tests}
skip_import_check="${skip_import_check-} -e sentry_sdk.db.explain_plan.sqlalchemy"
skip_import_check="${skip_import_check-} -e sentry_sdk.integrations.aiohttp"
skip_import_check="${skip_import_check-} -e sentry_sdk.integrations.asyncpg"
skip_import_check="${skip_import_check-} -e sentry_sdk.integrations.boto3"
skip_import_check="${skip_import_check-} -e sentry_sdk.integrations.bottle"
skip_import_check="${skip_import_check-} -e sentry_sdk.integrations.celery*"
skip_import_check="${skip_import_check-} -e sentry_sdk.integrations.django*"
skip_import_check="${skip_import_check-} -e sentry_sdk.integrations.executing"
skip_import_check="${skip_import_check-} -e sentry_sdk.integrations.falcon"
skip_import_check="${skip_import_check-} -e sentry_sdk.integrations.fastapi"
skip_import_check="${skip_import_check-} -e sentry_sdk.integrations.flask"
skip_import_check="${skip_import_check-} -e sentry_sdk.integrations.graphene"
skip_import_check="${skip_import_check-} -e sentry_sdk.integrations.grpc*"
skip_import_check="${skip_import_check-} -e sentry_sdk.integrations.httpx"
skip_import_check="${skip_import_check-} -e sentry_sdk.integrations.pure_eval"
skip_import_check="${skip_import_check-} -e sentry_sdk.integrations.pymongo"
skip_import_check="${skip_import_check-} -e sentry_sdk.integrations.pyramid"
skip_import_check="${skip_import_check-} -e sentry_sdk.integrations.rq"
skip_import_check="${skip_import_check-} -e sentry_sdk.integrations.sqlalchemy"
skip_import_check="${skip_import_check-} -e sentry_sdk.integrations.starlette"
skip_import_check="${skip_import_check-} -e sentry_sdk.integrations.tornado"
%endif

%pyproject_check_import ${skip_import_check}

%if %{with tests}
# Tests

# Deselect/ignore tests.

# These tests are not in tox.ini, and they are probably broken.
ignore="${ignore-} --ignore=tests/integrations/wsgi"

# In tox.ini, this environment is python 3.7 only.
#   https://github.com/getsentry/sentry-python/blob/2.7.1/tox.ini#L127
ignore="${ignore-} --ignore=tests/integrations/gcp"

# These tests require network.
%if %{without network_tests}
deselect="${deselect-} --deselect=tests/integrations/django/test_basic.py::test_cache_spans_decorator"
deselect="${deselect-} --deselect=tests/integrations/django/test_basic.py::test_cache_spans_disabled_decorator"
deselect="${deselect-} --deselect=tests/integrations/django/test_basic.py::test_cache_spans_disabled_middleware"
deselect="${deselect-} --deselect=tests/integrations/django/test_basic.py::test_cache_spans_disabled_templatetag"
deselect="${deselect-} --deselect=tests/integrations/django/test_basic.py::test_cache_spans_middleware"
deselect="${deselect-} --deselect=tests/integrations/django/test_basic.py::test_cache_spans_templatetag"
deselect="${deselect-} --deselect=tests/integrations/django/test_basic.py::test_ensures_spotlight_middleware_when_spotlight_is_enabled"
deselect="${deselect-} --deselect=tests/integrations/aiohttp/test_aiohttp.py::test_span_origin"
deselect="${deselect-} --deselect=tests/integrations/requests/test_requests.py::test_omit_url_data_if_parsing_fails"
deselect="${deselect-} --deselect=tests/integrations/requests/test_requests.py::test_crumb_capture"
deselect="${deselect-} --deselect=tests/integrations/stdlib/test_httplib.py::test_span_origin"
deselect="${deselect-} --deselect=tests/integrations/stdlib/test_httplib.py::test_http_timeout"
ignore="${ignore-} --ignore=tests/integrations/boto3"
ignore="${ignore-} --ignore=tests/integrations/httpx"
ignore="${ignore-} --ignore=tests/integrations/socket"
%endif

# These tests require credentials.
#   https://github.com/getsentry/sentry-python/blob/2.7.1/tests/integrations/aws_lambda/test_aws.py#L6
ignore="${ignore-} --ignore=tests/integrations/aws_lambda/"

# The testing suite relies on executing the test in a clean environment.
deselect="${deselect-} --deselect=tests/test_basics.py::test_auto_enabling_integrations_catches_import_error"

# Currently, this test will always fail: there is no env vars or git repository.
deselect="${deselect-} --deselect=tests/test_utils.py::test_default_release"

# These tests cannot be run during the Fedora build due to the version of pytest being used.
#   https://github.com/pytest-dev/pytest/issues/9621
#   https://github.com/pytest-dev/pytest-forked/issues/67
deselect="${deselect-} --deselect=tests/utils/test_contextvars.py"

# no_fakeredis
deselect="${deselect-} --deselect=tests/test_basics.py::test_redis_disabled_when_not_installed"
ignore="${ignore-} --ignore=tests/integrations/redis"
ignore="${ignore-} --ignore=tests/integrations/rq"

# old_graphene
ignore="${ignore-} --ignore=tests/integrations/graphene"

# no_mockupdb
ignore="${ignore-} --ignore=tests/integrations/pymongo"

# no_newrelic
deselect="${deselect-} --deselect=tests/integrations/celery/test_celery.py::test_newrelic_interference"

# new_werkzeug
ignore="${ignore-} --ignore=tests/integrations/bottle"
ignore="${ignore-} --ignore=tests/integrations/flask"
ignore="${ignore-} --ignore=tests/integrations/pyramid"

# These tests are time-dependent and may fail due to hardcoded delays.
# Deselect them until they are reimplemented using time mocking.
#   https://bugzilla.redhat.com/show_bug.cgi?id=2265822
#   https://github.com/getsentry/sentry-python/issues/3335
deselect="${deselect-} --deselect=tests/profiler/test_continuous_profiler.py::test_continuous_profiler_auto_start_and_manual_stop"
deselect="${deselect-} --deselect=tests/profiler/test_continuous_profiler.py::test_continuous_profiler_manual_start_and_stop"
deselect="${deselect-} --deselect=tests/profiler/test_transaction_profiler.py::test_profile_captured"
deselect="${deselect-} --deselect=tests/test_metrics.py::test_timing"
deselect="${deselect-} --deselect=tests/test_metrics.py::test_timing_decorator"

# These tests depends on http2 extra for httpcore Python package.
# https://src.fedoraproject.org/rpms/python-httpcore/pull-request/7
# has been merged, but update is still not published.
deselect="${deselect-} --deselect=tests/test_client.py::test_proxy"
deselect="${deselect-} --deselect=tests/test_transport.py::test_two_way_ssl_authentication"
deselect="${deselect-} --deselect=tests/test_transport.py::test_http2_with_https_dsn"
deselect="${deselect-} --deselect=tests/test_transport.py::test_no_http2_with_http_dsn"

defined_toxenvs=$(echo "%toxenvs_excluded" "%toxenvs" | xargs -n1 | sort -u)
tox_ini_toxenvs=$(cat tox.ini | sed -r -n 's/[[:blank:]]*(.*):[[:blank:]]*TESTPATH=.*/%{default_toxenv}-\1/p' | xargs -n1 | sort -u)
diff <(echo "$defined_toxenvs") <(echo "$tox_ini_toxenvs")

# Start redis-server, which is required for some integration tests.
%{_bindir}/redis-server --bind 127.0.0.1 --port 6379 &
REDIS_SERVER_PID=$!

# Start postresql-server, which is required for some integrations tests.
%postgresql_tests_run
export SENTRY_PYTHON_TEST_POSTGRES_USER=sentry_test_user
export SENTRY_PYTHON_TEST_POSTGRES_PASSWORD=sentry_test_password
export SENTRY_PYTHON_TEST_POSTGRES_NAME=sentry_test_name
export SENTRY_PYTHON_TEST_POSTGRES_PORT=$PGTESTS_PORT
psql -c "CREATE ROLE $SENTRY_PYTHON_TEST_POSTGRES_USER WITH LOGIN SUPERUSER PASSWORD '$SENTRY_PYTHON_TEST_POSTGRES_PASSWORD';"
createdb $SENTRY_PYTHON_TEST_POSTGRES_NAME --owner $SENTRY_PYTHON_TEST_POSTGRES_USER

DJANGO_SETTINGS_MODULE=tests.integrations.django.myapp.settings %tox -e %{toxenvs_csv} -- -- ${deselect-} ${ignore-}

# Terminate redis-server.
%{_bindir}/redis-cli shutdown nosave force now
# Wait for redis-server termination (the command above is asynchronous).
wait $REDIS_SERVER_PID
%endif

%files -n python3-sentry-sdk -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
