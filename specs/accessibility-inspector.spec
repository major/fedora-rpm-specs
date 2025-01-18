%global app_id  org.kde.accessibilityinspector
%global sname   accessibilityinspector

Name:           accessibility-inspector
Version:        24.12.1
Release:        2%{?dist}
Summary:        KDE Accessbility Inspector
# LGPL: code
# CC0: metadata
License:        LGPL-2.0-or-later AND (LGPL-2.1-only OR LGPL-3.0-only) AND CC0-1.0
URL:            https://apps.kde.org/accessibilityinspector/
Source :        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
# Qt dependencies
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Widgets)
# KF dependencies
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6XmlGui)
# other dependencies
BuildRequires:  cmake(QAccessibilityClient6)

Requires:       hicolor-icon-theme

%description
Accessibility Inspector is an inspector for your application accessibility
tree. It lets you check all the items exposed via At-SPI, too.


%prep
%autosetup


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang %{sname}


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{app_id}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{app_id}.metainfo.xml


%files -f %{sname}.lang
%license LICENSES/*.txt
%doc README.md
%{_bindir}/%{sname}
%{_libdir}/lib%{sname}.so.1*
%{_datadir}/applications/%{app_id}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{app_id}.svg
%{_datadir}/qlogging-categories6/%{sname}.*
%{_metainfodir}/%{app_id}.metainfo.xml


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 24.12.1-2
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

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.05.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jul 07 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.05.2-1
- 24.05.2

* Sun May 19 2024 Yaakov Selkowitz <yselkowi@redhat.com> - 24.05.0-1
- Initial build
