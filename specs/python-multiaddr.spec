%global pypi_name multiaddr

Name:          python-%{pypi_name}
Version:       0.0.9
Release:       %autorelease
BuildArch:     noarch
Summary:       Multiaddr implementation in Python
License:       MIT
URL:           https://github.com/multiformats/py-multiaddr
Source0:       %{pypi_source %{pypi_name}}

# Downstream-only: remove pytest-runner dependency
# We can’t send this upstream because the project is archived.
# https://fedoraproject.org/wiki/Changes/DeprecatePythonPytestRunner
Patch:         0001-Downstream-only-remove-pytest-runner-dependency.patch

BuildRequires: python3-idna
BuildRequires: python3-pytest
BuildSystem:   pyproject
BuildOption(prep):    -n %{pypi_name}-%{version}
BuildOption(install): -l %{pypi_name}

%description
%{summary}.

%package -n python3-%{pypi_name}
Summary: %{summary}

%description -n python3-%{pypi_name}
%{summary}.

%check -a
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc AUTHORS HISTORY.rst README.rst

%changelog
%autochangelog
