%global pypi_name triton

# For testing
%bcond_with test

# For debugging
%bcond_with debug

# Reduce link memory pressure
%global _lto_cflags %nil

%global __cmake_in_source_build 1

# So pre releases can be tried
%bcond_with gitcommit
%if %{with gitcommit}
# release/3.7.x 6/12/26
%global commit0 5d6048aa0a324e090ada215b609ea76620133845

# from cmake/llvm-hash
%global commit1 ac5dc54d509169d387fcfd495d71853d81c46484

%global pypi_version 3.7.0
%else

%global pypi_version 3.7.0

# The sdist does not contain enough to do the build
# Fetch top of release/3.1.x at 12/31/24
%global commit0 cf34004b8a67d290a962da166f5aa2fc66751326
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# Do no use the prebuilt llvm
# This commit should come from trition/cmake/llvm-hash.txt
%global commit1 ac5dc54d509169d387fcfd495d71853d81c46484
%endif

%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global shortcommit1 %(c=%{commit1}; echo ${c:0:7})

# The llvm build has its LLVM_PARALLEL_COMPILE|LINK_JOBS switches
# Triton uses the envionment variable MAX_JOBS for both.
%global _smp_mflags %{nil}

# Build clang with clang is easier
%global toolchain clang

# Compression type and level for source/binary package payloads.
#  "w7T0.xzdio"         xz level 7 using %%{getncpus} threads
%global _source_payload         w7T0.xzdio
%global _binary_payload         w7T0.xzdio

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        A language and compiler for custom Deep Learning operations

License:        MIT AND Apache-2.0 AND BSD-3-Clause AND BSD-2-Clause
# Main license is MIT
# llvm is Apache-2.0, BSD-3-Clause AND BSD-2-Clause

URL:            https://github.com/openai/triton/
Source0:        https://github.com/triton-lang/triton/archive/refs/tags/v%{version}.tar.gz
%if %{without local}
Source1:        https://github.com/llvm/llvm-project/archive/%{commit1}.tar.gz
Source2:        https://github.com/pybind/pybind11/archive/refs/tags/v2.11.1.tar.gz
%endif

%if %{without gitcommit}
# Can not download things
# Can not use git on a tarball
# Patch1:         0001-Prepare-triton-setup-for-fedora.patch
%else
# Patch1:         0001-triton-3.3-prepare-for-fedora.patch
%endif

# GPUs really only work on x86_64
ExclusiveArch:  x86_64

BuildRequires:  ccache
BuildRequires:  chrpath
BuildRequires:  clang
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  python3-devel
BuildRequires:  python3dist(filelock)
BuildRequires:  python3-nanobind-devel
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pybind11)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildRequires:  rocm-compilersupport-macros
BuildRequires:  zlib-devel

# Triton uses a custom snapshot of the in development llvm
# Because of instablity of the llvm api, we must use the one
# triton uses.  llvm is statically built and none of the
# llvm headers or libraries are distributed directly.
# From llvm.spec's license
#   Apache-2.0 WITH LLVM-exception OR NCSA
%global llvm_version 23
Provides:       bundled(llvm-project) = %{llvm_version}
# From pybind11.spec's license
#   BSD-3-Clause
Provides:       bundled(pybind11) = 2.11.1

%global _description %{expand:
Triton is a language and compiler for writing highly efficient custom
Deep-Learning primitives. The aim of Triton is to provide an open-source
environment to write fast code at higher productivity than CUDA, but
also with higher flexibility than other existing DSLs. }

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}

Requires:  rocm-hip-devel
Requires:  rocm-lld
Requires:  rocm-runtime-devel
Requires:  roctracer-devel

%description -n python3-%{pypi_name} %_description

%prep
%autosetup -p1 -n triton-%{version}
%if %{without local}
tar xf %{SOURCE1}
tar xf %{SOURCE2}
%endif

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# Up the max python version
sed -i -e 's@MAX_PYTHON = (3, 14)@MAX_PYTHON = (3, 15)@' setup.py

# No downloading
sed -i -E '/download_and_copy_dependencies\(\)$/d' setup.py

# remove -Werror
sed -i -e 's@-Werror@@' CMakeLists.txt

%build

# Real cores, No hyperthreading
COMPILE_JOBS=`cat /proc/cpuinfo | grep -m 1 'cpu cores' | awk '{ print $4 }'`
if [ ${COMPILE_JOBS}x = x ]; then
    COMPILE_JOBS=1
fi
# Try again..
if [ ${COMPILE_JOBS} = 1 ]; then
    COMPILE_JOBS=`lscpu | grep '^CPU(s)' | awk '{ print $2 }'`
    if [ ${COMPILE_JOBS}x = x ]; then
        COMPILE_JOBS=4
    fi
fi

# Take into account memmory usage per core, do not thrash real memory
BUILD_MEM=2
MEM_KB=0
MEM_KB=`cat /proc/meminfo | grep MemTotal | awk '{ print $2 }'`
MEM_MB=`eval "expr ${MEM_KB} / 1024"`
MEM_GB=`eval "expr ${MEM_MB} / 1024"`
COMPILE_JOBS_MEM=`eval "expr 1 + ${MEM_GB} / ${BUILD_MEM}"`
if [ "$COMPILE_JOBS_MEM" -lt "$COMPILE_JOBS" ]; then
    COMPILE_JOBS=$COMPILE_JOBS_MEM
fi
LINK_MEM=32
LINK_JOBS=`eval "expr 1 + ${MEM_GB} / ${LINK_MEM}"`

cd llvm-project-%{commit1}

%cmake -G Ninja \
       -DBUILD_SHARED_LIBS=OFF \
       -DCMAKE_BUILD_TYPE=RELEASE \
       -DCMAKE_INSTALL_PREFIX=$PWD/install \
       -DLLVM_PARALLEL_COMPILE_JOBS=$COMPILE_JOBS \
       -DLLVM_PARALLEL_LINK_JOBS=$LINK_JOBS \
       -DCMAKE_LINKER=lld \
       -DLLVM_BUILD_UTILS=ON \
       -DLLVM_BUILD_TOOLS=ON \
       -DLLVM_ENABLE_ASSERTIONS=OFF \
       -DMLIR_ENABLE_BINDINGS_PYTHON=ON \
       -DLLVM_ENABLE_PROJECTS="mlir;lld" \
       -DLLVM_INCLUDE_BENCHMARKS=OFF \
       -DLLVM_INSTALL_UTILS=ON \
       -DLLVM_TARGETS_TO_BUILD="host;NVPTX;AMDGPU" \
       -DLLVM_ENABLE_TERMINFO=OFF \
       -DBUILD_SHARED_LIBS=OFF \
       llvm
%cmake_build
%cmake_build -t install

export LLVM_SYSPATH=$PWD/install
cd ..

cd pybind11-2.11.1
%cmake -G Ninja \
       -DBUILD_SHARED_LIBS=OFF \
       -DCMAKE_BUILD_TYPE=Release \
       -DCMAKE_INSTALL_PREFIX=$PWD/install \
       -DPYBIND11_TEST=OFF

%cmake_build
%cmake_build -t install

export PYBIND11_SYSPATH=$PWD/install
cd ..

export PATH=$LLVM_SYSPATH/bin:$PATH

%if %{with debug}
export DEBUG=1
%else
# Needs to be the same as llvm
export RELEASE=1
%endif

export CC=clang
export CXX=clang++
export MAX_JOBS=$COMPILE_JOBS
export TRITON_BUILD_WITH_CLANG_LD=ON
export TRITON_BUILD_PROTON=OFF
export TRITON_CODEGEN_AMD=ON
export TRITON_CODEGEN_NVIDIA=ON
export TRITON_OFFLINE_BUILD=ON

%pyproject_wheel

%install
%pyproject_install

# empty files
rm %{buildroot}%{python3_sitearch}/triton/compiler/make_launcher.py

# Remove all the amd headers
rm -rf %{buildroot}%{python3_sitearch}/triton/backends/amd/include/*

# ERROR   0002: file '/usr/lib64/python3.15/site-packages/triton/plugins/libMLIRDialectPlugin.so.23.0git'
#  contains an invalid runpath
chrpath -d %{buildroot}%{python3_sitearch}/triton/plugins/libMLIRDialectPlugin.so.%{llvm_version}.0git
chrpath -d %{buildroot}%{python3_sitearch}/triton/plugins/libMLIRDialectPlugin.so
chrpath -d %{buildroot}%{python3_sitearch}/triton/plugins/libTritonPluginsTestLib.so

%check
%if %{with test}
# Unit tests download so are not suitable for mock
cd python
%pytest
%endif

%files -n python3-%{pypi_name}
%{python3_sitearch}/%{pypi_name}*

%changelog
* Fri Jun 19 2026 Tom Rix <Tom.Rix@amd.com> 3.7.0-1
- Update to 3.7

* Wed Jun 03 2026 Python Maint <python-maint@redhat.com> - 3.1.0-11
- Rebuilt for Python 3.15

* Wed Mar 11 2026 Tom Rix <Tom.Rix@amd.com> - 3.1.0-10
- Do no build benchmarks

* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Sep 19 2025 Python Maint <python-maint@redhat.com> - 3.1.0-8
- Rebuilt for Python 3.14.0rc3 bytecode

* Fri Aug 15 2025 Python Maint <python-maint@redhat.com> - 3.1.0-7
- Rebuilt for Python 3.14.0rc2 bytecode

* Fri Jul 25 2025 Tom Rix <Tom.Rix@amd.com> - 3.1.0-6
- Use pyproject macros

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue Jun 03 2025 Python Maint <python-maint@redhat.com> - 3.1.0-4
- Rebuilt for Python 3.14

* Mon Jan 20 2025 Tom Rix <Tom.Rix@amd.com> - 3.1.0-3
- gcc 15 include cstdint

* Mon Jan 20 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jan 4 2025 Tom Rix <trix@redhat.com> 3.1.0-1
- Inital release
