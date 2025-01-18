%global truename CombBLAS

%if 0%{?fedora} >= 40
%ifarch %{ix86}
%bcond_with openmpi
%else
%bcond_without openmpi
%endif
%else
%bcond_without openmpi
%endif
%bcond_without mpich

# Tests are performed really slowly with current version of OpenMPI (4.1.5)
%bcond_with check

# CTest flags for debugging only
%bcond_with debug
%if %{with debug}
%global _lto_cflags %{nil}
%global debug_flags -VV --debug -j1
%else
%global debug_flags %{nil}
%endif

Name:          combblas
Version:       2.0.0
Release:       10%{?dist}
Summary:       The Combinatorial BLAS Library

# Main license for CombBLAS is BSD.
# graph500-1.2/ under BSD license.
# graph500-1.2/generator/ under Boost license.
# include/Tommy/ under BSD license.
# include/CombBLAS/ under MIT or Expat license.
# psort-1.0/include/ under a mixed GPLv2+/MIT/BSD licenses.
# usort/ under MIT or Expat license.
# Automatically converted from old format: BSD and MIT and Boost and GPLv2+ - review is highly recommended.
License:       LicenseRef-Callaway-BSD AND LicenseRef-Callaway-MIT AND BSL-1.0 AND GPL-2.0-or-later
URL:           https://people.eecs.berkeley.edu/~aydin/%{truename}/html/index.html
Source0:       https://github.com/PASSIONLab/%{truename}/archive/refs/tags/v%{version}/%{truename}-%{version}.tar.gz
Source1:       http://eecs.berkeley.edu/~aydin/%{truename}_FILES/testdata_%{name}1.6.1.tgz

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: chrpath

# Set MPI library paths
Patch0: %{name}-libpaths.patch

# Use a versioned soname for all libraries
Patch1: %{name}-sublibs_soname.patch

# https://github.com/PASSIONLab/CombBLAS/commit/ecf96214a0c666662954cf24b84df97f61d52dc9
Patch2: %{name}-%{version}-removing_MPI_COMM_WORLD.patch

%global desc \
The Combinatorial BLAS (CombBLAS) is an extensible distributed-memory parallel \
graph library offering a small but powerful set of linear algebra primitives \
specifically targeting graph analytics.

%description
%desc

%if %{with openmpi}
%package openmpi
Summary:       The Combinatorial BLAS Library
Requires:      openmpi%{?_isa}
Provides:      Graph500-openmpi%{?_isa} = 1.2
Provides:      %{truename}-openmpi%{?_isa} = %version-%release
Provides:      %{truename}-openmpi = %version-%release

%description openmpi
%desc

%package openmpi-devel
Summary: Development files for %{name}-openmpi
BuildRequires: openmpi-devel
Requires: openmpi-devel%{?_isa}
Requires: %{name}-openmpi%{?_isa} = %version-%release

%description openmpi-devel
Development files for %{name}-openmpi
%endif

%if %{with mpich}
%package mpich
Summary:       The Combinatorial BLAS Library
BuildRequires: mpich-devel
BuildRequires: make
Requires:      mpich%{?_isa}
Provides:      Graph500-mpich%{?_isa} = 1.2
Provides:      %{truename}-mpich%{?_isa} = %version-%release
Provides:      %{truename}-mpich = %version-%release

%description mpich
%desc

%package mpich-devel
Summary: Development files for %{name}-mpich
Requires: mpich-devel%{?_isa}
Requires: %{name}-mpich%{?_isa} = %version-%release

%description mpich-devel
Development files for %{name}-mpich
%endif

%prep
%autosetup -a 1 -n %{truename}-%{version} -p 1

cp --no-preserve=mode,ownership usort/LICENSE usort/usort-LICENSE
cp --no-preserve=mode,ownership graph500-1.2/COPYING graph500-1.2/graph500-1.2-COPYING
cp --no-preserve=mode,ownership graph500-1.2/generator/LICENSE_1_0.txt graph500-1.2/generator/graph500-1.2-generator-LICENSE_1_0.txt

# Fix permissions
find . -type f -name "*.h" -exec chmod 0644 '{}' \;
find . -type f -name "*.*pp" -exec chmod 0644 '{}' \;
find . -type f -name "*.tcc" -exec chmod 0644 '{}' \;

%build

%if %{with openmpi}
%{_openmpi_load}
mkdir -p build/openmpi
export LDFLAGS="%{__global_ldflags} -lm -lrt"
export CC=$MPI_BIN/mpicc
export CXX=$MPI_BIN/mpic++
%cmake -B build/openmpi -S ./ -DCMAKE_INSTALL_PREFIX=%{_prefix} \
 -DMPIEXEC_NUMPROC_FLAG=-n -DMPIEXEC_MAX_NUMPROCS:STRING="`/usr/bin/getconf _NPROCESSORS_ONLN`" \
 -DMPI_C_HEADER_DIR:PATH=$MPI_INCLUDE -DMPI_C_ADDITIONAL_INCLUDE_DIRS:STRING=$MPI_INCLUDE \
 -DMPI_CXX_HEADER_DIR:PATH=$MPI_INCLUDE -DMPI_CXX_ADDITIONAL_INCLUDE_DIRS:STRING=$MPI_INCLUDE \
 -DMPI_LIB:PATH=..$MPI_LIB -DMPI_INCLUDE:PATH=..$MPI_INCLUDE \
%if %{with debug}
 -DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo \
 -DCMAKE_C_FLAGS_RELWITHDEBINFO:STRING="-O0 -g -DDEBUG" -DCMAKE_CXX_FLAGS_RELWITHDEBINFO:STRING="-O0 -g -DDEBUG" \
 -DCMAKE_C_FLAGS_DEBUG:STRING="-O0 -g -DDEBUG" -DCMAKE_CXX_FLAGS_DEBUG:STRING="-O0 -g -DDEBUG" \
 -DCMAKE_C_FLAGS_RELEASE:STRING=" " -DCMAKE_CXX_FLAGS_RELEASE:STRING=" "
%else
 -DCMAKE_BUILD_TYPE:STRING=Release
%endif

%make_build -C build/openmpi
%{_openmpi_unload}
%endif

###

%if %{with mpich}
%{_mpich_load}
mkdir -p build/mpich
export LDFLAGS="%{__global_ldflags} -lm -lrt"
export CC=$MPI_BIN/mpicc
export CXX=$MPI_BIN/mpic++
%cmake -B build/mpich -S ./ -DCMAKE_INSTALL_PREFIX=%{_prefix} \
 -DMPIEXEC_NUMPROC_FLAG=-n -DMPIEXEC_MAX_NUMPROCS:STRING="`/usr/bin/getconf _NPROCESSORS_ONLN`" \
 -DMPI_C_HEADER_DIR:PATH=$MPI_INCLUDE -DMPI_C_ADDITIONAL_INCLUDE_DIRS:STRING=$MPI_INCLUDE \
 -DMPI_CXX_HEADER_DIR:PATH=$MPI_INCLUDE -DMPI_CXX_ADDITIONAL_INCLUDE_DIRS:STRING=$MPI_INCLUDE \
 -DMPI_LIB:PATH=..$MPI_LIB -DMPI_INCLUDE:PATH=..$MPI_INCLUDE \
%if %{with debug}
 -DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo \
 -DCMAKE_C_FLAGS_RELWITHDEBINFO:STRING="-O0 -g -DDEBUG" -DCMAKE_CXX_FLAGS_RELWITHDEBINFO:STRING="-O0 -g -DDEBUG" \
 -DCMAKE_C_FLAGS_RELEASE:STRING=" " -DCMAKE_CXX_FLAGS_RELEASE:STRING=" "
%else
 -DCMAKE_BUILD_TYPE:STRING=Release
%endif

%make_build -C build/mpich
%{_mpich_unload}
%endif

%install

%if %{with openmpi}
%{_openmpi_load}
%make_install -C build/openmpi

mkdir -p %{buildroot}$MPI_INCLUDE/%{truename}/3DSpGEMM %{buildroot}$MPI_INCLUDE/%{truename}/Applications %{buildroot}$MPI_INCLUDE/%{truename}/BipartiteMatchings
install -pm 644 3DSpGEMM/*.h %{buildroot}$MPI_INCLUDE/%{truename}/3DSpGEMM/
install -pm 644 Applications/*.h %{buildroot}$MPI_INCLUDE/%{truename}/Applications/

chrpath -r $MPI_LIB %{buildroot}$MPI_LIB/libCombBLAS.so.*
%{_openmpi_unload}
%endif

%if %{with mpich}
%{_mpich_load}
%make_install -C build/mpich

mkdir -p %{buildroot}$MPI_INCLUDE/%{truename}/3DSpGEMM %{buildroot}$MPI_INCLUDE/%{truename}/Applications %{buildroot}$MPI_INCLUDE/%{truename}/BipartiteMatchings
install -pm 644 3DSpGEMM/*.h %{buildroot}$MPI_INCLUDE/%{truename}/3DSpGEMM/
install -pm 644 Applications/*.h %{buildroot}$MPI_INCLUDE/%{truename}/Applications/

chrpath -r $MPI_LIB %{buildroot}$MPI_LIB/libCombBLAS.so.*
%{_mpich_unload}
%endif

# Remove DS_Store directories and hidden files
find %{buildroot} -type f -name "*.DS_Store" -exec rm -rf '{}' \;
find %{buildroot} -type f -name "._CombBLAS.h" -exec rm -f '{}' \;

%if %{with check}
%check
# Both failed tests have been reported to upstream:
# https://bitbucket.org/berkeleylab/combinatorial-blas-2.0/issues/3/indexing_test-failed
# https://bitbucket.org/berkeleylab/combinatorial-blas-2.0/issues/4/spasgn_test-failed
%if %{with openmpi}
%{_openmpi_load}
cp -a TESTDATA build/openmpi/
export LD_LIBRARY_PATH=%{buildroot}$MPI_LIB:$MPI_LIB
%ctest -- %{debug_flags} --test-dir build/openmpi -E 'Indexing_Test|SpAsgn_Test|FBFS_Test|FMIS_Test|BPMM_Test'
%{_openmpi_unload}
%endif

%if %{with mpich}
%{_mpich_load}
cp -a TESTDATA build/mpich/
export LD_LIBRARY_PATH=%{buildroot}$MPI_LIB:$MPI_LIB
%ctest -- %{debug_flags} --test-dir build/mpich -E 'Indexing_Test|SpAsgn_Test|FBFS_Test|FMIS_Test|BPMM_Test'
%{_mpich_unload}
%endif
%endif

%if %{with openmpi}
%files openmpi
%doc README_DEVELOPERS graph500-1.2/Graph500.html graph500-1.2/Graph500.org
%license LICENSE usort/usort-LICENSE graph500-1.2/graph500-1.2-COPYING graph500-1.2/generator/graph500-1.2-generator-LICENSE_1_0.txt
%{_libdir}/openmpi/lib/libCombBLAS.so.2.0.0
%{_libdir}/openmpi/lib/libGraphGenlib.so.1.2
%{_libdir}/openmpi/lib/libUsortlib.so.2.0.0

%files openmpi-devel
%{_libdir}/openmpi/lib/libCombBLAS.so
%{_libdir}/openmpi/lib/libGraphGenlib.so
%{_libdir}/openmpi/lib/libUsortlib.so
%{_libdir}/openmpi/lib/cmake/%{truename}/
%{_includedir}/openmpi-%{_arch}/psort/
%{_includedir}/openmpi-%{_arch}/usort/
%{_includedir}/openmpi-%{_arch}/Tommy/
%{_includedir}/openmpi-%{_arch}/graph500/
%{_includedir}/openmpi-%{_arch}/%{truename}/
%endif

%if %{with mpich}
%files mpich
%doc README_DEVELOPERS graph500-1.2/Graph500.html graph500-1.2/Graph500.org
%license LICENSE usort/usort-LICENSE graph500-1.2/graph500-1.2-COPYING graph500-1.2/generator/graph500-1.2-generator-LICENSE_1_0.txt
%{_libdir}/mpich/lib/libCombBLAS.so.2.0.0
%{_libdir}/mpich/lib/libGraphGenlib.so.1.2
%{_libdir}/mpich/lib/libUsortlib.so.2.0.0

%files mpich-devel
%{_libdir}/mpich/lib/libCombBLAS.so
%{_libdir}/mpich/lib/libGraphGenlib.so
%{_libdir}/mpich/lib/libUsortlib.so
%{_libdir}/mpich/lib/cmake/%{truename}/
%{_includedir}/mpich-%{_arch}/psort/
%{_includedir}/mpich-%{_arch}/usort/
%{_includedir}/mpich-%{_arch}/Tommy/
%{_includedir}/mpich-%{_arch}/graph500/
%{_includedir}/mpich-%{_arch}/%{truename}/
%endif

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 2.0.0-9
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Oct 29 2023 Orion Poplawski <orion@nwra.com> - 2.0.0-5
- Rebuild for openmpi 5.0.0, drops support for i686

* Mon Aug 14 2023 Antonio Trande <sagitter@fedoraproject.org> - 2.0.0-4
- Disable LTO flags in debug builds
- Disable tests

* Thu Aug 03 2023 Antonio Trande <sagitter@fedoraproject.org> - 2.0.0-3
- Debug builds

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Feb 04 2023 Antonio Trande <sagitter@fedoraproject.org> - 2.0.0-1
- Release 2.0.0

* Sat Feb 04 2023 Antonio Trande <sagitter@fedoraproject.org> - 1.6.2-0.18.beta2
- Drop OpenMPI support in Fedora 38+ i686 only

* Sat Feb 04 2023 Antonio Trande <sagitter@fedoraproject.org> - 1.6.2-0.17.beta2
- Drop OpenMPI support on i686

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-0.16.beta2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-0.15.beta2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-0.14.beta2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-0.13.beta2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-0.12.beta2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Nov 21 2020 Antonio Trande <sagitter@fedoraproject.org> - 1.6.2-0.11.beta2
- Fix CMake command options

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-0.10.beta2
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-0.9.beta2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Antonio Trande <sagitter@fedoraproject.org> - 1.6.2-0.8.beta2
- Use devtools-7 on EPEL 7

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-0.7.beta2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 24 2019 Antonio Trande <sagitter@fedoraproject.org> - 1.6.2-0.6.beta2
- Use -j1 with ctest

* Thu Oct 24 2019 Antonio Trande <sagitter@fedoraproject.org> - 1.6.2-0.5.beta2
- Fix debug macro

* Thu Oct 24 2019 Antonio Trande <sagitter@fedoraproject.org> - 1.6.2-0.4.beta2
- Add debug macro

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-0.3.beta2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Mar 03 2019 Antonio Trande <sagitter@fedoraproject.org> - 1.6.2-0.2.beta2
- Fix Requires package on el7

* Fri Feb 22 2019 Antonio Trande <sagitter@fedoraproject.org> - 1.6.2-0.1.beta2
- Initial version
