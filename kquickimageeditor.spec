Name:    kquickimageeditor
Version: 0.2.0
Release: 5%{?dist}
Summary: QtQuick components providing basic image editing capabilities
License: GPLv2+
URL:     https://invent.kde.org/libraries/%{name}
Source0: https://invent.kde.org/libraries/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildRequires: extra-cmake-modules
BuildRequires: qt5-qtbase-devel        >= 5.12.0
BuildRequires: qt5-qtdeclarative-devel >= 5.12.0

%description
%{summary}

%package devel
Summary: Development files for %{name}

%description devel
The %{name}-devel package contains cmake and mkspecs for developing
applications that use %{name}.

%prep
%autosetup -n %{name}-v%{version}

%build
%{cmake_kf5}
%{cmake_build}

%install
%{cmake_install}

%files
%{_libdir}/qt5/qml/org/kde/kquickimageeditor

%files devel
%{_libdir}/cmake/KQuickImageEditor
%{_libdir}/qt5/mkspecs/modules/qt_KQuickImageEditor.pri

%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 18 2021 Marc Deop <marcdeop@fedoraproject.org> - 0.2.0-1
- Upgrade to version 0.2.0.

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 23 2020 Marc Deop <marcdeop@fedoraproject.org> - 0.1.2-1
- Initial package.

