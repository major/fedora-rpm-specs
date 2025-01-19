Name:		lightpack
Version:        5.11.2.31
Release:        6%{?dist}
Summary:        Hardware implementation of the backlight

License:        GPL-3.0-or-later AND GPL-2.0-or-later AND SMLNJ AND BSD-3-Clause AND MIT
URL:            https://github.com/psieg/Lightpack
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  qtchooser
BuildRequires:  pkgconfig(Qt5Designer)
BuildRequires:  pkgconfig(Qt5SerialPort)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  desktop-file-utils

Requires:       udev
Requires:       hicolor-icon-theme

Recommends:     gnome-shell-extension-appindicator

%description
Lightpack is a fully open-source and simple hardware implementation of the
backlight for any computer. It's a USB content-driven ambient lighting system.

Prismatik is an open-source software we buid to control Lightpack devices. It
grabs the screen, analyzes the picture, calculates resulting colors, and
provides soft and gentle lighting with a Lightpack device. Moreover, you can
handle other devices with Prismatik such as Adalight, Ardulight, or even
Alienware LightFX system.

%prep
%autosetup -n Lightpack-%{version}
#Fix desktop-file
sed -i -e 's|prismatik|Prismatik|' \
-e 's|Prismatik.png|Prismatik|' \
-e 's|Video|AudioVideo|' \
Software/dist_linux/package_template/usr/share/applications/prismatik.desktop


%build
pushd Software
    %{qmake_qt5} -r
    %make_build
popd

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_udevrulesdir}
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/22x22/apps
mkdir -p %{buildroot}%{_datadir}/pixmaps/

install -p -m 755 Software/bin/Prismatik %{buildroot}%{_bindir}/Prismatik
install -p -m 644 93-lightpack.rules %{buildroot}%{_udevrulesdir}/93-lightpack.rules
install -p -m 644 Software/dist_linux/package_template/usr/share/icons/hicolor/22x22/apps/prismatik-on.png \
%{buildroot}%{_datadir}/icons/hicolor/22x22/apps/prismatik-on.png
install -p -m 644 Software/dist_linux/package_template/usr/share/pixmaps/Prismatik.png \
%{buildroot}%{_datadir}/pixmaps/Prismatik.png

desktop-file-install Software/dist_linux/package_template/usr/share/applications/prismatik.desktop

%files
%license LICENSE
%doc README.md
%{_bindir}/Prismatik
%{_datadir}/applications/prismatik.desktop
%{_datadir}/icons/hicolor/22x22/apps/prismatik-on.png
%{_datadir}/pixmaps/Prismatik.png
%{_udevrulesdir}/93-lightpack.rules


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.11.2.31-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.11.2.31-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.11.2.31-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.11.2.31-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.11.2.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Vasiliy Glazov <vascom2@gmail.com> 5.11.2.31-1
- Initial packaging
