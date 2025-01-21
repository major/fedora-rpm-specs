Name:       tagtool
Version:    0.12.3
Release:    45%{?dist}
Summary:    Ogg Vorbis and MP3 tag manager

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:    GPL-2.0-only
URL:        https://github.com/tagtool/tagtool
Source0:    http://download.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Patch1:     %{name}-contents.patch
Patch2:     %{name}-desktop.patch
Patch3:     %{name}-0.12.3-oga.patch
Patch4:     %{name}-DSOLink.patch
Patch5:     tagtool-aarch64.patch

BuildRequires: make
BuildRequires:  libglade2-devel
BuildRequires:  libvorbis-devel
BuildRequires:  id3lib-devel
BuildRequires:  libstdc++-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  perl(XML::Parser)

%description
Audio Tag Tool is a program to manage the information fields in MP3 and 
Ogg Vorbis files.

It can be used to edit tags one by one, but the most useful features are 
mass tag and mass rename. These are designed to tag or rename hundreds of 
files at once, in any desired format. 


%prep
%setup -q
%patch -P1 -p1 -b .contents
%patch -P2 -p1 -b .desktop
%patch -P3 -p1 -b .oga
%patch -P4 -p1 -b .dsolinking
%patch -P5 -p1 -b .aarch64

%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot} INSTALL="install -p"
%find_lang %{name}

desktop-file-install --delete-original  \
    --dir %{buildroot}%{_datadir}/applications     \
    --add-category AudioVideoEditing                    \
    --add-category AudioVideo                           \
    --add-category Application                          \
    %{buildroot}%{_datadir}/applications/%{name}.desktop

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p %{buildroot}%{_datadir}/metainfo
cat > %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Richard Hughes <richard@hughsie.com> -->
<!--
BugReportURL: https://github.com/tagtool/tagtool/issues/7
SentUpstream: 2014-09-18
-->
<application>
  <id type="desktop">tagtool.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <name>Audio Tag Tool</name>
  <summary>Ogg Vorbis and MP3 tag manager</summary>
  <description>
    <p>
      Audio Tag Tool is a program to manage the information fields in MP3 and
      Ogg Vorbis files (commonly called 'tags').  It is available under the GNU
      General Public Licence (GPL).  Please send me any comments or bugs you
      find.
    </p>
    <p>
      Tag Tool can be used to edit tags one by one, but the most useful
      features are the ability to easily tag or rename hundreds of files at
      once, in any desired format.
    </p>
    <p>
      The interface is arranged into two sections, with the list of available
      files on the left and a set of tabs on the right. Each tab corresponds to
      one of the main operations Audio Tag Tool can do:
    </p>
    <ul>
      <li>Lets you edit the tags individually</li>
      <li>You can set the tags of multiple files at once</li>
      <li>The tag fields can be set to a fixed value, filled in from the file's name, or left alone</li>
      <li>Allows you to remove the tags from multiple files at once</li>
      <li>For MP3 files it lets you choose to remove only ID3v1 or ID3v2 tags</li>
      <li>You can rename multiple files at once and/or organize them into directories</li>
      <li>Generates playlists. Playlists can be sorted by file name or by any tag field</li>
    </ul>
    <p>
    The mass tag and mass rename features can handle filenames in any
    format thanks to an easily configurable format template.
    </p>
  </description>
  <!-- No screenshots :( -->
  <url type="homepage">https://github.com/tagtool/tagtool</url>
  <updatecontact>ms@ansta.lt</updatecontact>
</application>
EOF

%files -f %{name}.lang
%doc AUTHORS BUGS ChangeLog NEWS README
%license COPYING
%{_bindir}/%{name}
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/48x48/apps/TagTool.png
%{_datadir}/icons/hicolor/scalable/apps/TagTool.svg


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.3-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.12.3-44
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.3-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.3-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.3-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.3-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.3-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.3-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.3-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.3-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.3-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Feb 09 2020 Nils Philippsen <nils@tiptoe.de> - 0.12.3-34
- require gcc-c++ and libstdc++ for building to fix MP3 support

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.3-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.3-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.3-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.3-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 10 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.12.3-29
- Add gcc to BR
- Use license macro
- Use buildroot instead of RPM_BUILD_ROOT

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.3-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.12.3-27
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.12.3-21
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 0.12.3-20
- Add an AppData file for the software center

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Mar 24 2013 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.12.3-16
- Patch for ARM 64
- https://bugzilla.redhat.com/show_bug.cgi?id=926608

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Feb 14 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 0.12.3-14
- Remove vendor tag from desktop file
- Cleanup spec as per recently changed packaging guidelines

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.12.3-11
- Rebuild for new libpng

* Sun May 01 2011 Dominic Hopf <dmaphy@fedoraproject.org> - 0.12.3-10
- rebuilt against current glibc

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Mar  7 2010 Brian Pepple <bpepple@fedoraproject.org> - 0.12.3-8
- Add patch to fix DSOLinking. (#565078)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Nov 28 2008 Brian Pepple <bpepple@fedoraproject.org> - 0.12.3-5
- Add patch to support *.oga files.

* Fri Feb  8 2008 Brian Pepple <bpepple@fedoraproject.org> - 0.12.3-4
- Rebuild for gcc-4.3.

* Tue Aug 21 2007 Brian Pepple <bpepple@fedoraproject.org> - 0.12.3-3
- Rebuild.

* Mon Aug  6 2007 Brian Pepple <bpepple@fedoraproject.org> - 0.12.3-2
- Update license tag.

* Tue Feb 27 2007 Brian Pepple <bpepple@fedoraproject.org> - 0.12.3-1
- Drop genre patch, fixed upstream.
- Add scriptlets for gtk-icon-cache.
- Add patch to fix desktop file.
- Drop X-Fedora category from desktop file.

* Tue Oct 17 2006 Brian Pepple <bpepple@fedoraproject.org> - 0.12.2-9
- Add patch to fix genre ui bug. (#211145)

* Thu Aug 31 2006 Brian Pepple <bpepple@fedoraproject.org> - 0.12.2-8
- Rebuild for FC6.

* Fri Jun 23 2006 Brian Pepple <bpepple@fedoraproject.org> - 0.12.2-7
- Add BR for perl(XML::Parser).

* Sun Feb 26 2006 Brian Pepple <bdpepple@ameritech.net> - 0.12.2-5
- Let's actually bump it this time & fix changelog errors.

* Sun Sep 25 2005 Brian Pepple <bdpepple@ameritech.net> - 0.12.2-4
- Add dist tag.

* Fri Sep 23 2005 Brian Pepple <bdpepple@ameritech.net> - 0.12.2-2
- Drop redundant BR's: gtk2-devel, libxml2-devel.
- Add missing scriplets for desktop-database.
- Merge directories.

* Fri Sep 16 2005 Brian Pepple <bdpepple@ameritech.net> - 0.12.2-1
- Initial Fedora Extras spec.
- Add patch to remove content from menu, since no help file is provided.

