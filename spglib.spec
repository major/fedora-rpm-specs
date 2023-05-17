%bcond_without python

Name:    spglib
Summary: C library for finding and handling crystal symmetries
Version: 2.0.2
Release: %{autorelease}
License: BSD
URL:     https://spglib.github.io/%{name}/
Source0: https://github.com/atztogo/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:  spglib-unbundle_gtest.patch

BuildRequires: make
BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: gcc-gfortran
BuildRequires: gtest-devel

%description
C library for finding and handling crystal symmetries.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains libraries and header files for developing
applications that use spglib.


%package        fortran
Summary:        Runtime files for %{name} Fortran bindings
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gcc-gfortran%{?_isa}

%description    fortran
This package contains runtime files to run applications that were built
using %{name}'s Fortran bindings.

%package        fortran-devel
Summary:        Development files for %{name} with Fortran bindings
Requires:       %{name}-fortran%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description    fortran-devel
This package contains Fortran module and header files for developing
Fortran applications that use %{name}.

%if %{with python}
%package -n python3-%{name}
Summary: Python3 library of %{name}
BuildRequires: python3-devel
BuildRequires: python3-pip
BuildRequires: python3-setuptools
BuildRequires: python3-wheel
BuildRequires: python3-pytest
BuildRequires: python3-pyyaml

%description -n python3-%{name}
This package contains the libraries to 
develop applications with %{name} Python3 bindings.
%endif

%prep
%autosetup -n %{name}-%{version} -p1

%if %{with python}
%generate_buildrequires
%pyproject_buildrequires -N python/requirements.txt
%endif

%build
%cmake -DCMAKE_INSTALL_INCLUDEDIR:PATH=include/%{name} \
       -DSPGLIB_SHARED_LIBS=ON \
       -DSPGLIB_WITH_Python=ON \
       -DSPGLIB_WITH_TESTS=ON \
       -DWITH_Fortran:BOOL=ON
%cmake_build

pushd test
export CXXFLAGS="%{build_cxxflags} -Wl,--copy-dt-needed-entries"
%cmake
%cmake_build
popd

%if %{with python}
pushd python
%pyproject_wheel
%endif

%install
%cmake_install

# Remove static libraries
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a

# Move fortran libraries
mkdir -p $RPM_BUILD_ROOT%{_fmoddir}
mv $RPM_BUILD_ROOT%{_libdir}/*.mod $RPM_BUILD_ROOT%{_fmoddir}/

%if %{with python}
pushd python
%pyproject_install
%pyproject_save_files %{name}
%endif

%check
pushd test
%ctest
popd
%if %{with python}
pushd python
%pytest -v
%endif

%files
%doc README.md
%license COPYING
%{_libdir}/libsymspg.so.1
%{_libdir}/libsymspg.so.2.0.2

%files devel
%{_libdir}/libsymspg.so
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%{_libdir}/pkgconfig/spglib.pc

%files fortran
%{_libdir}/libspglib_f08.so.1
%{_libdir}/libspglib_f08.so.2.0.2

%files fortran-devel
%{_bindir}/spglib_example_fortran.X
%{_libdir}/libspglib_f08.so
%{_includedir}/%{name}/spglib_f08.f90
%{_fmoddir}/spglib_f08.mod
%{_libdir}/pkgconfig/spglib_f08.pc
%dir %{_includedir}/%{name}

%if %{with python}
%files -n python3-%{name} -f %{pyproject_files}
%license COPYING
%{python3_sitearch}/%{name}/
%{python3_sitearch}/%{name}-*.dist-info/
%endif

%changelog
%autochangelog
