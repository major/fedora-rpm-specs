Name:           jacktrip
Version:        1.6.4
Release:        1%{?dist}
Summary:        A system for high-quality audio network performance over the Internet

License:        MIT and GPLv3 and LGPLv3
URL:            https://github.com/%{name}/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  meson, cmake, gcc-c++
BuildRequires:  python3-pyyaml, python3-jinja2
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(rtaudio)
BuildRequires:  help2man
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5NetworkAuth)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5WebSockets)
BuildRequires:  hicolor-icon-theme
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
Requires:       hicolor-icon-theme
Obsoletes:      jacktrip-doc < 1.4.0

%description
JackTrip is a Linux and Mac OS X-based system used for multi-machine
network performance over the Internet. It supports any number of
channels (as many as the computer/network can handle) of
bidirectional, high quality, uncompressed audio signal steaming.

%prep
%autosetup -p1
rm -rf externals
mkdir -p externals/weakjack

%build
%meson -Drtaudio=enabled
%meson_build

%install
%meson_install
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml

%check
%meson_test

%files
%doc README.md
%license LICENSE.md LICENSES
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/applications/org.jacktrip.JackTrip.desktop
%{_metainfodir}/org.jacktrip.JackTrip.metainfo.xml

%changelog
* Mon Sep 19 2022 Iñaki Úcar <iucar@fedoraproject.org> - 1.6.4-1
- Update to v1.6.4

* Wed Aug 24 2022 Iñaki Úcar <iucar@fedoraproject.org> - 1.6.3-1
- Update to v1.6.3

* Mon Aug 22 2022 Iñaki Úcar <iucar@fedoraproject.org> - 1.6.2-1
- Update to v1.6.2

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 21 2022 Iñaki Úcar <iucar@fedoraproject.org> - 1.6.1-1
- Update to v1.6.1

* Thu Jun 02 2022 Iñaki Úcar <iucar@fedoraproject.org> - 1.6.0-1
- Update to v1.6.0

* Mon Mar 28 2022 Iñaki Úcar <iucar@fedoraproject.org> - 1.5.3-1
- Update to 1.5.3 (#2069182)

* Thu Mar 03 2022 Iñaki Úcar <iucar@fedoraproject.org> - 1.5.2-1
- Update to v1.5.2

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 17 2022 Iñaki Úcar <iucar@fedoraproject.org> - 1.5.1-1
- Update to v1.5.1

* Mon Jan 03 2022 Iñaki Úcar <iucar@fedoraproject.org> - 1.5.0-1
- Update to v1.5.0

* Mon Dec 20 2021 Iñaki Úcar <iucar@fedoraproject.org> - 1.4.3-1
- Update to v1.4.3

* Fri Dec 10 2021 Iñaki Úcar <iucar@fedoraproject.org> - 1.4.2-1
- Update to v1.4.2

* Thu Nov 11 2021 Iñaki Úcar <iucar@fedoraproject.org> - 1.4.1-1
- Update to v1.4.1

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 16 2021 Iñaki Úcar <iucar@fedoraproject.org> - 1.3.0-1
- Update to v1.3.0

* Sat Oct 24 2020 Iñaki Úcar <iucar@fedoraproject.org> - 1.2.1-1
- Initial packaging for Fedora
