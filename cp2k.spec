%global git 0
%global snapshot 20210528
%global commit f848ba0b7a55a5943658d43e9dc204f6f1beee25
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global dbcsr_commit 46cd0928465ee6bf21d82e5aac0a1970dcb54501
%global dbcsr_shortcommit %(c=%{dbcsr_commit}; echo ${c:0:7})
%global dbcsr_version 2.2.0

# TODO OpenCL support: -D__ACC -D__DBCSR_ACC -D__OPENCL

%global __provides_exclude_from ^%{_libdir}/(cp2k/lib|(mpich|openmpi)/lib/cp2k).*\\.so$
%global __requires_exclude ^lib(cp2k|clsmm|dbcsr|micsmm).*\\.so.*$

%bcond_with check

Name: cp2k
Version: 9.1
Release: 4%{?dist}
Summary: Ab Initio Molecular Dynamics
License: GPLv2+
URL: http://cp2k.org/
%if %{git}
Source0: https://github.com/cp2k/cp2k/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Source1: https://github.com/cp2k/dbcsr/archive/%{dbcsr_commit}/dbcsr-%{dbcsr_shortcommit}.tar.gz
%else
Source0: https://github.com/cp2k/cp2k/releases/download/v%{version}.0/cp2k-%{version}.tar.bz2
%endif
Source4: cp2k-snapshot.sh
# Fedora patches
# patch to:
# use rpm optflags
# link with flexiblas instead of vanilla blas/lapack
# build with libint and libxc
# build shared libraries
Patch10: %{name}-rpm.patch
BuildRequires: flexiblas-devel
# for regtests
BuildRequires: bc
BuildRequires: fftw-devel
BuildRequires: gcc-c++
BuildRequires: gcc-gfortran
BuildRequires: glibc-langpack-en
BuildRequires: libint2-devel
BuildRequires: libxc-devel >= 5.1.0
%ifarch x86_64
# See https://bugzilla.redhat.com/show_bug.cgi?id=1515404
BuildRequires: libxsmm-devel >= 1.8.1-3
%endif
BuildRequires: python3-fypp
BuildRequires: spglib-devel
BuildRequires: /usr/bin/hostname
BuildRequires: /usr/bin/pathfix.py
Provides: bundled(dbcsr) = %{dbcsr_version}

# Libint can break the API between releases
Requires: libint2(api)%{?_isa} = %{_libint2_apiversion}

Requires: %{name}-common = %{version}-%{release}

%global cp2k_desc_base \
CP2K is a freely available (GPL) program, written in Fortran 95, to\
perform atomistic and molecular simulations of solid state, liquid,\
molecular and biological systems. It provides a general framework for\
different methods such as e.g. density functional theory (DFT) using a\
mixed Gaussian and plane waves approach (GPW), and classical pair and\
many-body potentials.\
\
CP2K does not implement Car-Parinello Molecular Dynamics (CPMD).

%description
%{cp2k_desc_base}

This package contains the non-MPI single process and multi-threaded versions.

%package openmpi
Summary: Molecular simulations software - openmpi version
BuildRequires:  openmpi-devel
BuildRequires:  blacs-openmpi-devel
BuildRequires:  elpa-openmpi-devel >= 2018.05.001
BuildRequires:  scalapack-openmpi-devel
Provides: bundled(dbcsr) = %{dbcsr_version}
Requires: %{name}-common = %{version}-%{release}
# Libint may have API breakage
Requires: libint2(api)%{?_isa} = %{_libint2_apiversion}

%description openmpi
%{cp2k_desc_base}

This package contains the parallel single- and multi-threaded versions
using OpenMPI.

%package mpich
Summary: Molecular simulations software - mpich version
BuildRequires:  mpich-devel
BuildRequires:  blacs-mpich-devel
BuildRequires:  elpa-mpich-devel >= 2018.05.001
BuildRequires:  scalapack-mpich-devel
BuildRequires: make
Provides: bundled(dbcsr) = %{dbcsr_version}
Requires: %{name}-common = %{version}-%{release}
# Libint may have API breakage
Requires: libint2(api)%{?_isa} = %{_libint2_apiversion}

%description mpich
%{cp2k_desc_base}

This package contains the parallel single- and multi-threaded versions
using mpich.

%package common
Summary: Molecular simulations software - common files

%description common
%{cp2k_desc_base}

This package contains the documentation and the manual.

%prep
%if %{git}
%setup -q -n %{name}-%{commit}
tar xzf %{S:1} -C exts/dbcsr --strip-components=1
echo git:%{shortcommit} > REVISION
%else
%setup -q
%endif
%patch10 -p1 -b .r
sed -i 's|@libdir@|%{_libdir}|' Makefile
rm tools/build_utils/fypp
rm -rv exts/dbcsr/tools/build_utils/fypp

# Generate necessary symlinks
TARGET=Linux-%{_target_cpu}-gfortran
ln -s Linux-x86-64-gfortran.ssmp arch/${TARGET}.ssmp
for m in mpich openmpi ; do
    ln -s Linux-x86-64-gfortran.psmp arch/${TARGET}-${m}.psmp
done

# fix crashes in fftw on i686. Need to run on original file, otherwise symlinks will be replaced with copies.
%ifarch i686
sed -i 's/-D__FFTW3/-D__FFTW3 -D__FFTW3_UNALIGNED/g' arch/Linux-x86-64-gfortran*
%endif

for f in arch/Linux-x86-64-gfortran.{psmp,ssmp}; do
%ifarch x86_64
 sed -i 's|@LIBSMM_DEFS@|-D__LIBXSMM|;s|@LIBSMM_LIBS@|-lxsmmf -lxsmm|' $f
%else
 sed -i 's|@LIBSMM_DEFS@||;s|@LIBSMM_LIBS@||' $f
%endif
done

pathfix.py -i "%{__python3} -Es" -p $(find . -type f -name *.py)

%build
TARGET=Linux-%{_target_cpu}-gfortran
OPTFLAGS_COMMON="%(echo %{optflags} | sed -e 's/ -Werror=format-security//g') -fPIC -I%{_fmoddir} -fallow-argument-mismatch"
make OPTFLAGS="${OPTFLAGS_COMMON}" DISTLDFLAGS="%{__global_ldflags} -Wl,-rpath,%{_libdir}/cp2k" %{?_smp_mflags} ARCH="${TARGET}" VERSION="ssmp"
%{_openmpi_load}
make OPTFLAGS="${OPTFLAGS_COMMON} -I%{_fmoddir}/openmpi" DISTLDFLAGS="%{__global_ldflags} -Wl,-rpath,${MPI_LIB}/cp2k" %{?_smp_mflags} ARCH="${TARGET}-openmpi" VERSION="psmp"
%{_openmpi_unload}
%{_mpich_load}
make OPTFLAGS="${OPTFLAGS_COMMON} -I%{_fmoddir}/mpich" DISTLDFLAGS="%{__global_ldflags} -Wl,-rpath,${MPI_LIB}/cp2k" %{?_smp_mflags} ARCH="${TARGET}-mpich" VERSION="psmp"
%{_mpich_unload}

%install
TARGET=Linux-%{_target_cpu}-gfortran
mkdir -p %{buildroot}{%{_bindir},%{_libdir}/cp2k,%{_datadir}/cp2k}
install -pm755 exe/${TARGET}/cp2k.ssmp %{buildroot}%{_bindir}
ln -s cp2k.ssmp %{buildroot}%{_bindir}/cp2k.sopt
ln -s cp2k.ssmp %{buildroot}%{_bindir}/cp2k_shell.ssmp
install -pm755 lib/${TARGET}/ssmp/lib*.so %{buildroot}%{_libdir}/cp2k/
install -pm755 lib/${TARGET}/ssmp/exts/dbcsr/libdbcsr.so %{buildroot}%{_libdir}/cp2k/
%{_openmpi_load}
mkdir -p %{buildroot}{${MPI_BIN},${MPI_LIB}/cp2k}
install -pm755 exe/${TARGET}-openmpi/cp2k.psmp %{buildroot}${MPI_BIN}/cp2k.psmp_openmpi
ln -s cp2k.psmp_openmpi %{buildroot}${MPI_BIN}/cp2k.popt_openmpi
ln -s cp2k.psmp_openmpi %{buildroot}${MPI_BIN}/cp2k_shell.psmp_openmpi
install -pm755 lib/${TARGET}-openmpi/psmp/lib*.so %{buildroot}${MPI_LIB}/cp2k/
install -pm755 lib/${TARGET}-openmpi/psmp/exts/dbcsr/libdbcsr.so %{buildroot}${MPI_LIB}/cp2k/
%{_openmpi_unload}
%{_mpich_load}
mkdir -p %{buildroot}{${MPI_BIN},${MPI_LIB}/cp2k}
install -pm755 exe/${TARGET}-mpich/cp2k.psmp %{buildroot}${MPI_BIN}/cp2k.psmp_mpich
ln -s cp2k.psmp_mpich %{buildroot}${MPI_BIN}/cp2k.popt_mpich
ln -s cp2k.psmp_mpich %{buildroot}${MPI_BIN}/cp2k_shell.psmp_mpich
install -pm755 lib/${TARGET}-mpich/psmp/lib*.so %{buildroot}${MPI_LIB}/cp2k/
install -pm755 lib/${TARGET}-mpich/psmp/exts/dbcsr/libdbcsr.so %{buildroot}${MPI_LIB}/cp2k/
%{_mpich_unload}
cp -pr data/* %{buildroot}%{_datadir}/cp2k/

%if %{with check}
# regtests take ~12 hours on aarch64 and ~48h on s390x
%check
cat > fedora.config << __EOF__
export LC_ALL=C
dir_base=%{_builddir}
__EOF__
. /etc/profile.d/modules.sh
export CP2K_DATA_DIR=%{buildroot}%{_datadir}/cp2k/
for mpi in '' mpich openmpi ; do
  if [ -n "$mpi" ]; then
    module load mpi/${mpi}-%{_arch}
    libdir=${MPI_LIB}/cp2k
    mpiopts="-maxtasks 4 -mpiranks 2"
    par=p
    suf="-${mpi}"
  else
    libdir=%{_libdir}/cp2k
    mpiopts=""
    par=s
    suf=""
  fi
  export LD_LIBRARY_PATH=%{buildroot}${libdir}${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}
  tools/regtesting/do_regtest \
    -arch Linux-%{_target_cpu}-gfortran${suf} \
    -config fedora.config \
%if %{git}
    -cp2kdir cp2k-%{commit} \
%else
    -cp2kdir cp2k-%{version} \
%endif
    ${mpiopts} \
    -nobuild \
    -version ${par}smp \

  if [ -n "$mpi" ]; then
    module unload mpi/${mpi}-%{_arch}
  fi
done
%endif

%files common
%license LICENSE
%doc README.md
%{_datadir}/cp2k

%files
%{_bindir}/cp2k.sopt
%{_bindir}/cp2k.ssmp
%{_bindir}/cp2k_shell.ssmp
%dir %{_libdir}/cp2k
%{_libdir}/cp2k/lib*.so

%files openmpi
%{_libdir}/openmpi/bin/cp2k.popt_openmpi
%{_libdir}/openmpi/bin/cp2k.psmp_openmpi
%{_libdir}/openmpi/bin/cp2k_shell.psmp_openmpi
%dir %{_libdir}/openmpi/lib/cp2k
%{_libdir}/openmpi/lib/cp2k/lib*.so

%files mpich
%{_libdir}/mpich/bin/cp2k.popt_mpich
%{_libdir}/mpich/bin/cp2k.psmp_mpich
%{_libdir}/mpich/bin/cp2k_shell.psmp_mpich
%dir %{_libdir}/mpich/lib/cp2k
%{_libdir}/mpich/lib/cp2k/lib*.so

%changelog
* Thu Oct 27 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 9.1-4
- Rebuild for new libxc

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Mar 22 2022 Dominik Mierzejewski <dominik@greysector.net> - 9.1-2
- fix three failing tests due to wrong LD_LIBRARY_PATH setting

* Wed Mar 16 2022 Dominik Mierzejewski <dominik@greysector.net> - 9.1-1
- update to 9.1 (#2036421)
- re-enable LTO on x86_64

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Sep 30 2021 Dominik Mierzejewski <rpm@greysector.net> - 8.2-1
- update to 8.2 (#1911741)
- drop obsolete patch
- enable spglib support

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.1-2.20200925gitdbf7a77
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Sep 25 2020 Dominik Mierzejewski <rpm@greysector.net> - 7.1-1
- update to post-7.1 snapshot for gcc-10 compatibility (#1786794)
- [sp]opt variants are no longer built (use OMP_NUM_THREADS=1 instead)

* Mon Aug 10 2020 Iñaki Úcar <iucar@fedoraproject.org> - 6.1-10
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.1-9
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Nov 17 2019 Tom Callaway <spot@fedoraproject.org> - 6.1-6
- build against scalapack (no more libmpiblacs)

* Sat Aug 10 2019 Dominik Mierzejewski <rpm@greysector.net> - 6.1-5
- fix FTBFS due to wrong LDFLAGS override (#1735053)

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 14 2019 Orion Poplawski <orion@nwra.com> - 6.1-3
- Rebuild for openmpi 3.1.3

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 16 2018 Dominik Mierzejewski <rpm@greysector.net> - 6.1-1
- update to 6.1
- drop obsolete patches
- openblas is available on all supported arches, drop conditional atlas support

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 22 2018 Dominik Mierzejewski <rpm@greysector.net> - 5.1-4
- rebuild against libxsmm-1.8.3-1 which changed SONAME (#1577497)

* Wed Feb 07 2018 Dominik Mierzejewski <rpm@greysector.net> - 5.1-3
- use upstream patch for libxc-4.x support
- reorder and adjust patches
- unbundle fypp
- use python3 in build scripts

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 17 2018 Dominik Mierzejewski <rpm@greysector.net> - 5.1-1
- update to 5.1
- conditionalize testing and disable by default as they take too long
- test all flavors, not just OpenMPI ssmp
- fix compilation on 32bit architectures

* Mon Oct 23 2017 Susi Lehtola <susi.lehtola@iki.fi> - 4.1-5
- Rebuild against libxc 4.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 17 2017 Dominik Mierzejewski <rpm@greysector.net> - 4.1-2
- build with libxsmm on x86_64 for improved matrix multiplication performance
- simplify some loops
- drop support for old blacs (even EL6 has scalapack with blacs now)

* Thu Jun 15 2017 Dominik Mierzejewski <rpm@greysector.net> - 4.1-1
- update to 4.1 + two backported patches
- build with openblas on supported arches (following scalapack and elpa)
- don't run tests on armv7hl and s390x (too slow)

* Mon Feb 06 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.0-6
- Rebuild for libgfortran.so.4

* Sat Oct 22 2016 Orion Poplawski <orion@cora.nwra.com> - 3.0-5
- Rebuild for openmpi 2.0

* Thu May 26 2016 Dominik Mierzejewski <rpm@greysector.net> - 3.0-4
- merge cp2k-shared.patch into cp2k-rpm.patch
- build and install serial version first

* Mon May 09 2016 Dominik Mierzejewski <rpm@greysector.net> - 3.0-3
- filter out all private Requires: and Provides: (#1332985)

* Thu Apr 21 2016 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.0-2
- Build against libxc 3.0.0.

* Sun Apr 10 2016 Dominik Mierzejewski <rpm@greysector.net> - 3.0-1
- update to 3.0 release (#1217862)
- specify target manually instead of using get_arch_code, it's been removed upstream
- move shared libraries to private directory and don't invent ABI version
- separate regtest results tarball is no longer necessary
- bring back support for building with libxc-2.1.2
- fix paths for MPI-enabled libraries
- revamp regtest script calling
- disable regtests for now, they are hanging in tests/QS/regtest-ri-rpa (#1326661)
- clean-up spec file (drop unnecessary stuff)
- use license macro

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-0.4.20150911svn15878
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep 29 2015 Peter Robinson <pbrobinson@fedoraproject.org> 2.7.0-0.3.20150911svn15878
- Rebuild (MPI)

* Fri Sep 11 2015 Dominik Mierzejewski <rpm@greysector.net> - 2.7.0-0.2.20150911svn15878
- update to SVN trunk HEAD (r15878)
- drop obsolete patch
- fix ppc64 platform detection
- don't run regtests on armv7hl for now (too slow)

* Tue Sep 08 2015 Dominik Mierzejewski <rpm@greysector.net> - 2.7.0-0.1.20150908svn15859
- update to SVN trunk HEAD (r15859)
- drop obsolete patch
- build shared libraries and include cp2k_shell (#1132973)
- include data files (#1220730)
- fix compilation of MPI code on 32-bit platforms

* Mon Aug 24 2015 Dominik Mierzejewski <rpm@greysector.net> - 2.6.1-1
- update to 2.6.1
- drop obsolete patch
- use psmp build for regtesting
- make our regtesting config more similar to upstream

* Sun Aug 16 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.6.0-6
- Rebuild for MPI provides

* Mon Jul 27 2015 Sandro Mani <manisandro@gmail.com> - 2.6.0-5
- Rebuild for RPM MPI Requires Provides Change

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.6.0-3
- Rebuilt for GCC 5 C++11 ABI change

* Fri May 01 2015 Dominik Mierzejewski <rpm@greysector.net> - 2.6.0-2
- re-enable tests on i686 and armv7hl, they seem to complete now

* Tue Mar 17 2015 Dominik Mierzejewski <rpm@greysector.net> - 2.6.0-1
- update to 2.6.0 release
- makedepf90 no longer required (replaced with python script)
- drop upstreamed patch
- backport fixes from 2.6 stable branch

* Mon Mar 16 2015 Thomas Spura <tomspur@fedoraproject.org> - 2.5.1-11
- Rebuild for changed mpich libraries

* Tue Oct 14 2014 Dominik Mierzejewski <rpm@greysector.net> - 2.5.1-10
- add Linux on non-x86 support to tools/get_arch_code

* Tue Sep 09 2014 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.5.1-9
- Requires: libint(api).

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jun 24 2014 Dominik Mierzejewski <rpm@greysector.net> - 2.5.1-7
- add ELPA support
- fix download link for reference test data

* Wed Jun 18 2014 Dominik Mierzejewski <rpm@greysector.net> - 2.5.1-6
- rebuild for libint

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 20 2014 Thomas Spura <tomspur@fedoraproject.org> - 2.5.1-4
- run tests with openmpi on 2 cores

* Tue May 13 2014 Thomas Spura <tomspur@fedoraproject.org> - 2.5.1-3
- add upstream reference data for evaluating tests

* Mon May 12 2014 Tom Callaway <spot@fedoraproject.org> - 2.5.1-2
- compile against new blacs in rawhide

* Fri Mar 14 2014 Dominik Mierzejewski <rpm@greysector.net> - 2.5.1-1
- update to upstream 2.5.1 release
- drop backported compilation fix

* Tue Mar 11 2014 Dominik Mierzejewski <rpm@greysector.net> - 2.5.0-1
- update to upstream 2.5 release
- backport compilation fix from SVN
- fix description (cp2k doesn't implement Car-Parinello Molecular Dynamics)

* Mon Mar 10 2014 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.5-0.5.20131112svn13316
- Rebuild against updated libint.

* Sat Feb 22 2014 Deji Akingunola <dakingun@gmail.com> - 2.5-0.4.20131112svn13316
- Rebuild for mpich-3.1

* Mon Dec 23 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.5-0.3.20131112svn13316
- Rebuild against new libint.

* Fri Nov 15 2013 Dominik Mierzejewski <rpm@greysector.net> - 2.5-0.2.20131112svn13316
- use xz to compress SVN snapshot tarball

* Wed Nov 13 2013 Dominik Mierzejewski <rpm@greysector.net> - 2.5-0.1.20131112svn13316
- update to current SVN trunk
- fix build against atlas >= 3.10.1
- use non-threaded atlas for OpenMP builds per upstream recommendation
- fix BR broken by UsrMove feature

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 20 2013 Deji Akingunola <dakingun@gmail.com> - 2.4-5
- Rename mpich2 sub-packages to mpich and rebuild for mpich-3.0

* Sun Jul 14 2013 Dominik Mierzejewski <rpm@greysector.net> - 2.4-4
- rebuild for new OpenMPI

* Tue Jul 02 2013 Dominik Mierzejewski <rpm@greysector.net> - 2.4-3
- build psmp variants (MPI+OpenMP)
- move ssmp build to main package and drop smp subpackage
- drop local config files, patch upstream's and symlink when necessary
- save the output of tools/get_arch_code and re-use it

* Wed Jun 19 2013 Dominik Mierzejewski <rpm@greysector.net> - 2.4-2
- add MPI implementation suffix back to MPI binaries (required by guidelines)

* Mon Jun 17 2013 Dominik Mierzejewski <rpm@greysector.net> - 2.4-1
- update to 2.4 release
- drop gfortran-4.8 patch (fixed upstream)
- reorder libraries in LDFLAGS again to follow current upstream config
- rename both MPI binaries to cp2k.popt

* Thu Apr 18 2013 Dominik Mierzejewski <rpm@greysector.net> - 2.4-0.5.20130418
- correct SVN url in snapshot script
- update to current SVN trunk (r12842)
- use (and patch) upstream-provided configs for x86_64 ssmp and popt builds
- no need to force FC=gfortran anymore

* Wed Apr 17 2013 Dominik Mierzejewski <rpm@greysector.net> - 2.4-0.4.20130220
- fix build with gfortran-4.8 (bug #913927)
- link with libf77blas for MPI builds to avoid undefined reference to symbol 'dgemm_'

* Sun Apr 14 2013 Dominik Mierzejewski <rpm@greysector.net> - 2.4-0.3.20130220
- fix crashes in fftw on i686 (patch by Michael Banck)

* Fri Feb 22 2013 Dominik Mierzejewski <rpm@greysector.net> - 2.4-0.2.20130220
- add requires for respective blacs and scalapack versions

* Wed Feb 20 2013 Dominik Mierzejewski <rpm@greysector.net> - 2.4-0.1.20130220
- re-enable regtests
- update to current SVN trunk (2.4)
- drop svn patch (no longer needed)
- link with libfftw3_omp for ssmp build
- reorder libraries in LDFLAGS per M. Guidon's cp2k installation primer
- add -ffree-line-length-none to Fortran flags
- add a patch to echo the name of reach test (from Debian package)
- build with libxc
- update libint/libderiv options to match current builds

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Dec 26 2012 Kevin Fenzi <kevin@scrye.com> 2.3-2
- Rebuild for new libmpich

* Wed Sep 05 2012 Dominik Mierzejewski <rpm@greysector.net> - 2.3-1
- updated to 2.3 release

* Sun Aug 26 2012 Dominik Mierzejewski <rpm@greysector.net> - 2.3-0.20120825
- updated to current 2.3 branch (trunk)
- added snapshot creator script
- moved new files out of -rpm patch and into separate SourceN entries
- dropped non-standard compiler flags from MPI builds

* Wed Jul 25 2012 Jussi Lehtola <jussilehtola@fedoraproject.org> - 2.1-7.20101006
- Rebuild due to changed libint.

* Tue Jul 24 2012 Thomas Spura <tomspur@fedoraproject.org> - 2.1-6.20101006
- don't run testsuite as it is only usefull when comparing to old outputs
  (which we don't have at buildtime)
- define common description macro
- also build with openmpi/mpich2
- new url

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-5.20101006
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-4.20101006
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-3.20101006
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 07 2010 Dominik Mierzejewski <rpm@greysector.net> 2.1-2.20101006
- make Summary more descriptive
- use atlas instead of blas/lapack
- pass special CFLAGS to support libint's higher values of angular momentum

* Fri Dec 03 2010 Dominik Mierzejewski <rpm@greysector.net> 2.1-1.20101006
- initial package
