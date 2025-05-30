%global sqlite_version 3.49.2

Name:               python-apsw
Version:            %{sqlite_version}.0
Release:            %autorelease
Summary:            Another Python SQLite Wrapper
License:            any-OSI
URL:                https://github.com/rogerbinns/apsw
Source:             https://github.com/rogerbinns/apsw/releases/download/%{version}/apsw-%{version}.zip
# https://github.com/rogerbinns/apsw/commit/4d4a4ec4c9efea20cf15c52d
Patch:              Support-Python-3.14.patch

BuildRequires:      gcc
BuildRequires:      python3-devel
BuildRequires:      python3-setuptools
BuildRequires:      sqlite-devel >= %{sqlite_version}

%global _description %{expand:
APSW is a Python wrapper for the SQLite embedded relational database
engine. In contrast to other wrappers such as pysqlite it focuses on
being a minimal layer over SQLite attempting just to translate the
complete SQLite API into Python.}

%description %_description

%package -n python3-apsw
Summary:            Another Python SQLite Wrapper

%description -n python3-apsw %_description

%prep
%autosetup -n apsw-%{version} -p1
rm -f doc/.buildinfo

%build
%py3_build -- --enable=load_extension

%install
%py3_install

%check
%{python3} setup.py build_test_extension
%{py3_test_envvars} %{python3} setup.py test

%files -n python3-apsw
%license LICENSE
%doc doc/*
%{_bindir}/apsw
%{python3_sitearch}/apsw
%{python3_sitearch}/apsw*.egg-info

%changelog
%autochangelog
