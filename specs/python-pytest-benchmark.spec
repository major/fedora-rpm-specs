%global srcname pytest-benchmark

Name: python-%{srcname}
Version: 5.1.0
Release: 5%{?dist}
Summary: A py.test fixture for benchmarking code
# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
URL: https://pytest-benchmark.readthedocs.io
Source: https://github.com/ionelmc/%{srcname}/archive/v%{version}/%{srcname}-%{version}.tar.gz
BuildArch: noarch
BuildRequires: python3-devel

%global _description %{expand:
This plugin provides a benchmark fixture. This fixture is a callable object
that will benchmark any function passed to it.

Notable features and goals:

  - Sensible defaults and automatic calibration for microbenchmarks
  - Good integration with pytest
  - Comparison and regression tracking
  - Exhausive statistics
  - JSON export}

%description %_description

%package -n python3-%{srcname}
Summary: %summary
Requires: python3-pytest
Requires: python3-cpuinfo

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l pytest_benchmark

%check
# Tests disabled due to missing dependencies
#%%tox

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst CHANGELOG.rst CONTRIBUTING.rst AUTHORS.rst
%{_bindir}/py.test-benchmark
%{_bindir}/pytest-benchmark

%changelog
* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Sep 19 2025 Python Maint <python-maint@redhat.com> - 5.1.0-4
- Rebuilt for Python 3.14.0rc3 bytecode

* Fri Aug 15 2025 Python Maint <python-maint@redhat.com> - 5.1.0-3
- Rebuilt for Python 3.14.0rc2 bytecode

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

%autochangelog
