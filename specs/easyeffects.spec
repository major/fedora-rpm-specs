Name:           easyeffects
Version:        8.0.8
Release:        2%{?dist}
Summary:        Audio effects for PipeWire applications

License:        GPL-3.0-or-later
Url:            https://github.com/wwmm/easyeffects
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

Provides:       pulseeffects = 6.1.1-1
Obsoletes:      pulseeffects < 6.1.1-1

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  itstool

# Qt dependencies
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Graphs)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6WebEngineQuick)

# KF dependencies
BuildRequires:  cmake(KF6ColorScheme)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(KF6QQC2DesktopStyle)

# QML dependencies
BuildRequires:  qt6qml(org.kde.kirigami)

# The rest...
BuildRequires:  cmake(TBB)

BuildRequires:  pkgconfig(libpipewire-0.3) >= 1.0.6
BuildRequires:  pkgconfig(lilv-0) >= 0.24
BuildRequires:  pkgconfig(libebur128) >= 1.2.6
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(fftw3f)
BuildRequires:  pkgconfig(speexdsp)
BuildRequires:  pkgconfig(nlohmann_json)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(libbs2b)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(rnnoise)
BuildRequires:  pkgconfig(soundtouch)
BuildRequires:  pkgconfig(libportal)
BuildRequires:  pkgconfig(libportal-qt6)
BuildRequires:  pkgconfig(webrtc-audio-processing-2)

BuildRequires:  zita-convolver-devel >= 3.1.0

BuildRequires:  ladspa-devel
BuildRequires:  pkgconfig(libmysofa)

# Visual style stuff
Requires:       breeze-icon-theme
## Default theme in code
Requires:       kf6-qqc2-desktop-style%{?_isa}
## Upstream recommendation
Recommends:     plasma-breeze%{?_isa}

# Required runtime QML modules
Requires:       qt6qml(org.kde.kirigami)
Requires:       qt6qml(org.kde.kirigamiaddons.components)
Requires:       qt6qml(QtGraphs)
Requires:       qt6qml(QtWebEngine)


Requires:       hicolor-icon-theme
Requires:       dbus-common

Recommends:     lv2-calf-plugins
Recommends:     lv2-mdala-plugins
Recommends:     lsp-plugins-lv2
Recommends:     lv2-zam-plugins


# Because of QtWebEngine dependency
ExclusiveArch:  %{qt6_qtwebengine_arches}


%description
Limiters, compressor, reverberation, high-pass filter, low pass filter,
equalizer many more effects for PipeWire applications.

%prep
%autosetup


%conf
%cmake


%build
%cmake_build


%install
%cmake_install

%find_lang %{name}


%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/com.github.wwmm.%{name}.metainfo.xml


%files -f %{name}.lang
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/com.github.wwmm.%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/com.github.wwmm.%{name}{,-symbolic}.svg
%{_datadir}/metainfo/com.github.wwmm.%{name}.metainfo.xml


%changelog
* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Mon Dec 22 2025 Vasiliy Glazov <vascom2@gmail.com> - 8.0.8-1
- Update to 8.0.8

* Wed Nov 19 2025 Neal Gompa <ngompa@fedoraproject.org> - 8.0.3-1
- Rebase to 8.0.3

* Wed Aug 06 2025 Vasiliy Glazov <vascom2@gmail.com> - 7.2.5-1
- Update to 7.2.5

* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sun Feb 02 2025 Orion Poplawski <orion@nwra.com> - 7.2.3-4
- Rebuild with gsl 2.8

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jan 09 2025 Michel Lind <salimma@fedoraproject.org> - 7.2.3-2
- Rebuilt for rubberband 4

* Thu Jan 09 2025 Vasiliy N. Glazov <vascom2@gmail.com> - 7.2.3-1
- Update to 7.2.3

* Wed Jan 08 2025 Yaakov Selkowitz <yselkowi@redhat.com> - 7.1.9-3
- Update plugin dependencies

* Mon Oct 07 2024 Vasiliy N. Glazov <vascom2@gmail.com> - 7.1.9-2
- Update to 7.1.9
- Make lv2-calf-plugins weak dependency (#2313553)

* Mon Jul 22 2024 Vasiliy N. Glazov <vascom2@gmail.com> - 7.1.7-1
- Update to 7.1.7

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Apr 01 2024 Vasiliy N. Glazov <vascom2@gmail.com> - 7.1.6-1
- Update to 7.1.6

* Mon Mar 25 2024 Vasiliy N. Glazov <vascom2@gmail.com> - 7.1.5-1
- Update to 7.1.5

* Tue Feb 06 2024 Vasiliy N. Glazov <vascom2@gmail.com> - 7.1.4-1
- Update to 7.1.4

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 17 2024 Jonathan Wakely <jwakely@redhat.com> - 7.1.3-2
- Rebuilt for TBB 2021.11

* Thu Nov 09 2023 Vasiliy N. Glazov <vascom2@gmail.com> - 7.1.3-1
- Update to 7.1.3

* Mon Oct 30 2023 Vasiliy N. Glazov <vascom2@gmail.com> - 7.1.1-1
- Update to 7.1.1

* Tue Sep 12 2023 Vasiliy N. Glazov <vascom2@gmail.com> - 7.1.0-1
- Update to 7.1.0

* Thu Aug 31 2023 Vasiliy N. Glazov <vascom2@gmail.com> - 7.0.8-1
- Update to 7.0.8

* Mon Aug 14 2023 Vasiliy N. Glazov <vascom2@gmail.com> - 7.0.7-1
- Update to 7.0.7

* Tue Aug 01 2023 Vasiliy N. Glazov <vascom2@gmail.com> - 7.0.6-1
- Update to 7.0.6

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 28 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 7.0.5-2
- Rebuilt due to fmt 10 update.

* Wed Jun 28 2023 Vasiliy N. Glazov <vascom2@gmail.com> - 7.0.5-1
- Update to 7.0.5

* Tue May 23 2023 Vasiliy N. Glazov <vascom2@gmail.com> - 7.0.4-1
- Update to 7.0.4

* Sat Apr 08 2023 Vasiliy N. Glazov <vascom2@gmail.com> - 7.0.3-1
- Update to 7.0.3

* Sun Feb 26 2023 Vasiliy N. Glazov <vascom2@gmail.com> - 7.0.1-1
- Update to 7.0.1

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 15 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 7.0.0-1
- Update to 7.0.0

* Mon Sep 19 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 6.3.0-1
- Update to 6.3.0

* Mon Aug 01 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 6.2.8-1
- Update to 6.2.8

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 6.2.7-1
- Update to 6.2.7

* Sun Jul 17 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 6.2.6-2
- Rebuild for new fmt

* Mon Jun 27 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 6.2.6-1
- Update to 6.2.6

* Thu May 05 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 6.2.5-1
- Update to 6.2.5

* Mon Mar 14 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 6.2.4-1
- Update to 6.2.4

* Mon Jan 31 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 6.2.3-1
- Update to 6.2.3

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 11 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 6.2.1-1
- Update to 6.2.1

* Thu Nov 25 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 6.1.5-1
- Update to 6.1.5

* Fri Sep 24 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 6.1.2-2
- Fix obsoleting pulseeffects

* Tue Sep 21 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 6.1.2-1
- Update to 6.1.2

* Sun Sep 19 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 6.1.1-1
- Initial packaging
