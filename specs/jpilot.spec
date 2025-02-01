Summary: pilot desktop software
Name: jpilot
Version: 1.8.2
Release: 33%{?dist}
License: GPL-2.0-only
URL: https://www.jpilot.org/
Source0: https://www.jpilot.org/tarballs/jpilot-%{version}.tar.gz
Source1: jpilot.desktop

Patch0: jpilot-0.99.7-conf.patch
Patch1: jpilot-1.8.2-gcc10.patch
Patch2: jpilot-configure-c99.patch
Patch3: jpilot-callback-types.patch

BuildRequires: gcc
BuildRequires: gettext, pilot-link-devel, perl-XML-Parser, libgcrypt-devel
BuildRequires: intltool
BuildRequires: gtk2-devel >= 2.0.3
BuildRequires: pilot-link >= 0.12.5
BuildRequires: make
BuildRequires: ImageMagick
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

Requires: hicolor-icon-theme
# for XMP icons support
Requires: gdk-pixbuf2-modules-extra

ExcludeArch: s390, s390x

%description
J-Pilot is a desktop organizer application for the palm pilot that runs under
Linux.  It is similar in functionality to the one that 3com distributes for a
well known rampant legacy operating system.

%prep
%setup -q
%patch -P0 -p1 -b .confp
%patch -P1 -p1 -b .gcc10
%patch -P2 -p1
%patch -P3 -p1
iconv -f windows-1252 -t utf-8 AUTHORS >AUTHORS.aux
mv AUTHORS.aux AUTHORS

%build
%configure --disable-rpath --with-pilot-prefix=%{_prefix}

cd po
make clean
make update-po
cd ..

make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT libdir=%{_libdir}/jpilot/plugins install

mkdir -p $RPM_BUILD_ROOT%{_datadir}/jpilot/ \
         $RPM_BUILD_ROOT%{_datadir}/applications

ls -la jpilotrc*
install -m644 jpilotrc.* $RPM_BUILD_ROOT%{_datadir}/jpilot/
install -p empty/*.pdb $RPM_BUILD_ROOT%{_datadir}/jpilot/
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}

# install icon
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
convert icons/jpilot-icon3.xpm $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/jpilot.png

mkdir $RPM_BUILD_ROOT%{_metainfodir}
cat <<EOF > $RPM_BUILD_ROOT%{_metainfodir}/%{name}.appdata.xml
<?xml version="1.0" encoding="UTF-8"?>
<component type="desktop-application">
    <id>org.jpilot.JPilot</id>
    <name>J-Pilot</name>
    <summary>pilot desktop software</summary>
    <metadata_license>FSFAP</metadata_license>
    <project_license>GPL-2.0-only</project_license>
    <description>
        <p>
            J-Pilot is a desktop organizer application for the palm pilot that runs under
            Linux.  It is similar in functionality to the one that 3com distributes for a
            well known rampant legacy operating system.
        </p>
    </description>
    <launchable type="desktop-id">%{name}.desktop</launchable>
    <provides>
        <binary>jpilot</binary>
    </provides>
    <content_rating type="oars-1.1"/>
    <developer_name>Judd Montgomery</developer_name>
    <releases>
        <release version="%{version}" date="%(date +%F -r %{SOURCE0})" />
    </releases>
    <screenshots>
        <screenshot type="default">
            <caption>Datebook Screen</caption>
            <image>https://www.jpilot.org/screenshots/jpilot-datebook.png</image>
        </screenshot>
        <screenshot>
            <caption>Address Screen</caption>
            <image>https://www.jpilot.org/screenshots/jpilot-address.png</image>
        </screenshot>
        <screenshot>
            <caption>Todo Screen</caption>
            <image>https://www.jpilot.org/screenshots/jpilot-todo.png</image>
        </screenshot>
        <screenshot>
            <caption>Memo Screen</caption>
            <image>https://www.jpilot.org/screenshots/jpilot-memo.png</image>
        </screenshot>
    </screenshots>
    <url type="homepage">%{url}</url>
</component>
EOF
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_metainfodir}/%{name}.appdata.xml

%find_lang %name

%files -f %{name}.lang
%doc %{_docdir}/jpilot
%{_bindir}/*
%{_datadir}/jpilot
%{_datadir}/icons/hicolor/*/*/jpilot.*
%{_libdir}/%{name}
%{_mandir}/man1/*.*
%{_datadir}/applications/*
%{_metainfodir}/%{name}.appdata.xml

%changelog
* Thu Jan 30 2025 Nikola Forró <nforro@redhat.com> - 1.8.2-33
- Fix incompatible pointer type errors

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Dec 06 2024 Nikola Forró <nforro@redhat.com> - 1.8.2-31
- Require gdk-pixbuf2-modules-extra to enable loading XMP icons (#2330774)

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Aug 22 2023 Nikola Forró <nforro@redhat.com> - 1.8.2-27
- Added appstream file (thanks yselkowitz)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Mar 28 2023 Nikola Forró <nforro@redhat.com> - 1.8.2-25
- Fix License

* Tue Mar 28 2023 Nikola Forró <nforro@redhat.com> - 1.8.2-24
- Use SPDX license expression in License

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 19 2022 Florian Weimer <fweimer@redhat.com> - 1.8.2-22
- Port configure script to C99

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 23 2020 Nikola Forró <nforro@redhat.com> - 1.8.2-15
- fix build with GCC 10

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 09 2018 Nikola Forró <nforro@redhat.com> - 1.8.2-11
- resolves: #1598264
  fix BuildRequires for Keyring plugin

* Thu Jun 28 2018 Nikola Forró <nforro@redhat.com> - 1.8.2-10
- remove ldconfig from scriptlets

* Tue Feb 20 2018 Nikola Forró <nforro@redhat.com> - 1.8.2-9
- add missing gcc build dependency

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jun 11 2014 Peter Schiffer <pschiffe@redhat.com> - 1.8.2-1
- resolves: #1101955
  updated to 1.8.2

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr 11 2013 Peter Schiffer <pschiffe@redhat.com> - 1.8.1-6
- cleaned .spec file
- resolves: #925610
  added support for aarch64

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Sep 16 2011 Peter Schiffer <pschiffe@redhat.com> - 1.8.1-2
- added missing BuildRequires: intltool

* Tue Jul 12 2011 Ivana Hutarova Varekova <varekova@redhat.com> - 1.8.1-1
- update to 1.8.1

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 25 2011 Ivana Hutarova Varekova <varekova@redhat.com> - 1.8.0-5
- resolves: #667473
  fix the utf encoding

* Mon Jan  3 2011 Ivana Hutarova Varekova <varekova@redhat.com> - 1.8.0-4
- resolves: #663626
  rename the non-utf file name

* Mon Jan  3 2011 Ivana Hutarova Varekova <varekova@redhat.com> - 1.8.0-3
- Resolves: #665903
  Cannot delete entries from DateBook

* Thu Jun 24 2010 Ivana Hutarova Varekova <varekova@redhat.com> - 1.8.0-1
- update to 1.8.0

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 1.6.2-3
- rebuilt with new openssl

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild


* Sat Mar 28 2009 Ismael Olea <ismael@olea.org> - 1.6.2-1
- updated to 1.6.2
- removed jpilot-0.99.8-overfl.patch cause is included in upstream
- removed jpilot-0.99.9-trans.patch cause is included in upstream

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 17 2009 Tomas Mraz <tmraz@redhat.com> - 1.6.0-3
- rebuild with new openssl

* Tue Sep  2 2008 Ivana Varekova <varekova@redhat.com> - 1.6.0-2
- update patches

* Mon Jun 23 2008 Ivana Varekova <varekova@redhat.com> - 1.6.0-1
- update to 1.6.0

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.99.9-6
- Autorebuild for GCC 4.3

* Wed Dec  5 2007 Ivana Varekova <varekova@redhat.com> - 0.99.9-5
- Rebuild for openssl bump

* Thu Nov 22 2007 Ivana Varekova <varekova@redhat.com> - 0.99.9-4
- rebuilt

* Fri Feb 23 2007 Ivana Varekova <varekova@redhat.com> - 0.99.9-3
- incorporate package review feedback (#225951)

* Tue Nov 28 2006 Ivana Varekova <varekova@redhat.com> - 0.99.9-2
- add buildprereq (openssl-devel) (#214042)

* Tue Nov 28 2006 Ivana Varekova <varekova@redhat.com> - 0.99.9-1
- update to 0.99.9

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.99.8-7.1
- rebuild

* Tue Jun 27 2006 Ivana Varekova <varekova@redhat.com> 0.99.8-7
- fix translation problems (#196852)

* Mon May 29 2006 Ivana Varekova <varekova@redhat.com> 0.99.8-6
- add prereq (perl-XML-Parser) (#193405)

* Mon Apr 10 2006 Ivana Varekova <varekova@redhat.com> 0.99.8-5
- add upstream memory patch (#188425)
- add upstream sync patch

* Wed Mar 29 2006 Than Ngo <than@redhat.com> 0.99.8-4 
- rebuilt against pilot-link-0.11.8

* Mon Feb 27 2006 Ivana Varekova <varekova@redhat.com> - 0.99.8-3
- fix b183014 - jpilot startup problem

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 0.99.8-2.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 0.99.8-2.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Nov  9 2005 Ivana Varekova <varekova@redhat.com> 0.99.8-2
- rebuilt

* Mon Oct 31 2005 Ivana Varekova <varekova@redhat.com> 0.99.8-1
- update to 0.99.8

* Tue Aug 16 2005 Warren Togami <wtogami@redhat.com> 0.99.8-0.pre10.2
- rebuild for new cairo

* Thu Aug 11 2005 Ivana Varekova <varekova@redhat.com> 0.99.8-0.pre10.1
- new upstream version (0.99.8-pre10)

* Thu Jun  9 2005 Ivana Varekova <varekova@redhat.com> 0.99.8-0.pre9.1
- rebuilt new version (0.99.8-pre9)

* Fri May 06 2005 Ivana Varekova <varekova@redhat.com> 0.99.8-0.pre8.5
- fix typo (bug 157007)

* Wed Apr 27 2005 Radek Vokal <rvokal@redhat.com> 0.99.8-0.pre8.4
- fixed desktop file, show icon
- only one item in Office menu (overwrite package desktop file)

* Mon Apr 25 2005 Ivana Varekova <varekova@redhat.com> 0.99.8-0.pre8.3
- fix overflow problem (patch3 - patch from file from #153066 comment 12) 

* Wed Apr 20 2005 Ivana Varekova <varekova@redhat.com> 0.99.8-0.pre8.2
- rebuilt

* Wed Mar 30 2005 Than Ngo <than@redhat.com> 0.99.8-0.pre8.1
- 0.99.8-pre8
- cleanup specfile
- disable rpath
- update desktop file

* Fri Mar  4 2005 Ivana Varekova <varekova@redhat.com> 0.99.7-6
- rebuilt
 
* Fri Jan 21 2005 Ivana Varekova <varekova@redhat.com> 0.99.7-5
- fix problem with previous patch (problem with cb_cal_changed connection)
- fix problem with add_new_record (problem with cb_cal_changed connection)

* Mon Jan 10 2005 Ivana Varekova <varekova@redhat.com> 0.99.7-4
- fix part of bug #142520 - problem with Go to Today

* Mon Nov 22 2004 Ivana Varekova <varekova@redhat.com> 0.99.7-3
- fix bug #139377 - problem with x86_64

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Mar 03 2004 Than Ngo <than@redhat.com> 0.99.7-1
- update to 0.99.7

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Sep 03 2003 Than Ngo <than@redhat.com> 0.99.6-1
- 0.99.6

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Apr 15 2003 Michael K. Johnson <johnsonm@redhat.com> 0.99.5-2
- rebuild

* Tue Apr 15 2003 Michael K. Johnson <johnsonm@redhat.com> 0.99.5-1
- updated for new features and important bugfixes (like restoring
  the correct files)

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Tue Jan  7 2003 Nalin Dahyabhai <nalin@redhat.com> 0.99.2-10
- rebuild

* Sun Nov 10 2002 Than Ngo <than@redhat.com> 0.99.2-9
- unpackged files in buildroot

* Thu Aug 22 2002 Than Ngo <than@redhat.com> 0.99.2-8
- rebuild against new pilot-link

* Tue Aug  6 2002 Than Ngo <than@redhat.com> 0.99.2-7
- rebuild against pilot-link-0.11.2

* Wed Jul 24 2002 Than Ngo <than@redhat.com> 0.99.2-6
- desktop file issue (bug #69451)

* Thu Jul 18 2002 Than Ngo <than@redhat.com> 0.99.2-5
- rebuild against new pilot-link
- use desktop-file-install

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jun 19 2002 Than Ngo <than@redhat.com> 0.99.2-3
- Don't forcibly strip binaries

* Sun May 26 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed May 22 2002 Harald Hoyer <harald@redhat.de>
- 0.99.2
- added man pages

* Fri Apr 12 2002 Preston Brown <pbrown@redhat.com>
- fix icon in .desktop file

* Tue Mar 26 2002 Preston Brown <pbrown@redhat.com> 0.99-86
- fix Comment entry in desktop file

* Thu Feb 21 2002 Jeremy Katz <katzj@redhat.com> 0.99-85
- rebuild in new environment

* Fri Jan 25 2002 Than Ngo <than@redhat.com> 0.99-84
- rebuild in rawhide

* Thu Sep 20 2001 Than Ngo <than@redhat.com> 0.99-82
- rebuild against pilot-link

* Sun Aug  5 2001 Than Ngo <than@redhat.com>
- fix bug #50586

* Mon Jul 16 2001 Trond Eivind Glomsrød <teg@redhat.com>
- s/Copyright/License/
- Improve langification
- mark desktop file as config(noreplace)
- move dependency on ldconfig from requires to prereq

* Sat Jul  7 2001 Tim Powers <timp@redhat.com>
- languify to satisfy rpmlint

* Fri Jun 29 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- delete Packager: line in spec file

* Tue Jun 26 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- exclude s390,s390x

* Fri Jun 22 2001 Preston Brown <pbrown@redhat.com>
- build for dist

* Thu Feb  8 2001 Tim Powers <timp@redhat.com>
- updated to 0.99, bug fixes/feature enhancements

* Tue Dec 19 2000 Tim Powers <timp@redhat.com>
- rebuilt. For some reason buildsystem made the dirs 777 again. Now
  it's fine.

* Fri Dec 15 2000 Tim Powers <timp@redhat.com>
- fixd bad dir perms for ~/.jpilot (was creating them as 777, needs to
  be 700 for security purposes
- no devel package, was a waste to do that when only two files are included
- use %%makeinstall, and predefined macros for dirs so that if
  %%configure and %%makeinstall change it can be picked up without
  further editing of the files section
- changed Copyright, it's GPL'ed
 
* Thu Nov 23 2000 Than Ngo <than@redhat.com>
- add missing plugin library and jpilot-dump
- made devel package
- clean up spec file

* Mon Jul 24 2000 Prospector <prospector@redhat.com>
- rebuilt

* Mon Jul 10 2000 Tim Powers <timp@redhat.com>
- rebuilt

* Fri Jun 30 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Mon May 15 2000 Tim Powers <timp@redhat.com>
- using applnk now instead of a GNOME specific menu entry
- built for 7.0

* Wed Apr 19 2000 Tim Powers <timp@redhat.com>
- added desktop entry for GNOME

* Wed Apr 12 2000 Tim Powers <timp@redhat.com>
- updated to 0.98.1

* Mon Apr 3 2000 Tim Powers <timp@redhat.com>
- updated to 0.98
- bzipped source
- using percent configure instead of ./configure
- quiet setup
- minor spec file cleanups

* Tue Dec 21 1999 Tim Powers <timp@redhat.com>
- changed requires

* Mon Oct 25 1999 Tim Powers <timp@redhat.com>
- changed group to Applications/Productivity
- first build
