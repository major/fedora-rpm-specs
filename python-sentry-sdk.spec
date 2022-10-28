Name:           python-sentry-sdk
Version:        1.10.1
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
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)
BuildRequires:  python3dist(pytest-forked)
BuildRequires:  python3dist(werkzeug)
BuildRequires:  python3dist(pytest-localserver)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(jsonschema)
BuildRequires:  python3dist(pyrsistent)
BuildRequires:  python3dist(gevent)
BuildRequires:  python3dist(executing)
BuildRequires:  python3dist(asttokens)


%global _description %{expand:
Python Error and Performance Monitoring. Actionable insights to resolve Python
performance bottlenecks and errors. See the full picture of any Python exception
so you can diagnose, fix, and optimize performance in the Python debugging
process.}

%description %_description

%package -n python3-sentry-sdk
Summary:        %{summary}

%description -n python3-sentry-sdk %_description


# Dependencies for quart, sanic, beam, pyspark, and chalice extras are not yet in Fedora
# Dependencies for fastapi are not built for Fedora >= 37
%pyproject_extras_subpkg -n python3-sentry-sdk flask bottle falcon django celery rq aiohttp tornado sqlalchemy pure_eval httpx starlette


%prep
%autosetup -p1 -n sentry-python-%{version}


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files sentry_sdk


%check
# Deselect network-dependent tests and tests which cannot be run during Fedora build because of the version of pytest
# https://github.com/pytest-dev/pytest/issues/9621
# https://github.com/pytest-dev/pytest-forked/issues/67
%pytest \
  --deselect tests/integrations/gcp/test_gcp.py::test_handled_exception \
  --deselect tests/integrations/gcp/test_gcp.py::test_unhandled_exception \
  --deselect tests/integrations/gcp/test_gcp.py::test_timeout_error \
  --deselect tests/integrations/gcp/test_gcp.py::test_performance_no_error \
  --deselect tests/integrations/gcp/test_gcp.py::test_performance_error \
  --deselect tests/integrations/gcp/test_gcp.py::test_traces_sampler_gets_correct_values_in_sampling_context \
  --deselect tests/integrations/stdlib/test_httplib.py::test_crumb_capture \
  --deselect tests/integrations/stdlib/test_httplib.py::test_crumb_capture_hint \
  --deselect tests/integrations/stdlib/test_httplib.py::test_httplib_misuse \
  --deselect tests/integrations/threading/test_threading.py \
  --deselect tests/integrations/wsgi/test_wsgi.py \
  --deselect tests/tracing/test_deprecated.py \
  --deselect tests/utils/test_contextvars.py \
  --deselect tests/test_profiler.py::test_thread_scheduler_takes_first_samples \
  --deselect tests/test_profiler.py::test_thread_scheduler_takes_more_samples



%files -n python3-sentry-sdk -f %{pyproject_files}
%doc README.md


%changelog
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
