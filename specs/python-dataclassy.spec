%global pypi_name dataclassy
%global common_description %{expand:
An enhanced, tiny reimplementation of data classes in Python - an alternative
to the built-in dataclasses module that avoids many of its common pitfalls.
dataclassy is designed to be more flexible, less verbose, and more powerful
than dataclasses, while retaining a familiar interface.}

Name:          python-%{pypi_name}
Version:       1.0.1
Release:       %autorelease
BuildArch:     noarch
Summary:       An enhanced, tiny reimplementation of dataclasses
License:       MPL-2.0
URL:           https://github.com/biqqles/%{pypi_name}
VCS:           git:%{url}.git
Source0:       %{pypi_source %{pypi_name}}
# FIXME should go into PyPi package
Source1:       python-dataclassy-tests.py
BuildRequires: python3-mypy
BuildSystem:   pyproject
BuildOption(prep):    -n %{pypi_name}-%{version}
BuildOption(install): -l %{pypi_name}

%description %{common_description}

%package -n python3-%{pypi_name}
Summary: %{summary}

%description -n python3-%{pypi_name} %{common_description}

%prep -a
# FIXME should go into PyPi package
install -D -p -m 0644 %{SOURCE1} tests.py

%check -a
%python3 tests.py

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
