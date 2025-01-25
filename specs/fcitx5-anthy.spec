%global __provides_exclude_from ^%{_libdir}/fcitx5/.*\\.so$

Name:       fcitx5-anthy
Version:    5.1.6
Release:    %autorelease
Summary:    Anthy Wrapper for Fcitx5
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:    GPL-2.0-or-later
URL:        https://github.com/fcitx/fcitx5-anthy
Source:     https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.zst
Source1:    https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.zst.sig
Source2:    https://pgp.key-server.io/download/0x8E8B898CBF2412F9

BuildRequires:  gnupg2
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  cmake(Fcitx5Core)
BuildRequires:  pkgconfig(anthy)
BuildRequires:  gettext
BuildRequires:  /usr/bin/appstream-util
Requires:       hicolor-icon-theme
Requires:       fcitx5-data

%description
Anthy Wrapper for Fcitx5
Ported from scim-anthy. Released under GPL2+.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build
%cmake -GNinja
%cmake_build

%install
%cmake_install

# convert symlinked icons to copied icons, this will help co-existing with
# fcitx4-*
for iconfile in $(find %{buildroot}%{_datadir}/icons -type l)
do
  origicon=$(readlink -f ${iconfile})
  rm -f ${iconfile}
  cp ${origicon} ${iconfile}
done 
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
%find_lang %{name}

%files -f %{name}.lang
%license LICENSES/GPL-2.0-or-later.txt
%doc README.md AUTHORS 
%{_libdir}/fcitx5/libanthy.so
%{_datadir}/fcitx5/addon/anthy.conf
%{_datadir}/fcitx5/anthy
%{_datadir}/fcitx5/inputmethod/anthy.conf
%{_datadir}/icons/hicolor/*/status/*
%{_datadir}/icons/hicolor/*/apps/fcitx-anthy.png
%{_datadir}/icons/hicolor/*/apps/org.fcitx.Fcitx5.fcitx-anthy.png
%{_metainfodir}/org.fcitx.Fcitx5.Addon.Anthy.metainfo.xml

%changelog
%autochangelog
