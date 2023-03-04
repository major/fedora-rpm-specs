Name:            polkit-qt-1
Version:         0.114.0
Release:         6%{?dist}
Summary:         Qt bindings for PolicyKit

License:         GPLv2+
URL:             https://api.kde.org/kdesupport-api/polkit-qt-1-apidocs/
Source0:         http://download.kde.org/stable/%{name}/polkit-qt-1-%{version}.tar.xz

Patch0:          polkit-qt-1-change-installec-cmake-and-pc-files-to-contain-relatives.patch
Patch1:          polkit-qt-1-unexport-nested-private-classes.patch
Patch2:          polkit-qt-1-change-cmake-code-to-enable-buildint-against-qt6.patch
Patch3:          polkit-qt-1-fix-memory-leak.patch

BuildRequires:   cmake
BuildRequires:   gcc-c++
BuildRequires:   pkgconfig(polkit-agent-1)
BuildRequires:   pkgconfig(polkit-gobject-1)

%description
Polkit-qt is a library that lets developers use the PolicyKit API
through a nice Qt-styled API.

%package -n polkit-qt5-1
Summary: PolicyKit Qt5 bindings
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
Obsoletes: polkit-qt5 < 0.112.0-3
Provides:  polkit-qt5 = %{version}-%{release}
%description -n polkit-qt5-1
Polkit-qt is a library that lets developers use the PolicyKit API
through a nice Qt-styled API.

%package -n polkit-qt5-1-devel
Summary: Development files for PolicyKit Qt5 bindings
Obsoletes: polkit-qt5-devel < 0.112.0-3
Provides:  polkit-qt5-devel = %{version}-%{release}
Requires: polkit-qt5-1%{?_isa} = %{version}-%{release}
%description -n polkit-qt5-1-devel
%{summary}.

%package -n polkit-qt6-1
Summary: PolicyKit Qt6 bindings
BuildRequires:  pkgconfig(Qt6DBus)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Widgets)
%description -n polkit-qt6-1
Polkit-qt is a library that lets developers use the PolicyKit API
through a nice Qt-styled API.

%package -n polkit-qt6-1-devel
Summary: Development files for PolicyKit Qt5 bindings
Requires: polkit-qt6-1%{?_isa} = %{version}-%{release}
%description -n polkit-qt6-1-devel
%{summary}.

%prep
%autosetup -n %{name}-%{version} -p1


%build
%global _vpath_builddir %{_target_platform}-qt5
%cmake -DBUILD_EXAMPLES:BOOL=OFF -DQT_MAJOR_VERSION=5
%cmake_build

%global _vpath_builddir %{_target_platform}-qt6
%cmake -DBUILD_EXAMPLES:BOOL=OFF -DQT_MAJOR_VERSION=6
%cmake_build

%install
%global _vpath_builddir %{_target_platform}-qt5
%cmake_install

%global _vpath_builddir %{_target_platform}-qt6
%cmake_install

%files -n polkit-qt5-1
%doc AUTHORS README
%license LICENSES/*
%{_libdir}/libpolkit-qt5-core-1.so.1*
%{_libdir}/libpolkit-qt5-gui-1.so.1*
%{_libdir}/libpolkit-qt5-agent-1.so.1*

%files -n polkit-qt5-1-devel
%{_includedir}/polkit-qt5-1/
%{_libdir}/libpolkit-qt5-core-1.so
%{_libdir}/libpolkit-qt5-gui-1.so
%{_libdir}/libpolkit-qt5-agent-1.so
%{_libdir}/pkgconfig/polkit-qt5-1.pc
%{_libdir}/pkgconfig/polkit-qt5-core-1.pc
%{_libdir}/pkgconfig/polkit-qt5-gui-1.pc
%{_libdir}/pkgconfig/polkit-qt5-agent-1.pc
%{_libdir}/cmake/PolkitQt5-1/

%files -n polkit-qt6-1
%doc AUTHORS README
%license LICENSES/*
%{_libdir}/libpolkit-qt6-core-1.so.1*
%{_libdir}/libpolkit-qt6-gui-1.so.1*
%{_libdir}/libpolkit-qt6-agent-1.so.1*

%files -n polkit-qt6-1-devel
%{_includedir}/polkit-qt6-1/
%{_libdir}/libpolkit-qt6-core-1.so
%{_libdir}/libpolkit-qt6-gui-1.so
%{_libdir}/libpolkit-qt6-agent-1.so
%{_libdir}/pkgconfig/polkit-qt6-1.pc
%{_libdir}/pkgconfig/polkit-qt6-core-1.pc
%{_libdir}/pkgconfig/polkit-qt6-gui-1.pc
%{_libdir}/pkgconfig/polkit-qt6-agent-1.pc
%{_libdir}/cmake/PolkitQt6-1/

%changelog
* Thu Mar 02 2023 Jan Grulich <jgrulich@redhat.com> - 0.114.0-6
- Add Qt6 support

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.114.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.114.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.114.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.114.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 21 2021 Rex Dieter <rdieter@fedoraproject.org> - 0.114.0-1
- polkit-qt-1-0.114.0
- .spec cleanup

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.113.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Aug 21 2020 Troy Dawson <tdawson@redhat.com> - 0.113.0-5
- Fix FTBFS - cmake issues (#1863703)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.113.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.113.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.113.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 31 2019 Rex Dieter <rdieter@fedoraproject.org> - 0.113.0-1
- new qt5-only polkit-qt-1 package, let polkit-qt remain for qt4 legacy
