%bcond_without check

%global srcname astropy

Name: python-%{srcname}
Version: 7.1.0
Release: %autorelease
Summary: A Community Python Library for Astronomy
# File _strptime.py is under Python-2.0.1
# jquery is MIT
License: BSD-3-Clause AND CFITSIO AND Python-2.0.1 AND MIT

URL: http://astropy.org
Source: %{pypi_source %{srcname}}
Source: astropy-README.dist
Patch: python-astropy-system-configobj.patch
Patch: python-astropy-system-ply.patch
# Add python 3.14 to tox.ini
Patch: tox314.patch
# Backported fix 
# https://github.com/astropy/astropy/issues/18127
Patch: fix-18125.patch
# https://github.com/astropy/astropy/issues/18126
Patch: fix-18126.patch

BuildRequires: gcc
BuildRequires: expat-devel
BuildRequires: wcslib-devel >= 8.4
BuildRequires: python3-devel

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

%global _description %{expand:
The Astropy project is a common effort to develop a single core package
for Astronomy. Major packages such as PyFITS, PyWCS, vo, and asciitable
already merged in, and many more components being worked on. In
particular, we are developing imaging, photometric, and spectroscopic
functionality, as well as frameworks for cosmology, unit handling, and
coordinate transformations.}

%description %_description

%package -n python3-%{srcname}
Summary: %{summary}
BuildRequires: %{py3_dist tox}
BuildRequires: %{py3_dist pytest}
BuildRequires: %{py3_dist hypothesis}
# Unbundled
BuildRequires: %{py3_dist configobj}
BuildRequires: %{py3_dist ply}
Requires: %{py3_dist configobj}
Requires: %{py3_dist ply}
# Bundled
Provides: bundled(cfitsio) = 4.5.0
Provides: bundled(jquery) = 3.60
Provides: bundled(wcslib) = 8.4

# Drop doc subpackage, is empty 

%description -n python3-%{srcname}
%_description

Provides: python3-%{srcname}-doc = %{version}-%{release}
Obsoletes: python3-%{srcname}-doc < 6.0.1-1

%package -n %{srcname}-tools
Summary: Astropy utility tools
BuildArch: noarch
Requires: python3-%{srcname} = %{version}-%{release} 

%description -n %{srcname}-tools
Utilities provided by Astropy.

%prep
%autosetup -n %{srcname}-%{version} -p1
rm -rf astropy/extern/configobj
rm -rf astropy/extern/ply
rm -rf cextern/expat

# Apparently, --current-env doesn't like {list_dependencies_command}
sed -i 's/{list_dependencies_command}/python -m pip freeze --all/g' tox.ini

export ASTROPY_USE_SYSTEM_ALL=1
%generate_buildrequires
%if %{with check}
%pyproject_buildrequires -e %{toxenv}-test
%else
%pyproject_buildrequires 
%endif

%build
export ASTROPY_USE_SYSTEM_ALL=1
# Search for headers in subdirs
export CPATH="/usr/include/wcslib"
%pyproject_wheel

%install
export ASTROPY_USE_SYSTEM_ALL=1
# Search for headers in subdirs
export CPATH="/usr/include/wcslib"
%pyproject_install

%pyproject_save_files -l astropy

%check
%if %{with check}
pytest_args=(
 -k "not (test_coverage or test_basic_testing_completeness or test_all_included)"
 --verbosity=0
# Some doctest are failing because of different output in big/little endian
%ifarch s390x
 --ignore ../../docs/io/fits/index.rst
 --ignore ../../docs/io/fits/usage/image.rst
 --ignore ../../docs/io/fits/usage/unfamiliar.rst
%endif
)

%tox -- --parallel 0 -- "${pytest_args[@]}"

%else
%pyproject_check_import -t
%endif


%files -n %{srcname}-tools
%{_bindir}/*

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst 

%changelog
%autochangelog
