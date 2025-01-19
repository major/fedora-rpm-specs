Name:           njam
Version:        1.25
Release:        47%{?dist}
Summary:        Maze-game, eat all the cookies while avoiding the badguys
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://njam.sourceforge.net/
# should be
# http://downloads.sourceforge.net/%{name}/%{name}-%{version}-src.tar.gz
# but that file has got corrupted, hurray for sourceforge :(
Source0:        %{name}-%{version}-src.tar.gz
Source1:        njam.6
Source2:	njam.desktop
Patch0:         njam-1.25-drop-setgid.patch
Patch1:         njam-1.25-html.patch
Patch2:         njam-1.25-leveledit.patch
Patch3:         njam-1.25-gcc45.patch
Patch4:         njam-1.25-rhbz767015.patch
Patch5:         njam-1.25-format-security.patch
Patch6: njam-configure-c99.patch
BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires:  SDL-devel SDL_mixer-devel SDL_image-devel SDL_net-devel 
BuildRequires:  ImageMagick desktop-file-utils
Requires:       hicolor-icon-theme 

%description
Njam is a fast-paced maze-game where you must eat all the cookies while
avoiding the badguys. Special cookies give you the power to freeze or eat the
bad guys. The game features single and multiplayer modes, network play,
duelling and cooperative games, great music and sound effects, customizable
level skins, many different levels and an integrated level editor.


%prep
%setup -q -n %{name}-%{version}-src
%patch -P0 -p1 -z .setgid
%patch -P1 -p1
%patch -P2 -p1 -z .leveledit
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1


%build
%configure
make %{?_smp_mflags}
convert -transparent black njamicon.ico %{name}.png


%install
%make_install

# make install installs the docs under /usr/share/njam. We want them in %doc.
rm $RPM_BUILD_ROOT%{_datadir}/%{name}/README
rm $RPM_BUILD_ROOT%{_datadir}/%{name}/levels/readme.txt
rm -fr $RPM_BUILD_ROOT%{_datadir}/%{name}/html

# clean up cruft
rm $RPM_BUILD_ROOT%{_datadir}/%{name}/%{name}.*
rm $RPM_BUILD_ROOT%{_datadir}/%{name}/njamicon.ico

# we want the hiscore in /var/lib/games
mkdir -p $RPM_BUILD_ROOT%{_var}/lib/games
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/hiscore.dat \
  $RPM_BUILD_ROOT%{_var}/lib/games/%{name}.hs

# add the manpage (courtesy of Debian)
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man6
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man6

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE2}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
install -p -m 644 %{name}.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps

%files
%doc COPYING ChangeLog NEWS README TODO levels/readme.txt html
%attr(2755,root,games) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man6/%{name}.6.gz
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%config(noreplace) %attr (0664,root,games) %{_var}/lib/games/%{name}.hs


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.25-46
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Nov 27 2022 Florian Weimer <fweimer@redhat.com> - 1.25-40
- Port configure script to C99

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.25-29
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.25-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.25-23
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.25-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 14 2014 Hans de Goede <hdegoede@redhat.com> - 1.25-21
- Fix building with -Werror=format-security (rhbz#1037222)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.25-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.25-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 29 2013 Jon Ciesla <limburgher@gmail.com> - 1.25-18
- Drop desktop vendor tag.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.25-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.25-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.25-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Dec 11 2011 Hans de Goede <hdegoede@redhat.com> - 1.25-14
- Fix a crash on a very long SDL_VIDEODRIVER env variable (rhbz#767015)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.25-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Sep 10 2010 Hans de Goede <hdegoede@redhat.com> 1.25-12
- Fix compilation with gcc 4.5

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.25-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.25-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.25-9
- Autorebuild for GCC 4.3

* Sat Jan 12 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 1.25-8
- Fix compilation with gcc 4.3

* Fri Aug 31 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.25-7
- Fix Source0 URL

* Wed Aug 22 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.25-6
- Rebuild for buildId

* Sun Aug 12 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.25-5
- Update License tag for new Licensing Guidelines compliance
- Fix invalid desktop file (fix building with latest desktop-file-utils)

* Mon Aug 28 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.25-4
- FE6 Rebuild

* Tue May  9 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.25-3
- Add Patch2, which fixes the leveleditor to save custom made levels under
  $HOME/.njam-levels instead of trying to write them under /usr/share.
  Also teach njam to look for levels under both $HOME/.njam-levels and
  /usr/share (bug 188078).

* Tue Mar 28 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.25-2
- Cleaned up description in spec and man using the cleaner
  description provided in bz 186813
- Use cookies instead of dots in summary (bz 186813)
- Put manpage in man6 (bz 186813)
- fix broken home link in doc-editor.html (bz 186813)

* Wed Mar 22 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.25-1
- initial Fedora Extras package
