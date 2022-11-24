%global pypi_name pydeps

%global desc %{expand: \
Python module dependency visualization. This package installs the pydeps
command, and normal usage will be to use it from the command line.}

%bcond_without check

%global forgeurl https://github.com/thebjorn/pydeps

Name:		%{pypi_name}
Version:	1.10.24
Release:	%autorelease
Summary:	Display module dependencies
License:	BSD
%forgemeta
URL:		%forgeurl
Source0:	%forgesource
BuildArch:	noarch

%{?python_enable_dependency_generator}

BuildRequires:	python3-devel
%if %{with check}
BuildRequires:	python3-pytest
BuildRequires:	python3dist(pyyaml)
BuildRequires:	graphviz
%endif

%description
%{desc}

%prep
%autosetup -n %{pypi_name}-%{version} -N

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%if %{with check}
%check
# Exclude failing tests:
# https://github.com/thebjorn/pydeps/issues/71
%pytest -k "not (test_file or test_relative_imports_same_name_with_std \
or test_pydeps_colors or test_find_package_names)"
%endif

%files -n %{pypi_name} -f %{pyproject_files}
%doc README.rst
%{_bindir}/pydeps

%changelog
%autochangelog
