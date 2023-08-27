# RPATH issues are standard paths and result from upstream
%global __brp_check_rpaths %{nil}
%global debug_package %{nil}
%global fork Cantera

Name:          cantera
Version:       3.0.0
Release:       %{?autorelease}%{!?autorelease:22{?dist}} 
Summary:       Chemical kinetics, thermodynamics, and transport tool suite
License:       BSD
URL:           https://github.com/%{fork}/%{name}/
Source0:       %{url}archive/refs/tags/v%{version}.tar.gz

# Python 3.12 currently in pre-release and not officially supported
Patch0:        add-python3_12.patch

BuildRequires:  boost-devel
BuildRequires:  eigen3-devel
BuildRequires:  fmt-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  gmock-devel
BuildRequires:  gtest-devel
BuildRequires:  python3
BuildRequires:  python3-Cython
BuildRequires:  python3-devel
BuildRequires:  python3-h5py
BuildRequires:  python3-numpy
BuildRequires:  python3-pandas
BuildRequires:  python3-pint
BuildRequires:  python3-pip
BuildRequires:  python3-pytest
BuildRequires:  python3-ruamel-yaml
BuildRequires:  python3-scipy
BuildRequires:  python3-scons
BuildRequires:  python3-wheel
BuildRequires:  sundials-devel
BuildRequires:  yaml-cpp-devel

%if 0%{?fedora}
BuildRequires:  gcc-fortran
%else
BuildRequires:  gcc-gfortran
%endif

%global scons scons%{?rhel:-3}

ExcludeArch: %{ix86}

%global common_description %{expand: \
 Cantera is a suite of object-oriented software tools for solving problems
 involving chemical kinetics, thermodynamics, and/or transport processes.
 Cantera can be used for simulating time-dependent or steady reactor
 networks and one-dimensional reacting flows. Thermodynamic models for
 ideal gases, aqueous electrolytes, plasmas, and multiphase substances
 are provided.}

%description
%{common_description}


%package common
Summary: Common files needed for all Cantera interfaces
%description common
%{common_description}
 .
 This package includes programs for parsing and converting chemical
 mechanisms, a set of common mechanism files, and several sample problems.


%package -n python3-%{name}
Requires: %{name}-common%{_isa} = %{version}-%{release}
Summary: Python 3 user interface for Cantera
%description -n python3-%{name}
%{common_description}
 .
 This package includes the Cantera Python 3 module.


%package devel
Requires: %{name}-common%{_isa} = %{version}-%{release}
Summary: Header files and shared object libraries for Cantera
%description devel
%{common_description}
 .
 This package contains the header files and shared object libraries needed to
 develop applications with the C++ and Fortran interfaces of Cantera.


%package static
Requires: %{name}-common%{_isa} = %{version}-%{release}
Summary: Static libraries for Cantera
%description static
%{common_description}
 .
 This package contains the static libraries for the C++ and Fortran
 interfaces of Cantera.


%prep
%autosetup -n %{name}-%{version} -p1

%build
%set_build_flags

%scons build \
    extra_inc_dirs=%{_includedir}/eigen3 \
    f90_interface=y \
    libdirname=%{_lib} \
    prefix=%{_prefix} \
    python_package=full \
    python_prefix=%{_prefix} \
    renamed_shared_libraries=n \
    system_eigen=y \
    system_fmt=y \
    system_sundials=y \
    %{?_smp_mflags}


%install
%scons install \
    libdirname=%{_lib} \
    prefix=%{_prefix} \
    python_prefix=%{_prefix} \
    stage_dir=%{buildroot} \
    %{nil}

%check
%scons test %{?_smp_mflags}


%files common
%license %{_datadir}/%{name}/doc/LICENSE.txt

%doc AUTHORS README.rst
%doc %{_mandir}/man1/ck2yaml.1.gz
%doc %{_mandir}/man1/cti2yaml.1.gz
%doc %{_mandir}/man1/ctml2yaml.1.gz
%doc %{_mandir}/man1/yaml2ck.1.gz

%{_bindir}/ck2yaml
%{_bindir}/cti2yaml
%{_bindir}/ctml2yaml
%{_bindir}/yaml2ck

%{_datadir}/%{name}

#not required for packaged installations
%ghost %{_bindir}/setup_cantera
%ghost %{_bindir}/setup_cantera.csh


%files -n python3-%{name}
%{python3_sitearch}/%{name}/
%{python3_sitearch}/Cantera-%{version}.dist-info/

%files devel
%{_includedir}/%{name}

%{_libdir}/pkgconfig/cantera.pc
%{_libdir}/libcantera.so
%{_libdir}/libcantera.so.3
%{_libdir}/libcantera.so.%{version}
%{_libdir}/libcantera_fortran.so
%{_libdir}/libcantera_fortran.so.3
%{_libdir}/libcantera_fortran.so.%{version}
%{_libdir}/libcantera_python*.so


%files static
%{_libdir}/libcantera.a
%{_libdir}/libcantera_fortran.a


%changelog
%autochangelog
