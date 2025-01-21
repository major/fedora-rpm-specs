# The game contains a copy of these fonts, we replace these with symlinks to the system versions of these fonts
%global fonts font(amiri) font(dejavusans) font(dejavusansmono) font(dejavuserif) font(widelands) font(gargi) font(wenquanyimicrohei) font(frankruehlclm)

Name:           widelands
Version:        1.2
Release:        3%{?dist}
Summary:        Open source realtime-strategy game

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.widelands.org
Source0:        https://github.com/widelands/widelands/archive/v%{version}/%{name}-%{version}.tar.gz
# gnu++11 fix in CMakeLists.txt for PPC64 little-endian
Patch0:         widelands-1.2-build19-ppc64le.patch
# Fix failures on s390x due to uninitialized variables
Patch1:         widelands-1.2-build20-gcc10.patch
# widelands uses glew which atm is hardcoded to glx, see e.g.:
# https://github.com/nigels-com/glew/issues/172
# This can be fixed cleaner by switching to glewContextInit once we are
# at glew 2.3, or maybe backport:
# https://github.com/nigels-com/glew/commit/715afa0ff56c0eb12c23938b80aa2813daa10d81
Patch2:         widelands-1.0-make-sdl2-use-x11.patch
Patch3:         widelands-1.2-gcc13.patch
Patch4:         widelands-1.1-f37-sys-minizip-buildfix.patch
Patch5:         widelands-1.1-disable-some-tests.patch

BuildRequires: asio-devel
BuildRequires: SDL2-devel
BuildRequires: SDL2_image-devel
BuildRequires: SDL2_mixer-devel
BuildRequires: SDL2_ttf-devel
BuildRequires: boost-devel >= 1.48.0
BuildRequires: cmake
BuildRequires: ctags
BuildRequires: desktop-file-utils 
BuildRequires: libappstream-glib
BuildRequires: gettext
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: glew-devel
BuildRequires: libpng-devel >= 1.6.0
BuildRequires: libcurl-devel
BuildRequires: minizip-ng-compat-devel
BuildRequires: python3
# For the %%build part generating the symlinks
BuildRequires: fontconfig %{fonts}
Requires:      hicolor-icon-theme
Requires:      %{fonts}

%description
Widelands is an open source (GPLed), realtime-strategy game, using SDL and
other free libraries, which is still under development. Widelands is inspired
by Settlers II (Bluebyte) and is partly similar to it, so if you know it, you
perhaps will have a thought, what Widelands is all about.


%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%ifarch s390x
%patch -P5 -p1
%endif


%build
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DWL_INSTALL_BASEDIR=%{_prefix}/share/%{name} \
    -DWL_INSTALL_DATADIR=%{_prefix}/share/%{name} \
    -DOPTION_BUILD_WEBSITE_TOOLS=OFF \
    %{nil}
%cmake_build


%install
%cmake_install

mkdir -p $RPM_BUILD_ROOT%{_bindir}
mv $RPM_BUILD_ROOT%{_prefix}/games/%{name} \
   $RPM_BUILD_ROOT%{_bindir}/%{name}

# Validate desktop file (provided by upstream)
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/*.desktop

# Validate appdata (provided by upstream)
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_metainfodir}/*.appdata.xml

pushd $RPM_BUILD_ROOT
# Replace fonts with system fonts. We used to have symlinks directly from
# i18n/fonts/<widelands-name> to the /usr/share/fonts/<system-font-name> dir
# but with recent font packaging changes this no longer works because e.g.
# Widelands expects all DejaVu fonts in a single dir, where as now there are
# separate /usr/share/fonts dirs for the sans, sans-mono and serif versions.
#
# Replacing the symlinks at the dir level with keeping the
# i18n/fonts/<widelands-name> directory and then putting symlinks to the
# invidual font-files inside that directory does not work, because on upgrade
# that would mean replacing a symlink with a dir which breaks horribly.
# So for those cases where we used to have a symlink, we create a new dir
# under i18n/fonts with a different name, with symlinks to the individual
# files in that dir; and then point the symlink to this new dir, to avoid
# the replace a symlink with a dir problem.
rm -r usr/share/%{name}/i18n/fonts/amiri
mkdir usr/share/%{name}/i18n/fonts/amiri-fonts
ln -s amiri-fonts usr/share/%{name}/i18n/fonts/amiri
ln -s $(fc-match -f "%{file}" "amiri") \
  usr/share/%{name}/i18n/fonts/amiri-fonts/amiri-regular.ttf
ln -s $(fc-match -f "%{file}" "amiri:bold") \
  usr/share/%{name}/i18n/fonts/amiri-fonts/amiri-bold.ttf
ln -s $(fc-match -f "%{file}" "amiri:italic") \
  usr/share/%{name}/i18n/fonts/amiri-fonts/amiri-slanted.ttf
ln -s $(fc-match -f "%{file}" "amiri:bold:italic") \
  usr/share/%{name}/i18n/fonts/amiri-fonts/amiri-boldslanted.ttf

rm -r usr/share/%{name}/i18n/fonts/DejaVu
mkdir usr/share/%{name}/i18n/fonts/dejavu-fonts
ln -s dejavu-fonts usr/share/%{name}/i18n/fonts/DejaVu
ln -s $(fc-match -f "%{file}" "sans") \
  usr/share/%{name}/i18n/fonts/dejavu-fonts/DejaVuSans.ttf
ln -s $(fc-match -f "%{file}" "sans:bold") \
  usr/share/%{name}/i18n/fonts/dejavu-fonts/DejaVuSans-Bold.ttf
ln -s $(fc-match -f "%{file}" "sans:italic") \
  usr/share/%{name}/i18n/fonts/dejavu-fonts/DejaVuSans-Oblique.ttf
ln -s $(fc-match -f "%{file}" "sans:bold:italic") \
  usr/share/%{name}/i18n/fonts/dejavu-fonts/DejaVuSans-BoldOblique.ttf
ln -s $(fc-match -f "%{file}" "serif") \
  usr/share/%{name}/i18n/fonts/dejavu-fonts/DejaVuSerif.ttf
ln -s $(fc-match -f "%{file}" "serif:bold") \
  usr/share/%{name}/i18n/fonts/dejavu-fonts/DejaVuSerif-Bold.ttf
ln -s $(fc-match -f "%{file}" "serif:italic") \
  usr/share/%{name}/i18n/fonts/dejavu-fonts/DejaVuSerif-Italic.ttf
ln -s $(fc-match -f "%{file}" "serif:bold:italic") \
  usr/share/%{name}/i18n/fonts/dejavu-fonts/DejaVuSerif-BoldItalic.ttf
ln -s $(fc-match -f "%{file}" "monospace") \
  usr/share/%{name}/i18n/fonts/dejavu-fonts/DejaVuSansMono.ttf
ln -s $(fc-match -f "%{file}" "monospace:bold") \
  usr/share/%{name}/i18n/fonts/dejavu-fonts/DejaVuSansMono-Bold.ttf
ln -s $(fc-match -f "%{file}" "monospace:italic") \
  usr/share/%{name}/i18n/fonts/dejavu-fonts/DejaVuSansMono-Oblique.ttf
ln -s $(fc-match -f "%{file}" "monospace:bold:italic") \
  usr/share/%{name}/i18n/fonts/dejavu-fonts/DejaVuSansMono-BoldOblique.ttf

# Chinese fonts
rm -r usr/share/%{name}/i18n/fonts/MicroHei
mkdir usr/share/%{name}/i18n/fonts/wqy-microhei-fonts
ln -s wqy-microhei-fonts usr/share/%{name}/i18n/fonts/MicroHei
ln -s $(fc-match -f "%{file}" "wenquanyimicrohei") \
   usr/share/%{name}/i18n/fonts/wqy-microhei-fonts/wqy-microhei.ttc

### IMPORTANT NOTE ###
# The fonts below never had a symlink to another font-dir shipped, so here we need
# to keep the usr/share/%%{name}/i18n/fonts/foo dir, rather then replace it with a link

# Devanagari (Hindu) fonts
# Fedora doesn't ship Nakula, but other Devanagari font sets.
# Gargi is a TTF font set and should be compatible.
rm -r usr/share/%{name}/i18n/fonts/Nakula/*
ln -s $(fc-match -f "%{file}" "gargi") \
   usr/share/%{name}/i18n/fonts/Nakula/nakula.ttf

# Hebrew fonts
rm -r usr/share/%{name}/i18n/fonts/Culmus/*
ln -s $(fc-match -f "%{file}" "frankruehlclm:bold") \
  usr/share/%{name}/i18n/fonts/Culmus/TaameyFrankCLM-Bold.ttf
ln -s $(fc-match -f "%{file}" "frankruehlclm:bold:italic") \
  usr/share/%{name}/i18n/fonts/Culmus/TaameyFrankCLM-BoldOblique.ttf
ln -s $(fc-match -f "%{file}" "frankruehlclm:medium") \
  usr/share/%{name}/i18n/fonts/Culmus/TaameyFrankCLM-Medium.ttf
ln -s $(fc-match -f "%{file}" "frankruehlclm:medium:italic") \
  usr/share/%{name}/i18n/fonts/Culmus/TaameyFrankCLM-MediumOblique.ttf

# In-game Latin fonts - shipped as a separate package
rm -r usr/share/%{name}/i18n/fonts/Widelands/*
ln -s $(fc-match -f "%{file}" "widelands") \
   usr/share/%{name}/i18n/fonts/Widelands/Widelands.ttf


# Scripting magic to add proper %%lang() markings to the locale files
find usr/share/widelands/locale/ -maxdepth 1 -type d -name \*_\* | sed -n 's#\(usr/share/widelands/locale/\(.*\)_.*\)#%lang(\2) /\1#p' > %{_builddir}/%{?buildsubdir}/%{name}.files
find usr/share/widelands/locale/ -maxdepth 1 -type d ! -name "*_*" | sed -n -e 's#\(usr/share/widelands/locale/\(.\+\)\)#%lang(\2) /\1#p' >> %{_builddir}/%{?buildsubdir}/%{name}.files
find usr/share/widelands/ -mindepth 1 -maxdepth 1 -not -name locale | sed -n 's#\(usr/share/widelands/*\)#/\1#p' >> %{_builddir}/%{?buildsubdir}/%{name}.files
popd


%files -f %{name}.files
%doc ChangeLog CREDITS
%license COPYING
%{_mandir}/man6/widelands.6.gz
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/*/apps/*.png
%{_metainfodir}/*.appdata.xml
%{_datadir}/applications/*.desktop
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/locale


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Dec 08 2024 Pete Walter <pwalter@fedoraproject.org> - 1.2-2
- Rebuild for ICU 76

* Sun Aug 25 2024 Peter Hanecak <hany@hany.sk> - 1.2-1
- New upstream release 1.2 (rhbz#2271240)

* Wed Aug 07 2024 Miroslav Suchý <msuchy@redhat.com> - 1.1-8
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 31 2024 Pete Walter <pwalter@fedoraproject.org> - 1.1-6
- Rebuild for ICU 74

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 04 2023 Lukas Javorsky <ljavorsk@redhat.com> - 1.1-4
- Rebuilt for minizip-ng transition Fedora change
- Fedora Change: https://fedoraproject.org/wiki/Changes/MinizipNGTransition

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 František Zatloukal <fzatlouk@redhat.com> - 1.1-2
- Rebuilt for ICU 73.2

* Mon Mar 27 2023 Hans de Goede <hdegoede@redhat.com> - 1.1-1
- New upstream release 1.1 (rhbz#2135131)
- Fix FTBFS (rhbz#2171759)

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 31 2022 Pete Walter <pwalter@fedoraproject.org> - 1.0-5
- Rebuild for ICU 72

* Sun Aug 14 2022 Hans de Goede <hdegoede@redhat.com> - 1.0-4
- Fix FTBFS (rhbz#2114565)

* Mon Aug 01 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.0-3
- Rebuilt for ICU 71.1

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Mar  6 2022 Hans de Goede <hdegoede@redhat.com> - 1.0-1
- New upstream release 1.0 (rhbz1974007)
- Fix FTBFS (rhbz2047116)

* Thu Feb 10 2022 Orion Poplawski <orion@nwra.com> - 0-0.89.build21
- Rebuild for glew 2.2

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.88.build21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Aug 07 2021 Jonathan Wakely <jwakely@redhat.com> - 0-0.87.build21
- Rebuilt for Boost 1.76

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.86.build21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu May 20 2021 Pete Walter <pwalter@fedoraproject.org> - 0-0.85.build21
- Rebuild for ICU 69

* Mon Apr 19 2021 Hans de Goede <hdegoede@redhat.com> - 0-0.84.build21
- Stop replacing dirs with symlinks this breaks upgrades again (rhbz 1947182)

* Sun Feb 7 2021 Andy Mender <andymenderunix@fedoraproject.org> - 0-0.83.build21
- Unbundle Culmus fonts
- Update to build21
- Clean up patches
- Point Source0 to GitHub release tarballs
- Fix new issues with fonts
- Use appdata and desktop file provided by upstream
- Update records in %%files section

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.82.build20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 0-0.81.build20
- Rebuilt for Boost 1.75

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.80.build20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 03 2020 Jonathan Wakely <jwakely@redhat.com> - 0-0.79.build20
- Rebuilt for Boost 1.73

* Sat May 16 2020 Pete Walter <pwalter@fedoraproject.org> - 0-0.78.build20
- Rebuild for ICU 67

* Thu Mar 19 2020 Hans de Goede <hdegoede@redhat.com> - 0-0.77.build20
- Stop replacing symlinks with dirs this breaks upgrades (rhbz 1806272)
- Use fc-match to generate font file symlinks to future proof the package
  against future font file-path or name changes (rhbz 1806272)

* Sat Mar  7 2020 Hans de Goede <hdegoede@redhat.com> - 0-0.76.build20
- Adjust Dejavu font symlinks for dejavu font package path changes
- Fix FTBFS (rhbz#1800251)

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.75.build20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Jeff Law <law@redhat.com> - 0-0.74.build20
- Work around false positive uninitialized variable warning from gcc10

* Fri Nov 01 2019 Pete Walter <pwalter@fedoraproject.org> - 0-0.73.build20
- Rebuild for ICU 65

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.72.build20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 14 2019 Hans de Goede <hdegoede@redhat.com> - 0-0.71.build20
- Update to new upstream Build20 release

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.70.build19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 0-0.69.build19
- Rebuilt for Boost 1.69

* Wed Jan 23 2019 Pete Walter <pwalter@fedoraproject.org> - 0-0.68.build19
- Rebuild for ICU 63

* Thu Aug 23 2018 Nicolas Chauvet <kwizart@gmail.com> - 0-0.67.build19
- Rebuilt for glew 2.1.0

* Tue Aug 14 2018 Hans de Goede <hdegoede@redhat.com> - 0-0.66.build19
- Fix FTBFS (rhbz#1606678)
- Add appdata

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.65.build19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Pete Walter <pwalter@fedoraproject.org> - 0-0.64.build19
- Rebuild for ICU 62

* Mon Apr 30 2018 Pete Walter <pwalter@fedoraproject.org> - 0-0.63.build19
- Rebuild for ICU 61.1

* Tue Feb 20 2018 Nils Philippsen <nils@tiptoe.de> - 0-0.62.build19
- require gcc, gcc-c++ for building
- FTBFS: build with --std=gnu++11 on ppc64le

* Thu Feb 08 2018 Hans de Goede <hdegoede@redhat.com> - 0-0.61.build19
- Update to new upstream Build19 release (rhbz#1397883)
- Strip 2012 and older changelog entries

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0-0.60.build18
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.59.build18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.58.build18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.57.build18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.56.build18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 0-0.55.build18
- Rebuilt for Boost 1.63

* Tue Jan 10 2017 Orion Poplawski <orion@cora.nwra.com> - 0-0.54.build18
- Rebuild for glew 2.0.0

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.53.build18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 16 2016 Jonathan Wakely <jwakely@redhat.com> - 0-0.52.build18
- Rebuilt for Boost 1.60

* Thu Jan 14 2016 Adam Jackson <ajax@redhat.com> - 0-0.51.build18
- Rebuild for glew 1.13

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 0-0.50.build18
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.49.build18
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 0-0.48.build18
- rebuild for Boost 1.58

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.47.build18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0-0.46.build18
- Rebuilt for GCC 5 C++11 ABI change

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 0-0.45.build18
- Rebuild for boost 1.57.0

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.44.build18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 13 2014 Hans de Goede <hdegoede@redhat.com> - 0-0.43.build18
- Update to new upstream Build18 release (rhbz#1085517)
- Rebuild for new SDL_gfx

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.42.build17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 0-0.41.build17
- Rebuild for boost 1.55.0

* Tue Dec 03 2013 Nils Philippsen <nils@redhat.com> - 0-0.40.build17
- use string literals as format strings (#1037384)

* Mon Nov 18 2013 Dave Airlie <airlied@redhat.com> - 0-0.39.build17
- rebuilt for GLEW 1.10

* Sun Aug 04 2013 Hans de Goede <hdegoede@redhat.com> - 0-0.38.build17
- Build with compat-lua on f20+

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.37.build17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 0-0.36.build17
- Rebuild for boost 1.54.0

* Sat Feb 09 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 0-0.35.build17
- Remove vendor tag from desktop file as per https://fedorahosted.org/fesco/ticket/1077
- Cleanup spec as per recently changed packaging guidelines
