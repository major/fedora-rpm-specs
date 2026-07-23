Name:       xclock
Version:    1.2.1
Release:    %autorelease
Summary:    The classic X Window System clock utility

License:    MIT-open-group AND SMLNJ AND MIT
URL:        https://www.x.org
Source0:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xt)

%description
xclock is the classic X Window System clock utility. It displays
the time in analog or digital form, continuously updated at a
frequency which may be specified by the user.

%prep
%autosetup
%meson

%build
%meson_build

%install
%meson_install

%check
# No upstream test suite exists

%files
%license COPYING
%{_bindir}/xclock
%{_mandir}/man1/xclock.1*
%{_datadir}/X11/app-defaults/XClock
%{_datadir}/X11/app-defaults/XClock-ampm
%{_datadir}/X11/app-defaults/XClock-color
%{_datadir}/X11/app-defaults/XClock-grandfather

%changelog
%autochangelog
