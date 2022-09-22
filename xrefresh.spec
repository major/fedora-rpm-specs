Name:           xrefresh
Version:        1.0.7
Release:        %autorelease
Summary:        Refresh all or part of an X screen

License:        MIT
URL:            https://www.x.org
Source0:        %{url}/pub/individual/app/%{name}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

Obsoletes:      xorg-x11-server-utils < 7.7-40

%description
xrefresh is a simple X program that causes all or part of your screen to be
repainted.

%prep
%autosetup

%build
%configure --disable-silent-rules
%make_build

%install
%make_install

%files
%license COPYING
%doc ChangeLog README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
