%global tarname FreeFem-sources
%global tarvers 4.15
%global ffvers 4.15

%bcond_without serial

# Allow disabling building with/against openmpi
# Build with --without openmpi to not build openmpi
%bcond_without openmpi

# Allow disabling building with/against mpich
# Build with --without openmpi to not build mpich
%bcond_without mpich


%bcond_without xfail

# Don't exercise %%check on the archs below.
# They fail/hang for yet undetermined causes.
# Build with --with checks to force building them.
# Build with --without checks to skip building them.
%ifarch ppc64le aarch64 s390x armv7hl %{ix86} riscv64
%bcond_with checks
%else
%bcond_without checks
%endif

Summary: PDE solving tool
Name: freefem++
Version: %{expand:%(echo %tarvers | tr - .)}
Release: 4%{?dist}
URL: https://freefem.org
Source0: https://github.com/FreeFem/FreeFem-sources/archive/v%{tarvers}.tar.gz#/%{tarname}-%{tarvers}.tar.gz

# Fedora patches
Patch01: 0001-Build-fixes.patch
Patch02: 0002-Fix-formating-buffers.patch
Patch03: 0003-Wsign-compare.patch
Patch04: 0004-Wimplicit-function-declaration.patch
Patch05: 0005-Wreorder.patch
Patch06: 0006-Remove-src-medit-eigenv.h.patch
Patch07: 0007-Wformat-overflow.patch
Patch08: 0008-Use-test-e-instead-of-test-f.patch
Patch09: 0009-Fix-quoting.patch
Patch10: 0010-Use-prebuilt-FreeFEM-documentation.pdf.patch
Patch11: 0011-Install-docs-into-docdir.patch
Patch12: 0012-Use-libdir-to-setup-ff_prefix_dir.patch
Patch13: 0013-Wmisleading-indentation.patch
Patch14: 0014-Fix-missing-includes-for-gcc-11.patch
Patch15: 0015-Modernize-autotools.patch
Patch16: 0016-Unbundle-boost.patch
Patch17: 0017-Fedora-hacks.patch
Patch18: 0018-Comment-out-LD_LBFGS_NOCEDAL.patch

# --disable-download doesn't work
# Bundle hpddm.zip to prevent downloading during builds.
# cf. hpddm in 3rdparty/getall
%if 0%{fedora} > 42
# bleeding edge petsc
# Fails to build on Fedora <= 42
%global hpddm_git_hash acc20d7ad9c28d5cc57e794818689a166a4ccf8a
%global hpddm_git_md5sum 655e35271b8167df4ed0816df8cfe915
%global hpddm_gitdate 20240925
%else
# petsc-3.20.x compatible
# hpddm-20231112gita789a19
%global hpddm_git_hash a789a193f3c9c7c3c2674eb8d1f8db95cd1ae48c
%global hpddm_git_md5sum debcabc4cb0100cd5e79f9efb8cbafe3
%global hpddm_gitdate 20231112
%endif
%global hpddm_gitcommit %(c=%{hpddm_git_hash}; echo ${c:0:7})

%global htool_git_hash 1a3b198ffc6f73cd62059094ca7b606d151da976
%global htool_git_md5sum 325ab9411e7a50212f99c1302f4cf81f
%global htool_gitcommit %(c=%{htool_git_hash}; echo ${c:0:7})
%global htool_gitdate 20240802

%if "%{version}" >= "4.15"
%global bemtool_git_hash 6e61fbf86d8cd53994d9f597e60fde537650ba14
%global bemtool_git_md5sum 2de5404f4a88d7c8847bd85209fd69a1
%global bemtool_gitcommit %(c=%{bemtool_git_hash}; echo ${c:0:7})
%global bemtool_gitdate 20230923
%else
%global bemtool_git_hash 629c44513698405b58c50650cba69419474062ad
%global bemtool_git_md5sum 869832f5cbec4dfb2c16e2d94bad0b7d
%global bemtool_gitcommit %(c=%{bemtool_git_hash}; echo ${c:0:7})
%global bemtool_gitdate 20230917
%endif
Source1: https://github.com/hpddm/hpddm/archive/%{hpddm_gitcommit}/master.zip#/hpddm-%{hpddm_gitdate}git%{hpddm_gitcommit}.zip

# FreeFEM doesn't build docs anymore.
# Use pre-build binary, d/l'ed from
# https://doc.freefem.org/pdf/FreeFEM-documentation.pdf
Source2: https://raw.githubusercontent.com/FreeFem/FreeFem-doc/pdf/FreeFEM-documentation.pdf#/FreeFEM-documentation-4.13-20241205.pdf

# Bundled libraries
Source3: https://www.ljll.math.upmc.fr/frey/ftp/archives/freeyams.2012.02.05.tgz
Source4: https://github.com/htool-ddm/htool/archive/%{htool_gitcommit}/master.zip#/htool-%{htool_gitdate}git%{htool_gitcommit}.zip
%if "%{version}" >= "4.15"
# from branch update_htool
Source5: https://github.com/PierreMarchand20/BemTool/archive/%{bemtool_gitcommit}.zip#/bemtool-%{bemtool_gitdate}git%{bemtool_gitcommit}.zip
%else
Source5: https://github.com/PierreMarchand20/BemTool/archive/%{bemtool_gitcommit}/master.zip#/bemtool-%{bemtool_gitdate}git%{bemtool_gitcommit}.zip
%endif
Source6: https://www.ljll.math.upmc.fr/frey/ftp/archives/mshmet.2012.04.25.tgz
Source7: https://mumps-solver.org/MUMPS_5.6.2.tar.gz

License: LGPL-3.0-or-later

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

# for 3rdparty/getall
BuildRequires: perl(strict) perl(Getopt::Std) perl(Digest::MD5)

# FreeFEM uses a wild mixture of autotools and cmake
BuildRequires:	automake
BuildRequires:	cmake
BuildRequires:	make
BuildRequires:	wget

BuildRequires:	flex
BuildRequires:	bison
BuildRequires:	gcc-c++
BuildRequires:	gcc-gfortran
BuildRequires:	glut-devel
BuildRequires:	gsl-devel
BuildRequires:	libGLU-devel

BuildRequires:	arpack-devel
BuildRequires:	boost-devel
BuildRequires:	coin-or-Ipopt-devel
BuildRequires:	asio-devel
BuildRequires:	gmm-devel
BuildRequires:	fftw-devel
BuildRequires:	hdf5-devel
BuildRequires:	metis-devel
# mmg's packaging is a mess
# By installing mmg* packages, mmg3d plugin will be automatically enabled and test files will require mmg3d-v4 bundled library
# BuildRequires:	mmg-devel mmg2d-devel mmgs-devel mmg3d-devel
BuildRequires:	MUMPS-devel
BuildRequires:	NLopt-devel
BuildRequires:	flexiblas-devel
BuildRequires:	petsc-devel
BuildRequires:	scotch-devel
BuildRequires:	suitesparse-devel
BuildRequires:	SuperLU-devel
BuildRequires:	tetgen-devel

%description
A PDE oriented language using Finite Element Method FreeFem++ is an
implementation of a language dedicated to the finite element method. It
provides you a way to solve Partial Differential Equations (PDE) simply.

Problems involving partial differential equations (pde) of  several
branches of physics such as fluid-structure interactions require
interpolations of data on several meshes and their manipulation within
one program.

FreeFem++ is an extension of freefem, freefem+ written in C++.

%if %{with openmpi}
%package openmpi
Summary: PDE solving tool - OpenMPI version
BuildRequires:	/etc/profile.d/modules.sh
BuildRequires:	openmpi-devel
BuildRequires:	arpack-devel
BuildRequires:	flexiblas-devel
BuildRequires:	fftw-devel
BuildRequires:	hdf5-devel
BuildRequires:	suitesparse-devel
BuildRequires:	SuperLU-devel

BuildRequires:	hdf5-openmpi-devel
BuildRequires:	blacs-openmpi-devel
BuildRequires:	MUMPS-openmpi-devel
BuildRequires:	petsc-openmpi-devel
BuildRequires:	ptscotch-openmpi-devel
BuildRequires:	ptscotch-openmpi-devel-parmetis
BuildRequires:	scalapack-openmpi-devel
BuildRequires:	hypre-openmpi-devel
BuildRequires:	cgnslib-openmpi-devel
BuildRequires:	superlu_dist-openmpi-devel
BuildRequires:	flexiblas-devel

Requires: %{name} = %{version}-%{release}

%description openmpi
This package contains the OpenMPI version of FreeFem++.
%endif

%if %{with mpich}
%package mpich
Summary: PDE solving tool - MPICH version
BuildRequires:	/etc/profile.d/modules.sh
BuildRequires:	mpich-devel
BuildRequires:	arpack-devel
BuildRequires:	flexiblas-devel
BuildRequires:	fftw-devel
BuildRequires:	hdf5-devel
BuildRequires:	suitesparse-devel
BuildRequires:	SuperLU-devel

BuildRequires:	hdf5-mpich-devel
BuildRequires:	blacs-mpich-devel
BuildRequires:	MUMPS-mpich-devel
BuildRequires:	petsc-mpich-devel
BuildRequires:	ptscotch-mpich-devel
BuildRequires:	ptscotch-mpich-devel-parmetis
BuildRequires:	scalapack-mpich-devel
BuildRequires:	hypre-mpich-devel
BuildRequires:	cgnslib-mpich-devel
BuildRequires:	superlu_dist-mpich-devel
BuildRequires:	flexiblas-devel

Requires: %{name} = %{version}-%{release}

%description mpich
This package contains the MPICH version of FreeFem++.
%endif


%prep
%setup -q -c -T -a 0

mv %{tarname}-%{tarvers} serial
pushd serial
%patch -P 01 -p1
%patch -P 02 -p1
%patch -P 03 -p1
%patch -P 04 -p1
%patch -P 05 -p1
%patch -P 06 -p1
%patch -P 07 -p1
%patch -P 08 -p1
%patch -P 09 -p1
%patch -P 10 -p1
%patch -P 11 -p1
%patch -P 12 -p1
%patch -P 13 -p1
%patch -P 14 -p1
%patch -P 15 -p1
%patch -P 16 -p1
%patch -P 17 -p1
%patch -P 18 -p1

sed -i \
  -e 's,/hpddm/zip/7113b9a6b77fceee3f52490cb27941a87b96542f,/hpddm/zip/%{hpddm_git_hash},' \
  -e "s,'6910b7b974f0b60d9c247c666e7f3862','%{hpddm_git_md5sum}'," \
  3rdparty/getall

sed -i \
  -e 's,/htool/archive/946875d79d0036afb4dc2c0c13c165a607d830df.zip,/htool/archive/%{htool_git_hash}.zip,' \
  -e "s,'1403db4800a2d4b69f3da7eb3f6687a2','%{htool_git_md5sum}'," \
  3rdparty/getall

sed -i \
  -e 's,/BemTool/archive/629c44513698405b58c50650cba69419474062ad.zip,/BemTool/archive/%{bemtool_git_hash}.zip,' \
  -e "s,'869832f5cbec4dfb2c16e2d94bad0b7d','%{bemtool_git_md5sum}'," \
  3rdparty/getall

%if %{with xfail}
sed -i -e 's,XFAIL_TESTS = ,XFAIL_TESTS = Pinocchio.edp ,' examples/3dSurf/Makefile.am
sed -i -e 's,XFAIL_TESTS = ,XFAIL_TESTS = testvtk.edp ,' examples/3dSurf/Makefile.am
sed -i -e 's,XFAIL_TESTS =$,XFAIL_TESTS = ,' examples/3d/Makefile.am
sed -i -e 's,XFAIL_TESTS =,XFAIL_TESTS = fallingspheres.edp ,'	examples/3d/Makefile.am
%endif

# Bogus permissions
find . -type f -perm 755 \( -name "*.c*" -o -name "*.h*" -o -name "*.edp" -o -name "*.idp" \) | xargs chmod 644

autoreconf -vif

mkdir -p 3rdparty/pkg
cp %{SOURCE1} 3rdparty/pkg/hpddm.zip
cp %{SOURCE2} FreeFEM-documentation.pdf
cp %{SOURCE3} 3rdparty/pkg/
cp %{SOURCE4} 3rdparty/pkg/htool.zip
cp %{SOURCE5} 3rdparty/pkg/bemtool.zip
cp %{SOURCE6} 3rdparty/pkg/
cp %{SOURCE7} 3rdparty/pkg/
popd

# MPI flavors
%{?with_openmpi:cp -r serial openmpi}
%{?with_mpich:cp -r serial mpich}

%build
%if %{with serial}
pushd serial
%configure \
	INSTALL="%{__install} -p" \
	--disable-optim \
	--disable-download \
	--with-petsc=%{_libdir}/petsc/conf/petscvariables \
	--enable-hpddm --enable-download_hpddm \
	--enable-yams --enable-download_yams \
	--enable-gmm --disable-download_gmm \
	--enable-mumps \
	--enable-mumps_seq --enable-download_mumps_seq \
	--enable-bem --enable-download_bem \
	--enable-htool --enable-download_htool \
	--disable-scalapack --disable-download_scalapack \
	--enable-mshmet --enable-download_mshmet \
	--enable-boost \
	--disable-mmg3d \
	--disable-parmetis --disable-parmmg \
	--with-blas="-L%{_libdir} -lflexiblas" \
	--with-arpack="-L%{_libdir} -larpack" \
	--without-cadna \
	--with-mpi=no \
	--docdir=%{_pkgdocdir} \
	CPPFLAGS="-I$(pwd) -I/usr/include/scotch" \
	CFLAGS="%{optflags} -fPIC" \
	CXXFLAGS="%{optflags} -fPIC"

%define _smp_mflags -j48
make %{?_smp_mflags}
popd
%endif

for mpi in %{?with_mpich:mpich} %{?with_openmpi:openmpi} ; do
  pushd ${mpi}
  . /etc/profile.d/modules.sh
  module load mpi/${mpi}-%{_arch}
  %configure \
	INSTALL="%{__install} -p" \
	--disable-optim \
	--disable-download \
	--with-petsc=%{_libdir}/${mpi}/lib/petsc/conf/petscvariables \
	--enable-hpddm --enable-download_hpddm \
	--enable-yams --enable-download_yams \
	--enable-gmm --disable-download_gmm \
	--enable-mumps \
	--enable-mumps_seq --enable-download_mumps_seq \
	--enable-bem --enable-download_bem \
	--enable-htool --enable-download_htool \
	--enable-scalapack --disable-download_scalapack --with-scalapack-ldflags="-L%{_libdir}/${mpi}/lib" \
	--enable-mshmet --enable-download_mshmet \
	--enable-boost \
	--disable-mmg3d \
	--disable-parmetis --disable-parmmg \
	--with-blas="-L%{_libdir} -lflexiblas" \
	--with-arpack="-L%{_libdir} -larpack" \
	--without-cadna \
	--with-mpi=yes \
	--docdir=%{_pkgdocdir} \
	CPPFLAGS="-I$(pwd) -I/usr/include/scotch" \
	CFLAGS="%{optflags} -fPIC" \
	CXXFLAGS="%{optflags} -fPIC" \
	MPICXX=$MPI_BIN/mpic++ \
	MPIFC=$MPI_BIN/mpifort \
	MPICC=$MPI_BIN/mpicc \
	CXX=$MPI_BIN/mpic++ \
	FC=$MPI_BIN/mpifort \
	CC=$MPI_BIN/mpicc

%define _smp_mflags -j48
  make %{?_smp_mflags}
  module unload mpi/${mpi}-%{_arch}
  popd
done

%install
%if %{with serial}
pushd serial
make DESTDIR=%{buildroot} install
chmod 744 %{buildroot}%{_libdir}/ff++/%{ffvers}/lib/*.so
chmod 644 %{buildroot}%{_libdir}/ff++/%{ffvers}/lib/WHERE*
pushd %{buildroot}%{_datadir}/FreeFEM
popd
# the binary with no suffix should be the generic X11 one according to README
# the build system makes it identical to -nw version, so overwrite it
ln -sf FreeFem++-nw %{buildroot}%{_bindir}/FreeFem++
popd
%endif

for mpi in %{?with_mpich:mpich} %{?with_openmpi:openmpi} ; do
  pushd $mpi
  make DESTDIR=`pwd`/buildtree install
  for bin in FreeFem++-mpi ff-mpirun ; do
    install -D -m 755 -p buildtree/%{_bindir}/$bin %{buildroot}%{_libdir}/${mpi}/bin/${bin}_${mpi}
  done
  for lib in MPICG.so mpi-cmaes.so ; do
    install -D -m 744 -p buildtree/%{_libdir}/ff++/%{ffvers}/lib/mpi/$lib %{buildroot}%{_libdir}/${mpi}/lib/ff++/lib/$lib
  done
  popd
done

%check
%if %{with checks}
%if %{with serial}
pushd serial
export OMP_NUM_THREADS=4
make -j1 check
popd
%endif

for mpi in %{?with_mpich:mpich} %{?with_openmpi:openmpi} ; do
  pushd ${mpi}
  . /etc/profile.d/modules.sh
  module load mpi/${mpi}-%{_arch}
  make -j1 check
  module unload mpi/${mpi}-%{_arch}
  popd
done
%endif

%if %{with serial}
%files
%doc serial/AUTHORS serial/CHANGELOG.md
%doc FreeFEM-documentation.pdf
%license serial/readme/COPYRIGHT
%{_bindir}/FreeFem++
%{_bindir}/FreeFem++-nw
%{_bindir}/bamg
%{_bindir}/cvmsh2
%{_bindir}/ffglut
%{_bindir}/ffmedit
%{_bindir}/ffmaster
%{_libdir}/ff++
%{_bindir}/ff-c++
%{_bindir}/ff-get-dep
%{_datadir}/FreeFEM
# Not useful to install
%exclude %{_bindir}/ff-pkg-download
# Unclear, if to be shipped
%exclude %{_bindir}/md2edp
%endif

%if %{with openmpi}
%files openmpi
%{_libdir}/openmpi/bin/FreeFem++-mpi_openmpi
%{_libdir}/openmpi/bin/ff-mpirun_openmpi
%{_libdir}/openmpi/lib/ff++
%endif

%if %{with mpich}
%files mpich
%{_libdir}/mpich/bin/FreeFem++-mpi_mpich
%{_libdir}/mpich/bin/ff-mpirun_mpich
%{_libdir}/mpich/lib/ff++
%endif

%changelog
* Thu Feb 06 2025 Björn Esser <besser82@fedoraproject.org> - 4.15-4
- Rebuild (NLopt)

* Sun Feb 02 2025 Orion Poplawski <orion@nwra.com> - 4.15-3
- Rebuild with gsl 2.8

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Dec 23 2024 Ralf Corsépius <corsepiu@fedoraproject.org> - 4.14-1
- Update to 4.15.
- Rebase patches.

* Fri Oct 25 2024 Orion Poplawski <orion@nwra.com> - 4.14-12
- Rebuild for hdf5 1.14.5

* Sat Sep 07 2024 Antonio Trande <sagitter@fedoraproject.org> - 4.14-11
- Rebuild for SuperLU-7.0.0

* Fri Aug 16 2024 Sandro Mani <manisandro@gmail.com> - 4.14-10
- Rebuild (scotch-7.0.4)

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.14-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Feb 26 2024 Richard W.M. Jones <rjones@redhat.com> - 4.14-8
- Disable checks on riscv64

* Thu Feb  8 2024 Jerry James <loganjerry@gmail.com> - 4.14-7
- Rebuild for coin-or-Ipopt 3.14.14
- Stop building for i686

* Sun Feb 04 2024 Orion Poplawski <orion@nwra.com> - 4.14-6
- Rebuild with suitesparse 7.6.0

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 07 2024 Antonio Trande <sagitter@fedoraproject.org> - 4.14-3
- Rebuild for MUMPS-5.6.2
- Set Make jobs to 48
- Set MPI compilers
- Set OMP_NUM_THREADS 4

* Sun Dec 17 2023 Antonio Trande <sagitter@fedoraproject.org> - 4.14-2
- Rebuild for superlu_dist-8.2.0

* Fri Dec 08 2023 Ralf Corsépius <corsepiu@fedoraproject.org> - 4.14-1
- Update to 4.14.
- Run tests single-threaded (make -j1 check).
- Use different versions of hdppm on different Fedora releases.
- Drop 0015-Mark-failing-tests-XFAIL.patch.
- Mark failing tests XFAIL from inside spec.

* Sun Oct 29 2023 Orion Poplawski <orion@nwra.com> - 4.13-7
- Rebuild for openmpi 5.0.0, drops i686 and C++ API

* Sun Oct 15 2023 Antonio Trande <sagitter@fedoraproject.org> - 4.13-6
- Rebuild for petsc-3.20.0

* Sat Aug 19 2023 Sandro Mani <manisandro@gmail.com> - 4.13-5
- Rebuild (scotch)

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jul 16 2023 Antonio Trande <sagitter@fedoraproject.org> - 4.13-3
- Rebuild for SuperLU-6.0.0

* Thu Jun 15 2023 Ralf Corsépius <corsepiu@fedoraproject.org> - 4.13-2
- Switch off tests on %%{ix86}.

* Wed Jun 14 2023 Ralf Corsépius <corsepiu@fedoraproject.org> - 4.13-1
- Update to freefem++-4.13.

* Wed May 03 2023 Ralf Corsépius <corsepiu@fedoraproject.org> - 4.12-5
- Update FreeFEM-documentation.pdf.

* Wed May 03 2023 Ralf Corsépius <corsepiu@fedoraproject.org> - 4.12-4
- Reflect update to scotch-7.*.
- Reflect update to petsc-3.18.*.
- Drop support for freefem++-4.11.

* Wed May 03 2023 Ralf Corsépius <corsepiu@fedoraproject.org> - 4.12-3
- Use %%patch -PN instead of %%patchN.
- Update bundled MUMPS to MUMPS_5.5.1.tar.gz.
- Update bundled bemtool to bemtool-20230327git61aa37b.zip.

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 03 2022 Ralf Corsépius <corsepiu@fedoraproject.org> - 4.12-1
- Update to 4.12.

* Thu Sep 08 2022 Ralf Corsépius <corsepiu@fedoraproject.org> - 4.11-5
- Switch back to flexiblas (RHBZ#2121389).
- Modernize autotools.
- Eliminate egrep.
- Rebase patches.
- Drop freefem++-4.10.
- Fix broken changelog entry.
- Update License:-Tag.

* Tue Aug 23 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.11-4
- Rebuild for gsl-2.7.1

* Tue Aug 16 2022 Ralf Corsépius <corsepiu@fedoraproject.org> - 4.11-3
- Rebuild for asio-1.24.0.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Apr 11 2022 Ralf Corsépius <corsepiu@fedoraproject.org> - 4.11-1
- Update to 4.11.
- Rebase patches.
- Update docs.
- Remove support for freefem < 4.10.

* Fri Apr 08 2022 Ralf Corsépius <corsepiu@fedoraproject.org> - 4.10-1
- Update to 4.10.
- Rebase patches.

* Fri Apr 08 2022 Ralf Corsépius <corsepiu@fedoraproject.org> - 4.9-1
- Update to 4.9.
- Rebase patches.

* Fri Apr 08 2022 Ralf Corsépius <corsepiu@fedoraproject.org> - 4.8-1
- Update to 4.8.
- Rebase patches.
- Spec file cleanup.

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Nov 22 2021 Orion Poplawski <orion@nwra.com> - 4.7-9
- Rebuild for hdf5 1.12.1

* Sat Oct 30 2021 Antonio Trande <sagitter@fedoraproject.org> - 4.7-8
- Rebuild for SuperLU-5.3.0

* Mon Oct 18 2021 Antonio Trande <sagitter@fedoraproject.org> - 4.7-7
- Rebuild for PETSc-3.16.0

* Tue Aug 10 2021 Orion Poplawski <orion@nwra.com> - 4.7-6
- Rebuild for hdf5 1.10.7

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 17 2021 Antonio Trande <sagitter@fedoraproject.org> - 4.7-4
- Rebuild for MUMPS-5.4.0
- Restore LargeDiag_MC64 call

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 05 2020 Jeff Law <law@redhat.com> - 4.7-2
- Fix missing #includes for gcc-11

* Thu Sep 17 2020 Ralf Corsépius <corsepiu@fedoraproject.org> - 4.7-1
- Update to 4.7.
- Rebase patches.

* Wed Sep 16 2020 Ralf Corsépius <corsepiu@fedoraproject.org> - 4.6-6
- Fix previous changelog entry.

* Tue Sep 15 2020 Ralf Corsépius <corsepiu@fedoraproject.org> - 4.6-5
- Update FreeFEM-documentation.pdf
- Add %%{?_smp_mflags} to selected make calls.

* Wed Aug 12 2020 Iñaki Úcar <iucar@fedoraproject.org> - 4.6-4
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Orion Poplawski <orion@cora.nwra.com> - 4.6-2
- Rebuild for hdf5 1.10.6

* Sun May 03 2020 Ralf Corsépius <corsepiu@fedoraproject.org> - 4.6-1
- Update to 4.6
- Rebase patches.
- BR: asio-devel.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 06 2019 Ralf Corsépius <corsepiu@fedoraproject.org> - 4.4.2-1
- Update to 4.4.2
- Rebase patches.

* Tue Aug 20 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.62-5
- Rebuilt for GSL 2.6.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.62-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar 16 2019 Orion Poplawski <orion@nwra.com> - 3.62-3
- Rebuild for hdf5 1.10.5

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.62-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.62-1
- Update to 3.62.
- Rebase patches.

* Thu Jan 24 2019 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.61-1
- Update to 3.61.
- Rebase patches.
- Reflect upstream URL having changed.
- Disable checks on arm7vl.

* Thu Aug 23 2018 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.60-1
- Update to 3.60.
- Rebase patches.

* Tue Aug 21 2018 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.59-3
- Switch to using openblas instead of atlas (RHBZ#1618945).
- Enable checks on %%{x86}.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.59-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Feb 24 2018 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.59-1
- Upgrade to 3.59.
- Update patches.
- Reflect upstream having added ffmaster.

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.58-3
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.58-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Feb 02 2018 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.58-1
- Upgrade to 3.58.
- Drop supporting freefem++ < 3.57.
- Switch to superlu5.

* Fri Feb 02 2018 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.57-2
- Rebuilt for GCC-8.0.1
- Preps for 3.58.

* Mon Dec 11 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.57-1
- Update to 3.57.
- Append --without-cadna to %%configure.
- Build against SuperLU5 for freefem++ >= 3.57.

* Tue Oct 03 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.56.1-1
- Update to 3.56-1.
- Spec file cosmetics.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.56-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.56-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.56-1
- Update to 3.56.

* Fri Jun 23 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.55-1
- Update to 3.55.
- Remove bogus CFLAGS.
- Don't build unused parts of the source tree.
- Add  0008-Wdelete-non-virtual-dtor.patch (Bogus C++ code).

* Thu May 25 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.53-4
- Unbundle pstream.
- Preps for 3.53-1.
- Add 0007-Unbundle-pstream.patch (Remove bundled pstreams).
- Drop obsolete Obsoletes/Provides.
- Rework CFLAGS handling.

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.53-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Tue May 09 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.53-2
- Add SuperLU43.

* Mon May 08 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.53-1
- Update to 3.53.
- Rework patches.
- Skip %%check except on %%{ix86} ppc64le ppc64 aarch64 s390x.
- Add --with checks, -with openmpi, --with mpich.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.51-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 26 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.51-1
- Update to 3.51.

* Tue Jan 17 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.50.1-1
- Update to 3.50.1.
- Rebase patches.
- Spec cleanup.

* Mon Nov 28 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.50-2
- Enable NLopt.

* Mon Nov 28 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.50-1
- Update to 3.50.

* Fri Oct 21 2016 Orion Poplawski <orion@cora.nwra.com> - 3.49-2
- Rebuild for openmpi 2.0

* Tue Oct 04 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.49-1
- Update to 3.49.
- Eliminate %%dotpl, %%dashpl.

* Thu Sep 08 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.48-1
- Update to 3.48.
- Remove '._*' files.

* Tue Jun 14 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.47-1
- Update to 3.47.

* Mon Apr 11 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.46-1
- Update to 3.46.

* Sat Mar 26 2016 Mukundan Ragavan <nonamedotc@gmail.com> - 3.45-2
- Rebuild for SuperLU soname bump (libsuperlu.so.5.1)

* Sat Mar 12 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.45-1
- Update to 3.45.
- Rebase patches.

* Sat Mar 12 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.44-3
- Bundle hpddm*.zip to prevent downloading while building.

* Mon Feb 22 2016 Orion Poplawski <orion@cora.nwra.com> - 3.44-2
- Rebuild for gsl 2.1

* Sun Feb 21 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.44-1
- Update to 3.44
- Further spec cleanup.
- Drop FreeFem.1 (obsolete).
- Add %%license.

* Thu Feb 18 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.43-1.2
- Update to 3.43-2 (RHBZ#1163130).
- Fix F24FTBFS (RHBZ#1307512).

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.31-9.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep 15 2015 Orion Poplawski <orion@cora.nwra.com> - 3.31-8.3
- Rebuild for openmpi 1.10.0

* Sun Jul 26 2015 Sandro Mani <manisandro@gmail.com> - 3.31-7.3
- Rebuild for RPM MPI Requires Provides Change

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.31-6.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 11 2015 Nils Philippsen <nils@redhat.com> - 3.31-5.3
- rebuild for suitesparse-4.4.4

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 3.31-4.3
- Rebuilt for GCC 5 C++11 ABI change

* Tue Apr 07 2015 Ralf Corsépius <corsepiu@fedoraproject.org> 3.31-3.3
- Rebuild (mpich).

* Wed Feb 18 2015 Rex Dieter <rdieter@fedoraproject.org> 3.31-2.3
- rebuild (fltk,gcc5)

* Fri Sep 19 2014 Dominik Mierzejewski <rpm@greysector.net> 3.31-1.3
- update to 3.31-3 (rhbz#1116574)
- disable blas download attempts during build

* Sat Sep 06 2014 Rex Dieter <rdieter@fedoraproject.org> 3.30-5
- rebuild (gmm), use %%{?..} macro variants (for those possibly not defined or set to %%nil))

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.30-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 29 2014 Dominik Mierzejewski <rpm@greysector.net> 3.30-3
- build against tetgen

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 25 2014 Dominik Mierzejewski <rpm@greysector.net> 3.30-1
- update to 3.30

* Mon May 12 2014 Tom Callaway <spot@fedoraproject.org> 3.29-2
- compile against new blacs

* Mon Mar 10 2014 Dominik Mierzejewski <rpm@greysector.net> 3.29-1
- update to 3.29
- reduce redundant spec code

* Tue Feb 25 2014 Dominik Mierzejewski <rpm@greysector.net> 3.27-3
- fix compilation and build against SuperLU

* Sun Feb 23 2014 Dominik Mierzejewski <rpm@greysector.net> 3.27-2
- rebuild for mpich-3.1

* Sun Feb 16 2014 Dominik Mierzejewski <rpm@greysector.net> 3.27-1
- update to 3.27

* Fri Dec 06 2013 Nils Philippsen <nils@redhat.com> - 3.26-2.2
- rebuild (suitesparse)

* Thu Nov 28 2013 Dominik Mierzejewski <rpm@greysector.net> 3.26-1.2
- update to 3.26-2
- build with proper multi-MPI support
- build with gmm support
- WIP mumps/metis/scotch support (disabled for now)
- add missing tex dependencies
- drop obsolete patches
- explicitly disable all unavailable dependencies
- drop devel subpackage
- drop obsolete specfile constructs
- fix build with new atlas

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.19-5.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.19-4.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.19-3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jul 14 2012 Dominik Mierzejewski <rpm@greysector.net> 3.19-2.1
- move MPI plugins to mpi subpackage

* Fri Jul 13 2012 Dominik Mierzejewski <rpm@greysector.net> 3.19-1.1
- update to 3.19-1
- rebased patches
- dropped upstreamed patch
- enable gsl interface
- added missing include which breaks compilation with gcc-4.7

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.12-3
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Feb 27 2011 Dominik Mierzejewski <rpm@greysector.net> 3.12-1
- update to 3.12
- rebased patches

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 14 2010 Dominik Mierzejewski <rpm@greysector.net> 3.11-1
- update to 3.11
- fix build
- fix duplicate binaries in the main package

* Mon Nov 15 2010 Dominik Mierzejewski <rpm@greysector.net> 3.10-1
- update to 3.10-1
- drop no longer necessary gcc-4.5 patch

* Sat Sep 04 2010 Dominik Mierzejewski <rpm@greysector.net> 3.9-3.2
- update to 3.9-2

* Sun Aug 29 2010 Dominik Mierzejewski <rpm@greysector.net> 3.9-2.1
- update to 3.9-1

* Wed Aug 04 2010 Dominik Mierzejewski <rpm@greysector.net> 3.9-1
- update to 3.9
- fix compilation with gcc-4.5.1

* Thu Feb 25 2010 Dominik Mierzejewski <rpm@greysector.net> 3.8-1
- update to 3.8
- fix FTBFS (rhbz #564731)

* Fri Jan 15 2010 Dominik Mierzejewski <rpm@greysector.net> 3.7-1.1
- update to 3.7-1
- disable testsuite again (rhbz #524511)

* Sat Dec  5 2009 Dominik Mierzejewski <rpm@greysector.net> 3.6-1.1
- update to 3.6-1
- drop upstream'd/obsolete patches
- move scripts to %%{_datadir}
- reenable testsuite

* Mon Sep 21 2009 Dominik Mierzejewski <rpm@greysector.net> 3.5-2
- disable testsuite

* Sun Sep 20 2009 Dominik Mierzejewski <rpm@greysector.net> 3.5-1
- update to 3.5
- adjust environment modules setup for current version
- use openmpi instead of lam (regression tests pass locally)
- remove irrelevant READMEs and old changelogs from docs
- add examples to -devel subpackage
- fix some minor build problems

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-6.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Dominik Mierzejewski <rpm@greysector.net> 3.0-5.5
- update to 3.0-5
- fix build with gcc-4.4
- fix build with Fedora-mandated CFLAGS
- sort BRs alphabetically

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-3.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 15 2008 Deji Akingunola <dakingun@gmail.com> - 3.0-2.3
- Rebuild for atlas-3.8.2

* Wed Dec 10 2008 Dominik Mierzejewski <rpm@greysector.net> 3.0-2.2
- update to 3.0-2
- fix compilation
- fix installation paths and path substitution in ff-c++
- preserve timestamps in make install
- add missing BR
- disable regression tests for now

* Fri Dec 05 2008 Dominik Mierzejewski <rpm@greysector.net> 3.0-1.1
- update to 3.0
- fixed build of pdf doc
- dropped obsolete patch

* Wed Oct 01 2008 Dominik Mierzejewski <rpm@greysector.net> 2.24-5.2
- fix encoding of some doc files
- fix author's name in COPYRIGHT

* Sun Sep 28 2008 Dominik Mierzejewski <rpm@greysector.net> 2.24-4.2
- disabled testsuite on ppc64
- kill lamd processes upon completing make check

* Wed Sep 24 2008 Dominik Mierzejewski <rpm@greysector.net> 2.24-3.2
- updated to 2.24-2
- fixed build in rawhide
- re-enable testsuite

* Fri Feb 22 2008 Dominik Mierzejewski <rpm@greysector.net> 2.24-2
- fix build on ppc64

* Fri Feb 22 2008 Dominik Mierzejewski <rpm@greysector.net> 2.24-1
- updated to 2.24

* Wed Feb 20 2008 Dominik Mierzejewski <rpm@greysector.net> 2.23-1
- updated to 2.23
- fixed build with gcc-4.3 (with help from Denis Leroy)
- use file deps for latex tools
- MPI part doesn't build on ppc64 (bug #433870)

* Sun Apr 29 2007 Dominik Mierzejewski <rpm@greysector.net> 2.16-2
- enable testsuite
- remove load tests from testsuite, the rest completes fine

* Sat Apr 28 2007 Dominik Mierzejewski <rpm@greysector.net> 2.16-1
- updated to 2.16-2
- simplified defattr
- work around X11 "detection"
- work around lam's mpicxx.h misdetection in configure

* Tue Mar 27 2007 Dominik Mierzejewski <rpm@greysector.net> 2.14-2
- updated to 2.14-2

* Mon Mar 19 2007 Dominik Mierzejewski <rpm@greysector.net> 2.14-1
- updated to 2.14-1
- removed redundant builddeps

* Thu Nov 23 2006 Dominik Mierzejewski <rpm@greysector.net> 2.11-2
- specfile cleanups
- added manpage from CVS

* Fri Nov 17 2006 Dominik Mierzejewski <rpm@greysector.net> 2.11-1
- updated to 2.11
- specfile cleanups

* Tue Jun 27 2006 Dominik Mierzejewski <rpm@greysector.net>
- updated to latest CVS

* Mon May 15 2006 Dominik Mierzejewski <rpm@greysector.net>
- split into subpackages

* Wed Apr 26 2006 Dominik Mierzejewski <rpm@greysector.net>
- initial build
