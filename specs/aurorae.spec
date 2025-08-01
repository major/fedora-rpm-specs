Name:           aurorae
Summary:        Aurorae is a themeable window decoration for KWin
Version:        6.4.3
Release:        2%{?dist}
License:        GPL-2.0-or-later AND MIT AND CC0-1.0
URL:            https://invent.kde.org/plasma/%{name}

Source0:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz.sig

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: gcc
BuildRequires: kf6-rpm-macros
BuildRequires: extra-cmake-modules

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6UiTools)
BuildRequires: cmake(Qt6Widgets)

BuildRequires: cmake(KF6ColorScheme)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6KCMUtils)
BuildRequires: cmake(KF6NewStuff)
BuildRequires: cmake(KF6Package)
BuildRequires: cmake(KF6Svg)
BuildRequires: cmake(KF6WindowSystem)

BuildRequires: cmake(KDecoration3)

# Account for being split out of kwin
Conflicts:     kwin < 6.3.90
Supplements:   kwin%{?_isa} >= %{version}

%description
Aurorae is a themeable window decoration for KWin.
It supports theme files consisting of several SVG files for
decoration and buttons. Themes can be installed and selected
directly in the configuration module of KWin decorations.
Please have a look at theme-description on how to write a theme file.

%package devel
Summary: Development libraries for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%prep
%autosetup -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang %{name}

%files -f %{name}.lang
%doc README AUTHORS TODO
%license LICENSES/*
%{_kf6_qtplugindir}/org.kde.kdecoration3.kcm/kcm_auroraedecoration.so
%{_kf6_qtplugindir}/org.kde.kdecoration3/org.kde.kwin.aurorae.so
%{_kf6_qmldir}/org/kde/kwin/decoration/AppMenuButton.qml
%{_kf6_qmldir}/org/kde/kwin/decoration/ButtonGroup.qml
%{_kf6_qmldir}/org/kde/kwin/decoration/Decoration.qml
%{_kf6_qmldir}/org/kde/kwin/decoration/DecorationButton.qml
%{_kf6_qmldir}/org/kde/kwin/decoration/MenuButton.qml
%{_kf6_qmldir}/org/kde/kwin/decoration/libdecorationplugin.so
%{_kf6_qmldir}/org/kde/kwin/decoration/qmldir
%{_kf6_qmldir}/org/kde/kwin/decorations/plastik/libplastikplugin.so
%{_kf6_qmldir}/org/kde/kwin/decorations/plastik/qmldir
%{_libexecdir}/plasma-apply-aurorae
%{_kf6_datadir}/knsrcfiles/aurorae.knsrc
%{_kf6_datadir}/kwin/aurorae/
%{_kf6_datadir}/kwin/decorations/kwin4_decoration_qml_plastik/

%files devel
%{_kf6_libdir}/cmake/Aurorae/

%changelog
* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue Jul 15 2025 Steve Cossette <farchord@gmail.com> - 6.4.3-1
- 6.4.3

* Thu Jul 03 2025 Steve Cossette <farchord@gmail.com> - 6.4.2-1
- 6.4.2

* Tue Jun 24 2025 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.4.1-1
- 6.4.1

* Wed Jun 18 2025 Neal Gompa <ngompa@fedoraproject.org> - 6.4.0-2
- Add Supplements: kwin to account for the split from kwin
- Add Conflicts: kwin < 6.3.90 to account for the split on upgrade

* Mon Jun 16 2025 Steve Cossette <farchord@gmail.com> - 6.4.0-1
- 6.4.0

* Sat May 31 2025 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.3.91-2
- Add signature file

* Fri May 30 2025 Steve Cossette <farchord@gmail.com> - 6.3.91-1
- 6.3.91

* Thu May 15 2025 Steve Cossette <farchord@gmail.com> - 6.3.90-1
- Initial release
