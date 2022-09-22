# Sphinx-generated HTML documentation is not suitable for packaging; see
# RHBZ#2006555 for discussion. Additionally, upstream uses the furo theme,
# which we would have to patch; see RHBZ#1910798.
#
# We could, in theory, generate PDF documentation as a substitute, but this
# would still require it requires python3dist(myst-parser), which is not
# currently packaged–and we are not willing to package it solely for this
# purpose.

Name:           python-editables
Version:        0.3
Release:        %autorelease
Summary:        Editable installations

License:        MIT
URL:            https://github.com/pfmoore/editables
# PyPI source distributions lack tests; use the GitHub archive
Source0:        %{url}/archive/%{version}/editables-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

# Most of the dependencies, and all of the pytest options, in tox.ini are for
# coverage analysis and for installation with pip/virtualenv. Rather than
# working around all of these, it is simpler not to use tox for dependency
# generation or testing.
BuildRequires:  python3dist(pytest)

%global common_description %{expand:
A Python library for creating “editable wheels”

This library supports the building of wheels which, when installed, will expose
packages in a local directory on sys.path in “editable mode”. In other words,
changes to the package source will be reflected in the package visible to
Python, without needing a reinstall.}

%description %{common_description}


%package -n python3-editables
Summary:        %{summary}

%description -n python3-editables %{common_description}


%prep
%autosetup -n editables-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files editables


%check
%pytest


%files -n python3-editables -f %{pyproject_files}
# pyproject-rpm-macros handles LICENSE.txt; verify with “rpm -qL -p …”
%doc CHANGELOG.md
%doc README.md


%changelog
%autochangelog
