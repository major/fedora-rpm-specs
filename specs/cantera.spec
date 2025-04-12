# RPATH issues are standard paths and result from upstream
%global __brp_check_rpaths %{nil}

Name:          cantera
Version:       3.1.0
Release:       %{?autorelease}
Summary:       Chemical kinetics, thermodynamics, and transport tool suite
# Automatically converted from old format: BSD - review is highly recommended.
License:       LicenseRef-Callaway-BSD
URL:           https://github.com/Cantera/%{name}/
Source0:       %{url}archive/refs/tags/v%{version}.tar.gz
Source1:       https://github.com/Cantera/cantera-example-data/archive/refs/heads/main.tar.gz

BuildRequires:  boost-devel
BuildRequires:  eigen3-devel
BuildRequires:  fmt-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  hdf5-devel
BuildRequires:  highfive-devel
BuildRequires:  python3-devel
BuildRequires:  python3-numpy
BuildRequires:  python3-pip
BuildRequires:  python3-pytest
BuildRequires:  python3-scipy
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  sundials-devel
BuildRequires:  yaml-cpp-devel


%if 0%{?suse_version}
BuildRequires:  gmock
BuildRequires:  gtest
BuildRequires:  scons
BuildRequires:  python3-Cython
BuildRequires:  python3-numpy-devel
BuildRequires:  python3-Pint
BuildRequires:  python3-ruamel.yaml
%else
BuildRequires:  gmock-devel
BuildRequires:  gtest-devel
BuildRequires:  python3-cython
BuildRequires:  python3-pint
BuildRequires:  python3-scons
BuildRequires:  python3-ruamel-yaml
%endif

%if 0%{?fedora} || 0%{?suse_version}
BuildRequires:  gcc-fortran
BuildRequires:  python3-pandas
%else
BuildRequires:  gcc-gfortran
%endif

%global scons scons%{?rhel:-3}

ExcludeArch: %{ix86}

%global common_description %{expand:
Cantera is a suite of object-oriented software tools for solving problems
involving chemical kinetics, thermodynamics, and/or transport processes.
Cantera can be used for simulating time-dependent or steady reactor
networks and one-dimensional reacting flows. Thermodynamic models for
ideal gases, aqueous electrolytes, plasmas, and multiphase substances
are provided.}

%description %{common_description}


%package common
Summary: Common files needed for all Cantera interfaces
%description common %{common_description}

This package includes programs for parsing and converting chemical
mechanisms, a set of common mechanism files, and several sample problems.


%package -n python3-%{name}
Requires: %{name}-common%{_isa} = %{version}-%{release}
Recommends: python3-pint
Summary: Python 3 user interface for Cantera
%description -n python3-%{name} %{common_description}

This package includes the Cantera Python 3 module.


%package devel
Requires: %{name}-common%{_isa} = %{version}-%{release}
Summary: Header files and shared object libraries for Cantera
%description devel %{common_description}

This package contains the header files and shared object libraries needed to
develop applications with the C++ and Fortran interfaces of Cantera.


%package static
Requires: %{name}-common%{_isa} = %{version}-%{release}
Summary: Static libraries for Cantera
%description static %{common_description}

This package contains the static libraries for the C++ and Fortran
interfaces of Cantera.


%prep
%autosetup -n %{name}-%{version} -p1 0
gzip -dc %{S:1} | tar -xvvf - --strip-components=1 -C data/example_data

%build
%set_build_flags

%scons build \
    extra_inc_dirs=%{_includedir}/eigen3:%{_includedir}/highfive \
    f90_interface=y \
    hdf_support=y \
    libdirname=%{_lib} \
    prefix=%{_prefix} \
    python_package=y \
    python_prefix=%{_prefix} \
    renamed_shared_libraries=n \
    system_eigen=y \
    system_fmt=y \
    system_highfive=y \
    system_sundials=y \
    system_yamlcpp=y \
    system_blas_lapack=y \
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
%{_bindir}/lxcat2yaml
%{_bindir}/yaml2ck

%{_datadir}/%{name}

#not required for packaged installations
%ghost %{_bindir}/setup_cantera
%ghost %{_bindir}/setup_cantera.csh


%files -n python3-%{name}
%{python3_sitearch}/%{name}/
%{python3_sitearch}/*-%{version}.dist-info/

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
