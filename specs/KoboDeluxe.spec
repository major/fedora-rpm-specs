Name:           KoboDeluxe
Version:        0.5.1
Release:        44%{?dist}
Summary:        Third person scrolling 2D shooter
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://olofson.net/kobodl/
Source0:        http://olofson.net/kobodl/download/%{name}-%{version}.tar.bz2
Source1:        %{name}-32.png
Source2:        %{name}-64.png
Source3:        %{name}-128.png
Source4:        %{name}.desktop
Source5:        %{name}.appdata.xml
Patch1:         KoboDeluxe-defaults.patch
Patch2:         KoboDeluxe-0.5.1-avoid-unistd-pipe-collision.patch
Patch3:         KoboDeluxe-0.5.1-gcc44.patch
Patch4:         KoboDeluxe-0.5.1-midi-crash-fix.patch
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  SDL_image-devel desktop-file-utils libappstream-glib
BuildRequires: make
Requires:       hicolor-icon-theme
Requires(pre):  shadow-utils

%description
Kobo Deluxe is a 3'rd person  scrolling 2D shooter with a simple
and responsive control system  - which you'll need to tackle the
tons of enemy ships that shoot at you,  chase you, circle around
you shooting,  or even  launch other ships at you,  while you're
trying to  destroy the  labyrinth  shaped  bases.  There  are 50
action packed  levels with  smoothly increasing  difficulty, and
different combinations of enemies that require different tactics
to be dealt with successfully.


%prep
%autosetup -p1
sed -i 's|$(sharedstatedir)/kobo-deluxe/scores|%{_var}/games/kobo-deluxe|g' \
  configure
iconv -f ISO-8859-1 -t UTF8 README > tmp;         mv tmp README
iconv -f ISO-8859-1 -t UTF8 ChangeLog > tmp;      mv tmp ChangeLog
iconv -f ISO2022JP -t UTF8 README.jp > tmp;       mv tmp README.jp
iconv -f ISO2022JP -t UTF8 README.xkobo.jp > tmp; mv tmp README.xkobo.jp



%build
%configure --disable-dependency-tracking --enable-opengl
%make_build


%install
%make_install INSTALL="install -p"

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
install -p -m 644 %{SOURCE1} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -p -m 644 %{SOURCE2} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
install -p -m 644 %{SOURCE3} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE4}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml

%pre
getent group kobodl >/dev/null || groupadd -r kobodl
exit 0

%files
%doc ChangeLog COPYING* README README.jp README.xkobo.jp README.sfont 
%doc README.xkobo TODO
%attr(2755,root,kobodl) %{_bindir}/kobodl
%{_datadir}/kobo-deluxe
%{_mandir}/man6/kobodl.6.gz
%config(noreplace) %attr(0775,root,kobodl) %{_var}/games/kobo-deluxe
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul  26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.5.1-43
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Mar  4 2020 Hans de Goede <hdegoede@redhat.com> - 0.5.1-31
- Add 32x32 and 64x64 icons for cases where we need a lower res icon

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.1-25
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Hans de Goede <hdegoede@redhat.com> - 0.5.1-20
- Fix .desktop file Keywords field

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun  5 2015 Hans de Goede <hdegoede@redhat.com> - 0.5.1-18
- Fix crash when build with gcc-5.1 (rhbz#1227807)
- Better description for the appdata file

* Wed Jun  3 2015 Hans de Goede <hdegoede@redhat.com> - 0.5.1-17
- Add an appdata file

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.5.1-16
- Rebuilt for GCC 5 C++11 ABI change

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul  5 2013 Hans de Goede <hdegoede@redhat.com> - 0.5.1-12
- Create a system group for the highscore file (#981602)
- Modernize spec-file a bit

* Tue Feb 12 2013 Jon Ciesla <limburgher@gmail.com> - 0.5.1-11
- Drop desktop vendor tag.

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Aug 11 2009 Ville Skyttä <ville.skytta@iki.fi> - 0.5.1-7
- Use bzipped upstream tarball.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Mar 9  2009 Hans de Goede <hdegoede@redhat.com> 0.5.1-4
- Fix building with gcc 4.4

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Sep 24 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.5.1-3
- avoid variable collision between "pipe2" and unistd.h

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.5.1-2
- Autorebuild for GCC 4.3

* Fri Dec 28 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.5.1-1
- New upstream release 0.5.1

* Sun Dec 16 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.5.0-1
- New upstream release 0.5.0

* Wed Oct 31 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.4.1-1
- New upstream release 0.4.1
- Drop integrated patches

* Fri Aug  3 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.4-0.4.pre10
- Update License tag for new Licensing Guidelines compliance

* Mon Feb 19 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.4-0.3.pre10
- Some last small specfile improvements from review (bz 228707)

* Mon Feb 19 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.4-0.2.pre10
- various specfile improvements from review (bz 228707)
- install (do not remove after make install) kobosfx.h, its not a stray header
  file it actually gets loaded runtime by the game

* Mon Feb 12 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.4-0.1.pre10
- Initial Fedora Extras package
