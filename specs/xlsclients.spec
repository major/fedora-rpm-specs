Summary:    X client list utility
Name:       xlsclients
Version:    1.1.6
Release:    %autorelease
License:    MIT
URL:        https://www.x.org
Source0:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz
BuildRequires:  gettext-devel
BuildRequires:  libtool
BuildRequires:  make

BuildRequires:  pkgconfig(x11)

Obsoletes: xorg-x11-utils < 7.5-39

%description
xlsclients lists the names of the clients currently connected to an X server.

%prep
%autosetup

%build
%configure
%make_build

%check
make check

%install
%make_install

%files
%license COPYING
%{_bindir}/xlsclients
%{_mandir}/man1/xlsclients.1*

%changelog
%autochangelog
