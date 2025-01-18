Name: colobot
%global orgname info.colobot.Colobot

Version: 0.2.2
Release: 3%{?dist}
Summary: A video game that teaches programming in a fun way

License: GPL-3.0-only
URL: https://colobot.info

%global giturl https://github.com/colobot
%global gittag colobot-gold-%{version}-alpha
Source0: %{giturl}/colobot/archive/%{gittag}/colobot-%{gittag}.tar.gz
Source1: %{giturl}/colobot-data/archive/%{gittag}/colobot-data-%{gittag}.tar.gz
Source2: https://colobot.info/files/music/colobot-music_ogg_%{version}-alpha.tar.gz

# The game uses the translated string "Player" as the default player name
# yet it does not properly handle UTF-8 in player names,
# so non-English speakers may have the game always crash when putting in the player name.
#
# See: https://github.com/colobot/colobot/issues/1268 
Patch0: 0000-do-not-translate-default-player-name.patch

# Fix test compilation failure due to C++ "One Definition Rule" violation
Patch1: 0001-fix-test-compile-failure.patch

# Fix compilation failures due to GCC12 -Wrestrict warnings
# See: https://bugzilla.redhat.com/show_bug.cgi?id=2047428
Patch2: 0002-fix-gcc12-memcpy-restrict-warnings.patch

# Fix compilation failures due to GCC15 -Wpedantic errors
Patch3: 0003-gcc15-pedantic.patch

# Tests fail on ARM architectures. Needs some investigation.
%ifarch %{arm} aarch64
%global with_tests 0
%else
%global with_tests 1
%endif

BuildRequires: cmake >= 2.8
BuildRequires: desktop-file-utils
BuildRequires: gcc-c++
BuildRequires: libappstream-glib
BuildRequires: po4a
BuildRequires: xmlstarlet
BuildRequires: %{_bindir}/pod2man
BuildRequires: %{_bindir}/rsvg-convert

BuildRequires: boost-devel >= 1.51
BuildRequires: boost-filesystem >= 1.51
BuildRequires: boost-regex >= 1.51
BuildRequires: gettext-devel >= 0.18
BuildRequires: glew-devel >= 1.8.0
%if %{with_tests}
BuildRequires: gtest-devel
%endif
BuildRequires: libogg-devel >= 1.3.0
BuildRequires: libpng-devel >= 1.2
BuildRequires: libsndfile-devel >= 1.0.25
BuildRequires: libvorbis >= 1.3.2
BuildRequires: openal-soft-devel >= 1.13
BuildRequires: physfs-devel
BuildRequires: python3-devel
BuildRequires: SDL2-devel
BuildRequires: SDL2_image-devel
BuildRequires: SDL2_ttf-devel

Requires: colobot-data = %{version}-%{release}
Requires: colobot-music = %{version}-%{release}
Requires: hicolor-icon-theme

%description
Colobot: Gold Edition is a real-time strategy game, where you can program
your units (bots) in a language called CBOT, which is similar to C++ and Java.
Your mission is to find a new planet to live and survive.
You can save the humanity and get programming skills!


%package data
Summary: Data files for Colobot: Gold Edition
BuildArch: noarch

%description data
Data files (graphics, sounds, levels) required to run Colobot Gold.


%package music
Summary: Music for Colobot: Gold Edition
BuildArch: noarch

%description music
Music files used by Colobot Gold.


%prep
%autosetup -n colobot-%{gittag} -p1

# Unpack the -data tarball
rm -rf ./data
tar xzf %{SOURCE1}
mv ./colobot-data-%{gittag} ./data

# Unpack the -music tarball
pushd data/music
tar xzf %{SOURCE2}
popd

# Fix install paths
sed \
	-e 's|set(COLOBOT_INSTALL_BIN_DIR ${CMAKE_INSTALL_PREFIX}/games |set(COLOBOT_INSTALL_BIN_DIR %{_bindir}/ |' \
	-e 's|set(COLOBOT_INSTALL_LIB_DIR ${CMAKE_INSTALL_PREFIX}/lib/colobot |set(COLOBOT_INSTALL_LIB_DIR %{_libdir}/colobot |' \
	-e 's|set(COLOBOT_INSTALL_DATA_DIR ${CMAKE_INSTALL_PREFIX}/share/games/colobot |set(COLOBOT_INSTALL_DATA_DIR %{_datadir}/colobot |' \
	-e 's|set(COLOBOT_INSTALL_I18N_DIR ${CMAKE_INSTALL_PREFIX}/share/locale |set(COLOBOT_INSTALL_I18N_DIR %{_datadir}/locale |' \
	-e 's|set(COLOBOT_INSTALL_DOC_DIR ${CMAKE_INSTALL_PREFIX}/share/doc/colobot |set(COLOBOT_INSTALL_DOC_DIR %{_datadir}/doc/colobot |' \
	-i CMakeLists.txt


%build
%cmake \
	-DCMAKE_BUILD_TYPE=Release \
	-DDESKTOP=ON \
	-DPORTABLE=OFF \
	-DPYTHON_EXECUTABLE=%{__python3} \
	-DUSE_RELATIVE_PATHS=OFF \
	-DTESTS=%{with_tests}
%cmake_build


%install
%cmake_install

# Change the .desktop file name to match the .appdata.xml file name
mv %{buildroot}%{_datadir}/applications/%{name}.desktop %{buildroot}%{_datadir}/applications/%{orgname}.desktop
sed -e 's|%{name}.desktop|%{orgname}.desktop|' -i %{buildroot}%{_metainfodir}/%{orgname}.appdata.xml

%find_lang %{name} --with-man


%check
%if %{with_tests}
# Run unit tests. The test suite includes tests for parsing the .ini file,
# hence the test runner requires a colobot.ini file to read.
mkdir test-run-dir
cp -a --target-directory ./test-run-dir \
	test/unit/common/colobot.ini \
	%{_vpath_builddir}/colobot_ut
pushd test-run-dir
	./colobot_ut
popd
%endif

desktop-file-validate %{buildroot}%{_datadir}/applications/%{orgname}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{orgname}.appdata.xml


%files -f %{name}.lang
%license LICENSE.txt
%{_bindir}/%{name}
%{_libdir}/%{name}/

%{_datadir}/applications/%{orgname}.desktop
%{_metainfodir}/%{orgname}.appdata.xml

%{_datadir}/icons/hicolor/**/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_mandir}/man6/%{name}.6*


%files data
%license LICENSE.txt
%{_datadir}/%{name}/
%exclude %{_datadir}/%{name}/music


%files music
%license LICENSE.txt
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/music/


%changelog
* Thu Jan 16 2025 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.2.2-3
- Fix FTBFS

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Dec 23 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.2.2-1
- Update to v0.2.2

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 29 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Jonathan Wakely <jwakely@redhat.com> - 0.2.1-2
- Rebuilt for Boost 1.83

* Mon Aug 07 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.2.1-1
- Update to v0.2.1
- Drop Patch3 (missing <cstdint> includes - submitted and merged upstream)

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 0.2.0-10
- Rebuilt for Boost 1.81

* Thu Jan 19 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.2.0-9
- Add a patch to fix build failures with GCC13

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 27 2022 msuchy <msuchy@redhat.com> - 0.2.0-7
- migrate to SPDX license

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 0.2.0-5
- Rebuilt for Boost 1.78

* Sun Feb 20 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.2.0-4
- Add a patch to fix build failures with gcc-12

* Thu Feb 10 2022 Orion Poplawski <orion@nwra.com> - 0.2.0-3
- Rebuild for glew 2.2

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Aug 22 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.2.0-1
- Update to v0.2.0
- Drop Patch1 (missing includes - accepted upstream)
- Drop Patch2 (potential NULL casts - accepted upstream)
- Explicitly set some CMake options instead of relying on upstream defaults
- Build tests and run them in %%check

* Fri Aug 06 2021 Jonathan Wakely <jwakely@redhat.com> - 0.1.12-14
- Rebuilt for Boost 1.76

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.12-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.12-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 0.1.12-11
- Rebuilt for Boost 1.75

* Thu Sep 03 2020 Jeff Law <law@redhat.com> - 0.1.12-10
- Fix dynamic casts to avoid gcc-11 diagnostics

* Tue Jul 28 2020 Artur Iwicki <fedora@svgames.pl> - 0.1.12-9
- Update spec to use the new cmake_build and cmake_install macros

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Artur Iwicki <fedora@svgames.pl> - 0.1.12-7
- Edit Patch1 (missing includes) - fix build failures on Rawhide

* Fri Feb 07 2020 Artur Iwicki <fedora@svgames.pl> - 0.1.12-6
- Add a patch to fix build failures in Rawhide

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct 07 2019 Artur Iwicki <fedora@svgames.pl> - 0.1.12-4
- Make the game always use "Player" as the default player name
  (fixes the game crashing under certain system locale settings)
- Rename the .desktop file to match the .appdata.xml file name

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 24 2019 Artur Iwicki <fedora@svgames.pl> - 0.1.12-2
- Replace python3 BR with python3-devel
- Move music files to the fepdkg lookaside cache

* Sun Feb 24 2019 Artur Iwicki <fedora@svgames.pl> - 0.1.12-1
- Update to newest upstream release
- Drop Patch0 (appdata.xml file) - merged upstream
- Drop Patch1 (use snprintf() instead of sprintf()) - issue fixed upstream
- Drop Patch2 (strncpy() fix) - merged upstream

* Sat Feb 02 2019 Artur Iwicki <fedora@svgames.pl> - 0.1.11.1-8
- Add a patch for strncpy() usages

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.11.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 19 2018 Miro Hrončok <miro@hroncok.cz> - 0.1.11.1-7
- Use python3 during build instead of python2

* Tue Nov 13 2018 Artur Iwicki <fedora@svgames.pl> - 0.1.11.1-6
- Use %%find_lang for .mo files and man pages

* Thu Nov 08 2018 Artur Iwicki <fedora@svgames.pl> - 0.1.11.1-5
- Change the Summary: to something more descriptive
- Add a comment on music files
- Preserve timestamps on music files

* Thu Nov 08 2018 Artur Iwicki <fedora@svgames.pl> - 0.1.11.1-4
- Add a Requires: for hicolor-icon-theme
- Validate the desktop and appdata file

* Sun Nov 04 2018 Artur Iwicki <fedora@svgames.pl> - 0.1.11.1-3
- Fix build failures on F28 and later

* Mon Oct 29 2018 Artur Iwicki <fedora@svgames.pl> - 0.1.11.1-2
- Add an Appdata XML file
- Move music into a separate subpackage

* Tue Oct 16 2018 Artur Iwicki <fedora@svgames.pl> - 0.1.11.1-1
- Initial packaging
