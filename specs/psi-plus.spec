%global __provides_exclude_from ^%{_libdir}/psi-plus/plugins/.*$

%global version_l10n 1.5.2073

Name:           psi-plus
Version:        1.5.2081
Release:        %autorelease
Epoch:          1

# GPL-2.0-or-later - core project.
# LGPL-2.1-or-later - iris library, widgets, several tools.
# Zlib - bundled minizip library.
# MIT - bundled http-parser and qhttp libraries.
# Apache-2.0 - bundled libqite library.
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND Zlib AND MIT AND Apache-2.0
Summary:        XMPP client based on Qt
URL:            https://%{name}.com

Source0:        https://github.com/%{name}/%{name}-snapshots/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/%{name}/%{name}-l10n/archive/%{version_l10n}/%{name}-l10n-%{version_l10n}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
%if 0%{?fedora} && 0%{?fedora} >= 42
ExcludeArch: %{ix86}
%endif

BuildRequires:  cmake(Qca-qt6)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Keychain)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6SvgWidgets)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-app-1.0)
BuildRequires:  pkgconfig(gstreamer-audio-1.0)
BuildRequires:  pkgconfig(gstreamer-base-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(hunspell)
BuildRequires:  pkgconfig(libidn)
BuildRequires:  pkgconfig(libomemo-c)
BuildRequires:  pkgconfig(libotr)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(tidy)
BuildRequires:  pkgconfig(usrsctp)
BuildRequires:  pkgconfig(xscrnsaver)
BuildRequires:  pkgconfig(zlib)

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  libgcrypt-devel
BuildRequires:  ninja-build

Requires:       %{name}-common = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-plugins%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

Requires:       hicolor-icon-theme
Requires:       qca-qt6-gnupg%{?_isa}
Requires:       qca-qt6-ossl%{?_isa}

Provides:       bundled(http-parser) = 2.9.4
Provides:       bundled(iris) = 0~git
Provides:       bundled(libqite) = 0~git
Provides:       bundled(minizip) = 1.2.11
Provides:       bundled(qhttp) = 2.0.0

%description
%{name} is the premiere cross-platform Instant Messaging application.

Built upon an open protocol named XMPP, %{name} is a fast and lightweight
messaging client that utilises the best of open source technologies.

%{name} contains all the features necessary to chat, with no bloated extras
that slow your computer down. The XMPP protocol provides gateways to other
protocols.

%package common
License:        GPL-2.0-or-later
Summary:        Common assets for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}-i18n = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-i18n < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}-icons = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-icons < %{?epoch:%{epoch}:}%{version}-%{release}

%description common
This package contains architecture-agnostic common assets (language packs,
icons, themes, skins, etc.) for %{name}.

%package plugins
License:        GPL-2.0-or-later
Summary:        Additional plugins for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugins
This package adds additional plugins to %{name}.

%prep
%autosetup -n %{name}-snapshots-%{version} -p1

# Unpacking tarball with additional locales...
tar -xf %{SOURCE1} %{name}-l10n-%{version_l10n}/translations --strip=1

# Removing bundled libraries...
rm -rf iris/src/jdns

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_DEMO:BOOL=OFF \
    -DBUILD_PSIMEDIA:BOOL=ON \
    -DBUNDLED_QCA:BOOL=OFF \
    -DBUNDLED_USRSCTP:BOOL=OFF \
    -DCHAT_TYPE:STRING=BASIC \
    -DENABLE_PLUGINS:BOOL=ON \
    -DINSTALL_EXTRA_FILES:BOOL=ON \
    -DINSTALL_PLUGINS_SDK:BOOL=OFF \
    -DLIMIT_X11_USAGE:BOOL=OFF \
    -DPRODUCTION:BOOL=ON \
%if 0%{?fedora} && 0%{?fedora} >= 43
%if "%{?_lib}" == "lib64"
    -DLIB_SUFFIX:STRING=64 \
%endif
%endif
    -DUSE_ASPELL:BOOL=OFF \
    -DUSE_CRASH:BOOL=OFF \
    -DUSE_DBUS:BOOL=ON \
    -DUSE_ENCHANT:BOOL=OFF \
    -DUSE_HUNSPELL:BOOL=ON \
    -DUSE_KEYCHAIN:BOOL=ON \
    -DUSE_QT6:BOOL=ON \
    -DUSE_X11:BOOL=ON \
    -DUSE_XSS:BOOL=ON
%cmake_build

%install
%cmake_install
%find_lang psi --with-qt
rm -rf %{buildroot}%{_datadir}/%{name}/COPYING

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%license COPYING
%doc README
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/pixmaps/%{name}.png
%{_metainfodir}/%{name}.appdata.xml

%files common -f psi.lang
%{_datadir}/%{name}/certs
%{_datadir}/%{name}/iconsets
%{_datadir}/%{name}/skins
%{_datadir}/%{name}/sound
%{_datadir}/%{name}/*.{txt,html}

%files plugins
%{_libdir}/%{name}

%changelog
%autochangelog
