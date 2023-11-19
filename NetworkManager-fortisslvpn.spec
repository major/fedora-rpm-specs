%if 0%{?fedora} < 28 && 0%{?rhel} < 8
%bcond_without libnm_glib
%else
# Disable the legacy version by default
%bcond_with libnm_glib
%endif
%if 0%{?fedora} < 36 && 0%{?rhel} < 10
%bcond_with gtk4
%else
%bcond_without gtk4
%endif

Summary:   NetworkManager VPN plugin for Fortinet compatible SSLVPN
Name:      NetworkManager-fortisslvpn
Version:   1.4.0
Release:   6%{?dist}
License:   GPL-2.0-or-later
URL:       http://www.gnome.org/projects/NetworkManager/
Source0:   https://download.gnome.org/sources/NetworkManager-fortisslvpn/1.4/%{name}-%{version}.tar.xz
# backports from upstream: fix build with ppp 2.5.0
Patch0:    0001-Adding-support-for-compiling-against-pppd-2.5.0-or-m.patch
Patch1:    0002-Fixing-configure.ac-from-previous-change.patch

%global ppp_version %(pkg-config --modversion pppd 2>/dev/null || echo bad)

BuildRequires: make
BuildRequires: gcc
BuildRequires: gtk3-devel >= 3.4
BuildRequires: dbus-devel >= 0.74
BuildRequires: NetworkManager-libnm-devel >= 1:1.2.0
BuildRequires: glib2-devel >= 2.32
BuildRequires: pkgconfig
BuildRequires: ppp-devel >= 2.5.0
# ppp 2.5.0 patches require autoreconf, drop this when a new version
# is released and those patches are dropped
BuildRequires: autoconf automake gettext-devel
BuildRequires: libtool gettext
BuildRequires: libsecret-devel
BuildRequires: libnma-devel >= 1.2.0

%if %with libnm_glib
BuildRequires: NetworkManager-glib-devel >= 1:1.2.0
BuildRequires: libnm-gtk-devel >= 1.2.0
%endif

%if %with gtk4
BuildRequires: libnma-gtk4-devel
%endif

Requires: dbus-common
Requires: NetworkManager >= 1:1.2.0
Requires: openfortivpn
Requires: ppp = %{ppp_version}

%global __provides_exclude ^libnm-.*\\.so


%description
This package contains software for integrating VPN capabilities with
the Fortinet compatible SSLVPN server with NetworkManager.


%package -n NetworkManager-fortisslvpn-gnome
Summary: NetworkManager VPN plugin for SSLVPN - GNOME files

Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n NetworkManager-fortisslvpn-gnome
This package contains software for integrating VPN capabilities with
the Fortinet compatible SSLVPN server with NetworkManager (GNOME files).


%prep
%autosetup -p1


%build
# for ppp 2.5.0 patches
autoreconf -fi
%configure \
        --disable-static \
%if %with gtk4
	--with-gtk4 \
%endif
%if %without libnm_glib
	--without-libnm-glib \
%endif
        --with-pppd-plugin-dir=%{_libdir}/pppd/%{ppp_version} \
        --with-dist-version=%{version}-%{release}

%make_build

%check
make check


%install
make install DESTDIR=%{buildroot} INSTALL="%{__install} -p"

rm -f %{buildroot}%{_libdir}/NetworkManager/lib*.la
rm -f %{buildroot}%{_libdir}/pppd/%{ppp_version}/*.la

mv %{buildroot}%{_sysconfdir}/dbus-1 %{buildroot}%{_datadir}/

%find_lang %{name}


%pre
getent group nm-fortisslvpn >/dev/null || groupadd -r nm-fortisslvpn
getent passwd nm-fortisslvpn >/dev/null || \
        useradd -r -g nm-fortisslvpn -d / -s /sbin/nologin \
        -c "Default user for running openfortivpn spawned by NetworkManager" nm-fortisslvpn
exit 0


%files -f %{name}.lang
%{_libdir}/NetworkManager/libnm-vpn-plugin-fortisslvpn.so
%{_datadir}/dbus-1/system.d/nm-fortisslvpn-service.conf
%{_prefix}/lib/NetworkManager/VPN/nm-fortisslvpn-service.name
%{_libexecdir}/nm-fortisslvpn-pinentry
%{_libexecdir}/nm-fortisslvpn-service
%{_libdir}/pppd/%{ppp_version}/nm-fortisslvpn-pppd-plugin.so
%{_sharedstatedir}/NetworkManager-fortisslvpn
%doc AUTHORS README ChangeLog
%license COPYING

%files -n NetworkManager-fortisslvpn-gnome
%{_libexecdir}/nm-fortisslvpn-auth-dialog
%{_libdir}/NetworkManager/libnm-vpn-plugin-fortisslvpn-editor.so
%{_libdir}/NetworkManager/lib*.so*
%{_datadir}/appdata/network-manager-fortisslvpn.metainfo.xml

%if %with libnm_glib
%{_libdir}/NetworkManager/libnm-*-properties.so
%{_sysconfdir}/NetworkManager/VPN/nm-fortisslvpn-service.name
%endif


%changelog
* Fri Nov 03 2023 Íñigo Huguet <ihuguet@redhat.com> - 1.4.0-6
- Migrated to SPDX license

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Apr 18 2023 Adam Williamson <awilliam@redhat.com> - 1.4.0-4
- Rebuild for new ppp

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 11 2022 Lubomir Rintel <lkundrak@v3.sk> - 1.4.0-1
- Update to 1.4.0 release

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.90-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.90-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Feb 15 2021 Lubomir Rintel <lkundrak@v3.sk> - 1.3.90-11
- Move dbus service file into /usr/share/dbus-1

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.90-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 10 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.90-9
- rebuild against new ppp

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.90-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr 15 2020 Simone Caronni <negativo17@gmail.com> - 1.3.90-7
- Update DNS handling patch.

* Sat Feb 22 2020 Kevin Fenzi <kevin@scrye.com> - 1.3.90-6
- Rebuild for new ppp

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.90-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 30 2019 Simone Caronni <negativo17@gmail.com> - 1.3.90-4
- Proper workaround for openfortivpn 1.11.

* Fri Dec 20 2019 Simone Caronni <negativo17@gmail.com> - 1.3.90-3
- Fix regression with openfortivpn 1.11.
- Use autosetup and make build macro.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 16 2019 Lubomir Rintel <lkundrak@v3.sk> - 1.3.90-1
- Update to 1.4-rc1

* Thu Mar 21 2019 Lubomir Rintel <lkundrak@v3.sk> - 1.2.10-1
- Update to 1.2.10 release

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 17 2018 Thomas Haller <thaller@redhat.com> - 1.2.8-1
- Update to 1.2.8 release
- fix location of config file (rh #1519928)

* Thu Nov 30 2017 Lubomir Rintel <lkundrak@v3.sk> - 1.2.6-4
- Drop libnm-glib for Fedora 28

* Wed Nov 15 2017 Thomas Haller <thaller@redhat.com> - 1.2.6-3
- Fix broken plugin due to invalid linking of pppd plugin (rh #1512606) (2)

* Mon Nov 13 2017 Thomas Haller <thaller@redhat.com> - 1.2.6-2
- Fix broken plugin due to invalid linking of pppd plugin (rh #1512606)

* Tue Aug 29 2017 Lubomir Rintel <lkundrak@v3.sk> - 1.2.6-1
- Update to 1.2.6 release

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 24 2016 Thomas Haller <thaller@redhat.com> - 1.2.4-1
- Update to 1.2.4 release

* Mon Oct  3 2016 Thomas Haller <thaller@redhat.com> - 1.2.4-0.1
- Update to 1.2.4 pre-release
- Remove GTK dependency from base package
- Add new GTK-free VPN core editor plugin to base package
- Don't require nm-connection-editor anymore
- Support NM_VPN_LOG_LEVEL environment variable to control logging
- Support multiple concurrent VPN connections

* Wed May 11 2016 Lubomir Rintel <lkundrak@v3.sk> - 1.2.2-1
- Update to 1.2.2 release

* Wed Apr 20 2016 Lubomir Rintel <lkundrak@v3.sk> - 1.2.0-1
- Update to 1.2.0 release

* Thu Apr 14 2016 Lubomir Rintel <lkundrak@v3.sk> - 1.2.0-0.5.rc1
- Pull in newer translations and appstream metadata

* Tue Apr  5 2016 Lubomir Rintel <lkundrak@v3.sk> - 1.2.0-0.4.rc1
- Update to NetworkManager-fortisslvpn 1.2-rc1

* Tue Mar 29 2016 Lubomir Rintel <lkundrak@v3.sk> - 1.2.0-0.4.beta3
- Update to NetworkManager-fortisslvpn 1.2-beta3

* Tue Mar  1 2016 Lubomir Rintel <lkundrak@v3.sk> - 1.2.0-0.4.beta2
- Update to NetworkManager-fortisslvpn 1.2-beta2

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-0.4.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 19 2016 Lubomir Rintel <lkundrak@v3.sk> - 1.2.0-0.3.beta1
- Update to NetworkManager-fortisslvpn 1.2-beta1

* Tue Oct 27 2015 Lubomir Rintel <lkundrak@v3.sk> - 1.2.0-0.2.20151023git54599865
- Fix el7 build

* Fri Oct 23 2015 Lubomir Rintel <lkundrak@v3.sk> - 1.2.0-0.1.20151023git54599865
- A bit newer git snapshot

* Sat Oct 03 2015 Lubomir Rintel <lkundrak@v3.sk> - 1.2.0-0.1.20151003gitf89ab1f0
- Update to 1.2 git snapshot with libnm-based properties plugin

* Sat Oct 03 2015 Lubomir Rintel <lkundrak@v3.sk> - 1.0.6-1
- Bump to a newer release

* Tue Sep 29 2015 Lubomir Rintel <lkundrak@v3.sk> - 1.0.0-2
- Version BRs wherever appropriate

* Wed Sep 16 2015 Lubomir Rintel <lkundrak@v3.sk> - 1.0.0-1
- Initial packaging
