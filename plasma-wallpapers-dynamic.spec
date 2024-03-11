%global component wallpapers-dynamic

%global somajor 5

Name:           plasma-%{component}
Version:        5.0.0
Release:        %autorelease
Summary:        Dynamic wallpaper plugin for KDE Plasma

License:        GPL-3.0-or-later AND LGPL-3.0-or-later AND BSD-3-Clause AND CC0-1.0 AND CC-BY-SA-4.0
URL:            https://github.com/zzag/plasma5-%{component}
Source0:        %{url}/archive/%{version}/plasma5-%{component}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Positioning)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Package)
BuildRequires:  cmake(Plasma)
BuildRequires:  cmake(libavif)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  /usr/bin/appstreamcli

Recommends:     %{name}-builder

%description
A simple dynamic wallpaper plugin for KDE Plasma.

%package        devel
Summary:        Development headers and libraries for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the development headers and libraries.

%package        builder
Summary:        Wallpaper builder for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    builder
Command-line utility to build dynamic wallpapers.

%package        builder-bash-completion
Summary:        Bash completion support for %{name}-builder
BuildArch:      noarch
Requires:       %{name}-builder = %{version}-%{release}
Supplements:    (%{name}-builder and bash-completion)
Requires:       bash
Requires:       bash-completion

%description    builder-bash-completion
Files needed to support bash completion.

%package        builder-fish-completion
Summary:        Fish completion support for %{name}-builder
BuildArch:      noarch
Requires:       %{name}-builder = %{version}-%{release}
Supplements:    (%{name}-builder and fish)
Requires:       fish

%description    builder-fish-completion
Files needed to support fish completion.

%package        builder-zsh-completion
Summary:        Zsh completion support for %{name}-builder
BuildArch:      noarch
Requires:       %{name}-builder = %{version}-%{release}
Supplements:    (%{name}-builder and zsh)
Requires:       zsh

%description    builder-zsh-completion
Files needed to support zsh completion.

%prep
%autosetup -n plasma5-%{component}-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install
%find_lang plasma_wallpaper_com.github.zzag.dynamic

%check
appstreamcli validate --no-net %{buildroot}%{_datadir}/metainfo/com.github.zzag.dynamic.appdata.xml

%files -f plasma_wallpaper_com.github.zzag.dynamic.lang
%license LICENSES/*
%{_datadir}/plasma/wallpapers/com.github.zzag.dynamic/
%{_datadir}/metainfo/com.github.zzag.dynamic.appdata.xml
%{_libdir}/qt6/qml/com/github/zzag/plasma/wallpapers/dynamic/
%{_libdir}/qt6/plugins/kpackage/packagestructure/kdynamicwallpaper.so
%{_libdir}/libkdynamicwallpaper.so.%{somajor}{,.*}
%{_datadir}/wallpapers/Dynamic/

%files devel
%{_includedir}/KDynamicWallpaper/
%{_libdir}/libkdynamicwallpaper.so
%{_libdir}/cmake/KDynamicWallpaper/

%files builder
%{_bindir}/kdynamicwallpaperbuilder

%files builder-bash-completion
%{_datadir}/bash-completion/completions/kdynamicwallpaperbuilder

%files builder-fish-completion
%{_datadir}/fish/completions/kdynamicwallpaperbuilder.fish

%files builder-zsh-completion
%{_datadir}/zsh/site-functions/_kdynamicwallpaperbuilder

%changelog
%autochangelog
