# ASL upstream has not tagged any releases, so we use a git checkout
%global commit  877221766530d6bde7f15cb8c014eb6f3ca39c58

Name:           asl
Version:        20260109
Release:        %autorelease
Summary:        AMPL Solver Library

# AMPL files are licensed with BSD-3-Clause.
# NETLIB files are licensed with SMLNJ.
# src/solvers{,2}/dtoa.c is licensed with dtoa
License:        BSD-3-Clause AND SMLNJ AND dtoa
URL:            https://github.com/ampl/asl
VCS:            git:%{url}.git
Source:         %{url}/archive/%{commit}/%{name}-%{version}.tar.gz
# Build the C++ interface as a shared library instead of a static library
Patch:          %{name}-shared.patch
# Do not override Fedora architecture flags
Patch:          %{name}-arch-flags.patch

BuildSystem:    cmake
BuildOption(conf): -DBUILD_CPP:BOOL=ON
BuildOption(conf): -DBUILD_EXAMPLES:BOOL=OFF
BuildOption(conf): -DBUILD_MT_LIBS:BOOL=ON
BuildOption(conf): -DBUILD_SHARED_LIBS:BOOL=ON
BuildOption(conf): -DGENERATE_ARITH:BOOL=ON

BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran

%description
The AMPL Solver Library is an interface used to access a variety of solvers
from AMPL code.

%package        devel
Summary:        Header files and library links for asl
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Header files and library links for building projects that use %{name}.

%prep
%autosetup -p1 -n %{name}-%{commit}

%conf -p
# Fix install location of ampl-asl-config
sed -i 's,share/,lib/cmake/,' CMakeLists.txt

# Fix install location on 64-bit platforms
sed -i '/DESTINATION/s/lib/${LIB_INSTALL_DIR}/g' CMakeLists.txt

export CFLAGS="%{build_cflags} -DIGNORE_BOGUS_WARNINGS"
export CXXFLAGS="%{build_cxxflags} -DIGNORE_BOGUS_WARNINGS"

%install -a
# mp needs uninstalled files
cp -p src/solvers/{dvalue.hd,fg_read.c} %{buildroot}%{_includedir}/asl
cp -p src/solvers2/fg_read.c %{buildroot}%{_includedir}/asl2

%files
%doc README.md
%license LICENSE LICENSE.2
%{_libdir}/libasl.so.0{,.*}
%{_libdir}/libasl-mt.so.0{,.*}
%{_libdir}/libasl2.so.0{,.*}
%{_libdir}/libasl2-mt.so.0{,.*}
%{_libdir}/libaslcpp.so.0{,.*}

%files devel
%{_includedir}/asl/
%{_includedir}/asl2/
%{_includedir}/aslcpp/
%{_libdir}/libasl.so
%{_libdir}/libasl-mt.so
%{_libdir}/libasl2.so
%{_libdir}/libasl2-mt.so
%{_libdir}/libaslcpp.so
%{_libdir}/cmake/ampl-asl/

%changelog
%autochangelog
