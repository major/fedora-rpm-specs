Name:           onednn
Version:        3.13.2
Release:        %autorelease
Summary:     The oneAPI Deep Neural Network Library

License:         Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND BSL-1.0 AND MIT
URL:               https://github.com/uxlfoundation/oneDNN
Source0:        %{url}/archive/v%{version}/onednn-%{version}.tar.gz
Source1:        onednn-test.in

# This package only work in 64bit arches for now
ExclusiveArch:  x86_64 aarch64 ppc64le s390x

BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  chrpath

# Optionals not yet enabled
BuildRequires:  pkgconfig(OpenCL)
#BuildRequires:  pkgconfig(tbb)

# Virtual provides mkldnn
Provides: mkldnn = %{version}-%{release}
Provides: mkl-dnn = %{version}-%{release}
Obsoletes: mkl-dnn < 1.3
# Provides oneDNN
Provides: oneDNN = %{version}-%{release}


%description
oneAPI Deep Neural Network Library (oneDNN) is an open-source cross-platform
performance library of basic building blocks for deep learning applications.
oneDNN is part of oneAPI. The library is optimized for Intel(R) Architecture
Processors, Intel Graphics, and Arm* 64-bit Architecture (AArch64)-based
processors. oneDNN has experimental support for the following architectures:
NVIDIA* GPU, OpenPOWER* Power ISA (PPC64), IBMz* (s390x), and RISC-V.

oneDNN is intended for deep learning applications and framework developers
interested in improving application performance on Intel CPUs and GPUs.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        benchdnn
Summary:        benchdnn benchmark and test tool for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    benchdnn
benchdnn is a standalone correctness and performance benchmark for oneDNN
primitives. This package allows testing oneDNN functionality on target
hardware without requiring the full build environment.

%package        tests
Summary:        unit tests for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    tests
googletest-based unit tests for oneDNN. useful for validating oneDNN
functionality on target hardware.


%prep
%autosetup -p1 -n oneDNN-%{version}


%build
%cmake \
  -DDNNL_ARCH_OPT_FLAGS="" \
  -DDNNL_BUILD_EXAMPLES=OFF \
  -DDNNL_BUILD_TESTS=ON \
  -DCMAKE_C_STD=11 \
  -DCMAKE_CPP_STD=17 \
  -DONEDNN_GPU_RUNTIME=OCL

%cmake_build


%install
%cmake_install

# Remove docs
rm -rf %{buildroot}%{_docdir}/dnnl

# install benchdnn
install -d %{buildroot}%{_libexecdir}/onednn
install -pm0755 %{_vpath_builddir}/tests/benchdnn/benchdnn %{buildroot}%{_libexecdir}/onednn/
chrpath -d %{buildroot}%{_libexecdir}/onednn/benchdnn
cp -a %{_vpath_builddir}/tests/benchdnn/inputs %{buildroot}%{_libexecdir}/onednn/

# wrapper script for benchdnn
install -d %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/benchdnn << 'EOF'
#!/bin/sh
exec %{_libexecdir}/onednn/benchdnn "$@"
EOF
chmod 0755 %{buildroot}%{_bindir}/benchdnn

# install gtests
install -d %{buildroot}%{_libexecdir}/onednn/gtests
find %{_vpath_builddir}/tests/gtests -maxdepth 1 -type f -executable -name 'test_*' \
    -exec install -pm0755 {} %{buildroot}%{_libexecdir}/onednn/gtests/ \;
install -pm0755 %{_vpath_builddir}/tests/api-c %{buildroot}%{_libexecdir}/onednn/gtests/
[ -f %{_vpath_builddir}/tests/test_c_symbols-c ] && \
  install -pm0755 %{_vpath_builddir}/tests/test_c_symbols-c %{buildroot}%{_libexecdir}/onednn/gtests/ || true

# strip build-tree RUNPATH from test binaries
find %{buildroot}%{_libexecdir}/onednn/gtests -type f -executable \
    -exec chrpath -d {} \; 2>/dev/null || true

# test runner script
sed -e 's|@LIBEXECDIR@|%{_libexecdir}|g' \
    %{SOURCE1} > %{buildroot}%{_bindir}/onednn-test
chmod 0755 %{buildroot}%{_bindir}/onednn-test


# Some ocl/gpu tests will fails if lacking an appropriate implementation
%{?_with_tests:
%check
%ctest
}


%files
%license LICENSE THIRD-PARTY-PROGRAMS
%doc README.md CONTRIBUTING.md CODE_OF_CONDUCT.md
%{_libdir}/libdnnl.so.3
%{_libdir}/libdnnl.so.3.*


%files devel
%dir %{_includedir}/oneapi
%{_includedir}/oneapi/dnnl
%{_includedir}/dnnl*.h*
%{_libdir}/libdnnl.so
%dir %{_libdir}/cmake/dnnl
%{_libdir}/cmake/dnnl/*.cmake


%files benchdnn
%{_bindir}/benchdnn
%{_libexecdir}/onednn/benchdnn
%{_libexecdir}/onednn/inputs/


%files tests
%{_bindir}/onednn-test
%{_libexecdir}/onednn/gtests/


%changelog
%autochangelog
