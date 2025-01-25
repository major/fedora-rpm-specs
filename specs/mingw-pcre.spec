%?mingw_package_header

%global name1 pcre
# Is this a stable/testing release:
#%%global rcversion RC1

Name:		mingw-%{name1}
Version:	8.45
%global myversion %{version}%{?rcversion:-%rcversion}
Release:	8%{?dist}
Summary:	MinGW Windows pcre library

License:	BSD-3-Clause
URL:		http://www.pcre.org/
Source0:        https://ftp.pcre.org/pub/%{name1}/%{?rcversion:Testing/}%{name1}-%{myversion}.tar.bz2
Source1:        https://ftp.pcre.org/pub/%{name1}/%{?rcversion:Testing/}%{name1}-%{myversion}.tar.bz2.sig
Source2:        https://ftp.pcre.org/pub/pcre/Public-Key

# Refused by upstream, bug #675477
Patch1:         pcre-8.32-refused_spelling_terminated.patch
# Fix recursion stack estimator, upstream bug #2173, refused by upstream
Patch2:         pcre-8.41-fix_stack_estimator.patch
# Link applications to PCRE-specific symbols when using POSIX API, bug #1667614,
# upstream bug 1830, partially borrowed from PCRE2, proposed to upstream,
# This amends ABI, application built with this patch cannot run with
# previous libpcreposix builds.
Patch3:         pcre-8.42-Declare-POSIX-regex-function-names-as-macros-to-PCRE.patch
# Fix reading an uninitialized memory when populating a name table,
# upstream bug #2661, proposed to the upstream
Patch4:         pcre-8.44-Inicialize-name-table-memory-region.patch
# Implement CET, bug #1909554, proposed to the upstream
# <https://lists.exim.org/lurker/message/20201220.222016.d8cd6d61.en.html>
Patch5:         pcre-8.44-JIT-compiler-update-for-Intel-CET.patch
Patch6:         pcre-8.44-Pass-mshstk-to-the-compiler-when-Intel-CET-is-enable.patch

BuildArch:	noarch

BuildRequires:  make
BuildRequires:  git
BuildRequires:	redhat-rpm-config
BuildRequires:  gnupg2
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

BuildRequires:	mingw32-filesystem >= 95
BuildRequires:	mingw32-gcc
BuildRequires:	mingw32-gcc-c++
BuildRequires:	mingw32-binutils

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-binutils


%description
Cross compiled Perl-compatible regular expression library for use with mingw32.

PCRE has its own native API, but a set of "wrapper" functions that are based on
the POSIX API are also supplied in the library libpcreposix. Note that this
just provides a POSIX calling interface to PCRE: the regular expressions
themselves still follow Perl syntax and semantics. The header file
for the POSIX-style functions is called pcreposix.h.


# Win32
%package -n mingw32-pcre
Summary:	MinGW Windows pcre library
Requires:	pkgconfig

%description -n mingw32-pcre
Cross compiled Perl-compatible regular expression library for use with mingw32.

PCRE has its own native API, but a set of "wrapper" functions that are based on
the POSIX API are also supplied in the library libpcreposix. Note that this
just provides a POSIX calling interface to PCRE: the regular expressions
themselves still follow Perl syntax and semantics. The header file
for the POSIX-style functions is called pcreposix.h.

%package -n mingw32-pcre-static
Summary:       Static version of the mingw32-pcre library
Requires:      mingw32-pcre = %{version}-%{release}
BuildArch:     noarch

%description -n mingw32-pcre-static
Static version of the mingw32-pcre library.

# Win64
%package -n mingw64-pcre
Summary:        MinGW Windows pcre library
Requires:       pkgconfig

%description -n mingw64-pcre
Cross compiled Perl-compatible regular expression library for use with mingw64.

PCRE has its own native API, but a set of "wrapper" functions that are based on
the POSIX API are also supplied in the library libpcreposix. Note that this
just provides a POSIX calling interface to PCRE: the regular expressions
themselves still follow Perl syntax and semantics. The header file
for the POSIX-style functions is called pcreposix.h.

%package -n mingw64-pcre-static
Summary:       Static version of the mingw64-pcre library
Requires:      mingw64-pcre = %{version}-%{release}
BuildArch:     noarch

%description -n mingw64-pcre-static
Static version of the mingw64-pcre library.


%?mingw_debug_package


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -S git_am -n pcre-%{version}
autoreconf -vif


%build
%mingw_configure --enable-utf8 --enable-unicode-properties --enable-static --enable-pcre8 --enable-pcre16 --enable-pcre32
%mingw_make %{?_smp_mflags}


%install
%mingw_make DESTDIR=$RPM_BUILD_ROOT install

rm -rf $RPM_BUILD_ROOT%{mingw32_datadir}/doc/*
rm -rf $RPM_BUILD_ROOT%{mingw64_datadir}/doc/*
rm -rf $RPM_BUILD_ROOT%{mingw32_datadir}/man/*
rm -rf $RPM_BUILD_ROOT%{mingw64_datadir}/man/*

# Drop all .la files
find $RPM_BUILD_ROOT -name "*.la" -delete


# Win32
%files -n mingw32-pcre
%doc AUTHORS COPYING LICENCE NEWS README ChangeLog
%{mingw32_bindir}/pcre-config
%{mingw32_bindir}/pcregrep.exe
%{mingw32_bindir}/pcretest.exe
%{mingw32_bindir}/libpcre-1.dll
%{mingw32_bindir}/libpcre16-0.dll
%{mingw32_bindir}/libpcre32-0.dll
%{mingw32_bindir}/libpcrecpp-0.dll
%{mingw32_bindir}/libpcreposix-0.dll
%{mingw32_libdir}/libpcre.dll.a
%{mingw32_libdir}/libpcre16.dll.a
%{mingw32_libdir}/libpcre32.dll.a
%{mingw32_libdir}/libpcrecpp.dll.a
%{mingw32_libdir}/libpcreposix.dll.a
%{mingw32_libdir}/pkgconfig/libpcre.pc
%{mingw32_libdir}/pkgconfig/libpcre16.pc
%{mingw32_libdir}/pkgconfig/libpcre32.pc
%{mingw32_libdir}/pkgconfig/libpcrecpp.pc
%{mingw32_libdir}/pkgconfig/libpcreposix.pc
%{mingw32_includedir}/pcre.h
%{mingw32_includedir}/pcre_scanner.h
%{mingw32_includedir}/pcre_stringpiece.h
%{mingw32_includedir}/pcrecpp.h
%{mingw32_includedir}/pcrecpparg.h
%{mingw32_includedir}/pcreposix.h

%files -n mingw32-pcre-static
%{mingw32_libdir}/libpcre.a
%{mingw32_libdir}/libpcre16.a
%{mingw32_libdir}/libpcre32.a
%{mingw32_libdir}/libpcrecpp.a
%{mingw32_libdir}/libpcreposix.a

# Win64
%files -n mingw64-pcre
%doc AUTHORS COPYING LICENCE NEWS README ChangeLog
%{mingw64_bindir}/pcre-config
%{mingw64_bindir}/pcregrep.exe
%{mingw64_bindir}/pcretest.exe
%{mingw64_bindir}/libpcre-1.dll
%{mingw64_bindir}/libpcre16-0.dll
%{mingw64_bindir}/libpcre32-0.dll
%{mingw64_bindir}/libpcrecpp-0.dll
%{mingw64_bindir}/libpcreposix-0.dll
%{mingw64_libdir}/libpcre.dll.a
%{mingw64_libdir}/libpcre16.dll.a
%{mingw64_libdir}/libpcre32.dll.a
%{mingw64_libdir}/libpcrecpp.dll.a
%{mingw64_libdir}/libpcreposix.dll.a
%{mingw64_libdir}/pkgconfig/libpcre.pc
%{mingw64_libdir}/pkgconfig/libpcre16.pc
%{mingw64_libdir}/pkgconfig/libpcre32.pc
%{mingw64_libdir}/pkgconfig/libpcrecpp.pc
%{mingw64_libdir}/pkgconfig/libpcreposix.pc
%{mingw64_includedir}/pcre.h
%{mingw64_includedir}/pcre_scanner.h
%{mingw64_includedir}/pcre_stringpiece.h
%{mingw64_includedir}/pcrecpp.h
%{mingw64_includedir}/pcrecpparg.h
%{mingw64_includedir}/pcreposix.h

%files -n mingw64-pcre-static
%{mingw64_libdir}/libpcre.a
%{mingw64_libdir}/libpcre16.a
%{mingw64_libdir}/libpcre32.a
%{mingw64_libdir}/libpcrecpp.a
%{mingw64_libdir}/libpcreposix.a


%changelog
* Thu Jan 23 2025 Thomas Sailer <fedora@tsailer.ch> - 8.45-8
- Fix build

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 8.45-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.45-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.45-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.45-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.45-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.45-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 19 2022 Thomas Sailer <fedora@tsailer.ch> - 8.45-1
- Update to 8.45 to match native version

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.43-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 8.43-8
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.43-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.43-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.43-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.43-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.43-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 8.43-2
- Rebuild (Changes/Mingw32GccDwarf2)

* Wed Aug 14 2019 Marc-André Lureau <marcandre.lureau@redhat.com> - 8.43-1
- New upstream release 8.43

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.38-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.38-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.38-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.38-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.38-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.38-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Feb  6 2016 Erik van Pienbroek <epienbro@fedoraproject.org> - 8.38-1
- Update to 8.38
- Fixes various CVE's:
  RHBZ #1236660, #1249905, #1250947, #1256453, #1256454, #1287616,
  RHBZ #1287619, #1287626, #1287628, #1287631, #1287634, #1287640,
  RHBZ #1287642, #1287648, #1287650, #1287656, #1287658, #1287661,
  RHBZ #1287663, #1287668, #1287670, #1287673, #1287675, #1287692,
  RHBZ #1287694, #1287698, #1287700, #1287704, #1287706, #1287720,
  RHBZ #1287722

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 8.36-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.36-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Dec 25 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 8.36-1
- Update to 8.36
- Add upstream patches from main pcre package

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.34-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Jan 25 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 8.34-1
- Update to 8.34

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.33-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 11 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 8.33-2
- Added -static subpackages

* Wed Jul  3 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 8.33-1
- Update to 8.33
- Added the configure arguments --enable-pcre8 --enable-pcre16 --enable-pcre32
  (the pcre16 one is needed by mingw-qt5-qtbase)
- Use a more verbose filelist

* Sun Mar 24 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 8.32-1
- Update to 8.32

* Sun Jan 27 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 8.31-2
- Rebuild against mingw-gcc 4.8 (win64 uses SEH exceptions now)

* Wed Nov 21 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 8.31-1
- Update to 8.31
- Dropped patch as it doesn't have any effect on the mingw target

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Apr 14 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 8.30-9
- Update to 8.30
- Added win64 support

* Fri Mar 09 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 8.10-8
- Dropped .la files

* Wed Mar 07 2012 Kalev Lember <kalevlember@gmail.com> - 8.10-7
- Renamed the source package to mingw-pcre (#801011)
- Modernize the spec file
- Use mingw macros without leading underscore

* Mon Feb 27 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 8.10-6
- Rebuild against the mingw-w64 toolchain

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Apr 22 2011 Kalev Lember <kalev@smartlink.ee> - 8.10-4
- Rebuilt for pseudo-reloc version mismatch (#698827)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Sep 20 2010 Adam Stokes <astokes@redhat.com> - 8.10-2
- Restore changes from the native package to pass package review process

* Wed Jul 21 2010 Ryan O'Hara <rohara@redhat.com> - 8.10-1
- Initial spec file.
