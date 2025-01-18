%global gitcommit_full 5bfa8fa9c880db2374c75d2d25107da3926b8f29
%global gitcommit %(c=%{gitcommit_full}; echo ${c:0:7})
%global date 20220606

Name:           fancontrol-gui
Version:        0.8
Release:        6.%{date}git%{gitcommit}%{?dist}
Summary:        GUI for fancontrol

License:        GPL-2.0-or-later
URL:            https://github.com/Maldela/fancontrol-gui
Source0:        %{url}/tarball/%{gitcommit_full}

BuildRequires:  gcc-c++
BuildRequires:  cmake >= 3.0.2
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(KF5Auth)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5Package)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5Plasma)
BuildRequires:  gettext
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(KF5Declarative)
BuildRequires:  cmake(KF5Kirigami2)
#BuildRequires:  cmake(Qt5QuickLayouts)
#BuildRequires:  cmake(Qt5QuickDialogs)
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

Requires:       lm_sensors
Requires:       hicolor-icon-theme
Requires:       dbus-common
Requires:       polkit

%description
GUI for fancontrol which is part of lm_sensors.
It uses the KAuth module of the KDE Frameworks 5 to write the
generated config file. Furthermore it communicates with systemd
via dbus to control the fancontrol service.

%package        kcm
Summary:        KCM for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       plasma-settings
Requires:       kf5-filesystem
Requires:       kf5-kcmutils

%description    kcm
KCM for %{name}.

%package        plasmoid
Summary:        Plasmoid for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       plasma-workspace
Requires:       kf5-filesystem

%description    plasmoid
Plasmoid for %{name}.

%prep
%autosetup -n Maldela-%{name}-%{gitcommit}


%build
%cmake_kf5 -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_KCM=on -DBUILD_PLASMOID=on
%cmake_build

%install
%cmake_install
%find_lang fancontrol_kcm --all-name
# Remove icon tag
sed -i '/icon/d' %{buildroot}%{_metainfodir}/org.kde.fancontrol.gui.appdata.xml
sed -i '/icon/d' %{buildroot}%{_metainfodir}/org.kde.fancontrol.kcm.appdata.xml
sed -i '/icon/d' %{buildroot}%{_metainfodir}/org.kde.fancontrol.plasmoid.appdata.xml

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.fancontrol.gui.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.kde.fancontrol.*.appdata.xml

%files -f fancontrol_kcm.lang
%license LICENSE
%doc README.md
%{_bindir}/fancontrol_gui
%{_qt5_qmldir}/Fancontrol
%{_libexecdir}/kf5/kauth/fancontrol_gui-helper
%{_datadir}/applications/org.kde.fancontrol.gui.desktop
%{_datadir}/dbus-1/system-services/org.kde.fancontrol.gui.helper.service
%{_datadir}/dbus-1/system.d/org.kde.fancontrol.gui.helper.conf
%{_datadir}/icons/hicolor/scalable/apps/org.kde.fancontrol.gui.svg
%{_metainfodir}/org.kde.fancontrol.gui.appdata.xml
%{_datadir}/polkit-1/actions/org.kde.fancontrol.gui.helper.policy

%files kcm
%{_qt5_plugindir}/kcms/kcm_fancontrol.so
%{_datadir}/kpackage/genericqml/org.kde.fancontrol.gui
%{_datadir}/kpackage/kcms/org.kde.fancontrol.kcm
%{_datadir}/kservices5/kcm_fancontrol.desktop
%{_metainfodir}/org.kde.fancontrol.kcm.appdata.xml

%files plasmoid
%{_datadir}/kservices5/plasma-applet-org.kde.fancontrol.plasmoid.desktop
%{_metainfodir}/org.kde.fancontrol.plasmoid.appdata.xml
%{_datadir}/plasma/plasmoids/org.kde.fancontrol.plasmoid

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-6.20220606git5bfa8fa
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-5.20220606git5bfa8fa
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-4.20220606git5bfa8fa
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-3.20220606git5bfa8fa
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-2.20220606git5bfa8fa
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 27 2023 Vasiliy Glazov <vascom2@gmail.com> 0.8-1.20220606git5bfa8fa
- Initial packaging
