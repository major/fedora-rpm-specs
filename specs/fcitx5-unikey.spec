%global __provides_exclude_from ^%{_libdir}/fcitx5/.*\\.so$

Name:       fcitx5-unikey
Version:    5.1.7
Release:    %autorelease
Summary:    Unikey support for Fcitx5
# Automatically converted from old format: GPLv2+ and LGPLv2+ - review is highly recommended.
License:    GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:        https://github.com/fcitx/fcitx5-unikey
Source:     https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.zst
Source1:    https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.zst.sig
Source2:    https://pgp.key-server.io/download/0x8E8B898CBF2412F9

BuildRequires:  gnupg2
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  cmake(Fcitx5Core)
BuildRequires:  cmake(Fcitx5Qt6WidgetsAddons)
BuildRequires:  cmake(qt6)
BuildRequires:  gettext
BuildRequires:  libappstream-glib
Requires:       hicolor-icon-theme
Requires:       fcitx5-data

%description
Unikey (Vietnamese Input Method) engine support for Fcitx5.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build
%cmake -GNinja
%cmake_build

%install
%cmake_install
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml

%find_lang %{name}

%files -f %{name}.lang
%license LICENSES/GPL-2.0-or-later.txt LICENSES/LGPL-2.0-or-later.txt
%doc README ChangeLog
%{_libdir}/fcitx5/libunikey.so
%{_libdir}/fcitx5/qt6/libfcitx5-unikey-macro-editor.so
%{_libdir}/fcitx5/qt6/libfcitx5-unikey-keymap-editor.so
%{_datadir}/fcitx5/addon/unikey.conf
%{_datadir}/fcitx5/inputmethod/unikey.conf
%{_datadir}/icons/hicolor/*/apps/fcitx-unikey.png
%{_datadir}/icons/hicolor/*/apps/org.fcitx.Fcitx5.fcitx-unikey.png
%{_metainfodir}/org.fcitx.Fcitx5.Addon.Unikey.metainfo.xml

%changelog
%autochangelog
