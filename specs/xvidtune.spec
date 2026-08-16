%global forgeurl https://gitlab.freedesktop.org/xorg/app/xvidtune
Version:        1.0.4
%global tag     %{name}-%{version}
%forgemeta
%global distprefix %{nil}

Name:           xvidtune
Release:        %autorelease
Summary:        Video mode tuner for Xorg
License:        X11-distribute-modifications-variant
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xxf86vm)

%description
xvidtune is a client interface to the X server video mode extension
(XFree86-VidModeExtension).

%prep
%forgeautosetup

%build
autoreconf -v --install
%configure --disable-silent-rules
%make_build

%install
%make_install

%check
# No upstream tests exist

%files
%license COPYING
%{_bindir}/xvidtune
%{_mandir}/man1/xvidtune.1*
%{_datadir}/X11/app-defaults/Xvidtune

%changelog
%autochangelog
