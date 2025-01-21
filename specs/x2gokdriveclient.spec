# Default to Qt 5 for now.
%global         qt_version 5

Name:           x2gokdriveclient
Version:        0.0.0.1
Release:        5%{?dist}
Summary:        X2Go KDrive Client application
License:        GPL-3.0-or-later
URL:            https://www.x2go.org
Source0:        https://code.x2go.org/releases/source/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
%if %{qt_version} == 5
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  qt5-linguist
%endif
%if %{qt_version} == 6
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Svg)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  qt6-linguist
%endif

BuildRequires:  pkgconfig(zlib)
BuildRequires:  man2html-core
BuildRequires:  pkgconfig

%if 0%{?fedora} || 0%{?rhel} >= 8
Enhances:       x2goclient
%endif


%description
X2Go is a server-based computing environment with
    - session resuming
    - low bandwidth support
    - session brokerage support
    - client-side mass storage mounting support
    - client-side printing support
    - audio support
    - authentication by smartcard and USB stick

X2Go KDrive Client is the KDrive graphical backend (Qt%{qt_version})
for X2Go Client that provides support for running modern desktop
environments like GNOME, KDE Plasma, Cinnamon, etc. in X2Go Sessions.

The X2Go KDrive graphical backend is not suitable for low bandwidth
WAN connections between X2Go Client and X2Go Server. It is supposed
for X2Go being used on the local area network.


%prep
%autosetup
# Fix up install issues
sed -i -e 's/-o root -g root//' -e '/^MAKE/d' Makefile


%build
%if %{qt_version} == 5
export 'PATH=%{_qt5_bindir}:'"${PATH}"
%endif
%if %{qt_version} == 6
export 'PATH=%{_qt6_bindir}:'"${PATH}"
%endif
%make_build CXXFLAGS='%{optflags} %{?el7:-std=c++11 -fPIC}' QMAKE_OPTS='QMAKE_STRIP=:' QT_VERSION='%{qt_version}' PREFIX='%{_prefix}'


%install
%make_install PREFIX=%{_prefix}


%files
%license COPYING LICENSE
%doc AUTHORS
%{_bindir}/%{name}
%dir %{_datadir}/x2go
%dir %{_datadir}/x2go/versions
%{_datadir}/x2go/versions/VERSION.x2gokdriveclient
%{_mandir}/man1/%{name}.1.gz


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Sep 28 2023 Orion Poplawski <orion@nwra.com> - 0.0.0.1-2
- Add BR for gcc-c++
- Fix License tag
- Use %%global

* Thu Jun 15 2023 Orion Poplawski <orion@nwra.com> - 0.0.0.1-1
- Initial Fedora package
