%global app_id  org.kde.kalm


# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:           kalm
Version:        25.12.2
Release:        1%{?dist}
Summary:        Breathing techniques app
# LGPL: code
# CC0: metadata
License:        LGPL-2.1-or-later AND CC0-1.0
URL:            https://apps.kde.org/kalm/
Source:         https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
# Qt dependencies
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Widgets)
# KF dependencies
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(KF6QQC2DesktopStyle)

Requires:       hicolor-icon-theme
Requires:       qt6qml(org.kde.kirigamiaddons.formcard)

%description
Kalm can teach you different breathing techniques.


%prep
%autosetup


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang %{name}


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{app_id}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{app_id}.appdata.xml


%files -f %{name}.lang
%license LICENSES/LGPL-2.1-or-later.txt LICENSES/CC0-1.0.txt
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{app_id}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{app_id}.svg
%{_metainfodir}/%{app_id}.appdata.xml



%changelog
* Wed Feb 04 2026 Steve Cossette <farchord@gmail.com> - 25.12.2-1
- 25.12.2

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 25.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Wed Jan 07 2026 farchord@gmail.com - 25.12.1-1
- 25.12.1

* Sat Dec 06 2025 Steve Cossette <farchord@gmail.com> - 25.12.0-1
- 25.12.0

* Fri Nov 28 2025 Steve Cossette <farchord@gmail.com> - 25.11.90-1
- 25.11.90

* Sat Nov 15 2025 Steve Cossette <farchord@gmail.com> - 25.11.80-1
- 25.11.80

* Tue Nov 04 2025 Steve Cossette <farchord@gmail.com> - 25.08.3-1
- 25.08.3

* Wed Oct 08 2025 Steve Cossette <farchord@gmail.com> - 25.08.2-1
- 25.08.2

* Sun Sep 21 2025 Steve Cossette <farchord@gmail.com> - 25.08.1-1
- 25.08.1

* Sat Aug 16 2025 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 25.08.0-2
- Drop i686 support (leaf package)

* Fri Aug 08 2025 Steve Cossette <farchord@gmail.com> - 25.08.0-1
- 25.08.0

* Fri Jul 25 2025 Steve Cossette <farchord@gmail.com> - 25.07.90-1
- 25.07.90

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 25.07.80-2
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

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 24.12.1-2
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

* Thu Aug 22 2024 Steve Cossette <farchord@gmail.com> - 24.08.0-1
- 24.08.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.05.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jul 07 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.05.2-1
- 24.05.2

* Sun May 19 2024 Yaakov Selkowitz <yselkowi@redhat.com> - 24.05.0-1
- Initial build
