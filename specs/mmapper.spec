Name:           mmapper
Version:        24.03.1
Release:        4%{?dist}
Summary:        Graphical MUME mapper

License:        GPL-2.0-or-later
URL:            https://github.com/MUME/MMapper
Source0:        https://github.com/MUME/MMapper/archive/v%{version}/MMapper-%{version}.tar.gz
Source1:        https://github.com/g-truc/glm/releases/download/0.9.9.7/glm-0.9.9.7.zip
Patch0:         %{name}-miniupnp228.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  /usr/bin/appstream-util
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  miniupnpc-devel
BuildRequires:  openssl-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  zlib-devel

Requires:       hicolor-icon-theme

Provides:       bundled(glm) = 0.9.9.7

%description
MMapper is a graphical mapper for a MUD named MUME (Multi-Users in Middle
Earth). The game is traditionally played in a text-only mode, but MMapper tries
to represent the virtual world in user-friendly graphical environment. It acts
as a proxy between a telnet client and a MUD server, being able to analyze game
data in real time and show player's position in a map.


%prep
%autosetup -p1 -n MMapper-%{version}


%build
mkdir -p %{__cmake_builddir}/external/glm/glm-prefix/src
cp -a %{S:1} %{__cmake_builddir}/external/glm/glm-prefix/src/

%{cmake} \
  -DCMAKE_BUILD_TYPE=Release \
  -DWITH_MAP=OFF \
  -DWITH_UPDATER=OFF \
  %{nil}

%cmake_build


%install
%cmake_install


%check
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_datadir}/metainfo/org.mume.MMapper.appdata.xml
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.mume.MMapper.desktop


%files
%license COPYING.txt
%doc NEWS.txt
%{_bindir}/mmapper
%{_datadir}/applications/org.mume.MMapper.desktop
%{_datadir}/icons/hicolor/*/apps/org.mume.MMapper.png
%{_datadir}/metainfo/org.mume.MMapper.appdata.xml


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 24.03.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Oct 08 2024 Simone Caronni <negativo17@gmail.com> - 24.03.1-3
- Rebuild for updated miniupnpc.

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.03.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Mar 11 2024 Kalev Lember <klember@redhat.com> - 24.03.1-1
- Update to 24.03.1
- Switch to SPDX license identifiers
- ExcludeArch i686 for https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 23.05.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 23.05.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 23.05.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue May 02 2023 Kalev Lember <klember@redhat.com> - 23.05.0-1
- Update to 23.05.0

* Sun Mar 19 2023 Kalev Lember <klember@redhat.com> - 23.03.0-1
- Update to 23.03.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 23.01.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Jan 01 2023 Kalev Lember <klember@redhat.com> - 23.01.0-1
- Update to 23.01.0

* Sat Dec 31 2022 Kalev Lember <klember@redhat.com> - 22.12.1-1
- Update to 22.12.1

* Mon Dec 05 2022 Kalev Lember <klember@redhat.com> - 22.12.0-1
- Update to 22.12.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 22.05.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat May 07 2022 Kalev Lember <klember@redhat.com> - 22.05.0-1
- Update to 22.05.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 21.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 07 2021 Kalev Lember <klember@redhat.com> - 21.12.1-1
- Update to 21.12.1

* Mon Dec 06 2021 Kalev Lember <klember@redhat.com> - 21.12.0-1
- Update to 21.12.0

* Sat Oct 02 2021 Kalev Lember <klember@redhat.com> - 21.09.2-1
- Update to 21.09.2

* Sun Sep 26 2021 Kalev Lember <klember@redhat.com> - 21.09.0-1
- Update to 21.09.0

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 21.08.0-2
- Rebuilt with OpenSSL 3.0.0

* Tue Aug 10 2021 Kalev Lember <klember@redhat.com> - 21.08.0-1
- Update to 21.08.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 21.06.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 31 2021 Kalev Lember <klember@redhat.com> - 21.06.0-1
- Update to 21.06.0

* Tue Mar 30 2021 Jonathan Wakely <jwakely@redhat.com> - 21.01.0-3
- Rebuilt for removed libstdc++ symbol (#1937698)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 21.01.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 18 2021 Kalev Lember <klember@redhat.com> - 21.01.0-1
- Update to 21.01.0

* Thu Oct 15 2020 Jeff Law <law@redhat.com> - 20.10.0-2
- Add missing #include for gcc-11

* Wed Oct 14 2020 Kalev Lember <klember@redhat.com> - 20.10.0-1
- Update to 20.10.0

* Wed Aug 26 2020 Kalev Lember <klember@redhat.com> - 20.08.0-1
- Update to 20.08.0

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20.05.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20.05.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 21 2020 Kalev Lember <klember@redhat.com> - 20.05.0-1
- Update to 20.05.0

* Mon Mar 30 2020 Kalev Lember <klember@redhat.com> - 20.03.0-1
- Update to 20.03.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 01 2020 Kalev Lember <klember@redhat.com> - 19.12.1-1
- Update to 19.12.1

* Tue Dec 31 2019 Kalev Lember <klember@redhat.com> - 19.12.0-1
- Update to 19.12.0

* Sat Dec 14 2019 Jeff Law <law@redhat.com> - 19.10.1-2
- Fix missing #include for gcc-10

* Fri Nov 01 2019 Kalev Lember <klember@redhat.com> - 19.10.1-1
- Update to 19.10.1

* Sat Oct 26 2019 Kalev Lember <klember@redhat.com> - 19.10.0-1
- Update to 19.10.0
- Disable github version checks

* Wed Aug 28 2019 Kalev Lember <klember@redhat.com> - 19.04.0-1
- Update to 19.04.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Apr 06 2019 Kalev Lember <klember@redhat.com> - 2.8.0-1
- Update to 2.8.0

* Sun Feb 10 2019 Kalev Lember <klember@redhat.com> - 2.7.4-3
- Rebuilt for miniupnpc soname bump

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 03 2019 Kalev Lember <klember@redhat.com> - 2.7.4-1
- Update to 2.7.4

* Thu Dec 27 2018 Kalev Lember <klember@redhat.com> - 2.7.3-1
- Update to 2.7.3

* Mon Dec 10 2018 Kalev Lember <klember@redhat.com> - 2.7.2-1
- Update to 2.7.2

* Sat Dec 01 2018 Kalev Lember <klember@redhat.com> - 2.7.1-1
- Update to 2.7.1

* Tue Nov 27 2018 Kalev Lember <klember@redhat.com> - 2.7.0-1
- Update to 2.7.0

* Tue Nov 13 2018 Kalev Lember <klember@redhat.com> - 2.6.3-1
- Update to 2.6.3

* Sat Oct 27 2018 Kalev Lember <klember@redhat.com> - 2.6.2-1
- Update to 2.6.2

* Sun Oct 14 2018 Kalev Lember <klember@redhat.com> - 2.6.1-1
- Update to 2.6.1

* Sat Sep 29 2018 Kalev Lember <klember@redhat.com> - 2.6.0-1
- Update to 2.6.0
- Remove bundled QtIOCompressor now that mmapper is ported to use zlib

* Mon Aug 20 2018 Kalev Lember <klember@redhat.com> - 2.5.3-1
- Update to 2.5.3

* Sun Aug 12 2018 Kalev Lember <klember@redhat.com> - 2.5.2-1
- Update to 2.5.2

* Wed Aug 08 2018 Kalev Lember <klember@redhat.com> - 2.5.1-1
- Update to 2.5.1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 16 2018 Kalev Lember <klember@redhat.com> - 2.5.0-2
- Use bundled QtIOCompressor as the packaged one is only for Qt4

* Tue May 15 2018 Kalev Lember <klember@redhat.com> - 2.5.0-1
- Update to 2.5.0
- Set cmake build type as "Release"

* Wed Mar 07 2018 Adam Williamson <awilliam@redhat.com> - 2.4.5-2
- Rebuild to fix GCC 8 mis-compilation
  See https://da.gd/YJVwk ("GCC 8 ABI change on x86_64")

* Mon Feb 12 2018 Kalev Lember <klember@redhat.com> - 2.4.5-1
- Update to 2.4.5
- Use %%autosetup and %%make_build and %%make_install macros

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Kalev Lember <klember@redhat.com> - 2.4.4-1
- Update to 2.4.4

* Wed Jan 17 2018 Kalev Lember <klember@redhat.com> - 2.4.3-1
- Update to 2.4.3
- Add appdata file
- Remove obsolete icon cache scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 29 2015 Kalev Lember <klember@redhat.com> - 2.3.6-1
- Update to 2.3.6

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.3.4-1
- Update to 2.3.4
- Update upstream URL
- Switch to qt5
- Use license macro for the COPYING.txt file

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 14 2013 Kalev Lember <kalevlember@gmail.com> - 2.2.1-1
- Update to 2.2.1

* Sat Jul 13 2013 Kalev Lember <kalevlember@gmail.com> - 2.2.0-1
- Update to 2.2.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jul 22 2011 Kalev Lember <kalevlember@gmail.com> - 2.1.0-4
- Updated the mirrored textures patch for Qt >= 4.8

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 06 2011 Kalev Lember <kalev@smartlink.ee> - 2.1.0-2
- Added patch to fix mirrored textures with Qt >= 4.6

* Mon Aug 23 2010 Kalev Lember <kalev@smartlink.ee> - 2.1.0-1
- Update to 2.1.0
- Dropped upstreamed patches
- Use system copy of qtiocompressor

* Thu Feb 25 2010 Kalev Lember <kalev@smartlink.ee> - 2.0.4-5.final2
- Added patch to fix renderer crash with Qt 4.6
- patch to fix linking with the new --no-add-needed default

* Thu Feb 25 2010 Kalev Lember <kalev@smartlink.ee> - 2.0.4-4.final2
- Rebuilt with Qt 4.6

* Mon Nov 23 2009 Kalev Lember <kalev@smartlink.ee> - 2.0.4-3.final2
- Updated source URL.

* Tue Aug 11 2009 Kalev Lember <kalev@smartlink.ee> - 2.0.4-2.final2
- Changed license tag to read "GPLv2" as there is GPLv2-only code in the mix.

* Fri Aug 07 2009 Kalev Lember <kalev@smartlink.ee> - 2.0.4-1.final2
- Initial RPM release.
