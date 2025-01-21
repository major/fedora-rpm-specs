%undefine __cmake_in_source_build

Name:           xiphos
Version:        4.2.1
Release:        27%{?dist}
Summary:        Bible study and research tool
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://xiphos.org/
Source0:        https://github.com/crosswire/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
Patch0:         glib_version.patch
Patch1:         minizip.patch
BuildRequires:  biblesync-devel >= 2.0.1-3
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  dbus-glib-devel
BuildRequires:  docbook-utils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gtk3-devel
BuildRequires:  gtkhtml3-devel
BuildRequires:  intltool
BuildRequires:  itstool
BuildRequires:  libappstream-glib
BuildRequires:  libuuid-devel
BuildRequires:  minizip-ng-compat-devel
BuildRequires:  rarian-compat
BuildRequires:  sword-devel >= 1.8
BuildRequires:  util-linux
BuildRequires:  webkit2gtk3-devel
BuildRequires:  yelp-tools
BuildRequires:  libzip-devel
Requires:       yelp
Obsoletes:      xiphos-gtk2 < 4.1
Obsoletes:      xiphos-gtk3 < 4.1
Obsoletes:      xiphos-common < 4.1

%if 0%{?rhel} > 0 && 0%{?rhel} <= 7
ExcludeArch: ppc64
%endif

%description
Xiphos is a Bible study tool written for Linux,
UNIX, and Windows under the GNOME toolkit, offering a rich and featureful
environment for reading, study, and research using modules from The SWORD
Project and elsewhere.

%prep
%setup -q
rm -rf src/biblesync
%patch -P0 -p0
%patch -P1 -p1

%build
export CFLAGS="$CFLAGS -fPIC"
export CXXFLAGS="$CXXFLAGS -fPIC"
%ifarch %{power64}
 CFLAGS="$CFLAGS -D__SANE_USERSPACE_TYPES__"
 CXXFLAGS="$CXXFLAGS -D__SANE_USERSPACE_TYPES__"
%endif
export CXXFLAGS
export CFLAGS

LDFLAGS='%{?__global_ldflags}' \
%cmake -DGTKHTML:BOOL=ON \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    %{nil}
%cmake_build

%install
%cmake_install

desktop-file-install --delete-original         \
    --add-category=X-Bible                     \
    --add-category=X-Religion                  \
    --dir=%{buildroot}%{_datadir}/applications \
    --copy-name-to-generic-name                \
    %{buildroot}%{_datadir}/applications/xiphos.desktop

# package docs with macro
rm -frv %{buildroot}%{_docdir}/%{name}

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog README.md RELEASE-NOTES TODO
%license COPYING
%{_bindir}/xiphos
%{_bindir}/xiphos-nav
%{_datadir}/appdata/xiphos.appdata.xml
%{_datadir}/applications/xiphos.desktop
%{_datadir}/icons/hicolor/scalable/apps/xiphos.svg
%{_datadir}/xiphos/
%{_datadir}/help/C/xiphos
%{_datadir}/help/fa/xiphos
%{_datadir}/help/fr/xiphos
%{_datadir}/help/it/xiphos
%{_mandir}/man1/%{name}.1.gz
%{_mandir}/man1/%{name}-nav.1.gz

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Dec 08 2024 Pete Walter <pwalter@fedoraproject.org> - 4.2.1-26
- Rebuild for ICU 76

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 4.2.1-25
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Feb 01 2024 Pete Walter <pwalter@fedoraproject.org> - 4.2.1-23
- Rebuild for ICU 74

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 04 2023 Lukas Javorsky <ljavorsk@redhat.com> - 4.2.1-21
- Rebuilt for minizip-ng transition Fedora change
- Fedora Change: https://fedoraproject.org/wiki/Changes/MinizipNGTransition

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 František Zatloukal <fzatlouk@redhat.com> - 4.2.1-19
- Rebuilt for ICU 73.2

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 31 2022 Pete Walter <pwalter@fedoraproject.org> - 4.2.1-17
- Rebuild for ICU 72

* Tue Nov 15 2022 Sandro Mani <manisandro@gmail.com> - 4.2.1-16
- Rebuild (minizip-ng)

* Mon Aug 01 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 4.2.1-15
- Rebuilt for ICU 71.1

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 18 2022 Greg Hellings <greg.hellings@gmail.com> - 4.2.1-13
- Add minizip patch to fix FTBFS

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu May 20 2021 Pete Walter <pwalter@fedoraproject.org> - 4.2.1-10
- Rebuild for ICU 69

* Thu Apr 22 2021 Greg Hellings <greg.hellings@gmail.com> - 4.2.1-9
- Added patch for glib version incompatibility

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 14 2020 Greg Hellings <greg.hellings@gmail.com> - 4.2.1-7
- Force rebuild against SWORD 1.9.0

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 11 2020 Greg Hellings <greg.hellings@gmail.com> - 4.2.1-4
- Remove libglade2 from BR

* Sun May 17 2020 Pete Walter <pwalter@fedoraproject.org> - 4.2.1-3
- Rebuild for ICU 67

* Sat May 16 2020 Pete Walter <pwalter@fedoraproject.org> - 4.2.1-2
- Rebuild for ICU 67

* Thu May 14 2020 Greg Hellings <greg.hellings@gmail.com> - 4.2.1-1
- Upstream release 4.2.1
- Remove patches
- Remove GConf2 and libgsf dependencies
- Removed Xiphos.ogg doc
- Added Italian help translation

* Thu Apr 02 2020 Greg Hellings <greg.hellings@gmail.com> - 4.1.0-12
- Added fix_nasb.patch

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 01 2019 Pete Walter <pwalter@fedoraproject.org> - 4.1.0-10
- Rebuild for ICU 65

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Pete Walter <pwalter@fedoraproject.org> - 4.1.0-7
- Rebuild for ICU 63

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 4.1.0-6
- Rebuild with fixed binutils

* Thu Jul 26 2018 Greg Hellings <greg.hellings@gmail.com> - 4.1.0-5
- Change to CMake build process
- Add several BRs
- Include patch from upstream that adds CMake (TBR 4.1.1 or later)

* Thu Jul 12 2018 Greg Hellings <greg.hellings@gmail.com> - 4.1.0-2
- Rebuild for SWORD 1.8.1-7

* Tue Jul 10 2018 Pete Walter <pwalter@fedoraproject.org> - 4.1.0-3
- Rebuild for ICU 62

* Mon May 14 2018 Greg Hellings <greg.hellings@gmail.com> - 4.1.0-1
- Upstream release 4.1.0

* Mon Apr 30 2018 Pete Walter <pwalter@fedoraproject.org> - 4.0.7-6
- Rebuild for ICU 61.1

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Greg Hellings <greg.hellings@gmail.com> - 4.0.7-4
- Rebuild for SWORD 1.8

* Fri Jan 12 2018 Tomas Popela <tpopela@redhat.com> - 4.0.7-3
- Adapt to the webkitgtk4 rename

* Thu Nov 30 2017 Pete Walter <pwalter@fedoraproject.org> - 4.0.7-2
- Rebuild for ICU 60.1

* Mon Sep 25 2017 Greg Hellings <greg.hellings@gmail.com> - 4.0.7-1
- Upstream release 4.0.7

* Sat Aug 12 2017 Greg Hellings <greg.hellings@gmail.com> - 4.0.6-1
- Upstream release 4.0.6
- Addresses display bug BZ1448623

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 11 2017 Greg Hellings <greg.hellings@gmail.com> - 4.0.5-2
- Fix post install scripts for upgrades
- Added obsoletes for xiphos-common to stop collision issues
- Partially addresses BZ1448623

* Sun Apr 23 2017 Greg Hellings <greg.hellings@gmail.com> - 4.0.5-1
- Upstream version 4.0.5
- Added extra Provides lines
- Updated URL for source tarball

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 09 2017 Greg Hellings <greg.hellings@gmail.com> - 4.0.4-6
- Dropped GTK2 support
- Dropped WebKitGTK support

* Mon Sep 19 2016 Greg Hellings <greg.hellings@gmail.com> - 4.0.4-5
- Moved to WebKit2

* Wed Jun 01 2016 Greg Hellings <greg.hellings@gmail.com> - 4.0.4-4
- Moved appdata and desktop files to gtk2 build, allowing
  proper auto-discovery by gnome-software. BZ#1330096

* Mon Feb 08 2016 Greg Hellings <greg.hellings@gmail.com> - 4.0.4-3
- Exclude ppc64 from EPEL for lack of gtkhtml3

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep 01 2015 Greg Hellings <greg.hellings@gmail.com> - 4.0.4-1
- Update to new upstream version

* Fri Aug 07 2015 Greg Hellings <greg.hellings@gmail.com> - 4.0.3-1
- Update to new upstream version
- Fix major bug with large (> 200) language sets in a repository

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 15 2015 Greg Hellings <greg.hellings@gmail.com> 4.0.2-1
- Version bump - major upstream memory bugs

* Wed Apr 08 2015 Greg Hellings <greg.hellings@gmail.com> 4.0.1-1
- Version bump

* Fri Jan 16 2015 Greg Hellings <greg.hellings@gmail.com> 4.0.0-4
- Added GTK compat so that we can link against GTK2 all the way

* Wed Dec 24 2014 Greg Hellings <greg.hellings@gmail.com> 4.0.0-3
- New upstream tarball (same version)

* Wed Dec 24 2014 Greg Hellings <greg.hellings@gmail.com> 4.0.0-2
- Updated xiphos-compat obsoletes

* Tue Dec 23 2014 Greg Hellings <greg.hellings@gmail.com> 4.0.0-1
- New upstream version
- Removed obsolete build flags
- Removed references to GnomeSword (> 6 years old, version 2.x name)
- Added biblesync-devel minimum version

* Tue Dec 16 2014 Greg Hellings <greg.hellings@gmail.com> 3.2.3j-3
- Added workaround for waf insufficiently isolating multi-build

* Wed Dec 10 2014 Greg Hellings <greg.hellings@gmail.com> 3.2.3j-2
- Obsoleted old Xiphos unary package

* Tue Dec 09 2014 Greg Hellings <greg.hellings@gmail.com> 3.2.3j-1
- Add installation of GTK2 and GTK3 versions in parallel

* Thu Oct 16 2014 Karsten Hopp <karsten@redhat.com> 3.2.2-2
- fix ppc64* builds

* Mon Aug 25 2014 Greg Hellings <greg.hellings@gmail.com> - 3.2.2-1
- New upstream version

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Aug 02 2014 Christopher Meng <rpm@cicku.me> - 3.2.1-2
- Build against GTK+3

* Tue Jun 10 2014 Greg Hellings <greg.hellings@gmail.com> - 3.2.1-1
- New upstream release

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 16 2014 Greg Hellings <greg.hellings@gmail.com> - 3.2.0-1
- New upstream release

* Wed Jan 29 2014 Greg Hellings <greg.hellings@gmail.com> - 3.1.6-2
- Removed GTK3 in favor of GTK2, as GTK3 is known to be buggy for this release

* Wed Jan 29 2014 Deji Akingunola <dakingun@gmail.com> - 3.1.6-1
- Update to version 3.1.6

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Feb 22 2012 Deji Akingunola <dakingun@gmail.com> - 3.1.5-1
- Update to version 3.1.5

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 3.1.4-7
- Rebuild for new libpng

* Mon Jun 27 2011 Deji Akingunola <dakingun@gmail.com> - 3.1.4-6
- Update to svn snapshot from the webkit branch for gtk3 support

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Feb 01 2011 Deji Akingunola <dakingun@gmail.com> - 3.1.4-4
- Rebuild for newer gtkhtml3

* Thu Dec 23 2010 Deji Akingunola <dakingun@gmail.com> - 3.1.4-3
- Apply patch to bump the upper limit of allowable xulrunner version

* Wed Dec 22 2010 Deji Akingunola <dakingun@gmail.com> - 3.1.4-2
- Rebuild for newer xulrunner and gtkhtml3

* Sun Oct 17 2010 Deji Akingunola <dakingun@gmail.com> - 3.1.4-1
- Update to 3.1.4

* Fri Jul 16 2010 Deji Akingunola <dakingun@gmail.com> - 3.1.3-3
- Rebuild (with a small patch) for gtkhtml3-3.31.5.

* Fri May 28 2010 Deji Akingunola <dakingun@gmail.com> - 3.1.3-2
- Apply Karl Kleinpaste patch to fix the jump-to-anchor failure.

* Tue Mar 23 2010 Deji Akingunola <dakingun@gmail.com> - 3.1.3-1
- New upstream version

* Mon Mar 15 2010 Deji Akingunola <dakingun@gmail.com> - 3.1.2-4
- Backport upstream patch to fix bugs detected by ABRT caused by empty settings.xml file.

* Sat Mar 13 2010 Deji Akingunola <dakingun@gmail.com> - 3.1.2-3
- Backport upstream patch to fix bug with xulrunner-1.9.2.

* Sun Mar 07 2010 Deji Akingunola <dakingun@gmail.com> - 3.1.2-2
- Rebuild with current xulrunner to fix crashes.

* Tue Dec 29 2009 Deji Akingunola <dakingun@gmail.com> - 3.1.2-1
- New upstream version

* Mon Aug 10 2009 Deji Akingunola <dakingun@gmail.com> - 3.1.1-1
- New upstream version

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon May 18 2009 Deji Akingunola <dakingun@gmail.com> - 3.1-1
- Update to the 3.1 release

* Tue Mar 10 2009 Deji Akingunola <dakingun@gmail.com> - 3.0.1-2
- Couple of fixes from package review (Nils Philippsen)

* Fri Feb 20 2009 Deji Akingunola <dakingun@gmail.com> - 3.0.1-1
- Update to the bugfix 3.0.1 release

* Sun Feb 08 2009 Deji Akingunola <dakingun@gmail.com> - 3.0.0-1
- Gnomesword renamed to Xiphos
- First release under the new name

* Thu Nov 20 2008 Deji Akingunola <dakingun@gmail.com> - 2.4.1-1
- Update to 2.4.1

* Sun Sep 21 2008 Deji Akingunola <dakingun@gmail.com> - 2.4.0-1
- Update to 2.4.0

* Sat Aug 02 2008 Deji Akingunola <dakingun@gmail.com> - 2.3.6-2
- Package the 'RELEASE-NOTES'

* Sat Aug 02 2008 Deji Akingunola <dakingun@gmail.com> - 2.3.6-1
- Update to 2.3.6

* Thu Jul 24 2008 Deji Akingunola <dakingun@gmail.com> - 2.3.5-2
- Bump EVR 

* Thu Jul 03 2008 Deji Akingunola <dakingun@gmail.com> - 2.3.5-1
- Update to 2.3.5

* Mon Jun 23 2008 Deji Akingunola <dakingun@gmail.com> - 2.3.4-2
- Remove --enable-gtkthml configure option, to enable gecko support

* Mon May 26 2008 Deji Akingunola <dakingun@gmail.com> - 2.3.4-1
- Update to 2.3.4

* Sun Feb 10 2008 Deji Akingunola <dakingun@gmail.com> - 2.3.3-2
- Rebuild for gcc43

* Sun Jan 20 2008 Deji Akingunola <dakingun@gmail.com> - 2.3.3-1
- Update to 2.3.3

* Fri Dec 28 2007 Deji Akingunola <dakingun@gmail.com> - 2.3.2-1
- Update to 2.3.2

* Thu Dec 20 2007 Deji Akingunola <dakingun@gmail.com> - 2.3.1-4
- Build with gtkhtml for now, until building with latest xulrunner is fixed

* Thu Nov 29 2007 Deji Akingunola <dakingun@gmail.com> - 2.3.1-3
- Rebuild for firefox-2.0.0.10

* Tue Nov 06 2007 Deji Akingunola <dakingun@gmail.com> - 2.3.1-2
- Rebuild for firefox-2.0.0.9

* Mon Nov 05 2007 Deji Akingunola <dakingun@gmail.com> - 2.3.1
- Update to version 2.3.1

* Sat Aug 25 2007 Deji Akingunola <dakingun@gmail.com> - 2.2.3-5
- Rebuild

* Fri Aug 03 2007 Deji Akingunola <dakingun@gmail.com> - 2.2.3-4
- License tag update
- Rebuild for new icu

* Sat Jun 09 2007 Deji Akingunola <dakingun@gmail.com> - 2.2.3-3
- Require 'yelp' for the Help menu (BZ #243395)
- Remove extraneous key from the desktop file

* Sun Mar 25 2007 Deji Akingunola <dakingun@gmail.com> - 2.2.3
- Version 2.2.3
- Configure tweak no longer necesary, gtkhtml38 now in Extras

* Tue Mar 13 2007 Deji Akingunola <dakingun@gmail.com> - 2.2.2.1-5
- Tweak configure script to allow building with newer gtkhml3

* Tue Mar 13 2007 Deji Akingunola <dakingun@gmail.com> - 2.2.2.1-4
- Another rebuild for gtkhtml

* Wed Feb 28 2007 Deji Akingunola <dakingun@gmail.com> - 2.2.2.1-3
- Rebuild for new gtkhtml

* Sat Feb 24 2007 Deji Akingunola <dakingun@gmail.com> - 2.2.2.1-2
- Add libgnomeprintui22-devel as BR

* Fri Feb 23 2007 Deji Akingunola <dakingun@gmail.com> - 2.2.2.1-1
- New release

* Sun Jan 28 2007 Deji Akingunola <dakingun@gmail.com> - 2.2.1-1
- Remove un-neccesary gnome-spell and icu BRs

* Sat Jan 27 2007 Deji Akingunola <dakingun@gmail.com> - 2.2.1-1
- Update to 2.2.1

* Tue Dec 26 2006 Deji Akingunola <dakingun@gmail.com> - 2.2.0-1
- New stable release

* Sun Dec 10 2006 Deji Akingunola <dakingun@gmail.com> - 2.1.10-3
- Add gnome-doc-utils to BR

* Sun Dec 10 2006 Deji Akingunola <dakingun@gmail.com> - 2.1.10-2
- Clean up spec file

* Sun Dec 10 2006 Deji Akingunola <dakingun@gmail.com> - 2.1.10-1
- New Release

* Mon Nov 13 2006 Deji Akingunola <dakingun@gmail.com> - 2.1.9-1
- New release (2.1.9)

* Thu Nov 09 2006 Deji Akingunola <dakingun@gmail.com> - 2.1.8-3
- Seems parallel make is causing problems

* Thu Nov 09 2006 Deji Akingunola <dakingun@gmail.com> - 2.1.8-2
- Fix Build requires

* Wed Nov 08 2006 Deji Akingunola <dakingun@gmail.com> - 2.1.8-1
- Update to new (unstable) version 

* Wed Sep 20 2006 Deji Akingunola <dakingun@gmail.com> - 2.1.6-4
- Add perl(XML::Parser) to the BRs

* Wed Sep 20 2006 Deji Akingunola <dakingun@gmail.com> - 2.1.6-3
- Take over from Michael A. Peters
- Rebuild for FC6

* Tue May 02 2006 Michael A. Peters <mpeters@mac.com> - 2.1.6-2
- Fixed crash when viewing OT using KJV module (Patch0)
- Closes bug 190413

* Tue Apr 25 2006 Michael A. Peters <mpeters@mac.com> - 2.1.6-1
- New upstream version
- removed commented out fixes for since upstream fixed 64-bit issues

* Mon Apr 17 2006 Michael A. Peters <mpeters@mac.com> - 2.1.5-3
- fix bug 188581 (187198)

* Sat Feb 18 2006 Michael A. Peters <mpeters@mac.com> - 2.1.5-2
- Rebuild in devel

* Wed Dec 14 2005 Michael A. Peters <mpeters@mac.com> - 2.1.5-1
- New upstream version, works with gtkhtml3-3.8
- disable x86_64 patch

* Thu Sep 15 2005 Michael A. Peters <mpeters@mac.com> - 2.1.2-2.3
- trying patch suggested by Tom 'spot' Callaway to fix x86_64 bug
- 160186
- libtool, aclocal, autoheader, automake, autoconf on x86_64

* Sun Jun 12 2005 Michael A. Peters <mpeters@mac.com> - 2.1.2-2.1
- Exclude x86_64 for now

* Thu Jun 09 2005 Michael A. Peters <mpeters@mac.com> - 2.1.2-2
- added --copy-name-to-generic-name to desktop-file-install
- fixed line break packaging error

* Mon Jun 06 2005 Michael A. Peters <mpeters@mac.com> - 2.1.2-1
- Initial cvs checkin for Fedora Extras
