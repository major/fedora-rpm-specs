%global pypi_name pyswarms

%global _description %{expand:
PySwarms is an extensible research toolkit for particle swarm 
optimization (PSO) in Python. It is intended for swarm 
intelligence researchers, practitioners, and students who prefer 
a high-level declarative interface for implementing PSO in their 
problems. PySwarms enables basic optimization with PSO and 
interaction with swarm optimizations.}

Name:           python-%{pypi_name}
Version:        1.3.0
Release:        11%{?dist}
Summary:        A Python-based Particle Swarm Optimization (PSO) library

License:        MIT
URL:            https://github.com/ljvmiranda921/pyswarms
Source0:        %{pypi_source %{pypi_name}}

# Fix compatibility with the newest sphinx stack
# already resolved in https://github.com/ljvmiranda921/pyswarms/pull/468
# remove patch when new version is released
Patch0:         Patch1.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  git-core
BuildRequires:  python3dist(numpy) >= 1.10.4
BuildRequires:  python3dist(scipy) >= 0.17
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(matplotlib)
BuildRequires:  python3dist(pyparsing)
BuildRequires:  python3dist(six)
BuildRequires:  python3dist(future)
BuildRequires:  python3dist(cycler)
BuildRequires:  python3dist(kiwisolver)
BuildRequires:  python3dist(tqdm)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(nbsphinx)
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  python3-dateutil

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}

Requires:       python3dist(numpy) >= 1.10.4
Requires:       python3dist(scipy) >= 0.17

%description -n python3-%{pypi_name} %_description

%package -n python-%{pypi_name}-doc
Summary:        pyswarms documentation
%description -n python-%{pypi_name}-doc
Documentation for pyswarms package

%prep
%autosetup -n %{pypi_name}-%{version} -S git
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

# Remove extra install files
rm -rf %{buildroot}/%{python3_sitelib}/tests

%check
%pytest

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%doc AUTHORS.rst HISTORY.rst
%license LICENSE

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 1.3.0-10
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Nov 7 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.3.0-8
- Source correction

* Mon Nov 1 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.3.0-7
- Remove dependency

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jul 7 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.3.0-5
- New patch for compatibility with the new sphinx stack

* Tue Jul 6 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.3.0-4
- Use pytest macro

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.3.0-3
- Rebuilt for Python 3.10

* Sun May 2 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.3.0-2
- Add additional docs

* Sat Mar 20 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.3.0-1
- Initial package
