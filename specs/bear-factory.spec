# https://github.com/j-jorge/bear/commit/2a785228d85997dc1682ee71899841528fa09c33
%global commit0 2a785228d85997dc1682ee71899841528fa09c33
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global srcname bear

Name:           %{srcname}-factory
Version:        0.7.0
Release:        0.48.20200220git%{shortcommit0}%{?dist}
Summary:        Game engine and editors dedicated to creating great 2D games
# Automatically converted from old format: GPLv3+ and CC-BY-SA - review is highly recommended.
License:        GPL-3.0-or-later AND LicenseRef-Callaway-CC-BY-SA
URL:            https://github.com/j-jorge/bear
Source0:        https://github.com/j-jorge/bear/archive/%{commit0}/%{name}-%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
# Boost 1.73 support
Patch0:         bear-engine-boost.patch
# Various crash fixes from https://github.com/jwrdegoede/bear
Patch1:         0001-Fix-text_layout-compute_line_width.patch
Patch2:         0002-Fix-text_metric-issues.patch
Patch3:         0003-gl_renderer-Protect-pause-unpause-against-unbalanced.patch
Patch4:         0004-sound_manager-Fix-segmentation-fault-due-to-invalid-.patch
Patch5:         0005-world-Fix-assertion-failure-in-physical_item-set_own.patch

# Build is broken on ppc64le
ExcludeArch:    ppc64le

BuildRequires:  gcc-c++
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-utils
BuildRequires:  gettext
BuildRequires:  libclaw-devel >= 1.7.4-17
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  wxGTK-devel
Requires:       hicolor-icon-theme

%description
The Bear engine is a set of C++ libraries and tools dedicated to creating
great 2D games. It has been used to create Plee the Bear (plee-the-bear),
Andy's Super Great Park (asgp) and Tunnel (tunnel).

The engine comes with a set of tools, namely the Bear Factory, intended to
help creating resources for the game. These tools include a level editor,
a character/model editor and an animation editor.

%package -n %{srcname}-engine
Summary: Run-time libraries for games based on the Bear engine

%description -n %{srcname}-engine
The Bear engine is a set of C++ libraries and tools dedicated to creating
great 2D games. It has been used to create Plee the Bear (plee-the-bear),
Andy's Super Great Park (asgp) and Tunnel (tunnel).

This package contains the run-time libraries used by the games based on
the Bear engine.

%package devel
Summary: Development files for %{name}
Requires: %{srcname}-engine%{?_isa} = %{version}-%{release}

%description devel
Development files for %{name}

%prep
%autosetup -p1 -n %{srcname}-%{commit0}

# change docbook_to_man to docbook2man
sed -i -e 's|docbook-to-man|docbook2man|g' cmake-helper/docbook-to-man.cmake

# delete glew code because it picks up BSD license
rm -rf bear-engine/core/src/visual/glew/

%build
# https://github.com/j-jorge/bear/issues/9
# The Bear Factory (i.e. the editors for the Bear Engine) requires wiWidgets < 3.
# Changes in the API of wxWidgets broke some parts of the editors.
# The editor needs to be disabled with -DBEAR_EDITORS_ENABLED=0
%cmake -DBEAR_ENGINE_INSTALL_LIBRARY_DIR=%{_lib} \
       -DBEAR_FACTORY_INSTALL_LIBRARY_DIR=%{_lib} \
       -DCMAKE_SHARED_LINKER_FLAGS="-Wl,--as-needed" \
       -DCMAKE_SKIP_RPATH:BOOL=ON \
       -DBEAR_USES_FREEDESKTOP=ON \
       -DRUNNING_BEAR_ENABLED=ON \
       -DBEAR_EDITORS_ENABLED=0
%cmake_build

%install
%cmake_install

%find_lang bear-engine

# copy devel files for subpkg bear-devel
install -dm 755 %{buildroot}%{_includedir}/%{name}/cmake-helper/
install -D cmake-helper/{*.cmake,*.cmake.in} %{buildroot}%{_includedir}/%{name}/cmake-helper/
for file in $(find bear-engine/{core,lib}/src -name *.hpp -o -name *.tpp);
do
    install -Dm 0644 $file %{buildroot}%{_includedir}/%{name}/$file
done
# fixes E: script-without-shebang
chmod a-x %{buildroot}%{_includedir}/%{name}/cmake-helper/*.cmake*

rm -rf %{buildroot}%{_datadir}/pixmaps

install -d -m 0755 %{buildroot}%{_datadir}/applications/
install -Dm644 %{_builddir}/%{srcname}-%{commit0}/bear-factory/desktop/applications/*.desktop %{buildroot}%{_datadir}/applications/

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%doc README.md
%license LICENSE license/CCPL license/GPL
#{_bindir}/bend-image
#{_bindir}/image-cutter
#{_bindir}/bf*editor
#{_libdir}/libbear-editor.so
#{_datadir}/#{name}
#{_datadir}/icons/hicolor/*/apps/#{name}.png
%{_datadir}/applications/desc2img.desktop
%{_datadir}/applications/bf*editor.desktop
#{_mandir}/man1/bf*editor.1*

%files -n %{srcname}-engine -f %{srcname}-engine.lang
%doc README.md
%license LICENSE license/CCPL license/GPL
%{_bindir}/running-bear
%{_libdir}/libbear_*.so
#{_libdir}/libbear-editor.so
%{_mandir}/man6/running-bear.6*

%files devel
%doc README.md
%{_includedir}/%{name}
%{_datadir}/cmake/%{srcname}-engine

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-0.48.20200220git2a78522
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 0.7.0-0.47.20200220git2a78522
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-0.46.20200220git2a78522
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-0.45.20200220git2a78522
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-0.44.20200220git2a78522
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 17 2024 Jonathan Wakely <jwakely@redhat.com> - 0.7.0-0.43.20200220git2a78522
- Rebuilt for Boost 1.83

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-0.42.20200220git2a78522
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 0.7.0-0.41.20200220git2a78522
- Rebuilt for Boost 1.81

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-0.40.20200220git2a78522
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Sep 12 2022 Scott Talbert <swt@techie.net> - 0.7.0-0.39.20200220git2a78522
- Rebuild with wxWidgets 3.2

* Thu Aug 11 2022 Hans de Goede <hdegoede@redhat.com> - 0.7.0-0.38.20200220git2a78522
- Fix various crashes in plee-the-bear

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-0.37.20200220git2a78522
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 0.7.0-0.36.20200220git2a78522
- Rebuilt for Boost 1.78

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-0.35.20200220git2a78522
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Aug 06 2021 Jonathan Wakely <jwakely@redhat.com> - 0.7.0-0.34.20200220git2a78522
- Rebuilt for Boost 1.76

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-0.33.20200220git2a78522
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-0.32.20200220git2a78522
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 0.7.0-0.31.20200220git2a78522
- Rebuilt for Boost 1.75

* Thu Aug 06 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.7.0-0.30.20200220git2a78522
- Fixes FTBFS

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-0.29.20200220git2a78522
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-0.28.20200220git2a78522
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.7.0-0.27.20200220git2a78522
- Update to 0.7.0-0.27.20200220git2a78522
- Add Boost bear-engine-boost.patch to fix (RHBZ#1849442)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-0.26.20180825git2a78522
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-0.25.20180825git2a78522
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-0.24.20180825git2a78522
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 15 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.7.0-0.23.20180825git2a78522
- Make install preserve timestamps
- Remove obsolete bear <= 0.7.0-0.21 because there was never a bear package

* Fri Oct 12 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.7.0-0.22.20180825git2a78522
- Use global macro srcname bear
- Correct sub-package naming

* Fri Oct 12 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.7.0-0.21.20180825git2a78522
- Add BR gcc-c++
- Remove scriptlets
- Add -Wl,--as-needed" to avoid "unused-direct-shlib-dependency" warnings
- Rename subpackage engine to bear-engine
- Disable the bear editor with -DBEAR_EDITORS_ENABLED=0

* Sat Jan 27 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.7.0-0.20.20170906git40f2158
- Update to 0.7.0-0.20.20170906git40f2158
- Rename package to bear-factory

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 0.7.0-0.19.20161230git781ec80
- Rebuilt for Boost 1.66

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.0-0.18.20161230git781ec80
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-0.17.20161230git781ec80
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-0.16.20161230git781ec80
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Jonathan Wakely <jwakely@redhat.com> - 0.7.0-0.15.20161230git781ec80
- Rebuilt for s390x binutils bug

* Tue Jul 18 2017 Jonathan Wakely <jwakely@redhat.com> - 0.7.0-0.14.20161230git781ec80
- Rebuilt for Boost 1.64

* Wed Feb 01 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.7.0-0.13.20161230git
- rebuild for rawhide, with libclaw-devel >= 1.7.4-17

* Sat Jan 14 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.7.0-0.12.20161230git
- remove %%{name}-engine-%%{_arch}.conf %%{name}-factory-%%{_arch}.conf
- add missing /sbin/ldconfig calls in %%post and %%postun
- add CMAKE option -DRUNNING_BEAR_ENABLED=ON for missing running-bear file
- add %%{_bindir}/running-%%{name} to engine file section
- install engine libraries into -DBEAR_ENGINE_INSTALL_LIBRARY_DIR=%%{_lib}
- install factory libraries into -DBEAR_FACTORY_INSTALL_LIBRARY_DIR=%%{_lib}

* Mon Jan  9 2017 Michael Schwendt <mschwendt@fedoraproject.org> - 0.7.0-0.11.20161230git
- fix Release tag to include snapshot checkout date
- prepare rebuild against libclaw >= 1.7.4-16 for fix ABI compatibility

* Mon Jan 02 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.7.0-0.10git781ec80
- add RR hicolor-icon-theme

* Fri Dec 30 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.7.0-0.9git781ec80
- update to 0.7.0-0.9git781ec80

* Tue Dec 27 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.7.0-0.8gitac6be8b
- add if condition due ppc64le build problem

* Fri Dec 23 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.7.0-0.7gitac6be8b
- change to -DCMAKE_SKIP_RPATH:BOOL=ON
- obsolete chrpath command
- convert docbook2man filename taken from .sgml file to lowercase
- remove BR chrpath

* Tue Dec 13 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.7.0-0.6gitac6be8b
- use wildcard to copy all cmake and cmake.in files for subpkg bear-devel
- copy also *.tpp files for subpkg bear-devel
- fix spurious-executable-perm
- fixes E: script-without-shebang
- specfile cleanup

* Tue Dec 13 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.7.0-0.5gitac6be8b
- Dropped subpkg engine/factory-devel because unversioned files needed at runtime
- Add subpkg %%{name}-devel

* Mon Dec 12 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.7.0-0.4gitac6be8b
- Add Requires: %%{name}-engine%%{?_isa} = %%{version}-%%{release} to bear-factory
- Delete glew code because it picks up BSD license
- run-time is the correct spelling, not runtime
- Add gtk-update-icon-cache in %%postun and %%posttrans section for bear-factory
- Add update-desktop-database in %%post and %%postun section for bear-factory
- Take ownership of %%dir %%{_datadir}/%%{name}-factory/images/
  %%dir %%{_datadir}/%%{name}-factory/item-description/
  %%dir %%{_datadir}/%%{name}-factory//item-description/generic in file section
- Add subpkg engine/factory-devel for unversioned files

* Mon Nov 28 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.7.0-0.3gitac6be8b
- Add BR chrpath
- Add BR libjpeg-turbo-devel
- Add BuildConflicts wxGTK3-devel

* Sun Nov 27 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.7.0-0.2gitac6be8b
- Remove Conflicts: wxGTK3-devel"
- Compressed sed command
- replace (non packaged) with (tunnel) from the descriptions
- replace (andy-super-great-park) with (asgp) from the descriptions
- run-time is the correct spelling, not runtime
- Add %%config to fix the non-conffile-in-etc warnings
- Remove desc2img.desktop due desc2img binary missing

* Sun Nov 27 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.7.0-0.1gitac6be8b
- imported package bear
