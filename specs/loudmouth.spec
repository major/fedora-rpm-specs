Name:           loudmouth
Version:        1.5.4
Release:        13%{?dist}
Summary:        XMPP/Jabber C programming library

License:        LGPL-2.0-or-later
URL:            https://github.com/mcabber/loudmouth/
Source0:        https://mcabber.com/files/loudmouth/loudmouth-%{version}.tar.bz2
Source1:        https://mcabber.com/files/loudmouth/loudmouth-%{version}.tar.bz2.asc
# Not verified, trust on first use
Source2:        gpgkey-EACADFF156849BC89653139E3C2900DEACB7FC95.gpg

BuildRequires:  gcc
BuildRequires:  check-devel
BuildRequires:  glib2-devel
# for gpg source verification
BuildRequires:  gpg
BuildRequires:  gtk-doc
BuildRequires:  openssl-devel
BuildRequires:  libasyncns-devel
BuildRequires:  libidn-devel
BuildRequires: make

%description
Loudmouth is a lightweight and easy-to-use C library for programming
with the XMPP/Jabber protocol. It's designed to be easy to get started
with and yet extensible to let you do anything the XMPP protocol allows.


%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       glib2-devel
Requires:       libidn-devel
Requires:       pkgconfig
Requires:       gnutls-devel


%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
gpgv --quiet --keyring %{SOURCE2} %{SOURCE1} %{SOURCE0}
%setup -q

%build
%configure --enable-static=no --with-asyncns=yes --with-ssl=openssl \
  --enable-gtk-doc --with-compile-warnings=yes

make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -delete

# Copy the files from the tarball to avoid the IDs generated by gtk-doc being
# different on different builds
#mkdir -p $RPM_BUILD_ROOT%{_datadir}/gtk-doc/html/%{name}/
#cp -a docs/reference/html/* $RPM_BUILD_ROOT%{_datadir}/gtk-doc/html/%{name}/


%check
make check


%ldconfig_scriptlets


%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc NEWS README
%{_libdir}/libloudmouth*.so.*

%files devel
%{_libdir}/libloudmouth*.so
%{_libdir}/pkgconfig/%{name}-1.0.pc
%{_includedir}/%{name}-1.0


%changelog
* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Mar 07 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.5.4-7
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.5.4-3
- Rebuilt with OpenSSL 3.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.5.4-1
- 1.5.4

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Feb 27 2016 Peter Robinson <pbrobinson@fedoraproject.org> 1.5.3-1
- Update to 1.5.3 release

* Fri Feb 19 2016 Yaakov Selkowitz <yselkowi@redhat.com> - 1.5.2-2
- Work around gtk-doc breakage in tarball (#1306222)
- Disable -Werror in release tarball

* Fri Feb  5 2016 Peter Robinson <pbrobinson@fedoraproject.org> 1.5.2-1
- Update to 1.5.2 release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Nov 15 2015 Till Maas <opensource@till.name> - 1.5.1-1
- Update to new release
- Verify source

* Wed Oct 28 2015 Till Maas <opensource@till.name> - 1.4.3-18
- Do not mix tab and space indenting
- Add patch upstream status

* Sun Jul 19 2015 Peter Robinson <pbrobinson@fedoraproject.org> 1.4.3-17
- Build with openssl support
- Cleanup spec
- Don't overlink libidn (rhbz 836761)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Mar  7 2012 Daniel Drake <dsd@laptop.org> - 1.4.3-10
- Fix compile against new glib

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Nov 15 2009 Brian Pepple <bpepple@fedoraproject.org> - 1.4.3-7
- Add patch to fix parser that stops on certain stanzas. (#509341)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jun 12 2009 Brian Pepple <bpepple@fedoraproject.org> - 1.4.3-5
- Add patch to fix digest uri bug. (#503901)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Nov 28 2008 Brian Pepple <bpepple@fedoraproject.org> - 1.4.3-3
- Add patch to search correct location for ssl certs. (#473458)
- Add patch to fix async assertion. (#473436)

* Sat Nov 22 2008 Brian Pepple <bpepple@fedoraproject.org> - 1.4.3-2
- Simplify sumary & description.

* Sun Nov  9 2008 Brian Pepple <bpepple@fedoraproject.org> - 1.4.3-1
- Update to 1.4.3.

* Thu Aug 28 2008 Brian Pepple <bpepple@fedoraproject.org> - 1.4.2-1
- Update to 1.4.2.
- Enable libasyncns support.

* Sat Aug  2 2008 Brian Pepple <bpepple@fedoraproject.org> - 1.4.1-1
- Update to 1.4.1.

* Wed Jun 25 2008 Tomas Mraz <tmraz@redhat.com> - 1.4.0-2
- rebuild with new gnutls

* Tue Jun 10 2008 Brian Pepple <bpepple@fedoraproject.org> - 1.4.0-1
- Update to 1.4.0.

* Wed Apr  2 2008 Brian Pepple <bpepple@fedoraproject.org> - 1.3.4-1
- Update to 1.3.4.
- Run check test.
- Bump min version needed for gnutls-devel.
- Drop stream-error.patch. Fixed upstream.
- Drop eai-nodata.patch. Fixed upstream.
- Drop connect-fail-sync.patch. Fixed upstream.
- Drop connect-fail-async patch. Fixed upstream.
- Update URL & Source URL.
- Don't generate the gtk-doc docs, and use the ones in the tarball
  to avoid having different files in different builds, fixes
  multilib problems (#342551)

* Thu Feb 21 2008 Owen Taylor <otaylor@redhat.com> - 1.3.3-4
- Fix build with recent GNU libc

* Thu Feb  7 2008 Owen Taylor <otaylor@redhat.com> - 1.3.3-3
- Add patches fixing reentrancy problems on connection failure

* Wed Jan 30 2008 Owen Taylor <otaylor@redhat.com> - 1.3.3-2
- Add back stream-error patch, it wasn't fixed in the 1.3 branch

* Fri Jan 18 2008 Brian Pepple <bpepple@fedoraproject.org> - 1.3.3-1
- Update to 1.3.3.
- Drop reconnect-failure patch.
- Drop gnutls compression patch. fixed upstream.

* Thu Nov 15 2007 Brian Pepple <bpepple@fedoraproject.org> - 1.2.3-6
- Ugh.  Let's acutally use a valid e-mail addy.

* Thu Nov 15 2007 Brian Pepple <bpepple@fedoraproject.org> - 1.2.3-5
- Add patch to use gnutls compression.

* Mon Nov 12 2007 Brian Pepple <bpepple@fedoraproject.org> - 1.2.3-4
- Add reconnect-failure patch. Thanks to Robert McQueen.

* Tue Aug 21 2007 Brian Pepple <bpepple@fedoraproject.org> - 1.2.3-3
- Rebuild.

* Sun Aug  5 2007 Brian Pepple <bpepple@fedoraproject.org> - 1.2.3-2
- Update license tag.

* Sun Jun 10 2007 Brian Pepple <bpepple@fedoraproject.org> - 1.2.3-1
- Update to 1.2.3.
- Drop stream-error patch. fixed upstream.

* Wed May 16 2007 Brian Pepple <bpepple@fedoraproject.org> - 1.2.2-3
- Add patch to fix stream error.

* Tue May 15 2007 Brian Pepple <bpepple@fedoraproject.org> - 1.2.2-2
- Drop BR on libtasn1-devel.

* Mon May 14 2007 Brian Pepple <bpepple@fedoraproject.org> - 1.2.2-1
- Update to 1.2.2.

* Sat Feb 24 2007 Brian Pepple <bpepple@fedoraproject.org> - 1.2.1-2
- Fix typo.

* Sat Feb 24 2007 Brian Pepple <bpepple@fedoraproject.org> - 1.2.1-1
- Update to 1.2.1.

* Tue Feb 20 2007 Brian Pepple <bpepple@fedoraproject.org> - 1.2.0-3
- Add necessary requires to devel package. D'Oh!

* Tue Feb 20 2007 Brian Pepple <bpepple@fedoraproject.org> - 1.2.0-2
- Add BR on libidn-devel.
- Specify which ssl implementation to use.

* Mon Feb  5 2007 Brian Pepple <bpepple@fedoraproject.org> - 1.2.0-1
- Update to 1.2.0.
- Drop mono config option since it's been dropped from the tarball.

* Mon Sep 11 2006 Brian Pepple <bpepple@fedoraproject.org> - 1.0.5-2
- Change source to .gz.

* Mon Sep 11 2006 Brian Pepple <bpepple@fedoraproject.org> - 1.0.5-1
- Update to 1.0.5.

* Tue Aug 29 2006 Brian Pepple <bpepple@fedoraproject.org> - 1.0.4-3
- Rebuild for FC6.
- Simplify devel description.

* Thu Jun 29 2006 Brian Pepple <bpepple@fedoraproject.org> - 1.0.4-2
- Update to 1.0.4.
- Add devel requires on pkgconfig.
- Drop reentrancy patch, fixed upstream.

* Thu Jun 15 2006 Jeremy Katz <katzj@redhat.com> - 1.0.3-5
- rebuild for new gnutls

* Fri May 26 2006 Brian Pepple <bdpepple@ameritech.net> - 1.0.3-4
- Add patch to fix some reentrancy crashes.  (Thanks, Havoc)

* Wed Apr  5 2006 Brian Pepple <bdpepple@ameritech.net> - 1.0.3-3
- Update to 1.0.3.
- Add BR for gnutls-devel to devel package.
- Disable static libs.
- Add BR for check-devel.

* Thu Feb 16 2006 Brian Pepple <bdpepple@ameritech.net> - 1.0.1-6
- Remove unnecessary BR (libgcrypt-devel).

* Mon Feb 13 2006 Brian Pepple <bdpepple@ameritech.net> - 1.0.1-5
- rebuilt for new gcc4.1 snapshot and glibc changes

* Mon Dec 26 2005 Brian Pepple <bdpepple@ameritech.net> - 1.0.1-4
- Rebuild.

* Wed Aug 31 2005 Brian Pepple <bdpepple@ameritech.net> - 1.0.1-3
- Update to 1.0.1.

* Sun Aug 14 2005 Brian Pepple <bdpepple@ameritech.net> - 1.0-2
- Update to 1.0.

* Mon Aug  8 2005 Brian Pepple <bdpepple@ameritech.net> - 0.90-5
- Rebuild due to new gnutls.

* Sat Jul 30 2005 Brian Pepple <bdpepple@ameritech.net> - 0.90-4
- Fix description.

* Fri May 13 2005 Brian Pepple <bdpepple@ameritech.net> - 0.90-2
- Add dist tag.

* Fri May 13 2005 Brian Pepple <bdpepple@ameritech.net> - 0.90-1
- Update to 0.9.

* Thu May  5 2005 Brian Pepple <bdpepple@ameritech.net> - 0.17.2-3
- Adde glib2-devel requires.

* Thu May  5 2005 Brian Pepple <bdpepple@ameritech.net> - 0.17.2-2
- added %%{_includedir}.
- Add libgcrypt-devel BR.

* Sun May  1 2005 Brian Pepple <bdpepple@ameritech.net> - 0.17.2-1
- Initial Fedora build.

