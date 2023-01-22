%global pypi_name aioftp
%bcond_with network

Name:           python-%{pypi_name}
Version:        0.21.3
Release:        2%{?dist}
Summary:        FTP client/server for asyncio

License:        ASL 2.0
URL:            https://github.com/aio-libs/aioftp
Source0:        %{pypi_source}
BuildArch:      noarch

%description
FTP client/server for asyncio.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%if %{with network}
BuildRequires:  python3-async-timeout
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-asyncio
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-siosocks
BuildRequires:  python3-trustme
%endif
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
FTP client/server for asyncio.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%if %{with network}
%check
%pytest -v tests
%endif

%files -n python3-%{pypi_name}
%license license.txt
%doc README.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info

%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Sep 25 2022 Fabian Affolter <mail@fabian-affolter.ch> - 0.21.3-1
- Update to latest upstream release 0.21.3 (closes rhbz#2077148)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.21.0-2
- Rebuilt for Python 3.11

* Fri Mar 25 2022 Fabian Affolter <mail@fabian-affolter.ch> - 0.21.0-1
- Update to latest upstream release 0.21.0 (closes rhbz#2017567)

* Fri Mar 04 2022 Fabian Affolter <mail@fabian-affolter.ch> - 0.20.1-1
- Update to latest upstream release 0.20.1 (closes rhbz#2017567)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.18.1-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Oct 10 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.18.1-1
- Update to latest upstream release 0.18.1 (#1887058)

* Sat Aug 22 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.17.2-1
- Update to latest upstream release 0.17.2

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 12 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.16.1-1
- Update to latest upstream release 0.16.1

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.16.0-2
- Rebuilt for Python 3.9

* Fri Apr 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.16.0-1
- Update to latest upstream release 0.16.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 10 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.14.0-2
- Better use of wildcards (rhbz#1787314)

* Wed Jan 01 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.14.0-1
- Initial package for Fedora
