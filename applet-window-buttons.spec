%global orig_name org.kde.windowbuttons

Name:           applet-window-buttons
Version:        0.11.1
Release:        8%{?dist}
Summary:        Plasma 5 applet to show window buttons in panels
License:        GPLv2+
URL:            https://github.com/psifidotos/%{name}
Source0:        https://github.com/psifidotos/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

# https://github.com/psifidotos/applet-window-buttons/pull/191
Patch0:         191.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  appstream

BuildRequires:  kf5-kconfig-devel
BuildRequires:  kf5-kconfigwidgets-devel
BuildRequires:  kf5-kdeclarative-devel
BuildRequires:  kf5-kdoctools-devel
BuildRequires:  kf5-kglobalaccel-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kwindowsystem-devel
BuildRequires:  kf5-kxmlgui-devel
BuildRequires:  libSM-devel
BuildRequires:  kf5-plasma-devel

BuildRequires:  cmake(KDecoration2) 
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5QuickWidgets)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)


%description
This is a Plasma 5 applet that shows the current window appmenu in
one's panels. This plasmoid is coming from Latte land, but it can also
support Plasma panels.

%prep
%autosetup -n %{name}-%{version} -p1

%build
%cmake
%cmake_build

%install
%cmake_install


%check
appstreamcli validate --no-net %{buildroot}%{_datadir}/metainfo/%{orig_name}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/plasma/plasmoids/%{orig_name}/metadata.desktop

%files
%license LICENSE
%dir %{_kf5_datadir}/plasma/plasmoids/%{orig_name}
%{_kf5_datadir}/plasma/plasmoids/%{orig_name}
%{_qt5_qmldir}/org/kde/appletdecoration
%{_kf5_datadir}/kservices5/plasma-applet-%{orig_name}.desktop
%{_kf5_metainfodir}/%{orig_name}.appdata.xml

%{_kf5_datadir}/plasma/plasmoids/%{orig_name}/metadata.desktop
%{_kf5_datadir}/plasma/plasmoids/%{orig_name}/contents/
%{_kf5_datadir}/plasma/plasmoids/%{orig_name}/metadata.json


%changelog
* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Feb 21 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 0.11.1-6
- Cosmetic changes to the spec file.
- Add patch from PR 191 locally.

* Tue Jan 31 2023 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 0.11.1-5
- Rebuilt for kde 5.26.90 library changes

* Tue Jan 31 2023 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 0.11.1-4
- Rebuilt for libkdecorations2private.so

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Mar 31 2022  Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 0.11.1-1
- Update to version 0.11.1

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 7 2021  Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 0.10.1-1
- 0.10.1

* Tue Dec 7 2021  Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 0.9.0-5
- 00-fix-update-override.patch add into git source for fix build problem (#2024145)
- cosmetic fixes

* Wed Oct 13 2021 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 0.9.0-4
- rawhide-fixing build attempt #1
- 00-fix-update-override.patch added.

* Thu Jul 29 2021 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 0.9.0-3
- BR : appstream added fix build errors

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed May 12 2021 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 0.9.0-1
- initial package
