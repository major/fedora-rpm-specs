%global __provides_exclude_from ^%{_libdir}/weechat/plugins/.*$

Name:      weechat
Version:   4.5.1
Release:   %autorelease
Summary:   Portable, fast, light and extensible IRC client
Group:     Applications/Communications
URL:       http://weechat.org
License:   GPL-3.0-only

Source:    https://weechat.org/files/src/%{name}-%{version}.tar.xz
Source1:   https://weechat.org/files/src/%{name}-%{version}.tar.xz.asc
Source2:   https://keys.openpgp.org/vks/v1/by-fingerprint/A9AB5AB778FA5C3522FD0378F82F4B16DEC408F8

# https://github.com/weechat/weechat/pull/2229
Patch:     https://github.com/weechat/weechat/commit/68c70e55389bcd7a39ebec13cd9645a09b7f6a99.patch
Patch1:    https://github.com/weechat/weechat/commit/4b7be27028dac22b3ec6703c53c7bc154a0cb2b0.patch
# https://github.com/weechat/weechat/pull/2230
Patch2:    https://github.com/weechat/weechat/commit/04aea1bcb5b6f1e3e6e1253f92772fa6c2f4f939.patch

BuildRequires: asciidoctor
BuildRequires: ca-certificates
BuildRequires: cjson-devel
BuildRequires: cmake
BuildRequires: cpputest-devel
BuildRequires: docbook-style-xsl
BuildRequires: enchant-devel
BuildRequires: gcc
BuildRequires: gettext
BuildRequires: glibc-langpack-en
BuildRequires: gnupg2
BuildRequires: gnutls-devel
BuildRequires: guile30-devel
BuildRequires: libcurl-devel
BuildRequires: libgcrypt-devel
BuildRequires: libzstd-devel
BuildRequires: lua-devel
BuildRequires: ncurses-devel
BuildRequires: perl-devel
BuildRequires: perl-ExtUtils-Embed
BuildRequires: pkgconfig
BuildRequires: python3-devel
BuildRequires: ruby
BuildRequires: ruby-devel
BuildRequires: source-highlight
BuildRequires: tcl-devel
BuildRequires: zlib-devel

Requires:      hicolor-icon-theme

%description
WeeChat (Wee Enhanced Environment for Chat) is a portable, fast, light and
extensible IRC client. Everything can be done with a keyboard.
It is customizable and extensible with scripts.

%package devel
Summary: Development files for weechat
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig

%description devel
WeeChat (Wee Enhanced Environment for Chat) is a portable, fast, light and
extensible IRC client. Everything can be done with a keyboard.
It is customizable and extensible with scripts.

This package contains include files and pc file for weechat.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1 -n %{name}-%{version}


%build
%cmake \
  -DPREFIX=%{_prefix} \
  -DLIBDIR=%{_libdir} \
  -DENABLE_ENCHANT=ON \
  -DENABLE_PHP=OFF \
  -DENABLE_TESTS=ON \
  -DENABLE_DOC=ON \
  -DENABLE_DOC_INCOMPLETE=ON \
  -DENABLE_MAN=ON \
  %{nil}
%cmake_build


%install
%cmake_install

%find_lang %name


%check
%ctest --verbose


%files -f %{name}.lang
%doc AUTHORS.md CHANGELOG.md CONTRIBUTING.md
%doc README.md UPGRADING.md
%license COPYING
%{_bindir}/%{name}-curses
%{_bindir}/%{name}
%{_bindir}/%{name}-headless
%{_libdir}/%{name}
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
%{_datadir}/icons/hicolor/512x512/apps/%{name}.png
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%{_pkgdocdir}/weechat_*.html
%{_mandir}/man1/weechat.1*
%{_mandir}/*/man1/weechat.1*
%{_mandir}/man1/%{name}-headless.1*
%{_mandir}/*/man1/%{name}-headless.1*

%files devel
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/weechat-plugin.h
%{_libdir}/pkgconfig/*.pc


%changelog
%autochangelog
