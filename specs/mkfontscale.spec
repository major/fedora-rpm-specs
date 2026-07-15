Name:       mkfontscale
Version:    1.2.4
Release:    %autorelease
Summary:    Tool to generate legacy X11 font system index files

License:    MIT-open-group AND X11 AND MIT AND HPND-sell-variant
URL:        https://www.x.org
Source0:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz
Source1:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz.sig
Source2:    gpgkey-3AB285232C46AE43D8E192F4DAB0F78EA6E7E2D2.gpg

Patch0:     mkfontscale-examine-all-encodings.patch

BuildRequires: gcc
BuildRequires: gpgverify
BuildRequires: meson
BuildRequires: pkgconfig(fontenc)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(xproto) >= 7.0.25
BuildRequires: pkgconfig(zlib)

# Used to be a separate upstream repo in xorg-x11-font-utils, now it's part
# of mkfontscale. Keep the Provides alive though.
Provides:   mkfontdir = %{version}

%description
mkfontscale creates the fonts.scale and fonts.dir index files used by the
legacy X11 font system.  It now includes the mkfontdir script previously
distributed separately for compatibility with older X11 versions.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license COPYING
%{_bindir}/mkfontdir
%{_bindir}/mkfontscale
%{_mandir}/man1/mkfontdir.1*
%{_mandir}/man1/mkfontscale.1*

%changelog
%autochangelog
