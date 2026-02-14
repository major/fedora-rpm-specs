%global app_id  org.kde.kimagemapeditor

Name:           kimagemapeditor
Version:        25.12.2
Release:        2%{?dist}
Summary:        HTML image map editor
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/kimagemapeditor/
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

ExclusiveArch:  %{qt6_qtwebengine_arches}

BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib

BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6WebEngineWidgets)

BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6Parts)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6XmlGui)

Requires:       hicolor-icon-theme

# split out from kdewebdev (add < EVR once dropped therefrom)
Conflicts:      kdewebdev

%description
KImageMapEditor is an editor of image maps embedded inside HTML files,
based on the <map> HTML tag.


%prep
%autosetup -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install

%find_lang %{name} --with-html


%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/%{app_id}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/%{app_id}.appdata.xml


%files -f %{name}.lang
%license COPYING
%doc README
%{_kf6_bindir}/%{name}
%{_kf6_plugindir}/parts/%{name}part.so
%{_kf6_datadir}/applications/%{app_id}.desktop
%{_kf6_datadir}/icons/hicolor/*/apps/%{name}.*
%{_kf6_datadir}/icons/hicolor/*/actions/*
%{_kf6_datadir}/qlogging-categories6/%{name}.categories
%{_kf6_datadir}/%{name}/
%{_kf6_metainfodir}/%{app_id}.appdata.xml


%changelog
* Thu Feb 12 2026 Steve Cossette <farchord@gmail.com> - 25.12.2-2
- Full Stack Rebuild (kio abi break)

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

* Fri May 16 2025 Yaakov Selkowitz <yselkowi@redhat.com> - 25.04.1-1
- 25.04.1

* Mon Apr 21 2025 Yaakov Selkowitz <yselkowi@redhat.com> - 25.04.0-1
- 25.04.0

* Mon Mar 24 2025 Yaakov Selkowitz <yselkowi@redhat.com> - 25.03.80-1
- 25.03.80

* Mon Mar 24 2025 Yaakov Selkowitz <yselkowi@redhat.com> - 24.12.3-1
- 24.12.3
