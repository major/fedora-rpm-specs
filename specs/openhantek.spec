Name:           openhantek
Version:        3.4~rc3
Release:        3%{?dist}
Summary:        Hantek and compatible USB digital signal oscilloscope

License:        GPL-3.0-or-later AND GPL-2.0-or-later AND Apache-2.0
URL:            https://github.com/OpenHantek/OpenHantek6022
#Source0:        %{url}/archive/%{version}/OpenHantek6022-%{version}.tar.gz
Source0:        %{url}/archive/3.4-rc3/OpenHantek6022-3.4-rc3.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake3
BuildRequires:  qt5-qtbase-devel
BuildRequires:  fftw-devel
BuildRequires:  libusbx-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  qt5-qttranslations
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLES-devel
BuildRequires:  binutils-devel
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  pkgconfig(udev)

Requires:       hicolor-icon-theme
Requires:       udev

%description
OpenHantek is a free software for Hantek and compatible
(Voltcraft/Darkwire/Protek/Acetech) USB digital signal oscilloscopes.
Supported devices: 6022BE/BL.

%prep
%autosetup -p1 -n OpenHantek6022-3.4-rc3

%build
export VERSION=%{version}
%cmake3
%cmake3_build

%install
%cmake3_install
mkdir -p %{buildroot}%{_udevrulesdir}
rm %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/OpenHantek.png
rm %{buildroot}%{_datadir}/doc/%{name}/*

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/OpenHantek.desktop

%files
%license LICENSE
%doc README.md CHANGELOG docs/OpenHantek6022_User_Manual.pdf CODE_OF_CONDUCT
%{_bindir}/OpenHantek
%{_datadir}/applications/OpenHantek.desktop
%{_datadir}/icons/hicolor/scalable/apps/OpenHantek.svg
%{_udevrulesdir}/60-openhantek.rules


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.4~rc3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.4~rc3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Mar 25 2024 Vasiliy Glazov <vascom2@gmail.com> - 3.4~rc3-1
- Update to 3.4-rc3

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Aug 14 2023 Vasiliy Glazov <vascom2@gmail.com> - 3.3.3-1
- Update to 3.3.3

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 08 2023 Vasiliy Glazov <vascom2@gmail.com> - 3.3.2.2-1
- Update to 3.3.2.2

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Jan 08 2023 Vasiliy N. Glazov <vascom2@gmail.com> - 3.3.2-1
- Update to 3.3.2

* Sat Oct 29 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 3.3.1-1
- Update to 3.3.1

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 28 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 3.3.0.1-1
- Update to 3.3.0.1

* Sat Apr 30 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 3.3.0-rc1-1
- Update to 3.3.0-rc1

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec 17 2021 Vasiliy Glazov <vascom2@gmail.com> - 3.2.5-1
- Update to 3.2.5

* Tue Jul 27 2021 Vasiliy Glazov <vascom2@gmail.com> - 3.2.4-1
- Update to 3.2.4

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue May 25 2021 Vasiliy Glazov <vascom2@gmail.com> - 3.2.3-1
- Update to 3.2.3

* Thu Apr 22 2021 Vasiliy Glazov <vascom2@gmail.com> - 3.2.2-1
- Update to 3.2.2

* Thu Apr 08 2021 Vasiliy Glazov <vascom2@gmail.com> - 3.2.1-1
- Update to 3.2.1

* Mon Mar 01 2021 Vasiliy Glazov <vascom2@gmail.com> - 3.2-1
- Update to 3.2

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 27 2020 Vasiliy Glazov <vascom2@gmail.com> - 3.1.5-1
- Update to 3.1.5

* Wed Dec 09 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 3.1.4-1
- Update to 3.1.4

* Fri Sep 04 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 3.1.3-1
- Update to 3.1.3

* Mon Aug 10 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 3.1.2-1
- Update to 3.1.2

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 01 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 3.1.1-1
- Update to 3.1.1

* Fri May 08 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 3.1.0-1
- Update to 3.1.0

* Tue Apr 14 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 3.0.4b-1
- Update to 3.0.4b

* Wed Mar 18 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 3.0.3-1
- Update to 3.0.3

* Tue Mar 03 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 3.0.2-2
- Update to 3.0.2
- Fix BR

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 19 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 3.0.1-1
- Update to 3.0.1

* Mon Nov 18 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 3.0.0-1
- Update to 3.0.0

* Thu Oct 17 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 2.16-1
- Update to 2.16

* Mon Oct 07 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 2.15-1
- Update to 2.15

* Mon Sep 09 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 2.14-1
- Update to 2.14

* Sat Sep 07 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 2.13-1
- Update to 2.13

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 08 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 2.12-1
- Update to 2.12

* Tue Jun 11 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 2.10-1
- Update to 2.10
- Correct udev Require

* Mon May 27 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 2.09-1
- Update to 2.09
- Corrected license

* Thu May 23 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 2.07-1
- Update to 2.07

* Wed May 15 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 2.06-1
- Update to 2.06

* Sat May 11 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 2.05-1
- Update to 2.05

* Fri May 10 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 2.04-1
- Update to 2.04

* Mon May 06 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 2.03-1
- Update to 2.03
- Fix crashing in normal mode

* Sat Apr 27 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 2.01-1
- Update to 2.01

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0-4.20190110giteb33325
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Feb 25 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 0-2.20190110giteb33325
- Update to latest git

* Sat Dec 08 2018 Nicolas Chauvet <kwizart@gmail.com> - 0-3.20180722git7862387
- Drop systemd-udev as it's installed by default.
  This avoid a dependency break in el7 as udev is provided by the systemd package

* Wed Aug 01 2018 Vasiliy N. Glazov <vascom2@gmail.com> - 0-2.20180722git7862387
- Update to latest git

* Fri Jul 27 2018 RPM Fusion Release Engineering <sergio@serjux.com> - 0-2.20180715git57e0beb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 16 2018 Vasiliy N. Glazov <vascom2@gmail.com> - 0-1.20180715git57e0beb
- Update to latest git

* Wed Jul 11 2018 Vasiliy N. Glazov <vascom2@gmail.com> - 0-1.20180710git9935f0a
- Update to latest git

* Thu Mar 15 2018 Vasiliy N. Glazov <vascom2@gmail.com> - 0-1.20180320git0eff8d4
- Initial package for Fedora
