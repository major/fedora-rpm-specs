Name:          kontrast
Version:       23.08.2
Release:       1%{?dist}
Summary:       Color contrast checker
# BSD, CC0 are only for build files
License:       GPL-3.0-only AND GPL-3.0-or-later AND CC-BY-SA-4.0
URL:           https://apps.kde.org/kontrast/
Source0:       https://download.kde.org/%{stable_kf5}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: gettext
BuildRequires: kf5-rpm-macros
BuildRequires: libappstream-glib

BuildRequires: cmake(FutureSQL5)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5Kirigami2)
BuildRequires: cmake(QCoro5Core)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Qml)
BuildRequires: cmake(Qt5QuickControls2)
BuildRequires: cmake(Qt5Sql)
BuildRequires: cmake(Qt5Svg)
BuildRequires: cmake(Qt5Widgets)

Requires:      hicolor-icon-theme
Requires:      kf5-filesystem
# QML dependencies
Requires:      kf5-kirigami2%{?_isa}
Requires:      kf5-kirigami2-addons%{?_isa}
Requires:      qt5-qtquickcontrols2%{?_isa}

%description
Kontrast is a color contrast checker and tell you if your color combinations
are accessible for people with color vision deficiencies.


%prep
%autosetup -p1


%build
%cmake_kf5
%cmake_build


%install
%cmake_install

%find_lang %{name} --with-html


%check
appstream-util validate-relax --nonet %{buildroot}%{_kf5_metainfodir}/org.kde.%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_kf5_datadir}/applications/org.kde.%{name}.desktop


%files  -f %{name}.lang
%doc README.md
%license LICENSES/CC-BY* LICENSES/GPL-*
%{_kf5_bindir}/%{name}
%{_kf5_datadir}/applications/org.kde.%{name}.desktop
%{_kf5_datadir}/icons/hicolor/*/*/org.kde.%{name}.*
%{_kf5_metainfodir}/org.kde.%{name}.appdata.xml


%changelog
* Fri Oct 13 2023 Yaakov Selkowitz <yselkowitz@fedoraproject.org> - 23.08.2-1
- Initial build
