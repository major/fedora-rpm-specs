Name:           telepathy-salut
Version:        0.99.11
Release:        2%{?dist}
Summary:        Link-local XMPP telepathy connection manager

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://telepathy.freedesktop.org/wiki/FrontPage
Source0:        http://telepathy.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.gz
# python3
Patch0:         telepathy-salut-0.8.1-python3.patch
# Fix compilation with gcc14 -Werror=incompatible-pointer-types
Patch1:         telepathy-salut-0.8.1-gcc14-fix-incompatible-pointer-types.patch

BuildRequires: make
BuildRequires:  dbus-devel >= 1.1.0
BuildRequires:	dbus-glib-devel >= 0.61
BuildRequires:	python3-dbus
BuildRequires:	avahi-gobject-devel
BuildRequires:	libxml2-devel
# Use gnutls as wocky backend
# wocky defaults to gnutls : see
# https://gitlab.freedesktop.org/telepathy/wocky/-/commit/71d67e44ce3072ebeae477f1b493bbb80f6f7958
# also, due to https://fedoraproject.org/wiki/Changes/OpensslDeprecateEngine
# code depending on ENGINE API (wocky-openssl.c) no longer compiles
BuildRequires:	gnutls-devel
BuildRequires:	cyrus-sasl-devel
BuildRequires:	libxslt
BuildRequires:	libasyncns-devel >= 0.3
BuildRequires:	telepathy-glib-devel >= 0.17.1
BuildRequires:  libuuid-devel
BuildRequires:	libsoup-devel
BuildRequires:	sqlite-devel
BuildRequires:  gtk-doc
# for tests
BuildRequires:  dbus-daemon

Requires:	telepathy-filesystem

%description
%{name} is a Telepathy connection manager for link-local XMPP.
Normally, XMPP does not support direct client-to-client interactions,
since it requires authentication with a server.  This package makes
it is possible to establish an XMPP-like communications system on a
local network using zero-configuration networking.


%prep
%setup -q
%patch -P0 -p1 -b .py3
%patch -P1 -p1 -b .pointer_type

%build
export PYTHON=python3
%configure --enable-ssl --enable-olpc --disable-avahi-tests --enable-static=no
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

## Don't package html doc to incorrect doc directory
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}/*.html


%check
make check


%ldconfig_scriptlets


%files
%doc COPYING AUTHORS NEWS README docs/clique.xml
%{_libexecdir}/%{name}
%{_datadir}/dbus-1/services/*.service
%{_datadir}/telepathy/managers/*.manager
%{_mandir}/man8/%{name}.8.gz
%dir %{_libdir}/telepathy
%dir %{_libdir}/telepathy/salut-0
%dir %{_libdir}/telepathy/salut-0/lib
%{_libdir}/telepathy/salut-0/lib/libsalut-plugins-*.so
%{_libdir}/telepathy/salut-0/lib/libsalut-plugins.so
%{_libdir}/telepathy/salut-0/lib/libwocky-telepathy-salut-*.so
%{_libdir}/telepathy/salut-0/lib/libwocky.so


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Dec 30 2024 Chihurumnaya Ibiam <ibiam@sugarlabs.org> - 0.99.11-1
- Update to 0.99.11

* Sat Dec 28 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.8.1-34
- Fix compilation with -Werror=incompatible-pointer-types
- Switch wocky backend to gnutls which is already upstream default

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.8.1-33
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 0.8.1-26
- Rebuilt with OpenSSL 3.0.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 09 2021 Chihurumnaya Ibiam <ibiamchihurumnaya@gmail.com> - 0.8.1-23
- Limit openssl version to >=1.1

* Thu Dec 31 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.8.1-22
- Port to openssl110, patch extracted from upstream

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Feb 07 2020 Petr Viktorin <pviktori@redhat.com> - 0.8.1-20
- Remove BuildRequires on pygobject2

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 20 2019 Tom Callaway <spot@fedoraproject.org> - 0.8.1-18
- port to python3

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Mar 18 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.8.1-14
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Oct 17 2013 Debarshi Ray <rishi@fedoraproject.org> - 0.8.1-5
- Add %%check to run the upstream test suite on each build

* Wed Oct 16 2013 Debarshi Ray <rishi@fedoraproject.org> - 0.8.1-4
- Resolve possible multilib conflict

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov 16 2012 Brian Pepple <bpepple@fedoraproject.org> - 0.8.1-1
- Update to 0.8.1.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Apr  4 2012 Brian Pepple <bpepple@fedoraproject.org> - 0.8.0-1
- Update to 0.8.0.

* Mon Mar 26 2012 Brian Pepple <bpepple@fedoraproject.org> - 0.7.2-1
- Update to 0.7.2.
- Add BR on libuuid-devel.

* Tue Feb 21 2012 Brian Pepple <bpepple@fedoraproject.org> - 0.7.1-1
- Update to 0.7.1.

* Sun Jan 08 2012 Brian Pepple <bpepple@fedoraproject.org> - 0.7.0-2
- Rebuild for new gcc.

* Wed Nov 16 2011 Brian Pepple <bpepple@fedoraproject.org> - 0.7.0-1
- Update to 0.7.0.
- Bump minimum version of tp-glib needed.

* Tue Oct 18 2011 Brian Pepple <bpepple@fedoraproject.org> - 0.6.0-1
- Update to 0.6.0.

* Wed Oct  5 2011 Brian Pepple <bpepple@fedoraproject.org> - 0.5.2-1
- Update to 0.5.2.
- Bump minimum version of tp-glib needed.
- Drop olpc-activity-properties patch. Fix upstream.
- Drop buildroot. No longer necessary
- Drop no-xmldiff patch. No longer needed.

* Wed Sep 28 2011 Daniel Drake <dsd@laptop.org> - 0.5.1-1
- Update to 0.5.1

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Oct  6 2010 Brian Pepple <bpepple@fedoraproject.org> - 0.4.0-1
- Update to 0.4.0.

* Thu Aug 19 2010 Brian Pepple <bpepple@fedoraproject.org> - 0.3.13-1
- Update to 0.3.13.

* Thu May 20 2010 Brian Pepple <bpepple@fedoraproject.org> - 0.3.12-1
- Update to 0.3.12.
- Drop DSO linking patch. Fixed upstream.

* Sun Apr 25 2010 Brian Pepple <bpepple@fedoraproject.org> - 0.3.10-3
- Drop clean section. No longer needed.

* Fri Mar  5 2010 Peter Robinson <pbrobinson@gmail.com> 0.3.10-2
- Fix DSO linking. Fixes 565145

* Thu Sep 10 2009 Brian Pepple <bpepple@fedoraproject.org> - 0.3.10-1
- Update to 0.3.10.

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 0.3.9-3
- rebuilt with new openssl

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Apr  2 2009 Brian Pepple <bpepple@fedoraproject.org> - 0.3.9-1
- Update to 0.3.9.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 17 2009 Brian Pepple <bpepple@fedoraproject.org> - 0.3.8-1
- Update to 0.3.8.
- Bump minimum version of tp-glib-devel needed.

* Sun Jan 18 2009 Tomas Mraz <tmraz@redhat.com> - 0.3.7-2
- rebuild with new openssl

* Mon Jan  5 2009 Brian Pepple <bpepple@fedoraproject.org> - 0.3.7-1
- Update to 0.3.7.
- Change BR to libsoup-devel, since they support it now.

* Mon Dec  8 2008 Brian Pepple <bpepple@fedoraproject.org> - 0.3.6-2
- Enable OLPC support code. It is not used unless a client explicitely requests them.

* Sat Dec  6 2008 Brian Pepple <bpepple@fedoraproject.org> - 0.3.6-1
- Update to 0.3.6.
- Add BR on libsoup22-devel.

* Wed Sep 17 2008 Brian Pepple <bpepple@fedoraproject.org> - 0.3.5-1
- Update to 0.3.5.

* Sun Aug 24 2008 Brian Pepple <bpepple@fedoraproject.org> - 0.3.4-2
- Build with libasyncns support.

* Sat Aug 23 2008 Brian Pepple <bpepple@fedoraproject.org> - 0.3.4-1
- Update to 0.3.4.
- bump minimum tp-glib version needed.

* Mon Mar 24 2008 Brian Pepple <bpepple@fedoraproject.org> - 0.2.3-1
- Update to 0.2.3.

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.2.2-3
- Autorebuild for GCC 4.3

* Fri Feb  8 2008 Brian Pepple <bpepple@fedoraproject.org> - 0.2.2-2
- Rebuild for gcc-4.3.

* Wed Jan 30 2008 Brian Pepple <bpepple@fedoraproject.org> - 0.2.2-1
- Update to 0.2.2.

* Tue Jan  8 2008 Brian Pepple <bpepple@fedoraproject.org> - 0.2.1-1
- Update to 0.2.1.

* Fri Dec  7 2007 Brian Pepple <bpepple@fedoraproject.org> - 0.2.0-1
- Update to 0.2.0.

* Wed Dec  5 2007 Brian Pepple <bpepple@fedoraproject.org> - 0.1.11-2
- rebuild for new libssl.so.6/libcrypto.so.6

* Sat Dec  1 2007 Brian Pepple <bpepple@fedoraproject.org> - 0.1.11-1
- Update to 0.1.11.
- Add min. version of check needed.

* Tue Nov 27 2007 Brian Pepple <bpepple@fedoraproject.org> - 0.1.1-1
- Update to 0.1.10.

* Wed Nov 14 2007 Brian Pepple <bpepple@fedoraproject.org> - 0.1.9-1
- Update to 0.1.9.

* Tue Nov 13 2007 Brian Pepple <bpepple@fedoraproject.org> - 0.1.8-1
- Update to 0.1.8.

* Mon Nov 12 2007 Brian Pepple <bpepple@fedoraproject.org> - 0.1.7-1
- Update to 0.1.7.

* Wed Nov  7 2007 Brian Pepple <bpepple@fedoraproject.org> - 0.1.6-1
- Update to 0.1.6.
- Add man page.
- Bump min version of telepathy-glib-devel needed.

* Sat Aug 25 2007 Brian Pepple <bpepple@fedoraproject.org> - 0.1.4-1
- Update to 0.1.4.
- Update minimum BR versions needed.

* Tue Aug 21 2007 Brian Pepple <bpepple@fedoraproject.org> - 0.1.3-3
- Rebuild.

* Fri Aug  3 2007 Brian Pepple <bpepple@fedoraproject.org> - 0.1.3-2
- Update license tag.

* Tue Jun 26 2007 Brian Pepple <bpepple@fedoraproject.org> - 0.1.3-1
- Update to 0.1.3.
- Add BR on telepathy-glib-devel & libxslt.

* Mon Apr 16 2007 Brian Pepple <bpepple@fedoraproject.org> - 0.1.1-1
- Update to 0.1.1
- Add BR on openssl-devel & cyrus-sasl-devel.

* Sun Jan 21 2007 Brian Pepple <bpepple@fedoraproject.org> - 0.1.0-1
- Initial Fedora spec file.
