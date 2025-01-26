%global __provides_exclude_from ^%{_libdir}/fcitx5/.*\\.so$

%if 0%{?fedora} >= 40 
  %ifarch %qt6_qtwebengine_arches
    %global use_qt6 1
    %define qtwebengine 1
  %else
    %global use_qt6 0
    %ifarch %qt5_qtwebengine_arches
      %define qtwebengine 1
    %else
      %define qtwebengine 0
    %endif
  %endif
%else
  %global use_qt6 0
  %ifarch %qt5_qtwebengine_arches
    %define qtwebengine 1
  %else
    %define qtwebengine 0
  %endif
%endif

%if %{use_qt6}
%define qt_major_ver 6
%else
%define qt_major_ver 5
%endif

Name:           fcitx5-chinese-addons
Version:        5.1.8
Release:        %autorelease
Summary:        Chinese related addon for fcitx5
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://github.com/fcitx/fcitx5-chinese-addons
Source:         https://download.fcitx-im.org/fcitx5/fcitx5-chinese-addons/fcitx5-chinese-addons-%{version}_dict.tar.zst
Source1:        https://download.fcitx-im.org/fcitx5/fcitx5-chinese-addons/fcitx5-chinese-addons-%{version}_dict.tar.zst.sig
Source2:        https://pgp.key-server.io/download/0x8E8B898CBF2412F9
Patch1:         0001-include-config.h-before-checking-macros.patch

BuildRequires:  gnupg2
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  fcitx5-qt-devel
BuildRequires:  fcitx5-lua-devel
BuildRequires:  gcc-c++
BuildRequires:  libime-devel
BuildRequires:  ninja-build
BuildRequires:  gettext-devel
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(fmt)
%if %{qtwebengine}
BuildRequires:  cmake(Qt%{qt_major_ver}WebEngineWidgets)
%else
BuildRequires:  cmake(Qt%{qt_major_ver}WebKitWidgets)
%endif
BuildRequires:  pkgconfig(opencc)
BuildRequires:  pkgconfig(Fcitx5Core)
BuildRequires:  pkgconfig(Fcitx5Module)
BuildRequires:  /usr/bin/appstream-util
Requires:       hicolor-icon-theme
Requires:       %{name}-data = %{version}-%{release}
Requires:       fcitx5-lua
Requires:       fcitx5-data

%description
This provides pinyin and table input method
support for fcitx5. Released under LGPL-2.1+.

im/pinyin/emoji.txt is derived from Unicode 
CLDR with modification.

%package data
Summary:        Data files of %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       hicolor-icon-theme
Requires:       fcitx5-lua
Requires:       fcitx5-data

%description data
The %{name}-data package provides shared data for %{name}.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       fcitx5-devel

%description devel
devel files for fcitx5-chinese-addons

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
%cmake -GNinja \
%if %{use_qt6}
    -DUSE_QT6=On \
%else
    -DUSE_QT6=Off \
%endif
%if %{qtwebengine}
    -DUSE_WEBKIT=Off
%else
    -DUSE_WEBKIT=On
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

%check
%ctest

%files -f %{name}.lang
%license LICENSES/LGPL-2.1-or-later.txt
%doc README.md 
%{_bindir}/scel2org5
%{_libdir}/fcitx5/*.so
%{_libdir}/fcitx5/qt%{qt_major_ver}/libpinyindictmanager.so
%{_libdir}/fcitx5/qt%{qt_major_ver}/libcustomphraseeditor.so

%files data
%dir %{_datadir}/fcitx5/pinyin
%dir %{_datadir}/fcitx5/punctuation
%dir %{_datadir}/fcitx5/pinyinhelper
%{_datadir}/fcitx5/addon/*.conf
%{_datadir}/fcitx5/inputmethod/*.conf
%{_datadir}/fcitx5/lua/imeapi/extensions/pinyin.lua
%{_datadir}/fcitx5/pinyin/*.dict
%{_datadir}/fcitx5/pinyin/symbols
%{_datadir}/fcitx5/pinyinhelper/py_*.mb
%{_datadir}/fcitx5/punctuation/punc.mb.*
%dir %{_datadir}/fcitx5/chttrans
%{_datadir}/fcitx5/chttrans/gbks2t.tab
%{_datadir}/icons/hicolor/*/apps/*
%{_metainfodir}/org.fcitx.Fcitx5.Addon.ChineseAddons.metainfo.xml

%files devel
%{_includedir}/Fcitx5/Module/fcitx-module/*
%{_libdir}/cmake/Fcitx5Module*

%changelog
%autochangelog
