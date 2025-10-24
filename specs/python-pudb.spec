%global srcname pudb

Name:          python-pudb
Version:       2025.1.3
Release:       %autorelease
Summary:       A full-screen, console-based Python debugger
License:       MIT
URL:           https://github.com/inducer/pudb
Source0:       %{pypi_source}

BuildArch:     noarch
BuildRequires: python3-devel
BuildRequires: python3-pytest
BuildRequires: python3-pytest-mock
BuildRequires: pyproject-rpm-macros

%global _description %{expand:
PuDB is a full-screen, console-based visual debugger for Python.

Its goal is to provide all the niceties of modern GUI-based debuggers in a more
lightweight and keyboard-friendly package. PuDB allows you to debug code right
where you write and test it--in a terminal. If you've worked with the excellent
(but nowadays ancient) DOS-based Turbo Pascal or C tools, PuDB's UI might look
familiar.}

%description %_description

%package -n python3-%{srcname}
Summary:       A full-screen, console-based Python debugger
%description -n python3-%{srcname} %_description

%prep
%autosetup -p1 -n %{srcname}-%{version}
rm -rf %{srcname}.egg-info

sed -i '1{\@^#! /usr/bin/env python@d}' pudb/debugger.py

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst
%license LICENSE
%{_bindir}/pudb

%changelog
%autochangelog
