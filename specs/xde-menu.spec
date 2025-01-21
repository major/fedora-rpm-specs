Name:           xde-menu
Version:        0.14
Release:        8%{?dist}
Summary:        Menu system for the X Desktop Environment

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/bbidulock/xde-menu
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  autoconf >= 2.71
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make

BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gdk-pixbuf-xlib-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gtk+-2.0) >= 2.4.0
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(libgnome-menu-3.0)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libwnck-1.0)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xau)
BuildRequires:  pkgconfig(xdmcp)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xscrnsaver)

%description
This package provides a number of "C"-language tools for working with the X
Desktop Environment. Most of these tools were previously written in perl(1) and
were part of the xde-tools package. They have now been codified in "C" for speed
and to provide access to libraries not available from perl(1).


%prep
%autosetup -p1


%build
autoreconf -vfi
%configure
%make_build


%install
%make_install
rm %{buildroot}%{_libdir}/%{name}/modules/*.la


%check
# https://github.com/bbidulock/xde-menu/issues/5
%dnl desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files
%license COPYING
%doc README.md AUTHORS ChangeLog NEWS THANKS
%{_bindir}/%{name}
%{_bindir}/%{name}-monitor
%{_bindir}/%{name}-popmenu
%{_bindir}/%{name}-quit
%{_bindir}/%{name}-refresh
%{_bindir}/%{name}-replace
%{_bindir}/%{name}-restart
%{_bindir}/xde-menugen
%{_datadir}/applications/*.desktop
%{_datadir}/X11/app-defaults
%{_libdir}/%{name}
%{_mandir}/man1/*.1*
%{_sysconfdir}/xdg/autostart/%{name}.desktop


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.14-7
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Feb 03 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 0.14-1
- chore(update): 0.14

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 11 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.12-1
- Update to 0.12

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep 05 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.11-2
- Update to 0.11

* Wed Sep 04 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.10-2
- Update to 0.10

* Fri Aug 30 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.9-1
- Initial package
