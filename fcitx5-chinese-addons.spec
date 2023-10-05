%global __provides_exclude_from ^%{_libdir}/fcitx5/.*\\.so$

Name:           fcitx5-chinese-addons
Version:        5.1.1
Release:        %autorelease
Summary:        Chinese related addon for fcitx5
License:        LGPLv2+
URL:            https://github.com/fcitx/fcitx5-chinese-addons
Source:         https://download.fcitx-im.org/fcitx5/fcitx5-chinese-addons/fcitx5-chinese-addons-%{version}_dict.tar.xz
Source1:        https://download.fcitx-im.org/fcitx5/fcitx5-chinese-addons/fcitx5-chinese-addons-%{version}_dict.tar.xz.sig
Source2:        https://pgp.key-server.io/download/0x8E8B898CBF2412F9

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
BuildRequires:  pkgconfig(Qt5WebKit)
BuildRequires:  pkgconfig(Qt5WebKitWidgets)
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

%check
# workaround for a testing failure due to not finding .dict files
%ctest

%files -f %{name}.lang
%license LICENSES/LGPL-2.1-or-later.txt
%doc README.md 
%{_bindir}/scel2org5
%{_libdir}/fcitx5/*.so
%{_libdir}/fcitx5/qt5/libpinyindictmanager.so
%{_libdir}/fcitx5/qt5/libcustomphraseeditor.so

%files data
%dir %{_datadir}/fcitx5/pinyin
%dir %{_datadir}/fcitx5/punctuation
%dir %{_datadir}/fcitx5/pinyinhelper
%{_datadir}/fcitx5/addon/*.conf
%{_datadir}/fcitx5/inputmethod/*.conf
%{_datadir}/fcitx5/lua/imeapi/extensions/pinyin.lua
%{_datadir}/fcitx5/pinyin/*.dict
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
