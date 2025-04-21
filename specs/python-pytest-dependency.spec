%global srcname pytest-dependency

Name:           python-%{srcname}
Version:        0.6.0
Release:        %autorelease
Summary:        Pytest plugin to manage dependencies of tests

License:        Apache-2.0
URL:            https://github.com/RKrahl/pytest-dependency
Source:         %{pypi_source}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
This module is a plugin for the popular Python testing framework pytest.
It manages dependencies of tests: you may mark some tests as dependent from
other tests. These tests will then be skipped if any of the dependencies did
fail or has been skipped.}

%description %_description

%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description

%prep
%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pytest_dependency

%check
%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst CHANGES.rst

%changelog
%autochangelog
