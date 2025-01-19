Name:		mcrypt
Version:	2.6.8
Release:	36%{?dist}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:	GPL-3.0-or-later
Summary:	Replacement for crypt()
URL:		http://mcrypt.sourceforge.net/
Source0:	http://download.sourceforge.net/mcrypt/mcrypt-%{version}.tar.gz
# From upstream, a combination of:
# http://sourceforge.net/tracker/index.php?func=detail&aid=1191020&group_id=87941&atid=584895
# http://sourceforge.net/tracker/index.php?func=detail&aid=1872812&group_id=87941&atid=584895
Patch0:		mcrypt-rfc2440-bugfixes.patch
# From upstream:
# http://sourceforge.net/tracker/index.php?func=detail&aid=1872809&group_id=87941&atid=584895
Patch1:		mcrypt-2.6.7-format_strings.patch
# Upstream:
# http://sourceforge.net/tracker/index.php?func=detail&aid=1829488&group_id=87941&atid=584895
Patch2:		mcrypt-2.6.7-gaafix.patch
# Upstream:
# http://sourceforge.net/tracker/index.php?func=detail&aid=2075758&group_id=87941&atid=584895
Patch3:		mcrypt-2.6.7-native-by-default.patch
# Upstream: 
# https://sourceforge.net/tracker/index.php?func=detail&aid=3559099&group_id=87941&atid=584893
Patch4:		mcrypt-2.6.8-manpage-typofixes.patch
# Fix for CVE-2012-4409
# https://bugzilla.redhat.com/show_bug.cgi?id=855029
Patch5:		mcrypt-CVE-2012-4409.patch
# No gaa in Fedora
Patch6:		mcrypt-2.6.8-no-gaa.patch
# Fix for CVE-2012-4527 (workaround, really)
Patch7:		mcrypt-CVE-2012-4527-80-width-patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:	libmcrypt-devel, mhash-devel, gettext, zlib-devel

%description
MCrypt is a replacement for the old crypt() package and crypt(1) command, 
with extensions. It allows developers to use a wide range of encryption 
functions, without making drastic changes to their code. It allows users 
to encrypt files or data streams without having to be cryptographers. 

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1 -b .format_strings
%patch -P2 -p1 -b .gaafix
%patch -P3 -p1 -b .native_by_default
%patch -P4 -p1 -b .typos
%patch -P5 -p1 -b .CVE-2012-4409
%patch -P6 -p1 -b .no-gaa
%patch -P7 -p1 -b .CVE-2012-4527

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING NEWS README THANKS TODO
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.8-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 2.6.8-35
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.8-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.8-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.8-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.8-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.8-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.8-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.8-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.8-27
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.8-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.8-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.8-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.8-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.8-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.8-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.8-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.8-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.8-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.8-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.8-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.8-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Oct 30 2012 Tom Callaway <spot@fedoraproject.org> - 2.6.8-10
- apply workaround patch for CVE-2012-4527
  Thanks to Attila Bogar and Nobuhiro Iwamatsu

* Fri Sep  7 2012 Tom Callaway <spot@fedoraproject.org> - 2.6.8-9
- don't try to use gaa

* Fri Sep  7 2012 Tom Callaway <spot@fedoraproject.org> - 2.6.8-8
- apply fix for CVE-2012-4409 (thanks to Raphael Geissert)

* Fri Aug 17 2012 Tom Callaway <spot@fedoraproject.org> - 2.6.8-7
- fix typos in manpage

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Nov 24 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.6.8-1
- update to 2.6.8

* Mon Aug 25 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.6.7-3
- use native mcrypt format by default (not openpgp) (bz 433582)
- fix gaa
- fix format strings

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.6.7-2
- Autorebuild for GCC 4.3

* Mon Dec 17 2007 Tom "spot" Callaway <tcallawa@redhat.com> 2.6.7-1
- 2.6.7
- fix bugs in rfc2440.c (resolves bugzilla 418481)

* Fri Aug 24 2007 Tom "spot" Callaway <tcallawa@redhat.com> 2.6.6-2
- rebuild for ppc32, license fix

* Thu Jul 19 2007 Tom "spot" Callaway <tcallawa@redhat.com> 2.6.6-1
- bump to 2.6.6
- destdir patch obsoleted upstream

* Tue Sep 12 2006 Tom "spot" Callaway <tcallawa@redhat.com> 2.6.4-3
- bump for FC-6

* Tue Feb 28 2006 Tom "spot" Callaway <tcallawa@redhat.com> 2.6.4-2
- bump for FC-5

* Thu Sep 22 2005 Tom "spot" Callaway <tcallawa@redhat.com> 2.6.4-1
- initial package for Fedora Extras
