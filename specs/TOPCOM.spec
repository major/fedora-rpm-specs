Name:           TOPCOM
Version:        1.1.2
Release:        7%{?dist}
Summary:        Triangulations Of Point Configurations and Oriented Matroids

%global upver %(tr . _ <<< %{version})

License:        GPL-2.0-or-later
URL:            https://www.wm.uni-bayreuth.de/de/team/rambau_joerg/TOPCOM/
VCS:            git:%{url}.git
Source0:        https://www.wm.uni-bayreuth.de/de/team/rambau_joerg/TOPCOM-Downloads/%{name}-%{upver}.tgz
# A replacement Makefile.  See the %%build section for more information.
Source1:        %{name}-Makefile
# Remove a pessimizing call to std::move
Patch:          %{name}-pessimizing-move.patch
# Add virtual destructors where needed
Patch:          %{name}-virtual-destructor.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  boost-devel
BuildRequires:  gcc-c++
BuildRequires:  libsoplex-devel
BuildRequires:  make
BuildRequires:  pkgconfig(cddlib)
BuildRequires:  pkgconfig(gmp)
BuildRequires:  pkgconfig(mpfr)
BuildRequires:  pkgconfig(tbb)
BuildRequires:  pkgconfig(zlib-ng)
BuildRequires:  qsopt-ex-devel
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%global topcom_major %(cut -d. -f1 <<< %{version})
%global topcom_minor %(cut -d. -f2 <<< %{version})

%description
TOPCOM is a package for computing Triangulations Of Point Configurations
and Oriented Matroids.  It was very much inspired by the maple program
PUNTOS, which was written by Jesus de Loera.  TOPCOM is entirely written
in C++, so there is a significant speed up compared to PUNTOS.

%package devel
Summary:        Header files needed to build with %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       cddlib-devel%{?_isa}
Requires:       gmp-devel%{?_isa}
Requires:       qsopt-ex-devel%{?_isa}

%description devel
Header files needed to build applications that use the %{name} library.

%package libs
Summary:        Core %{name} functionality in a library

%description libs
Command line tools that expose %{name} library functionality.

%package examples
Summary:        Example inputs and outputs for TOPCOM
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description examples
Example input and output files for TOPCOM.

%prep
%autosetup -n topcom-%{version} -p1

%conf
# Fix character encoding
iconv -f iso8859-1 -t utf8 -o README.utf8 README
touch -r README README.utf8
mv -f README.utf8 README

# Mimic upstream's modification of gmpxx.h, using the system gmpxx.h
mkdir -p external/include
sed "s|// \(q\.canonicalize\)|\1|" %{_includedir}/gmpxx.h > \
  external/include/gmpxx.h

%build
# We cannot use upstream's build system.  It has the following problems.
# (1) It builds two static libraries, libTOPCOM.a and libCHECKREG.a, then
#     includes both libraries in each of the 60 binaries that it installs in
#     %%{_bindir}.
# (2) Each of libTOPCOM.a and libCHECKREG.a refers to symbols defined by the
#     other.
# (3) It builds static cddlib and qsopt_ex libraries, which are also linked into
#     all of the constructed binaries.  There is no way to make it use the
#     installed versions of those libraries instead.
# We could fix (3) with a little build system hackery.  We could fix (1) by
# building shared libraries, but that doesn't help with (2).  Instead, we pull
# in our own evilly constructed Makefile to build a single shared library
# containing all of the object files in both libTOPCOM.a and libCHECKREG.a,
# and link the binaries against that and the system cddlib and qsopt_ex
# libraries.
sed -e 's|@RPM_OPT_FLAGS@|%{build_cxxflags}|' \
    -e 's|@RPM_LD_FLAGS@|%{build_ldflags}|' \
    -e 's|@bindir@|%{_bindir}|' \
    -e 's|@libdir@|%{_libdir}|' \
    -e 's|@includedir@|%{_includedir}|' \
    -e 's|@version@|%{version}|' \
    -e 's|@major@|%{topcom_major}|' \
    -e 's|@minor@|%{topcom_minor}|' \
    -e 's|#version#|@version@|' \
    %{SOURCE1} > Makefile
%make_build

%install
%make_install

# Get rid of the Makefiles in the examples dir before packaging
rm -f examples/Makefile*

# Rename binaries with common names
for bin in cross cube cyclic hypersimplex lattice; do
  mv %{buildroot}%{_bindir}/$bin %{buildroot}%{_bindir}/TOPCOM-$bin
done

# Do not package the check executable
rm %{buildroot}%{_bindir}/check

%check
LD_LIBRARY_PATH=$PWD src/check

%files
%{_bindir}/B_A
%{_bindir}/B_A_center
%{_bindir}/B_D
%{_bindir}/B_D_center
%{_bindir}/B_S
%{_bindir}/B_S_center
%{_bindir}/TOPCOM*
%{_bindir}/binomial
%{_bindir}/checkregularity
%{_bindir}/chiro2*
%{_bindir}/cocircuits2facets
%{_bindir}/Dnxk
%{_bindir}/kDn
%{_bindir}/permutahedron
%{_bindir}/points2*
%{_bindir}/santos_*

%files devel
%{_includedir}/%{name}/
%{_libdir}/libTOPCOM.so

%files libs
%doc AUTHORS ChangeLog README
%license COPYING
%{_libdir}/libTOPCOM.so.1*

%files examples
%doc examples

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Dec  4 2024 Jerry James <loganjerry@gmail.com> - 1.1.2-6
- Link with libz-ng instead of libz

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 24 2024 Jerry James <loganjerry@gmail.com> - 1.1.2-4
- Rebuild for soplex 7.1.0

* Wed Jun 19 2024 Jerry James <loganjerry@gmail.com> - 1.1.2-3
- Rebuild for soplex 7.0.1

* Wed Mar 13 2024 Jerry James <loganjerry@gmail.com> - 1.1.2-2
- Rebuild for soplex 7.0.0

* Fri Feb 23 2024 Jerry James <loganjerry@gmail.com> - 1.1.2-1
- Version 1.1.2
- Drop the custom man pages due to lack of ability to maintain them
- Build with soplex support
- Stop building for 32-bit x86

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 14 2022 Jerry James <loganjerry@gmail.com> - 0.17.10-2
- Use more specific globs in %%files
- Convert License tag to SPDX

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 21 2022 Jerry James <loganjerry@gmail.com> - 0.17.10-1
- Version 0.17.10

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.8-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct 13 2018 Jerry James <loganjerry@gmail.com> - 0.17.8-8
- Rebuild for cddlib 0.94j

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Sep 28 2017 Jerry James <loganjerry@gmail.com> - 0.17.8-5
- Rebuild for cddlib

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Sep 28 2016 Jerry James <loganjerry@gmail.com> - 0.17.8-1
- New upstream release

* Wed Jul 13 2016 Jerry James <loganjerry@gmail.com> - 0.17.7-1
- New upstream release

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 12 2016 Jerry James <loganjerry@gmail.com> - 0.17.6-2
- Rename some binaries (bz 1297088)

* Thu Oct 15 2015 Jerry James <loganjerry@gmail.com> - 0.17.6-1
- New upstream release

* Wed Sep 16 2015 Jerry James <loganjerry@gmail.com> - 0.17.5-4
- Link with RPM_LD_FLAGS

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.17.5-2
- Rebuilt for GCC 5 C++11 ABI change

* Thu Jan  8 2015 Jerry James <loganjerry@gmail.com> - 0.17.5-1
- New upstream release
- Use license macro

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Sep  3 2013 Jerry James <loganjerry@gmail.com> - 0.17.4-4
- Split examples into a noarch subpackage, due to their size

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Aug  8 2012 Jerry James <loganjerry@gmail.com> - 0.17.4-1
- New upstream release
- Drop upstreamed GCC 4.7 patch
- Adapt to upstream modification of gmpxx.h
- Move man page installation to the Makefile

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Mar 29 2012 Jerry James <loganjerry@gmail.com> - 0.17.1-3
- Preserve timestamps when installing
- Move most of the doc files to the -libs subpackage

* Wed Mar 28 2012 Jerry James <loganjerry@gmail.com> - 0.17.1-2
- Fix build failure due to restricted C++ lookups in GCC 4.7

* Tue Oct 18 2011 Jerry James <loganjerry@gmail.com> - 0.17.1-1
- Initial RPM
