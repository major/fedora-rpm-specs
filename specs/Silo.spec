Name:           Silo
Version:        4.12.0
%global sover   412
Release:        2%{?dist}
Summary:        Mesh and Field I/O Library and Scientific Database

License:        BSD-3-Clause 
URL:            https://silo.llnl.gov/
Source0:        https://github.com/LLNL/Silo/archive/%{version}/%{name}-%{version}.tar.gz
# Fix build with python-3.14
Patch0:         https://patch-diff.githubusercontent.com/raw/llnl/Silo/pull/533.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  hdf5-devel 
BuildRequires:  qt6-qtbase-devel 
BuildRequires:  python3-devel
BuildRequires:  perl-interpreter

%global silo_desc \
Silo is a C/Fortran API for reading and writing a wide variety of \
scientific data to binary files. Silo files can be easily shared and \
exchanged between wholly independently developed applications running \
on disparate computing platforms. Consequently, Silo facilitates the \
development of general purpose tools for processing scientific data. \
One of the more popular tools to process Silo data is the VisIt \
visualization tool. Silo supports a variety of mesh types including \
simple curves, gridless (point), structured, unstructured-zoo and \
unstructured-arbitrary, block structured AMR, and constructive solid \
geometry (CSG).

%description
%{silo_desc}

%package devel
Summary:        Development files for the %{name} package
Requires:       %{name} = %{version}-%{release}
%description devel
%{silo_desc}

This package contains the development files of %{name}.

%package python
Summary:        Python module for the %{name} package
Requires:       %{name} = %{version}-%{release}
%description python
%{silo_desc}

This package contains the python module of the %{name} package.
%prep
%autosetup -p1

%build
# json support is still experimental
%cmake \
  -DBUILD_TESTING=ON \
  -DSILO_ENABLE_SHARED=ON \
  -DSILO_ENABLE_SILOCK=ON \
  -DSILO_ENABLE_SILEX=ON \
  -DSILO_ENABLE_BROWSER=ON \
  -DSILO_ENABLE_FORTRAN=ON \
  -DSILO_ENABLE_HDF5=ON \
  -DSILO_ENABLE_JSON=OFF \
  -DSILO_ENABLE_PYTHON_MODULE=ON \
  -DSILO_INSTALL_PYTHONDIR=%{python3_sitelib} \
  -DSILO_ENABLE_TESTS=ON \
  -DCMAKE_SKIP_INSTALL_RPATH=ON \
  -DSILO_BUILD_FOR_BSD_LICENSE=ON \
  %{nil}
%cmake_build

%install
%cmake_install

%check
# LLNL/Silo#504, memfile_simple-hdf5 is broken on s390x
%ifarch s390x
%global testargs --exclude-regex memfile_simple-hdf5
%endif

# LLNL/Silo#502, parallel testing not supported
%ctest --parallel 1 %{?testargs}

%files
%doc README.md
%license LICENSE
%{_bindir}/browser
%{_bindir}/silock
%{_bindir}/silodiff
%{_bindir}/silofile
%{_bindir}/silex
%{_bindir}/s2ex.py
%{_libdir}/libsiloh5.so.%{sover}

%files devel
%{_includedir}/silo.h
%{_includedir}/silo.inc
%{_includedir}/silo_FC.h
%{_includedir}/silo_exports.h
%{_includedir}/silo_f9x.inc
%{_includedir}/pmpio.h
%{_libdir}/cmake/%{name}/SiloConfig.cmake
%{_libdir}/cmake/%{name}/SiloConfigVersion.cmake
%{_libdir}/cmake/%{name}/SiloTargets-release.cmake
%{_libdir}/cmake/%{name}/SiloTargets.cmake
%{_libdir}/libsiloh5.so
%{_libdir}/libsiloh5.so.4*

%files python
%{python3_sitelib}/Silo.so

%changelog
* Wed Apr 08 2026 Christoph Junghans <junghans@votca.org> - 4.12.0-2
- Review comments from bug #2416748
- Fixes: rhbz#2416748

* Mon Nov 24 2025 Christoph Junghans <junghans@votca.org> - 4.12.0-1
- Initial commit

