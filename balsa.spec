%define config_opts --prefix=%{_prefix} --sysconfdir=%{_sysconfdir} --mandir=%{_mandir} --libdir=%{_libdir} --bindir=%{_bindir} --includedir=%{_includedir} --datadir=%{_datadir} --disable-more-warnings --with-gss --with-spell-checker=gtkspell  --without-gnome --with-html-widget=webkit2 --with-libsecret --disable-static

Name:           balsa
Version:        2.6.4
Release:        2%{?dist}
Summary:        Mail Client

License:        GPLv2+
URL:            https://pawsa.fedorapeople.org/balsa/
Source0:        https://pawsa.fedorapeople.org/balsa/%{name}-%{version}.tar.xz

#BuildRequires: gnome-vfs2-devel
BuildRequires: desktop-file-utils
BuildRequires: enchant-devel
BuildRequires: gettext
BuildRequires: gmime30-devel >= 3.2.6
BuildRequires: gnutls-devel
BuildRequires: gnome-doc-utils
BuildRequires: gpgme-devel
BuildRequires: gtkspell3-devel
BuildRequires: intltool
BuildRequires: krb5-devel
BuildRequires: libical-devel
BuildRequires: libsecret-devel
BuildRequires: libtool
BuildRequires: webkitgtk4-devel
BuildRequires: yelp-tools
BuildRequires: make

%description
Balsa is a GNOME email client which supports mbox, maildir, and mh
local mailboxes, and IMAP4 and POP3 remote mailboxes. Email can be
sent via sendmail or SMTP. Optional multithreading support allows for
non-intrusive retrieval and sending of mail. A finished GUI similar to
that of the Eudora email client supports viewing images inline, saving
message parts, viewing headers, adding attachments, moving messages,
and printing messages.

%prep
%setup -q

# Needed for aclocal to work
#mkdir m4

%build

#autoreconf -f -i
%configure %{config_opts}

make %{?_smp_mflags}

%install
%make_install

desktop-file-install $RPM_BUILD_ROOT%{_datadir}/applications/org.desktop.Balsa.desktop \
%if (0%{?fedora} && 0%{?fedora} < 19) || (0%{?rhel} && 0%{?rhel} < 7)
        --vendor fedora \
%endif
        --add-category=Email \
        --remove-category=Application \
        --dir=$RPM_BUILD_ROOT%{_datadir}/applications \

%find_lang %{name}

%files -f %{name}.lang
%doc README.md COPYING ChangeLog NEWS TODO AUTHORS HACKING docs/mh-mail-HOWTO
%doc docs/vconvert.awk docs/pine2vcard
%{_bindir}/balsa
%{_bindir}/balsa-ab
%{_libdir}/balsa/libhtmlfilter.so
%{_datadir}/applications/*.desktop
%{_datadir}/balsa/
%{_datadir}/help/C/balsa/
%{_datadir}/help/cs/balsa/
%{_datadir}/help/de/balsa/
%{_datadir}/help/el/balsa/
%{_datadir}/help/es/balsa/
%{_datadir}/help/fr/balsa/
%{_datadir}/help/sl/balsa/
%{_datadir}/pixmaps/gnome-balsa2.png
%{_datadir}/sounds/balsa/
%{_datadir}/metainfo/balsa.appdata.xml
%{_mandir}/man1/balsa.1*
%config(noreplace) %{_sysconfdir}/sound/events/balsa.soundlist

%changelog
* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Sep 20 2022 Pawel Salek <pawsa0@gmail.com> - 2.6.4-1
- Update to upstream balsa-2.6.4

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 18 2021 Pawel Salek <pawsa0@gmail.com> - 2.6.3-1
- Update to upstream balsa-2.6.3

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 21 2020 Pawel Salek <pawsa0@gmail.com> - 2.6.2-1
- Update to upstream balsa-2.6.2

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 10 2020 Pawel Salek <pawsa0@gmail.com> - 2.6.1-1
- Update to upstream balsa-2.6.1.

* Sun Apr 12 2020 Pawel Salek <pawsa0@gmail.com> - 2.6.0-1
- Update to upstream balsa-2.6.0.
- Remove --with-gpgme as gpg is fixed build requirement now.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Oct 19 2019 Pawel Salek <pawsa0@gmail.com> - 2.5.9-1
- Update to upstream balsa-2.5.9

* Wed Oct 09 2019 Pawel Salek <pawsa0@gmail.com> - 2.5.7-3
- Drop dependency on libesmtp

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 25 2019 Pawel Salek <pawsa0@gmail.com> - 2.5.7-1
- Update to upstream balsa-2.5.7

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 23 2018 Pawel Salek <pawsa0@gmail.com> - 2.5.6-3
- Remove obsolete compile options

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 09 2018 Pawel Salek <pawsa0@gmail.com> - 2.5.6-1
- Update to upstream balsa-2.5.6

* Wed Mar 14 2018 Pawel Salek <pawsa0@gmail.com> - 2.5.5-1
- Update to upstream balsa-2.5.5

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.5.3-7
- Remove obsolete scriptlets

* Wed Jan 03 2018 Lubomir Rintel <lkundrak@v3.sk> - 2.5.3-6
- Drop NetworkManager-lib BR

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May 04 2017 Pawel Salek <pawsa0@gmail.com> - 2.5.3-3
- build against webkit2

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 10 2016 Pawel Salek <pawsa0@gmail.com> - 2.5.3-1
- Update to upstream balsa-2.5.3; fix build against openssl-1.1.0

* Sat Dec 10 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.5.2-4
- Rebuild for gpgme 1.18

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 30 2015 Pawel Salek <salek@kth.se> - 2.5.2-1
- update to upstream 2.5.2

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Apr 28 2013 Pawel Salek <salek@kth.se> - 2.5.1-1
- update to upstream 2.5.1

* Thu Feb 28 2013 Pawel Salek <salek@kth.se> - 2.5.0-1
- update to upstream 2.5.0

* Fri Feb 15 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 2.4.12-4
- Fix FTBFS
- Conditionalize vendor so it will still be present on F18 or less

* Sun Feb 10 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 2.4.12-3
- remove vendor tag from desktop file. https://fedorahosted.org/fpc/ticket/247
- clean up spec to follow current guidelines

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 20 2012 Pawel Salek <salek@kth.se> - 2.4.12-1
- update to upstream 2.4.12

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov 22 2011 Pawel Salek <salek@kth.se> - 2.4.11-1
- update to upstream 2.4.11

* Tue Sep 20 2011 Pawel Salek <pawsa@ice> - 2.4.10-1
- update to upstream 2.4.10

* Sat Mar 26 2011 Pawel Salek <salek@kth.se> - 2.4.9-6
- use webkit as HTML widget.

* Fri Feb 25 2011 Pawel Salek <salek@kth.se> - 2.4.9-5
- disable gnome libs and HTML support until it stabilizes.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 28 2010 Pawel Salek <salek@kth.se> - 2.4.9-3
- rebuild against new gtk and gtkhtml.

* Tue Dec 07 2010 Pawel Salek <salek@kth.se> - 2.4.9-2
- rebuild against libesmtp-1.0.6

* Fri Nov 19 2010 Pawel Salek <salek@kth.se> - 2.4.9-1
- update to upstream 2.4.9

* Sat Aug 21 2010 Pawel Salek <salek@kth.se> - 2.4.8-1
- update to upstream 2.4.8

* Sat Feb 20 2010 Pawel Salek <salek@kth.se> - 2.4.7-2
- add a partial gmime-2.5.1 port patch, remove gpgme support for now.

* Sat Feb 13 2010 Pawel Salek <salek@kth.se> - 2.4.7-1
- update to upstream 2.4.7

* Mon Feb  1 2010 Pawel Salek <salek@kth.se> - 2.4.6-3
- We use libunique - GNOME_Balsa.server is redundant now.

* Mon Feb  1 2010 Pawel Salek <salek@kth.se> - 2.4.6-1
- update to upstream 2.4.6

* Wed Dec 30 2009 Pawel Salek <salek@kth.se> - 2.4.2-1
- update to upstream 2.4.2

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 2.4.1-2
- rebuilt with new openssl

* Sun Aug 09 2009 Pawel Salek <salek@kth.se> - 2.4.1-1
- update to upstream 2.4.1.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu May 28 2009 Pawel Salek <salek@kth.se> - 2.4.0-1
- update to upstream 2.4.0.

* Thu Mar 19 2009 Lubomir Rintel <lkundrak@v3.sk> - 2.3.28-4
- Patch for newer gmime
- Fix BRs

* Mon Mar  2 2009 Pawel Salek <pawsa@theochem.kth.se> - 2.3.28-3
- Add autoreconf, mock on devel does not work right now.

* Mon Mar  2 2009 Pawel Salek <pawsa@theochem.kth.se> - 2.3.28-2
- specify a correct patch path strip argument.

* Mon Mar  2 2009 Pawel Salek <pawsa@theochem.kth.se> - 2.3.28-1
- upgrade to 2.3.28. Fix bug 487780.

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.26-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 15 2009 Tomas Mraz <tmraz@redhat.com> - 2.3.26-4
- rebuild with new openssl

* Thu Dec 18 2008 Pawel Salek <pawsa at theochem.kth.se> - 2.3.26-3
- Port to gmime-2.4 using http://bugzilla.gnome.org/537507 

* Sun Sep 07 2008 Pawel Salek <pawsa at theochem.kth.se> - 2.3.26-2
- Use deprecated GTK+ interface until upstream fixes their bugs.

* Sun Sep 07 2008 Pawel Salek <pawsa at theochem.kth.se> - 2.3.26-1
- update to upstream 2.3.26.

* Mon Jul 14 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.3.25-2
- fix license tag

* Wed Jun 18 2008 Pawel Salek <pawsa at theochem.kth.se> - 2.3.25-1
- update to upstream 2.3.25.

* Sat May 31 2008 Pawel Salek <pawsa at theochem.kth.se> - 2.3.24-1
- update to upstream 2.3.24.

* Mon Mar 31 2008 Pawel Salek <pawsa at theochem.kth.se> - 2.3.23-1
- update to upstream 2.3.23.

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.3.22-2
- Autorebuild for GCC 4.3

* Tue Dec 25 2007 Pawel Salek <pawsa at theochem kth se> - 2.3.22-1
- Update to upstream 2.3.22.

* Sat Dec 08 2007 Pawel Salek <pawsa@theochem.kth.se> - 2.3.21-1
- update to 2.3.21 and rebuild.

* Thu Dec 06 2007 Release Engineering <rel-eng at fedoraproject dot org> - 2.3.20-2
 - Rebuild for deps

* Fri Sep  7 2007 Pawel Salek <pawsa@theochem.kth.se> - 2.3.20-1
- update to upstream 2.3.20.

* Sat Aug 25 2007 Pawel Salek <pawsa@theochem.kth.se> - 2.3.19-1
- Update to upstream 2.3.19.

* Wed Aug 22 2007 Pawel Salek <pawsa@theochem.kth.se> - 2.3.18-4
- Fix parallel build.

* Wed Aug 22 2007 Pawel Salek <pawsa@theochem.kth.se> - 2.3.18-1
- update to upstream 2.3.18.

* Sat Aug 11 2007 Pawel Salek <pawsa@theochem.kth.se> - 2.3.17-2
- work around build problem.

* Wed Jul  4 2007 Pawel Salek <pawsa@theochem.kth.se> - 2.3.17-1
- update to upstream 2.3.17.

* Sun May 27 2007 Pawel Salek <pawsa@theochem.kth.se> - 2.3.16-1
- update to upstream 2.3.16.

* Sat May  5 2007 Pawel Salek <pawsa@theochem.kth.se> - 2.3.15-3
- fix HTML+print interaction.

* Tue May  1 2007 Pawel Salek <pawsa@theochem.kth.se> - 2.3.15-1
- update to upstream 2.3.15.

* Tue Dec 12 2006 Pawel Salek <pawsa@theochem.kth.se> - 2.3.14-1
- update to upstream version 2.3.14.

* Mon Sep 11 2006 Pawel Salek <pawsa@theochem.kth.se> - 2.3.13-2
- rebuild for FC6.

