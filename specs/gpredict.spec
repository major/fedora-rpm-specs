Name:           gpredict
Version:        2.2.1
Release:        21%{?dist}
Summary:        Real-time satellite tracking and orbit prediction program
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://gpredict.oz9aec.net/
Source0:        https://github.com/csete/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.bz2
Source1:        gpredict.desktop
Source2:        gpredict.appdata.xml
Patch0:         build_fix.patch

BuildRequires: gtk3-devel
BuildRequires: glib2-devel
BuildRequires: curl-devel
BuildRequires: desktop-file-utils
BuildRequires: intltool
BuildRequires: goocanvas2-devel
BuildRequires: gettext
BuildRequires: libtool
BuildRequires: make
Requires:      hamlib
Requires:      hicolor-icon-theme

%description
Gpredict is a real time satellite tracking and orbit prediction
program written using the Gtk+ widgets. Gpredict is targeted mainly
towards ham radio operators but others interested in satellite
tracking may find it useful as well. Gpredict uses the SGP4/SDP4
algorithms, which are compatible with the NORAD Keplerian elements.


%prep
%setup -q
%patch -P0 -p1


%build
%{configure} --prefix=%{_prefix}
%make_build


%install
%make_install

%find_lang %{name}
desktop-file-install --dir %{buildroot}/%{_datadir}/applications/ %{SOURCE1}
install -D -p -m644 pixmaps/logos/gpredict_icon_color.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
install -D -p -m644 %{SOURCE2} %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/appdata/*%{name}.appdata.xml
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/pixmaps/gpredict/icons/*
%{_datadir}/pixmaps/gpredict/maps/*
%{_datadir}/pixmaps/gpredict/logos/*
%{_datadir}/pixmaps/gpredict-icon.png
%{_mandir}/man1/gpredict*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 2.2.1-20
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jul 02 2023 Daniel Rusek <mail@asciiwolf.com> - 2.2.1-15
- Install better desktop icon, fix typo

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 07 2022 Richard Shaw <hobbes1069@gmail.com> - 2.2.1-13
- Rebuild for updated hamlib 4.5.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 23 2021 Richard Shaw <hobbes1069@gmail.com> - 2.2.1-10
- Rebuild for hamlib 4.4.

* Thu Dec 23 2021 Richard Shaw <hobbes1069@gmail.com> - 2.2.1-9
- 36-build-side-49086

* Tue Oct 12 2021 Richard Shaw <hobbes1069@gmail.com> - 2.2.1-8
- Rebuild for hamlib 4.3.1.

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 30 2021 Richard Shaw <hobbes1069@gmail.com> - 2.2.1-6
- Rebuild for hamlib 4.2.

* Tue Feb 02 2021 Richard Shaw <hobbes1069@gmail.com> - 2.2.1-5
- Rebuild for hamlib 4.1.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 2.2.1-2
- fix wrong patch

* Mon Jun 22 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 2.2.1-1
- Update to 2.2.1 upstream release

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 10 2018 Nikos Roussos <comzeradd@fedoraproject.org> - 2.2-1
- Update to 2.2

* Fri Dec 22 2017 Nikos Roussos <comzeradd@fedoraproject.org> - 2.0-1
- Update to 2.0

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Apr 12 2013 Jon Ciesla <limburgher@gmail.com> - 1.3-7
- Drop desktop vendor tag.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 31 2012 Eric "Sparks" Christensen <sparks@fedoraproject.org> - 1.3-4
- Mapped localized files

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.3-2
- Rebuild for new libpng

* Wed Mar 02 2011 Eric "Sparks" Christensen <sparks@fedoraproject.org> - 1.3-1
- Feature request 2873824: Flip Passes.
- Feature Request 3022617: Malaysia's location.
- Automatically refresh the Sky at a glance view every minute.
- Added more checks with hamlib communications.
- List satellite as available or selected when configuring module.
- Fixed bug 2116691: Leave network connection open.
- Fixed bug 3099314: Rotator Thrashing.
- Fixed bug 2167508: problems in rotator controller.
- Fixed bug from Ubuntu #706452: Update from local files won't work with files in UPPER case 
- Fixed bug 3171615: Searching for satellites in the satellite selector
- Fixed bug 3113190: .desktop file error
- Address bug 2945538: Pass in polar display going outside the circle (Improve the graphical portion.)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Nov 21 2010 Eric "Sparks" Christensen <sparks@fedoraproject.org> - 1.2-2
- Updated desktop file to fix icon.

* Mon Nov 15 2010 Eric "Sparks" Christensen <sparks@fedoraproject.org> - 1.2-1
- Updated to newest version available (1.2).

* Tue May 04 2010 Lubomir Rintel (Fedora Astronomy) <lkundrak@v3.sk> - 0.9.0-7
- Adjust for yet newer GTK, rebuild

* Wed Mar 3 2010 Lubomir Rintel (Fedora Astronomy) <lkundrak@v3.sk> - 0.9.0-6
- Fix build with new linker
- Adjust for newer GTK

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Mar 24 2009 Lubomir Rintel (Fedora Astronomy) <lkundrak@v3.sk> - 0.9.0-4
- Fix up the menu entry for Astronomy menus

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.9.0-2
- Autorebuild for GCC 4.3

* Sat Sep 29 2007 Denis Leroy <denis@poolshark.org> - 0.9.0-1
- Update to 0.9.0
- Removed tooltip patch, is now upstream

* Mon Aug 20 2007 Denis Leroy <denis@poolshark.org> - 0.8.0-3
- Updated License tag
- Added patch for new GtkTooltip interface

* Tue Jun 19 2007 Denis Leroy <denis@poolshark.org> - 0.8.0-2
- Fixed desktop StartupNotify line

* Tue Jun 19 2007 Denis Leroy <denis@poolshark.org> - 0.8.0-1
- Update to 0.8.0

* Sun Jan 21 2007 Denis Leroy <denis@poolshark.org> - 0.7.1-1
- Update to 0.7.1

* Tue Jan  9 2007 Denis Leroy <denis@poolshark.org> - 0.7.0-1
- Update to 0.7.0, needs curl-devel

* Thu Sep 14 2006 Denis Leroy <denis@poolshark.org> - 0.6.1-1
- Update to 0.6.1
- Removed patch, was integrated upstream

* Tue Sep  5 2006 Denis Leroy <denis@poolshark.org> - 0.6.0-1
- Update to 0.6.0
- New gtk2 BRs. No longer needs hamlib
- Fixed desktop database file

* Sat Mar 19 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.5.0-4
- %%

* Wed Mar 16 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.5.0-3
- Broke %%description at 80 columns

* Wed Mar 16 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.5.0-2
- Removed explicit Requires

* Tue Mar 15 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.5.0-1
- Bump release to 1
- Added d-f-u to BR

* Sun Feb 13 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0:0.5.0-0.iva.0
- Initial RPM release.
