Name:       utox
Version:    0.18.1
Release:    %autorelease
Summary:    The lightweight Tox client

# Automatically converted from old format: MIT or GPLv3+ - review is highly recommended.
License:    LicenseRef-Callaway-MIT OR GPL-3.0-or-later
URL:        https://github.com/uTox/uTox/
Source0:    %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:    %{name}.appdata.xml
# git clone https://github.com/uTox/uTox
# cd uTox
# git checkout v0.18.1
# git submodule init ; git submodule update
# tar -zcvf third_party.tar.gz third_party/
Source2:    third_party.tar.gz

# https://github.com/uTox/uTox/issues/1541
# ExcludeArch:    s390x

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(filteraudio)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(vpx)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(libv4l2)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(libsodium)
BuildRequires:  pkgconfig(toxcore)
Requires:       hicolor-icon-theme

%description
%summary

%prep
%autosetup -p 1 -n uTox-%{version}
%autosetup -N -T -D -a 2 -n uTox-%{version}

%build
# We use CMAKE_BUILD_TYPE="Release" to turn ASAN off
%cmake -DCMAKE_POLICY_VERSION_MINIMUM=3.5  -DCMAKE_BUILD_TYPE="Release"
%cmake_build

%install
%cmake_install
install -Dp -m 644 %{SOURCE1} %{buildroot}/%{_datadir}/metainfo/%{name}.appdata.xml
rm -rf %{buildroot}/%{_datadir}/icons/hicolor/14x14

%check
# Test "chrono" fails on armv7l
%ifnarch %{arm}
%ctest
%endif
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/%{name}.appdata.xml

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/%{name}
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}*
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
