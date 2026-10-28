Name:           python-pytest-env
Version:        1.8.3
Release:        %autorelease
Summary:        Set environment variables for pytest sessions

# SPDX
License:        MIT
URL:            https://github.com/pytest-dev/pytest-env
Source:         %{url}/archive/%{version}/pytest-env-%{version}.tar.gz

BuildSystem:    pyproject
BuildOption(install): --assert-license pytest_env

BuildArch:      noarch

# From “test” dependency group, which also has unwanted coverage dependencies:
BuildRequires:  %{py3_dist pytest-mock}

%global common_description %{expand:
A pytest plugin that sets environment variables from pyproject.toml,
pytest.toml, .pytest.toml, or pytest.ini configuration files. It can also load
variables from .env files.}

%description %{common_description}


%package -n     python3-pytest-env
Summary:        %{summary}

%description -n python3-pytest-env %{common_description}


%prep -a
# Loosen some unnecessarily aggressive version bounds
%if %{defined fc45}
%pyproject_patch_dependency hatchling:set_lower:1.31.0
%endif
# https://bugzilla.redhat.com/show_bug.cgi?id=2544657
%pyproject_patch_dependency python-dotenv:set_lower:1.2.2


%generate_buildrequires -p
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'


%build -p
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'


%check -a
%pytest --verbose


%files -n python3-pytest-env -f %{pyproject_files}
%doc CHANGELOG.md
%doc README.md


%changelog
%autochangelog
