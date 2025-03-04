Name:           spglib
Summary:        C library for finding and handling crystal symmetries
Version:        2.5.0
Release:        %autorelease
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://spglib.readthedocs.io/

Source:         https://github.com/spglib/spglib/archive/refs/tags/v%{version}.tar.gz

Patch:          https://github.com/spglib/spglib/commit/8e342ccbaaa6a06b9b4ab2a4a32d511e3cf4e174.patch#/fix-python-metadata.patch

BuildRequires:  ninja-build
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  cmake(GTest)
BuildRequires:  python3-devel

%description
C library for finding and handling crystal symmetries.

%package        devel
Summary:        Development files for spglib
Requires:       spglib%{?_isa} = %{version}-%{release}

%description    devel
This package contains libraries and header files for developing
applications that use spglib.

%package        fortran
Summary:        Runtime files for spglib Fortran bindings
Requires:       spglib = %{version}-%{release}
Requires:       gcc-gfortran%{_isa}

%description    fortran
This package contains runtime files to run applications that were built
using spglib's Fortran bindings.

%package        fortran-devel
Summary:        Development files for spglib with Fortran bindings
Requires:       spglib-fortran%{?_isa} = %{version}-%{release}
Requires:       spglib-devel = %{version}-%{release}

%description    fortran-devel
This package contains Fortran module and header files for developing
Fortran applications that use spglib.

%package -n     python3-spglib
Summary:        Python3 library of spglib
Requires:       spglib = %{version}

%description -n python3-spglib
This package contains the libraries to
develop applications with spglib Python3 bindings.


%prep
%autosetup -p1 -n spglib-%{version}


%generate_buildrequires
%pyproject_buildrequires -x test


%build
%cmake \
    -DSPGLIB_SHARED_LIBS=ON \
    -DSPGLIB_WITH_Fortran=ON \
    -DSPGLIB_WITH_Python=OFF \
    -DSPGLIB_WITH_TESTS=ON \
    -DCMAKE_INSTALL_MODULEDIR=%{_fmoddir}

%cmake_build
%pyproject_wheel


%install
%cmake_install

%pyproject_install
%pyproject_save_files spglib

rm %{buildroot}%{python3_sitearch}/spglib/lib/libsymspg.so*
rm %{buildroot}%{python3_sitearch}/spglib/include/spglib.h
# Delete from pyproject_files as well
sed -i "/libsymspg.so/d" %{pyproject_files}
sed -i "/spglib.h/d" %{pyproject_files}


%check
%ctest
# Need to set LD_LIBRARY_PATH manually for this test
LD_LIBRARY_PATH=%{buildroot}%{_libdir} %pytest -v


%files
%doc README.md
%license COPYING
%{_libdir}/libsymspg.so.*

%files fortran
%{_libdir}/libspglib_f08.so.*

%files devel
%{_libdir}/libsymspg.so
%{_includedir}/spglib.h
%{_libdir}/cmake/Spglib
%exclude %{_libdir}/cmake/Spglib/SpglibTargets_fortran*
%{_libdir}/pkgconfig/spglib.pc

%files fortran-devel
%{_libdir}/libspglib_f08.so
%{_includedir}/spglib_f08.F90
%{_fmoddir}/spglib_f08.mod
%{_libdir}/pkgconfig/spglib_f08.pc
%{_libdir}/cmake/Spglib/SpglibTargets_fortran*

%files -n python3-%{name} -f %{pyproject_files}


%changelog
%autochangelog
