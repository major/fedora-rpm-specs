%if 0%{?rhel} && 0%{?rhel} >= 10
%bcond_with kf5
%else
%bcond_without kf5
%endif

Name:    kquickimageeditor
Version: 0.5.0
Release: 1%{?dist}
Summary: QtQuick components providing basic image editing capabilities
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL:     https://invent.kde.org/libraries/%{name}
Source0: https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz

BuildRequires: extra-cmake-modules

%if %{with kf5}
BuildRequires: kf5-rpm-macros
BuildRequires: cmake(Qt5Core)  >= 5.15.0
BuildRequires: cmake(Qt5Quick) >= 5.15.0
%endif

BuildRequires: kf6-rpm-macros
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Quick)

%description
%{summary}

%if %{with kf5}
%package qt5
Summary: Qt5 QtQuick components providing basic image editing capabilities
Obsoletes: %{name} < 0.3.0

%description qt5
%{summary}

%package qt5-devel
Summary: Development files for %{name}-qt5
Requires: %{name}-qt5%{?_isa} = %{version}-%{release}
Obsoletes: %{name}-devel < 0.3.0

%description qt5-devel
The %{name}-qt5-devel package contains cmake and mkspecs for developing
applications that use %{name}-qt5.
%endif

%package qt6
Summary: Qt6 QtQuick components providing basic image editing capabilities

%description qt6
%{summary}

%package qt6-devel
Summary: Development files for %{name}-qt6
Requires: %{name}-qt6%{?_isa} = %{version}-%{release}

%description qt6-devel
The %{name}-qt6-devel package contains cmake and mkspecs for developing
applications that use %{name}-qt6.

%prep
%autosetup -n %{name}-%{version}

%build
%if %{with kf5}
mkdir -p build-qt5
pushd build-qt5
%cmake_kf5 -S ..
%cmake_build
popd
%endif

mkdir -p build-qt6
pushd build-qt6
%cmake_kf6 -S .. -DQT_MAJOR_VERSION=6
%cmake_build
popd


%install
%if %{with kf5}
pushd build-qt5
%cmake_install
popd
%endif

pushd build-qt6
%cmake_install
popd

%if %{with kf5}
%files qt5
%{_kf5_qmldir}/org/kde/kquickimageeditor

%files qt5-devel
# the qt5 and qt6 cmake packages conflict
# https://invent.kde.org/libraries/kquickimageeditor/-/merge_requests/23
#{_kf5_libdir}/cmake/KQuickImageEditor
%{_kf5_archdatadir}/mkspecs/modules/qt_KQuickImageEditor.pri
%endif

%files qt6
%{_kf6_qmldir}/org/kde/kquickimageeditor

%files qt6-devel
%{_kf6_libdir}/cmake/KQuickImageEditor
%{_kf6_archdatadir}/mkspecs/modules/qt_KQuickImageEditor.pri

%changelog
* Sat Jan 18 2025 Steve Cossette <farchord@gmail.com> - 0.5.0-1
- 0.5.0

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.3.0-5
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Nov 27 2023 Yaakov Selkowitz <yselkowitz@fedoraproject.org> - 0.3.0-1
- 0.3.0
- Create parallel qt5 and qt6 builds

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

