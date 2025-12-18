# Default to clang unless building with GCC explicitly
%bcond          gcc 0

Name:           ispc
Version:        1.29.0
Release:        %autorelease
Summary:        C-based SPMD programming language compiler
License:        BSD-3-Clause
URL:            https://ispc.github.io/
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

# Build dependencies
BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  flex
BuildRequires:  help2man
BuildRequires:  llvm-devel
BuildRequires:  make
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(tbb)
BuildRequires:  clang-devel
%if %{with gcc}
BuildRequires:  gcc-c++
%endif
%ifarch x86_64
BuildRequires:  (glibc32 or glibc-devel(%__isa_name-32))
BuildRequires:  pkgconfig(level-zero)
Recommends:     %{name}-gpu%{?_isa}
%endif

# Supported architectures
ExclusiveArch:  x86_64 aarch64

%description
A compiler for a variant of the C programming language with extensions for
"single program, multiple data" (SPMD) programming.

# Development subpackage
%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development headers and CMake configuration for %{name}.

# GPU runtime subpackage (only for x86_64)
%ifarch x86_64
%package gpu
Summary:        GPU runtime for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description gpu
GPU runtime libraries for %{name}, required for running ISPC programs on GPUs.
%endif

# Static libraries subpackage
%package static
Summary:        Static libraries for %{name}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description static
Static libraries for developing programs with %{name}.

%prep
%autosetup -p1 -n %{name}-%{version}

# Remove GCC-only warning suppression
sed -i 's|-Wno-c99-extensions -Wno-deprecated-register||g' CMakeLists.txt

# Fix Python shebangs
%py3_shebang_fix .

%build
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
%if %{with gcc}
    -DCMAKE_C_COMPILER=gcc \
    -DCMAKE_CXX_COMPILER=g++ \
%endif
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

# Generate and install man pages.
install -d '%{buildroot}%{_mandir}/man1'
for cmd in %{buildroot}%{_bindir}/*
do
  LD_LIBRARY_PATH='%{buildroot}%{_libdir}' \
      help2man \
      --no-info --no-discard-stderr --version-string='%{version}' \
      --output="%{buildroot}%{_mandir}/man1/$(basename "${cmd}").1" \
      "${cmd}"
done

%check
PATH="${PATH}:%{buildroot}%{_bindir}" %{python3} scripts/run_tests.py

%files
%license LICENSE.txt
%doc docs/ReleaseNotes.txt
%{_bindir}/check_isa
%{_bindir}/%{name}
%{_libdir}/lib%{name}.so.{1,%{version}}
%{_libdir}/lib%{name}rt.so.{1,%{version}}
%{_libdir}/lib%{name}rt_device_cpu.so.{1,%{version}}
%{_mandir}/man1/check_isa.1.gz
%{_mandir}/man1/%{name}.1.gz

%files devel
%doc docs/ReleaseNotes.txt
%{_includedir}/intrinsics/
%{_includedir}/%{name}/
%{_includedir}/%{name}rt/
%{_includedir}/stdlib/
%{_libdir}/cmake/%{name}/
%{_libdir}/cmake/%{name}rt-%{version}/
%{_libdir}/lib%{name}.so
%{_libdir}/lib%{name}rt.so
%{_libdir}/lib%{name}rt_device_cpu.so
%{_libdir}/lib%{name}rt_device_gpu.so

%ifarch x86_64
%files gpu
%doc docs/ReleaseNotes.txt
%{_libdir}/lib%{name}rt_device_gpu.so.{1,%{version}}
%endif

%files static
%license LICENSE.txt
%doc docs/ReleaseNotes.txt
%{_libdir}/lib%{name}rt_static.a

%changelog
%autochangelog
