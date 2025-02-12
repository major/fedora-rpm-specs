# should be vendor 'fedora', but that would break upgrades for
# people who have linked the desktop icon
%global desktopvendor redhat

%global is_prerelease 0

%if 0%{?is_prerelease}
%global prerelease rc2
%endif

Name:           sylpheed
Version:        3.7.0
Release:        18%{?prerelease:.%{?prerelease}}%{?dist}
Summary:        GTK+ based, lightweight, and fast email client

License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND MIT AND LicenseRef-Fedora-Public-Domain
URL:            http://sylpheed.sraoss.jp/
#VCS:           https://github.com/sylpheed-mail/sylpheed

Source0:        http://sylpheed.sraoss.jp/sylpheed/v3.7/%{name}-%{version}%{?prerelease}.tar.bz2
Source1:        sylpheed.1

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gtk2-devel
BuildRequires:  openssl-devel
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig
BuildRequires:  gettext
BuildRequires:  xdg-utils
%{!?_without_gpgme:BuildRequires: gpgme-devel}
%{!?_without_compface:BuildRequires: compface-devel}
%{!?_without_ldap:BuildRequires: openldap-devel}
%{?_with_oniguruma:BuildRequires: oniguruma-devel}
%{?_with_jpilot:BuildRequires: jpilot-devel}
BuildRequires:  gtkspell-devel
BuildRequires:  enchant-devel

# customisations for default program paths
Patch1:         sylpheed-3.1.0-defs.h.patch
# customisations in the .desktop file
Patch2:         sylpheed-3.5.0-desktop.patch
# customisation for /etc/pki/tls/
Patch3:         sylpheed-2.5.0-certsdir.patch
# harden link checker
# https://bugzilla.redhat.com/show_bug.cgi?id=1988552
Patch4:         sylpheed-3.7.0-uri-check.patch
# various type and format related fixes
Patch5:         sylpheed-3.7.0-types.patch

Requires: sylpheed-libs%{?_isa} = %{version}-%{release}
# For xdg-open in patch1
Requires: xdg-utils

%description
This program is an X based fast email client which has features like:

o user-friendly and intuitive interface
o integrated NetNews client (partially implemented)
o ability of keyboard-only operation
o Mew/Wanderlust-like key bind
o multipart MIME
o unlimited multiple account handling
o message queueing
o assortment function
o XML-based address book

See /usr/share/doc/sylpheed*/README for more information.


%package libs
Summary: Libraries for sylpheed

%description libs
This package contains libraries for Sylpheed.


%package devel
Summary: Development files for sylpheed
Requires: sylpheed-libs%{?_isa} = %{version}-%{release}

%description devel
This package contains development files for Sylpheed.


%prep
%autosetup %{?prerelease:-n %{name}-%{version}%{?prerelease}} -p1

%build
%global optflags %{optflags} -std=gnu17

%configure --disable-silent-rules \
    --enable-ssl --disable-updatecheck \
    --with-plugindir=%{_libdir}/%{name}/plugins \
    %{!?_without_gpgme:--enable-gpgme} \
    %{?_without_compface:--disable-compface} \
    %{!?_without_ldap:--enable-ldap} \
    %{?_with_oniguruma:--enable-oniguruma} \
    %{?_with_jpilot:--enable-jpilot}
# Remove rpaths
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build


%install
%make_install

# Install plugins
pushd plugin/attachment_tool
make install-plugin DESTDIR=$RPM_BUILD_ROOT INSTALL='install -p'
popd

find $RPM_BUILD_ROOT -name \*.la -exec rm {} \;

# Install an icon
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -p -m 644 sylpheed-64x64.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/sylpheed.png

# Install menu entries
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --delete-original \
  %if (0%{?fedora} && 0%{?fedora} < 19) || (0%{?rhel} && 0%{?rhel} < 7)
    --vendor %{desktopvendor} \
  %endif
    --dir $RPM_BUILD_ROOT%{_datadir}/applications \
    ${RPM_BUILD_ROOT}%{_datadir}/applications/%{name}.desktop

# Install the manpage
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -p -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man1/

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog ChangeLog-1.0 COPYING COPYING.LIB LICENSE
%doc NEWS NEWS-1.0 NEWS-2.0 README TODO
%lang(ja) %doc ChangeLog.ja ChangeLog-1.0.ja README.ja INSTALL.ja TODO.ja
%lang(es) %doc README.es
%{_bindir}/sylpheed
%{_datadir}/sylpheed/
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/pixmaps/*
%{_mandir}/man1/*
%{_libdir}/sylpheed/

%files libs
%doc COPYING COPYING.LIB LICENSE
%{_libdir}/libsylph-0.so.*
%{_libdir}/libsylpheed-plugin-0.so.*


%files devel
%doc PLUGIN.txt 
%lang(ja) %doc PLUGIN.ja.txt
%{_includedir}/sylpheed/
%{_libdir}/*.so

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 3.7.0-11
- Rebuilt with OpenSSL 3.0.0

* Mon Aug 02 2021 Dan Horák <dan[at]danny.cz> - 3.7.0-10
- harden link checker (#1988552)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Dan Horák <dan[at]danny.cz> - 3.7.0-1
- update to 3.7.0 (#1536003)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 18 2017 Dan Horák <dan[at]danny.cz> - 3.6.0-1
- update to 3.6.0 (#1460700)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 10 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 3.5.1-2
- Rebuild for gpgme 1.18

* Mon Sep 05 2016 Dan Horák <dan[at]danny.cz> - 3.5.1-1
- update to 3.5.1 (#1361572)

* Tue Feb 16 2016 Dan Horák <dan[at]danny.cz> - 3.5.0-2
- add missing dep on libs subpackage

* Sun Feb 14 2016 Dan Horák <dan[at]danny.cz> - 3.5.0-1
- update to 3.5.0 (#1111896)
- cleanup spec

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 10 2016 Dan Horák <dan[at]danny.cz> - 3.4.3-3
- introduce libs subpackage (related #1265685)

* Tue Dec 08 2015 Dan Horák <dan[at]danny.cz> - 3.4.3-2
- Update BR

* Sat Nov 21 2015 Dan Horák <dan[at]danny.cz> - 3.4.3-1
- Update to 3.4.3

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 13 2014 Christoph Wickert <cwickert@fedoraproject.org> - 3.4.2-1
- Update to 3.4.2 (#1108822)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 04 2014 Christoph Wickert <cwickert@fedoraproject.org> - 3.4.1-1
- Update to 3.4.1 (#1080927)

* Mon Mar 24 2014 Dan Horák <dan[at]danny.cz> - 3.4.0-0.8.beta8
- Update to 3.4.0beta8 (#1079558)

* Fri Dec 20 2013 Christoph Wickert <cwickert@fedoraproject.org> - 3.4.0-0.7.beta7
- Update to 3.4.0beta7 (#1024941)

* Sat Nov 02 2013 Christoph Wickert <cwickert@fedoraproject.org> - 3.4.0-0.7.beta6
- Update to 3.4.0beta6 (#1024941)

* Tue Sep 10 2013 Christoph Wickert <cwickert@fedoraproject.org> - 3.4.0-0.6.beta5
- Update to 3.4.0beta5 (#1003405)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.0-0.6.beta4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 05 2013 Christoph Wickert <cwickert@fedoraproject.org> - 3.4.0-0.5.beta4
- Update to 3.4.0beta4 (#968437)
- Remove patches for DSO fix and aarch64 support, no longer required

* Sat Apr 20 2013 Christoph Wickert <cwickert@fedoraproject.org> - 3.4.0-0.4.beta3
- Update to 3.4.0beta3 (#946898)
- Add aarch64 support (#926591)
- Make desktop file vendor conditional

* Mon Feb 18 2013 Christoph Wickert <cwickert@fedoraproject.org> - 3.4.0-0.3.beta2
- Don't install the test plugin (#912469)

* Fri Feb 15 2013 Christoph Wickert <cwickert@fedoraproject.org> - 3.4.0-0.2.beta2
- Remove the --vendor switch to desktop-file-install

* Fri Feb 15 2013 Christoph Wickert <cwickert@fedoraproject.org> - 3.4.0-0.1.beta2
- Update to 3.4.0beta2 (#907136)

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Nov 15 2012 Christoph Wickert <cwickert@fedoraproject.org> - 3.3.0-1
- Update to 3.3.0 (#861429)

* Thu Sep 20 2012 Christoph Wickert <cwickert@fedoraproject.org> - 3.2.0-1
- Update to 3.2.0 final

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.0-0.5.rc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 26 2012 Christoph Wickert <cwickert@fedoraproject.org> - 3.2.0-0.4.rc
- Update to 3.2.0 RC (#835445)

* Tue Jun 19 2012 Christoph Wickert <cwickert@fedoraproject.org> - 3.2.0-0.4.beta9
- Update to 3.2.0 Beta 9 (#833341)

* Sun Jun 10 2012 Christoph Wickert <cwickert@fedoraproject.org> - 3.2.0-0.4.beta8
- Update to 3.2.0 Beta 8 (#812311)
- Drop upstreamed glib.patch

* Wed Feb 29 2012 Christoph Wickert <cwickert@fedoraproject.org> - 3.2.0-0.4.beta6
- Update to 3.2.0 Beta 6 (#798620)

* Mon Jan 30 2012 Christoph Wickert <cwickert@fedoraproject.org> - 3.2.0-0.3.beta5
- Update to 3.2.0 Beta 5
- Fix plugin installation

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.0-0.2.beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Sep 08 2011 Christoph Wickert <cwickert@fedoraproject.org> - 3.2.0-0.1.beta3
- Update to 3.2.0 Beta 3 (#736646)

* Fri Aug 12 2011 Christoph Wickert <cwickert@fedoraproject.org> - 3.2.0-0.1.beta2
- Update to 3.2.0 Beta 2 (#730283)

* Tue Jul 05 2011 Christoph Wickert <cwickert@fedoraproject.org> - 3.2.0-0.1.beta1
- Update to 3.2.0 Beta 1 (#718980)

* Fri May 06 2011 Christoph Wickert <wickert@kolabsys.com> - 3.1.1-1
- Update to 3.1.1 (#702612)
- Remove rpaths

* Thu Mar 24 2011 Christoph Wickert <cwickert@fedoraproject.org> - 3.1.0-2
- Add MimeType 'x-scheme-handler/mailto' for GNOME 3 (#690298)

* Mon Feb 21 2011 Christoph Wickert <cwickert@fedoraproject.org> - 3.1.0-1
- Update to 3.1.0 final

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-0.3.beta7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 18 2011 Christoph Wickert <cwickert@fedoraproject.org> - 3.1.0-0.2.beta7
- Configure with --disable-updatecheck instead of patching

* Tue Jan 18 2011 Christoph Wickert <cwickert@fedoraproject.org> - 3.1.0-0.1.beta7
- Update to 3.1.0 Beta 7 (#665632)

* Sun Dec 12 2010 Christoph Wickert <cwickert@fedoraproject.org> - 3.1.0-0.1.beta5
- Update to 3.1.0 Beta 5 (#662504)

* Thu Dec 09 2010 Christoph Wickert <cwickert@fedoraproject.org> - 3.1.0-0.1.beta4
- Update to 3.1.0 Beta 4 (#661481)

* Thu Aug 19 2010 Christoph Wickert <cwickert@fedoraproject.org> - 3.1.0-0.1.beta3
- Update to 3.1.0 Beta 3 (#625001)

* Sat Jul 17 2010 Christoph Wickert <cwickert@fedoraproject.org> - 3.1.0-0.1.beta2
- Update to 3.1.0 Beta 2 (#615273)

* Tue Jun 15 2010 Christoph Wickert <cwickert@fedoraproject.org> - 3.1.0-0.1.beta1
- Update to 3.1.0 Beta 1 (#589493)

* Tue Jun 15 2010 Christoph Wickert <cwickert@fedoraproject.org> - 3.0.2-1
- Update to 3.0.2

* Fri Feb 26 2010 Christoph Wickert <cwickert@fedoraproject.org> - 3.0.0-4
- Update to 3.0.0 final
- Add patch to fix DSO linking (#565108)
- Add some more %%doc files
- Use new layout of the folder view (don't display message numbers in colums)
- Disable update check by default

* Mon Feb 01 2010 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 3.0.0-3.0.beta7
- sylpheed-3.0.0beta7

* Mon Dec 21 2009 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 3.0.0-1.0.beta4
- new version 3.0.0beta4

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 2.7.1-2
- rebuilt with new openssl

* Thu Aug 13 2009 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 2.7.1-1
- new version 2.7.1

* Wed Jul 29 2009 Michael Schwendt <mschwendt@fedoraproject.org> - 2.7.0-3
- no ldconfig scriptlets in -devel package
- add more/new %%doc files

* Mon Jul 27 2009 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 2.7.0-2
- small fix in spec files about libs

* Mon Jul 27 2009 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 2.7.0-1
- new version 2.7.0

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Michael Schwendt <mschwendt@fedoraproject.org> - 2.6.0-4
- fix crash in import of csv address-books with empty Name fields

* Fri Feb 13 2009 Michael Schwendt <mschwendt@fedoraproject.org> - 2.6.0-3
- no build, add comments to spec file, remove old cruft

* Sun Jan 18 2009 Tomas Mraz <tmraz@redhat.com> - 2.6.0-2
- rebuild with new openssl

* Fri Dec 19 2008 Michael Schwendt <mschwendt@fedoraproject.org> - 2.6.0-1
- update to 2.6.0 final (obsoletes SOCK_NONBLOCK patch)

* Mon Dec  1 2008 Michael Schwendt <mschwendt@fedoraproject.org> - 2.6.0-0.1.rc
- update to 2.6.0rc

* Mon Nov 17 2008 Michael Schwendt <mschwendt@fedoraproject.org> - 2.6.0-0.1.beta2
- update to 2.6.0beta2

* Tue Sep 30 2008 Michael Schwendt <mschwendt@fedoraproject.org> - 2.6.0-0.1.beta1
- update to 2.6.0beta1

* Thu Aug 28 2008 Michael Schwendt <mschwendt@fedoraproject.org> - 2.5.0-4.2029svn
- patch libsylph/socket.* to not redefine SOCK_NONBLOCK from
  /usr/include/bits/socket.h
- rediff some patches for Fedora fuzz=0 pedantry

* Tue Jul 22 2008 Michael Schwendt <mschwendt@fedoraproject.org> - 2.5.0-2.2029svn
- update to post-2.5.0 revision 2029
- upstream's IMAP LIST modifications move away from RFC 2683 (test this!)

* Tue Jun 17 2008 Michael Schwendt <mschwendt@fedoraproject.org> - 2.5.0-1
- update to 2.5.0 final (a few translation updates)

* Tue Jun 10 2008 Michael Schwendt <mschwendt@fedoraproject.org> - 2.5.0-0.10.rc2
- work around build problem with gtk2 >= 2.13.1 which drastically
  changed the number of header-includes for the deprecated header files

* Sun Jun  8 2008 Michael Schwendt <mschwendt@fedoraproject.org> - 2.5.0-0.8.rc2
- avoid duplicate desktop menu entry
- conditional BR oniguruma-devel and --enable-oniguruma

* Fri Jun  6 2008 Michael Schwendt <mschwendt@fedoraproject.org> - 2.5.0-0.7.rc2
- Update to 2.5.0rc2.

* Thu Jun  5 2008 Michael Schwendt <mschwendt@fedoraproject.org> - 2.5.0-0.6.rc
- Add CTE procmime.c patch from svn.
- Fix codeconv.c to support "utf8" locales and not just "UTF-8"
  (fixes #450063).

* Thu May 22 2008 Michael Schwendt <mschwendt@fedoraproject.org> - 2.5.0-0.4.rc
- Fix glibc double-free/invalidptr in src/summaryview.c
  (assumably also fixes #447815).

* Tue May 20 2008 Michael Schwendt <mschwendt@fedoraproject.org> - 2.5.0-0.3.rc
- Update to 2.5.0rc (bug-fixes, enhancements).

* Thu May 15 2008 Michael Schwendt <mschwendt@fedoraproject.org> - 2.5.0-0.2.beta3
- desktop-file: validate for F9+

* Fri Apr 25 2008 Michael Schwendt <mschwendt@fedoraproject.org> - 2.5.0-0.1.beta3
- Update to 2.5.0beta3 (two minor features added).

* Mon Apr 14 2008 Michael Schwendt <mschwendt@fedoraproject.org> - 2.5.0-0.1.beta2
- Update to 2.5.0beta2 (several added features, few bug-fixes).

* Fri Feb 29 2008 Michael Schwendt <mschwendt@fedoraproject.org> - 2.5.0-0.1.beta1
- Update to 2.5.0beta1 (bug-fixes and few added features).

* Fri Feb 08 2008 Michael Schwendt <mschwendt@fedoraproject.org> - 2.4.8-3
- rebuilt for GCC 4.3 as requested by Fedora Release Engineering

* Wed Jan 23 2008 Michael Schwendt <mschwendt@fedoraproject.org> - 2.4.8-2
- Compile with deprecated OpenLDAP API to fix segfaults on 64-bit.

* Sun Dec 23 2007 Michael Schwendt <mschwendt@fedoraproject.org> - 2.4.8-1
- Patch spell-checking support. Retrieve list of dictionaries from
  Enchant instead of Aspell, because GtkSpell no longer uses Aspell.
- BR enchant-devel
- Update to 2.4.8 (accumulated bug-fixes).

* Mon Dec 17 2007 Michael Schwendt <mschwendt@fedoraproject.org> - 2.4.7-4
- Upstreamed patch lead to discovery of similar memory leaks in syldap.c

* Wed Dec 05 2007 Michael Schwendt <mschwendt@fedoraproject.org> - 2.4.7-3
- rebuilt for new openldap/openssl per request on fedora-devel-list
- in desktop file use absolute path to icon file

* Fri Nov 02 2007 Michael Schwendt <mschwendt@fedoraproject.org> - 2.4.7-2
- Patch a memory leak and glib critical warning in LDAP syldap.c.

* Fri Oct 05 2007 Michael Schwendt <mschwendt@fedoraproject.org> - 2.4.7-1
- Update to 2.4.7 (bug-fixes).
- Add more %%doc files.

* Tue Oct 02 2007 Michael Schwendt <mschwendt@fedoraproject.org> - 2.4.6-2
- Require xdg-utils and use xdg-open instead of gnome-open in defs.h
  patch.

* Wed Sep 19 2007 Michael Schwendt <mschwendt@fedoraproject.org> - 2.4.6-1
- Update to 2.4.6 (bug-fixes, but also minor feature additions
  and rewrites).

* Fri Aug 31 2007 Michael Schwendt <mschwendt@fedoraproject.org> - 2.4.5-1
- Update to 2.4.5 (accumulated bug-fixes).

* Fri Aug 24 2007 Michael Schwendt <mschwendt@fedoraproject.org> - 2.4.4-3
- Patch POP3 format string vulnerability CVE-2007-2958 (#254123).

* Tue Aug 21 2007 Michael Schwendt <mschwendt@fedoraproject.org>
- rebuilt

* Sat Jul 21 2007 Michael Schwendt <mschwendt@fedoraproject.org> - 2.4.4-1
- Update to 2.4.4.

* Fri Jun 29 2007 Michael Schwendt <mschwendt@fedoraproject.org> - 2.4.3-1
- Update to 2.4.3.

* Mon May 21 2007 Michael Schwendt <mschwendt@fedoraproject.org> - 2.4.2-1
- Update to 2.4.2 (new stable branch).
- Prune %%changelog entries which date back as far as Jul 4 2000
  and Sylpheed 0.3.2.

* Fri May 18 2007 Michael Schwendt <mschwendt@fedoraproject.org> - 2.3.1-4
- Backport patch for libsylph to improve/fix handling of escapes
  and quotes in headers.

* Sun May 13 2007 Michael Schwendt <mschwendt@fedoraproject.org> - 2.3.1-3
- Patch PGP/MIME signed message compose, so it doesn't strip off
  whitespace of the "-- " body signature delimiter. It's upstream
  preference that it still does that for ISO 2022 JP to be compatible
  with a few broken MUAs that have problems with QP encoding.
- Remove .desktop categories "Application" and "X-Fedora".

* Sat Apr 21 2007 Michael Schwendt <mschwendt@fedoraproject.org> - 2.3.1-2
- Patch APOP vulnerability (CVE-2007-1558) as in 2.4.0.
- Patch default directory for SSL/TLS certificates.

* Wed Jan 17 2007 Michael Schwendt <mschwendt@fedoraproject.org> - 2.3.1-1
- Update to 2.3.1.

* Sat Dec 23 2006 Michael Schwendt <mschwendt@fedoraproject.org> - 2.3.0-1
- Update to 2.3.0 (new stable branch).

* Thu Nov 16 2006 Michael Schwendt <mschwendt@fedoraproject.org> - 2.2.10-1
- Update to 2.2.10 (recommended bug-fixes only).

* Mon Oct 02 2006 Michael Schwendt <mschwendt@fedoraproject.org>
- rebuilt

* Sat Sep 23 2006 Michael Schwendt <mschwendt@fedoraproject.org> - 2.2.9-1
- Update to 2.2.9 (also works around #201949).
- New upstream URLs.

* Fri Sep  8 2006 Michael Schwendt <mschwendt@fedoraproject.org> - 2.2.7-3
- Set StartupWMClass in desktop file.

* Fri Sep 01 2006 Michael Schwendt <mschwendt@fedoraproject.org>
- rebuilt

* Mon Jul 31 2006 Michael Schwendt <mschwendt@fedoraproject.org> - 2.2.7-1
- Update to 2.2.7 (includes patches from 2.2.6-2 and -3).

* Sun Jul 30 2006 Michael Schwendt <mschwendt@fedoraproject.org> - 2.2.6-4
- Enable OpenLDAP support as requested by several users.
- Drop minimal version from GPGME build requirement
  (it's superfluous in our environments).

* Tue Jun 27 2006 Michael Schwendt <mschwendt@fedoraproject.org> - 2.2.6-3
- Adapt upstream's patch for a crash with Turkish locales.

* Mon Jun 26 2006 Michael Schwendt <mschwendt@fedoraproject.org> - 2.2.6-2
- Adapt upstream's patch to prevent a crash when switching folders
  (sylpheed-2.2.6-summaryview-crash.patch).

* Fri Jun  9 2006 Michael Schwendt <mschwendt@fedoraproject.org> - 2.2.6-1
- Update to 2.2.6 (includes the smtp_timeout patch).

* Sat Jun  3 2006 Michael Schwendt <mschwendt@fedoraproject.org> - 2.2.5-2
- Add smtp_timeout patch.
- Add display_folder_num_columns patch.

* Tue May 30 2006 Michael Schwendt <mschwendt@fedoraproject.org> - 2.2.5-1
- Update to 2.2.5 (includes more "bold" fixes, too).

* Fri Mar 31 2006 Michael Schwendt <mschwendt@fedoraproject.org> - 2.2.4-1
- Update to 2.2.4.

* Sun Mar 19 2006 Michael Schwendt <mschwendt@fedoraproject.org> - 2.2.3-1
- Update to 2.2.3.
- Update external commands (defs.h) patch.

* Sat Feb 18 2006 Michael Schwendt <mschwendt@fedoraproject.org> - 2.2.0-1
- Update to 2.2.0 (new stable series).
- BR gtkspell-devel.

* Wed Feb 15 2006 Michael Schwendt <mschwendt@fedoraproject.org> - 2.0.4-2
- rebuilt for FC5

* Thu Nov 10 2005 Michael Schwendt <mschwendt@fedoraproject.org> - 2.0.4-1
- Update to 2.0.4 (security).

* Sat Oct 22 2005 Michael Schwendt <mschwendt@fedoraproject.org> - 2.0.3-1
- Update to 2.0.3.

* Sat Oct  1 2005 Michael Schwendt <mschwendt@fedoraproject.org> - 2.0.2-1
- Update to 2.0.2.

* Mon Sep  5 2005 Michael Schwendt <mschwendt@fedoraproject.org> - 2.0.1-1
- Update to 2.0.1.

* Wed Aug 17 2005 Michael Schwendt <mschwendt@fedoraproject.org> - 2.0.0-2
- rebuilt

* Sat Jul 30 2005 Michael Schwendt <mschwendt@fedoraproject.org> - 2.0.0-1
- Update to 2.0.0.

* Tue Jul 26 2005 Michael Schwendt <mschwendt@fedoraproject.org> - 2.0.0-0.4.rc
- Update to 2.0.0rc.

* Fri Jul 15 2005 Michael Schwendt <mschwendt@fedoraproject.org> - 2.0.0-0.4.beta6
- Update to 2.0.0beta6 (feature freeze).

* Sun Jul 10 2005 Michael Schwendt <mschwendt@fedoraproject.org> - 2.0.0-0.4.beta5
- Update to 2.0.0beta5.

* Tue Jul  5 2005 Michael Schwendt <mschwendt@fedoraproject.org> - 2.0.0-0.4.beta4
- Update to 2.0.0beta4.

* Tue Jun 28 2005 Michael Schwendt <mschwendt@fedoraproject.org>
- remove work-around from previous entry again, bug has been fixed

* Sun Jun 26 2005 Michael Schwendt <mschwendt@fedoraproject.org> - 2.0.0-0.2.beta3
- temporarily add BR libpng-devel to work around a broken cairo-devel
  package, which is pulled in and breaks the pkg-config dependency
  chain (#161688)

* Fri Jun 24 2005 Michael Schwendt <mschwendt@fedoraproject.org> - 2.0.0-0.1.beta3
- Update to 2.0.0beta3.
- Patch1 (flexible OpenSSL pkg-config support) merged upstream.

* Fri Jun 17 2005 Michael Schwendt <mschwendt@fedoraproject.org> - 2.0.0-0.1.beta2
- Update to 2.0.0beta2.

* Fri Jun 10 2005 Michael Schwendt <mschwendt@fedoraproject.org> - 2.0.0-0.1.beta1
- Update to 2.0.0beta1.

* Mon May 30 2005 Michael Schwendt <mschwendt@fedoraproject.org> - 1.9.12-1
- Update to 1.9.12 to get a bunch of fixes.

* Fri May 13 2005 Michael Schwendt <mschwendt@fedoraproject.org> - 1.9.10-1
- Update to 1.9.10.
- Upstream incorporated some desktop file fixes.

* Fri Apr 22 2005 Michael Schwendt <mschwendt@fedoraproject.org> - 1.9.9-1
- Update to 1.9.9.

* Mon Apr 18 2005 Michael Schwendt <mschwendt@fedoraproject.org> - 1.9.8-1
- Update to 1.9.8.

* Thu Mar 31 2005 Michael Schwendt <mschwendt@fedoraproject.org> - 1.9.7-1
- Update to 1.9.7.
- Patch4 (draftsegf) merged upstream.

* Sun Mar 20 2005 Michael Schwendt <mschwendt@fedoraproject.org> - 1.9.6-1
- Update to 1.9.6 development release for testing purposes.

* Thu Mar 17 2005 Michael Schwendt <mschwendt@fedoraproject.org> - 1.0.3-2
- Fix segfault when reopening drafts.

* Sat Mar  5 2005 Michael Schwendt <mschwendt@fedoraproject.org> - 1.0.3-1
- Update to 1.0.3.
- Enable support for GPGME 1.0 and compface.
- Apply common spec cleanup. Make desktop file UTF-8.

* Wed Jan  5 2005 Akira TAGOH <tagoh@redhat.com> - 1.0.0-1
- New upstream release.

* Mon Dec 20 2004 Akira TAGOH <tagoh@redhat.com> - 1.0.0-0.1.rc
- New upstream release.

* Mon Nov 22 2004 Akira TAGOH <tagoh@redhat.com> - 1.0.0-0.1.beta3
- New upstream release.
- sylpheed-default-browser.patch: updated to apply cleanly.
- sylpheed.1: added a simple man page. (#129387)

* Wed Jun 23 2004 Akira TAGOH <tagoh@redhat.com> 0.9.12-1
- New upstream release.

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon May 31 2004 Akira TAGOH <tagoh@redhat.com> 0.9.11-1
- New upstream release.

* Wed Mar 24 2004 Akira TAGOH <tagoh@redhat.com> 0.9.10-2
- sylpheed-default-browser.patch: applied to change the default browser to
  gnome-open. (#119007, Michael Schwendt)

* Wed Mar 10 2004 Akira TAGOH <tagoh@redhat.com> 0.9.10-1
- New upstream release.

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Akira TAGOH <tagoh@redhat.com> 0.9.9-1
- New upstream release.

* Fri Jan 30 2004 Akira TAGOH <tagoh@redhat.com> 0.9.8a-3
- don't strip the binary. Thanks to Michael Schwendt
- use upstream's icon for the desktop file.
- install the desktop file using desktop-install-file

* Thu Jan 29 2004 Akira TAGOH <tagoh@redhat.com> 0.9.8a-2
- add _with_gpgme to build enabled gpgme support.
  NOTE: it's disabled as default. just define _with_gpgme to enable it.
