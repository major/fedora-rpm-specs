%global commit e201da5a4efbb767fb64fd694bbf9d33758a85eb
%global date 20231021
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global ppp_version %(pkg-config --modversion pppd 2>/dev/null || echo bad)
%global __provides_exclude ^libnm-.*\\.so

Summary:    NetworkManager VPN plugin for Fortinet compatible SSLVPN
Name:       NetworkManager-fortisslvpn
Version:    1.4.1
Release:    8.%{date}git%{shortcommit}%{?dist}
License:    GPL-2.0-or-later
URL:        http://www.gnome.org/projects/NetworkManager/

Source0:    https://gitlab.gnome.org/GNOME/%{name}/-/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gtk3-devel >= 3.4
BuildRequires:  dbus-devel >= 0.74
BuildRequires:  NetworkManager-libnm-devel >= 1:1.2.0
BuildRequires:  glib2-devel >= 2.32
BuildRequires:  pkgconfig
BuildRequires:  ppp-devel >= 2.5.0
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gettext-devel
BuildRequires:  libtool
BuildRequires:  gettext
BuildRequires:  libsecret-devel
BuildRequires:  libnma-devel >= 1.2.0
BuildRequires:  libnma-gtk4-devel

Requires:       dbus-common
Requires:       NetworkManager >= 1:1.2.0
Requires:       openfortivpn
Requires:       ppp = %{ppp_version}

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
%autosetup -p1 -n %{name}-%{commit}

%build
autoreconf -fi
%configure \
  --disable-static \
  --with-gtk4 \
  --with-pppd-plugin-dir=%{_libdir}/pppd/%{ppp_version} \
  --with-dist-version=%{version}-%{release}

%make_build

%check
make check

%install
%make_install

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
%license COPYING
%doc AUTHORS README ChangeLog
%{_libdir}/NetworkManager/libnm-vpn-plugin-fortisslvpn.so
%{_datadir}/dbus-1/system.d/nm-fortisslvpn-service.conf
%{_prefix}/lib/NetworkManager/VPN/nm-fortisslvpn-service.name
%{_libexecdir}/nm-fortisslvpn-pinentry
%{_libexecdir}/nm-fortisslvpn-service
%{_libdir}/pppd/%{ppp_version}/nm-fortisslvpn-pppd-plugin.so
%{_sharedstatedir}/NetworkManager-fortisslvpn

%files -n NetworkManager-fortisslvpn-gnome
%{_libexecdir}/nm-fortisslvpn-auth-dialog
%{_libdir}/NetworkManager/lib*.so*
%{_datadir}/metainfo/network-manager-fortisslvpn.metainfo.xml

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-8.20231021gite201da5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Nov 27 2024 Adam Williamson <awilliam@redhat.com> - 1.4.1-7.20231021gite201da5
- Rebuild for ppp 2.5.1

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-6.20231021gite201da5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-5.20231021gite201da5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-4.20231021gite201da5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Nov 22 2023 Simone Caronni <negativo17@gmail.com> - 1.4.1-3.20231021gite201da5
- Drop the --no-routes patch, this is not the correct approach.

* Wed Nov 22 2023 Simone Caronni <negativo17@gmail.com> - 1.4.1-2.20231021gite201da5
- Do not add --no-routes to openfortivpn connection.

* Wed Nov 22 2023 Simone Caronni <negativo17@gmail.com> - 1.4.1-1.20231021gite201da5
- Update to upstream snapshot.
- Trim changelog.
- Drop conditionals for obsolete distributions or distributions that have their
  own branch.
- Use macros where possible.
- Format SPEC file and sort build requirements.

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
