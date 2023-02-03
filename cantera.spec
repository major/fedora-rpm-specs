%global fork Cantera

Name:          cantera
Version:       2.6.0
Release:       %{?autorelease}%{!?autorelease:22{?dist}} 
Summary:       Chemical kinetics, thermodynamics, and transport tool suite
License:       BSD
URL:           https://github.com/%{fork}/%{name}/
Source0:       %{url}archive/refs/tags/v%{version}.tar.gz

# thermoToYaml test failures on ppc64le and aarch64 and s390x - BZ #2081451
# increase test tolerance to pass
Patch0:        cantera-test-ppc64le-aarch64-s390x.patch

# Fails to build under Python 3.11 due to deprecated mode 'rU' - BZ #2094258
# implement patch until upstream releases fix
Patch1:        cantera-py311-deprecated-U.patch

# Fix failure to build with pip >= 21.1
# Fixed upstream: https://github.com/Cantera/cantera/pull/1272
Patch2:        fix-pip-build-21.1.patch

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
BuildRequires:  python3-numpy
BuildRequires:  python3-pip
BuildRequires:  python3-pytest
BuildRequires:  python3-ruamel-yaml
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
%setup -n %{name}-%{version}
%patch0 -p0
%patch1 -p1
%patch2 -p1

%build
%set_build_flags

%scons build \
    cxx_flags='-std=c++14' \
    extra_inc_dirs=/usr/include/eigen3 \
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
%doc %{_mandir}/man1/ck2cti.1.gz
%doc %{_mandir}/man1/ctml_writer.1.gz

%{_bindir}/ck2yaml
%{_bindir}/cti2yaml
%{_bindir}/ctml2yaml
%{_bindir}/ctml_writer
%{_bindir}/ck2cti

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
%{_libdir}/libcantera.so.2
%{_libdir}/libcantera.so.%{version}
%{_libdir}/libcantera_fortran.so
%{_libdir}/libcantera_fortran.so.2
%{_libdir}/libcantera_fortran.so.%{version}


%files static
%{_libdir}/libcantera.a
%{_libdir}/libcantera_fortran.a


%changelog
%autochangelog
