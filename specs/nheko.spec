Name: nheko
Version: 0.12.1
Release: %autorelease

License: GPL-3.0-or-later
Summary: Desktop client for the Matrix protocol
URL: https://github.com/Nheko-Reborn/%{name}
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# https://github.com/Nheko-Reborn/nheko/commit/af2ca72030deb14a920a888e807dc732d93e3714
Patch100: %{name}-0.12.1-search-for-qt-6.10.0-private-modules.patch
# https://github.com/Nheko-Reborn/nheko/commit/2769642d3c7bd3c0d830b2f18ef6b3bf6a710bf4
Patch101: %{name}-0.12.1-fix-most-reply-rendering-issues-with-qt-6.9.2.patch
# https://github.com/Nheko-Reborn/nheko/commit/93ce60d6f14679ab9f34edec166e9ad1884d3edd
Patch102: 0001-Qt-6.10-compat.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
%if 0%{?fedora} && 0%{?fedora} >= 42
ExcludeArch: %{ix86}
%endif

BuildRequires: cmake(KDSingleApplication-qt6) >= 1.0.0
BuildRequires: cmake(MatrixClient) >= 0.10.1
BuildRequires: cmake(Olm) >= 3.2.12
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Keychain)
BuildRequires: cmake(Qt6LinguistTools)
BuildRequires: cmake(Qt6Multimedia)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6QuickControls2)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(fmt) >= 9.1.0
BuildRequires: cmake(httplib) >= 0.5.12
BuildRequires: cmake(mpark_variant)
BuildRequires: cmake(nlohmann_json) >= 3.11.0
BuildRequires: cmake(spdlog) >= 1.0.0

BuildRequires: pkgconfig(blurhash) >= 0.2.0
BuildRequires: pkgconfig(coeurl) >= 0.3.1
BuildRequires: pkgconfig(gstreamer-1.0)
BuildRequires: pkgconfig(gstreamer-app-1.0)
BuildRequires: pkgconfig(gstreamer-audio-1.0)
BuildRequires: pkgconfig(gstreamer-base-1.0)
BuildRequires: pkgconfig(gstreamer-sdp-1.0)
BuildRequires: pkgconfig(gstreamer-video-1.0)
BuildRequires: pkgconfig(gstreamer-webrtc-1.0)
BuildRequires: pkgconfig(libcmark) >= 0.29.0
BuildRequires: pkgconfig(libcrypto)
BuildRequires: pkgconfig(libevent)
BuildRequires: pkgconfig(lmdb)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(re2)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xcb-ewmh)
BuildRequires: pkgconfig(zlib)

BuildRequires: lmdbxx-devel >= 1.0.0

BuildRequires: asciidoc
BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: libappstream-glib
BuildRequires: ninja-build

BuildRequires: qt6-qtbase-private-devel
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
Requires: hicolor-icon-theme

Recommends: google-noto-emoji-color-fonts
Recommends: google-noto-emoji-fonts
Recommends: qt-jdenticon%{?_isa}

%description
The motivation behind the project is to provide a native desktop app
for Matrix that feels more like a mainstream chat app.

%prep
%autosetup -p1
rm -rf third_party/{blurhash,cpp-httplib*}

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON \
    -DHUNTER_ENABLED:BOOL=OFF \
    -DCI_BUILD:BOOL=OFF \
    -DASAN:BOOL=OFF \
    -DQML_DEBUGGING:BOOL=OFF \
    -DBUILD_DOCS:BOOL=OFF \
    -DVOIP:BOOL=ON \
    -DMAN:BOOL=ON \
    -DUSE_BUNDLED_BLURHASH:BOOL=OFF \
    -DUSE_BUNDLED_CMARK:BOOL=OFF \
    -DUSE_BUNDLED_COEURL:BOOL=OFF \
    -DUSE_BUNDLED_CPPHTTPLIB:BOOL=OFF \
    -DUSE_BUNDLED_GTEST:BOOL=OFF \
    -DUSE_BUNDLED_JSON:BOOL=OFF \
    -DUSE_BUNDLED_KDSINGLEAPPLICATION:BOOL=OFF \
    -DUSE_BUNDLED_LIBCURL:BOOL=OFF \
    -DUSE_BUNDLED_LIBEVENT:BOOL=OFF \
    -DUSE_BUNDLED_LMDB:BOOL=OFF \
    -DUSE_BUNDLED_LMDBXX:BOOL=OFF \
    -DUSE_BUNDLED_MTXCLIENT:BOOL=OFF \
    -DUSE_BUNDLED_OLM:BOOL=OFF \
    -DUSE_BUNDLED_OPENSSL:BOOL=OFF \
    -DUSE_BUNDLED_QTKEYCHAIN:BOOL=OFF \
    -DUSE_BUNDLED_RE2:BOOL=OFF \
    -DUSE_BUNDLED_SPDLOG:BOOL=OFF
%cmake_build

%install
%cmake_install

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc README.md CHANGELOG.md
%license COPYING
%{_bindir}/%{name}
%{_metainfodir}/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_mandir}/man1/%{name}.1*
%{zsh_completions_dir}/_%{name}

%changelog
%autochangelog
