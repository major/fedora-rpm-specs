%global appname org.speedcrunch.SpeedCrunch
%global commit 3c1b4c18ccb275eb2891f9d8ff36a9205c0f566b
%global date 20241202

%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global tarballcommit %(c=%{commit}; echo ${c:0:12})

Name:           speedcrunch
Version:        0.12^%{date}git%{shortcommit}
Release:        %autorelease

License:        GPL-2.0-or-later
Summary:        A fast power user calculator
URL:            https://bitbucket.org/heldercorreia/%{name}
Source0:        %{url}/get/%{commit}.tar.bz2#/%{name}-%{tarballcommit}.tar.bz2

# https://bugs.gentoo.org/953885
Patch100:       %{name}-0.12-qhash.patch
Patch101:       %{name}-0.12-qsignalmapper.patch
# fixed id, name in qhp keywords section
Patch102:       %{name}-0.12-manual.patch
# workaround missing taskbar icon
Patch103:       %{name}-0.12-icon.patch

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Help)
BuildRequires:  cmake(Qt6Widgets)

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  librsvg2-tools
BuildRequires:  ninja-build
BuildRequires:  sed

Requires:       hicolor-icon-theme

%description
SpeedCrunch is a fast, high precision and powerful desktop calculator.
Among its distinctive features are a scrollable display, up to 50 decimal
precisions, unlimited variable storage, intelligent automatic completion
full keyboard-friendly and more than 15 built-in math function.

%prep
%autosetup -n heldercorreia-%{name}-%{tarballcommit} -p1

# fix project version
sed -i '/set(speedcrunch_VERSION/c\set(speedcrunch_VERSION "0.12")' src/CMakeLists.txt

# regenerate qch and qhc files
for lang in en_US de_DE fr_FR es_ES; do
    $(qtpaths6 --query QT_HOST_LIBEXECS)/qhelpgenerator doc/build_html_embedded/${lang}/manual-${lang}.qhp
    $(qtpaths6 --query QT_HOST_LIBEXECS)/qhelpgenerator doc/build_html_embedded/${lang}/manual-${lang}.qhcp
done

%build
%cmake \
    -S src \
    -G Ninja \
    -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmake_install

# Install SVG icon
install -D -m 0644 -p gfx/%{name}.svg %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/%{appname}.svg

# Create icons on the fly
for size in 16 22 24 32 48 64 128 256; do
    dest=%{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps
    mkdir -p ${dest}
    rsvg-convert -w ${size} -h ${size} gfx/%{name}.svg -o ${dest}/%{appname}.png
    chmod 0644 ${dest}/%{appname}.png
    touch -r gfx/%{name}.svg ${dest}/%{appname}.png
done

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{appname}.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{appname}.desktop

%files
%license pkg/COPYING.rtf
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{appname}.desktop
%{_datadir}/icons/hicolor/*/apps/%{appname}.*
%{_datadir}/pixmaps/%{appname}.png
%{_metainfodir}/%{appname}.metainfo.xml

%changelog
%autochangelog
