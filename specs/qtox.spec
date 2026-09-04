Name:       qtox
Version:    1.18.5
Release:    3%{?dist}
Summary:    Feature-rich Tox client

# Main program: GPLv3+
# src/widget/flowlayout.*: BSD-3-Clause
# Smileys/Universe Smileys/emojione: CC-BY-4.0 and MIT
# Smileys/Classic: CC-BY-SA-4.0
License:    GPL-3.0-or-later AND BSD-3-Clause AND MIT AND CC-BY-4.0 AND CC-BY-SA-4.0
URL:        https://github.com/TokTok/qTox/
Source0:    %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  cmake(Qt6)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(KF6Sonnet)
BuildRequires:  qtsingleapplication-qt6-devel
BuildRequires:  pkgconfig(toxcore) >= 0.2.10
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libv4l2)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(libqrencode)
BuildRequires:  pkgconfig(sqlcipher)
BuildRequires:  pkgconfig(filteraudio)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(xscrnsaver)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(libsodium)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(vpx)
Requires:       hicolor-icon-theme
Requires:       toxcore >= 0.2.10

%description
qTox is a powerful Tox client that follows the Tox design
guidelines while running on all major platforms.

%prep
%autosetup -p1 -n qTox-%{version}

%build
%cmake \
 -DUPDATE_CHECK=OFF \
 -DGIT_DESCRIBE=%{version}
%cmake_build

%install
%cmake_install

%check
# test_bsu requires network connectivity
%ctest --exclude-regex test_bsu
desktop-file-validate %{buildroot}%{_datadir}/applications/io.github.qtox.qTox.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/io.github.qtox.qTox.appdata.xml

%files
%license LICENSE smileys/Universe/LICENSE-GRAPHICS
%doc README.md CHANGELOG.md
%{_bindir}/qtox
%{_metainfodir}/io.github.qtox.qTox.appdata.xml
%{_datadir}/applications/io.github.qtox.qTox.desktop
%{_datadir}/icons/hicolor/*/apps/qtox.*

%changelog
* Thu Sep 03 2026 Dominik Mierzejewski <dominik@greysector.net> - 1.18.5-3
- Rebuilt for FFmpeg 9

* Sat Jun 06 2026 Dominik Mierzejewski <dominik@greysector.net> - 1.18.5-2
- Use generic dependency names
- Run tests using standard macro and stop ignoring failures
- Skip test_bsu which requires network connectivity
- Add missing build dependency on libv4l
- Drop non-existent CMake option
- Use SPDX expression in License: tag

* Fri Jun 05 2026 Nikolay 168 <nick975@rpmfusion.org> - 1.18.5-1
- Update qtox to 1.18.5

* Fri Feb 27 2026 Nikolay 168 <nick975@rpmfusion.org> - 1.18.4-1
- Update qtox to 1.18.4

* Mon Feb 02 2026 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.18.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Thu Nov 06 2025 Leigh Scott <leigh123linux@gmail.com> - 1.18.3-3
- Rebuild for ffmpeg-8.0

* Sun Jul 27 2025 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.18.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sun Mar 23 2025 Sérgio Basto <sergio@serjux.com> - 1.18.3-1
- Update qtox to 1.18.3

* Tue Jan 28 2025 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.17.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Nov 28 2024 Nikolay 168 <nick975@rpmfusion.org> - 1.17.8-1
- Rebuild for new version
- Stability fixes

* Wed Nov 06 2024 Sérgio Basto <sergio@serjux.com> - 1.17.6-9
- Rebuild for ffmpeg-7
- Add qTox-1.17.6-ffmpeg7.patch (Mamoru TASAKA) from rfbz #7096

* Fri Aug 02 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.17.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Feb 04 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.17.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 02 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.17.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 01 2023 Leigh Scott <leigh123linux@gmail.com> - 1.17.6-5
- Rebuild for new ffmpeg

* Wed Feb 08 2023 Leigh Scott <leigh123linux@gmail.com> - 1.17.6-4
- rebuilt

* Sun Aug 07 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.17.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Tue May 17 2022 Leigh Scott <leigh123linux@gmail.com> - 1.17.6-2
- Fix crash (rfbz#6301)

* Thu Apr 07 2022 Leigh Scott <leigh123linux@gmail.com> - 1.17.6-1
- Update to 1.17.6

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.17.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Nov 12 2021 Leigh Scott <leigh123linux@gmail.com> - 1.17.3-5
- Rebuilt for new ffmpeg snapshot

* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.17.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.17.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan  1 2021 Leigh Scott <leigh123linux@gmail.com> - 1.17.3-2
- Rebuilt for new ffmpeg snapshot

* Sat Dec 05 22:19:55 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.17.3-1
- Update to 1.17.3

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.16.3-5.20191018gita44cce6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Feb 22 2020 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1.16.3-4.20191018gita44cce6
- Rebuild for ffmpeg-4.3 git

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.16.3-3.20191018gita44cce6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 18 17:59:35 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.16.3-2.20191018gita44cce6
- Pre-release a44cce65beb60c5f280b651e0c084fa9c2bdb0dc
- Update BuildRequires

* Sun Sep 22 19:59:25 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.16.3-1.20190922gitaf02542
- Pre-release af02542e05992bf94fcff37c365f638ad7b53d8d

* Wed Aug 07 2019 Leigh Scott <leigh123linux@gmail.com> - 1.16.2-4
- Rebuild for new ffmpeg version

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.16.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 27 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.16.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 17 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.16.2-1
- Upstream release 1.16.2

* Tue Jul 03 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.16.0-1
- Upstream release 1.16.0

* Tue Jun 26 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.15.0-3
- Rebuilt for toxcore soname bump

* Thu May 10 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.15.0-2
- Rebuild with new Toxcore

* Thu Apr 19 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.15.0-1
- Upstream release 1.15.0

* Thu Apr 19 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.14.1-1
- Upstream release 1.14.1

* Fri Feb 16 2018 Robert-André Mauchin <zebob.m@gmail.com> 1.13.0-2
- Spec file refresh
- Move Appdata to metainfo

* Mon Nov 27 2017 Robert-André Mauchin <zebob.m@gmail.com> 1.13.0-1
- New upstream release 1.13.0

* Thu Oct 12 2017 Robert-André Mauchin <zebob.m@gmail.com> 1.12.1-1
- New upstream release 1.12.1

* Fri Aug 18 2017 Robert-André Mauchin <zebob.m@gmail.com> 1.11.0-2
- Fix typo

* Sat Jul 29 2017 Robert-André Mauchin <zebob.m@gmail.com> 1.11.0-1
- First RPM release
