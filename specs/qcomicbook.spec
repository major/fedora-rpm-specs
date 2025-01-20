%undefine __cmake_in_source_build

Summary: A viewer for comic book archives
Name:    qcomicbook
Version: 0.9.1
Release: 19%{?dist}

# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
URL:     https://github.com/stolowski/QComicBook/
Source0: https://github.com/stolowski/QComicBook/archive/%{version}/%{name}-%{version}.tar.gz
# https://github.com/stolowski/QComicBook/pull/30
Patch1: qcomicbook-12638e6947c95657dfdb0f779528260bace72a47.patch
Patch2: qcomicbook-123b0f02c3860f122e55029d29c75bdb9431034d.patch

BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: pkgconfig(poppler-qt5)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: qt5-linguist
#BuildRequires: pkgconfig(xmu)
#BuildRequires: pkgconfig(xi)

#%%{?_qt5_version:Requires: qt5%%{?_isa} >= %%{_qt5_version}}
## runtime utilities for viewing comic book archives
#Requires: bzip2
#Requires: gzip
#Requires: p7zip
#Requires: tar
#Requires: unzip
## nonfree stuff
#Requires: unace
#Requires: unrar


%description
QComicBook is a viewer for PDF files and comic book archives containing
jpeg/png/xpm/gif/bmp images, which aims at convenience and simplicity.
Features include: automatic unpacking of archive files, full-screen mode, continuous
scrolling mode, double-pages viewing, manga mode, thumbnails view, page scaling,
mouse or keyboard navigation etc.

You will also need unzip, rar (or unrar), unace, p7zip and tar (with gzip and
bzip2 support compiled in) somewhere in your PATH to handle archives. If one of
these tools is missing you can still use QComicBook, but you won't be able to
open some archives. You may check status of supported archives via Help > System information
menu option of QComicBook.


%prep
%autosetup -p1 -n QComicBook-%{version}


%build
%{cmake}
%cmake_build


%install
%cmake_install

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Ryan Lerch <rlerch@redhat.com> -->
<!--
EmailAddress: stolowski@gmail.com
SentUpstream: 2014-09-18
-->
<application>
  <id type="desktop">qcomicbook.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Read comics</summary>
  <description>
    <p>
      QComicBook is an application for reading comics and supports a wide
      range of formats, including CBZ, CBR and CBT.
      QComicBook has a wide range of features to enhance your comic reading,
      including page preview, a thumbnails view, bookmarks, and a specific
      mode for reading manga.
    </p>
  </description>
  <url type="homepage">http://qcomicbook.org/</url>
  <screenshots>
    <screenshot type="default">http://qcomicbook.org/screenshots/qcomicbook072-os2.png</screenshot>
  </screenshots>
</application>
EOF

%find_lang qcomicbook --without-mo --with-qt


%check
desktop-file-validate ${RPM_BUILD_ROOT}%{_datadir}/applications/*%{name}.desktop

%files -f qcomicbook.lang
%doc AUTHORS README ChangeLog COPYING THANKS TODO
%{_bindir}/qcomicbook
%{_mandir}/man1/qcomicbook.1*
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/qcomicbook.desktop
%{_datadir}/pixmaps/qcomicbook.png
%dir %{_datadir}/qcomicbook/
%dir %{_datadir}/qcomicbook/i18n/


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.9.1-18
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Marek Kasik <mkasik@redhat.com> - 0.9.1-6
- Rebuild for poppler-0.84.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 23 2018 Marek Kasik <mkasik@redhat.com> - 0.9.1-2
- Rebuild for poppler-0.63.0

* Wed Feb 07 2018 Peter Lemenkov <lemenkov@gmail.com> - 0.9.1-1
- Ver. 0.9.1
- Switch to Qt5
- Fix rhbz#1471770

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.9.0-7
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 0.9.0-6
- Add an AppData file for the software center

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Aug 08 2012 Rex Dieter <rdieter@fedoraproject.org> 0.9.0-1
- 0.9.0

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-4
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 14 2010 Rex Dieter <rdieter@fedoraproject.org> -  0.7.2-1
- 0.7.2 (#663151)

* Sun Feb 07 2010 Rex Dieter <rdieter@fedoraproject.org> - 0.5.0-1
- qcomicbook-0.5.0 (#560632)
- update URL
- convert build to use cmake
- BR: qt4-devel (to avoid ambiguity)
- drop needless/explicit Requires: qt
- drop needless .desktop vendor (f13+)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Sep  3 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.4.0-3
- fix license tag

* Tue Apr 01 2008 Scott Baker <scott@perturb.org> - 0.4.0-2
- QT4 -> QT convesions (WOOHOO KDE4)

* Wed Nov 07 2007 Scott Baker <scott@perturb.org> - 0.4.0-1
- Added the requirment for QT4

* Wed Nov 07 2007 Scott Baker <scott@perturb.org> - 0.4.0-1
- Update to the latest version and drop the imlib dependency

* Thu Nov 30 2006 Scott Baker <scott@perturb.org> - 0.3.4-1
- Update to the latest version

* Mon Oct 09 2006 Scott Baker <scott@perturb.org> - 0.3.3-5
- Build on FC6

* Wed Sep 20 2006 Scott Baker <scott@perturb.org> - 0.3.3-2
- Bumped release to 0.3.3

* Sun Sep 03 2006 Scott Baker <scott@perturb.org> - 0.3.2-6
- Fixed building for SMP arches

* Thu Aug 31 2006 Scott Baker <scott@perturb.org> - 0.3.2-5
- Removed the BuildArch

* Mon Aug 28 2006 Scott Baker <scott@perturb.org> - 0.3.2-4
- Updated how the .desktop file is handled
- Updated the make to include SMP options
- Remove bogus "requires"
- Update the rm -rf in clean and install

* Mon Aug 28 2006 Scott Baker <scott@perturb.org> - 0.3.2-3
- Removed requirement for unrar since it's not available via Fedora

* Sun Aug 27 2006 Scott Baker <scott@perturb.org> - 0.3.2-2
- Begin packaging for Fedora Extras.
