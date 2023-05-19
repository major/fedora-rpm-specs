%global srcname optcomplete
%global commit 4079d7ab75f6361a4309fdf647595d878ca4a4fe
%global shortcommit %(c=%{commit}; echo ${c:0:12})

Name:           python-%{srcname}
Version:        1.2.1
Release:        15%{?dist}
Summary:        Shell Completion Self-Generator for Python
License:        BSD
URL:            http://furius.ca/%{srcname}
Source0:        https://github.com/blais/optcomplete/archive/%{commit}.zip
BuildArch:      noarch

%description
This Python module aims at providing almost automatically shell completion

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        Shell Completion Self-Generator for Python 3
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  /usr/bin/2to3
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
This Python 3 module aims at providing almost automatically shell completion
for any Python program that already uses the optparse module.

%prep
%autosetup -p1 -n %{srcname}-%{commit}
2to3 --write --nobackups .

%build
%py3_build

%install
%py3_install

%files -n python%{python3_pkgversion}-%{srcname}
%license COPYING
%doc CHANGES CREDITS doc/*.txt README.rst TODO
%{python3_sitelib}/*.egg-info
%{python3_sitelib}/*.py
%{python3_sitelib}/__pycache__/*

%changelog
%autochangelog
