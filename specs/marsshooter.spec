%global __cmake_in_source_build 1

Summary:        M.A.R.S. - A Ridiculous Shooter
Name:           marsshooter
Version:        0.7.6
Release:        32%{?dist}
# Engine is GPLv3+, the libs under ext_libs_for_windows are LGPLv2+ / MPLv1.1
# but those are unused, so the resulting binary is pure GPLv3+
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://www.marsshooter.org/
Source0:        https://github.com/jwrdegoede/M.A.R.S./archive/%{name}-%{version}/%{name}-%{version}.tar.gz
Patch0:         %{name}-crash-fix.patch
Patch1:         %{name}-crash-fix2.patch
Patch2:         %{name}-waree-type.patch
Patch3:         %{name}-gcc11-fix.patch
# https://sources.debian.org/patches/marsshooter/0.7.6-4/avoid-crash-because-of-missing-return-statement.patch/
Patch4:         avoid-crash-because-of-missing-return-statement.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  dos2unix
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  SFML-devel
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(fribidi)
BuildRequires:  pkgconfig(taglib)

# Automate finding font paths at build time
%global fonts font(comfortaa) font(dejavusans) font(gargi) font(wenquanyimicrohei) font(waree)
BuildRequires:  fontconfig %{fonts}

Requires:       %{name}-data = %{version}-%{release}
Requires:       hicolor-icon-theme

%description
M.A.R.S. - a ridiculous shooter is a 2D space shooter with awesome visual
effects and attractive physics. Players can battle each other or computer
controlled enemies in exciting game modes:
    * awesome 2D-graphics with an unique style
    * a stunning amount of particles
    * single- and multi-player-support
    * an artificial intelligence using an aggro-system, which
      reacts differently upon varying situations
    * many impressive weapons
    * customizable ships
    * a very sexy GUI
    * several game modes: Space-ball, TeamDeathmatch, Cannonkeep,
      Deathmatch, Grave-Itation Pit


%package data
Summary:        Audio, icons and XML files for %{name}
License:        CC-BY and CC-BY-SA
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       %{fonts}

%description data
This package contains audio, icons and XML files for %{name}.


%prep
%autosetup -n M.A.R.S.-%{name}-%{version} -p1
rm -fr cmake data_src ext_libs_for_windows
for i in data/locales/Polish.txt \
         include/Interface/ComboBox.hpp src/Interface/ComboBox.cpp \
         include/Interface/DropDownWindow.hpp src/Interface/DropDownWindow.cpp \
         include/Items/PUSleep.hpp src/Items/PUSleep.cpp; do
  chmod -x $i;
done
dos2unix credits.txt license.txt


%build
%cmake -Dmars_DATA_DEST_DIR=%{_datadir}/%{name} -Dmars_EXE_DEST_DIR=%{_bindir} .
#make %%{?_smp_mflags}
%cmake_build


%install
%cmake_install
# This includes license files, remove it and pick up with %%license in %%files
rm -r %{buildroot}%{_docdir}
# Remove obsolete pixmap
rm %{buildroot}%{_datadir}/pixmaps/%{name}.xpm

# Replace bundled fonts with symlink to system fonts
ln -f -s $(fc-match -f "%{file}" "comfortaa") \
         %{buildroot}%{_datadir}/%{name}/fonts/Comfortaa-Regular.ttf
ln -f -s $(fc-match -f "%{file}" "dejavusans") \
         %{buildroot}%{_datadir}/%{name}/fonts/DejaVuSans.ttf
ln -f -s $(fc-match -f "%{file}" "gargi") \
         %{buildroot}%{_datadir}/%{name}/fonts/gargi.ttf
ln -f -s $(fc-match -f "%{file}" "waree") \
         %{buildroot}%{_datadir}/%{name}/fonts/Waree.ttf
mv %{buildroot}%{_datadir}/%{name}/fonts/Waree.ttf \
         %{buildroot}%{_datadir}/%{name}/fonts/Waree.otf
ln -f -s $(fc-match -f "%{file}" "wenquanyimicrohei") \
         %{buildroot}%{_datadir}/%{name}/fonts/wqy-microhei.ttc

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet \
  %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

%files
%doc README.md NEWS
%license license.txt
%{_bindir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_mandir}/man6/%{name}.6.gz

%files data
%license credits.txt music-license.eml
%{_datadir}/%{name}/

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.7.6-31
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Nov 05 2023 Sérgio Basto <sergio@serjux.com> - 0.7.6-27
- Rebuild for SFML-2.6.1

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug 04 2022 Martin Gansser <martinkg@fedoraproject.org> - 0.7.6-24
- Rebuilt for rawhide
- Add "%%global __cmake_in_source_build 1" due marsshooter doesn't support out-of-src tree builds

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 16 2021 Martin Gansser <martinkg@fedoraproject.org> - 0.7.6-19
- Add avoid-crash-because-of-missing-return-statement.patch to fix
  BotController::checkSpecial(): marsshooter killed by SIGABRT (BZ #1916705)

* Sat Dec 19 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.7.6-18
- Fixes FTBFS
- Add marsshooter-gcc11-fix.patch

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-17
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 14 2020 Bruno Wolff III <bruno@wolff.to> - 0.7.6-15
- Automate finding font files during build

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Aug 21 2019 Hans de Goede <hdegoede@redhat.com> - 0.7.6-13
- Fix crash in configfile parsing
- Add relevant license files to -data subpackage
- Fix some rpmlint warnings

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.6-8
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 19 2017 Hans de Goede <hdegoede@redhat.com> - 0.7.6-3
- Add a patch to hopefully fix:
  https://retrace.fedoraproject.org/faf/reports/729626/

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 10 2016 Hans de Goede <hdegoede@redhat.com> - 0.7.6-1
- Switch to new upstream: https://github.com/jwrdegoede/M.A.R.S.
- Update to 0.7.6 release:
 - Replace a few non-free fonts and sound files which accidentally
   slipped in with free alternatives
 - Add appdata

* Tue Jun 23 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.7.5-10.20140507gitc855d04
- Add some header to fix compilation with SFML 2.3

* Sat Jun 20 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.7.5-9.20140507gitc855d04
- dropped 'if' conditions for f23 build

* Mon Jun 08 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.7.5-8.20140507gitc855d04
- added 'if' conditions to fix f23 build

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.7.5-7.20140507gitc855d04
- Rebuilt for GCC 5 C++11 ABI change

* Wed Feb 25 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.7.5-6.20140507gitc855d04
- dropped CMAKE_INSTALL_PREFIX because already sets by %%cmake macro

* Sat Jan 03 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.7.5-5.20140507gitc855d04
- added %%{name}-data as requirement

* Fri Jan 02 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.7.5-4.20140507gitc855d04
- added Group tag
- package game files and data files separately
- fixed desktop file

* Fri Jan 02 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.7.5-3.20140507gitc855d04
- added %%{_datadir}/%%{name}/
- removed %%{_datadir}/icons/hicolor owned by hicolor-icon-theme
- added license.txt to %%license 

* Thu Jan 01 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.7.5-2.20140507gitc855d04
- added BR desktop-file-utils

* Wed Dec 31 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.7.5-1.20140507gitc855d04
- initial build for Fedora

