# The memory management scheme does not work with PIE
%undefine _hardened_build

%global giturl  https://github.com/polyml/polyml

Name:           polyml
Version:        5.9.1
Release:        6%{?dist}
Summary:        Poly/ML compiler and runtime system

License:        LGPL-2.1-or-later
URL:            https://www.polyml.org/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/v%{version}/%{name}-%{version}.tar.gz

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

# The standard solution to kill the libtool-induced RPATH is to edit the
# libtool script to kill it.  However, that causes problems for us as we need
# to run polyimport at build time.  With the standard approach, it cannot find
# its libraries.
#
# A clean solution would involve upstream changing their Makefiles.  We use
# the unclean solution instead: go with the flow, then strip the RPATHs out
# of the binaries at the end.
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  chrpath
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  motif-devel
BuildRequires:  libffi-devel
BuildRequires:  libtool
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libXt-devel
BuildRequires:  make

Requires:       gcc-c++
Requires:       polyml-libs%{?_isa} = %{version}-%{release}

%description
Poly/ML is a full implementation of Standard ML available as
open-source.  This release supports the ML97 version of the language
and the Standard Basis Library.

%package doc
Summary:        Poly/ML documentation
BuildArch:      noarch

%description doc
Documentation for Poly/ML.

%package libs
Summary:        Poly/ML runtime libraries

%description libs
Runtime libraries for Poly/ML.

%prep
%autosetup -p1

%conf
# Fix end of line encoding
sed -i 's/\r//' documentation/main.css

# Finding asm/elf.h makes the build fail for unknown reasons
sed -i 's, asm/elf\.h,,' configure.ac

# Regenerate the configure script after changing configure.ac
autoreconf -fi .

%build
# Some hand-coded assembler is included.  While it does contain an explicit
# section marker stating that the stack section does not need the executable
# bit, for some reason that marker does not always take effect, causing the
# executable to be marked as needing an executable stack on some arches.  This
# is bad news for people running SELinux.  The execstack flag is not really
# needed, so we go through the contortions below to keep it off.
%configure --enable-shared --disable-static \
%ifarch x86_64 aarch64
  --enable-compact32bit \
%endif
  CPPFLAGS="-D_GNU_SOURCE" \
  CFLAGS="%{build_cflags} -fno-strict-aliasing -Wa,--noexecstack" \
  CXXFLAGS="%{build_cxxflags} -fno-strict-aliasing -Wa,--noexecstack" \
  CCASFLAGS="-Wa,--noexecstack" \
  LDFLAGS="%{build_ldflags} -Wl,-z,noexecstack"
%make_build
chrpath -d .libs/poly
chrpath -d .libs/polyimport

# Change polyc to avoid adding an rpath, and also don't link to extra libraries
# unnecessarily.
sed -i 's/-Wl,-rpath,\${LIBDIR} //;s/-lffi //;s/-lgmp //' polyc

%install
%make_install
rm -f %{buildroot}%{_libdir}/*.la

%check
make check

%files
%{_bindir}/poly
%{_bindir}/polyc
%{_bindir}/polyimport
%{_libdir}/libpolymain.a
%{_libdir}/libpolyml.so
%{_libdir}/polyml/
%{_libdir}/pkgconfig/polyml.pc
%{_mandir}/man1/poly.1*
%{_mandir}/man1/polyc.1*
%{_mandir}/man1/polyimport.1*

%files doc
%doc documentation/*
%license COPYING

%files libs
%license COPYING
%{_libdir}/libpolyml.so.14*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.9.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Jan 14 2025 Jerry James <loganjerry@gmail.com> - 5.9.1-5
- Fix FTBFS by avoiding asm/elf.h

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan  9 2024 Jerry James <loganjerry@gmail.com> - 5.9.1-1
- Version 5.9.1
- Drop upstreamed patch to fix segfault in the bytecode interpreter
- Stop building for 32-bit x86

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 12 2022 Jerry James <loganjerry@gmail.com> - 5.9-4
- Convert License tag to SPDX

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 23 2021 Jerry James <loganjerry@gmail.com> - 5.9-2
- Add upstream patch to fix segfault in the bytecode interpreter

* Sun Nov 21 2021 Jerry James <loganjerry@gmail.com> - 5.9-1
- Version 5.9
- Drop all patches
- Enable compact 32-bit pointers on aarch64
- Skip a segfaulting test on 32-bit ARM until upstream can fix it

* Fri Jul 23 2021 Jerry James <loganjerry@gmail.com> - 5.8.2-3
- Add -pthread-stack-min patch to fix FTBFS

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 21 2021 Jerry James <loganjerry@gmail.com> - 5.8.2-2
- Add upstream patches 4-5 from the fixes-5.8.2 branch

* Wed May  5 2021 Jerry James <loganjerry@gmail.com> - 5.8.2-1
- Version 5.8.2
- Add uptream patches 1-3 from the fixes-5.8.2 branch

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 22 2020 Jerry James <loganjerry@gmail.com> - 5.8.1-1
- Version 5.8.1
- Drop upstreamed -fixes patch

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 25 2019 Jerry James <loganjerry@gmail.com> - 5.8-2
- Upstream's executable stack approach does not work in all cases, so bring
  back the workarounds

* Sat May 18 2019 Jerry James <loganjerry@gmail.com> - 5.8-1
- Add -fixes patch to fix s390x build

* Tue Mar 12 2019 Jerry James <loganjerry@gmail.com> - 5.8-1
- New upstream version
- Drop all patches; all upstreamed
- Drop executable stack workarounds, now handled upstream

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 31 2018 Jerry James <loganjerry@gmail.com> - 5.7.1-5
- Add upstream patches -in-ml, -mutable, and -thread-count

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jul  7 2018 Jerry James <loganjerry@gmail.com> - 5.7.1-3
- Add upstream patch to fix an immutable area bug

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 29 2017 Jerry James <loganjerry@gmail.com> - 5.7.1-1
- New upstream version
- Drop upstreamed -crowbar patch
- Drop ExclusiveArch tag; all Fedora arches are now supported

* Sat Aug 19 2017 Jerry James <loganjerry@gmail.com> - 5.7-3
- Added -crowbar patch to make timeouts while building less likely

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat May 13 2017 Jerry James <loganjerry@gmail.com> - 5.7-1
- New upstream version
- Drop all patches; all were upstreamed

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 24 2017 Jerry James <loganjerry@gmail.com> - 5.6-3
- Do not require libgmp or libffi at runtime (bz 1394556)
- Do not add unnecessary rpaths to user programs
- Add bug fixes from upstream's bug fix branch
- Add -endian patch to fix build failure on ppc64

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 25 2016 Jerry James <loganjerry@gmail.com> - 5.6-1
- New upstream version
- Update the ExclusiveArch list
- Add a check script

* Thu Oct 08 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 5.5.2-9
- Build against motif on fedora >= 24.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.5.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May  2 2015 Jerry James <loganjerry@gmail.com> - 5.5.2-7
- Update -5.5.2-fixes.patch to add the following:
  o Initialise the largeObjectCache fully in the constructor.  When
    MTGCProcessMarkPointers is subclassed in RescanMarked the resulting object
    is created on the stack and the largeObjectCache can contain invalid data
    if it is not cleared (trunc commit 2007)

* Mon Apr 20 2015 Jerry James <loganjerry@gmail.com> - 5.5.2-6
- Update -5.5.2-fixes.patch to add the following:
  o Ensure the large object cache pointer is cleared when processing the roots
    as well as for the marking tasks (trunk commit 2006)
- Do not harden the build; breaks the memory management scheme

* Sat Feb 21 2015 Jerry James <loganjerry@gmail.com> - 5.5.2-5
- Use license macro

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jul 28 2014 Jerry James <loganjerry@gmail.com> - 5.5.2-3
- Add -5.5.2-fixes patch to fix the following:
  o Check for negative sized arrays (trunk commit 1950)
  o Fix segfault in FFI when malloc runs out of memory (trunk commit 1953)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May  9 2014 Jerry James <loganjerry@gmail.com> - 5.5.2-1
- New upstream release
- All patches have been upstreamed; drop them

* Tue Nov  5 2013 Jerry James <loganjerry@gmail.com> - 5.5.1-2
- Add -5.5.1-fixes patch to fix two optimizer bugs (trunk commits 1855 and
  1867), and to fix TexIO.inputN and StreamIO.inputN to return immediately if
  asked for zero characters (trunk commit 1874).

* Tue Sep 17 2013 Jerry James <loganjerry@gmail.com> - 5.5.1-1
- New upstream version

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jun 10 2013 Jerry James <loganjerry@gmail.com> - 5.5-4
- Update -5.5-fixes patch to r1789 to fix an assertion failure during GC.
- Build with -D_FILE_OFFSET_BITS=64 and add -largefile patch.
- Link with RPM_LD_FLAGS.

* Tue Apr 23 2013 Jerry James <loganjerry@gmail.com> - 5.5-3
- Update -5.5-fixes patch to r1693 to fix a bug in Real.fromInt on x86.

* Mon Feb 11 2013 Jerry James <loganjerry@gmail.com> - 5.5-2
- Apply post-release fixes from upstream
- Drop the -sem-wait patch; no longer needed

* Thu Sep 20 2012 Jerry James <loganjerry@gmail.com> - 5.5-1
- New upstream version

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan  7 2012 Jerry James <loganjerry@gmail.com> - 5.4.1-2
- Rebuild for GCC 4.7
- Minor spec file cleanups

* Wed Oct 26 2011 Marcela Mašláňová <mmaslano@redhat.com> - 5.4.1-1.2
- rebuild with new gmp without compat lib

* Wed Oct 12 2011 Peter Schiffer <pschiffe@redhat.com> - 5.4.1-1.1
- rebuild with new gmp

* Mon Aug  8 2011 Jerry James <loganjerry@gmail.com> - 5.4.1-1
- New upstream release

* Fri Apr 29 2011 Dan Horák <dan[at]danny.cz> - 5.4-3
- updated the supported arch list

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Feb  3 2011 Jerry James <loganjerry@gmail.com> - 5.4-1
- Update to 5.4
- Update the -doc files.
- Enable building the portable (non-native) version on unsupported arches.
- Get rid of the execstack flag; prevents running on SELinux-enabled systems.
- Kill RPATH in the executables.
- Add a BR on gmp-devel.
- Add the -sem-wait patch.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 15 2009 Gerard Milmeister <gemi@bluewin.ch> - 5.2.1-1
- new release 5.2.1

* Sun Oct 19 2008 Gerard Milmeister <gemi@bluewin.ch> - 5.2-1
- new release 5.2

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 5.1-4
- Autorebuild for GCC 4.3

* Wed Jan  2 2008 Gerard Milmeister <gemi@bluewin.ch> - 5.1-3
- Exclude arch ppc64

* Wed Jan  2 2008 Gerard Milmeister <gemi@bluewin.ch> - 5.1-1
- new release 5.1

* Tue Mar 27 2007 Gerard Milmeister <gemi@bluewin.ch> - 5.0-2
- spec file fixes

* Mon Feb 12 2007 Gerard Milmeister <gemi@bluewin.ch> - 5.0-1
- new version 5.0
