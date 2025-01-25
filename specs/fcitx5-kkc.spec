%global __provides_exclude_from ^%{_libdir}/fcitx5/.*\\.so$

%if 0%{?fedora} >= 40
%global use_qt6 1
%else
%global use_qt6 0
%endif

%if %{use_qt6}
%define qt_major_ver 6
%else
%define qt_major_ver 5
%endif

Name:           fcitx5-kkc
Version:        5.1.6
Release:        %autorelease
Summary:        Libkkc input method support for Fcitx5
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
Url:            https://github.com/fcitx/fcitx5-kkc
Source:         https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.zst
Source1:        https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.zst.sig
Source2:        https://pgp.key-server.io/download/0x8E8B898CBF2412F9

BuildRequires:  gnupg2
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(Fcitx5Core)
BuildRequires:  cmake(Fcitx5Qt5WidgetsAddons)
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(kkc-1.0)
BuildRequires:  pkgconfig(Qt%{qt_major_ver}Core)
BuildRequires:  pkgconfig(Qt%{qt_major_ver}Gui)
BuildRequires:  pkgconfig(Qt%{qt_major_ver}Widgets)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  gettext
BuildRequires:  /usr/bin/appstream-util
Requires:       hicolor-icon-theme
Requires:       fcitx5-data
Requires:       libkkc-data

%description
This provides libkkc input method support for fcitx5. Released under GPL3+.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
%cmake -GNinja \
%if %{use_qt6}
  -DUSE_QT6=On
%else
  -DUSE_QT6=Off
%endif
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
%doc README.md
%license LICENSES/GPL-3.0-or-later.txt
%{_libdir}/fcitx5/kkc.so
%{_libdir}/fcitx5/qt%{qt_major_ver}/libfcitx5-kkc-config.so

%{_datadir}/fcitx5/addon/kkc.conf
%{_datadir}/fcitx5/inputmethod/kkc.conf

%dir %{_datadir}/fcitx5/kkc
%{_datadir}/fcitx5/kkc/dictionary_list
%{_datadir}/fcitx5/kkc/rule

%{_datadir}/icons/hicolor/*/apps/fcitx_kkc.png
%{_datadir}/icons/hicolor/*/apps/org.fcitx.Fcitx5.fcitx_kkc.png
%{_metainfodir}/org.fcitx.Fcitx5.Addon.Kkc.metainfo.xml
%changelog
%autochangelog
