%global pname QMPlay2
%global __provides_exclude_from ^%{_libdir}/%{name}/modules/.*$
%undefine _strict_symbol_defs_build

Name:           qmplay2
Version:        25.01.19
Release:        %autorelease
Summary:        A Qt based media player, streamer and downloader
# LGPL-3.0-or-later: QMPlay2
# MIT: src/qmvk, src/modules/AudioFilters/bs2b
# Public-Domain: src/modules/Modplug/libmodplug
License:        LGPL-3.0-or-later AND MIT AND LicenseRef-Fedora-Public-Domain
URL:            https://github.com/zaps166/QMPlay2
Source:         %{url}/releases/download/%{version}/%{pname}-src-%{version}.tar.xz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  ninja-build

BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6LinguistTools)

BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(libass)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libcddb)
BuildRequires:  pkgconfig(libcdio)
BuildRequires:  pkgconfig(libgme)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libpulse-simple)
BuildRequires:  pkgconfig(libsidplayfp)
BuildRequires:  pkgconfig(libswresample)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(libva-drm)
BuildRequires:  pkgconfig(portaudio-2.0)
BuildRequires:  pkgconfig(rubberband)
BuildRequires:  pkgconfig(taglib)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xv)
BuildRequires:  glslc

Requires:       hicolor-icon-theme
Requires:       kde-filesystem
Requires:       shared-mime-info
Recommends:     yt-dlp

# These have been converted to C++ and otherwise modified, not cleanly unbundleable
Provides:       bundled(libbs2b) = 3.1.0
Provides:       bundled(libmodplug)
# Private library from the same project
Provides:       bundled(qmvk)

Obsoletes:      %{name}-kde-integration < %{version}-%{release}

%description
%{name} is a video player, it can play and stream all formats supported by
ffmpeg and libmodplug (including J2B). It has an integrated Youtube browser.

%package        devel
Summary:        %{pname} development files
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
It's a development package for %{name}.


%prep
%autosetup -p1 -n %{pname}-src-%{version}
# unbundle vulkan headers
find src/qmplay2/vulkan/headers -delete
%if 0%{?fedora} >= 41 || 0%{?rhel} >= 11
# fix for vulkan-headers >= 1.3.301
# https://github.com/KhronosGroup/Vulkan-Headers/pull/512
sed -i -r 's/vk::(DispatchLoaderDynamic|DynamicLoader)/vk::detail::\1/g' \
    src/qmvk/*.[ch]pp src/qmplay2/vulkan/VulkanInstance.cpp
%endif
# subproject and bundled license files
cp src/qmvk/LICENSE LICENSE.qmvk
cp src/modules/Modplug/libmodplug/COPYING COPYING.libmodplug


%build
%cmake \
    -G Ninja \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DUSE_UPDATES=OFF \
    -DSOLID_ACTIONS_INSTALL_PATH=%{_datadir}/solid/actions

%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name --with-qt

# AUTHORS & ChangeLog are required for Help->About window
rm -f %{buildroot}%{_datadir}/qmplay2/{LICENSE,README.md}


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{pname}*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{pname}.appdata.xml


%files -f %{name}.lang
%doc AUTHORS ChangeLog README.md
%license LICENSE LICENSE.qmvk COPYING.libmodplug
%{_bindir}/%{pname}
%{_libdir}/%{name}/
%{_libdir}/libqmplay2.so
%{_datadir}/applications/%{pname}*.desktop
%{_datadir}/icons/hicolor/*/apps/%{pname}.*
%{_datadir}/mime/packages/x-*.xml
%{_datadir}/solid/actions/*.desktop
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/AUTHORS
%{_datadir}/%{name}/ChangeLog
%dir %{_datadir}/%{name}/lang/
%{_mandir}/man1/%{pname}.1*
%{_metainfodir}/%{pname}.appdata.xml

%files devel
%{_includedir}/%{pname}/

%changelog
%autochangelog
