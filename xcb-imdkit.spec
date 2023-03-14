Name:       xcb-imdkit
Version:    1.0.5
Release:    %autorelease
Summary:    Input method development support for xcb
# source files in src/xlibi18n use the "old style" MIT license known as NTP.
License:    LGPLv2 and MIT
URL:        https://github.com/fcitx/xcb-imdkit
Source:     https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.xz
Source1:    https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.xz.sig
Source2:    https://pgp.key-server.io/download/0x8E8B898CBF2412F9

BuildRequires:  gnupg2
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-util)

%description
xcb-imdkit is an implementation of xim protocol in xcb, 
comparing with the implementation of IMDkit with Xlib, 
and xim inside Xlib, it has less memory foot print, 
better performance, and safer on malformed client.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Devel files for xcb-imdkit

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSES/LGPL-2.1-only.txt
%doc README.md
%{_libdir}/lib%{name}.so.1*

%files devel
%{_includedir}/xcb-imdkit/
%{_libdir}/cmake/XCBImdkit/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/xcb-imdkit.pc

%changelog
%autochangelog
