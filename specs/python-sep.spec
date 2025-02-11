%global srcname sep

Name: python-%{srcname}
Version: 1.4.0
Release: %autorelease
Summary: Astronomical source extraction and photometry in Python

# Code from photutils is BSD (src/overlap.h)
# Code from sextractor is LGPLv3
# Python wrapper is MIT (sex.pyx)
License: MIT AND LGPL-3.0-only AND BSD-3-Clause

URL: http://sep.readthedocs.org/
Source0: %{pypi_source}
# https://github.com/sep-developers/sep/issues/165
Patch: sep_version.patch

BuildRequires: gcc
BuildRequires: python3-devel

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

%description
SEP makes available some of the astronomical source extraction and 
photometry algorithms in Source Extractor as stand-alone 
functions and classes. These operate directly on in-memory numpy arrays 
(no FITS files, configuration files, etc). It’s derived directly from 
(and tested against) the Source Extractor code base.

%package -n python3-%{srcname}
Summary: Astronomical source extraction and photometry in Python
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
SEP makes available some of the astronomical source extraction and 
photometry algorithms in Source Extractor as stand-alone 
functions and classes. These operate directly on in-memory numpy arrays 
(no FITS files, configuration files, etc). It’s derived directly from 
(and tested against) the Source Extractor code base.


%prep
%autosetup -n %{srcname}-%{version}
# Unpin setuptools
sed -i -e "s/setuptools>=61.0, <72.2.0/setuptools/"  pyproject.toml
# https://github.com/sep-developers/sep/issues/165
mv src/_version.py src/sep_version.py

%generate_buildrequires
%pyproject_buildrequires -e py-linux

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files sep sep_version

%check
%ifarch s390x
%pyproject_check_import -t
%else
%pyproject_check_import -t
%tox
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%doc AUTHORS.md README.md CHANGES.md
%license licenses/MIT_LICENSE.txt licenses/LGPL_LICENSE.txt licenses/BSD_LICENSE.txt

%changelog
%autochangelog
