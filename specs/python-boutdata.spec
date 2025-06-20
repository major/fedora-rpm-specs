# Created by pyp2rpm-3.3.4
%global pypi_name boutdata

Name:           python-%{pypi_name}
Version:        0.3.0
Release:        %autorelease
Summary:        Python package for collecting BOUT++ data

License:        LGPL-3.0-or-later
URL:            http://boutproject.github.io
Source0:        %pypi_source
BuildArch:      noarch

# Fix for 3.14: allow pickling
Patch:          https://github.com/boutproject/boutdata/pull/126.patch
# Fix license format
Patch:          https://github.com/boutproject/boutdata/pull/125.patch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
# From setup_requires in setup.py:
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm[toml]) >= 3.4
# For tests:
BuildRequires:  python3dist(pytest)

%description
Python interface for reading bout++ data files.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

Provides:       python3-boututils = %{version}-%{release}
Obsoletes:      python3-boututils < %{version}-%{release}

%description -n python3-%{pypi_name}
Python interface for reading bout++ data files.

%generate_buildrequires
%pyproject_buildrequires -r


%prep
%autosetup -n %{pypi_name}-%{version} -p 1
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{pypi_name} boututils boutupgrader


%check
# Workaround for https://bugzilla.redhat.com/show_bug.cgi?id=1997717
export HDF5_USE_FILE_LOCKING=FALSE
# Smoke test for squash
echo ${RPM_BUILD_ROOT}/%{python3_sitelib}:${PYTHONPATH}
PYTHONPATH=${RPM_BUILD_ROOT}/%{python3_sitelib}:${PYTHONPATH} ${RPM_BUILD_ROOT}/%{_bindir}/bout-squashoutput --help
PYTHONPATH=${RPM_BUILD_ROOT}/%{python3_sitelib}:${PYTHONPATH} ${RPM_BUILD_ROOT}/%{_bindir}/bout-upgrader --help
# run unit tests
%pytest


%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/bout-squashoutput
%{_bindir}/bout-upgrader


%changelog
%{autochangelog}
