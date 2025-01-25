%global __provides_exclude_from ^%{_libdir}/fcitx5/.*\\.so$

Name:       fcitx5-hangul
Version:    5.1.6
Release:    %autorelease
Summary:    Hangul Wrapper for Fcitx5
# data/symbol.txt is licensed under BSE license
# Automatically converted from old format: LGPLv2+ and BSD - review is highly recommended.
License:    LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-BSD
URL:        https://github.com/fcitx/fcitx5-hangul
Source:     https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.zst
Source1:    https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.zst.sig
Source2:    https://pgp.key-server.io/download/0x8E8B898CBF2412F9

BuildRequires:  gnupg2
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  cmake(Fcitx5Core)
BuildRequires:  pkgconfig(libhangul) >= 0.0.12
BuildRequires:  gettext
BuildRequires:  /usr/bin/appstream-util
Requires:       hicolor-icon-theme
Requires:       fcitx5-data

%description
%{summary}.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build
%cmake -GNinja
%cmake_build

%install
%cmake_install

# convert symlinked icons to copied icons, this will help co-existing with
# fcitx4
for iconfile in $(find %{buildroot}%{_datadir}/icons -type l)
do
  origicon=$(readlink -f ${iconfile})
  rm -f ${iconfile}
  cp ${origicon} ${iconfile}
done 
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
%find_lang %{name}

%files -f %{name}.lang
%license LICENSES/LGPL-2.1-or-later.txt
%doc README.md 
%{_libdir}/fcitx5/libhangul.so
%{_datadir}/fcitx5/addon/hangul.conf
%{_datadir}/fcitx5/hangul
%{_datadir}/fcitx5/inputmethod/hangul.conf
%{_datadir}/icons/hicolor/*/apps/*.png
%{_metainfodir}/org.fcitx.Fcitx5.Addon.Hangul.metainfo.xml

%changelog
%autochangelog
