%global srcname inquirer

Name:           python-%{srcname}
Version:        3.1.3
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
interfaces, based on Inquirer.js.}

%description %_description

%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description

%prep
%autosetup -p1

# Fix interpreter invocations in tests
sed -i 's:python:python3:g' tests/acceptance/*.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%license %{python3_sitelib}/%{srcname}-%{version}.dist-info/LICENSE
%doc README.md

%changelog
%autochangelog
