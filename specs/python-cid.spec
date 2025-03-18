%global pypi_name cid
%global common_description %{expand:
Self-describing content-addressed identifiers for distributed systems
implementation in Python.}

Name:          python-%{pypi_name}
Version:       0.3.0
Release:       %autorelease
BuildArch:     noarch
Summary:       Self-describing content-addressed identifiers
License:       MIT
URL:           https://github.com/ipld/py-cid
Source0:       %{pypi_source py-%{pypi_name}}
Patch1:        python-cid-0001-Relax-dependencies.patch
BuildRequires: python3-hypothesis
BuildRequires: python3-pytest
BuildSystem:   pyproject
BuildOption(prep):    -n py-%{pypi_name}-%{version}
BuildOption(install): -l %{pypi_name}

%description %{common_description}

%package -n python3-%{pypi_name}
Summary: %{summary}

%description -n python3-%{pypi_name} %{common_description}

%check -a
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc AUTHORS.rst HISTORY.rst README.rst

%changelog
%autochangelog
