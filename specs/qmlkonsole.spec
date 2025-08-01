Name:           qmlkonsole
Version:        25.07.90
Release:        1%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
Summary:        Terminal app for Plasma Mobile
Url:            https://invent.kde.org/plasma-mobile/qmlkonsole
Source:         https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  appstream

BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(KF6Pty)
BuildRequires:  cmake(KF6WindowSystem)

Requires:       kf6-kirigami
Requires:       kf6-kirigami-addons
Recommends:     dejavu-fonts-all

%description
%{summary}.

%prep
%autosetup

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang %{name}

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.kde.%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.%{name}.desktop

%files -f %{name}.lang
%license LICENSES/GPL-2.0-or-later.txt
%{_kf6_bindir}/%{name}
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_datadir}/icons/hicolor/scalable/apps/org.kde.%{name}.svg
%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
%{_kf6_datadir}/config.kcfg/terminalsettings.kcfg

%changelog
* Fri Jul 25 2025 Steve Cossette <farchord@gmail.com> - 25.07.90-1
- 25.07.90

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 25.07.80-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jul 11 2025 Steve Cossette <farchord@gmail.com> - 25.07.80-1
- 25.07.80

* Thu Jul 03 2025 Steve Cossette <farchord@gmail.com> - 25.04.3-1
- 25.04.3

* Wed Jun 04 2025 Steve Cossette <farchord@gmail.com> - 25.04.2-1
- 25.04.2

* Wed May 14 2025 Steve Cossette <farchord@gmail.com> - 25.04.1-1
- 25.04.1

* Sat Apr 12 2025 Steve Cossette <farchord@gmail.com> - 25.04.0-1
- 25.04.0

* Thu Mar 20 2025 Steve Cossette <farchord@gmail.com> - 25.03.80-1
- 25.03.80 (Beta)

* Tue Mar 04 2025 Steve Cossette <farchord@gmail.com> - 24.12.3-1
- 24.12.3

* Fri Feb 21 2025 Steve Cossette <farchord@gmail.com> - 24.12.2-2
- Rebuild for ppc64le enablement

* Wed Feb 05 2025 Steve Cossette <farchord@gmail.com> - 24.12.2-1
- 24.12.2

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 24.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Jan 07 2025 Steve Cossette <farchord@gmail.com> - 24.12.1-1
- 24.12.1

* Sat Dec 07 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.12.0-1
- 24.12.0

* Fri Nov 29 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.11.90-1
- 24.11.90

* Fri Nov 15 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.11.80-1
- 24.11.80

* Tue Nov 05 2024 Steve Cossette <farchord@gmail.com> - 24.08.3-1
- 24.08.3

* Tue Oct 08 2024 Steve Cossette <farchord@gmail.com> - 24.08.2-1
- 24.08.2

* Wed Sep 25 2024 Alessandro Astone <ales.astone@gmail.com> - 24.08.1-1
- 24.08.1

* Sun Aug 25 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 24.08.0-2
- Rebuilt for abseil-cpp-20240722.0

* Thu Aug 22 2024 Steve Cossette <farchord@gmail.com> - 24.08.0-1
- 24.08.0

* Fri Aug 16 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 24.05.2-4
- Remove spurious BuildRequires: abseil-cpp-devel

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 24.05.2-3
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.05.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jul 07 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.05.2-1
- 24.05.2

* Fri Jun 14 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.05.1-1
- 24.05.1

* Fri May 17 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.05.0-1
- 24.05.0

* Fri Apr 12 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.02.2-1
- 24.02.2

* Fri Mar 29 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.02.1-1
- 24.02.1

* Wed Feb 21 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.02.0-1
- 24.02.0

* Sun Feb 04 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 24.01.95-2
- Rebuilt for abseil-cpp-20240116.0

* Wed Jan 31 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.01.95-1
- 24.01.95

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.01.90-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.01.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 11 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.01.90-1
- 24.01.90

* Sat Dec 23 2023 ales.astone@gmail.com - 24.01.85-1
- 24.01.85

* Sun Dec 17 2023 Justin Zobel <justin.zobel@gmail.com> - 24.01.80-1
- Update to 24.01.80

* Thu Oct 12 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.2-1
- 23.08.2

* Sat Sep 16 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.1-1
- 23.08.1

* Thu Sep 07 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.0-1
- 23.08.0

* Wed Aug 30 2023 Benjamin A. Beasley <code@musicinmybrain.net> - 23.04.3-3
- Rebuilt for abseil-cpp 20230802.0

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 23.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jul 08 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.3-1
- 23.04.3

* Tue Jun 06 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.2-1
- 23.04.2

* Sat May 13 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.1-1
- 23.04.1

* Thu Apr 20 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.0-1
- 23.04.0

* Mon Mar 27 2023 Rich Mattes <richmattes@gmail.com> - 23.01.0-2
- Rebuild for abseil-cpp-20230125.1

* Mon Jan 30 2023 Justin Zobel <justin@1707.io> - 23.01.0-1
- Update to 23.01.0

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 22.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 01 2022 Justin Zobel <justin@1707.io> - 22.11-1
- Update to 22.11

* Wed Sep 28 2022 Justin Zobel <justin@1707.io> - 22.09-1
- Update to 22.09

* Thu Aug 25 2022 Justin Zobel <justin@1707.io> - 22.06-1
- Update to 22.06

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 22.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Feb 10 2022 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 22.02-1
- Plasma mobile version 22.02

* Sun Jan 23 2022 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 21.12-1
- 21.12

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 21.08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Sep 13 2021 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 21.08-1
- 21.08

* Tue Jun 08 2021 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 21.06-1
- initial version of package
