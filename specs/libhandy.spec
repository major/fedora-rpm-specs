%bcond glade %[!(0%{?rhel} >= 10)]

Name:           libhandy
Version:        1.8.3
Release:        4%{?dist}
Summary:        Building blocks for modern adaptive GNOME apps
License:        LGPL-2.1-or-later

URL:            https://gitlab.gnome.org/GNOME/libhandy
%global majmin %(echo %{version} | cut -d . -f -2)
Source0:        https://download.gnome.org/sources/%{name}/%{majmin}/%{name}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  gi-docgen
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  pkgconfig(gio-2.0)
%if %{with glade}
BuildRequires:  pkgconfig(gladeui-2.0)
%endif
BuildRequires:  pkgconfig(glib-2.0) >= 2.44
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.24.1
# Support graphical tests in non-graphical environment
BuildRequires:  xwayland-run
BuildRequires:  mesa-dri-drivers
BuildRequires:  mutter
BuildRequires:  rsvg-pixbuf-loader

# Retired in F34
Obsoletes:      libhandy1 < 1.1.90-2
Conflicts:      libhandy1 < 1.1.90-2
Provides:       libhandy1 = %{version}-%{release}
Provides:       libhandy1%{?_isa} = %{version}-%{release}

%description
libhandy provides GTK+ widgets and GObjects to ease developing
applications for mobile phones.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
# Retired in F34
Obsoletes:      libhandy1-devel < 1.1.90-2
Conflicts:      libhandy1-devel < 1.1.90-2
Provides:       libhandy1-devel = %{version}-%{release}
Provides:       libhandy1-devel%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1


%build
%meson -Dgtk_doc=true -Dexamples=false \
%if %{without glade}
    -Dglade_catalog=disabled \
%endif
    %{nil}
%meson_build


%install
%meson_install

%find_lang libhandy


%check
export NO_AT_BRIDGE=1
%{shrink:xwfb-run -c mutter -- %meson_test}


%files -f libhandy.lang
%license COPYING
%doc AUTHORS HACKING.md NEWS README.md
%{_libdir}/girepository-1.0/
%{_libdir}/libhandy-1.so.0

%files devel
%{_includedir}/libhandy-1/
%{_libdir}/libhandy-1.so
%{_libdir}/pkgconfig/libhandy-1.pc
%{_datadir}/gir-1.0/
%if %{with glade}
%{_libdir}/glade/
%{_datadir}/glade/
%endif
%doc %{_datadir}/doc/libhandy-1/
%{_datadir}/vala/


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Jul 23 2024 Niels De Graef <ndegraef@redhat.com> - 1.8.3-3
- Move away from xvfb-run

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Feb 09 2024 Kalev Lember <klember@redhat.com> - 1.8.3-1
- Update to 1.8.3
- Re-enable tests on s390x

* Wed Feb 07 2024 Kalev Lember <klember@redhat.com> - 1.8.2-8
- Migrate to SPDX license

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Dec 10 2023 Kalev Lember <klember@redhat.com> - 1.8.2-5
- Backport an upstream patch to fix a write after free issue (rhbz#2253814)

* Tue Oct 31 2023 Yaakov Selkowitz <yselkowi@redhat.com> - 1.8.2-4
- Disable glade catalog in RHEL builds

* Tue Oct 24 2023 Yanko Kaneti <yaneti@declera.com> - 1.8.2-3
- BR: rsvg-pixbuf-loader for svg support in tests

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Mar 04 2023 David King <amigadave@amigadave.com> - 1.8.2-1
- Update to 1.8.2

* Wed Feb 01 2023 David King <amigadave@amigadave.com> - 1.8.1-1
- Update to 1.8.1 (#2166285)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Sep 16 2022 Kalev Lember <klember@redhat.com> - 1.8.0-1
- Update to 1.8.0

* Mon Aug 08 2022 Kalev Lember <klember@redhat.com> - 1.7.90-1
- Update to 1.7.90

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 12 2022 Kalev Lember <klember@redhat.com> - 1.7.0-1
- Update to 1.7.0

* Sun Apr 24 2022 David King <amigadave@amigadave.com> - 1.6.2-1
- Update to 1.6.2 (#2022621)

* Fri Mar 18 2022 David King <amigadave@amigadave.com> - 1.6.1-1
- Update to 1.6.1

* Fri Mar 18 2022 David King <amigadave@amigadave.com> - 1.6.0-1
- Update to 1.6.0

* Tue Mar 08 2022 David King <amigadave@amigadave.com> - 1.5.91-1
- Update to 1.5.91

* Sun Feb 13 2022 David King <amigadave@amigadave.com> - 1.5.90-1
- Update to 1.5.90

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Dec 11 2021 Kalev Lember <klember@redhat.com> - 1.5.0-2
- Backport an upstream patch to fix swipe-tracker criticals

* Sat Nov 13 2021 Kalev Lember <klember@redhat.com> - 1.5.0-1
- Update to 1.5.0

* Wed Sep 08 2021 Kalev Lember <klember@redhat.com> - 1.4.0-1
- Update to 1.4.0

* Mon Aug 16 2021 Kalev Lember <klember@redhat.com> - 1.3.90-1
- Update to 1.3.90

* Fri Jul 30 2021 Yanko Kaneti <yaneti@declera.com> - 1.2.3-3
- Delay xvfb-run test run in an attempt to fix FTBFS

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 21 2021 Kalev Lember <klember@redhat.com> - 1.2.3-1
- Update to 1.2.3

* Tue Apr 27 2021 Kalev Lember <klember@redhat.com> - 1.2.2-1
- Update to 1.2.2

* Mon Apr 19 2021 Michael Catanzaro <mcatanzaro@redhat.com> - 1.2.1-2
- Add patch to fix Geary crashes

* Tue Apr 13 2021 Kalev Lember <klember@redhat.com> - 1.2.1-1
- Update to 1.2.1

* Fri Mar 19 2021 Kalev Lember <klember@redhat.com> - 1.2.0-2
- Add conflicts with libhandy1 packages to help with the upgrade path

* Mon Mar 15 2021 Kalev Lember <klember@redhat.com> - 1.2.0-1
- Update to 1.2.0

* Wed Mar 03 2021 Kalev Lember <klember@redhat.com> - 1.1.90-2
- Update to 1.1.90 and libhandy 1 ABI, based on earlier libhandy1 packaging
- Obsolete separate libhandy1 and libhandy1-devel packages

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Sep 13 2020 Kalev Lember <klember@redhat.com> - 0.0.13-6
- Disable glade catalog for F33+

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 22 2020 Kalev Lember <klember@redhat.com> - 0.0.13-3
- Rebuilt for libgladeui soname bump

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 20 2020 Kalev Lember <klember@redhat.com> - 0.0.13-1
- Update to 0.0.13

* Mon Sep 09 2019 Kalev Lember <klember@redhat.com> - 0.0.11-1
- Update to 0.0.11

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 22 2019 Michael Catanzaro <mcatanzaro@gnome.org> - 0.0.10-2
- Add patch to fix installation of glade resources for flatpak builds

* Thu Jun 13 2019 Yanko Kaneti <yaneti@declera.com> - 0.0.10-1
- Update to 0.0.10

* Thu Mar 07 2019 Kalev Lember <klember@redhat.com> - 0.0.9-1
- Update to 0.0.9

* Fri Mar 1 2019 Yanko Kaneti <yaneti@declera.com> - 0.0.8-2
- Pull an upstream fix to prevent broken translations in
  libhandy using apps

* Sat Feb 16 2019 Kalev Lember <klember@redhat.com> - 0.0.8-1
- Update to 0.0.8

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 24 2019 Kalev Lember <klember@redhat.com> - 0.0.7-1
- Update to 0.0.7

* Fri Jan 11 2019 Yanko Kaneti <yaneti@declera.com> - 0.0.6-2
- Swap some runtime vs devel bits

* Wed Jan 09 2019 Kalev Lember <klember@redhat.com> - 0.0.6-1
- Initial Fedora packaging
