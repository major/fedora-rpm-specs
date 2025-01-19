Summary:       Graphical LDAP directory browser and editor
Name:          gq
Version:       1.3.4
Release:       54%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later
URL:           http://sourceforge.net/projects/gqclient/
Source0:       http://downloads.sourceforge.net/project/gqclient/GQ%20Unstable/%{version}/gq-%{version}.tar.gz
Patch0:        gq-1.2.1-desktop.patch
Patch1:        gq-1.3.4-kerberos.patch
Patch2:        gq-1.3.4-configure.patch
Patch3:        gq-1.3.4-dso.patch
Patch4:        gq-1.3.4-glibfix.patch
Patch5:        gq-1.3.4-errorchain.patch
Patch6:        gq-1.3.4-strcmp-null-safe.patch
Patch7:        gq-1.3.4-sanity-check.patch
Patch8:        gq-1.3.4-format.patch
Patch9:        gq-1.3.4-openssl.patch
Patch10: gq-configure-c99.patch
BuildRequires: gcc
BuildRequires: gtk2-devel
BuildRequires: libglade2-devel
Buildrequires: libgcrypt-devel
BuildRequires: libgnome-keyring-devel
BuildRequires: libxml2-devel
BuildRequires: krb5-devel
Buildrequires: gettext
BuildRequires: desktop-file-utils
BuildRequires: gnome-doc-utils
BuildRequires: openldap-devel
BuildRequires: openssl-devel
BuildRequires: perl(XML::Parser)
# for /usr/bin/iconv
BuildRequires: glibc-common
BuildRequires: make
%description
GQ is a graphical browser for LDAP directories and schemas.  Using GQ,
an administrator can search through a directory and modify objects
stored in that directory.

%prep
%autosetup -p1
for f in TODO AUTHORS ChangeLog ; do
    mv $f $f.iso88591
    iconv -f ISO-8859-1 -t UTF-8 -o $f $f.iso88591
    touch -r $f.iso88591 $f
    rm -f $f.iso88591
done

%build
export CFLAGS="%{optflags} -fcommon -Wno-incompatible-pointer-types -Wno-return-mismatch"
%configure --with-included-gettext      \
           --disable-update-mimedb      \
           --with-default-codeset=UTF-8 \
           --disable-scrollkeeper       \
           --enable-cache               \
           --enable-browser-dnd         \
           --with-kerberos-prefix=%{_prefix}/kerberos
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
desktop-file-install --delete-original      \
        --dir %{buildroot}%{_datadir}/applications          \
        %{buildroot}%{_datadir}/applications/%{name}.desktop
%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog NEWS README* TODO
%{_bindir}/%{name}
%{_datadir}/%{name}/%{name}.glade
%{_datadir}/pixmaps/%{name}/*.xpm
%{_datadir}/pixmaps/%{name}/*.png
%{_datadir}/mime/packages/%{name}-ldif.xml
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/omf/gq-manual
%{_datadir}/gnome/help/gq-manual
%{_datadir}/icons/hicolor/16x16/apps/ldap-*.png
%dir %{_datadir}/pixmaps/%{name}
%dir %{_datadir}/%{name}

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-54
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Oct 08 2024 Terje Rosten <terjeros@gmail.com> - 1.3.4-53
- Disable some warnings to build

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.3.4-52
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Feb 07 2023 Florian Weimer <fweimer@redhat.com> - 1.3.4-47
- Port configure script to C99

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.3.4-43
- Rebuilt with OpenSSL 3.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Oct 11 2020 Terje Rosten <terje.rosten@ntnu.no> - 1.3.4-40
- Switch to openssl-devel

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 12 2020 Terje Rosten <terje.rosten@ntnu.no> - 1.3.4-38
- Rebuild

* Sat Feb 01 2020 Terje Rosten <terje.rosten@ntnu.no> - 1.3.4-37
- Add GCC10 workaround

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Terje Rosten <terje.rosten@ntnu.no> - 1.3.4-32
- Minor clean up

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.3.4-30
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 18 2017 Terje Rosten <terje.rosten@ntnu.no> - 1.3.4-27
- Use compat openssl

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Rex Dieter <rdieter@fedoraproject.org> 1.3.4-23
- update scriptlets

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 23 2014 Tomáš Mráz <tmraz@redhat.com> - 1.3.4-20
- Rebuild for new libgcrypt

* Thu Nov 21 2013 Terje Røsten <terje.rosten@ntnu.no> - 1.3.4-19
- Try to avoid some more crash bugs.

* Mon Nov 11 2013 Terje Røsten <terje.rosten@ntnu.no> - 1.3.4-18
- Add errorchain patch

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Apr 12 2013 Jon Ciesla <limburgher@gmail.com> - 1.3.4-16
- Drop desktop vendor tag.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Mar 21 2012 Tom Callaway <spot@fedoraproject.org> - 1.3.4-13
- fix build against glib

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.3.4-11
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Feb 11 2010 Terje Røsten <terje.rosten@ntnu.no> - 1.3.4-9
- Add DSO patch

* Sun Nov 08 2009 Terje Røsten <terje.rosten@ntnu.no> - 1.3.4-8
- Add patch to build with krb5 1.7, thanks to Nalin for help

* Thu Nov 05 2009 Terje Røsten <terje.rosten@ntnu.no> - 1.3.4-7
- Build with kerberos support (bz #522095)
- Add patch to fix typo in kerberos code

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 1.3.4-6
- rebuilt with new openssl

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 16 2009 Tomas Mraz <tmraz@redhat.com> - 1.3.4-3
- rebuild with new openssl

* Mon Sep  1 2008 Terje Røsten <terje.rosten@ntnu.no> - 1.3.4-2
- adapt to new rpm patch macro policy

* Sun Feb 17 2008 Terje Røsten <terje.rosten@ntnu.no> - 1.3.4-1
- 1.3.4
- Drop infinite loop patch

* Tue Feb 12 2008 Terje Røsten <terje.rosten@ntnu.no> - 1.3.3-3
- Rebuild

* Mon Jan 21 2008 Terje Røsten <terje.rosten@ntnu.no> - 1.3.3-2
- Add patch from svn to fix infinite loop
- Adjust buildreq
- Fix scrollkeeper stuff

* Tue Jan  8 2008 Terje Røsten <terje.rosten@ntnu.no> - 1.3.3-1
- 1.3.3

* Thu Nov 29 2007 Terje Røsten <terje.rosten@ntnu.no> - 1.3.2-0.1.svn20071129
- 1.3.2 from svn 2007-11-29
- Drop lang pack
- Drop auth patch (now upstream)
- Fix some %%doc files
- Install help docs and new icons
- Add gtk-update-icon-cache to %%post

* Wed Nov  7 2007 Terje Røsten <terje.rosten@ntnu.no> - 1.2.2-8
- Rebuild for openssl and openldap

* Thu Sep  6 2007 Terje Røsten <terje.rosten@ntnu.no> - 1.2.2-7
- Add default-codeset to configure (fix bz #281431)

* Tue Aug 21 2007 Terje Røsten <terje.rosten@ntnu.no> - 1.2.2-6
- Tag problem

* Sun Aug 19 2007 Terje Røsten <terje.rosten@ntnu.no> - 1.2.2-5
- Fix license tag

* Mon Jun 25 2007 Terje Røsten <terje.rosten@ntnu.no> - 1.2.2-4
- Fix categories in desktop file

* Sun May 20 2007 Terje Røsten <terje.rosten@ntnu.no> - 1.2.2-3
- Add auth patch

* Mon Nov 20 2006 Terje Røsten <terje.rosten@ntnu.no> - 1.2.2-2
- Fix patch/source naming
- Add gettext to BuildReq
- Move %%post/%%postun
- Remove cp macro
- Add libgcrypt-devel to BuildReq

* Sun Nov 19 2006 Terje Røsten <terje.rosten@ntnu.no> - 1.2.2-1
- 1.2.2

* Sun Nov 19 2006 Terje Røsten <terje.rosten@ntnu.no> - 1.2.1-3
- Fix defattr
- Remove X-Fedora as category in desktop file
- libglade2-devel pulls in gtk2-devel and libxml2-devel in BuildReq
- Use perl modules, not perl package name in BuildReq
- Remove ldconfig from %%post
- Fix install of translations
- Remove some macros (rm, make and install)
- Fix mime: script and remove shared-mime-info from BuildReq
- Patch, not replace desktop file
- Switch icon to redhat-system_tools

* Sun Nov 12 2006 Terje Røsten <terje.rosten@ntnu.no> - 1.2.1-2
- Dont use %%makeinstall
- Some more buildreq: gnome-keyring-devel, libglade2-devel
- Add --disable-update-mimedb to configure

* Sun Oct 15 2006 Terje Røsten <terje.rosten@ntnu.no> - 1.2.1-1
- 1.2.1
- Add perl-XML-Parser to buildreq
- Translations broken, skip
- Fix mime stuff (stolen from planner.spec)

* Wed Sep 06 2006 Terje Røsten <terje.rosten@ntnu.no> - 1.2.0-1
- 1.2.0

* Sun Aug 06 2006 Terje Røsten <terje.rosten@ntnu.no> - 1.0.1-1
- 1.0.1

* Tue May 02 2006 Terje Røsten <terje.rosten@ntnu.no> - 1.0.0-4
- Fix source urls

* Tue May 02 2006 Terje Røsten <terje.rosten@ntnu.no> - 1.0.0-3
- More desktop file work

* Mon May 01 2006 Terje Røsten <terje.rosten@ntnu.no> - 1.0.0-2
- Proper desktop file handling
- Drop krb5-devel in buildrequires
- Add langpack

* Fri Apr 28 2006 Terje Røsten <terje.rosten@ntnu.no> - 1.0.0-1
- 1.0.0

* Mon Apr 10 2006 Terje Røsten <terje.rosten@ntnu.no> - 1.0-0.5.rc1
- 1.0-rc1

* Thu Apr 06 2006 Terje Røsten <terje.rosten@ntnu.no> - 1.0-0.4.beta2
- 1.0-beta2
- Remove patches now upstream
- Add libxml2-devel to build requires
- Include pix

* Mon Jun 20 2005 Terje Røsten <terje.rosten@ntnu.no> - 1.0-0.3.beta1
- Fix some rpmlint warnings

* Thu Jun 16 2005 Terje Røsten <terje.rosten@ntnu.no> - 1.0-beta1.0.2
- Build on fc4
- Add gcc4 patch
  <URL: http://sourceforge.net/tracker/index.php?func=detail&aid=1184399&group_id=3805&atid=103805> 

* Tue Mar 29 2005 Terje Røsten <terje.rosten@ntnu.no> - 1.0-beta1.0.1
- OpenLDAP 2.2 patch 
  <URL: http://sourceforge.net/mailarchive/forum.php?thread_id=6736116&forum_id=5986>
- build with: setarch i686 rpmbuild -ba --target=x86-64 ...

* Wed Jun 09 2004 Dag Wieers <dag@wieers.com> - 0.6.0-4
- Merged SPEC file with my version
- Changes to build on older releases
- Added improved desktop file

* Wed May 19 2004 Matthias Saou <http://freshrpms.net/> 1.0-0.beta1.1
- Update to 1.0beta1.
- Rebuild for Fedora Core 2

* Thu Nov 13 2003 Matthias Saou <http://freshrpms.net/> 0.6.0-3
- Rebuild for Fedora Core 1

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9
- Added new desktop entry
- Added find_lang usage

* Wed Jan 29 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.6.0

* Tue May 21 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.5.0

* Fri Feb 22 2002 Nalin Dahyabhai <nalin@redhat.com> 0.4.0-5
- rebuild

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Jun 19 2001 Nalin Dahyabhai <nalin@redhat.com>
- rebuild in new environment

* Fri Mar  2 2001 Nalin Dahyabhai <nalin@redhat.com>
- rebuild in new environment

* Tue Feb 20 2001 Nalin Dahyabhai <nalin@redhat.com>
- update to 0.4.0, fixes bugs #24160, #24161

* Wed Dec 27 2000 Nalin Dahyabhai <nalin@redhat.com>
- update to 0.3.1

* Fri Dec  1 2000 Nalin Dahyabhai <nalin@redhat.com>
- rebuild in new environment

* Fri Nov 10 2000 Nalin Dahyabhai <nalin@redhat.com>
- initial package
