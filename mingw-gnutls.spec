%?mingw_package_header

Name:           mingw-gnutls
Version:        3.7.1
Release:        5%{?dist}
Summary:        MinGW GnuTLS TLS/SSL encryption library

# The libraries are LGPLv2.1+, utilities are GPLv3+
License: GPLv3+ and LGPLv2+
URL:            http://www.gnutls.org/
Source0:        ftp://ftp.gnutls.org/gcrypt/gnutls/v3.7/gnutls-%{version}.tar.xz
Source1:        ftp://ftp.gnutls.org/gcrypt/gnutls/v3.7/gnutls-%{version}.tar.xz.sig
Source2:        gpgkey-462225C3B46F34879FC8496CD605848ED7E69871.gpg
Patch0:         gnutls-3.7.1-aggressive-realloc-fixes.patch

BuildArch:      noarch

BuildRequires: make
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-libtasn1 >= 4.3
BuildRequires:  mingw32-readline
BuildRequires:  mingw32-zlib
BuildRequires:  mingw32-p11-kit >= 0.23.1
BuildRequires:  mingw32-nettle >= 3.6

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-libtasn1 >= 4.3
BuildRequires:  mingw64-readline
BuildRequires:  mingw64-zlib
BuildRequires:  mingw64-p11-kit >= 0.23.1
BuildRequires:  mingw64-nettle >= 3.6

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  byacc
BuildRequires:  gnupg2
BuildRequires:  gtk-doc
BuildRequires:  libtool
BuildRequires:  git


# Yes, really ...
BuildRequires:  pkgconfig

# For native /usr/bin/msgfmt etc.
BuildRequires:  gettext-devel


%description
GnuTLS TLS/SSL encryption library.  This library is cross-compiled
for MinGW.


# Win32
%package -n mingw32-gnutls
Summary:        MinGW GnuTLS TLS/SSL encryption library
Requires:       pkgconfig
Requires:       mingw32-libtasn1 >= 4.3

%description -n mingw32-gnutls
GnuTLS TLS/SSL encryption library.  This library is cross-compiled
for MinGW.

# Win64
%package -n mingw64-gnutls
Summary:        MinGW GnuTLS TLS/SSL encryption library
Requires:       pkgconfig
Requires:       mingw64-libtasn1 >= 4.3

%description -n mingw64-gnutls
GnuTLS TLS/SSL encryption library.  This library is cross-compiled
for MinGW.


%?mingw_debug_package


%prep
gpgv2 --keyring %{SOURCE2} %{SOURCE1} %{SOURCE0}
%autosetup -S git -n gnutls-%{version}

rm -f lib/minitasn1/*.c lib/minitasn1/*.h

%build
%mingw_configure \
    --enable-sha1-support \
    --disable-static \
    --disable-openssl-compatibility \
    --disable-non-suiteb-curves \
    --disable-libdane \
    --disable-rpath \
    --disable-nls \
    --disable-cxx \
    --enable-local-libopts \
    --enable-shared \
    --without-tpm \
    --with-included-unistring \
    --disable-doc \
    --with-default-priority-string="@SYSTEM"
%mingw_make %{?_smp_mflags}

%install
%mingw_make_install DESTDIR=$RPM_BUILD_ROOT

# Remove .la files
rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/*.la

# The .def files aren't interesting for other binaries
rm -f $RPM_BUILD_ROOT%{mingw32_bindir}/*.def
rm -f $RPM_BUILD_ROOT%{mingw64_bindir}/*.def

# Remove info and man pages which duplicate stuff in Fedora already.
rm -rf $RPM_BUILD_ROOT%{mingw32_infodir}
rm -rf $RPM_BUILD_ROOT%{mingw32_mandir}
rm -rf $RPM_BUILD_ROOT%{mingw32_docdir}/gnutls

rm -rf $RPM_BUILD_ROOT%{mingw64_infodir}
rm -rf $RPM_BUILD_ROOT%{mingw64_mandir}
rm -rf $RPM_BUILD_ROOT%{mingw64_docdir}/gnutls

# Remove test libraries
rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/crypt32.dll*
rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/ncrypt.dll*
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/crypt32.dll*
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/ncrypt.dll*


%files -n mingw32-gnutls
%license LICENSE doc/COPYING doc/COPYING.LESSER
%{mingw32_bindir}/certtool.exe
%{mingw32_bindir}/gnutls-cli-debug.exe
%{mingw32_bindir}/gnutls-cli.exe
%{mingw32_bindir}/gnutls-serv.exe
%{mingw32_bindir}/libgnutls-30.dll
%{mingw32_bindir}/ocsptool.exe
%{mingw32_bindir}/p11tool.exe
%{mingw32_bindir}/psktool.exe
%{mingw32_bindir}/srptool.exe
%{mingw32_libdir}/libgnutls.dll.a
%{mingw32_libdir}/libgnutls-30.def
%{mingw32_libdir}/pkgconfig/gnutls.pc
%{mingw32_includedir}/gnutls/

%files -n mingw64-gnutls
%license LICENSE doc/COPYING doc/COPYING.LESSER
%{mingw64_bindir}/certtool.exe
%{mingw64_bindir}/gnutls-cli-debug.exe
%{mingw64_bindir}/gnutls-cli.exe
%{mingw64_bindir}/gnutls-serv.exe
%{mingw64_bindir}/libgnutls-30.dll
%{mingw64_bindir}/ocsptool.exe
%{mingw64_bindir}/p11tool.exe
%{mingw64_bindir}/psktool.exe
%{mingw64_bindir}/srptool.exe
%{mingw64_libdir}/libgnutls.dll.a
%{mingw64_libdir}/libgnutls-30.def
%{mingw64_libdir}/pkgconfig/gnutls.pc
%{mingw64_includedir}/gnutls/


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 3.7.1-4
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Sep 04 2020 Michael Cronenworth <mike@cchtml.com> - 3.6.15-1
- New upstream release 3.6.15

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 04 2020 Michael Cronenworth <mike@cchtml.com> - 3.6.14-1
- New upstream release 3.6.14

* Tue Mar 31 2020 Michael Cronenworth <mike@cchtml.com> - 3.6.13-1
- New upstream release 3.6.13

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 3.6.9-3
- Rebuild (Changes/Mingw32GccDwarf2)
- Add missing BR: byacc, bison

* Tue Aug 20 2019 Michael Cronenworth <mike@cchtml.com> - 3.6.9-2
- Nettle 3.5.1 rebuild

* Wed Aug 14 2019 Marc-André Lureau <marcandre.lureau@redhat.com> - 3.6.9-1
- New upstream release 3.6.9

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Aug 27 2018 Christophe Fergeau <cfergeau@redhat.com> - 3.6.3-1
- Update to 3.6.3 and sync patches with rawhide native package

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 29 2018 Michael Cronenworth <mike@cchtml.com> - 3.6.2-1
- Update to 3.6.2

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 08 2017 Michael Cronenworth <mike@cchtml.com> - 3.5.13-1
- Update to 3.5.13

* Tue Apr 18 2017 Michael Cronenworth <mike@cchtml.com> - 3.5.11-1
- Update to 3.5.11

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Nov 03 2016 Michael Cronenworth <mike@cchtml.com> - 3.5.5-2
- Nettle 3.3 rebuild

* Thu Nov 03 2016 Michael Cronenworth <mike@cchtml.com> - 3.5.5-1
- Update to 3.5.5

* Thu Sep 08 2016 Michael Cronenworth <mike@cchtml.com> - 3.5.4-1
- Update to 3.5.4

* Tue Jul 12 2016 Michael Cronenworth <mike@cchtml.com> - 3.5.2-1
- Update to 3.5.2

* Wed Jun 01 2016 Michael Cronenworth <mike@cchtml.com> - 3.4.12-1
- Update to 3.4.12

* Wed Feb 03 2016 Michael Cronenworth <mike@cchtml.com> - 3.4.9-1
- Update to 3.4.9

* Wed Nov 25 2015 Michael Cronenworth <mike@cchtml.com> - 3.4.7-1
- Update to 3.4.7 (CVE-2015-6251)
- Stop linking against iconv/libintl (RHBZ#1284810)
- Use Windows trust store by default instead of p11-kit
- Drop C++ library

* Mon Jul 27 2015 Michael Cronenworth <mike@cchtml.com> - 3.4.3-1
- Update to 3.4.3

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 13 2015 Michael Cronenworth <mike@cchtml.com> - 3.4.1-1
- Update to 3.4.1

* Sat Apr 11 2015 Kalev Lember <kalevlember@gmail.com> - 3.3.14-2
- Rebuild against latest mingw-gcc

* Wed Apr 01 2015 Michael Cronenworth <mike@cchtml.com> - 3.3.14-1
- Update to 3.3.14

* Fri Jan 30 2015 Michael Cronenworth <mike@cchtml.com> - 3.3.12-1
- Update to 3.3.12

* Mon Dec 15 2014 Michael Cronenworth <mike@cchtml.com> - 3.3.11-1
- Update to 3.3.11

* Mon Oct 27 2014 Michael Cronenworth <mike@cchtml.com> - 3.3.9-1
- Update to 3.3.9

* Tue Aug 26 2014 Michael Cronenworth <mike@cchtml.com> - 3.3.7-1
- Update to 3.3.7

* Sun Aug 17 2014 Michael Cronenworth <mike@cchtml.com> - 3.3.6-1
- Update to 3.3.6

* Tue Jul 01 2014 Michael Cronenworth <mike@cchtml.com> - 3.3.5-1
- Update to 3.3.5

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 26 2014 Michael Cronenworth <mike@cchtml.com> - 3.3.2-1
- Update to 3.3.2

* Thu Apr 17 2014 Michael Cronenworth <mike@cchtml.com> - 3.3.0-1
- Update to 3.3.0

* Tue Mar 04 2014 Michael Cronenworth <mike@cchtml.com> - 3.2.12.1-1
- Update to 3.2.12.1
- Fixes CVE-2014-0092 and CVE-2014-1959

* Thu Feb 13 2014 Michael Cronenworth <mike@cchtml.com> - 3.2.11-1
- Update to 3.2.11

* Sun Jan 26 2014 Michael Cronenworth <mike@cchtml.com> - 3.2.8-1
- Update to 3.2.8
- Drop iconv patch, upstream has dropped gnulib
- Drop cli patch, now upstream

* Thu Nov 07 2013 Michael Cronenworth <mike@cchtml.com> - 3.1.16-1
- Update to 3.1.16

* Tue Oct 29 2013 Michael Cronenworth <mike@cchtml.com> - 3.1.15-1
- Update to 3.1.15
- Enable ECC NIST Suite B curves

* Sun Sep 22 2013 Michael Cronenworth <mike@cchtml.com> - 3.1.13-1
- Update to 3.1.13

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jun 17 2013 Kalev Lember <kalevlember@gmail.com> - 3.1.11-5
- One more rebuild for InterlockedCompareExchange

* Sun Jun 16 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 3.1.11-4
- Rebuild to resolve InterlockedCompareExchange regression in mingw32 libraries

* Sat Jun 15 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 3.1.11-3
- Fix FTBFS due to invalid use of cdecl

* Sat Jun 15 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 3.1.11-2
- Rebuild to resolve InterlockedCompareExchange regression in mingw32 libraries

* Thu May 30 2013 Michael Cronenworth <mike@cchtml.com> - 3.1.11-1
- Update to 3.1.11

* Thu May 09 2013 Michael Cronenworth <mike@cchtml.com> - 3.1.10-1
- Update to 3.1.10
- license of the library is back to LGPLv2.1+

* Mon Mar 04 2013 Michael Cronenworth <mike@cchtml.com> - 3.1.8-1
- Update to 3.1.8
- Update No-ECC patch (#913797)

* Thu Feb 07 2013 Michael Cronenworth <mike@cchtml.com> - 3.1.7-1
- Update to 3.1.7

* Sun Jan 27 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.12.21-3
- Rebuild against mingw-gcc 4.8 (win64 uses SEH exceptions now)

* Thu Nov 22 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.12.21-2
- Rebuild against the latest mingw-readline

* Sat Nov 10 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.12.21-1
- Update to 2.12.21

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 19 2012 Michael Cronenworth <mike@cchtml.com> - 2.12.20-1
- New upstream version.

* Sun May 20 2012 Michael Cronenworth <mike@cchtml.com> - 2.12.19-1
- New upstream version.

* Sun May 13 2012 Michael Cronenworth <mike@cchtml.com> - 2.12.18-1
- New upstream version.

* Thu Mar 29 2012 Michael Cronenworth <mike@cchtml.com> - 2.12.17-1
- New upstream version.
- Use system libtasn1.

* Sun Mar 11 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.12.14-7
- Added win64 support
- Dropped .def files

* Fri Mar 09 2012 Kalev Lember <kalevlember@gmail.com> - 2.12.14-6
- Remove .la files

* Wed Mar 07 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.12.14-5
- Renamed the source package to mingw-gnutls (RHBZ #800878)
- Use mingw macros without leading underscore
- Dropped unneeded RPM tags

* Tue Feb 28 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.12.14-4
- Rebuild against the mingw-w64 toolchain
- Fix compatibility with mingw-w64

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Dec 03 2011 Michael Cronenworth <mike@cchtml.com> - 2.12.14-2
- Include new tool from p11-kit support.

* Sat Dec 03 2011 Michael Cronenworth <mike@cchtml.com> - 2.12.14-1
- Update to 2.12.14
- Allow p11-kit support.

* Wed Nov 02 2011 Michael Cronenworth <mike@cchtml.com> - 2.12.12-1
- Update to 2.12.12

* Mon Oct 24 2011 Michael Cronenworth <mike@cchtml.com> - 2.12.11-1
- Update to 2.12.11

* Wed Jul 06 2011 Kalev Lember <kalevlember@gmail.com> - 2.10.5-2
- Rebuilt against win-iconv

* Thu Apr 28 2011 Kalev Lember <kalev@smartlink.ee> - 2.10.5-1
- Update to 2.10.5

* Wed Apr 27 2011 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.6.4-7
- Dropped the proxy-libintl pieces

* Fri Apr 22 2011 Kalev Lember <kalev@smartlink.ee> - 2.6.4-6
- Rebuilt for pseudo-reloc version mismatch (#698827)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Nov  7 2010 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.6.4-4
- Rebuild in order to have soft dependency on libintl

* Fri Oct  9 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.6.4-3
- Use %%global instead of %%define
- Automatically generate debuginfo subpackage

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Mar  9 2009 Richard W.M. Jones <rjones@redhat.com> - 2.6.4-1
- New Fedora native version 2.6.4.

* Fri Feb 20 2009 Richard W.M. Jones <rjones@redhat.com> - 2.6.3-5
- Rebuild for mingw32-gcc 4.4

* Thu Feb 19 2009 Richard W.M. Jones <rjones@redhat.com> - 2.6.3-4
- +BR mingw32-gcc-c++

* Fri Feb  6 2009 Richard W.M. Jones <rjones@redhat.com> - 2.6.3-3
- Include license.

* Fri Jan 23 2009 Richard W.M. Jones <rjones@redhat.com> - 2.6.3-2
- Rebase to native Fedora version 2.6.3.
- Enable C++ library.
- Use find_lang macro.
- Don't build static library.
- Rebase MinGW patch to 2.6.3.
- +BR mingw32-dlfcn.
- +BR mingw32-readline.
- Force rebuild of libtool.

* Tue Jan 13 2009 Richard W.M. Jones <rjones@redhat.com> - 2.4.2-4
- Requires pkgconfig.

* Thu Nov 13 2008 Richard W.M. Jones <rjones@redhat.com> - 2.4.2-3
- fix chain verification issue CVE-2008-4989 (#470079)
- separate out the MinGW-specific patch from the others

* Wed Sep 24 2008 Richard W.M. Jones <rjones@redhat.com> - 2.4.2-2
- Rename mingw -> mingw32.

* Wed Sep 24 2008 Richard W.M. Jones <rjones@redhat.com> - 2.4.2-1
- New native version.

* Mon Sep 22 2008 Daniel P. Berrange <berrange@redhat.com> - 2.4.1-9
- Switch to source tar.bz2 with SRP stuff removed

* Sun Sep 21 2008 Richard W.M. Jones <rjones@redhat.com> - 2.4.1-8
- Remove duplicate manpages and info files.

* Thu Sep 11 2008 Daniel P. Berrange <berrange@redhat.com> - 2.4.1-7
- Add BR on autoconf, automake and libtool

* Wed Sep 10 2008 Richard W.M. Jones <rjones@redhat.com> - 2.4.1-6
- Need to run autoreconf after patching src/Makefile.am.
- Remove static libs.

* Fri Sep  5 2008 Richard W.M. Jones <rjones@redhat.com> - 2.4.1-5
- Add patch to build certtool.exe because of missing dep of gnulib on intl.
- BuildArch is noarch.

* Thu Sep  4 2008 Richard W.M. Jones <rjones@redhat.com> - 2.4.1-3
- Use mingw-filesystem RPM macros.
- Depends on mingw-iconv, mingw-gettext.

* Tue Sep  2 2008 Daniel P. Berrange <berrange@redhat.com> - 2.4.1-2
- List files explicitly and use custom CFLAGS

* Mon Jul  7 2008 Richard W.M. Jones <rjones@redhat.com> - 2.4.1-1
- Initial RPM release, largely based on earlier work from several sources.
