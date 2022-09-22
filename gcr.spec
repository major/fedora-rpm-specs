%ifarch %{valgrind_arches}
%global has_valgrind 1
%endif

Name:           gcr
Version:        3.90.0
Release:        2%{?dist}
Summary:        A library for bits of crypto UI and parsing

License:        LGPLv2+
URL:            https://wiki.gnome.org/Projects/CryptoGlue
Source0:        https://download.gnome.org/sources/%{name}/3.90/%{name}-%{version}.tar.xz

BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  pkgconfig(gi-docgen)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(p11-kit-1)
BuildRequires:  libgcrypt-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  vala
%if 0%{?has_valgrind}
BuildRequires:  valgrind-devel
%endif
BuildRequires:  /usr/bin/gpg2
BuildRequires:  /usr/bin/ssh-add
BuildRequires:  /usr/bin/ssh-agent
BuildRequires:  /usr/bin/xsltproc

Requires: %{name}-base%{?_isa} = %{version}-%{release}
Requires: /usr/bin/ssh-add
Requires: /usr/bin/ssh-agent

%description
gcr is a library for displaying certificates, and crypto UI, accessing
key stores. It also provides a viewer for crypto files on the GNOME
desktop.

gck is a library for accessing PKCS#11 modules like smart cards.

%package base
Summary: Common library files for %{name}
Conflicts: %{name} < 3.28.1-3

%description base
The %{name}-base package includes the %{name} common library files used by both gtk3 and gtk4 versions.

%package gtk3
Summary: Library files for %{name} using gtk3
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-base%{?_isa} = %{version}-%{release}

%description gtk3
The %{name}-gtk3 package includes the library files for the %{name} package using gtk3.

%package gtk4
Summary: Library files for %{name} using gtk4
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-base%{?_isa} = %{version}-%{release}

%description gtk4
The %{name}-gtk4 package includes the library files for the %{name} package using gtk4.

%package devel
Summary: Common development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package includes the common header files for the %{name} library.

%package gtk3-devel
Summary: Development files for %{name} using gtk3
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-gtk3%{?_isa} = %{version}-%{release}
Requires: %{name}-devel%{?_isa} = %{version}-%{release}

%description gtk3-devel
The %{name}-gtk3-devel package includes the header files for the %{name} library using gtk3.

%package gtk4-devel
Summary: Development files for %{name} using gtk4
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-gtk4%{?_isa} = %{version}-%{release}
Requires: %{name}-devel%{?_isa} = %{version}-%{release}

%description gtk4-devel
The %{name}-gtk4-devel package includes the header files for the %{name} library using gtk4.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name}-4

%post
%systemd_user_post gcr-ssh-agent.service

%preun
%systemd_user_preun gcr-ssh-agent.service

%postun
%systemd_user_postun_with_restart gcr-ssh-agent.service


%files -f %{name}-4.lang
%doc NEWS README.md
%license COPYING
%{_libdir}/girepository-1.0
%{_libexecdir}/gcr-ssh-agent
%{_libexecdir}/gcr4-ssh-askpass
%{_userunitdir}/gcr-ssh-agent.service
%{_userunitdir}/gcr-ssh-agent.socket

%files base
%{_libdir}/libgck-2.so.1.90.0
%{_libdir}/libgck-2.so.0.0.0
%{_libdir}/libgcr-4.so.3.90.0
%{_libdir}/libgcr-4.so.0.0.0

%files gtk3
%{_libdir}/libgcr-4-gtk3.so.0.0.0
%{_libdir}/libgcr-4-gtk3.so.3.90.0

%files gtk4
%{_libdir}/libgcr-4-gtk4.so.0.0.0
%{_libdir}/libgcr-4-gtk4.so.3.90.0

%files devel
%{_includedir}/gck-2
%{_includedir}/gcr-4/gcr
%{_libdir}/libgck-2.so
%{_libdir}/libgcr-4.so
%{_libdir}/pkgconfig/gck-2.pc
%{_libdir}/pkgconfig/gcr-4.pc
%{_datadir}/gir-1.0/Gck-2.gir
%{_datadir}/gir-1.0/Gcr-4.gir
%dir %{_datadir}/doc
%{_datadir}/doc/gck-2
%{_datadir}/doc/gcr-4
%{_datadir}/vala/vapi/gck-2.deps
%{_datadir}/vala/vapi/gck-2.vapi
%{_datadir}/vala/vapi/gcr-4.deps
%{_datadir}/vala/vapi/gcr-4.vapi

%files gtk3-devel
%{_bindir}/gcr-viewer-gtk3
%{_datadir}/doc/gcr-4-gtk3
%{_datadir}/gir-1.0/GcrGtk3-4.gir
%{_datadir}/vala/vapi/gcr-4-gtk3.deps
%{_datadir}/vala/vapi/gcr-4-gtk3.vapi
%{_includedir}/gcr-4/gcr-gtk3
%{_libdir}/libgcr-4-gtk3.so
%{_libdir}/pkgconfig/gcr-4-gtk3.pc

%files gtk4-devel
%{_bindir}/gcr-viewer-gtk4
%{_datadir}/doc/gcr-4-gtk4
%{_datadir}/gir-1.0/GcrGtk4-4.gir
%{_datadir}/vala/vapi/gcr-4-gtk4.deps
%{_datadir}/vala/vapi/gcr-4-gtk4.vapi
%{_includedir}/gcr-4/gcr-gtk4
%{_libdir}/libgcr-4-gtk4.so
%{_libdir}/pkgconfig/gcr-4-gtk4.pc

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.90.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Milan Crha <mcrha@redhat.com> - 3.90.0-1
- Update to 3.90.0
- Split subpackages for gtk3 and gtk4

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.41.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Sep 30 2021 Kalev Lember <klember@redhat.com> - 3.41.0-1
- Update to 3.41.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.40.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Mar 27 2021 Kalev Lember <klember@redhat.com> - 3.40.0-1
- Update to 3.40.0
- Tighten soname globs

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.38.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 16 2021 Kalev Lember <klember@redhat.com> - 3.38.1-1
- Update to 3.38.1

* Mon Sep 28 2020 Kalev Lember <klember@redhat.com> - 3.38.0-2
- Avoid BuildRequiring vala twice

* Mon Sep 28 2020 Kalev Lember <klember@redhat.com> - 3.38.0-1
- Update to 3.38.0

* Sun Sep 20 2020 Kalev Lember <klember@redhat.com> - 3.37.91-1
- Update to 3.37.91

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.36.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Mar 11 2020 Kalev Lember <klember@redhat.com> - 3.36.0-1
- Update to 3.36.0

* Tue Feb 18 2020 Kalev Lember <klember@redhat.com> - 3.35.91-1
- Update to 3.35.91

* Mon Feb 03 2020 Kalev Lember <klember@redhat.com> - 3.35.90-1
- Update to 3.35.90

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.35.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 20 2020 Kalev Lember <klember@redhat.com> - 3.35.1-1
- Update to 3.35.1
- Switch to the meson build system

* Mon Oct 14 2019 Kalev Lember <klember@redhat.com> - 3.34.0-1
- Update to 3.34.0

* Mon Aug 19 2019 Kalev Lember <klember@redhat.com> - 3.33.4-1
- Update to 3.33.4

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.28.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 02 2019 Dan Horák <dan[at]danny.cz> - 3.28.1-4
- fix gcr-prompter crash (rhbz#1631759)

* Thu Apr 11 2019 Fabiano Fidêncio <fidencio@redhat.com> - 3.28.1-3
- Split gcr-base into a new package

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.28.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Kalev Lember <klember@redhat.com> - 3.28.1-1
- Update to 3.28.1

* Fri Jan 04 2019 Kalev Lember <klember@redhat.com> - 3.28.0-3
- Backport a patch to fix gnome-shell crashes with glib 2.59
- Use make_build and make_install macros

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.28.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 12 2018 Kalev Lember <klember@redhat.com> - 3.28.0-1
- Update to 3.28.0

* Mon Mar 05 2018 Kalev Lember <klember@redhat.com> - 3.27.92-1
- Update to 3.27.92
- Use valgrind_arches macro instead of hardcoding valgrind arch list
- Drop group tags
- Drop ldconfig scriptlets
- Move desktop file validation to check section
- Drop ancient conflicts

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.20.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.20.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.20.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.20.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 25 2017 Kalev Lember <klember@redhat.com> - 3.20.0-3
- Build with gpg2 support to match seahorse (#1005916)

* Thu Sep 22 2016 Kalev Lember <klember@redhat.com> - 3.20.0-2
- BR vala instead of obsolete vala-tools subpackage

* Fri Mar 25 2016 Kalev Lember <klember@redhat.com> - 3.20.0-1
- Update to 3.20.0

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 20 2016 Kalev Lember <klember@redhat.com> - 3.19.4-1
- Update to 3.19.4

* Mon Sep 28 2015 Kalev Lember <klember@redhat.com> - 3.18.0-1
- Update to 3.18.0

* Tue Sep 15 2015 Kalev Lember <klember@redhat.com> - 3.17.4-1
- Update to 3.17.4

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 12 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.0-1
- Update to 3.16.0

* Tue Mar 17 2015 Kalev Lember <kalevlember@gmail.com> - 3.15.92-1
- Update to 3.15.92

* Fri Feb 27 2015 David King <amigadave@amigadave.com> - 3.15.90-1
- Update to 3.15.90
- Update URL
- Add more documentation and use license macro for COPYING
- Use pkgconfig for BuildRequires
- Preserve timestamps during install

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 3.14.0-3
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Mon Sep 29 2014 Dan Horák <dan[at]danny.cz> - 3.14.0-2
- valgrind available only on selected arches

* Tue Sep 23 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.0-1
- Update to 3.14.0

* Sat Sep 20 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.91-4
- Update mime scriptlets

* Sun Sep 14 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.91-2
- Use system valgrind headers (#1141470)

* Thu Sep 11 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.91-1
- Update to 3.13.91

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.12.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 3.12.2-3
- Rebuilt for gobject-introspection 1.41.4

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 15 2014 Kalev Lember <kalevlember@gmail.com> - 3.12.2-1
- Update to 3.12.2

* Sat Apr 05 2014 Kalev Lember <kalevlember@gmail.com> - 3.12.0-2
- Tighten -devel deps

* Sun Mar 23 2014 Kalev Lember <kalevlember@gmail.com> - 3.12.0-1
- Update to 3.12.0

* Sat Mar 08 2014 Richard Hughes <rhughes@redhat.com> - 3.11.91-1
- Update to 3.11.91

* Mon Oct 28 2013 Richard Hughes <rhughes@redhat.com> - 3.10.1-1
- Update to 3.10.1

* Wed Sep 25 2013 Kalev Lember <kalevlember@gmail.com> - 3.10.0-1
- Update to 3.10.0

* Tue Sep  3 2013 Matthias Clasen <mclasen@redhat.com> - 3.9.91-1
- Update to 3.9.91

* Wed Aug 28 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.90-1
- Update to 3.9.90

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 10 2013 Adam Williamson <awilliam@redhat.com> - 3.9.1-2
- use current guidelines for mimeinfo, desktop-database, gsettings
  schema and icon cache scriptlets

* Sat May 04 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.1-1
- Update to 3.9.1

* Tue Apr 16 2013 Richard Hughes <rhughes@redhat.com> - 3.8.1-1
- Update to 3.8.1

* Tue Mar 26 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.0-1
- Update to 3.8.0

* Mon Mar 18 2013 Richard Hughes <rhughes@redhat.com> - 3.7.92-1
- Update to 3.7.92

* Thu Mar  7 2013 Matthias Clasen <mclasen@redhat.com> - 3.7.91-1
- Update to 3.7.91

* Wed Feb 06 2013 Kalev Lember <kalevlember@gmail.com> - 3.7.5-1
- Update to 3.7.5

* Mon Jan 14 2013 Tomas Bzatek <tbzatek@redhat.com> - 3.7.2-2
- Fix crash on parsing some certificates (#894157)

* Wed Jan 09 2013 Richard Hughes <hughsient@gmail.com> - 3.7.2-1
- Update to 3.7.2

* Fri Nov 09 2012 Kalev Lember <kalevlember@gmail.com> - 3.7.1-1
- Update to 3.7.1

* Tue Oct 16 2012 Kalev Lember <kalevlember@gmail.com> - 3.6.1-1
- Update to 3.6.1

* Tue Sep 25 2012 Kalev Lember <kalevlember@gmail.com> - 3.6.0-1
- Update to 3.6.0

* Wed Sep 19 2012 Richard Hughes <hughsient@gmail.com> - 3.5.92-1
- Update to 3.5.92

* Tue Aug 21 2012 Richard Hughes <hughsient@gmail.com> - 3.5.90-1
- Update to 3.5.90

* Tue Aug 07 2012 Richard Hughes <hughsient@gmail.com> - 3.5.5-1
- Update to 3.5.5

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 17 2012 Richard Hughes <hughsient@gmail.com> - 3.5.4-1
- Update to 3.5.4

* Mon Jun 25 2012 Richard Hughes <hughsient@gmail.com> - 3.5.3-1
- Update to 3.5.3

* Tue Apr 24 2012 Kalev Lember <kalevlember@gmail.com> - 3.4.1-2
- Silence glib-compile-schemas output

* Mon Apr 16 2012 Richard Hughes <hughsient@gmail.com> - 3.4.1-1
- Update to 3.4.1

* Mon Mar 26 2012 Debarshi Ray <rishi@fedoraproject.org> - 3.4.0-1
- Update to 3.4.0

* Wed Mar 21 2012 Matthias Clasen <mclasen@redhat.com> - 3.3.92-2
- Enable introspection, needed for gnome-shell now

* Wed Mar 21 2012 Kalev Lember <kalevlember@gmail.com> - 3.3.92-1
- Update to 3.3.92

* Fri Mar 09 2012 Rex Dieter <rdieter@fedoraproject.org> 3.3.90-2
- suppress scriptlet output

* Mon Mar  5 2012 Matthias Clasen <mclasen@redhat.com> - 3.3.90-1
- Update to 3.3.90

* Mon Feb 13 2012 Matthias Clasen <mclasen@redhat.com> - 3.3.5-1
- Update to 3.3.5

* Tue Jan 17 2012 Matthias Clasen <mclasen@redhat.com> - 3.3.4-1
- Update to 3.3.4

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jan  3 2012 Tomas Bzatek <tbzatek@redhat.com> 3.3.3.1-4
- Add a Conflicts directive for older gnome-keyring packages (#771299)

* Wed Dec 21 2011 Matthias Clasen <mclasen@redhat.com> 3.3.3.1-3
- Own some directories

* Wed Dec 21 2011 Matthias Clasen <mclasen@redhat.com> 3.3.3.1-2
- Delete rpaths

* Wed Dec 21 2011 Matthias Clasen <mclasen@redhat.com> 3.3.3.1-1
- Update to 3.3.3.1

* Fri Dec 16 2011 Matthias Clasen <mclasen@redhat.com> 3.3.2.1-1
- Update to 3.3.2.1

* Thu Nov 10 2011 Matthias Clasen <mclasen@redhat.com> 3.3.1-1
- Initial packaging

