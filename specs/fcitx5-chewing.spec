%global __provides_exclude_from ^%{_libdir}/fcitx5/.*\\.so$

Name:       fcitx5-chewing
Version:    5.1.7
Release:    %autorelease
Summary:    Chewing Wrapper for Fcitx
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:    LicenseRef-Callaway-LGPLv2+
URL:        https://github.com/fcitx/fcitx5-chewing
Source:     https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.zst
Source1:    https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.zst.sig
Source2:    https://pgp.key-server.io/download/0x8E8B898CBF2412F9

BuildRequires:  gnupg2
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  intltool
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(Fcitx5Core)
BuildRequires:  pkgconfig(chewing)
BuildRequires:  gettext
BuildRequires:  /usr/bin/appstream-util
Requires:       hicolor-icon-theme
Requires:       fcitx5-data

%description
fcitx5-chewing is a Chewing Wrapper for Fcitx.

Chewing is a set of free intelligent Chinese 
Phonetic IME.


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
%{_libdir}/fcitx5/libchewing.so
%{_datadir}/fcitx5/addon/chewing.conf
%{_datadir}/fcitx5/inputmethod/chewing.conf
%{_datadir}/icons/hicolor/*/apps/fcitx-chewing.png
%{_datadir}/icons/hicolor/*/apps/org.fcitx.Fcitx5.fcitx-chewing.png
%{_metainfodir}/org.fcitx.Fcitx5.Addon.Chewing.metainfo.xml

%changelog
%autochangelog
