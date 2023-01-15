Name:           python-sentry-sdk
Version:        1.13.0
Release:        1%{?dist}
Summary:        The new Python SDK for Sentry.io

License:        BSD
URL:            https://sentry.io/for/python/
Source0:        https://github.com/getsentry/sentry-python/archive/%{version}/sentry-python-%{version}.tar.gz

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
BuildRequires:  python3dist(httpx)
BuildRequires:  python3dist(jsonschema)
BuildRequires:  python3dist(mock)
BuildRequires:  python3dist(python-multipart)
BuildRequires:  python3dist(opentelemetry-distro)
BuildRequires:  python3dist(psycopg2)
BuildRequires:  python3dist(pure-eval)
BuildRequires:  python3dist(pymongo)
BuildRequires:  python3dist(pyramid)
BuildRequires:  python3dist(pyrsistent)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-aiohttp)
BuildRequires:  python3dist(pytest-asyncio)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(pytest-forked)
BuildRequires:  python3dist(pytest-localserver)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(rq)
BuildRequires:  python3dist(sqlalchemy)
BuildRequires:  python3dist(starlette)
BuildRequires:  python3dist(tornado)
BuildRequires:  python3dist(werkzeug)


%global _description %{expand:
Python Error and Performance Monitoring. Actionable insights to resolve Python
performance bottlenecks and errors. See the full picture of any Python exception
so you can diagnose, fix, and optimize performance in the Python debugging
process.}

%description %_description

%package -n python3-sentry-sdk
Summary:        %{summary}

%description -n python3-sentry-sdk %_description


# Dependencies for quart, sanic, beam, pyspark, chalice, and starlite extras are not yet in Fedora
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
}
%pyproject_extras_subpkg -n python3-sentry-sdk %_extras


%prep
%autosetup -p1 -n sentry-python-%{version}

# Typo, see https://github.com/getsentry/sentry-python/pull/1796
sed -i 's/opentelemetry-distro>=0.350b0/opentelemetry-distro>=0.35b0/' setup.py


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files sentry_sdk


%check
%global _check_import_options %{expand:
  -e sentry_sdk.integrations.chalice
  -e sentry_sdk.integrations.falcon
  -e sentry_sdk.integrations.quart
  -e sentry_sdk.integrations.sanic
  -e sentry_sdk.integrations.starlite
  -e sentry_sdk.integrations.trytond
}
%pyproject_check_import %_check_import_options
# Testing suite relies on the test to be executed on clean env.
# By some reason, skipping the test breaks other tests, marking it as expected to fail.
sed -i '/def test_auto_enabling_integrations_catches_import_error/i@pytest.mark.xfail' tests/test_basics.py
# Deselect/ignore:
# 1. Network-dependent tests
# 2. Tests which cannot be run during Fedora build because of the version of pytest:
#    https://github.com/pytest-dev/pytest/issues/9621
#    https://github.com/pytest-dev/pytest-forked/issues/67
# 3. django integration tests (django-rest-framework is not available for Fedora 38)
# 4. pymongo integration tests (mockupdb is unpackaged because it appears unmaintained)
# 5. redis and rq integration tests (fakeredis is unpackaged yet)
# 6. bottle, django, and flask integration tests (werkzeug in Fedora 38 is too new, see: https://github.com/getsentry/sentry-python/issues/1398)
%pytest --durations=5 \
  --deselect tests/integrations/celery/test_celery.py::test_newrelic_interference \
  --deselect tests/integrations/celery/test_celery.py::test_retry \
  --deselect tests/integrations/requests/test_requests.py::test_crumb_capture \
  --deselect tests/integrations/stdlib/test_httplib.py::test_crumb_capture \
  --deselect tests/integrations/stdlib/test_httplib.py::test_crumb_capture_hint \
  --deselect tests/integrations/stdlib/test_httplib.py::test_httplib_misuse \
  --deselect tests/integrations/threading/test_threading.py \
  --deselect tests/test_transport.py::test_transport_works \
  --deselect tests/utils/test_contextvars.py \
  --ignore tests/integrations/bottle \
  --ignore tests/integrations/django \
  --ignore tests/integrations/flask \
  --ignore tests/integrations/gcp \
  --ignore tests/integrations/httpx \
  --ignore tests/integrations/pymongo \
  --ignore tests/integrations/pyramid \
  --ignore tests/integrations/redis \
  --ignore tests/integrations/rq \
  --ignore tests/integrations/wsgi


%files -n python3-sentry-sdk -f %{pyproject_files}
%doc README.md


%changelog
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
