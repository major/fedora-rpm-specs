Summary:	C++ Implementation of W3C security standards for XML
Name:		xml-security-c
Version:	2.0.4
Release:	7%{?dist}
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:	Apache-2.0
URL:		http://santuario.apache.org/cindex.html
Source0:	https://www.apache.org/dist/santuario/c-library/%{name}-%{version}.tar.gz
BuildRequires: make
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gcc-c++
BuildRequires:	libtool
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
BuildRequires:	xalan-c-devel
BuildRequires:	xerces-c-devel

%description
The xml-security-c library is a C++ implementation of the XML Digital Signature
specification. The library makes use of the Apache XML project's Xerces-C XML
Parser and Xalan-C XSLT processor. The latter is used for processing XPath and
XSLT transforms.

%package devel
Summary:	Development files for xml-security-c
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	libstdc++-devel
Requires:	openssl-devel
Requires:	xalan-c-devel
Requires:	xerces-c-devel

%description devel
This package provides development files for xml-security-c, a C++ library for
XML Digital Signatures.

%prep
%autosetup -p1

%build
autoreconf -fiv
%configure \
	--disable-debug \
	--disable-static \
	--without-nss \
	--with-openssl \
	--with-xalan \
	%{nil}
%make_build

%install
%make_install

%check
./xsec/xsec-xtest

%files
%{_libdir}/libxml-security-c.so.20{,.*}

%files devel
%license LICENSE.txt
%doc CHANGELOG.txt NOTICE.txt
%{_includedir}/xsec
%{_libdir}/libxml-security-c.so
%{_libdir}/pkgconfig/xml-security-c.pc
%exclude %{_bindir}/*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Oct 18 2024 Pete Walter <pwalter@fedoraproject.org> - 2.0.4-6
- Rebuild for xerces-c 3.3

* Wed Jul  24 2024 Miroslav Suchý <msuchy@redhat.com> - 2.0.4-5
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 26 2023 Yaakov Selkowitz <yselkowi@redhat.com> - 2.0.4-1
- Update to 2.0.4

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 2.0.2-10
- Rebuilt with OpenSSL 3.0.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec  7 18:18:40 EST 2020 Benjamin A. Beasley <code@musicinmybrain.net> - 2.0.2-7
- Work around removed XALAN_USING_XALAN compatibility macro in xalan-c 1.12

* Mon Dec  7 19:42:40 CET 2020 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.0.2-6
- Rebuilt for xalan-c 1.12.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Tomasz Kłoczko <kloczek@fedoraproject.org> - 2.0.2-1
- use %%exclude does not cause include those files into package %%files (revert last commit)
- format text to 80 col
- use https:// in Source0 url
- improved BuildRequires

* Fri Nov 16 2018 Pete Walter <pwalter@fedoraproject.org> - 2.0.2-1
- Update to 2.0.2
- Remove explicit attr modes

* Wed Jul 18 2018 Tomasz Kłoczko <kloczek@fedoraproject.org> - 1.7.3-5
- added /usr/bin/c++ to BuildRequires

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Tomasz Kłoczko <kloczek@fedoraproject.org> - 1.7.3-3
- remove ldconfig scriptlets
- more cleanups

* Wed Aug 30 2017 Tomasz Kłoczko <kloczek@fedoraproject.org> - 1.7.3-2
- added patch which allows build xml-security-c against openssl 1.1
- added ac_fixes patch: do not use sed to remove hardcoded compile
  options. Use patch because you will never know is such correction
  still needed (added autoconf, automake and libtool to BuildRequires)
- added libstdc++-devel to BuildReqires and to devel Requires
- add explicit all %%configure options to prevent build by mistake package
  against nss and force use openssl
- added --disable-debug to %%configure options
- added use %%autosetup in %%prep
- do not waste IOs on remove not packaged files and add them %%files
  with %%exclude
- indent and clean spec (move patch comments to the patch)

* Tue Aug 29 2017 Kalev Lember <klember@redhat.com> - 1.7.3-1
- Update to 1.7.3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Feb 02 2016 Jonathan Wakely <jwakely@redhat.com> - 1.6.1-11
- Patched for C++11 compatibility

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.6.1-9
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Oct 11 2013 Antti Andreimann <Antti.Andreimann@mail.ee> - 1.6.1-6
- Rebuild for xalan-c 110 to 111 .so bump

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 7 2011 Steve Traylen <steve.traylen@cern.ch> 1.6.1-1
- New upstream release, Correct source URL.

* Wed Mar 16 2011 Antti Andreimann <Antti.Andreimann@mail.ee> 1.6.0-1
- New upstream release

* Thu Mar 10 2011 Kalev Lember <kalev@smartlink.ee> - 1.5.1-5
- Rebuilt with xerces-c 3.1

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Feb 06 2010 steve.traylen@cern.ch - 1.5.1-3
- Rebuild for xerces 2 to 3 .so bump

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 1.5.1-2
- rebuilt with new openssl

* Tue Jul 28 2009 Antti Andreimann <Antti.Andreimann@mail.ee> 1.5.1-1
- New upstream relase (#513078)
- Fixes CVE-2009-0217 (#511915)

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 06 2009 Antti Andreimann <Antti.Andreimann@mail.ee> - 1.5.0-1
- New upstream release

* Tue Apr 28 2009 Antti Andreimann <Antti.Andreimann@mail.ee> - 1.4.0-2
- Execute sed magic against configure instead of configure.ac to
  avoid calling autotools
- Removed build dependency on autotools.
- Do not ship test binaries (not needed for end-users)
- Added proper dependencies for devel sub-package
- Added CPPROG="cp -p" to preserve header file timestamps.

* Mon Mar 30 2009 Antti Andreimann <Antti.Andreimann@mail.ee> - 1.4.0-1
- Initial RPM release.
