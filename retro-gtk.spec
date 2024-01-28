%global libver 1
%global pkgver 1-0

Name:       retro-gtk
Version:    1.0.2
Release:    9%{?dist}
Summary:    The GTK+ Libretro frontend framework

License:    GPLv3+
URL:        https://gitlab.gnome.org/GNOME/retro-gtk
Source0:    %{url}/-/archive/%{version}/%{name}-%{version}.tar.gz

# meson: remove unknown arguments that cause fail to build
# https://gitlab.gnome.org/GNOME/retro-gtk/-/commit/8016c10e7216394bc66281f2d9be740140b6fad6
Patch0:     %{url}/-/commit/8016c10e7216394bc66281f2d9be740140b6fad6.patch#/meson-remove-unknown-arguments-that-cause-fail-to-build.patch

BuildRequires:  meson >= 0.50.0
BuildRequires:  vala

BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.50
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 0.6.7
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:  pkgconfig(libpulse-simple)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(vapigen)

%description
Libretro is a plugin format design to implement video game console emulators,
video games and similar multimedia software. Such plugins are called Libretro
cores.

retro-gtk is a framework easing the usage of Libretro cores in conjunction
with GTK+.


%package     -n libretro-gtk-%{pkgver}
Summary:        The GTK+ Libretro frontend framework

%description -n libretro-gtk-%{pkgver}
Libretro is a plugin format design to implement video game console emulators,
video games and similar multimedia software. Such plugins are called Libretro
cores.

retro-gtk is a framework easing the usage of Libretro cores in conjunction
with GTK+.

(libretro is an API specification implemented by some emulator libraries like
libretro-bsnes).


%package     -n typelib-1_0-Retro-%{pkgver}
Summary:        GObject introspection bindings for libretro-gtk

%description -n typelib-1_0-Retro-%{pkgver}
retro-gtk wraps the libretro API for use in Gtk applications.

This subpackage contains the gobject bindings for the libretro-gtk shared
library.


%package        devel
Summary:        Development files for %{name}

Requires:       libretro-gtk-%{pkgver}%{?_isa} = %{version}
Requires:       typelib-1_0-Retro-%{pkgver}%{?_isa} = %{version}

%description    devel
This subpackage contains the headers to make use of the libretro-gtk library.


%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install


%files -n libretro-gtk-%{pkgver}
%license COPYING
%doc AUTHORS NEWS README.md
%{_libdir}/libretro-gtk-%{libver}.so.0
%{_libexecdir}/retro-runner

%files -n typelib-1_0-Retro-%{pkgver}
%{_libdir}/girepository-1.0/Retro-%{libver}.typelib

%files devel
%{_bindir}/retro-demo
%{_datadir}/gir-1.0/Retro-%{libver}.gir
%{_datadir}/vala/vapi/%{name}-%{libver}*
%{_includedir}/%{name}/
%{_libdir}/libretro-gtk-%{libver}.so
%{_libdir}/pkgconfig/%{name}-%{libver}.pc


%changelog
* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Feb 10 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.2-4
- fix: FTBFS 36

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Mar 21 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.2-1
- build(update): 1.0.2

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Nov 29 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.1-1
- build(update): 1.0.1

* Sat Sep 12 16:27:55 EEST 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.0-1
- Update to 1.0.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.18.1-1
- Update to 0.18.1

* Thu Dec 12 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.18.0-3
- Add pcsx-rearmed core

* Wed Oct 09 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.18.0-2
- Add libretro cores as weak deps

* Fri Sep 13 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.18.0-1
- Update to 0.18.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 15 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.16.1-2
- Initial package
