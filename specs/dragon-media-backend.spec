Name:           dragon-media-backend
Version:        0.82.1
Release:        1%{?dist}
Summary:        Qt C++ library intended for desktop music players

License:        (LGPL-2.1-only OR LGPL-3.0-only) AND MIT AND CC0-1.0
URL:            https://invent.kde.org/libraries/dragon-media-backend
Source0:        https://invent.kde.org/libraries/dragon-media-backend/-/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildRequires:  extra-cmake-modules
BuildRequires:  cmake
BuildRequires:  gcc-c++

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6QmlIntegration)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)

BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)

BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libswresample)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  cmake(SDL3)
BuildRequires:  cmake(kissfft)
BuildRequires:  cmake(QCoro6)

%description
%{summary}.

Can play any audio ffmpeg decodes (~everything)
Plugin system for audio output, with support for:

PipeWire
PulseAudio
SDL

Calculates FFTs for audio visualizations
Can play music over KDE's KIO system
Can play audio CDs and provide basic audio CD track information
Supports ICY metadata for radio streams
Volume API keeps in sync with Linux desktop application volume
A QWidget-based desktop example app and a QML-based Android example app

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       bundled(LockFreeSpscQueue) = 1.0.3
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1 -n %{name}-v%{version}

%conf
%cmake_kf6 -DCMAKE_SKIP_INSTALL_RPATH=ON -DBUILD_EXAMPLES=OFF

%build
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSES/*
%doc README.md
%{_kf6_qtplugindir}/DragonMediaBackend/
%{_kf6_qmldir}/org/kde/dragonmediabackend/
%{_kf6_datadir}/qlogging-categories6/dragonmediabackend.categories
%{_kf6_libdir}/libDragonMediaBackend.so.{0,%{version}}

%files devel
%{_includedir}/DragonMediaBackend/
%{_kf6_libdir}/cmake/DragonMediaBackend/
%{_kf6_libdir}/libDragonMediaBackend.so

%changelog
* Thu Oct 15 2026 Steve Cossette <steve@ninjasinpajamas.com> - 0.82.1-1
- Initial Release
