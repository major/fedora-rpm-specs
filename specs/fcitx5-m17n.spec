%global __provides_exclude_from ^%{_libdir}/fcitx5/.*\\.so$

Name:       fcitx5-m17n
Version:    5.1.3
Release:    %autorelease
Summary:    m17n Wrapper for Fcitx5
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:    LicenseRef-Callaway-LGPLv2+
URL:        https://github.com/fcitx/fcitx5-m17n
Source:     https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.zst
Source1:    https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.zst.sig
Source2:    https://pgp.key-server.io/download/0x8E8B898CBF2412F9

BuildRequires:  gnupg2
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  gettext
BuildRequires:  pkgconfig
BuildRequires:  cmake(Fcitx5Core)
BuildRequires:  cmake(fmt)
BuildRequires:  pkgconfig(m17n-gui) > 1.6.3
BuildRequires:  pkgconfig(m17n-db)
BuildRequires:  /usr/bin/appstream-util
Requires:       fcitx5-data
Requires:       pkgconfig(m17n-db)

%description
M17N is a large collection of input method, which can cover 
quite a lot languages in the world, including Latin, Arabic, 
etc.

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
%license LICENSES/LGPL-2.1-or-later.txt
%doc README.md 
%{_libdir}/fcitx5/m17n.so
%{_datadir}/fcitx5/addon/m17n.conf
%dir %{_datadir}/fcitx5/m17n
%{_datadir}/fcitx5/m17n/default
%{_metainfodir}/org.fcitx.Fcitx5.Addon.M17N.metainfo.xml

%changelog
%autochangelog
