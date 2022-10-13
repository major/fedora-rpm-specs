%global srcname Yapsy
%global modname yapsy

Name:           python-%{modname}
Version:        1.12.2
Release:        %autorelease
Summary:        Simple plugin system for Python applications

License:        BSD and ISC and CC-BY-SA
URL:            http://yapsy.sourceforge.net
Source0:        http://downloads.sourceforge.net/project/%{modname}/%{srcname}-%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%global _description \
Yapsy’s main purpose is to offer a way to easily design a plugin system in\
Python. Yapsy only depends on Python’s standard library.

%description %{_description}

%package doc
Summary:        Documentation for python-yapsy, a plugin system for Python applications
BuildRequires:  python3-sphinx
Obsoletes:      python3-%{modname}-doc < 1.11.223-4

%description doc
Documentation for yapsy, a simple plugin system for Python applications.

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-%{modname} %{_description}

%prep
%autosetup -n %{srcname}-%{version}
rm -vrf *.egg-info

%build
%py3_build
%{__python3} setup.py build_sphinx

%install
%py3_install

%check
%{__python3} setup.py test || :

%files -n python3-%{modname}
%license LICENSE.txt
%doc CHANGELOG.txt README.txt
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{modname}/

%files doc
%doc build/sphinx/html

%changelog
%autochangelog
