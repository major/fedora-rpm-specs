Name:       oclock
Version:    1.0.6
Release:    %autorelease
Summary:    A simple analog clock
License:    MIT
URL:        https://www.x.org
Source0:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz
Source1:    %{name}-%{version}.tar.xz.sig
# Keyring copied on 2023-02-26 from: xfontsel.gpg
Source2:        %{name}.gpg
BuildRequires:  automake libtool
BuildRequires:  gcc make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  xorg-x11-util-macros
BuildRequires:  gnupg2

Obsoletes:  xorg-x11-apps < 7.7-31

%description
oclock is a simple analog clock using the SHAPE extension to make
a round (possibly transparent) window.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build
autoreconf -v --install
%configure --disable-silent-rules
%make_build

%install
%make_install

%files
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/X11/app-defaults/Clock-color

%changelog
%autochangelog
