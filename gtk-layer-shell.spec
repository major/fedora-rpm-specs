%global apiver  0

Name:           gtk-layer-shell
Version:        0.7.0
Release:        2%{?dist}
Summary:        Library to create components for Wayland using the Layer Shell

License:        LGPLv3+ and MIT
URL:            https://github.com/wmww/gtk-layer-shell
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  meson >= 0.45.1

# https://github.com/wmww/gtk-layer-shell/blob/master/compatibility.md
BuildRequires:  pkgconfig(gtk+-wayland-3.0) >= 3.22.0

BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(wayland-client) >= 1.10.0
BuildRequires:  pkgconfig(wayland-protocols) >= 1.16
BuildRequires:  pkgconfig(wayland-scanner) >= 1.10.0
BuildRequires:  pkgconfig(wayland-server) >= 1.10.0


%description
A library to write GTK applications that use Layer Shell. Layer Shell is a
Wayland protocol for desktop shell components, such as panels, notifications
and wallpapers. You can use it to anchor your windows to a corner or edge of
the output, or stretch them across the entire output. This library only makes
sense on Wayland compositors that support Layer Shell, and will not work on
X11. It supports all Layer Shell features including popups and popovers
(GTK popups Just Work™). Please open issues for any bugs you come across.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for %{name}.


%prep
%autosetup


%build
%meson           \
    -Dtests=true \
    %{nil}
%meson_build


%install
%meson_install


%check
%meson_test


%files
%license LICENSE_LGPL.txt LICENSE_MIT.txt
%doc README.md CHANGELOG.md
%{_libdir}/lib%{name}.so.%{apiver}*
%{_libdir}/girepository-1.0/GtkLayerShell-%{apiver}.?.typelib

%files devel
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/*.pc
%{_libdir}/lib%{name}.so
%{_datadir}/gir-1.0/GtkLayerShell-%{apiver}.?.gir


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 26 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 0.7.0-1
- chore(update): 0.7.0
- test: Add tests

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Mar 03 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.6.0-1
- build(update): 0.6.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 20 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.5.2-1
- build(update): 0.5.2

* Mon Nov  2 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.5.1-1
- Update to 0.5.1

* Fri Oct 30 09:02:47 EET 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.5.0-2
- fix: license now LGPLv3+ and MIT
  https://github.com/wmww/gtk-layer-shell#licensing-rationale

* Thu Oct 29 07:32:33 EET 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.5.0-1
- build(update): 0.5.0

* Thu Oct 22 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.4.0-1
- build(update): 0.4.0

* Thu Aug 13 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.3.0-1
- Update to 0.3.0

* Wed Jul 29 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.2.0-1
- Update to 0.2.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep 26 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.1.0-2
- Cosmetic fixes

* Thu Sep 26 2019 gasinvein <gasinvein@gmail.com>
- Initial package
