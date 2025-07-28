%global xwlver 24.1

Name:           wayback
Version:        0.2
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

%prep
%autosetup -S git_am


%conf
%meson


%build
%meson_build


%install
%meson_install


%files
%license LICENSE
%doc README.md
%{_bindir}/Xwayback
%{_bindir}/wayback-*
%{_libexecdir}/wayback-*
%{_mandir}/man1/*wayback*.1*


%changelog
%autochangelog
