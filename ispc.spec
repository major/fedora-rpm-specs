%global with_snapshot 1
%global commit ec62d6cbef2fab4c49003c0206716d3d6248b59e
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:		ispc
Version:	1.19.0
%if %{with_snapshot}
Release:	%autorelease -p -s 20230102git%{shortcommit}
%else
Release:	%autorelease
%endif
Summary:	C-based SPMD programming language compiler

License:	BSD-3-Clause
URL:		https://ispc.github.io/
%if %{with_snapshot}
Source0:	https://github.com/%{name}/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
%else
Source0:	https://github.com/%{name}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
%endif
BuildRequires:	bison
BuildRequires:	cmake
BuildRequires:	clang-devel
BuildRequires:	doxygen
BuildRequires:	flex 
BuildRequires:	gcc-c++
BuildRequires:	llvm-devel
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	pkgconfig(python3)
# Hardcoded path from 32-bit glibc-devel needed to build
# See https://github.com/ispc/ispc/wiki/Building-ispc:-Linux-and-Mac-OS-X
%ifarch x86_64
BuildRequires:	/usr/lib/crt1.o
%endif
BuildRequires:	pkgconfig(zlib)

# Upstream only supports these architectures
ExclusiveArch:	x86_64 aarch64

# https://fedoraproject.org/wiki/Changes/Stop-Shipping-Individual-Component-Libraries-In-clang-lib-Package
# 
Patch0:	0001-Link-against-libclang-cpp.so.patch

%description
A compiler for a variant of the C programming language, with extensions for
"single program, multiple data" (SPMD) programming.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
 applications that use %{name}.
 
%prep
%if %{with_snapshot}
%autosetup -n %{name}-%{commit} -p1
%else
%autosetup -n %{name}-%{version} -p1
%endif

# Use gcc rather clang by default
sed -i 's|set(CMAKE_C_COMPILER "clang")|set(CMAKE_C_COMPILER "gcc")|g' CMakeLists.txt
sed -i 's|set(CMAKE_CXX_COMPILER "clang++")|set(CMAKE_CXX_COMPILER "g++")|g' CMakeLists.txt

# Delete unrecognized command options from gcc-c++
sed -i 's|-Wno-c99-extensions -Wno-deprecated-register||g' CMakeLists.txt

# Suppress warning message as error
sed -i 's| -Werror ||g' CMakeLists.txt 

# Fix all Python shebangs recursively in .
%py3_shebang_fix .

%build
%cmake \
	-DCMAKE_BUILD_TYPE=Release \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DCMAKE_EXE_LINKER_FLAGS="%{optflags} -fPIE" \
	-DISPC_INCLUDE_EXAMPLES=OFF \
	-DISPC_INCLUDE_TESTS=OFF \
	-DISPC_NO_DUMPS=ON \
	-DLEVEL_ZERO_INCLUDE_DIR=%{_includedir} \
	-DLEVEL_ZERO_LIB_LOADER=%{_libddir} \
	-DLLVM_ENABLE_ASSERTIONS=OFF 
%cmake_build

%install
%cmake_install

#Remove static file
rm %{buildroot}%{_libdir}/lib%{name}rt_static.a

%files
%license LICENSE.txt
%{_bindir}/%{name}
%{_bindir}/check_isa
%{_libdir}/lib%{name}rt.so.1
%{_libdir}/lib%{name}rt.so.%{version}

%files devel
%{_includedir}/%{name}rt/
%{_libdir}/cmake/%{name}rt-%{version}/
%{_libdir}/lib%{name}rt.so

%changelog
%autochangelog
