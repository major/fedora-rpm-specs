%global forgeurl https://gitlab.freedesktop.org/xorg/app/xeyes
Version:    1.3.1
%global archiveext tar.xz
%forgemeta

Name:       xeyes
Release:    %autorelease
Summary:    A follow the mouse X demo

License:    X11
URL:        %{forgeurl}
Source0:    %{forgesource}

BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb-damage)
BuildRequires:  pkgconfig(xcb-present) >= 1.9
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xi) >= 1.7
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xproto) >= 7.0.22
BuildRequires:  pkgconfig(xrender) >= 0.4
BuildRequires:  pkgconfig(xt)

%description
xeyes displays a pair of eyes that follow the mouse cursor.

%prep
%forgeautosetup

%build
autoreconf -v --install
%configure --disable-silent-rules
%make_build

%install
%make_install

%check
%make_build check

%files
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
