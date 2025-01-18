Name:           celluloid
Version:        0.27
Release:        3%{?dist}
Summary:        A simple GTK+ frontend for mpv

License:        GPL-3.0-or-later
URL:            https://github.com/celluloid-player/celluloid
Source0:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(glib-2.0) >= 2.44
BuildRequires:  pkgconfig(gtk4) >= 4.6.1
BuildRequires:  intltool >= 0.40.6
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  mpv-libs-devel
BuildRequires:  pkgconfig(libadwaita-1)
Requires:       yt-dlp
Requires:       hicolor-icon-theme
Requires:       dbus-common

Provides:       gnome-mpv = %{version}-%{release}
Obsoletes:      gnome-mpv < 0.17

%description
Celluloid (formerly GNOME MPV) is a simple GTK+ frontend for mpv.
It aims to be easy to use while maintaining high level of configurability.

%prep
%autosetup -p1

%build
%meson
pushd redhat-linux-build
    %ninja_build
popd

%install
pushd redhat-linux-build
    %ninja_install
popd
%find_lang %{name}

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/io.github.celluloid_player.Celluloid.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/io.github.celluloid_player.Celluloid.desktop

%files -f %{name}.lang
%doc AUTHORS README.md
%license COPYING
%{_bindir}/%{name}
%{_metainfodir}/io.github.celluloid_player.Celluloid.appdata.xml
%{_datadir}/applications/io.github.celluloid_player.Celluloid.desktop
%{_datadir}/dbus-1/services/io.github.celluloid_player.Celluloid.service
%{_datadir}/glib-2.0/schemas/io.github.celluloid_player.Celluloid.gschema.xml
%{_datadir}/icons/hicolor/*/apps/*.svg
 %{_mandir}/man1/%{name}.1.*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 24 2024 Vasiliy Glazov <vascom2@gmail.com> - 0.27-1
- Update to 0.27

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Sep 16 2023 Vasiliy Glazov <vascom2@gmail.com> - 0.26-1
- Update to 0.26

* Mon Jul 24 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 0.25-7
- Rebuilt due to libmpv 0.36 update.

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Mar 27 2023 Vasiliy N. Glazov <vascom2@gmail.com>  - 0.25-1
- Update to 0.25

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Nov 13 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 0.24-4
- Rebuilt due to mpv update.

* Fri Sep 09 2022 Vasiliy N. Glazov <vascom2@gmail.com>  - 0.24-3
- Require dbus-common

* Fri Sep 09 2022 Vasiliy N. Glazov <vascom2@gmail.com>  - 0.24-2
- Bump release for Fedora official repo

* Sun Aug 21 2022 Vasiliy N. Glazov <vascom2@gmail.com>  - 0.24-1
- Update to 0.24

* Sun Aug 07 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Mon Mar 07 2022 Vasiliy N. Glazov <vascom2@gmail.com>  - 0.23-1
- Update to 0.23

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 08 2021 Vasiliy N. Glazov <vascom2@gmail.com>  - 0.22-3
- Fix autofit triggering regardless of settings

* Tue Nov 16 2021 Vasiliy N. Glazov <vascom2@gmail.com>  - 0.22-2
- Switch to yt-dlp

* Fri Nov 05 2021 Vasiliy N. Glazov <vascom2@gmail.com>  - 0.22-1
- Update to 0.22

* Mon Aug 02 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Mar 22 2021 Vasiliy N. Glazov <vascom2@gmail.com>  - 0.21-1
- Update to 0.21

* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 23 2020 Leigh Scott <leigh123linux@gmail.com> - 0.20-2
- Rebuild for new mpv

* Sat Sep 19 2020 Vasiliy N. Glazov <vascom2@gmail.com>  - 0.20-1
- Update to 0.20

* Mon Aug 17 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 31 2020 Vasiliy N. Glazov <vascom2@gmail.com>  - 0.19-3
- Fix wayland blackscreen

* Tue Apr 21 2020 Vasiliy N. Glazov <vascom2@gmail.com>  - 0.19-2
- Enable LTO

* Thu Apr 09 2020 Vasiliy N. Glazov <vascom2@gmail.com>  - 0.19-1
- Update to 0.19

* Tue Feb 04 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 05 2019 Vasiliy N. Glazov <vascom2@gmail.com>  - 0.18-1
- Update to 0.18

* Mon Sep 23 2019 Vasiliy N. Glazov <vascom2@gmail.com>  - 0.17-2
- Fix crash #5392

* Fri Aug 09 2019 Vasiliy N. Glazov <vascom2@gmail.com>  - 0.17-1
- Update to 0.17
- Renamed gnome-mpv to celluloid
