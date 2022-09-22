Summary:	SIP swiss army knife
Name:		sipsak
Version:	0.9.8.1
Release:	6%{?dist}
License:	GPLv2+
URL:		https://github.com/nils-ohlmeier/sipsak
VCS:            scm:git:https://github.com/nils-ohlmeier/sipsak.git
Source0:	https://github.com/nils-ohlmeier/sipsak/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	c-ares-devel
BuildRequires:	gcc
#BuildRequires:	gnutls-devel
BuildRequires:	libtool
BuildRequires:	make
BuildRequires:	openssl-devel

%description
sipsak is a small command line tool for developers and
administrators of Session Initiation Protocol (SIP) applications.
It can be used for some simple tests on SIP applications and
devices.

%prep
%autosetup -p1

%build
autoreconf -ivf
%configure --disable-gnutls
%make_build

%install
%make_install
rm -f %{buildroot}/%{_libdir}/*.la

%files
%doc AUTHORS ChangeLog NEWS README TODO
%license COPYING
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 0.9.8.1-4
- Rebuilt with OpenSSL 3.0.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan  9 2021 Peter Lemenkov <lemenkov@gmail.com> - 0.9.8.1-1
- Ver. 0.9.8.1

* Sun Dec 27 2020 Peter Lemenkov <lemenkov@gmail.com> - 0.9.8-1
- Ver. 0.9.8

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Feb 27 2020 Peter Lemenkov <lemenkov@gmail.com> - 0.9.7-1
- Ver. 0.9.7 (14 years since 0.9.6)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Aug 31 2016 Peter Lemenkov <lemenkov@gmail.com> - 0.9.6-22
- Fixed build failure with c11

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Aug 12 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.9.6-20
- Append -std=gnu89 to CFLAGS (Address F23FTBFS, RHBZ#1240007).
- Modernize spec.
- Add %%license.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 21 2013 Peter Lemenkov <lemenkov@gmail.com> - 0.9.6-15
- Reconfigure to allow building on AArch64

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 16 2011 Peter Lemenkov <lemenkov@gmail.com> - 0.9.6-11
- Proper fix for rhbz #753372 now

* Tue Nov 15 2011 Peter Lemenkov <lemenkov@gmail.com> - 0.9.6-10
- Fix rhbz #753372

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 0.9.6-8
- rebuilt with new openssl

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 17 2009 Tomas Mraz <tmraz@redhat.com> - 0.9.6-5
- rebuild with new openssl

* Thu Sep 04 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.9.6-4
- fix license tag

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.9.6-3
- Autorebuild for GCC 4.3

* Fri Dec 07 2007 Release Engineering <rel-eng@fedoraproject.org> - 0.9.6-2
- Rebuild for deps

* Sun Sep 17 2006 Peter Lemenkov <lemenkov@gmail.com> - 0.9.6-1
- Initial build for FE

* Wed Feb 08 2006 Oden Eriksson <oeriksson@mandriva.com> - 0.9.6-1mdk
- 0.9.6
- disable gnutls support
- fix deps

* Sun Apr 24 2005 Oden Eriksson <oeriksson@mandriva.com> - 0.8.12-1mdk
- initial Mandriva package
