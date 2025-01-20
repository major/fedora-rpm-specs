%global srcname rq
%bcond_without tests

Name:           python-%{srcname}
Version:        1.16.2
Release:        3%{?dist}
Summary:        Simple, lightweight, library for creating background jobs, and processing them

License:        BSD-2-Clause
URL:            https://python-rq.org
Source:         https://github.com/rq/rq/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  python3-pytest
BuildRequires:  python3-psutil
# python3-sentry-sdk in Fedora 41 is old and is blocked:
# https://bugzilla.redhat.com/show_bug.cgi?id=2291914
# Also, upstream does not support Python 3.13:
# https://github.com/getsentry/sentry-python/issues/2664
# https://github.com/getsentry/sentry-python/pull/3200
# Enable Sentry SDK for current non-rawhide distros
%{?fc39:BuildRequires:  python3dist(sentry-sdk)}
%{?fc40:BuildRequires:  python3dist(sentry-sdk)}
BuildRequires:  redis
%endif

%global _description %{expand:
RQ (Redis Queue) is a simple Python library for queueing jobs
and processing them in the background with workers.
It is backed by Redis and it is designed to have a low barrier to entry.
It should be integrated in your web stack easily.}

%description %{_description}

%package     -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}
Python 3 version.

%prep
%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%if %{with tests}
%{_bindir}/redis-server --bind 127.0.0.1 --port 6379 &
REDIS_SERVER_PID=$!
%if 0%{?fedora} >= 41
# See comment about python3-sentry-sdk above
pytest_deselect="--deselect=tests/test_sentry.py::TestSentry::test_failure_capture"
%endif
%pytest -v $pytest_deselect
%{_bindir}/redis-cli shutdown nosave force now
# Wait for redis-server termination (the command above is async)
wait $REDIS_SERVER_PID
%endif

%files -n python3-%{srcname} -f %pyproject_files
%license LICENSE
%doc README.md
%{_bindir}/rq
%{_bindir}/rqinfo
%{_bindir}/rqworker

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jul 02 2024 Roman Inflianskas <rominf@pm.me> - 1.16.2-1
- Update to 1.16.2 (fedora#1851741, fedora#2291904)

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.12.0-7
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jul 13 2023 Python Maint <python-maint@redhat.com> - 1.12.0-3
- Rebuilt for Python 3.12

* Sat Jul 01 2023 Python Maint <python-maint@redhat.com> - 1.12.0-2
- Bootstrap for Python 3.12

* Mon Jan 23 2023 Ali Erdinc Koroglu <aekoroglu@fedoraproject.org> - 1.12.0-1
- Update to 1.12.0

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.7.0-7
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.7.0-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 15 2020 Charalampos Stratakis <cstratak@redhat.com> - 1.7.0-2
- Convert to pyproject macros

* Sat Dec 12 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.7.0-1
- Update to 1.7.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.2-2
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.2.2-1
- Update to 1.2.2

* Fri Jan 31 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.2.1-1
- Update to 1.2.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 06 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1.0-1
- Initial package
