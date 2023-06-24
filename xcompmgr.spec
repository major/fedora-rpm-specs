Name:          xcompmgr
Version:       1.1.9
Release:       %autorelease
Summary:       X11 composite manager

License:       MIT
URL:           https://gitlab.freedesktop.org/xorg/app/xcompmgr
Source:        https://www.x.org/archive/individual/app/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: make
BuildRequires: xorg-x11-util-macros

BuildRequires: libX11-devel
BuildRequires: libXfixes-devel
BuildRequires: libXrender-devel
BuildRequires: libXdamage-devel
BuildRequires: libXcomposite-devel
BuildRequires: libXext-devel

%description
xcompmgr is a sample compositing manager for X servers supporting the XFIXES,
DAMAGE, and COMPOSITE extensions. It enables basic eye-candy effects

%prep
%autosetup

%build
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc README.md ChangeLog
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
