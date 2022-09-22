Name:		phoc
Version:	0.21.1
Release:	1%{?dist}
Summary:	Display compositor designed for phones

License:	GPLv3+
URL:		https://gitlab.gnome.org/World/Phosh/phoc
Source0:	https://gitlab.gnome.org/World/Phosh/phoc/-/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildRequires:	gcc
BuildRequires:	meson

BuildRequires:	pkgconfig(gio-2.0) >= 2.50.0
BuildRequires:	pkgconfig(glib-2.0) >= 2.50.0
BuildRequires:	pkgconfig(gobject-2.0) >= 2.50.0
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:	pkgconfig(libinput)
BuildRequires:	pkgconfig(pixman-1)
BuildRequires:	pkgconfig(wayland-client)
BuildRequires:	pkgconfig(wayland-protocols) >= 1.15
BuildRequires:	pkgconfig(wayland-server)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	(pkgconfig(wlroots) >= 0.15 with pkgconfig(wlroots) < 0.16)

BuildRequires:	pkgconfig(gnome-desktop-3.0)

%description
Phoc is a wlroots based Phone compositor as used on the Librem5. Phoc is
pronounced like the English word fog.


%prep
%setup -q -n %{name}-v%{version}

%build
%meson -Dembed-wlroots=disabled
%meson_build


%install
%meson_install


%files
%{_bindir}/phoc
%{_datadir}/glib-2.0/schemas/sm.puri.phoc.gschema.xml
%doc README.md
%license COPYING


%changelog
* Thu Sep 01 2022 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.21.1-1
= Update to 0.21.1

* Thu Aug 04 2022 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.21.0-1
- Update to 0.21.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0~beta1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Kalev Lember <klember@redhat.com> - 0.21.0~beta1-2
- Rebuilt for libgnome-desktop soname bump

* Sun Jun 26 2022 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.21.0~beta1-1
- Update to 0.21.0~beta1

* Fri Mar 25 2022 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.13.0-1
- Update to 0.13.0

* Tue Jan 25 2022 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.12.0-1
- Update to 0.12.0-1

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 19 2022 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.11.0-3
- Update to 0.11.0-3

* Wed Jan 19 2022 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.11.0-2
- Update to 0.11.0-2

* Wed Jan 05 2022 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.11.0-1
- Update to 0.11.0

* Wed Dec 15 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.10.0-1
- Update to 0.10.0

* Thu Oct 28 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.9.0-1
- Update to 0.9.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 10 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.8.0-1
- Update to 0.8.0

* Mon Jun 14 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.7.1-1
- Update to 0.7.1

* Wed Apr 07 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.7.0-2
- Pin wlroots dependency to 0.12 compat package

* Fri Mar 19 2021 Torrey Sorensen <torbuntu@fedpraproject.org> - 0.7.0-1
- Update to 0.7.0

* Tue Jan 05 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.6.0-1
- Update to 0.6.0

* Thu Nov 19 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.5.1-1
- Update to 0.5.1

* Sat Nov 14 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.5.0-1
- Update to 0.5.0

* Tue Oct 27 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.4.4-1
- Update to 0.4.4

* Thu Oct 08 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.4.3-1
- Update to 0.4.3

* Thu Aug 06 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.4.2-1
- Update to 0.4.2

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 24 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.4.1-2
- Rebuild for new wlroots

* Wed Jul 22 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.4.1-1
- Update to 0.4.1

* Tue Jun 23 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.4.0-1
- Update to 0.4.0, note: update version is to align with phosh, thus the jump to 0.4.0

* Tue Jun 23 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.1.9-1
- Update to 0.1.9

* Thu Jun 11 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.1.8-1
- Update to 0.1.8

* Thu Mar 26 2020 Nikhil Jha <hi@nikhiljha.com> - 0.1.7-1
- Update to 0.1.7 with upstreamed patches

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 09 2019 Lubomir Rintel <lkundrak@v3.sk> - 0.1.0-2
- Fix build with newer wlroots

* Tue Oct 01 2019 Lubomir Rintel <lkundrak@v3.sk> - 0.1.0-1
- Initial packaging
