Name:       wapanel
Version:    1.1.0
Release:    6%{?dist}
Summary:    Desktop-dedicated wayland bar for wayfire and other wlroots based compositors

License:    MIT
URL:        https://github.com/Firstbober/wapanel
Source0:    %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: meson
BuildRequires: toml11-devel

BuildRequires: pkgconfig(gtk-layer-shell-0) >= 0.6
BuildRequires: pkgconfig(gtk+-3.0) >= 3.22.30
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-protocols) >= 1.12
BuildRequires: pkgconfig(wayland-server)

# ------------------------------------------------------------------
# Based on upstream defaults. See:
# https://github.com/Firstbober/wapanel/blob/master/wapanel.toml#L14
Recommends: swaylock

Suggests: thunar
Suggests: xfce4-settings
# ------------------------------------------------------------------

# For futute builds and upstream updates
%dnl Requires:  hicolor-icon-theme

%global _description %{expand:
Simple panel/status bar/task bar for your custom stacking Wayland-based
desktop. Documentation: https://firstbober.github.io/wapanel

Features

  * Good configurability
  * Config hot reload
  * Exposed API for writing custom applets
  * Custom themes with CSS}

%description %{_description}


%package    devel
Summary:    Development files for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel %{_description}

Development files for %{name}.


%prep
%autosetup -p1


%build
%meson                   \
    -Dsystem_toml11=true \
    %{nil}
%meson_build


%install
%meson_install
rm %{buildroot}%{_datadir}/%{name}/3RD_PARTY_LICENSES
rm %{buildroot}%{_libdir}/lib%{name}-appletapi.a


%files
%license LICENSE 3RD_PARTY_LICENSES
%doc README.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_libdir}/%{name}/

%files devel
%{_includedir}/%{name}-appletapi
%{_libdir}/pkgconfig/*.pc


%changelog
* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jan 06 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 1.1.0-1
- chore(update): 1.1.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Apr 23 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.2-1
- build(update): 1.0.2

* Thu Apr 22 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.1-1
- build(update): 1.0.1

* Wed Apr 21 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0-1
- Initial package
