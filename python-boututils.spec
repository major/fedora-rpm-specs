# Created by pyp2rpm-3.3.4
%global pypi_name boututils

Name:           python-%{pypi_name}
Version:        0.1.10
Release:        %autorelease
Summary:        Python package containing BOUT++ utils

License:        LGPLv3+
URL:            http://boutproject.github.io
Source0:        %pypi_source
BuildArch:      noarch

Patch:          https://github.com/boutproject/boututils/pull/47.patch
Patch:          https://github.com/boutproject/boututils/pull/48.patch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
# From setup_requires in setup.py:
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm[toml]) >= 3.4
BuildRequires:  python3dist(setuptools-scm-git-archive)
# For tests:
BuildRequires:  python3dist(pytest)

%description
Utils for postprocessing of BOUT++ simulations.


%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
Utils for BOUT++


%pyproject_extras_subpkg -n python3-%{pypi_name} mayavi


%generate_buildrequires
%pyproject_buildrequires -r


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{pypi_name}


%check
%pytest


%files -n python3-%{pypi_name} -f  %{pyproject_files}
%license LICENSE
%doc README.md


%changelog
%autochangelog
