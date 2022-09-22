# The package notes feature leads to failed builds for everything that depends
# on ECL.  Turn it off until somebody figures out how to make it work without
# polluting linker flags.
%undefine _package_note_file

Name:           ecl
Version:        21.2.1
Release:        6%{?dist}
Summary:        Embeddable Common-Lisp

License:        LGPLv2+ and BSD and MIT and Public Domain
URL:            https://common-lisp.net/project/ecl/
Source0:        https://common-lisp.net/project/ecl/static/files/release/%{name}-%{version}.tgz
Source1:        %{name}.desktop
# A modified version of src/util/ecl.svg with extra whitespace removed.  The
# extra whitespace made the icon appear very small and shoved into a corner.
Source2:        %{name}.svg
# Metainfo for ECL
Source3:        net.common-lisp.ecl.metainfo.xml
# This patch was sent upstream on 4 Feb 2012.  It fixes a few warnings
# from the C compiler that indicate situations that might be dangerous at
# runtime.
Patch0:         %{name}-21.2.1-warnings.patch
# Do not use a separate thread to handle signals by default if built with
# boehm-gc support.
# This prevents a deadlock when building maxima with ecl support in
# fedora, and should handle by default these problems:
# http://trac.sagemath.org/sage_trac/ticket/11752
# http://www.mail-archive.com/ecls-list@lists.sourceforge.net/msg00644.html
Patch1:         %{name}-20.4.24-signal_handling_thread.patch
# GCC does not implement support for #pragma STDC FENV_ACCESS
Patch2:         %{name}-20.4.24-fenv-access.patch
# Avoid an infinite loop if there is a write error on stderr.  See
# build/pkgs/ecl/patches/write_error.patch in the sagemath distribution.
Patch3:         %{name}-20.4.24-write-error.patch
# Fix bogus test compromised by LTO.
Patch4:         %{name}-20.4.24-configure.patch


BuildRequires:  appstream
BuildRequires:  desktop-file-utils
BuildRequires:  docbook5-schemas
BuildRequires:  docbook5-style-xsl
BuildRequires:  emacs-common
BuildRequires:  gcc
BuildRequires:  gmp-devel
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(atomic_ops)
BuildRequires:  pkgconfig(bdw-gc)
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(x11)
BuildRequires:  texinfo
BuildRequires:  xmlto

Requires:       gcc
Requires:       libgcc%{?_isa}
Requires:       glibc-devel%{?_isa}
Requires:       gc-devel%{?_isa}
Requires:       gmp-devel%{?_isa}
Requires:       libatomic_ops-devel%{?_isa}
Requires:       libffi-devel%{?_isa}
Requires:       hicolor-icon-theme

%description
ECL (Embeddable Common Lisp) is an implementation of the Common Lisp
language as defined by the ANSI X3J13 specification.  ECL features a
bytecode compiler and interpreter, the ability to build standalone
executables and libraries, and extensions such as ASDF, sockets, and
Gray streams.

# no -devel package for header files is split off
# since they are required by the main package


%prep
%autosetup -p0

# Remove spurious executable bits
find src/{c,h} -type f -perm /0111 -exec chmod a-x {} \+

# Temporary fix for missing braces in initializers, causes build failure
sed -i 's/{.*,.*,.*,.*,.*}/{&}/g' src/c/symbols_list.h

# Don't give the library a useless rpath
sed -i "/ECL_LDRPATH='-Wl,--rpath,~A'/d" src/configure


%build
%configure --enable-manual=html --with-sse=auto \
  CFLAGS="%{build_cflags} -Wno-unused -Wno-return-type -Wno-unknown-pragmas"

# Parallel build does NOT work.  Do NOT use _smp_mflags.
make

%install
%make_install

# Remove installed files that are in the wrong place
rm -fr %{buildroot}%{_docdir}
rm -f %{buildroot}%{_libdir}/Copyright
rm -f %{buildroot}%{_libdir}/LGPL

# Install the man pages
mkdir -p %{buildroot}%{_mandir}/man1
sed -e "s|@bindir@|%{_bindir}|" src/doc/ecl.man.in > \
  %{buildroot}%{_mandir}/man1/ecl.1
cp -p src/doc/ecl-config.man.in %{buildroot}%{_mandir}/man1/ecl-config.1

# Add missing executable bits
chmod a+x %{buildroot}%{_libdir}/ecl-%{version}/dpp
chmod a+x %{buildroot}%{_libdir}/ecl-%{version}/ecl_min

# Install the desktop file
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}

# Install the desktop icon
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
cp -p %{SOURCE2} %{buildroot}%{_datadir}/icons/hicolor/scalable/apps

# Install the AppData file
mkdir -p %{buildroot}%{_metainfodir}
install -pm 644 %{SOURCE3} %{buildroot}%{_metainfodir}
appstreamcli validate --no-net \
  %{buildroot}%{_metainfodir}/net.common-lisp.ecl.metainfo.xml


%files
%{_bindir}/ecl
%{_bindir}/ecl-config
%{_datadir}/applications/ecl.desktop
%{_datadir}/icons/hicolor/scalable/apps/ecl.svg
%{_metainfodir}/net.common-lisp.ecl.metainfo.xml
%{_libdir}/ecl*
%{_libdir}/libecl.so.21*
%{_libdir}/libecl.so
%{_includedir}/ecl/
%{_mandir}/man1/*
%doc examples CHANGELOG README.md build/doc/manual/html
%doc src/doc/amop.txt src/doc/types-and-classes
%license COPYING LICENSE


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 21.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Feb  4 2022 Jerry James <loganjerry@gmail.com> - 21.2.1-5
- Turn off package-notes to fix maxima breakage

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 21.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Jan 08 2022 Miro Hrončok <mhroncok@redhat.com> - 21.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/LIBFFI34

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 21.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 19 2021 Jerry James <loganjerry@gmail.com> - 21.2.1-1
- Validate with appstreamcli instead of appstream-util

* Mon Feb  1 2021 Jerry James <loganjerry@gmail.com> - 21.2.1-1
- Version 21.2.1
- Drop upstreamed patches: -fpe-macro, -stack-size
- Add metainfo

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20.4.24-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20.4.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 15 2020 Jeff Law <law@redhat.com> - 20.4.24-2
- Fix configure test compromised by LTO

* Wed Jul  8 2020 Jerry James <loganjerry@gmail.com> - 20.4.24-1
- Version 20.4.24
- Drop upstreamed patches: -atan, -end_of_line, -format-directive-limit,
  -sse-printer
- Add -stack-size and -fpe-macro patches
- Documentation sources are now available in the main tarball

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 16.1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 16.1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar  7 2019 Tim Landscheidt <tim@tim-landscheidt.de> - 16.1.3-9
- Remove obsolete requirements for %%post/%%postun scriptlets

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 16.1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 17 2019 Jerry James <loganjerry@gmail.com> - 16.1.3-7
- Add -format-directive-limit patch from sagemath

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 16.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 16.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 16.1.3-4
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 16.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 16.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 24 2017 Jerry James <loganjerry@gmail.com> - 16.1.3-1
- New upstream release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 16.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Mar  4 2016 Jerry James <loganjerry@gmail.com> - 16.1.2-1
- New upstream release

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 16.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Oct  3 2015 Jerry James <loganjerry@gmail.com> - 16.0.0-1
- New upstream release
- Drop many upstreamed patches

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13.5.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Feb 20 2015 Jerry James <loganjerry@gmail.com> - 13.5.1-9
- Fix stack direction detection (broken with gcc 5)

* Fri Feb 13 2015 Jerry James <loganjerry@gmail.com> - 13.5.1-8
- Use license macro

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 18 2014 Rex Dieter <rdieter@fedoraproject.org> 13.5.1-5
- fix configure check for end-of-line when using -Werror=format-security

* Wed May 14 2014 Rex Dieter <rdieter@fedoraproject.org> 13.5.1-4
- backport GC_start_call_back fixes

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul  3 2013 Jerry James <loganjerry@gmail.com> - 13.5.1-2
- Update -warnings patch with more fixes from upstream

* Mon Jun  3 2013 Jerry James <loganjerry@gmail.com> - 13.5.1-1
- New upstream release
- Drop upstreamed -fixes patch
- Add -fenv-access patch to work around a GCC limitation

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 12.12.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 20 2012 Jerry James <loganjerry@gmail.com> - 12.12.1-3
- BR libatomic_ops-static instead of -devel (bz 889173)
- Pull in upstream patches for bugs discovered post-release
- Documentation needs docbook 5 schemas and XSL

* Sat Dec 08 2012 Rex Dieter <rdieter@fedoraproject.org> 12.12.1-2
- track libecl soname, so bumps aren't a surprise

* Fri Dec  7 2012 Jerry James <loganjerry@gmail.com> - 12.12.1-1
- New upstream release
- Drop upstreamed patches

* Wed Aug  8 2012 Jerry James <loganjerry@gmail.com> - 12.7.1-1
- New upstream release
- Add sighandler patch to fix thread-enabled build

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 12.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 03 2012 Rex Dieter <rdieter@fedoraproject.org> 12.2.1-4
- ecl missing Requires: libffi-devel (#837102)

* Wed Jun 13 2012 Jerry James <loganjerry@gmail.com> - 12.2.1-3
- Fix Requires so 32-bit gcc is not dragged into 64-bit platforms (bz 831383)
- Apply multiple fixes from bz 821183
- Rebuild to fix bz 822296

* Thu Apr 26 2012 Jerry James <loganjerry@gmail.com> - 12.2.1-2
- Add missing Requires (bz 816675)

* Sat Feb  4 2012 Jerry James <loganjerry@gmail.com> - 12.2.1-1
- New upstream release
- Fix source URL

* Fri Jan  6 2012 Jerry James <loganjerry@gmail.com> - 11.1.1-2
- Rebuild for GCC 4.7
- Drop unnecessary spec file elements (clean script, etc.)

* Thu Oct 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 11.1.1-1.2
- rebuild with new gmp without compat lib

* Mon Oct 10 2011 Peter Schiffer <pschiffe@redhat.com> - 11.1.1-1.1
- rebuild with new gmp

* Tue Mar  1 2011 Jerry James <loganjerry@gmail.com> - 11.1.1-1
- New release 11.1.1
- Drop libffi patch (fixed upstream)
- Add -configure and -warnings patches
- Add SSE2 support on x86_64
- Disable rpath explicitly, as it is now enabled by default
- Add desktop file and icon

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Apr 12 2010 Jerry James <loganjerry@gmail.com> - 10.4.1-1
- New release 10.4.1
- Drop upstreamed semaphore patch
- Add manual built from ecl-doc sources, replaces info documentation

* Tue Mar  9 2010 Jerry James <loganjerry@gmail.com> - 10.3.1-1
- New release 10.3.1

* Wed Feb 24 2010 Jerry James <loganjerry@gmail.com> - 10.2.1-1
- New release 10.2.1

* Sun Aug  9 2009 Gerard Milmeister <gemi@bluewin.ch> - 9.8.1-1
- new release 9.8.1

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun 16 2009 Gerard Milmeister <gemi@bluewin.ch> - 9.6.1-1
- new release 9.6.1

* Mon Oct  6 2008 Gerard Milmeister <gemi@bluewin.ch> - 0.9l-2
- disable ppc64 (fails to build)

* Wed Aug  6 2008 Gerard Milmeister <gemi@bluewin.ch> - 0.9l-1
- new release 0.9l

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.9j-2
- Autorebuild for GCC 4.3

* Sat Dec 29 2007 Gerard Milmeister <gemi@bluewin.ch> - 0.9j-1
- new release 0.9j

* Mon Aug 28 2006 Gerard Milmeister <gemi@bluewin.ch> - 0.9i-3
- Rebuild for FE6

* Sun Jul 23 2006 Gerard Milmeister <gemi@bluewin.ch> - 0.9i-2
- release number fix

* Sat Jul  8 2006 Gerard Milmeister <gemi@bluewin.ch> - 0.9i-1
- new version 0.9i

* Wed Mar 15 2006 Gerard Milmeister <gemi@bluewin.ch> - 0.9h-5
- patch for gcc 4.1

* Tue Mar 14 2006 Gerard Milmeister <gemi@bluewin.ch> - 0.9h-4
- removed buildreq perl

* Fri Mar 10 2006 Gerard Milmeister <gemi@bluewin.ch> - 0.9h-3
- fixed permissions and texinfo problems

* Sun Dec  4 2005 Gerard Milmeister <gemi@bluewin.ch> - 0.9h-2
- buildreq m4, texinfo

* Mon Nov 21 2005 Gerard Milmeister <gemi@bluewin.ch> - 0.9h-1
- New Version 0.9h

* Sat Aug 20 2005 Gerard Milmeister <gemi@bluewin.ch> - 0.9g-1
- New Version 0.9g

* Sun Apr 10 2005 Gerard Milmeister <gemi@bluewin.ch> - 0.9e-1.cvs20050410
- CVS Version 20050410

* Sun Apr 10 2005 Gerard Milmeister <gemi@bluewin.ch> - 0.9e-1
- New Version 0.9e

* Sat Nov  6 2004 Gerard Milmeister <gemi@bluewin.ch> - 0:0.9-0.fdr.1.d
- New Version 0.9d

* Sat Mar 27 2004 Gerard Milmeister <gemi@bluewin.ch> - 0:0.9-0.fdr.1.c
- First Fedora release
