# Needed for Python bootstrap
%bcond_without tests

Name:           python-pyproject-hooks
Version:        1.2.0
Release:        %autorelease
Summary:        Wrappers to call pyproject.toml-based build backend hooks

# SPDX
License:        MIT
URL:            https://pypi.org/project/pyproject_hooks/
Source:         %{pypi_source pyproject_hooks}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
This is a low-level library for calling build-backends in
pyproject.toml-based project. It provides the basic functionality
to help write tooling that generates distribution files from
Python projects.}


%description %_description

%package -n     python3-pyproject-hooks
Summary:        %{summary}

%description -n python3-pyproject-hooks %_description


%prep
%autosetup -p1 -n pyproject_hooks-%{version}
sed -i "/flake8/d" dev-requirements.txt


%generate_buildrequires
%pyproject_buildrequires %{?with_tests:dev-requirements.txt}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files pyproject_hooks


%check
%pyproject_check_import
%if %{with tests}
%pytest
%endif


%files -n python3-pyproject-hooks -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
