Name:           python-sentry-sdk
Version:        1.29.2
Release:        2%{?dist}
Summary:        The new Python SDK for Sentry.io

License:        MIT
URL:            https://sentry.io/for/python/
Source0:        https://github.com/getsentry/sentry-python/archive/%{version}/sentry-python-%{version}.tar.gz
Patch0:         0001-tests-add-support-for-Python-3.12.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(certifi)
BuildRequires:  python3dist(wheel)
# Use Fedora versions of testing dependencies + pytest instead of pinned versions in upstream + tox
BuildRequires:  python3dist(aiohttp)
BuildRequires:  python3dist(asttokens)
BuildRequires:  python3dist(blinker)
BuildRequires:  python3dist(botocore)
BuildRequires:  python3dist(bottle)
BuildRequires:  python3dist(celery)
BuildRequires:  python3dist(django)
BuildRequires:  python3dist(djangorestframework)
BuildRequires:  python3dist(executing)
BuildRequires:  python3dist(fastapi)
BuildRequires:  python3dist(flask)
BuildRequires:  python3dist(flask-login)
BuildRequires:  python3dist(gevent)
BuildRequires:  python3dist(grpcio)
BuildRequires:  python3dist(httpx)
BuildRequires:  python3dist(jsonschema)
BuildRequires:  python3dist(mock)
BuildRequires:  python3dist(opentelemetry-distro)
BuildRequires:  python3dist(protobuf)
BuildRequires:  python3dist(psycopg2)
BuildRequires:  python3dist(pure-eval)
BuildRequires:  python3dist(pymongo)
BuildRequires:  python3dist(pyramid)
BuildRequires:  python3dist(pyrsistent)
BuildRequires:  python3dist(pysocks)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-aiohttp)
BuildRequires:  python3dist(pytest-asyncio)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(pytest-forked)
BuildRequires:  python3dist(pytest-localserver)
BuildRequires:  python3dist(python-multipart)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(responses)
BuildRequires:  python3dist(rq)
BuildRequires:  python3dist(sqlalchemy)
BuildRequires:  python3dist(starlette)
BuildRequires:  python3dist(tornado)
BuildRequires:  python3dist(werkzeug)

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


# Dependencies for quart, sanic, beam, pyspark, chalice, starlite, huey, arq, loguru extras are not yet in Fedora
# falcon version >= 3.0 is not yet supported => skipping this extra as well
%global _extras %{expand:
  flask
  bottle
  django
  celery
  rq
  aiohttp
  tornado
  sqlalchemy
  pure_eval
  httpx
  starlette
  fastapi
  pymongo
  opentelemetry
  grpcio
}
%pyproject_extras_subpkg -n python3-sentry-sdk %_extras


%prep
%autosetup -p1 -n sentry-python-%{version}


%generate_buildrequires
%pyproject_buildrequires -r


%build
# Re-generate the protobuf bindings for compatibility with the packaged
# protobuf version.
pushd tests/integrations/grpc/
protoc --python_out="${PWD}" grpc_test_service.proto
popd

%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files sentry_sdk


%check
%global _check_import_options %{expand:
  -e sentry_sdk.integrations.arq
  -e sentry_sdk.integrations.chalice
  -e sentry_sdk.integrations.falcon
  -e sentry_sdk.integrations.grpc
  -e sentry_sdk.integrations.grpc.client
  -e sentry_sdk.integrations.grpc.server
  -e sentry_sdk.integrations.huey
  -e sentry_sdk.integrations.loguru
  -e sentry_sdk.integrations.quart
  -e sentry_sdk.integrations.sanic
  -e sentry_sdk.integrations.starlite
  -e sentry_sdk.integrations.trytond
}
%pyproject_check_import %_check_import_options

# Remove old content_type argument from starlette test (not supported in current version of starlette).
sed -i '/content_type=/D' tests/integrations/starlette/test_starlette.py

# Deselect/ignore:
# 1. Network-dependent tests
# 2. Tests which cannot be run during Fedora build because of the version of pytest:
#    https://github.com/pytest-dev/pytest/issues/9621
#    https://github.com/pytest-dev/pytest-forked/issues/67
# 3. django integration tests (django-rest-framework is not available for Fedora 38)
# 4. pymongo integration tests (mockupdb is unpackaged because it appears unmaintained)
# 5. redis and rq integration tests (fakeredis is unpackaged yet)
# 6. bottle, django, and flask integration tests (werkzeug in Fedora 38 is too new, see: https://github.com/getsentry/sentry-python/issues/1398)
# 7. celery & newrelic test (newrelic is unpackaged yet)
# 8. test_auto_enabling_integrations_catches_import_error: testing suite relies on the test to be executed on clean env
%pytest --durations=5 \
  --deselect tests/integrations/asyncio/test_asyncio_py3.py \
  --deselect tests/integrations/celery/test_celery.py::test_newrelic_interference \
  --deselect tests/integrations/requests/test_requests.py::test_crumb_capture \
  --deselect tests/integrations/requests/test_requests.py::test_omit_url_data_if_parsing_fails \
  --deselect tests/integrations/threading/test_threading.py::test_circular_references \
  --deselect tests/test_basics.py::test_auto_enabling_integrations_catches_import_error \
  --deselect tests/test_transport.py::test_transport_works \
  --deselect tests/utils/test_contextvars.py \
  --ignore tests/integrations/arq \
  --ignore tests/integrations/bottle \
  --ignore tests/integrations/django \
  --ignore tests/integrations/flask \
  --ignore tests/integrations/gcp \
  --ignore tests/integrations/httpx \
  --ignore tests/integrations/loguru \
  --ignore tests/integrations/pymongo \
  --ignore tests/integrations/pyramid \
  --ignore tests/integrations/redis \
  --ignore tests/integrations/rq \
  --ignore tests/integrations/socket \
  --ignore tests/integrations/wsgi


%files -n python3-sentry-sdk -f %{pyproject_files}
%doc README.md


%changelog
* Thu Oct 12 2023 Miro Hrončok <mhroncok@redhat.com> - 1.29.2-2
- Explicitly BuildRequire python3dist(pysocks), as the tests fail without it

* Mon Sep 04 2023 Roman Inflianskas <rominf@aiven.io> - 1.29.2-1
- Update to 1.29.2 (fedora#2222617)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.28.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jul 13 2023 Roman Inflianskas <rominf@aiven.io> - 1.28.0-1
- Update to 1.28.0 (fedora#2220929)
- Tests: add support for Python 3.12 (fedora#2220496)

* Thu Jul 13 2023 Python Maint <python-maint@redhat.com> - 1.27.0-2
- Rebuilt for Python 3.12

* Wed Jul 05 2023 Roman Inflianskas <rominf@aiven.io> - 1.27.0-1
- Update to 1.27.0 (resolve rhbz#2219588)

* Mon Jun 26 2023 Roman Inflianskas <rominf@aiven.io> - 1.26.0-1
- Update to 1.26.0 (resolve rhbz#2216744)

* Wed Jun 21 2023 Roman Inflianskas <rominf@aiven.io> - 1.25.1-1
- Update to 1.25.1 (resolve rhbz#2211880)
- Improve testing

* Thu May 25 2023 Roman Inflianskas <rominf@aiven.io> - 1.24.0-1
- Update to 1.24.0 (resolve rhbz#2196238)

* Mon May 22 2023 Benjamin A. Beasley <code@musicinmybrain.net> - 1.22.1-2
- Add grpcio extra metapackage and test dependency
- Add an explicit protobuf dependency for testing
- Re-generate integration grpc test proto bindings; fixes FTBFS with
  python-opentelemetry 1.18.0/0.39~b0

* Mon May 08 2023 Roman Inflianskas <rominf@aiven.io> - 1.22.1-1
- Update to 1.22.1 (resolve rhbz#2193365)

* Tue May 02 2023 Roman Inflianskas <rominf@aiven.io> - 1.21.1-1
- Update to 1.21.1 (resolve rhbz#2182365)

* Mon Mar 27 2023 Roman Inflianskas <rominf@aiven.io> - 1.17.0-1
- Update to 1.17.0 (resolve rhbz#2179098)

* Tue Feb 28 2023 Roman Inflianskas <rominf@aiven.io> - 1.16.0-1
- Update to 1.16.0 (resolve rhbz#2167733)
- Switch to MIT license

* Mon Jan 23 2023 Roman Inflianskas <rominf@aiven.io> - 1.14.0-1
- Update to 1.14.0 (resolve rhbz#2163387)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jan 13 2023 Roman Inflianskas <rominf@aiven.io> - 1.13.0-1
- Update to 1.13.0 (resolve rhbz#2160514)
- Cleanup check section

* Thu Jan 12 2023 Roman Inflianskas <rominf@aiven.io> - 1.12.1-1
- Update to 1.12.1 (resolve rhbz#2153838)
- Add fastapi, pymongo, and opentelemetry extras
- Remove falcon extra
- Check imports

* Wed Nov 23 2022 Roman Inflianskas <rominf@aiven.io> - 1.11.1-1
- Update to 1.11.1 (resolve rhbz#2144826)

* Mon Nov 21 2022 Roman Inflianskas <rominf@aiven.io> - 1.11.0-1
- Update to 1.11.0 (resolve rhbz#2142588)

* Wed Oct 26 2022 Roman Inflianskas <rominf@aiven.io> - 1.10.1-1
- Update to 1.10.1 (resolve rhbz#2136521)

* Tue Oct 04 2022 Roman Inflianskas <rominf@aiven.io> - 1.9.10-1
- Update to 1.9.10 (resolve rhbz#2131775)

* Wed Sep 28 2022 Roman Inflianskas <rominf@aiven.io> - 1.9.9-1
- Update to 1.9.9 (resolve rhbz#2115953)
- Add falcon extra again

* Fri Jul 29 2022 Roman Inflianskas <rominf@aiven.io> - 1.9.0-1
- Update to 1.9.0 (resolve rhbz#2111875)

* Tue Jul 26 2022 Roman Inflianskas <rominf@aiven.io> - 1.8.0-2
- Remove extras, which fail to install (resolve rhbz#2110754)

* Sat Jul 23 2022 Roman Inflianskas <rominf@aiven.io> - 1.8.0-1
- Update to 1.8.0 (resolve rhbz#2105940)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 01 2022 Roman Inflianskas <rominf@aiven.io> - 1.6.0-1
- Update to 1.6.0
- Remove falcon extra (resolve rhbz#2102851)

* Fri Jun 10 2022 Roman Inflianskas <rominf@aiven.io> - 1.5.12-1
- Initial package
