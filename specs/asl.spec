# ASL upstream has not tagged any releases, so we use a git checkout
%global commit     ae937db9bd1169ec2c4cb8d75196f67cdcb8041b
%global date       20241212
%global forgeurl   https://github.com/ampl/asl

Name:           asl
Version:        20241122
Summary:        AMPL Solver Library

%forgemeta

# AMPL files are licensed with BSD-3-Clause.
# NETLIB files are licensed with SMLNJ.
License:        BSD-3-Clause AND SMLNJ
Release:        %autorelease
URL:            %{forgeurl}
VCS:            git:%{forgeurl}.git
Source:         %{forgesource}
# Build the C++ interface as a shared library instead of a static library
Patch:          %{name}-shared.patch
# Do not override Fedora architecture flags
Patch:          %{name}-arch-flags.patch

BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran

%description
The AMPL Solver Library is an interface used to access a variety of
solvers from AMPL code.

%package        devel
Summary:        Header files and library links for asl
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Header files and library links for building projects that use
%{name}.

%prep
%forgeautosetup -p1

%conf
# Fix install location of ampl-asl-config
sed -i 's,share/,lib/cmake/,' CMakeLists.txt

# Fix install location on 64-bit platforms
if [ "%{_lib}" != "lib" ]; then
  sed -i '/DESTINATION/s/lib/%{_lib}/g' CMakeLists.txt
fi

export CFLAGS="%{build_cflags} -DIGNORE_BOGUS_WARNINGS"
export CXXFLAGS="%{build_cxxflags} -DIGNORE_BOGUS_WARNINGS"
%cmake \
  -DBUILD_CPP:BOOL=ON \
  -DBUILD_EXAMPLES:BOOL=OFF \
  -DBUILD_MT_LIBS:BOOL=ON \
  -DBUILD_SHARED_LIBS:BOOL=ON \
  -DGENERATE_ARITH:BOOL=ON

%build
%cmake_build

%install
%cmake_install

# mp needs uninstalled files
cp -p src/solvers/{dvalue.hd,fg_read.c} %{buildroot}%{_includedir}/asl
cp -p src/solvers2/fg_read.c %{buildroot}%{_includedir}/asl2

# Save space by not duplicating header files between asl and asl2
%fdupes %{buildroot}%{_includedir}

%files
%doc README.md
%license LICENSE LICENSE.2
%{_libdir}/libasl.so.0*
%{_libdir}/libasl-mt.so.0*
%{_libdir}/libasl2.so.0*
%{_libdir}/libasl2-mt.so.0*
%{_libdir}/libaslcpp.so.0*

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
