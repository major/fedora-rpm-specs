Summary: A library that hides the complexity of using the SIP protocol
Name: libeXosip2
Version: 5.3.0
Release: 2%{?dist}
License: GPL-2.0-or-later

URL: https://savannah.nongnu.org/projects/eXosip

Source0: https://download.savannah.nongnu.org/releases/exosip/libexosip2-%{version}.tar.gz

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: c-ares-devel
BuildRequires: doxygen
BuildRequires: gcc
BuildRequires: libosip2-devel >= 5.3.1
BuildRequires: libtool
BuildRequires: make
BuildRequires: openssl-devel
BuildRequires: ortp-devel >= 5.2.45

%description
A library that hides the complexity of using the SIP protocol for
mutlimedia session establishement. This protocol is mainly to be used
by VoIP telephony applications (endpoints or conference server) but
might be also useful for any application that wish to establish
sessions like multiplayer games.

%package devel
Summary: Development files for libeXosip2
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: libosip2-devel

%description devel
Development files for libeXosip2.

%prep
# Upstream renamed release archive, so need to name for succesful building.
%autosetup -p1 -n libexosip2-%{version}

%build
autoreconf -fi -I scripts
%configure --disable-static
%make_build
# Generate html docs and manpage.
make doxygen

%install
%make_install

# Remove .la files on EL.
%if 0%{?rhel}
rm %{buildroot}%{_libdir}/*.la
%endif

# Move manpage to correct install location.
mkdir -p %{buildroot}%{_mandir}/man3
cp help/doxygen/doc/man/man3/*.3* %{buildroot}%{_mandir}/man3

# Move html docs to correct install location.
mkdir -p %{buildroot}%{_docdir}/libeXosip2-devel/html
cp help/doxygen/doc/html/* %{buildroot}%{_docdir}/libeXosip2-devel/html

%files
%license COPYING
%{_bindir}/sip_reg
%{_bindir}/sip_monitor
%{_bindir}/sip_storm
%{_libdir}/libeXosip2.so.15*

%files devel
%doc AUTHORS ChangeLog NEWS README
%doc %{_docdir}/libeXosip2-devel/html/
%{_includedir}/eXosip2
%{_libdir}/libeXosip2.so
%{_mandir}/man3/*.3*

%changelog
* Thu May 18 2023 Phil Wyett <philip.wyett@kathenas.org> - 5.3.0-2
- Remove .la files on EL.

* Sat Apr 01 2023 Phil Wyett <philip.wyett@kathenas.org> - 5.3.0-1
- New upstream version 5.3.0.
- Use SPDX license identifier.
- Rework of spec file.

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Apr 22 2022 Petr Pisar <ppisar@redhat.com> - 3.6.0-27
- Regenerate autotools scripts (bug #1987645)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 3.6.0-25
- Rebuilt with OpenSSL 3.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.6.0-17
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 26 2017 Robert Scheck <robert@fedoraproject.org> - 3.6.0-15
- Added patch to build with OpenSSL >= 1.1.0 (#1423847)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Mar 23 2013 Alexey Kurov <nucleo@fedoraproject.org> - 3.6.0-6
- add aarch64 patch (#925719)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 26 2011 Alexey Kurov <nucleo@fedoraproject.org> - 3.6.0-2
- BR: c-ares-devel

* Mon Dec 26 2011 Alexey Kurov <nucleo@fedoraproject.org> - 3.6.0-1
- libeXosip2-3.6.0

* Fri Sep  2 2011 Alexey Kurov <nucleo@fedoraproject.org> - 3.5.0-1
- libeXosip2-3.5.0
- add BR: openssl-devel
- drop gcc43 patch

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 14 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 3.1.0-1
- Update to 3.1.0

* Tue Feb  5 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 3.0.3-3
- Apply patch from Adam Tkac that fixes compilation with GCC 4.3.

* Mon Feb  4 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 3.0.3-2
- Update to new patchlevel release.

* Tue Aug 28 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 3.0.3-1
- Update to 3.0.3

* Mon Aug 28 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 2.2.3-3
- Bump release and rebuild.

* Mon Jun  5 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 2.2.3-2
- Add BR for doxygen.

* Mon May 29 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 2.2.3-1
- Update to 2.2.3

* Mon Feb 20 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 2.2.2-4
- Bump release for rebuild.

* Mon Feb 13 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 2.2.2-3
- Bump release and rebuild for gcc 4.1 and glibc.

* Wed Jan  4 2006 Jeffrey C. Ollie <jeff@max1.ocjtech.us> - 2.2.2
- Update to 2.2.2.
- Bump release because forgot to upload new source.

* Sat Oct 29 2005 Jeffrey C. Ollie <jcollie@lt16585.campus.dmacc.edu> - 1.9.1-0.5.pre17
- Update to next prerelease.

* Mon Oct 24 2005 Jeffrey C. Ollie <jcollie@lt16585.campus.dmacc.edu> - 1.9.1-0.4.pre16
- Remove INSTALL from %%doc - not needed in an RPM package

* Sun Oct 23 2005 Jeffrey C. Ollie <jcollie@lt16585.campus.dmacc.edu> - 1.9.1-0.3.pre16
- Added -n to BuildRoot
- BR libosip2-devel for -devel subpackage.

* Sun Oct 16 2005 Jeffrey C. Ollie <jcollie@lt16585.campus.dmacc.edu> - 1.9.1-0.2.pre16
- Changed BuildRoot to match packaging guidelines.
- Remove extraneous %%dir in -devel %%files
- Replace %%makeinstall with proper invocation.

* Fri Oct 14 2005 Jeffrey C. Ollie <jcollie@lt16585.campus.dmacc.edu> - 1.9.1-0.1.pre16
- Initial build.

