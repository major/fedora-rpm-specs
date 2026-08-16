%global forgeurl https://gitlab.freedesktop.org/xorg/app/x11perf
Version:    1.7.0
%global archiveext tar.xz
%forgemeta

Name:       x11perf
Release:    %autorelease
Summary:    X11 server performance test program

License:    SMLNJ AND HPND
URL:        %{forgeurl}
Source0:    %{forgesource}

BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xmuu)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xrender)

%description
The x11perf program runs one or more performance tests and reports how fast
an X server can execute the tests.

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
%{_bindir}/x11perf
%{_bindir}/x11perfcomp
%{_mandir}/man1/x11perf.1*
%{_mandir}/man1/x11perfcomp.1*
%{_mandir}/man1/Xmark.1*
%{_datadir}/X11/x11perfcomp

%changelog
%autochangelog
