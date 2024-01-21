Version:        0.30.0
Name:           lfortran
Release:        9%{?dist}
Summary:        A modern Fortran compiler

# Main code is BSD-3-Clause
# src/libasr/codegen/KaleidoscopeJIT.h is available under the Apache 2.0
# License with LLVM exception
License:        BSD-3-Clause AND Apache-2.0 WITH LLVM-exception
URL:            https://lfortran.org/
Source0:        https://lfortran.github.io/tarballs/release/lfortran-%{version}.tar.gz
# fix missing symbols in runtime library
Patch0:         https://github.com/lfortran/lfortran/pull/3043.patch
# https://github.com/lfortran/lfortran/issues/2981
ExclusiveArch: x86_64

BuildRequires: binutils-devel
BuildRequires: bison
BuildRequires: cmake
BuildRequires: fmt-devel
BuildRequires: gcc-c++
BuildRequires: json-devel
BuildRequires: libffi-devel
BuildRequires: libunwind-devel
BuildRequires: libuuid-devel
%if 0%{?fedora} == 38
BuildRequires: llvm-devel
%else
BuildRequires: llvm16-devel
%endif
BuildRequires: libzstd-devel
BuildRequires: libzstd-static
BuildRequires: python3-devel
BuildRequires: rapidjson-devel
BuildRequires: re2c
%if 0%{?fedora} > 39
BuildRequires: zlib-ng-compat-devel
BuildRequires: zlib-ng-compat-static
%else
BuildRequires: zlib-devel
BuildRequires: zlib-static
%endif
# Needed for Jupyter kernel
BuildRequires: cppzmq-devel
BuildRequires: json-devel
BuildRequires: openssl-devel
BuildRequires: xeus-devel
BuildRequires: xeus-zmq-devel
BuildRequires: xtl-devel
# For manpage, drop in next release
BuildRequires: pandoc
# For backend=cpp
BuildRequires: kokkos-devel
# Not explicitly linked, hence listed here
Requires: kokkos-devel

Requires: %{name}-shared%{?_isa} = %{version}-%{release}

%global lfortran_desc \
LFortran is a modern open-source (BSD licensed) interactive Fortran \
compiler built on top of LLVM. It can execute user's code interactively \
to allow exploratory work (much like Python, MATLAB or Julia) as well as \
compile to binaries with the goal to run user's code on modern \
architectures such as multi-core CPUs and GPUs.

%description
%{lfortran_desc}

%package devel
Summary:  Development headers and libraries for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
%{lfortran_desc}

This package contains development headers and libraries for %{name}.

%package static
Summary:   Static runtime library for %{name}

%description static
%{lfortran_desc}

This package contains static runtime library for %{name}.

%package shared
Summary:   Shared runtime library for %{name}

%description shared
%{lfortran_desc}

This package contains shared runtime library for %{name}.

# F38 has no jupyterlab
%if 0%{?fedora} > 38
%package jupyter
Summary:   Jupyter kernel for %{name}
Requires:  %{name}%{?_isa} = %{version}-%{release}
Requires:  jupyterlab
Requires:  python-jupyter-filesystem

%description jupyter
%{lfortran_desc}

This package contains the jupyter kernel for %{name}.
%endif


%prep
%autosetup -p1

%build
%cmake -DCMAKE_PREFIX_PATH=%{_libdir}/llvm16/ \
       -DWITH_LLVM=ON \
       -DWITH_RUNTIME_LIBRARY=ON \
       -DWITH_FMT=ON \
       -DWITH_JSON=ON \
       -DWITH_KOKKOS=ON \
       -DWITH_STACKTRACE=ON \
       -DWITH_TARGET_WASM=ON \
       -DWITH_UNWIND=ON \
       -DWITH_WHEREAMI=OFF \
       -DWITH_XEUS=ON \
       -DWITH_ZLIB=ON
%cmake_build

%install
%cmake_install
%if 0%{?fedora} == 38
%{__rm} -rfv %{buildroot}%{_datadir}/jupyter/kernels
%endif

%check
%ctest

%files
%doc README.md
%license LICENSE
%{_bindir}/lfortran
%{_mandir}/man1/lfortran.1.*

%files devel
%dir %{_includedir}/lfortran
%dir %{_includedir}/lfortran/impure
%{_includedir}/lfortran/impure/lfortran_intrinsics.h
%{_libdir}/liblfortran_runtime.so
%{_libdir}/lfortran_*.mod

%files static
%{_libdir}/liblfortran_runtime_static.a

%files shared
%{_libdir}/liblfortran_runtime.so.*

%if 0%{?fedora} > 38
%files jupyter
%dir %{_datadir}/jupyter/kernels/fortran
%{_datadir}/jupyter/kernels/fortran/kernel.json
%endif

%changelog
* Fri Jan 19 2024 Christoph Junghans <junghans@votca.org> - 0.30.0-9
- Drop jupyter package on F38

* Fri Jan 19 2024 Christoph Junghans <junghans@votca.org> - 0.30.0-8
- Add kokkos dependency

* Fri Jan 19 2024 Benson Muite <benson_muite@emailplus.org> - 0.30.0-7
- Use conditional includes for llvm and zlib

* Fri Jan 19 2024 Benson Muite <benson_muite@emailplus.org> - 0.30.0-6
- Use llvm instead of llvm16 on f38

* Fri Jan 19 2024 Benson Muite <benson_muite@emailplus.org> - 0.30.0-5
- Use zlib for f39 and f38

* Tue Jan 16 2024 Benson Muite <benson_muite@emailplus.org> - 0.30.0-4
- Use zlib-ng
- Ensure all directories are owned

* Mon Jan 15 2024 Christoph Junghans <junghans@votca.org> - 0.30.0-3
- Enable WASM backend

* Wed Jan 10 2024 Christoph Junghans <junghans@votca.org> - 0.30.0-2
- More subpackages

* Thu Jan 04 2024 Christoph Junghans <junghans@votca.org> - 0.30.0-1
- Version bump v0.30.0

* Sat Oct 07 2023 Benson Muite <benson_muite@emailplus.org> - 0.21.5-1
- Initial packaging
