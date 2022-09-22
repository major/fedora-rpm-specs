%global srcname anyio

%if %{defined fedora}
# As of 2022-03-04, neither EL9 or EPEL9 have python3-uvloop
%bcond_without tests
# As of 2022-03-04, neither EL9 or EPEL9 have python3-sphinx-autodoc-typehints
%bcond_without docs
%endif

%global common_description %{expand:
AnyIO is an asynchronous networking and concurrency library that works on top
of either asyncio or trio.  It implements trio-like structured concurrency (SC)
on top of asyncio, and works in harmony with the native SC of trio itself.}

Name:           python-%{srcname}
Version:        3.5.0
Release:        4%{?dist}
Summary:        Compatibility layer for multiple asynchronous event loop implementations
License:        MIT
URL:            https://github.com/agronholm/anyio
Source:         %pypi_source

# Support for pytest 7
# Fixes https://bugzilla.redhat.com/2069194
# https://github.com/agronholm/anyio/commit/58fcb0c495
# setup.cfg hunk manually removed (it failed to apply)
Patch:          pytest7.patch

# Skip @asyncio.coroutine tests on Python 3.11+ where it no longer exists
Patch:          https://github.com/agronholm/anyio/pull/431.patch

# Cancel messages are only supported on Python 3.9 and 3.10
# https://github.com/agronholm/anyio/commit/95f43f8db1
Patch:           0001-Fixed-cancel-message-related-test-failure-on-py3.11.patch

BuildArch:      noarch


%description %{common_description}


%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel


%description -n python3-%{srcname} %{common_description}


%pyproject_extras_subpkg -n python3-%{srcname} trio


%if %{with docs}
%package -n python-%{srcname}-doc
Summary:        anyio documentation


%description -n python-%{srcname}-doc
Documentation for anyio
%endif


%prep
%autosetup -n %{srcname}-%{version} -p1

# disable coverage test requirement
sed -e '/coverage/d' -i setup.cfg

# Disable some tests till uvloop is compatible with Python 3.11
# upstream discussion: https://github.com/agronholm/anyio/issues/439
sed -i '/uvloop/d' setup.cfg

# despite the prescense of a pytest "network" marker, socket tests still fail
# without internet access
rm tests/test_sockets.py


%generate_buildrequires
%pyproject_buildrequires -x trio%{?with_tests:,test}%{?with_docs:,doc}


%build
%pyproject_wheel
%if %{with docs}
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif


%install
%pyproject_install
%pyproject_save_files %{srcname}


%if %{with tests}
%check
%pytest -m "not network"
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst


%if %{with docs}
%files -n python-%{srcname}-doc
%doc html
%license LICENSE
%endif


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 3.5.0-3
- Rebuilt for Python 3.11

* Tue Mar 29 2022 Miro Hrončok <mhroncok@redhat.com> - 3.5.0-2
- Fix for pytest7
- Fixes: rhbz#2069194

* Fri Mar 04 2022 Carl George <carl@george.computer> - 3.5.0-1
- Latest upstream rhbz#2007952
- Enable test suite
- Only run test on Fedora
- Only build docs on Fedora

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Oct 08 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 3.3.1-2
- Add metapackage for “trio” extra

* Wed Sep 08 2021 Fabian Affolter <mail@fabian-affolter.ch> - 3.3.1-1
- Update to latest upstream release 3.3.1 (closes rhbz#1975540)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 22 2021 Carl George <carl@george.computer> - 3.2.0-1
- Latest upstream
- Fixes: rhbz#1926501
- Fixes: rhbz#1900506

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.0.2-2
- Rebuilt for Python 3.10

* Thu Jan 28 2021 Dan Čermák <dan.cermak@cgc-instruments.com> - 2.0.2-1
- New upstream release 2.0.2

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 02 2020 Carl George <carl@george.computer> - 1.3.1-1
- Latest upstream

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.3-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 13 2020 Carl George <carl@george.computer> - 1.2.3-1
- Latest upstream rhbz#1786957

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 16 2019 Carl George <carl@george.computer> - 1.0.0-1
- Initial package
