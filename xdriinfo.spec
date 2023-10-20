Name: xdriinfo
Version: 1.0.4
Release: %autorelease
Summary: X application to query configuration information of DRI drivers
License: MIT
URL: https://gitlab.freedesktop.org/xorg/app/xdriinfo
Source: https://www.x.org/pub/individual/app/%{name}-%{version}.tar.bz2

# This package was split from the mesa-demos Fedora package, which used to
# also build and install xdriinfo in its glx-utils until mesa-demos-9.0.0-3
Conflicts: glx-utils < 9.0.0-4

# This patch was kept from the previous mesa-demos state for xdriinfo for this
# version and should be unnecessary in future versions of xdriinfo:
# https://gitlab.freedesktop.org/xorg/app/xdriinfo/-/commit/6273d9dacbf165331c21bcda5a8945c8931d87b8
Patch0: xdriinfo-1.0.4-glvnd.patch

BuildRequires: gcc
BuildRequires: libglvnd-devel
BuildRequires: xorg-x11-util-macros
BuildRequires: make autoconf automake libtool

%description
xdriinfo can be used to query configuration information of direct
rendering drivers.

%prep
%autosetup

%build
%configure
%make_build

%install
%make_install

%files
%license COPYING
%{_bindir}/xdriinfo
%{_mandir}/man1/xdriinfo.1*
%doc AUTHORS ChangeLog README

%changelog
%autochangelog
