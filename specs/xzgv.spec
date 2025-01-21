
Summary:         Picture viewer
Name:            xzgv
Version:         0.9.2
Release:         20%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:         GPL-2.0-or-later
URL:             http://sourceforge.net/projects/xzgv/
Source0:         http://downloads.sourceforge.net/xzgv/xzgv-%{version}.tar.gz
Patch0:          xzgv-0.9-fix-doc-install.patch
Patch1:          xzgv-0.9-fix-thumbnail-generation.patch
Patch2:          0001-Fix-xzgv-man-page-so-it-is-valid-nroff.patch
BuildRequires: make
BuildRequires:   gcc
BuildRequires:   gtk2-devel
BuildRequires:   libexif-devel
BuildRequires:   libpng-devel
BuildRequires:   texinfo
BuildRequires:   desktop-file-utils
Requires:        xterm
Requires:        gnome-icon-theme
%description 
A picture viewer with a thumbnail-based file selector.  Many file
formats are supported, and the thumbnails used are compatible with xv,
zgv and the Gimp.

%prep
%autosetup -p1
for f in ChangeLog NEWS; do
  iconv -f iso8859-1 -t utf8 $f -o $f.txt
  touch -r $f.txt $f
  mv $f.txt $f
done

%build
sed -i 's|^CFLAGS.*|CFLAGS=%{optflags}|' config.mk
make %{?_smp_flags}
make info

cat <<EOF > %{name}.desktop
[Desktop Entry]
Name=xzgv Image Viewer
Comment=View different types of images
Exec=xzgv
Icon=xzgv
Terminal=false
Type=Application
Categories=GTK;Graphics;RasterGraphics;Viewer;
EOF

%install
install -d -m 0755 %{buildroot}%{_datadir}/applications
install -d -m 0755 %{buildroot}%{_datadir}/pixmaps

make PREFIX=%{buildroot}/%{_prefix} \
     MANDIR=%{buildroot}/%{_mandir}/man1 \
     INFODIR=%{buildroot}/%{_infodir} \
     DESKTOPDIR2=%{buildroot}%{_datadir}/applications \
     install
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p %{buildroot}/%{_datadir}/appdata
cat > %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Ryan Lerch <rlerch@redhat.com> -->
<!--
BugReportURL: https://sourceforge.net/p/xzgv/feature-requests/5/
-->
<application>
  <id type="desktop">xzgv.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Simple image viewer</summary>
  <description>
    <p>
      xzgv is a simple image editor, with a focus on controlling all actions
      using keyboard input.
      It has a simple, two pane layout, with all the thumbnails of the current
      directory listed in the left pane, and the image viewed in the main pane.
      The menu in xzgv can be viewed in a context menu that is shown by
      right-clicking on the main image pane.
      This context menu also lists all the keyboard shortcuts if you are new to
      xzgv and need to know them.
    </p>
  </description>
  <url type="homepage">http://sourceforge.net/projects/xzgv/</url>
  <screenshots>
    <screenshot type="default">https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/xzgv/a.png</screenshot>
  </screenshots>
</application>
EOF

%files
%license COPYING
%doc AUTHORS NEWS README TODO ChangeLog
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*
%{_infodir}/%{name}*
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/xzgv.xpm

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.9.2-19
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 25 2020 Terje Rosten <terjeros@phys.ntnu.no> - 0.9.2-9
- Add patch from upstream to fix man page

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 16 2018 Terje Rosten <terjeros@phys.ntnu.no> - 0.9.2-5
- Add C compiler

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.2-2
- Remove obsolete scriptlets

* Thu Nov 09 2017 Terje Rosten <terjeros@phys.ntnu.no> - 0.9.2-1
- 0.9.2

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 0.9.1-11
- Add an AppData file for the software center

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Feb 10 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 0.9.1-7
- Remove vendor tag from desktop file as per https://fedorahosted.org/fesco/ticket/1077
- Cleanup spec as per recently changed packaging guidelines

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 07 2011 Terje Rosten <terje.rosten@ntnu.no> - 0.9.1-4
- Rebuilt for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb 10 2010 Terje Rosten <terjeros@phys.ntnu.no> - 0.9.1-2
- Add DSO patch

* Sat Dec 05 2009 Terje Rosten <terjeros@phys.ntnu.no> - 0.9.1-1
- 0.9.1

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon May 18 2009 Hans de Goede <hdegoede@redhat.com> - 0.9-7
- Add an icon for the menu entry
- Make ChangeLog and NEWS UTF-8

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 10 2009 Hans de Goede <hdegoede@redhat.com> - 0.9-5
- Update to latest upstream svn (r41) fixing several crashes
- Add a patch fixing thumbnail loading
- Add a patch fixing thumbnail generation for pictures where
  the width is not a multiple of 4
- Add a patch fixing thumbnail generation for pictures which have an alpha
  channel
- Fix scriptlet error on uninstall (make it preun instead of postun)

* Sat Feb 09 2008 Terje Rosten <terjeros@phys.ntnu.no> - 0.9-4
- rebuild

* Sun Jan 06 2008 Terje Rosten <terjeros@phys.ntnu.no> - 0.9-3
- info file has moved, fix scripts

* Sat Jan 05 2008 Terje Rosten <terjeros@phys.ntnu.no> - 0.9-2
- rebuild

* Sat Jan 05 2008 Terje Rosten <terjeros@phys.ntnu.no> - 0.9-1
- 0.9
- add all patches upto svn r35 
  fixing install and some other simple stuff
- new upstream maintainer, src and url updated
- drop patch now upstream
- build with gtk2 (yeah!) -> update summary and desc
- remove icon line from desktop file (icon gone)
- add texinfo to buildreq
- add patch to fix install of man and info files

* Sun Aug 19 2007 Terje Rosten <terjeros@phys.ntnu.no> - 0.8-6
- Fix license tag

* Wed Jul 04 2007 Terje Rosten <terjeros@phys.ntnu.no> - 0.8-5
- importing, fix tag problem

* Tue Jul 03 2007 Terje Rosten <terjeros@phys.ntnu.no> - 0.8-4
- add gnome-icon-theme to req

* Sun Jul 01 2007 Terje Rosten <terjeros@phys.ntnu.no> - 0.8-3
- really add AUTHORS and NEWS to %%doc
- use image-viewer.png from gnome-icon-theme as icon
- help system need xterm

* Wed Jun 20 2007 Terje Rosten <terjeros@phys.ntnu.no> - 0.8-2
- add AUTHORS and NEWS to %%doc
- fix scriplets
- add buildreq: desktop-file-utils
- add smp_mflags macro
- remove app categori from desktop file
- switch icon to eog

* Mon Jun 18 2007 Terje Rosten <terjeros@phys.ntnu.no> - 0.8-1
- 0.8
- add integer overflow patch
- cleanup description
- add correct buildrequires
- desktop file
- add req for post, preun

* Thu Jan  3 2002 Aleksey Nogin <ayn2@cornell.edu> - 0.7-3.rh
- Borrowed the SPEC from Mandrake
- Minor updates
- Added info files to the package

* Fri Nov 30 2001 Yves Duret <yduret@mandrakesoft.com> - 0.7-2mdk
- rebuild against libpng3
- really fix doc perm aka etienne sux

* Thu Aug 23 2001 Etienne Faure <etienne@mandrakesoft.com> - 0.7-1mdk
- 0.7
- fix doc permissions

* Sat Jan 06 2001 David BAUDENS <baudens@mandrakesoft.com> - 0.6-2mdk
- ExclusiveArch: %%ix86
- Fix group
- %%setup -q
- Fix %%postun
- Spec clean up

* Mon Nov 06 2000 Lenny Cartier <lenny@mandrakesoft.com> - 0.6-1mdk
- new in contribs
- add menu entry
