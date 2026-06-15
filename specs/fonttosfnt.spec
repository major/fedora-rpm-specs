Name:       fonttosfnt
Version:    1.2.5
Release:    %autorelease
Summary:    Tool to wrap BDF or PCF bitmap fonts in an sfnt wrapper

License:    MIT
URL:        https://www.x.org
Source:     https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(fontenc)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xproto) >= 7.0.33

Conflicts:  xorg-x11-font-utils < 7.5-51

%description
fonttosfnt wraps a set of BDF or PCF bitmap fonts in a sfnt (TrueType or
OpenType) wrapper.

%prep
%autosetup

%build
%configure --disable-silent-rules
%make_build

%install
%make_install

%check
./fonttosfnt --version

%files
%license COPYING
%doc README.md
%{_bindir}/fonttosfnt
%{_mandir}/man1/fonttosfnt.1*

%changelog
%autochangelog
