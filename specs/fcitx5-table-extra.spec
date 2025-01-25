Name:       fcitx5-table-extra
Version:    5.1.7
Release:    %autorelease
Summary:    Extra tables for Fcitx5
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:    GPL-3.0-or-later
URL:        https://github.com/fcitx/fcitx5-table-extra
Source:     https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.zst
Source1:    https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.zst.sig
Source2:    https://pgp.key-server.io/download/0x8E8B898CBF2412F9
Patch1:     0001-tell-CMAKE-no-compiler-will-be-used.patch

BuildArch:  noarch

BuildRequires:  gnupg2
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  ninja-build
BuildRequires:  boost-devel
BuildRequires:  cmake(Fcitx5Core)
BuildRequires:  cmake(LibIMETable)
BuildRequires:  gettext
BuildRequires:  /usr/bin/appstream-util
Requires:       hicolor-icon-theme
Requires:       fcitx5-data

%description
Extra tables for Fcitx5.
fcitx5-table-extra provides extra table for 
Fcitx5, including Boshiamy, Zhengma, Cangjie, 
and Quick.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build
# %%{_libdir} expands to /usr/lib, even on 64bit platform, that we need to
# to this tricky thing
%cmake -GNinja -DCMAKE_PREFIX_PATH="%{_libdir}/cmake;%{_libdir}64/cmake"
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
%files
%license LICENSES/GPL-3.0-or-later.txt
%doc README NEWS AUTHORS 
%{_datadir}/fcitx5/table/*
%{_datadir}/fcitx5/inputmethod/*
%{_datadir}/icons/hicolor/*/apps/*
%{_metainfodir}/org.fcitx.Fcitx5.Addon.TableExtra.metainfo.xml

%changelog
%autochangelog
