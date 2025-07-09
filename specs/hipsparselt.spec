%global upstreamname hipSPARSELt
%global rocm_release 6.4
%global rocm_patch 1
%global rocm_version %{rocm_release}.%{rocm_patch}

# The tensilelite that hipSPARELt use comes from hipBLASLt
# But not the matching release tag, a custom commit that is
# stored in the toplevel tensilelite_tag.txt file
#
# https://github.com/ROCm/hipSPARSELt/issues/248
%global hipblaslt_commit 510dcac724743ff35ec8c60270bc08505eddcfd7
%global hipblaslt_scommit %(c=%{hipblaslt_commit}; echo ${c:0:7})

%global toolchain rocm
# hipcc does not support some clang flags
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/')

%bcond_with test
%if %{with test}
%global __brp_check_rpaths %{nil}
%global build_test ON
%else
%global build_test OFF
%endif
# Fortran is only used in testing
%global build_fflags %{nil}

%global tensile_version 4.33.0
%global tensile_verbose 1

%global amdgpu_targets "gfx1100"

# Compression type and level for source/binary package payloads.
#  "w7T0.xzdio"	xz level 7 using %%{getncpus} threads
%global _source_payload w7T0.xzdio
%global _binary_payload w7T0.xzdio

Name:           hipsparselt
Version:        %{rocm_version}
Release:        1%{?dist}
Summary:        A SPARSE marshaling library
Url:            https://github.com/ROCm/%{upstreamname}
License:        MIT

Source0:        %{url}/archive/rocm-%{rocm_version}.tar.gz#/%{upstreamname}-%{rocm_version}.tar.gz
Source1:        https://github.com/ROCm/hipBLASLt/archive/%{hipblaslt_commit}/hipBLASLt-%{hipblaslt_scommit}.tar.gz

BuildRequires:  ninja-build
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  hipcc
BuildRequires:  hipsparse-devel
BuildRequires:  libzstd-devel
BuildRequires:  rocminfo
BuildRequires:  rocm-cmake
BuildRequires:  rocm-comgr-devel
BuildRequires:  rocm-compilersupport-macros
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-llvm-devel
BuildRequires:  rocm-runtime-devel
BuildRequires:  rocm-rpm-macros
BuildRequires:  rocm-smi
BuildRequires:  rocsparse-devel
BuildRequires:  roctracer-devel
BuildRequires:  zlib-devel

# For tensilelite
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(joblib)
BuildRequires:  python3dist(msgpack)
BuildRequires:  msgpack-devel

%if %{with test}
BuildRequires:  chrpath
BuildRequires:  gcc-gfortran
BuildRequires:  gtest-devel
BuildRequires:  gmock-devel
BuildRequires:  blas-static
BuildRequires:  lapack-static
BuildRequires:  rocm-omp-devel
%endif

Provides:       bundled(python-tensile) = %{tensile_version}

# Only x86_64 works right now:
ExclusiveArch:  x86_64

%description
hipSPARSELt is a SPARSE marshaling library, with multiple
supported backends. It sits between the application and a
'worker' SPARSE library, marshaling inputs into the backend
library and marshaling results back to the application.
hipSPARSELt exports an interface that does not require the
client to change, regardless of the chosen backend. Currently,
hipSPARSELt supports the rocSPARSELt backend.

%package devel
Summary:        Libraries and headers for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}

%if %{with test}
%package test
Summary:        Tests for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description test
%{summary}
%endif

%prep
%autosetup -p1 -n %{upstreamname}-rocm-%{version}

tar xf %{SOURCE1}
mv hipBLASLt-%{hipblaslt_commit} hipBLASLt
cd hipBLASLt

# Remove venv
sed -i -e 's@. ${venv}/bin/activate@@'                                         tensilelite/Tensile/Ops/gen_assembly.sh
sed -i -e 's@deactivate@@'                                                     tensilelite/Tensile/Ops/gen_assembly.sh
# Change some paths in Common.py
# change rocm path from /opt/rocm to /usr
# need to be able to find hipcc, rocm-smi, extractkernel, rocm_agent_enumerator
sed -i -e 's@opt/rocm@usr@'                                                    tensilelite/Tensile/Common.py
# Use PATH to find where TensileGetPath and other tensile bins are
sed -i -e 's@${Tensile_PREFIX}/bin/TensileGetPath@TensileGetPath@g'            tensilelite/Tensile/cmake/TensileConfig.cmake

# defer to cmdline
sed -i -e 's@set(CMAKE_INSTALL_LIBDIR@#set(CMAKE_INSTALL_LIBDIR@' CMakeLists.txt
# Do not use virtualenv_install
sed -i -e 's@virtualenv_install@#virtualenv_install@'                          CMakeLists.txt
# do not mess with prefix path
sed -i -e 's@APPEND CMAKE_PREFIX_PATH@APPEND NO_CMAKE_PREFIX_PATH@'            CMakeLists.txt

sed -i 's@find_package(LLVM REQUIRED CONFIG)@find_package(LLVM REQUIRED CONFIG PATHS "%{rocmllvm_cmakedir}")@' tensilelite/Tensile/Source/lib/CMakeLists.txt

# Changes different from hipBLASLt
sed -i -e 's@/opt/rocm/bin@/usr/bin@' tensilelite/Tensile/Utilities/Toolchain.py
sed -i -e 's@/opt/rocm/lib/llvm/bin@/usr/lib64/rocm/llvm/bin@' tensilelite/Tensile/Utilities/Toolchain.py
sed -i -e 's@amdclang@clang@g' tensilelite/Tensile/Utilities/Toolchain.py

cd ..

# Prevent the virtualenv install from cmake
sed -i -e 's@virtualenv_install@#virtualenv_install@' CMakeLists.txt

# Unforce the setting of libdir
# https://github.com/ROCm/hipSPARSELt/issues/256
sed -i -e 's@set(CMAKE_INSTALL_LIBDIR@#set(CMAKE_INSTALL_LIBDIR@' CMakeLists.txt
    
%build

# Do a manual install instead of cmake's virtualenv
cd hipBLASLt/tensilelite
TL=$PWD

python3 setup.py install --root $TL
cd ../..

# Should not have to do this
CLANG_PATH=`hipconfig --hipclangpath`
ROCM_CLANG=${CLANG_PATH}/clang
RESOURCE_DIR=`${ROCM_CLANG} -print-resource-dir`
export DEVICE_LIB_PATH=${RESOURCE_DIR}/amdgcn/bitcode
export TENSILE_ROCM_ASSEMBLER_PATH=${CLANG_PATH}/clang++
export TENSILE_ROCM_OFFLOAD_BUNDLER_PATH=${CLANG_PATH}/clang-offload-bundler

# Look for the just built tensilelite
export PATH=${TL}/%{_bindir}:$PATH
export PYTHONPATH=${TL}%{python3_sitelib}:$PYTHONPATH
export Tensile_DIR=${TL}%{python3_sitelib}/Tensile
# Uncomment and see if the path is sane
# TensileGetPath

%cmake -G Ninja \
       -DTensile_TEST_LOCAL_PATH=${TL} \
       -DAMDGPU_TARGETS=%{amdgpu_targets} \
       -DBUILD_CLIENTS_TESTS=%{build_test} \
       -DBUILD_FILE_REORG_BACKWARD_COMPATIBILITY=OFF \
       -DBUILD_VERBOSE=ON \
       -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DCMAKE_INSTALL_LIBDIR=%{_lib} \
       -DCMAKE_C_COMPILER=%{rocmllvm_bindir}/clang \
       -DCMAKE_CXX_COMPILER=%{rocmllvm_bindir}/clang++ \
       -DCMAKE_Fortran_COMPILER=gfortran \
       -DCMAKE_VERBOSE_MAKEFILE=ON \
       -DHIP_PLATFORM=amd \
       -DROCM_SYMLINK_LIBS=OFF \
       -DBUILD_WITH_TENSILE=ON \
       -DTensile_COMPILER=clang++ \
       -DTensile_LIBRARY_FORMAT=msgpack \
       -DTensile_VERBOSE=%{tensile_verbose} \
       -DVIRTUALENV_BIN_DIR=%{_bindir} \
       %{nil}

%cmake_build

%install
%cmake_install

if [ -f %{buildroot}%{_prefix}/share/doc/hipsparselt/LICENSE.md ]; then
    rm %{buildroot}%{_prefix}/share/doc/hipsparselt/LICENSE.md
fi

# hipsparselt.x86_64: W: unstripped-binary-or-object /usr/lib64/hipsparselt/library/Kernels.so-000-gfx1100.hsaco
%{rocmllvm_bindir}/llvm-strip %{buildroot}%{_libdir}/hipsparselt/library/Kernels*.hsaco

# hipsparselt.x86_64: E: ldd-failed /usr/lib64/hipsparselt/library/Kernels.so-000-gfx1100.hsaco /usr/bin/bash: warning: setlocale: LC_ALL: cannot change locale (en_US.UTF-8): No such file or directory
# ldd: warning: you do not have execution permission for `/usr/lib64/hipsparselt/library/Kernels.so-000-gfx1100.hsaco'
# 	not a dynamic executable
# Do something about the prems
chmod a+x %{buildroot}%{_libdir}/hipsparselt/library/Kernels*.hsaco
# But not much to do about the rest, this is not a normal *.so
# file /usr/lib64/hipsparselt/library/Kernels.so-000-gfx1100.hsaco 
# /usr/lib64/hipsparselt/library/Kernels.so-000-gfx1100.hsaco: ELF 64-bit LSB shared object, AMD GPU architecture version 1, dynamically linked, BuildID[sha1]=99e2194d9647da308804928d27ea1f336bfd76cc, stripped

%if %{with test}
# hipsparselt-test's rpath is pretty messed up
# chrpath -l /usr/bin/hipsparselt-test 
# /usr/bin/hipsparselt-test: RUNPATH=$ORIGIN/../lib:$ORIGIN/../lib/hipsparselt-clients/lib:/usr/llvm/lib
# So adjust it here
chrpath -r %{rocmllvm_libdir} %{buildroot}%{_bindir}/hipsparselt-test
%endif

%files
%dir %{_libdir}/cmake/hipsparselt/
%dir %{_libdir}/hipsparselt/
%dir %{_libdir}/hipsparselt/library/
%license LICENSE.md
%{_libdir}/libhipsparselt.so.*
%{_libdir}/hipsparselt/library/*

%files devel
%doc README.md
%{_includedir}/hipsparselt
%{_libdir}/cmake/hipsparselt/
%{_libdir}/libhipsparselt.so

%if %{with test}
%files test
%{_bindir}/hipsparselt*
%endif

%changelog
* Sat Jun 28 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.1-1
- Initial package
