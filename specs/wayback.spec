%global commit d7baac754450ccd389b834f337c85b677ced95a5
%global commitdate 20250718
%global shortcommit %{sub %{commit} 1 7}

%global baserelease 1

%global xwlver 24.1

Name:           wayback
Version:        0~git%{commitdate}.%{baserelease}.%{shortcommit}
Release:        %autorelease
Summary:        X11 compatibility layer built on wlroots and Xwayland

License:        MIT
URL:            https://gitlab.freedesktop.org/wayback/wayback
Source:         %{url}/-/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc
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
%autosetup -n %{name}-%{commit}


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
