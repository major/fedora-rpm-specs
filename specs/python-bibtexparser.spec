%global srcname bibtexparser

Name:           python-%{srcname}
Version:        1.4.3
Release:        %autorelease
Summary:        A BibTeX parsing library

License:        BSD-3-Clause OR  	LGPL-3.0-or-later
URL:            https://github.com/sciunto-org/python-%{srcname}
Source0:        https://github.com/sciunto-org/python-%{srcname}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-sphinx

%global _description %{expand:
BibtexParser is a python library to parse BibTeX files. The code relies
on pyparsing and is tested with unit tests.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %_description

%package doc
Summary: python-bibtexparser documentation

%description doc
Documentation for python-bibtexparser.

%prep
%autosetup -p1 -n python-%{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
# Generate html documentation.
PYTHONPATH=${PWD} sphinx-build docs/source html
# Remove the sphinx-build leftovers.
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files -l bibtexparser

# Avoid tox, as that requires python-nose, and Fedora retired that package
# for lack of maintenance. Upstream appears to have abandoned tox too, but
# they have not yet published a release with this change.
%check
%pyproject_check_import

%files -n python3-%{srcname} -f %{pyproject_files}
%doc CHANGELOG README.rst requirements.txt
%license COPYING

%files doc
%doc html
%license COPYING

%changelog
%autochangelog
