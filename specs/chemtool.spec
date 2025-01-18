Summary: A program for 2D drawing organic molecules
Name: chemtool
Version: 1.6.14
Release: 28%{?dist}
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Source0: http://ruby.chemie.uni-freiburg.de/~martin/chemtool/%{name}-%{version}.tar.gz
Patch0: %{name}-compile.patch
Patch1: %{name}-desktop.patch
Patch2: %{name}-gmd.patch
Patch3: %{name}-gcc10.patch
URL: http://ruby.chemie.uni-freiburg.de/~martin/chemtool/chemtool.html
BuildRequires:  gcc
BuildRequires: desktop-file-utils
BuildRequires: gtk2-devel
BuildRequires: kde3-filesystem
BuildRequires: libXt-devel
BuildRequires: make
Requires: openbabel
Requires: transfig

%description
Chemtool is a program for drawing organic molecules easily and store them
in a variety of output formats including as a X bitmap, Xfig, SVG or EPS
file.  It runs under the X Window System using the GTK widget set.

%prep
%autosetup -p1

%build
%configure \
  --with-kdedir=%{_prefix} \
  --with-gnomedir=%{_prefix}
%make_build

%install
install -d %{buildroot}%{_datadir}/{applications,mimelnk/application,mime-info,mime-types,pixmaps} \
        %{buildroot}%{_datadir}/icons/hicolor/{32x32/mimetypes,48x48/apps}

# fix line endings
pushd examples
tr -d '\r' < 14263232.mol > 14263232.mol.unix && mv -f 14263232.mol.unix 14263232.mol
tr -d '\r' < sample.sdf > sample.sdf.unix && mv -f sample.sdf.unix sample.sdf
popd

%make_install

install -pm644 kde/mimelnk/application/x-chemtool.desktop     %{buildroot}%{_datadir}/mimelnk/application
install -pm644 kde/icons/hicolor/32x32/mimetypes/chemtool.png %{buildroot}%{_datadir}/icons/hicolor/32x32/mimetypes
install -pm644 gnome/mime-types/chemtool.*                    %{buildroot}%{_datadir}/mime-types
install -pm644 gnome/gnome-application-chemtool.png           %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/chemtool.png
desktop-file-install \
                     --dir=%{buildroot}%{_datadir}/applications \
                     --add-category=Education \
                     --add-category=Science \
                     chemtool.desktop

%find_lang %{name}

%files -f %{name}.lang
%doc ChangeLog README TODO examples using_chemtool.html
%{_bindir}/chemtool
%{_bindir}/chemtoolbg
%{_bindir}/cht
%{_datadir}/mimelnk/application/x-chemtool.desktop
%{_datadir}/mime-types/chemtool.keys
%{_datadir}/mime-types/chemtool.mime
%{_datadir}/icons/hicolor/32x32/mimetypes/chemtool.png
%{_datadir}/icons/hicolor/48x48/apps/chemtool.png
%{_datadir}/applications/chemtool.desktop
%{_mandir}/man1/chemtool.1*
%{_mandir}/man1/cht.1*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.14-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.14-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.14-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.14-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Nov 20 2023 Dominik Mierzejewski <dominik@greysector.net> - 1.6.14-24
- correct build requirement on KDE
- switch to autosetup macro
- use SPDX identifier in License field

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.14-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.14-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.14-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.14-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.14-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.14-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.14-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Feb 20 2020 Dominik Mierzejewski <rpm@greysector.net> - 1.6.14-17
- fix build with GCC10

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.14-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.14-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.14-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.14-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.14-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.6.14-11
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.14-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.14-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb 21 2017 Dominik Mierzejewski <rpm@greysector.net> - 1.6.14-8
- add missing semicolon to the desktop file (#1423253)
- drop unnecessary update-desktop-database calls for F25+

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 17 2014 Dominik Mierzejewski <rpm@greysector.net> - 1.6.14-3
- use PNG icon in .desktop file
- drop XPM icon, it's never used at run-time
- add HTML doc to docs
- list all files in the file list explicitly
- drop some unnecessary spec file bits
- replace $RPM_BUILD_ROOT with (shorter) buildroot macro
- fix bogus date in changelog
- set mode on installed files explicitly

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Aug 13 2013 Dominik Mierzejewski <rpm@greysector.net> - 1.6.14-1
- updated to 1.6.14

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 1.6.13-4
- remove vendor tag from desktop file. https://fedorahosted.org/fpc/ticket/247
- clean up spec to follow current guidelines

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Mar 12 2012 Dominik Mierzejewski <rpm@greysector.net> - 1.6.13-1
- updated to 1.6.13
- dropped upstreamed explicit libX11 linking patch

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.6.12-4
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Feb 15 2010 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 1.6.12-2
- fixed FTBFS with new ld (rhbz#564785)

* Sat Aug 22 2009 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 1.6.12-1
- updated to 1.6.12
- dropped obsolete patch hunks
- moved gtk-update-icon-cache to posttrans scriptlet

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.6.11-3
- Autorebuild for GCC 4.3

* Sun Sep 23 2007 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 1.6.11-2
- drop libEMF dependency (current transfig/fig2dev supports EMF output)

* Sun Aug 26 2007 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 1.6.11-1
- updated to 1.6.11
- updated license tag
- specfile cleanups
- fixed GNOME dir detection
- fixed build with libEMF

* Wed Apr 25 2007 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 1.6.10-1
- updated to 1.6.10

* Fri Dec 22 2006 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 1.6.9-7
- fix stupid directory creation bug

* Thu Dec 21 2006 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 1.6.9-6
- fix MIME type in desktop file (#220125)

* Mon Nov 20 2006 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 1.6.9-5
- keep the whole examples dir in docs
- add update-desktop-database call to post{,un} scripts

* Mon Nov 20 2006 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 1.6.9-4
- fix build without mock

* Sun Nov 19 2006 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 1.6.9-3
- added missing BRs
- add scriptlets to update icon cache

* Sun Nov 19 2006 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 1.6.9-2
- don't use non-standard macros

* Fri Nov 17 2006 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 1.6.9-1
- initial build, based on bioxray.dk and PLD specfiles
