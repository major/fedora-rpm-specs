%global __provides_exclude_from ^%{_libdir}/fcitx5/.*\\.so$

Name:           fcitx5-lua
Version:        5.0.14
Release:        %autorelease
Summary:        Lua support for fcitx
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://github.com/fcitx/fcitx5-lua
Source:         https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.zst
Source1:        https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.zst.sig
Source2:        https://pgp.key-server.io/download/0x8E8B898CBF2412F9

BuildRequires:  gnupg2
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(lua)
BuildRequires:  pkgconfig(Fcitx5Core)
BuildRequires:  pkgconfig(Fcitx5Module)
BuildRequires:  /usr/bin/appstream-util
# to make testing happy
BuildRequires:  fcitx5
Requires:       fcitx5-data

%description
Lua support for fcitx.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       fcitx5-devel

%description devel
Devel files for fcitx5-lua

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build
%cmake -GNinja
%cmake_build 

%install
%cmake_install
install -d  %{buildroot}%{_datadir}/lua/imeapi/extensions
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
%find_lang %{name}

%check
%ctest

%files -f %{name}.lang
%license LICENSES/LGPL-2.1-or-later.txt
%doc README.md 
%{_libdir}/fcitx5/libluaaddonloader.so
%{_datadir}/fcitx5/addon/imeapi.conf
%{_datadir}/fcitx5/addon/luaaddonloader.conf
%{_datadir}/fcitx5/lua
%{_metainfodir}/org.fcitx.Fcitx5.Addon.Lua.metainfo.xml

%files devel
%{_includedir}/Fcitx5/Module/fcitx-module/luaaddonloader
%{_libdir}/cmake/Fcitx5ModuleLuaAddonLoader


%changelog
%autochangelog
