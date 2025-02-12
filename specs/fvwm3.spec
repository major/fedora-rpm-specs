Name:		fvwm3
Version:	1.1.2
Release:	%autorelease
Summary:	Highly configurable multiple virtual desktop window manager
# ./fvwm/screen.h "NTP License (legal disclaimer)",
# ./libs/cJSON.[ch] "MIT License"
# ./libs/queue.h "BSD 3-Clause License"
# ./libs/tree.h "BSD 2-Clause License"
License:	GPL-2.0-or-later AND NTP AND MIT and BSD-2-Clause AND BSD-3-Clause
URL:		https://www.fvwm.org/
Source0:	https://github.com/fvwmorg/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
# Fedora-specific
Patch1:		%{name}-0001-Use-mimeopen-instead-of-EDITOR.patch
# Fedora-specific
Patch2:		%{name}-0002-Skip-install-data-hook-for-default-configs.patch
# Submitted upstream as https://github.com/fvwmorg/fvwm/pull/100 and https://github.com/fvwmorg/fvwm3/pull/1132
Patch3:		%{name}-0003-Fixes-for-C99-compatibility.patch
# Upstream deprecated autotools support. https://github.com/fvwmorg/fvwm3/pull/1131
Patch4:		%{name}-0004-Replace-deprecated-AM_CONFIG_HEADER-with-AC_CONFIG_H.patch
Patch5:		%{name}-0005-Install-locale-into-standard-directory.patch
BuildRequires:	asciidoctor
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	desktop-file-utils
BuildRequires:	fribidi-devel
BuildRequires:	gcc
BuildRequires:	gettext
BuildRequires:	libX11-devel
BuildRequires:	libXcursor-devel
BuildRequires:	libXext-devel
BuildRequires:	libXft-devel
BuildRequires:	libXpm-devel
BuildRequires:	libXrandr-devel
BuildRequires:	libXt-devel
BuildRequires:	libevent-devel
BuildRequires:	libpng-devel
BuildRequires:	librsvg2-devel
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	readline-devel
BuildRequires:	xorg-x11-xtrans-devel
Requires:	xterm
Requires:	%{_bindir}/mimeopen
# for fvwm-menu-xlock
Requires:	xlockmore
# for fvwm-menu-desktop
Requires:	python3-pyxdg

%description
Fvwm is a window manager for X11. It is designed to minimize memory
consumption, provide a 3D look to window frames, and implement a virtual
desktop.

%prep
%autosetup -p1
rm -rf ./bin/FvwmPrompt/vendor/

%build
aclocal --force
autoreconf -ivf
%configure --enable-mandoc
%make_build

%install
%make_install
%find_lang %{name}

# xsession
install -D -m0644 -p %{SOURCE1} \
	%{buildroot}%{_datadir}/xsessions/%{name}.desktop

desktop-file-validate %{buildroot}%{_datadir}/xsessions/%{name}.desktop

%files -f %{name}.lang
%license COPYING
%doc README.md NEWS
%{_bindir}/*
%{_datadir}/%{name}/
%{_datadir}/xsessions/%{name}.desktop
%{_libexecdir}/%{name}/
%{_mandir}/man1/*

%changelog
%autochangelog
