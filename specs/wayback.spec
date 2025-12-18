%global xwlver 24.1

# Allow wayback to stand as an X11 server
%bcond xserver 0

Name:           wayback
Version:        0.3
Release:        %autorelease
Summary:        X11 compatibility layer built on wlroots and Xwayland

License:        MIT
URL:            https://gitlab.freedesktop.org/wayback/wayback
Source:         %{url}/-/archive/%{version}/%{name}-%{version}.tar.bz2

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.14
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xwayland) >= %{xwlver}
BuildRequires:  (pkgconfig(wlroots-0.19) or pkgconfig(wlroots-0.18))
BuildRequires:  pkgconfig(scdoc)

Requires:       xorg-x11-server-Xwayland%{?_isa} >= %{xwlver}

%description
%{summary}.

%files
%license LICENSE
%doc README.md
%{_bindir}/Xwayback
%{_bindir}/wayback-*
%{_libexecdir}/wayback-*
%{_mandir}/man1/*wayback*.1*

%dnl ----------------------------------------------------------------
%if %{with xserver}

%package        xserver
Summary:        %{name} shim to provide /usr/bin/X
Requires:       %{name} = %{version}-%{release}
Provides:       Xserver
Conflicts:      xorg-x11-server-Xorg

%description    xserver
This package provides the shim links for %{name} to be automatically
used as the Xserver. This ensures that %{name} is used as the system
provider of the Xserver.

%files xserver
%{_bindir}/X

%endif
%dnl ----------------------------------------------------------------


%prep
%autosetup -S git_am


%conf
%meson


%build
%meson_build


%install
%meson_install

%if %{with xserver}
# Allow Xwayback to be called as X
ln -sr %{buildroot}%{_bindir}/Xwayback %{buildroot}%{_bindir}/X
%endif


%changelog
%autochangelog
