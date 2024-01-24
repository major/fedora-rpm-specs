%bcond_without tests

%global srcname urwid

Name:          python-%{srcname}
Version:       2.4.4
Release:       %autorelease
Summary:       Console user interface library

License:       LGPLv2+
URL:           http://excess.org/urwid/
Source0:       %{pypi_source urwid}

%global _description\
Urwid is a Python library for making text console applications.  It has\
many features including fluid interface resizing, support for UTF-8 and\
CJK encodings, standard and custom text layout modes, simple markup for\
setting text attributes, and a powerful, dynamic list box that handles a\
mix of widget types.  It is flexible, modular, and leaves the developer in\
control.

%description %_description

%package -n python3-%{srcname}
Summary: %summary
%{?python_provide:%python_provide python3-urwid}
BuildRequires: gcc
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-setuptools_scm
# needed by selftest suite for test.support
BuildRequires: python3-test

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}
find urwid -type f -name "*.py" -exec sed -i -e '/^#!\//, 1d' {} \;
find urwid -type f -name "*.py" -exec chmod 644 {} \;

%build
%py3_build

find examples -type f -exec chmod 0644 \{\} \;

%check
%if %{with tests}
# tests are failing: https://github.com/urwid/urwid/issues/344
PYTHON=%{__python3} %{__python3} setup.py test || :
%endif

%install
%py3_install

%files -n python3-%{srcname}
%license COPYING
%doc README.rst examples docs
%{python3_sitearch}/urwid/
%{python3_sitearch}/urwid-%{version}*.egg-info/

%changelog
%autochangelog
