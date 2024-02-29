%bcond_without tests
%global debug_package %{nil}

%global srcname urwid

Name:          python-%{srcname}
Version:       2.6.5
Release:       %autorelease
Summary:       Console user interface library

# examples/twisted_serve_ssh.py is MIT
License:       LGPL-2.1-or-later AND MIT
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
BuildRequires: python3-pytest
BuildRequires: python3-pytest-cov
BuildRequires: python3-tox

%description -n python3-%{srcname} %_description

%generate_buildrequires
%pyproject_buildrequires

%prep
%autosetup -n %{srcname}-%{version}
find urwid -type f -name "*.py" -exec sed -i -e '/^#!\//, 1d' {} \;
find urwid -type f -name "*.py" -exec chmod 644 {} \;

%build
%pyproject_wheel
find examples -type f -exec chmod 0644 \{\} \;

%check
%if %{with tests}
%pytest tests/
%endif

%install
%pyproject_install
%pyproject_save_files %{srcname}

%files -n python3-%{srcname} -f %{pyproject_files}
%license COPYING
%doc README.rst examples docs

%changelog
%autochangelog
