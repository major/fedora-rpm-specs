# necessary since commit string is part of release tar ball - Roland
%global _commit_string ea93b21f9498

Name:           speedcrunch
Version:        0.12
Release:        %autorelease
Summary:        A fast power user calculator

License:        GPL-2.0-or-later
URL:            https://www.speedcrunch.org
Source0:        https://bitbucket.org/heldercorreia/%{name}/get/release-%{version}.0.tar.bz2

Patch100:       %{name}-0.12-metainfo-fixes.patch
Patch101:       %{name}-0.12-cmake4-fixes.patch

BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Help)

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  librsvg2-tools
BuildRequires:  ninja-build
BuildRequires:  gcc-c++
BuildRequires:  cmake

%description
SpeedCrunch is a fast, high precision and powerful desktop calculator.
Among its distinctive features are a scrollable display, up to 50 decimal
precisions, unlimited variable storage, intelligent automatic completion
full keyboard-friendly and more than 15 built-in math function.

%prep
%autosetup -n heldercorreia-%{name}-%{_commit_string} -p1

%build
%cmake \
    -S src \
    -G Ninja \
    -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmake_install

# Install SVG icon
install -D -m 0644 -p gfx/%{name}.svg %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

# Create icons on the fly
for size in 16 22 24 32 48 64 128 256; do
    dest=%{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps
    mkdir -p ${dest}
    rsvg-convert -w ${size} -h ${size} gfx/%{name}.svg -o ${dest}/%{name}.png
    chmod 0644 ${dest}/%{name}.png
    touch -r gfx/%{name}.svg ${dest}/%{name}.png
done

desktop-file-install \
    --set-key=StartupWMClass \
    --set-value=%{name} \
    --dir=%{buildroot}%{_datadir}/applications \
    pkg/%{name}.desktop

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%license pkg/COPYING.rtf
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/pixmaps/%{name}.png
%{_metainfodir}/%{name}.appdata.xml

%changelog
%autochangelog
