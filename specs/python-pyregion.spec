%global srcname pyregion
%global upname pyregion

Name: python-%{upname}
Version: 2.3.0
Release: %autorelease
Summary: ds9 region parser for Python
License: MIT

URL: https://github.com/astropy/pyregion
Source: %{pypi_source %{srcname}}
# include pyregion.tests as a pkg properly
Patch: pyregion-test.patch

BuildRequires: python3-devel
BuildRequires: gcc

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

%global _description %{expand:
pyregion is a python astronomy package to parse ds9 region files. 
It also supports ciao region files.}

%description %_description

%package -n python3-%{upname}
Summary: %{summary}

%description -n python3-%{upname}
%_description

%prep
%autosetup -n %{srcname}-%{version} -p1
# Add python 3.13
sed -i -e "s/310,311,312/%{python3_version_nodots}/" tox.ini
# Drop this line, it causes the build to fail
sed -i -e "s/{list_dependencies_command}/#{list_dependencies_command}/" tox.ini
# This file is a leftover of cython migration and can be removed
# https://github.com/astropy/pyregion/issues/173
rm -f pyregion/geom.h

%generate_buildrequires
%pyproject_buildrequires -e %{toxenv}-test

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l pyregion

%check
%tox

%files -n python3-%{upname} -f %{pyproject_files}
%doc README.rst 

%changelog
%autochangelog
