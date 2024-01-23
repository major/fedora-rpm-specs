Name:		fvwm
Version:	2.7.0
Release:	%autorelease
Summary:	Highly configurable multiple virtual desktop window manager
License:	GPLv2+
URL:		https://www.fvwm.org/
Source0:	https://github.com/fvwmorg/fvwm/archive/%{version}/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch1:		fvwm-0001-Change-html-viewer-to-xdg-open.patch
Patch2:		fvwm-0002-Use-mimeopen-instead-of-EDITOR.patch
# This has to be proposed upstream
Patch3:		fvwm-0003-FvwmPager-be-more-careful-with-window-labels.patch
# Fedora-specific
Patch4:		fvwm-0004-Skip-install-data-hook-for-default-configs.patch
# Backported from https://github.com/fvwmorg/fvwm3/pull/683
Patch5:		fvwm-0005-Fix-for-lock-recusion-in-handle_all_expose.patch
# Suvbmitted upstream as https://github.com/fvwmorg/fvwm/pull/100
Patch6:		fvwm-0006-Fixes-for-C99-compatibility.patch
# Suvbmitted upstream as https://github.com/fvwmorg/fvwm/pull/100
Patch7:		fvwm-0007-Fixes-for-C99-compatibility.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	fribidi-devel
BuildRequires:	gcc
BuildRequires:	gettext
BuildRequires:	libX11-devel
BuildRequires:	libXcursor-devel
BuildRequires:	libXext-devel
BuildRequires:	libXft-devel
BuildRequires:	libXinerama-devel
BuildRequires:	libXpm-devel
BuildRequires:	libXrender-devel
BuildRequires:	libXt-devel
BuildRequires:	libpng-devel
BuildRequires:	librsvg2-devel
BuildRequires:	libxslt
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	readline-devel
Requires:	xterm
Requires:	%{_bindir}/mimeopen
# for fvwm-bug
Requires:	%{_sbindir}/sendmail
# for fvwm-menu-headlines
Requires:	xdg-utils
# for fvwm-menu-xlock
Requires:	xlockmore
# for fvwm-menu-desktop
Requires:	python3-pyxdg

%description
Fvwm is a window manager for X11. It is designed to
minimize memory consumption, provide a 3D look to window frames,
and implement a virtual desktop.


%prep
%autosetup -p1


%build
aclocal --force
autoreconf -ivf
%configure --enable-mandoc
%make_build


%install
%make_install
%find_lang %{name}
%find_lang FvwmScript
cat FvwmScript.lang >> %{name}.lang

# xsession
install -D -m0644 -p %{SOURCE1} \
	%{buildroot}%{_datadir}/xsessions/%{name}.desktop

%files -f %{name}.lang
%license COPYING
%doc README.md NEWS
%{_bindir}/*
%{_libexecdir}/%{name}/
%{_datadir}/%{name}/
%{_mandir}/man1/*
%{_datadir}/xsessions/%{name}.desktop


%changelog
%autochangelog
