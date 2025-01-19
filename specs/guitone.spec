%global rctag rc5

Name:		guitone
Version:	1.0
Release:	0.37%{?rctag:.%rctag}%{?dist}
Summary:	A frontend for Monotone
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:	GPL-3.0-or-later
URL:		http://guitone.thomaskeller.biz/
Source:		%{url}releases/%{version}%{?rctag:%rctag}/%{name}-%{version}%{?rctag:%rctag}.tgz
Patch0:		guitone-1.0rc5-cpp11.patch
Patch1:		guitone-1.0rc5-format-security.patch
# License is GPLv3+.  This forces us to build against qt >= 4.3.4.
BuildRequires:	qt4-devel >= 4.3.4
BuildRequires:	gcc-c++
BuildRequires:	make
BuildRequires:	desktop-file-utils
Requires:	monotone >= 0.99.1

%description 
Guitone is a Qt-based, cross-platform graphical user interface for the
distributed version control system monotone. It aims towards a full
implementation of the monotone automation interface and is especially
targeted at beginners. 

Functionality provided by guitone:

* Browse a loaded workspace, filter by file states
* Display attributes of selected files
* Open files in the system's default viewer on double-click
* Show file differences for single and multiple files
* List keys from the loaded database and generate new keys
* Checkout, export and commit revisions
* Query recent revisions from a loaded database

and much more.


%prep
%setup -q -n %{name}-%{version}%{?rctag:%rctag}
%patch -P0 -p1
%patch -P1 -p1

cat >%{name}.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=Guitone
Comment=Frontend for Monotone
Exec=guitone
Icon=guitone
Terminal=false
Type=Application
Categories=Application;Development;
EOF


%build
%{qmake_qt4} LRELEASE=lrelease-qt4 -config release guitone.pro
make %{?_smp_mflags}


%install
install -m 755 -D -p bin/guitone %{buildroot}%{_bindir}/guitone
install -m 644 -D -p res/icons/guitone.png %{buildroot}%{_datadir}/pixmaps/guitone.png

desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  --vendor="" \
  %{name}.desktop

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
<!-- Copyright 2014 Richard Hughes <richard@hughsie.com> -->
<!--
EmailAddress: me@thomaskeller.biz
SentUpstream: 2014-09-18
-->
<application>
  <id type="desktop">guitone.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Graphical viewer for Monotone repositories</summary>
  <description>
    <p>
     Guitone is a tool to visually navigate Monotone repositories.
     Guitone aims to be a full implementation of the monotone automation
     interface, and provides features such as:
    </p>
    <ul>
      <li>Browsing a loaded workspace, with filtering by file states</li>
      <li>Display of the attributes of files</li>
      <li>Opening of files with the system's default editor or browser</li>
      <li>Showing differences between files</li>
    </ul>
  </description>
  <url type="homepage">https://guitone.thomaskeller.biz/</url>
  <screenshots>
    <screenshot type="default">https://guitone.thomaskeller.biz/web/screens/1.0rc2/changeset_browser.png</screenshot>
  </screenshots>
  <!-- FIXME: change this to an upstream email address for spec updates
  <updatecontact>someone_who_cares@upstream_project.org</updatecontact>
   -->
</application>
EOF

# the tests subdir currently contains only a stub of a testsuite, and
# upstream told us not to use it yet, so no 'check' section.


%files
%doc NEWS README README.driver
%license COPYING
%{_bindir}/guitone
%{_datadir}/pixmaps/guitone.png
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/guitone.desktop


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.37.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0-0.36.rc5
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.35.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.34.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.33.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.32.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.31.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.30.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.29.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.28.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.27.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.26.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.25.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.24.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.23.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.22.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Mar 25 2018 Thomas Moschny <thomas.moschny@gmx.de> - 1.0-0.21.rc5
- Add BRs on make and gcc-c++.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.20.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug  8 2017 Thomas Moschny <thomas.moschny@gmx.de> - 1.0-0.19.rc5
- Add patch to fix a format-security error.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.18.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.17.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.16.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb  4 2016 Thomas Moschny <thomas.moschny@gmx.de> - 1.0-0.15rc5
- Add patch to fix FTBFS with gcc6.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.14.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Feb 02 2016 Rex Dieter <rdieter@fedoraproject.org> - 1.0-0.13.rc5
- use %%qmake_qt4 macro to ensure proper build flags

* Mon Aug 17 2015 Thomas Moschny <thomas.moschny@gmx.de> - 1.0-0.12.rc5
- Mark COPYING as %%license.
- Modernized spec file.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.11.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.0-0.10.rc5
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 1.0-0.9.rc5
- Add an AppData file for the software center

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.8.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.7.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.6.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.5.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.4.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.3.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.2.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Nov  6 2010 Thomas Moschny <thomas.moschny@gmx.de> - 1.0-0.1.rc5
- Update to 1.0rc5.

* Sun May 30 2010 Thomas Moschny <thomas.moschny@gmx.de> - 1.0-0.1.rc4
- Update to 1.0rc4.

* Sun Apr 25 2010 Thomas Moschny <thomas.moschny@gmx.de> - 1.0-0.1.rc3
- Update to 1.0rc3.
- lrelease is called by qmake now.

* Wed Apr  7 2010 Thomas Moschny <thomas.moschny@gmx.de> - 1.0-0.1.rc2
- Update to 1.0rc2.

* Mon Feb 15 2010 Thomas Moschny <thomas.moschny@gmx.de> - 1.0-0.1.rc1
- Update to 1.0rc1.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9_1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9_1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Oct  7 2008 Thomas Moschny <thomas.moschny@gmx.de> - 0.9_1-1
- Upstream updated the tarfile.
- Added README.driver to %%doc.

* Sat Oct  4 2008 Thomas Moschny <thomas.moschny@gmx.de> - 0.9-1
- Update to version 0.9.

* Wed May 28 2008 Thomas Moschny <thomas.moschny@gmx.de> - 0.8-2
- Fix order of commands in the build section.

* Mon May 26 2008 Thomas Moschny <thomas.moschny@gmx.de> - 0.8-1
- Update to upstream version 0.8.
- Add a zero-day patch from upstream.
- License is GPLv3+ now.

* Sun Apr  6 2008 Thomas Moschny <thomas.moschny@gmx.de> - 0.7.1-1
- Update to upstream version 0.7.1.

* Fri Feb 22 2008 Thomas Moschny <thomas.moschny@gmx.de> - 0.7-4
- Add patch to fix GCC 4.3 build.

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.7-3
- Autorebuild for GCC 4.3

* Tue Jan 22 2008 Thomas Moschny <thomas.moschny@gmx.de> - 0.7-2
- Small patch: Add Qt SVG module.
- Add note about the testsuite.

* Wed Jan 16 2008 Thomas Moschny <thomas.moschny@gmx.de> - 0.7-1
- Initial version.
