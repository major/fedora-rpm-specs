%global srcname python-masscan

Name:           %{srcname}
Version:        0.1.6
Release:        10%{?dist}
Summary:        Python module to interact with masscan

License:        GPLv3+
URL:            https://github.com/MyKings/python-masscan
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

Requires:       masscan

%description
python-masscan is a python library which helps in using masscan port scanner.

%package -n python3-masscan
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-masscan}

%description -n python3-masscan
python-masscan is a python library which helps in using masscan port scanner.

%prep
%autosetup -n %{srcname}-%{version}
sed -i -e '/^#!\//, 1d' masscan/*.py

%build
%py3_build

%install
%py3_install

%files -n python3-masscan
%doc CHANGELOG.md README.rst
%license LICENSE
%{python3_sitelib}/*.egg-info
%{python3_sitelib}/masscan/

%changelog
* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.1.6-10
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.1.6-7
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.1.6-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.6-1
- Update to latest upstream release 0.1.6

* Sun Apr 21 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.2-1
- Initial package for Fedora
