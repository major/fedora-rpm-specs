Name:       xclipboard
Version:    1.1.6
Release:    %autorelease
Summary:    Utility to collect and display text selections

License:    MIT-open-group
URL:        https://www.x.org
Source0:    https://xorg.freedesktop.org/archive/individual/app/%{name}-%{version}.tar.xz
Source1:    https://xorg.freedesktop.org/archive/individual/app/%{name}-%{version}.tar.xz.sig
Source2:    gpgkey-3AB285232C46AE43D8E192F4DAB0F78EA6E7E2D2.gpg

BuildRequires:  gcc
BuildRequires:  gpgverify
BuildRequires:  meson
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xproto) >= 7.0.17
BuildRequires:  pkgconfig(xt) >= 1.1

%description
xclipboard is used to collect and display text selections that are
sent to the CLIPBOARD by other clients.  It is typically used to save
CLIPBOARD selections for later use.  It stores each CLIPBOARD
selection as a separate string, each of which can be selected.

%prep
%{gpgverify} --keyring=%{SOURCE2} --signature=%{SOURCE1} --data=%{SOURCE0}
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
%doc README.md
%{_bindir}/xclipboard
%{_bindir}/xcutsel
%{_mandir}/man1/xclipboard.1*
%{_mandir}/man1/xcutsel.1*
%{_datadir}/X11/app-defaults/XClipboard

%changelog
%autochangelog
