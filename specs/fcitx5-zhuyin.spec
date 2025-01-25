%global __provides_exclude_from ^%{_libdir}/fcitx5/.*\\.so$

Name:       fcitx5-zhuyin
Version:    5.1.3
Release:    %autorelease
Summary:    Libzhuyin Wrapper for Fcitx
License:    GPL-2.0-or-later
URL:        https://github.com/fcitx/fcitx5-zhuyin
Source:     https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}_dict.tar.zst
Source1:    https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}_dict.tar.zst.sig
Source2:    https://pgp.key-server.io/download/0x8E8B898CBF2412F9

BuildRequires:  gnupg2
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  cmake(Fcitx5Core)
BuildRequires:  pkgconfig(libzhuyin) >= 2.3.0
BuildRequires:  libpinyin-tools
BuildRequires:  cmake(fmt)
BuildRequires:  gettext
BuildRequires:  libappstream-glib
Requires:       %{name}-data = %{version}-%{release}

%description
Libzhuyin Wrapper for Fcitx.

%package data
Summary:        Data files for fcitx5-zhuyin
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       fcitx5-lua
Requires:       fcitx5-data
Requires:       hicolor-icon-theme

%description data
Provides data files and icon files need for fcitx5-zhuyin package.

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

%files -f %{name}.lang
%license LICENSES/GPL-2.0-or-later.txt
%doc README AUTHORS ChangeLog 
%{_libdir}/fcitx5/zhuyin.so
%{_metainfodir}/org.fcitx.Fcitx5.Addon.Zhuyin.metainfo.xml

%files data
%{_datadir}/fcitx5/addon/zhuyin.conf
%{_datadir}/fcitx5/inputmethod/zhuyin.conf
%{_datadir}/icons/hicolor/*/apps/fcitx-bopomofo.png
%{_datadir}/icons/hicolor/*/apps/org.fcitx.Fcitx5.fcitx-bopomofo.png
%{_datadir}/fcitx5/zhuyin
%{_datadir}/fcitx5/lua/imeapi/extensions/zhuyin.lua

%changelog
%autochangelog
