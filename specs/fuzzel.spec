Name:           fuzzel
Version:        1.11.1
Release:        %autorelease
Summary:        Application launcher for wlroots based Wayland compositors

License:        MIT
URL:            https://codeberg.org/dnkl/fuzzel
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# https://codeberg.org/dnkl/fuzzel/issues/453#issuecomment-2544508
Patch:          %{url}/pulls/437.patch

BuildRequires:  gcc
BuildRequires:  meson >= 0.58
BuildRequires:  nanosvg-devel
BuildRequires:  tllist-static

BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(fcft) >= 3.0.0
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(scdoc)
BuildRequires:  pkgconfig(tllist) >= 1.0.1
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.32
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(xkbcommon)

%description
Fuzzel is a Wayland-native application launcher and fuzzy finder, inspired by rofi and dmenu.

Features:
  * Wayland native
  * Rofi drun-like mode of operation
  * dmenu mode where newline separated entries are read from stdin
  * Emacs key bindings
  * Icons!
  * Remembers frequently launched applications


%prep
%autosetup -n %{name} -p1


%build
%meson                  \
  -Dsystem-nanosvg=enabled \
  %{nil}
%meson_build


%install
%meson_install
# Will be installed to correct location with rpm macros
rm %{buildroot}%{_docdir}/%{name}/LICENSE


%check
%meson_test


%files
%doc CHANGELOG.md README.md
%license LICENSE
%{_bindir}/%{name}
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/fish/vendor_completions.d/*.fish
%{_datadir}/zsh/site-functions/_%{name}
%{_mandir}/man1/%{name}.1*
%{_mandir}/man5/*.5*
%{_sysconfdir}/xdg/%{name}/


%changelog
%autochangelog
