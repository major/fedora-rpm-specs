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


Name:       fcitx5-skk
Version:    5.1.6
Release:    %autorelease
Summary:    Japanese SKK (Simple Kana Kanji) Engine for Fcitx5
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:    GPL-3.0-or-later
URL:        https://github.com/fcitx/fcitx5-skk
Source:     https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.zst
Source1:    https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.zst.sig
Source2:    https://pgp.key-server.io/download/0x8E8B898CBF2412F9

BuildRequires:  gnupg2
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  extra-cmake-modules
BuildRequires:  fcitx5-qt-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Fcitx5Core)
BuildRequires:  pkgconfig(libskk)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(Qt%{qt_major_ver})
BuildRequires:  pkgconfig(Qt%{qt_major_ver}Core)
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  /usr/bin/appstream-util
Requires:       skkdic
Requires:       hicolor-icon-theme
Requires:       fcitx5-data

%description
Fcitx5-skk is an SKK (Simple Kana Kanji) engine for Fcitx.  It provides
Japanese input method using libskk.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build
%cmake -DCMAKE_CXX_STANDARD=17 -GNinja \
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
%license LICENSES/GPL-3.0-or-later.txt
%doc README.md 
%{_libdir}/fcitx5/qt%{qt_major_ver}/libfcitx5-skk-config.so
%{_libdir}/fcitx5/skk.so
%{_datadir}/fcitx5/addon/skk.conf
%{_datadir}/fcitx5/inputmethod/skk.conf
%dir %{_datadir}/fcitx5/skk
%{_datadir}/fcitx5/skk/dictionary_list
%{_datadir}/icons/hicolor/*/apps/fcitx_skk.png
%{_datadir}/icons/hicolor/*/apps/org.fcitx.Fcitx5.fcitx_skk.png
%{_metainfodir}/org.fcitx.Fcitx5.Addon.Skk.metainfo.xml

%changelog
%autochangelog
