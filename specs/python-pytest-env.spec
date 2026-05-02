Name:           python-pytest-env
Version:        1.6.0
Release:        %autorelease
Summary:        Pytest plugin that allows you to add environment variables

# SPDX
License:        MIT
URL:            https://github.com/pytest-dev/pytest-env
Source:         %{url}/archive/%{version}/pytest-env-%{version}.tar.gz

BuildSystem:            pyproject
BuildOption(install):   -l pytest_env

BuildArch:      noarch

%global common_description %{expand:
A pytest plugin that sets environment variables from pyproject.toml,
pytest.toml, .pytest.toml, or pytest.ini configuration files. It can also load
variables from .env files.}

%description %{common_description}


%package -n     python3-pytest-env
Summary:        %{summary}

%description -n python3-pytest-env %{common_description}


%generate_buildrequires -p
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'


%build -p
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'


%check -a
%pytest -v


%files -n python3-pytest-env -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
