%global	pidgin_version 2.0.0

Name:		pidgin-libnotify
Version:	0.14
Release:	37%{?dist}
Summary:	Libnotify Pidgin plugin 

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://gaim-libnotify.sourceforge.net/

Source0:	http://downloads.sourceforge.net/gaim-libnotify/%{name}-%{version}.tar.gz
Source1:        pidgin-libnotify.metainfo.xml
Patch0:		pidgin-libnotify-fix-show-button.patch
Patch1:		pidgin-libnotify-0.14-libnotify-0.7.0.patch

# Fix typo in German translation
# https://bugzilla.redhat.com/show_bug.cgi?id=654111
Patch2:		pidgin-libnotify-german-translation-typo.patch

BuildRequires: make
BuildRequires:	gettext
BuildRequires:	libnotify-devel >= 0.3.2
BuildRequires:	perl(XML::Parser)
BuildRequires:	pidgin-devel >= %{pidgin_version}
BuildRequires:	intltool
# For AppData verification
BuildRequires:  libappstream-glib

# In order to enable aarch64 support a more recent autotools
# needs to be used to build this package
# https://bugzilla.redhat.com/show_bug.cgi?id=926114
BuildRequires:  autoconf automake libtool

Requires:	pidgin >= %{pidgin_version}

## Provides a proper upgrade path from gaim-libnotify installations.
Provides:	gaim-libnotify = %{version}-%{release} 
Obsoletes:	gaim-libnotify < %{version}-%{release}

%description
This is a plugin for the open-source Pidgin instant messaging client that uses
libnotify to display graphic notifications of new messages and other events
such as a buddy signing on or off.


%prep
%setup -q -n "%{name}-%{version}"

autoreconf -i --force

%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p0


%build
%configure --disable-static --disable-deprecated
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}%{_datadir}/appdata/
cp -p %{SOURCE1} %{buildroot}%{_datadir}/appdata/
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/*.metainfo.xml
%find_lang %{name}


%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING NEWS TODO
%exclude %{_libdir}/purple-2/*.la
%{_libdir}/purple-2/%{name}.so
%{_datadir}/appdata/%{name}.metainfo.xml


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.14-36
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 09 2017 Michael Cronenworth <mike@cchtml.com> - 0.14-18
- Add AppData metainfo file (RHBZ#1295181)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat May  4 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.14-12
- Add support for aarch64 (RHBZ #926333)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Aug 27 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.14-10
- Fix typo in German translation (RHBZ #654111)
- Cleanup of unneeded RPM tags

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.14-7
- Rebuild for new libpng

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 08 2010 Stu Tomlinson <stu@nosnilmot.com> 0.14-5
- Added a patch to build against libnotify 0.7.0

* Fri Jun 11 2010 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.14-4
- Added a patch from Adel Gadllah which fixes the 'Show' button in notifications (RHBZ #562575)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Dec 20 2008 Erik van Pienbroek <erik-fedora@vanpienbroek.nl> - 0.14-1
- Update to version 0.14 (BZ #477267)
- Add BR: intltool

* Thu Aug 28 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.13-4
- fix license tag

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.13-3
- Autorebuild for GCC 4.3

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 0.13-2
- Rebuild for selinux ppc32 issue.

* Sun Jul 01 2007 Peter Gordon <peter@thecodergeek.com> - 0.13-1
- Update to new upstream release (0.13).
- Drop renamed-to-pidgin patch (fixed upstream):
  - renamed-to-pidgin.patch
- Alphabetize BuildRequires (aesthetic-only change).

* Fri May 18 2007 Peter Gordon <peter@thecodergeek.com> - 0.12-7
- Make Provides/Obsoletes tags use macros for the Version/Release of the
  upgrade.

* Fri May 18 2007 Peter Gordon <peter@thecodergeek.com> - 0.12-6
- Package renamed to pidgin-libnotify.
- Reword earlier %%changelog entry.

* Fri May 18 2007 Warren Togami <wtogami@redhat.com> - 0.12-5
- buildreq gettext (#240604)

* Sat May 12 2007 Peter Gordon <peter@thecodergeek.com> - 0.12-4
- Gaim has been renamed to Pidgin: adjust the sources accordingly.  
- Add patch based on the Arch Linux packaging to make the sources and build
  scripts properly use the new Pidgin/Libpurple nomenclature of what was
  formerly called Gaim.
  + renamed-to-pidgin.patch
- Drop gtk2-devel build dependency (pulled in by libnotify-devel).
- Update Source0 to point to simpler SourceForge URL.

* Sun Dec 10 2006 Peter Gordon <peter@thecodergeek.com> - 0.12-3
- Bump EVR to fix CVS tagging issue

* Sun Dec 10 2006 Peter Gordon <peter@thecodergeek.com> - 0.12-2
- Shorten line lengths in %%description (and rewrite it a bit)
- Add gaim runtime requirement so that the parent directory of the plugin in
  %%{_libdir}/gaim is properly owned
- Removed unnecessary perl(XML::Parser) and gettext BuildRequires
- Add TODO to %%doc

* Sat Dec 09 2006 Peter Gordon <peter@thecodergeek.com> - 0.12-1
- Initial packaging for Fedora Extras
