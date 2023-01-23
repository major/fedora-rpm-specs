%{!?tcl_version: %global tcl_version %((echo '8.5'; echo 'puts $tcl_version' | tclsh 2>/dev/null) | tail -1)}
%{!?tcl_sitearch: %global tcl_sitearch %{_libdir}/tcl%{tcl_version}}

Name:           tcltls
Version:        1.7.22
Release:        9%{?dist}
Summary:        OpenSSL extension for Tcl

License:        BSD
URL:            https://core.tcl.tk/tcltls/home
Source0:        https://core.tcl.tk/tcltls/uv/%{name}-%{version}.tar.gz

Patch0:         tcltls-1.7.21-cipher-tests.patch
Patch1:         tcltls-1.7.21-hostname-tests.patch
Patch2:         tcltls-1.7.22-cert-tests.patch
Patch3:         tcltls-1.7.22-fall-through.patch
Patch4:         tcltls-1.7.22-openssl3.patch

BuildRequires:  make
%if 0%{?fedora} || 0%{?rhel} >= 8
BuildRequires:  openssl-devel
%else
BuildRequires:  openssl11-devel
%endif
BuildRequires:  tcl-devel
BuildRequires:  gcc

Requires:       tcl(abi) = %{tcl_version}

%description
A TLS OpenSSL extension for Tcl

%package devel
Summary:        Header files for the OpenSSL extension for Tcl
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The TLS OpenSSL extension to Tcl

This package contains the development files for tls.

%prep
%autosetup -p1

# Disable strip via objcopy(1) to achieve -debuginfo
sed -e 's/-@\(WEAKEN\|REMOVE\)SYMS@/:/' -i Makefile.in

# Build against OpenSSL 1.1 on RHEL 7 (for TLSv1.3 support)
%if 0%{?rhel} == 7
sed -e 's|-L$openssldir/lib|-L%{_libdir}/openssl11|g' \
    -e 's|-I$openssldir/include|-I%{_includedir}/openssl11|g' \
    -i configure
%endif

%build
%configure --disable-rpath --with-ssl-dir=%{_prefix}
%make_build

%check
make test

%install
%make_install libdir=%{tcl_sitearch}

%{__install} -D -p -m 0644 tls.h %{buildroot}%{_includedir}/tls.h

%files
%license license.terms
%doc README.txt ChangeLog
%{tcl_sitearch}/%{name}%{version}

%files devel
%{_includedir}/tls.h

%changelog
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.22-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.22-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat May 28 2022 Robert Scheck <robert@fedoraproject.org> - 1.7.21-7
- Build against OpenSSL 1.1 on RHEL 7 (for TLSv1.3 support)

* Sat May 28 2022 Robert Scheck <robert@fedoraproject.org> - 1.7.21-6
- Disabled strip via objcopy to achieve proper -debuginfo package
- Added patch to fix compiler warnings about implicit fall-through
- Added patch to fix "ee key too small" error messages during tests
- Added patch for OpenSSL 3.0 support (#2088363)

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.22-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.7.22-4
- Rebuilt with OpenSSL 3.0.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 07 2021 Jason Taylor <jtfas90@gmail.com> - 1.7.22-1
- Upgrade to latest release (#1887951)
- Disabled debug output (#1912469)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 24 2020 Robert Scheck <robert@fedoraproject.org> - 1.7.21-1
- Upgrade to 1.7.21 and spec file modernization (#1753651)

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 30 2019 Jason Taylor <jtfas90@gmail.com> - 1.7.18-1
- update to latest upstream

* Thu Apr 11 2019 Jason Taylor <jtfas90@gmail.com> - 1.7.17-1
- update to latest upstream

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 21 2018 Jason Taylor <jtfas90@gmail.com> - 1.7.16-1
- update to latest upstream

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Dec 02 2017 Jason Taylor <jtfas90@gmail.com> - 1.7.14-1
- update to latest upstream

* Fri Sep 01 2017 Sander Hoentjen <sander@hoentjen.eu> - 1.7.13-1
- update to latest upstream (resolves #1487627)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Jason Taylor <jtfas90@gmail.com> - 1.7.12-1
- update to latest upstream (resolves #1447157)

* Mon Feb 20 2017 Jason Taylor <jtfas90@gmail.com> - 1.7.11-1
- update to latest upstream (resolves #1424078)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 06 2016 Sander Hoentjen <sander@hoentjen.eu> - 1.6.7-4
- Don't use macro's in changelog
- fix bogus dates in changelog

* Tue Jan 05 2016 Jason Taylor <jtfas90@gmail.com> - 1.6.7-3
- Replaced define with global in spec file

* Sat Nov 21 2015 Jason Taylor <jtfas90@gmail.com> - 1.6.7-2
- Updated spec to account for epel tcl versions

* Thu Nov 19 2015 Sander Hoentjen <sander@hoentjen.eu> - 1.6.7-1
- Update to latest upstream

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 1.6-13
- Changed requires to require tcl-8.6

* Wed May 21 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 1.6-12
- Rebuilt for https://fedoraproject.org/wiki/Changes/f21tcl86

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 1.6-6
- rebuilt with new openssl

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 18 2009 Tomas Mraz <tmraz@redhat.com> - 1.6-3
- rebuild with new openssl

* Thu Dec 04 2008 Sander Hoentjen <sander@hoentjen.eu> - 1.6-2
- Add requires on tcl

* Thu Oct 09 2008 Sander Hoentjen <sander@hoentjen.eu> - 1.6-1
- Update to latest release

* Tue Feb 12 2008 Sander Hoentjen <sander@hoentjen.eu> - 1.5.0-16
- Rebuilt for gcc-4.3

* Tue Jan 08 2008 Sander Hoentjen <sander@hoentjen.eu> - 1.5.0-14
- disable make test for the moment

* Sat Jan 05 2008 Sander Hoentjen <sander@hoentjen.eu> - 1.5.0-13
- update for tcl 8.5

* Wed Dec 05 2007 Sander Hoentjen <sander@hoentjen.eu> - 1.5.0-12
- rebuild for openssl soname change

* Tue Aug 29 2006 Sander Hoentjen <tjikkun@xs4all.nl> - 1.5.0-11
- FE6 Mass Rebuild

* Fri May 26 2006 Sander Hoentjen <tjikkun@xs4all.nl> - 1.5.0-10
- reverted name change to tcltls

* Fri May 26 2006 Sander Hoentjen <tjikkun@xs4all.nl> - 1.5.0-9
- in reply to comment #39 from bug #186327 (review by wart)
- changed name from tcltls to tcl-tls
- changed lib dir from tls1.50 to tls1.5.0
- changed summary
- removed some commented lines
- use macro in configure instead of hardcoded /usr
- changed group
- removed inhereted tags in devel package

* Tue Apr 25 2006 Sander Hoentjen <tjikkun@xs4all.nl> - 1.5.0-8
- Source0 dl.sf.net instead of download.sf.net

* Tue Apr 25 2006 Sander Hoentjen <tjikkun@xs4all.nl> - 1.5.0-7
- source tarball has same md5sum as upstream now

* Tue Apr 25 2006 Sander Hoentjen <tjikkun@xs4all.nl> - 1.5.0-6
- added make test
- no more enable-symbols

* Tue Apr 25 2006 Sander Hoentjen <tjikkun@xs4all.nl> - 1.5.0-5
patches from Wart (wart@kobold.org):
- Patch1: tcltls-configurein.pkgname.patch
- Patch2: tcltls-1.5-rpmoptflags.patch
- Patch3: tcltls-1.5-64bit.patch
Moved libtls out of /usr/lib into subdir

* Tue Mar 28 2006 Sander Hoentjen <tjikkun@xs4all.nl> - 1.5.0-4

* Tue Mar 28 2006 Sander Hoentjen <tjikkun@xs4all.nl> - 1.5.0-3

* Thu Mar 23 2006 Sander Hoentjen <tjikkun@xs4all.nl> - 1.5.0-2
- invalid-soname fixed
- docs added (including license)
- devel package has defattr macro now

* Tue Mar 21 2006 Sander Hoentjen <tjikkun@xs4all.nl> - 1.5.0-1
- created
