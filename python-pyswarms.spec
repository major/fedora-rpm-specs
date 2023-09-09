%global pypi_name pyswarms
%global forgeurl https://github.com/ljvmiranda921/pyswarms

# Disable tests until upstream provides feedback
# https://github.com/ljvmiranda921/pyswarms/issues/516
%bcond_with tests

%global _description %{expand:
PySwarms is an extensible research toolkit for particle swarm 
optimization (PSO) in Python. It is intended for swarm 
intelligence researchers, practitioners, and students who prefer 
a high-level declarative interface for implementing PSO in their 
problems. PySwarms enables basic optimization with PSO and 
interaction with swarm optimizations.}

Name:           python-%{pypi_name}
Version:        1.3.0
Release:        %autorelease
Summary:        A Python-based Particle Swarm Optimization (PSO) library
%forgemeta
License:        MIT
URL:            %forgeurl
Source0:        %forgesource

# Fix compatibility with the newest sphinx stack
# already resolved in https://github.com/ljvmiranda921/pyswarms/pull/468
# remove patch when new version is released
Patch0:         Patch1.patch
# matplotlib 3.7 support
Patch1:         https://patch-diff.githubusercontent.com/raw/ljvmiranda921/pyswarms/pull/509.patch

BuildArch:      noarch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

BuildRequires:  python3-devel
BuildRequires:  git-core
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(nbsphinx)
BuildRequires:  python3-sphinx_rtd_theme


%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}

Requires:       python3dist(numpy) >= 1.10.4
Requires:       python3dist(scipy) >= 0.17

%description -n python3-%{pypi_name} %_description

%package -n python-%{pypi_name}-doc
Summary:        Documentation for PySwarms
%description -n python-%{pypi_name}-doc
Documentation for pyswarms package

%prep
%autosetup -n %{pypi_name}-%{version} -S git
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files pyswarms

# Remove extra install files
rm -rf %{buildroot}/%{python3_sitelib}/tests

%check
%if %{with tests}
  %pytest
%else
  %pyproject_check_import
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md

%files -n python-%{pypi_name}-doc
%doc html
%doc AUTHORS.rst HISTORY.rst
%license LICENSE

%changelog
%autochangelog
