Name:           fuzzel
Version:        1.14.0
Release:        %autorelease
Summary:        App launcher and fuzzy finder for Wayland, inspired by rofi

License:        MIT
URL:            https://codeberg.org/dnkl/fuzzel
Source0:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.gz.sig
# Daniel Eklöf (Git signing) <daniel@ekloef.se>
Source2:        gpgkey-5BBD4992C116573F.asc

BuildRequires:  gcc
BuildRequires:  meson >= 0.58
BuildRequires:  nanosvg-devel
BuildRequires:  tllist-static
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(fcft) >= 3.3.1
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(pixman-1) >= 0.46.0
BuildRequires:  pkgconfig(scdoc)
BuildRequires:  pkgconfig(tllist) >= 1.0.1
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.41
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(xkbcommon)

%description
Fuzzel is a Wayland-native application launcher and fuzzy finder, inspired by
rofi and dmenu.


%prep
%autosetup -p1


%build
%meson \
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
