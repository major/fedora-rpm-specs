# Not needed by default
%bcond asan 0
# Not packaged in Fedora yet (cf. rhbz#2372509)
%bcond breakpad 0
# Not available in RHEL
%bcond x11 %[%{undefined rhel}]

Name:               quickshell
Version:            0.2.1
Release:            8%{?dist}
Summary:            Flexible QtQuick based desktop shell toolkit
# Code is LGPL, Hyprland protocols are BSD-3-Clause, wlr protocols are HPND-sell-variant
License:            LGPL-3.0-or-later and BSD-3-Clause and HPND-sell-variant
URL:                https://quickshell.org/
Source:             https://git.outfoxxed.me/%{name}/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:      cmake
BuildRequires:      cmake(Qt6Core)
BuildRequires:      cmake(Qt6Qml)
BuildRequires:      cmake(Qt6CorePrivate)
BuildRequires:      cmake(Qt6QuickPrivate)
BuildRequires:      cmake(Qt6ShaderTools)
BuildRequires:      cmake(Qt6WaylandClient)
BuildRequires:      desktop-file-utils
BuildRequires:      gcc-c++
BuildRequires:      ninja-build
BuildRequires:      pkgconfig(CLI11)
BuildRequires:      pkgconfig(gbm)
BuildRequires:      pkgconfig(jemalloc)
BuildRequires:      pkgconfig(libdrm)
BuildRequires:      pkgconfig(libpipewire-0.3)
BuildRequires:      pkgconfig(pam)
BuildRequires:      pkgconfig(wayland-client)
BuildRequires:      pkgconfig(wayland-protocols)
BuildRequires:      spirv-tools

# Add undetectable runtime dependencies
Requires:           (qt6-qtwayland%{?_isa} if qt6-qtbase%{?_isa} < 6.10)
Requires:           qt6-qtsvg%{?_isa}

%if %{with asan}
BuildRequires:      libasan
%endif

%if %{with breakpad}
BuildRequires:      breakpad-static
BuildRequires:      pkgconfig(breakpad)
%endif

Provides:           desktop-notification-daemon = %{version}-%{release}
Provides:           PolicyKit-authentication-agent = %{version}-%{release}

%description
Quickshell is a toolkit for building status bars, widgets,
lockscreens, and other desktop components using QtQuick.

It can be used alongside a Wayland compositor to build
a complete desktop environment.

%prep
%autosetup -C

%conf
%cmake  -GNinja \
        -DCMAKE_BUILD_TYPE=RelWithDebInfo \
        -DCMAKE_SKIP_INSTALL_RPATH=ON \
        -DDISTRIBUTOR="%{vendor}" \
        -DDISTRIBUTOR_DEBUGINFO_AVAILABLE=YES \
        -DINSTALL_QML_PREFIX=%{_lib}/qt6/qml \
        -DASAN=%{?with_asan:ON}%{!?with_asan:OFF} \
        -DCRASH_REPORTER=%{?with_breakpad:ON}%{!?with_breakpad:OFF} \
        -DX11=%{?with_x11:ON}%{!?with_x11:OFF} \
        %{nil}

%build
%cmake_build

%install
%cmake_install

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%license LICENSE*
%doc BUILD.md CONTRIBUTING.md README.md changelog/
%{_bindir}/qs
%{_bindir}/quickshell
%{_datadir}/applications/org.quickshell.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.quickshell.svg
%{_qt6_qmldir}/Quickshell/

%changelog
* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Sun Jan 04 2026 Neal Gompa <ngompa@fedoraproject.org> - 0.2.1-7
- Initial package based on ErrorNoInternet/quickshell COPR version
