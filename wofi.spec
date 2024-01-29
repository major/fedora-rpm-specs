Name:		wofi
Summary:	A launcher/menu for wlroots based wayland compositors
Version:	1.3
Release:	4%{?dist}

License:	GPLv3
URL:		https://hg.sr.ht/~scoopta/wofi
Source0:	%{URL}/archive/v%{version}.tar.gz

BuildRequires:	meson
BuildRequires:	gcc
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gio-unix-2.0)
BuildRequires:	pkgconfig(wayland-client)

%description
A launcher/menu for wlroots based wayland compositors.

%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Files for development with %{name}.

%prep
%autosetup -n %{name}-v%{version}

%build
%meson
%meson_build

%install
%meson_install

%files
%license COPYING.md
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/wofi.1*
%{_mandir}/man5/wofi.5*
%{_mandir}/man7/wofi-keys.7*
%{_mandir}/man7/wofi.7*

%files devel
%{_includedir}/wofi-1/*.h
%{_libdir}/pkgconfig/wofi.pc
%{_mandir}/man3/wofi-api.3*
%{_mandir}/man3/wofi-config.3*
%{_mandir}/man3/wofi-map.3*
%{_mandir}/man3/wofi-utils.3*
%{_mandir}/man3/wofi-widget-builder.3*
%{_mandir}/man3/wofi.3*

%changelog
* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Nov 26 2022 Stefano Figura <stefano@figura.im> - 1.3-1
- Update to version 1.3

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Feb 05 2021 Stefano Figura <stefano@figura.im> - 1.2.4-1
- Update to version 1.2.4

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Nov 14 2020 Stefano Figura <stefano@figura.im> - 1.2.3-1
- Update to version 1.2.3

* Sun Aug 23 2020 Stefano Figura <stefano@figura.im> - 1.2.1-1
- Update to version 1.2.1

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Mar  9 2020 Christian Kellner <ckellner@redhat.com> - 1.1.1-1
- New upstream release 1.1.1, includes header and pkg config file

* Wed Mar  4 2020 Christian Kellner <ckellner@redhat.com> - 1.1-1
- New upstream release 1.1, which includes man pages

* Mon Jan 27 2020 Christian Kellner <ckellner@redhat.com> - 1.0-1
- Initial package of v1.0
