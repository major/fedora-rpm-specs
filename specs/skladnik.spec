%global app_id  org.kde.skladnik

Name:           skladnik
Version:        24.12.2
Release:        1%{?dist}
Summary:        Warehouse keeper game
# GPL: code
# GFDL: docs
# CC0: metadata, themes
# CC-BY-SA: themes
License:        GPL-2.0-or-later AND CC0-1.0 AND CC-BY-SA-4.0 AND GFDL-1.2-or-later
URL:            https://apps.kde.org/skladnik/
Source :        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
# Qt dependencies
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
# KF dependencies
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(KF6DocTools)
# KDE Gear dependencies
BuildRequires:  cmake(KDEGames6)

Requires:       hicolor-icon-theme

%description
Skladnik is an implementation of a Japanese warehouse keeper game.
The idea is that you are a warehouse keeper trying to push crates to their
proper locations in a warehouse. The problem is that you cannot pull the
crates or step over them. If you are not careful, some of the crates can get
stuck in wrong places and/or block your way.


%prep
%autosetup


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang %{name} --with-html --with-man


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{app_id}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{app_id}.metainfo.xml


%files -f %{name}.lang
%license LICENSES/*.txt
%doc AUTHORS README
%{_bindir}/%{name}
%{_datadir}/applications/%{app_id}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/%{name}/
%{_mandir}/man6/%{name}.6*
%{_metainfodir}/%{app_id}.metainfo.xml


%changelog
* Wed Feb 05 2025 Steve Cossette <farchord@gmail.com> - 24.12.2-1
- 24.12.2

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 24.12.1-2
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

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.05.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jul 07 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.05.2-1
- 24.05.2

* Sun May 19 2024 Yaakov Selkowitz <yselkowi@redhat.com> - 24.05.0-1
- Initial build
