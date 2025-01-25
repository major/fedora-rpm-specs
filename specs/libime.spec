Name:       libime  
Version:    1.1.10
# Automatically converted from old format: LGPLv2+ and MIT and BSD - review is highly recommended.
License:    LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-MIT AND LicenseRef-Callaway-BSD
Release:    %autorelease
Summary:    This is a library to support generic input method implementation
URL:        https://github.com/fcitx/libime
Source:     https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}_dict.tar.zst
Source1:    https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}_dict.tar.zst.sig
Source2:    https://pgp.key-server.io/download/0x8E8B898CBF2412F9

BuildRequires: gnupg2
BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: gcc-c++
BuildRequires: fcitx5-devel
BuildRequires: boost-devel
BuildRequires: extra-cmake-modules
BuildRequires: python3
BuildRequires: doxygen
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(bzip2)
BuildRequires: pkgconfig(libzstd)
BuildRequires: pkgconfig(eigen3)
Requires:      %{name}-data


%description
This is a library to support generic input method implementation.

%package data
Summary:        Data files of %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       hicolor-icon-theme

%description data
The %{name}-data package provides shared data for %{name}.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       boost-devel%{?_isa}

%description devel
Development files for %{name}

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build
%cmake -GNinja
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSES/LGPL-2.1-or-later.txt src/libime/core/kenlm/LICENSE
%doc README.md 
%{_bindir}/%{name}_history
%{_bindir}/%{name}_pinyindict
%{_bindir}/%{name}_prediction
%{_bindir}/%{name}_slm_build_binary
%{_bindir}/%{name}_tabledict
%{_bindir}/%{name}_migrate_fcitx4_pinyin
%{_bindir}/%{name}_migrate_fcitx4_table
%{_libdir}/libIMECore.so.0
%{_libdir}/libIMEPinyin.so.0
%{_libdir}/libIMETable.so.0
# upstream's soname and soversion dont match 
# libxxx.so.X* won't work
%{_libdir}/libIMECore.so.*.*
%{_libdir}/libIMEPinyin.so.*.*
%{_libdir}/libIMETable.so.*.*
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/zh_CN.lm
%{_libdir}/%{name}/zh_CN.lm.predict

%files data
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.dict

%files devel
%{_libdir}/libIMECore.so
%{_libdir}/libIMEPinyin.so
%{_libdir}/libIMETable.so
%{_libdir}/cmake/LibIME*
%{_includedir}/LibIME/



%changelog
%autochangelog
