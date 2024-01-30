Name:           rpi-imager
Version:        1.8.5
Release:        1%{?dist}
Summary:        Graphical user-interface to write disk images and format SD cards

License:        ASL 2.0
URL:            https://github.com/raspberrypi/%{name}
Source0:        %{URL}/archive/v%{version}/%{name}.tar.gz#/%{name}-%{version}.tar.gz

#https://github.com/raspberrypi/rpi-imager/blob/qml/src/CMakeLists.txt#L95
ExcludeArch:    s390x

# Needed to validate the desktop and metainfo files
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils

BuildRequires:  sudo
BuildRequires:  git
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  libarchive-devel
BuildRequires:  libcurl-devel
BuildRequires:  lzma-sdk-devel
BuildRequires:  openssl-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtquickcontrols2-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-linguist
BuildRequires:  xz-devel
BuildRequires:  libdrm-devel

# Needed because we don't own /usr/share/icons/hicolor
Requires:       hicolor-icon-theme
# Needed if you want to be able to run rpi-imager as a regular user
Recommends:     udisks2

Requires:       dosfstools
Requires:       qt5-qtbase
Requires:       qt5-qtbase-gui
Requires:       qt5-qtdeclarative
Requires:       qt5-qtgraphicaleffects
Requires:       qt5-qtsvg
Requires:       qt5-qtquickcontrols2
Requires:       util-linux

%description
Graphical user-interface to download and write Raspberry Pi disk images, or
write custom disk images and format SD cards.

%prep
%autosetup -p1

%build
pushd src
%cmake -DENABLE_CHECK_VERSION=OFF \
       -DENABLE_TELEMETRY=OFF
%cmake_build

%install
pushd src
%cmake_install
desktop-file-install \
    --add-category="X-GNOME-Utilities" \
    %{buildroot}%{_datadir}/applications/org.raspberrypi.%{name}.desktop

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.metainfo.xml

%files
%{_bindir}/%{name}
%{_datadir}/applications/org.raspberrypi.%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_metainfodir}/%{name}.metainfo.xml
%license license.txt
%doc README.md

%changelog
* Sun Jan 28 2024 K. de Jong <keesdejong@fedoraproject.org> - 1.8.5-1
- New upstream release

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 02 2024 K. de Jong <keesdejong@fedoraproject.org> - 1.8.4-1
- New upstream release

* Fri Oct 20 2023 K. de Jong <keesdejong@fedoraproject.org> - 1.8.1-1
- New upstream release

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue May 23 2023 K. de Jong <keesdejong@fedoraproject.org> - 1.7.5-1
- New upstream release

* Sun Mar 19 2023 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 1.7.4-1
- rpi-imager version 1.7.4
- Telemery disabled
- Auto-update checker disabled
- autosetup patch param added in case of patches added
- 0001-fix-header-import-cstdint.patch added
- ExcludeArch s390x because upstream not supported

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Sep 09 2022 K. de Jong <keesdejong@fedoraproject.org> - 1.7.3-1
- New upstream release

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Apr 07 2022 K. de Jong <keesdejong@fedoraproject.org> - 1.7.2-1
- New upstream release

* Sat Feb 05 2022 K. de Jong <keesdejong@fedoraproject.org> - 1.7.1-1
- New upstream release

* Thu Feb 03 2022 K. de Jong <keesdejong@fedoraproject.org> - 1.7-1
- New upstream release

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.6.2-3
- Rebuilt with OpenSSL 3.0.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu May 27 2021 K. de Jong <keesdejong@fedoraproject.org> - 1.6.2-1
- New upstream release

* Mon May 24 2021 K. de Jong <keesdejong@fedoraproject.org> - 1.6.1-2
- Updated runtime dependencies

* Thu Apr 08 2021 K. de Jong <keesdejong@fedoraproject.org> - 1.6.1-1
- New upstream release

* Fri Mar 19 2021 K. de Jong <keesdejong@fedoraproject.org> - 1.6-1
- First release
- Applied patch to fix custom disk image selection menu, for more info
please check: https://github.com/raspberrypi/rpi-imager/issues/159
