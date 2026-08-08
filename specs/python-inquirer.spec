%global srcname inquirer

Name:           python-%{srcname}
Version:        3.4.1
Release:        %autorelease
Summary:        Collection of common interactive command line user interfaces

License:        MIT
URL:            https://github.com/magmax/python-inquirer
# The PyPI tarball doesn't include tests so use GitHub instead
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pexpect
BuildRequires:  python3-pytest
BuildRequires:  sed

%global _description %{expand:
This package provides a collection of common interactive command line user
interfaces, based on the Inquirer JavaScript library.}

%description %_description

%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description

%prep
%autosetup -p1

# Fix interpreter invocations in tests
sed -i 's:python:python3:g' tests/acceptance/*.py

# PyPI package name is editor, but Fedora packages it as python-editor
sed -i 's/editor = ">=1.6.0"/python-editor = ">=1.0.4"/' pyproject.toml

# Fedora packages readchar as 4.0.5, but inquirer 3.4.1 asks for >=4.2.0
# The API is compatible enough, so relax the version requirement to >=4.0.0
# This workaround can be removed when readchar is upgraded to 4.2.2
# https://src.fedoraproject.org/rpms/python-readchar/pull-request/2
sed -i 's/readchar = ">=4.2.0"/readchar = ">=4.0.0"/' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%pyproject_check_import
%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
