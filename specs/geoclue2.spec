Name:           geoclue2
Version:        2.7.2
Release:        3%{?dist}
Summary:        Geolocation service

License:        GPL-2.0-or-later
URL:            http://www.freedesktop.org/wiki/Software/GeoClue/
Source0:        https://gitlab.freedesktop.org/geoclue/geoclue/-/archive/%{version}/geoclue-%{version}.tar.bz2
Source1:        geoclue2.sysusers

# Backport from upstream
## Generated with: git format-patch -N --stdout 2.7.2...master > geoclue-2.7.2-git41-backports.patch
Patch0:         geoclue-2.7.2-git41-backports.patch

BuildRequires:  avahi-glib-devel
BuildRequires:  gettext
BuildRequires:  git-core
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  json-glib-devel
BuildRequires:  libsoup3-devel
BuildRequires:  meson
BuildRequires:  ModemManager-glib-devel
BuildRequires:  systemd, systemd-rpm-macros
BuildRequires:  vala
Requires:       dbus
%{?sysusers_requires_compat}

Obsoletes:      geoclue2-server < 2.1.8

Obsoletes:      geoclue < 0.12.99-10
Obsoletes:      geoclue-devel < 0.12.99-10
Obsoletes:      geoclue-gsmloc < 0.12.99-10
Obsoletes:      geoclue-gui < 0.12.99-10
Obsoletes:      geoclue-gypsy < 0.12.99-10

%description
Geoclue is a D-Bus service that provides location information. The primary goal
of the Geoclue project is to make creating location-aware applications as
simple as possible, while the secondary goal is to ensure that no application
can access location information without explicit permission from user.


%package        libs
Summary:        Geoclue client library
License:        LGPL-2.0-or-later AND LGPL-2.1-or-later
Recommends:     %{name} = %{version}-%{release}

%description    libs
The %{name}-libs package contains a convenience library to interact with
Geoclue service.


%package        devel
Summary:        Development files for %{name}
# /docs/*xml is GFDL-1.1-or-later
License:        GPL-2.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND GFDL-1.1-or-later
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains files for developing applications that
use %{name}.


%package        demos
Summary:        Demo applications for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Recommends:     %{name} = %{version}-%{release}
BuildRequires:  libnotify-devel

%description    demos
The %{name}-demos package contains demo applications that use %{name}.


%prep
%autosetup -n geoclue-%{version} -S git_am


%conf
%meson \
       -Ddbus-srv-user=geoclue \
       -Ddefault-wifi-url="https://api.beacondb.net/v1/geolocate" \
       -Ddefault-wifi-submit-url="https://api.beacondb.net/v2/geosubmit" \
       %{nil}


%build
%meson_build


%install
%meson_install
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/geoclue2.conf

# Home directory for the 'geoclue' user
mkdir -p $RPM_BUILD_ROOT/var/lib/geoclue


%pre
%sysusers_create_compat %{SOURCE1}
exit 0

%post
%systemd_post geoclue.service

%preun
%systemd_preun geoclue.service

%postun
%systemd_postun_with_restart geoclue.service


%files
%license COPYING
%doc NEWS
%config %{_sysconfdir}/geoclue/
%dir %{_libexecdir}/geoclue-2.0
%dir %{_libexecdir}/geoclue-2.0/demos
%{_sysconfdir}/xdg/autostart/geoclue-demo-agent.desktop
%{_libexecdir}/geoclue
%{_datadir}/dbus-1/system.d/org.freedesktop.GeoClue2.conf
%{_datadir}/dbus-1/system.d/org.freedesktop.GeoClue2.Agent.conf
%{_datadir}/dbus-1/system-services/org.freedesktop.GeoClue2.service
%{_datadir}/polkit-1/rules.d/org.freedesktop.GeoClue2.rules
%{_datadir}/applications/geoclue-demo-agent.desktop
%{_mandir}/man5/geoclue.5*
%{_unitdir}/geoclue.service
%{_libexecdir}/geoclue-2.0/demos/agent
%{_sysusersdir}/geoclue2.conf
%attr(755,geoclue,geoclue) %dir /var/lib/geoclue

%files libs
%license COPYING.LIB
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/Geoclue-2.0.typelib
%{_libdir}/libgeoclue-2.so.0*

%files devel
%{_datadir}/dbus-1/interfaces/org.freedesktop.GeoClue2*.xml
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Geoclue-2.0.gir
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/geoclue/
%{_datadir}/gtk-doc/html/libgeoclue/
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/libgeoclue-2.0.*
%{_includedir}/libgeoclue-2.0/
%{_libdir}/pkgconfig/geoclue-2.0.pc
%{_libdir}/pkgconfig/libgeoclue-2.0.pc
%{_libdir}/libgeoclue-2.so

%files demos
%{_libexecdir}/geoclue-2.0/demos/where-am-i
%{_datadir}/applications/geoclue-where-am-i.desktop


%changelog
* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Wed Feb 12 2025 Neal Gompa <ngompa@fedoraproject.org> - 2.7.2-2
- Add BeaconDB geosubmit URL

* Wed Feb 12 2025 Neal Gompa <ngompa@fedoraproject.org> - 2.7.2-1
- Update to 2.7.2
- Backport fixes from upstream to use BeaconDB
- Use BeaconDB for the default location services source

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Oct 02 2023 Daan De Meyer <daan.j.demeyer@gmail.com> - 2.7.0-3
- Provide a sysusers.d file to get user() and group() provides
  (see https://fedoraproject.org/wiki/Changes/Adopting_sysusers.d_format).

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 29 2023 Kalev Lember <klember@redhat.com> - 2.7.0-1
- Update to 2.7.0
- Switch to libsoup 3

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 30 2022 Kalev Lember <klember@redhat.com> - 2.6.0-4
- Tighten dependencies between -libs and -demos subpackages

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Feb 16 2022 David King <amigadave@amigadave.com> - 2.6.0-2
- Do not own polkit rules.d dir

* Wed Feb 16 2022 Bilal Elmoussaoui <belmouss@redhat.com> - 2.6.0-1
- Bump to 2.6.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Oct 07 2021 Kalev Lember <klember@redhat.com> - 2.5.7-6
- Backport upstream patch to fix IP-based geolocation (#1991075)

* Fri Oct 01 2021 Kalev Lember <klember@redhat.com> - 2.5.7-5
- Avoid requiring systemd for systemd rpm scriptlets
- Recommend the daemon package instead of hard requiring

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.5.7-3
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 04 2021 Michael Catanzaro <mcatanzaro@redhat.com> - 2.5.7-1
- Update to 2.5.7

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 24 2020 Michael Catanzaro <mcatanzaro@redhat.com> - 2.5.6-2
- Add patch to fix location privacy setting

* Wed Feb 26 2020 Kalev Lember <klember@redhat.com> - 2.5.6-1
- Update to 2.5.6

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 30 2019 Kalev Lember <klember@redhat.com> - 2.5.5-1
- Update to 2.5.5

* Fri Sep 27 2019 Kalev Lember <klember@redhat.com> - 2.5.4-1
- Update to 2.5.4

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 16 2019 Kalev Lember <klember@redhat.com> - 2.5.3-1
- Update to 2.5.3

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 11 2019 Kalev Lember <klember@redhat.com> - 2.5.2-1
- Update to 2.5.2

* Tue Oct 16 2018 Kalev Lember <klember@redhat.com> - 2.5.1-1
- Update to 2.5.1

* Sun Oct 14 2018 Kalev Lember <klember@redhat.com> - 2.5.0-1
- Update to 2.5.0
- Switch to the meson build system
- Build gtk-doc documentation
- Remove ldconfig scriptlets

* Thu Jul 26 2018 Kalev Lember <klember@redhat.com> - 2.4.11-1
- Update to 2.4.11
- Include vala bindings
- Fix gir directory ownership

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 03 2018 Bastien Nocera <bnocera@redhat.com> - 2.4.10-1
+ geoclue2-2.4.10-1
- Update to 2.4.10

* Thu May 03 2018 Bastien Nocera <bnocera@redhat.com> - 2.4.9-1
+ geoclue2-2.4.9-1
- Update to 2.4.9

* Thu Apr 12 2018 Kalev Lember <klember@redhat.com> - 2.4.8-1
- Update to 2.4.8

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.4.7-3
- Switch to %%ldconfig_scriptlets

* Wed Nov 29 2017 Lubomir Rintel <lkundrak@v3.sk> - 2.4.7-2
- Obsolete old geoclue

* Tue Sep 05 2017 Kalev Lember <klember@redhat.com> - 2.4.7-1
- Update to 2.4.7

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Mar 24 2017 Florian Müllner <fmuellner@redhat.com> - 32.4.5-4
- Add gnome-shell's weather integration to the whitelist

* Wed Mar 01 2017 Kalev Lember <klember@redhat.com> - 2.4.5-3
- Add "Night Light" functionality to the whitelist

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Kalev Lember <klember@redhat.com> - 2.4.5-1
- Update to 2.4.5

* Tue Sep 06 2016 Bastien Nocera <bnocera@redhat.com> - 2.4.4-1
- Update to 2.4.4

* Tue Mar 08 2016 Zeeshan Ali <zeenix@redhat.com> 2.4.3-1
- Update to 2.4.3.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 08 2015 Kalev Lember <klember@redhat.com> - 2.4.1-1
- Update to 2.4.1

* Wed Nov 04 2015 Kalev Lember <klember@redhat.com> - 2.4.0-1
- Update to 2.4.0
- Package new libgeoclue-2.0 library in -libs subpackage
- Fix directory ownership for /usr/libexec/geoclue-2.0/demos/
- Use license macro for COPYING

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 16 2015 Zeeshan Ali <zeenix@redhat.com> 2.2.0-1
- Update to 2.2.0.

* Tue Apr  7 2015 Zeeshan Ali <zeenix@redhat.com> 2.1.10-2
- Package demo applications too.

* Tue Jan  6 2015 Peter Robinson <pbrobinson@fedoraproject.org> 2.1.10-1
- Update to 2.1.10

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 21 2014 Kalev Lember <kalevlember@gmail.com> - 2.1.9-1
- Update to 2.1.9

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 16 2014 Kalev Lember <kalevlember@gmail.com> - 2.1.8-1
- Update to 2.1.8
- Remove and obsolete the -server subpackage

* Wed Mar 26 2014 Kalev Lember <kalevlember@gmail.com> - 2.1.7-1
- Update to 2.1.7

* Fri Mar 07 2014 Kalev Lember <kalevlember@gmail.com> - 2.1.6-1
- Update to 2.1.6

* Thu Feb 06 2014 Kalev Lember <kalevlember@gmail.com> - 2.1.2-2
- Add systemd rpm scripts
- Don't install the demo .desktop files

* Tue Feb 04 2014 Richard Hughes <rhughes@redhat.com> - 2.1.2-1
- Update to 2.1.2

* Sun Oct 06 2013 Kalev Lember <kalevlember@gmail.com> - 2.0.0-1
- Update to 2.0.0
- Create a home directory for the 'geoclue' user

* Thu Sep 19 2013 Kalev Lember <kalevlember@gmail.com> - 1.99.4-2
- Run the service as 'geoclue' user

* Wed Sep 18 2013 Kalev Lember <kalevlember@gmail.com> - 1.99.4-1
- Update to 1.99.4

* Tue Sep 03 2013 Kalev Lember <kalevlember@gmail.com> - 1.99.3-1
- Update to 1.99.3

* Sun Aug 25 2013 Kalev Lember <kalevlember@gmail.com> - 1.99.2-3
- Update -devel subpackage description (#999153)

* Sat Aug 24 2013 Kalev Lember <kalevlember@gmail.com> - 1.99.2-2
- Review fixes (#999153)
- Drop ldconfig calls that are unnecessary now that the shared library is gone
- Drop the build dep on gobject-introspection-devel
- Include API-Documentation.txt in the -server subpackage

* Fri Aug 23 2013 Kalev Lember <kalevlember@gmail.com> - 1.99.2-1
- Update to 1.99.2
- The shared library is gone in this release and all users should use the
  dbus service directly

* Wed Aug 21 2013 Kalev Lember <kalevlember@gmail.com> - 1.99.1-3
- Include geoip-lookup in the -server subpackage as well

* Wed Aug 21 2013 Kalev Lember <kalevlember@gmail.com> - 1.99.1-2
- Ship geoip-update in -server subpackage

* Tue Aug 20 2013 Kalev Lember <kalevlember@gmail.com> - 1.99.1-1
- Initial Fedora packaging
