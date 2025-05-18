Name:		ispc
Version:	1.27.0
Release:	%autorelease
Summary:	C-based SPMD programming language compiler

License:	BSD-3-Clause
URL:		https://ispc.github.io/
Source0:	https://github.com/%{name}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

#Patch0:		aarch64-tests.patch

BuildRequires:	bison
BuildRequires:	cmake
BuildRequires:	clang-devel
BuildRequires:	flex 
BuildRequires:	gcc-c++
BuildRequires:	llvm-devel
BuildRequires:	pkgconfig(python3)
%ifarch x86_64
# Koji 64-bit buildroots do not contain packages from 32-bit builds, therefore
# the 'glibc-devel.i686' variant is provided as 'glibc32'.
BuildRequires: (glibc32 or glibc-devel(%__isa_name-32))
BuildRequires:	oneapi-level-zero-devel
%endif
BuildRequires:  pkgconfig(tbb)

# Upstream only supports these architectures
ExclusiveArch:	x86_64 aarch64

%description
A compiler for a variant of the C programming language, with extensions for
"single program, multiple data" (SPMD) programming.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
applications that use %{name}.

%package	static
Summary:	Static libraries for %{name} development
Requires:	%{name}-devel%{?_isa} = %{version}-%{release}

%description	static
The %{name}-static package includes static libraries needed
to develop programs that use %{name}.

%prep
%autosetup -p1 -n %{name}-%{version}

# Delete unrecognized command options from gcc-c++
sed -i 's|-Wno-c99-extensions -Wno-deprecated-register||g' CMakeLists.txt

# Fix all Python shebangs recursively in .
%py3_shebang_fix .

%build
%cmake \
	-DCMAKE_BUILD_TYPE=Release \
	-DCMAKE_C_COMPILER=gcc \
	-DCMAKE_CXX_COMPILER=g++ \
	-DCMAKE_EXE_LINKER_FLAGS="%{optflags} -fPIE" \
	-DISPC_INCLUDE_EXAMPLES=OFF \
	-DISPC_INCLUDE_TESTS=ON \
%ifarch x86_64
	-DLEVEL_ZERO_INCLUDE_DIR=%{_includedir} \
	-DLEVEL_ZERO_LIB_LOADER=%{_libdir}/libze_loader.so.1 \
	-DISPCRT_BUILD_CPU=ON \
	-DISPCRT_BUILD_GPU=ON \
	-DISPCRT_BUILD_TESTS=OFF \
%endif
	-DLLVM_ENABLE_ASSERTIONS=OFF
%cmake_build

%install
%cmake_install

%check
PATH="${PATH}:%{buildroot}%{_bindir}" %{python3} scripts/run_tests.py

%files
%license LICENSE.txt
%{_bindir}/%{name}
%{_bindir}/check_isa
%{_libdir}/lib%{name}rt.so.{1,%{version}}
%{_libdir}/lib%{name}rt_device_cpu.so.{1,%{version}}
%ifarch x86_64
%{_libdir}/lib%{name}rt_device_gpu.so.{1,%{version}}
%endif

%files devel
%{_includedir}/%{name}rt/
%{_libdir}/cmake/%{name}rt-%{version}/
%{_libdir}/lib%{name}rt.so
%{_libdir}/lib%{name}rt_device_cpu.so
%ifarch x86_64
%{_libdir}/lib%{name}rt_device_gpu.so
%endif

%files static
%license LICENSE.txt
%{_libdir}/lib%{name}rt_static.a

%changelog
%autochangelog
