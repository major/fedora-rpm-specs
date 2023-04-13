%global component wallpapers-dynamic

%global somajor 4

Name:           plasma-%{component}
Version:        4.4.0
Release:        9%{?dist}
Summary:        Dynamic wallpaper plugin for KDE Plasma

License:        GPL-3.0-or-later AND LGPL-3.0-or-later AND BSD-3-Clause AND CC0-1.0 AND CC-BY-SA-4.0
URL:            https://github.com/zzag/plasma5-%{component}
Source0:        %{url}/archive/%{version}/plasma5-%{component}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Positioning)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5Package)
BuildRequires:  cmake(KF5Plasma)
BuildRequires:  cmake(libavif)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  /usr/bin/appstreamcli
BuildRequires:  /usr/bin/desktop-file-validate

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
desktop-file-validate %{buildroot}%{_datadir}/kservices5/plasma-wallpaper-com.github.zzag.dynamic.desktop

%files -f plasma_wallpaper_com.github.zzag.dynamic.lang
%license LICENSES/*
%{_datadir}/plasma/wallpapers/com.github.zzag.dynamic/
%{_datadir}/metainfo/com.github.zzag.dynamic.appdata.xml
%{_datadir}/kservices5/plasma-wallpaper-com.github.zzag.dynamic.desktop
%{_libdir}/qt5/qml/com/github/zzag/plasma/wallpapers/dynamic/
%{_libdir}/qt5/plugins/kpackage/packagestructure/packagestructure_dynamicwallpaper.so
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
* Tue Apr 11 2023 Iñaki Úcar <iucar@fedoraproject.org> - 4.4.0-9
- Adapt license tag to SPDX

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 01 2022 Kalev Lember <klember@redhat.com> - 4.4.0-7
- Rebuild for new libavif

* Sun Oct 23 2022 Robert-André Mauchin <zebob.m@gmail.com> - 4.4.0-6
- Rebuild for new libavif

* Sun Oct 23 2022 Robert-André Mauchin <zebob.m@gmail.com> - 4.4.0-5
- Rebuild for new libavif

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jul 16 2022 Iñaki Úcar <iucar@fedoraproject.org> - 4.4.0-3
- Rebuild for new version of private API

* Thu Jun 23 2022 Robert-André Mauchin <zebob.m@gmail.com> - 4.4.0-2
- Rebuilt for new libavif

* Tue Jun 14 2022 Iñaki Úcar <iucar@fedoraproject.org> - 4.4.0-1
- Bump to version 4.4.0

* Tue May 24 2022 Iñaki Úcar <iucar@fedoraproject.org> - 4.3.1-2
- Rebuild for new version of private API

* Sat Apr 23 2022 Iñaki Úcar <iucar@fedoraproject.org> - 4.3.1-1
- Bump to version 4.3.1

* Tue Apr 12 2022 Iñaki Úcar <iucar@fedoraproject.org> - 4.3.0-1
- Bump to version 4.3.0

* Mon Apr 11 2022 Iñaki Úcar <iucar@fedoraproject.org> - 4.1.0-1
- Bump to version 4.1.0

* Sat Apr 09 2022 Neal Gompa <ngompa@fedoraproject.org> - 4.0.0-1
- Bump to version 4.0.0 final

* Mon Mar 28 2022 Iñaki Úcar <iucar@fedoraproject.org> - 4.0.0~git20220328.d37f412-1
- Bump snapshot, fixes a crash when creating a preview

* Sun Mar 27 2022 Neal Gompa <ngompa@fedoraproject.org> - 4.0.0~git20220327.ca7b129-1
- Bump to snapshot version using AVIF instead HEIF
- Modernize spec
- Add checks for appstream metainfo and desktop files

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 3.3.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 3.3.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jun 05 2021 Iñaki Úcar <iucar@fedoraproject.org> - 3.3.9-1
- Update to v3.3.9

* Sat Nov 14 2020 Iñaki Úcar <iucar@fedoraproject.org> - 3.3.5-1
- Initial packaging for Fedora
