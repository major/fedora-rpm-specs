Name:			orsa
Version:		0.7.0
Release:		61%{?dist}
Summary:		Orbit Reconstruction, Simulation and Analysis

License:		GPLv2+ 
URL:			http://orsa.sourceforge.net
Source0:		http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:		ORSA_MPI
# Patch to build with GCC 4.3
# Reported into upstream bugtracker as
# http://sourceforge.net/tracker/index.php?func=detail&aid=2099077&group_id=44502&atid=439768
Patch0:			orsa-gcc43.patch
# Patching configure in order to:
# - make it find the fftw2 library properly (-lm was missing but needed)
# - make it find the cln and ginac libraries properly as they do not use 
# {cln,ginac}-config anymore but rely on pkg-config instead in F9 and higher
# Reported into upstream bugtracker as
# http://sourceforge.net/tracker/index.php?func=detail&aid=2099054&group_id=44502&atid=439768
Patch1:			orsa-configure.patch
# Patch that prevents orsa from printing many errors on startup because of missing
# configuration files.
# Reported into upstream bugtracker as
# http://sourceforge.net/tracker/?func=detail&aid=2741094&group_id=44502&atid=439768
Patch2:			orsa-file.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1282004
Patch3:                 orsa-gsl-2.patch

Patch4:                 orsa-linking.patch
Patch5: orsa-configure-c99.patch

# Files copied in from rpm-build-4.15.1 since they are gone in later versions.
Source2:                config.guess
Source3:                config.sub

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  readline-devel
BuildRequires:  qt3-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  fftw2-devel
BuildRequires:  gsl-devel
BuildRequires:  cln-devel
BuildRequires:  ginac-devel
BuildRequires:  autoconf
BuildRequires:  libtool

Requires:	%{name}-common = %{version}-%{release}

%description
ORSA is an interactive tool for scientific grade Celestial Mechanics
computations. Asteroids, comets, artificial satellites, Solar and extra-Solar
planetary systems can be accurately reproduced, simulated, and analyzed. 

%package devel
Summary:	Development files for %{name}

Requires:	fftw2-devel
Requires:	gsl-devel
Requires:	zlib-devel
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-headers = %{version}-%{release}

%description devel
This package contains development files for %{name}.

%package openmpi
Summary:	A build of %{name} with support for OpenMPI

BuildRequires: openmpi-devel
Requires:	%{name}-common = %{version}-%{release}

%description openmpi
This package contains a build of %{name} with support for OpenMPI.

%package openmpi-devel
Summary:	Development files for %{name} build with support for OpenMPI

Requires: %{name}-openmpi = %{version}-%{release}
Requires: %{name}-headers = %{version}-%{release}

%description openmpi-devel
This package contains development files for a build of %{name}
 with support for OpenMPI.

%package mpich
Summary:	A build of %{name} with support for MPICH MPI

BuildRequires:	mpich-devel-static
Requires:	%{name}-common = %{version}-%{release}
Provides:	%{name}-mpich2 = %{version}-%{release}
Obsoletes:	%{name}-mpich2 < 0.7.0-24

%description mpich
This package contains a build of %{name} with support for MPICH MPI.

%package mpich-devel
Summary:	Development files for %{name} build with support for MPICH MPI

Requires:	%{name}-mpich = %{version}-%{release}
Requires:	%{name}-headers = %{version}-%{release}
Provides:	%{name}-mpich2-devel = %{version}-%{release}
Obsoletes:	%{name}-mpich2-devel < 0.7.0-24

%description mpich-devel
This package contains development files for a build of %{name}
with support for MPICH MPI.

%package headers
Summary:	Headers for development with %{name}

%description headers
This package contains C++ header files for development with %{name}.

%package common
Summary:	Common files for %{name}

%description common
This package contains files shared across the MPI/non-MPI builds of %{name}.

%prep
%autosetup -p1

# Install user hints for MPI support
install -p -m644 %{SOURCE1} .

# Update config.guess/sub to fix builds on new architectures (aarch64/ppc64le)
cp %{SOURCE2} %{SOURCE3} .

%build
# We need to rebuild generated files after updating Makefile.am. Let's
# use a big hammer.
autoreconf -iv

# honor $RPM_OPT_FLAGS
sed -i 's|-g -Wall -W -pipe -ftemplate-depth-64 -O3 -fno-exceptions -funroll-loops -fstrict-aliasing -fno-gcse|$CXXFLAGS|' configure

%global _configure ../configure

# To avoid replicated code define a build macro
%global dobuild() \
mkdir $MPI_COMPILER && \
pushd $MPI_COMPILER && \
%configure $WITH_MPI --prefix=$MPI_HOME --bindir=$MPI_BIN --libdir=$MPI_LIB --program-suffix=$MPI_SUFFIX \\\
	   --disable-dependency-tracking --disable-static \\\
	   "CLN_CONFIG=`which pkg-config` cln" \\\
	   "GINACLIB_CONFIG=`which pkg-config` ginac" \\\
	   CXXFLAGS="$CXXFLAGS -DHAVE_INLINE -DINLINE_FUN=inline" && \
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool && \
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool && \
%make_build && \
popd

%global openmpi_bin %{_libdir}/openmpi/bin
%global openmpi_lib %{_libdir}/openmpi/lib
%global mpich_bin %{_libdir}/mpich/bin
%global mpich_lib %{_libdir}/mpich/lib

################################
echo -e "\n##############################\nNow making the non-MPI version\n##############################\n"
################################

# Build serial version, dummy arguments
MPI_COMPILER=serial MPI_SUFFIX= WITH_MPI=--without-mpi MPI_HOME=%{_prefix} MPI_BIN=%{_bindir} MPI_LIB=%{_libdir} %dobuild

# Build parallel versions: set compiler variables to MPI wrappers
export CC=mpicc
export CXX=mpicxx
export FC=mpif90
export F77=mpif77

################################
echo -e "\n##############################\nNow making the OpenMPI version\n##############################\n"
################################

%{_openmpi_load}
WITH_MPI=--with-mpi %dobuild
%{_openmpi_unload}

################################
echo -e "\n##############################\nNow making the MPICH version\n##############################\n"
################################
%{_mpich_load}
WITH_MPI=--with-mpi %dobuild
%{_mpich_unload}

%install
# Install serial version
%make_install -C serial CPPROG="cp -p"
rm %{buildroot}%{_libdir}/{liborsa.la,libxorsa.la}

# Install OpenMPI version
%{_openmpi_load}
%make_install -C $MPI_COMPILER CPPROG="cp -p"
rm %{buildroot}$MPI_LIB/{liborsa.la,libxorsa.la}
%{_openmpi_unload}

# Install MPICH version
%{_mpich_load}
%make_install -C $MPI_COMPILER CPPROG="cp -p"
rm %{buildroot}$MPI_LIB/{liborsa.la,libxorsa.la}
%{_mpich_unload}

%files
%{_bindir}/xorsa
%{_libdir}/liborsa.so.*
%{_libdir}/libxorsa.so.*

%files devel
%{_libdir}/*.so

%files headers
%{_includedir}/*

%files openmpi
%{openmpi_lib}/liborsa.so.*
%{openmpi_lib}/libxorsa.so.*
%{openmpi_bin}/*

%files openmpi-devel
%{openmpi_lib}/*.so

%files mpich
%{mpich_lib}/liborsa.so.*
%{mpich_lib}/libxorsa.so.*
%{mpich_bin}/*

%files mpich-devel
%{mpich_lib}/*.so

%files common
%license COPYING
%doc DEVELOPERS ORSA_MPI

%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-61
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-60
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 10 2023 Florian Weimer <fweimer@redhat.com> - 0.7.0-59
- Port configure script to C99

* Tue Aug 23 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.7.0-58
- Rebuild for gsl-2.7.1

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-57
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-56
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-55
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-54
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-53
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 24 2020 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.7.0-52
- Fix build with rpm-4.16 (found by koschei)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Aug 20 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.7.0-50
- Rebuilt for GSL 2.6.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar  1 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.7.0-48
- Modernize and fix build (#1675599)

* Thu Feb 14 2019 Orion Poplawski <orion@nwra.com> - 0.7.0-48
- Rebuild for openmpi 3.1.3

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 27 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.7.0-46
- Update linking order to fix build (#1653155)
- Drop obsolete ldconfig scriplets

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Oct 21 2016 Orion Poplawski <orion@cora.nwra.com> - 0.7.0-39
- Rebuild for openmpi 2.0

* Thu May 12 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.7.0-38
- Rebuild for ginac 1.7.0

* Mon Feb 22 2016 Orion Poplawski <orion@cora.nwra.com> - 0.7.0-37
- Rebuild for gsl 2.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep 15 2015 Orion Poplawski <orion@cora.nwra.com> - 0.7.0-34
- Rebuild for openmpi 1.10.0

* Sat Aug 15 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.7.0-33
- Rebuild for MPI provides

* Sun Jul 26 2015 Sandro Mani <manisandro@gmail.com> - 0.7.0-32
- Rebuild for RPM MPI Requires Provides Change

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.7.0-30
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jun 25 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.7.0-28
- Update config.guess/sub to fix FTBFS on new arches

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Feb 22 2014 Deji Akingunola <dakingun@gmail.com> - 0.7.0-26
- Rebuild for mpich-3.1

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 20 2013 Deji Akingunola <dakingun@gmail.com> - 0.7.0-24
- Rename mpich2 sub-packages to mpich and rebuild for mpich-3.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Nov 04 2012 Miloš Jakubíček <xjakub@fi.muni.cz> - 0.7.0-22
- Rebuilt for new mpich2
- Use %%{_*mpi*-_load/unload} macros

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-20
- Rebuilt for c++ ABI breakage

* Tue Jan 24 2012 Orion Poplawski <orion@cora.nwra.com> - 0.7.0-19
- Rebuild for ginac 1.6.2 soname bump

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.7.0-17
- Rebuild for new libpng

* Tue Mar 29 2011 Deji Akingunola <dakingun@gmail.com> - 0.7.0-16
- Rebuild for mpich2 soname bump

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Oct 19 2010 Deji Akingunola <dakingun@gmail.com> - 0.7.0-14
- Rebuild for both mpich2 and openmpi updates

* Thu Dec 10 2009 Deji Akingunola <dakingun@gmail.com> - 0.7.0-13
- No need to force mpicxx to be CC for mpich2 subpackage
- BR mpich2-devel-static

* Thu Nov 26 2009 Deji Akingunola <dakingun@gmail.com> - 0.7.0-12
- Rebuild for mpich2 
- Remove the lam subpackage, lam is no more in Fedora
- Clean-up the spec

* Thu Aug 27 2009 Milos Jakubicek <xjakub@fi.muni.cz> - 0.7.0-11
- Make compliant to new MPI guidelines:
- Do not build in %%install (resolves BZ#513697)
- Split docs into a -common subpackage

* Fri Jul 24 2009 Milos Jakubicek <xjakub@fi.muni.cz> - 0.7.0-10
- Reenabled MPI support in a way described in BZ#511099, introduced
  separate subpackages with support for OpenMPI, MPICH2 and LAM MPI
  implementations.
- Written ORSA_MPI user documentation about MPI support

* Mon Jul 13 2009 Milos Jakubicek <xjakub@fi.muni.cz> - 0.7.0-9
- Rebuilt against new cln 1.3.0
- Temporarily disabled MPI support as current openmpi builds do not ship -devel,
  nor its previous content in the main package

* Sun Apr 12 2009 Milos Jakubicek <xjakub@fi.muni.cz> - 0.7.0-8
- Do not complain at all if the configuration file is missing.

* Wed Apr 08 2009 Milos Jakubicek <xjakub@fi.muni.cz> - 0.7.0-7
- Fix segfault on missing jpl file.

* Tue Apr 07 2009 Milos Jakubicek <xjakub@fi.muni.cz> - 0.7.0-6
- Do not complain loudly if the configuration file is missing (fix #494342)

* Sat Feb 28 2009 Milos Jakubicek <xjakub@fi.muni.cz> - 0.7.0-5
- Rebuilt against new ginac 1.5

* Fri Feb 27 2009 Milos Jakubicek <xjakub@fi.muni.cz> - 0.7.0-4
- Fixed gcc 4.4 build

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Sep 10 2008 Milos Jakubicek <xjakub@fi.muni.cz> - 0.7.0-2
- Patched configure to honor $RPM_OPT_FLAGS
- Added missing Requires: to the -devel subpackage

* Fri Sep 5 2008 Milos Jakubicek <xjakub@fi.muni.cz> - 0.7.0-1
- Initial release.

