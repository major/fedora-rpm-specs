%global pypi_name lazy_load
%global common_description %{expand:
A minimalistic interface that allows lazy evaluation of expressions and
function calls.}

Name:          python-%{pypi_name}
Version:       0.8.3
Release:       %autorelease
BuildArch:     noarch
Summary:       A minimalistic interface that allows lazy evaluation
License:       MIT
URL:           https://github.com/kutoga/lazy-load
VCS:           git:%{url}.git
Source0:       %{pypi_source %{pypi_name}}
BuildRequires: python3-pytest
BuildSystem:   pyproject
BuildOption(prep):    -n %{pypi_name}-%{version}
BuildOption(install): -l %{pypi_name}

%description %{common_description}

%package -n python3-%{pypi_name}
Summary: %{summary}

%description -n python3-%{pypi_name} %{common_description}

%check -a
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
