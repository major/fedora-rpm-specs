%global pypi_name lru-dict

Name:          python-%{pypi_name}
Version:       1.3.0
Release:       %autorelease
Summary:       A fast and memory efficient LRU cache
License:       MIT
URL:           https://github.com/amitdev/%{pypi_name}
VCS:           git:%{url}.git
Source0:       %{pypi_source %{pypi_name}}
BuildRequires: gcc
BuildRequires: python3-pytest
BuildSystem:   pyproject
BuildOption(prep):    -n %{pypi_name}-%{version}
BuildOption(install): -l lru

%description
%{summary}.

%package -n python3-%{pypi_name}
Summary: %{summary}

%description -n python3-%{pypi_name}
%{summary}.

%check -a
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
