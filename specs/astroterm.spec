Name:           astroterm
Version:        1.0.6
Release:        1%{?dist}
Summary:        A planetarium for your terminal

License:        MIT
URL:            https://github.com/da-luce/astroterm
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        http://tdc-www.harvard.edu/catalogs/ybsc5.gz

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  argtable-devel
BuildRequires:  ncurses-devel
BuildRequires:  ninja-build
BuildRequires:  /usr/bin/xxd

%description
astroterm is a terminal-based star map.
It displays the real-time positions of stars, planets,
constellations, and more, all within your terminal—no telescope required!
Configure sky views by date, time, and location with precise ASCII-rendered
visuals.

%prep
%autosetup
gunzip -dc %{SOURCE1} > data/ybsc5


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
%{_bindir}/astroterm


%changelog
* Thu Jan 23 2025 Jonathan Wright <jonathan@almalinux.org> - 1.0.6-1
- update to 1.0.6 rhbz#2341135
- enable builds for s390x

* Tue Jan 21 2025 Jonathan Wright <jonathan@almalinux.org> - 1.0.5-1
- Initial package build rhbz#2339148
