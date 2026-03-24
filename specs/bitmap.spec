Name:           bitmap
Version:        1.1.2
Release:        %autorelease
Summary:        Bitmaps editor and converter utilities for the X Window System
License:        MIT
URL:            https://www.x.org
Source0:        https://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz
Source1:        bitmap.desktop
Source2:        bitmap.png

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xbitmaps)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xproto) >= 7.0.25
BuildRequires:  pkgconfig(xt)

Requires:       xorg-x11-xbitmaps

%description
Bitmap provides a bitmap editor and misc converter utilities for the X
Window System.

The package also includes files defining bitmaps associated with the 
Bitmap x11 editor.

%prep
%autosetup

%build
%configure
%make_build AM_LDFLAGS=-lXmu

%install
%make_install INSTALL="install -p"

desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE1}

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
install -p -m 644 %{SOURCE2} %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/bitmap.desktop

%files
%license COPYING
%doc ChangeLog README.md
%{_bindir}/atobm
%{_bindir}/bmtoa
%{_bindir}/bitmap
%{_includedir}/X11/bitmaps/*
%{_datadir}/X11/app-defaults/Bitmap*
%{_datadir}/applications/bitmap.desktop
%{_datadir}/icons/hicolor/32x32/apps/bitmap.png
%{_mandir}/man1/*.1*

%changelog
%autochangelog
