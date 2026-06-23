Name:		xedit
Version:	1.2.4
Release:	%autorelease
Summary:	Simple text editor for X
URL:		https://xorg.freedesktop.org
Source0:	https://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz
Source1:	%{name}.desktop
License:	MIT AND BSD-3-Clause
BuildRequires:	gcc make
BuildRequires:	desktop-file-utils
BuildRequires:	libXaw-devel
BuildRequires:	xorg-x11-util-macros
Patch:		xedit-hunspell.patch
Requires:	xorg-x11-xbitmaps
Requires:	hunspell
Requires:	hunspell-en
Requires:	grep
Requires:	words
Requires:	ctags
Requires:	xorg-x11-fonts-misc
Requires:	xorg-x11-fonts-75dpi
Requires:	xorg-x11-fonts-100dpi

%description
Xedit provides a simple text editor for X.

%prep
%autosetup -p1
cp lisp/README README.lisp
cp lisp/re/README README.re

%build
%configure --with-lispdir=%{_datadir}/X11/%{name}
%make_build

%install
%make_install
install -D -m 644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
%make_build check

%files
%license COPYING
%doc AUTHORS ChangeLog README README.lisp README.re
%{_bindir}/%{name}
%{_datadir}/X11/%{name}
%{_datadir}/X11/app-defaults/Xedit
%{_datadir}/X11/app-defaults/Xedit-color
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/xedit.1*

%changelog
%autochangelog
