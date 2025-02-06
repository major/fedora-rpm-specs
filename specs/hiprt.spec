%global upstreamname HIPRT

%bcond_with debug
%if %{with debug}
%global build_type DEBUG
%else
%global build_type RelWithDebInfo
%endif

%global lib_suffix 64

# Needs a supported gpu
%bcond_with check
%if %{with check}
%global build_no_test OFF
%else
%global build_no_test ON
%endif

%global __cmake_in_source_build 1

%global toolchain clang

ExclusiveArch: x86_64

Name:           hiprt
Version:        2.5
%global xver    cfa5e2a
Release:        %autorelease -e %{xver}

License:        Apache-2.0 AND BSD-3-Clause AND MIT AND NCSA
Summary:        HIP Raytracing
URL:            https://github.com/GPUOpen-LibrariesAndSDKs/%{upstreamname}
Source0:        %{url}/archive/refs/tags/%{version}.%{xver}.tar.gz
# https://github.com/GPUOpen-LibrariesAndSDKs/HIPRT/issues/22
Patch0:         0001-hiprt-soversion.patch
# Not upstreamable, nvidia is not an option for fedora but is for upstream.
Patch2:         0001-disable-cuda-test.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  python-unversioned-command
BuildRequires:  python3-devel
BuildRequires:  rocm-clang
BuildRequires:  rocm-compilersupport-macros
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-runtime-devel

%description
HIP RT is a ray tracing library for HIP, making it easy to write ray-tracing
applications in HIP. The APIs and library are designed to be minimal, lower
level, and simple to use and integrate into any existing HIP applications.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
%{summary}

%prep
%autosetup -p1 -n %{upstreamname}-%{version}.%{xver}

# GAH.. binaries
rm -rf contrib/easy-encryption/bin
rm -rf contrib/Orochi/contrib/bin

# Need a reasonable version
sed -i -e 's@HIPRT_SO_VERSION@%{version}@' CMakeLists.txt
# bin?? 
sed -i -e 's@install(TARGETS ${HIPRT_NAME} DESTINATION bin)@install(TARGETS ${HIPRT_NAME} DESTINATION %{_lib})@' CMakeLists.txt
# No building nvidia things
sed -i -e 's@compile.py --nvidia@compile.py @' CMakeLists.txt
sed -i -e 's@precompile_bitcode.py --nvidia@precompile_bitcode.py @' CMakeLists.txt

# Tutorial uses Orochi symbols, which are hidden on linux but not windows, unhide
sed -i -e 's@-fvisibility=hidden@-fvisibility=default@' CMakeLists.txt
%build

%cmake -G Ninja $src \
       -DCMAKE_BUILD_TYPE=%{build_type} \
       -DCMAKE_CXX_COMPILER=%rocmllvm_bindir/clang++ \
       -DCMAKE_C_COMPILER=%rocmllvm_bindir/clang \
      -DBAKE_KERNEL=OFF \
      -DBITCODE=ON \
      -DPRECOMPILE=ON \
      -DNO_ENCRYPT=ON \
      -DNO_UNITTEST=%{build_no_test} \
      -DHIP_PATH=%{_prefix} \

%if %{with debug}
%cmake_build --config DEBUG
%else
%cmake_build --config RELEASE
%endif

%if %{with check}
%check
cd dist
./bin/%{build_type}/unittest64
%endif

%install
%cmake_install

# Bitcode install needs help
install --mode=644 scripts/bitcodes/*.bc %{buildroot}%{_libdir}
install --mode=644 scripts/bitcodes/*.hipfb %{buildroot}%{_libdir}

# Orochi needs some help
rm -rf %{buildroot}%{_includedir}/contrib/Orochi
mkdir %{buildroot}%{_includedir}/Orochi
install --mode=644 contrib/Orochi/Orochi/*.h %{buildroot}%{_includedir}/Orochi
# mv hipew.h so it is usable
install --mode=644 contrib/Orochi/contrib/hipew/include/hipew.h %{buildroot}%{_includedir}/Orochi
sed -i -e 's@../contrib/hipew/include/hipew.h@hipew.h@' %{buildroot}%{_includedir}/Orochi/Orochi.h

%files
%license license.txt
%{_libdir}/lib%{name}%{lib_suffix}.so.*
%{_libdir}/*.bc
%{_libdir}/*.hipfb

%files devel
%{_includedir}/%{name}
%{_includedir}/Orochi
%{_libdir}/lib%{name}%{lib_suffix}.so

%changelog
%autochangelog
