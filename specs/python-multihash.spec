%global pypi_name multihash

Name:          python-%{pypi_name}
Version:       2.0.1
Release:       %autorelease
BuildArch:     noarch
Summary:       Multihash implementation in Python
License:       MIT
URL:           https://github.com/multiformats/py-%{pypi_name}
VCS:           git:%{url}.git
Source0:       %{pypi_source py-%{pypi_name}}
BuildRequires: python3-pytest
BuildSystem:   pyproject
BuildOption(prep):    -n py-%{pypi_name}-%{version}
BuildOption(install): -l %{pypi_name}

%description
%{summary}.

%package -n python3-%{pypi_name}
Summary: %{summary}.

%description -n python3-%{pypi_name}
%{summary}.

%check -a
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc AUTHORS.rst HISTORY.rst README.rst

%changelog
%autochangelog
