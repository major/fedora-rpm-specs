%global srcname SnipeIT-PythonAPI
%global modname snipeit   

Name:           python-%{modname}
# changelog has versions in README
Version:        1.2 
Release:        7%{?dist}
Summary:        Python Interface to the SnipeIT API

# MIT license mentioned in setup.py
License:        MIT
URL:            https://github.com/jbloomer/%{srcname}
Source0:        %{url}/raw/master/dist/%{modname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-requests
BuildRequires:  python3-simplejson

%global _description\
Use this package to interface with the SnipeIT\
(https://snipeitapp.com/) API directly from Python.

%description
%_description

%package -n python3-%{modname}
Summary:        %{summary}
Requires:       python3-requests
Requires:       python3-simplejson

%description -n python3-%{modname}
%_description

%prep
%autosetup -n%{modname}-%{version}

%build
%{py3_build}

%install
%{py3_install}
 
%files -n python3-%{modname}
%doc README.rst
%doc doc/snipeit/*.html
%{python3_sitelib}/%{modname}/
%{python3_sitelib}/%{modname}-%{version}-py%{python3_version}.egg-info/

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.2-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.2-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Nov 08 2020 Raphael Groner <raphgro@fedoraproject.org> - 1.2-1
- initial
