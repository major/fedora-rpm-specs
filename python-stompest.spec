# Build for Python 2 too in EPEL <= 7
%if 0%{?rhel} && 0%{?rhel} <= 7
%global with_python2 1
%else
%global with_python2 0
%endif

%global pypi_name stompest
%global _description \
Stompest is a full-featured STOMP 1.0, 1.1 and 1.2 implementation for Python \
2.7 and Python 3 (versions 3.3 and higher), with optional TLS/SSL support.

%global commit 715f358b8503320ea42bd4de6682916339943edc
%global commit_short %(c=%{commit}; echo ${c:0:7})

Name:           python-%{pypi_name}
Version:        2.3.0
Release:        16.20191018git%{commit_short}%{?dist}
Summary:        STOMP library for Python including a synchronous client

License:        ASL 2.0
URL:            https://github.com/nikipore/stompest
Source0:        %{url}/archive/%{commit}/%{pypi_name}-%{commit}.tar.gz
BuildArch:      noarch
# Don't use the reserved async name: https://github.com/nikipore/stompest/pull/54
Patch0:         %{name}-PR54.patch
Patch1:         %{name}-mutablemapping.patch

%if 0%{?with_python2}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  pytest
BuildRequires:  python2-mock
BuildRequires:  python2-twisted >= 16.4.0
%endif

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-sphinx
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-twisted >= 16.4.0

%description %{_description}


%if 0%{?with_python2}
%package -n     python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name} %{_description}

%package -n     python2-%{pypi_name}-twisted
Summary:        %{summary} (Twisted support)
%{?python_provide:%python_provide python2-%{pypi_name}-twisted}
Requires:       python2-%{pypi_name} == %{version}-%{release}

%description -n python2-%{pypi_name}-twisted %{_description}
This package contains Twisted (asynchronous) support.
%endif


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name} %{_description}

%package -n     python%{python3_pkgversion}-%{pypi_name}-twisted
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}-twisted}
Requires:       python%{python3_pkgversion}-%{pypi_name} == %{version}-%{release}

%description -n python%{python3_pkgversion}-%{pypi_name}-twisted %{_description}
This package contains Twisted (asynchronous) support.


%prep
%autosetup -p1 -n %{pypi_name}-%{commit}
# Remove bundled egg-info
rm -rf src/*/*.egg-info

%build
pushd src/core
%if 0%{?with_python2}
%py2_build
%endif
%py3_build
popd
pushd src/twisted
%if 0%{?with_python2}
%py2_build
%endif
%py3_build
popd

%install
pushd src/core
%if 0%{?with_python2}
%py2_install
%endif
%py3_install
popd
pushd src/twisted
%if 0%{?with_python2}
%py2_install
%endif
%py3_install
popd

%check
pushd src/core
# Ignore integration tests, they require a running server.
%if 0%{?with_python2}
pytest -v --ignore stompest/tests/sync_client_integration_test.py stompest/tests
%endif
%{__python3} -m pytest -v --ignore stompest/tests/sync_client_integration_test.py stompest/tests
popd
pushd src/twisted
export PYTHONPATH=../core
%if 0%{?with_python2}
pytest -v --ignore stompest/twisted/tests/async_client_integration_test.py stompest/twisted/tests
%endif
%{__python3} -m pytest -v --ignore stompest/twisted/tests/async_client_integration_test.py stompest/twisted/tests
popd


%if 0%{?with_python2}
%files -n python2-%{pypi_name}
%doc README.markdown src/core/README.txt
%license LICENSE
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?-*.pth
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%exclude %{python2_sitelib}/%{pypi_name}/twisted

%files -n python2-%{pypi_name}-twisted
%doc README.markdown src/twisted/README.txt
%license LICENSE
%{python2_sitelib}/%{pypi_name}/twisted
%{python2_sitelib}/%{pypi_name}.twisted-%{version}-py?.?-*.pth
%{python2_sitelib}/%{pypi_name}.twisted-%{version}-py?.?.egg-info
%endif

%files -n python%{python3_pkgversion}-%{pypi_name}
%doc README.markdown src/core/README.txt
%license LICENSE
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}-*.pth
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%exclude %{python3_sitelib}/%{pypi_name}/twisted

%files -n python%{python3_pkgversion}-%{pypi_name}-twisted
%doc README.markdown src/twisted/README.txt
%license LICENSE
%{python3_sitelib}/%{pypi_name}/twisted
%{python3_sitelib}/%{pypi_name}.twisted-%{version}-py%{python3_version}-*.pth
%{python3_sitelib}/%{pypi_name}.twisted-%{version}-py%{python3_version}.egg-info


%changelog
* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-16.20191018git715f358
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-15.20191018git715f358
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-14.20191018git715f358
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 28 2023 Python Maint <python-maint@redhat.com> - 2.3.0-13.20191018git715f358
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-12.20191018git715f358
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-11.20191018git715f358
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 2.3.0-10.20191018git715f358
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-9.20191018git715f358
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Aug 05 2021 Ken Dreyer <kdreyer@redhat.com> - 2.3.0-8.20191018git715f358
- patch for collections.abc.MutableMapping for py310 (rhbz#1926350)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-7.20191018git715f358
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.3.0-6.20191018git715f358
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-5.20191018git715f358
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-4.20191018git715f358
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.3.0-3.20191018git715f358
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2.20191018git715f358
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 18 2019 Aurelien Bompard <abompard@fedoraproject.org> - 2.3.0-1.20191018git715f358
- Initial package.
