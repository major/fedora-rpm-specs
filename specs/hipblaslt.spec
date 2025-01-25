%global upstreamname hipBLASLt
%global rocm_release 6.3
%global rocm_patch 1
%global rocm_version %{rocm_release}.%{rocm_patch}

%global toolchain rocm
# hipcc does not support some clang flags
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/')

# gfx90a: 10343 pass, 152 fail
%bcond_with test
# Disable rpatch checks for a local build
%if %{with test}
%global __brp_check_rpaths %{nil}
%global build_test ON
%else
%global build_test OFF
%endif

%global tensile_version 4.33.0
# The upstream hipBLASTLt project has a hard fork of the python-tensile package
# The rocBLAS uses.  The two versions are incompatible.  It appears that the
# fork happened around version 4.33.0.  Unfortunately hipBLASLt can no longer be
# build without using this fork.
# https://github.com/ROCm/hipBLASLt/issues/535
# The problem with the fork has been raised here.
# https://github.com/ROCm/hipBLASLt/issues/908

# hipblaslt does not support our default set
# These are the ones it does, gfx942 building still has problems
%global amdgpu_targets "gfx90a:xnack+;gfx90a:xnack-;gfx1100;gfx1101;gfx1102;gfx1200;gfx1201"

# Compression type and level for source/binary package payloads.
#  "w7T0.xzdio"	xz level 7 using %%{getncpus} threads
%define _source_payload	w7T0.xzdio
%define _binary_payload	w7T0.xzdio

Name:           hipblaslt
Version:        %{rocm_version}
Release:        4%{?dist}
Summary:        ROCm general matrix operations beyond BLAS
Url:            https://github.com/ROCmSoftwarePlatform/%{upstreamname}
License:        MIT

Source0:        %{url}/archive/rocm-%{rocm_version}.tar.gz#/%{upstreamname}-%{rocm_version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  hipblas-devel
BuildRequires:  hipcc
BuildRequires:  msgpack-devel
BuildRequires:  rocblas-devel
BuildRequires:  rocminfo
BuildRequires:  rocm-cmake
BuildRequires:  rocm-comgr-devel
BuildRequires:  rocm-compilersupport-macros
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-llvm-devel
BuildRequires:  rocm-runtime-devel
BuildRequires:  rocm-rpm-macros
BuildRequires:  rocm-smi

# For tensilelite
BuildRequires:  python3-devel
BuildRequires:  python3dist(joblib)
BuildRequires:  python3dist(msgpack)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(setuptools)

%if %{with test}
BuildRequires:  gcc-gfortran
BuildRequires:  gtest-devel
BuildRequires:  gmock-devel
BuildRequires:  blas-static
BuildRequires:  hipcc-libomp-devel
%endif

Provides:       bundled(python-tensile) = %{tensile_version}

# Only x86_64 works right now:
ExclusiveArch:  x86_64

%description
hipBLASLt is a library that provides general matrix-matrix
operations. It has a flexible API that extends functionalities
beyond a traditional BLAS library, such as adding flexibility
to matrix data layouts, input types, compute types, and
algorithmic implementations and heuristics.

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

# rocm path
sed -i -e 's@rocm_path=/opt/rocm@rocm_path=/usr@'                              tensilelite/Tensile/Ops/gen_assembly.sh
# No llvm/bin/clang, use clang++-17 or similar
sed -i -e 's@toolchain=${rocm_path}/llvm/bin/clang++@toolchain=%{rocmllvm_bindir}/clang++@'    tensilelite/Tensile/Ops/gen_assembly.sh
sed -i -e 's@clang_path="${rocm_path}/bin/amdclang++"@clang_path="%{rocmllvm_bindir}/clang++"@' library/src/amd_detail/rocblaslt/src/kernels/compile_code_object.sh

# Remove venv
sed -i -e 's@. ${venv}/bin/activate@@'                                         tensilelite/Tensile/Ops/gen_assembly.sh
sed -i -e 's@deactivate@@'                                                     tensilelite/Tensile/Ops/gen_assembly.sh
# Change some paths in Common.py
# change rocm path from /opt/rocm to /usr
# need to be able to find hipcc, rocm-smi, extractkernel, rocm_agent_enumerator
sed -i -e 's@opt/rocm@usr@'                                                    tensilelite/Tensile/Common.py
# look for clang things in 'usr' + '/lib64/llv17/bin'  or similar
# need to be able to find clang++, ld.lld, clang-offload-bundler
sed -i -e 's@llvm/bin@%{rocmllvm_bindir}@'                      tensilelite/Tensile/Common.py
# Use PATH to find where TensileGetPath and other tensile bins are
sed -i -e 's@${Tensile_PREFIX}/bin/TensileGetPath@TensileGetPath@g'            tensilelite/Tensile/cmake/TensileConfig.cmake

# defer to cmdline
sed -i -e 's@set(CMAKE_INSTALL_LIBDIR@#set(CMAKE_INSTALL_LIBDIR@' CMakeLists.txt
# Do not use virtualenv_install
sed -i -e 's@virtualenv_install@#virtualenv_install@'                          CMakeLists.txt
# do not mess with prefix path
sed -i -e 's@APPEND CMAKE_PREFIX_PATH@APPEND NO_CMAKE_PREFIX_PATH@'            CMakeLists.txt

# For debugging
# set threads to 1
# sed -i -e 's@default=-1@default=1@'                                          tensilelite/Tensile/TensileCreateLibrary.py
# sed -i -e 's@return cpu_count@return 1@'                                     tensilelite/Tensile/Parallel.py
# Print things
# sed -i -e 's@if globalParameters["PrintCodeCommands"]:@if True:@'            tensilelite/Tensile/TensileCreateLibrary.py
# sed -i -e 's@#print@print@'                                                  tensilelite/Tensile/Parallel.py

%if %{with test}
# Remove problem libraries, why are we linking gfortran AND flang ?
sed -i -e 's@-lgfortran -lflang -lflangrti@-lgfortran@'                        clients/gtest/CMakeLists.txt
%endif

%build

# Do a manual install instead of cmake's virtualenv
cd tensilelite
TL=$PWD
%{python3} setup.py install --root $TL
cd ..

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

# Only gfx90a seems to be useful and works
# gfx942 has some unknown to llvm17 asm directives
# Use ld.lld to work around a problem with ld
%cmake \
       -DAMDGPU_TARGETS=%{amdgpu_targets} \
       -DBUILD_CLIENTS_TESTS=%{build_test} \
       -DBUILD_FILE_REORG_BACKWARD_COMPATIBILITY=OFF \
       -DBUILD_VERBOSE=ON \
       -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DCMAKE_INSTALL_LIBDIR=%{_lib} \
       -DCMAKE_C_COMPILER=hipcc \
       -DCMAKE_CXX_COMPILER=hipcc \
       -DCMAKE_CXX_FLAGS="-fuse-ld=%{rocmllvm_bindir}/ld.lld" \
       -DHIP_PLATFORM=amd \
       -DROCM_SYMLINK_LIBS=OFF \
       -DBUILD_WITH_TENSILE=ON \
       -DTensile_COMPILER=hipcc \
       -DTensile_LIBRARY_FORMAT=msgpack \
       -DVIRTUALENV_BIN_DIR=%{_bindir} 

%cmake_build

%install
%cmake_install

%files
%dir %{_libdir}/cmake/%{name}/
%dir %{_libdir}/%{name}/
%dir %{_libdir}/%{name}/library/
%license LICENSE.md
%exclude %{_docdir}/%{name}/LICENSE.md
%{_libdir}/lib%{name}.so.*
%{_libdir}/%{name}/library/*

%files devel
%doc README.md
%{_includedir}/%{name}
%{_libdir}/cmake/%{name}/
%{_libdir}/lib%{name}.so

%if %{with test}
%files test
%{_bindir}/%{name}*
%endif

%changelog
* Thu Jan 23 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.1-4
- Add gfx1200,gfx1201
- multithread compress

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jan 15 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.1-2
- build requires gcc-c++

* Mon Dec 23 2024 Tom Rix <Tom.Rix@amd.com> - 6.3.1-1
- Update to 6.3.1

* Wed Dec 11 2024 Tom Rix <Tom.Rix@amd.com> - 6.3.0-1
- Update to 6.3

