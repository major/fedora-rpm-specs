%global commit a380201dff5bfac2dace553d7eaedb6cea6855f9
%global short_commit %(c=%{commit}; echo ${c:0:7})

Name:           dmenu-wayland
# master used because 0.1:
# 1) fails to build with the following error: multiple definition of `progname'
# 2) is from June 2019, so it's quite old
Version:        0.1^20241231.%{short_commit}
Release:        %autorelease
Summary:        An efficient dynamic menu for wayland (wlroots)
License:        MIT
URL:            https://github.com/nyyManni/dmenu-wayland
Source:         %{url}/archive/%{commit}/%{name}-%{short_commit}.tar.gz

BuildRequires:  gcc
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  meson

%description
%{summary}

%prep
%autosetup -n %{name}-%{commit}

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license LICENSE
%doc README.md
%{_bindir}/dmenu-wl
%{_bindir}/dmenu-wl_path
%{_bindir}/dmenu-wl_run
%{_mandir}/man1/dmenu-wl.1*

%changelog
%autochangelog
