%if 0%{?fedora} < 36 && 0%{?rhel} < 10
%bcond_with gtk4
%else
%bcond_without gtk4
%endif

Summary:   NetworkManager VPN plugin for L2TP and L2TP/IPsec
Name:      NetworkManager-l2tp
Version:   1.20.20
Release:   2%{?dist}
License:   GPL-2.0-or-later
URL:       https://github.com/nm-l2tp/NetworkManager-l2tp
Source:    https://github.com/nm-l2tp/NetworkManager-l2tp/releases/download/%{version}/%{name}-%{version}.tar.xz

%global ppp_version %(pkg-config --modversion pppd 2>/dev/null || sed -n 's/^#define\\s*VERSION\\s*"\\([^\\s]*\\)"$/\\1/p' %{_includedir}/pppd/patchlevel.h 2>/dev/null | grep . || echo bad)

BuildRequires: make
BuildRequires: gcc
BuildRequires: glib2-devel
BuildRequires: gtk3-devel
BuildRequires: NetworkManager-libnm-devel >= 1:1.20.0
BuildRequires: libnma-devel >= 1.8.0
BuildRequires: pkgconfig
BuildRequires: ppp-devel >= 2.4.5
BuildRequires: autoconf automake
BuildRequires: libtool gettext
BuildRequires: libsecret-devel
BuildRequires: openssl-devel >= 1:1.1.0
BuildRequires: nss-devel
%if %with gtk4
BuildRequires: libnma-gtk4-devel
%endif

Requires: dbus-common
Requires: NetworkManager >= 1:1.20.0
Requires: ppp = %{ppp_version}
Requires: xl2tpd
Recommends: (libreswan or strongswan)
Recommends: (%{name}-gnome  if gnome-shell)
Recommends: (plasma-nm-l2tp if plasma-desktop)

%global __provides_exclude ^libnm-.*\\.so

%description
This package contains software for integrating L2TP and L2TP over
IPsec VPN support with the NetworkManager.

%package gnome
Summary: NetworkManager VPN plugin for L2TP and L2TP/IPsec - GNOME files
Requires: %{name}%{?_isa} = %{version}-%{release}

%description gnome
This package contains software for integrating L2TP and L2TP over
IPsec VPN support with the NetworkManager (GNOME files).

%prep
%autosetup -p1

%build
if [ ! -f configure ]; then
  autoreconf -fi
fi
%configure \
    --disable-static \
    --runstatedir=/run \
%if %with gtk4
    --with-gtk4 \
%endif
%if 0%{?rhel} == 8
    --enable-libreswan-dh2 \
    --with-nm-ipsec-nss-dir=%{_sysconfdir}/ipsec.d \
%else
    --with-nm-ipsec-nss-dir=%{_sharedstatedir}/ipsec/nss \
%endif
    --with-pppd-plugin-dir=%{_libdir}/pppd/%{ppp_version} \
    --with-dist-version=%{version}-%{release}
make %{?_smp_mflags}

%check
make check

%install
make install DESTDIR=%{buildroot} INSTALL="%{__install} -p"

rm -f %{buildroot}%{_libdir}/NetworkManager/lib*.la
rm -f %{buildroot}%{_libdir}/pppd/%{ppp_version}/*.la

mkdir -p %{buildroot}%{_sysconfdir}/ipsec.d
mkdir -p %{buildroot}%{_sysconfdir}/strongswan/ipsec.d
touch %{buildroot}%{_sysconfdir}/ipsec.d/ipsec.nm-l2tp.secrets
touch %{buildroot}%{_sysconfdir}/strongswan/ipsec.d/ipsec.nm-l2tp.secrets

%find_lang %{name}

%pre
# remove any NetworkManager-l2tp <= 1.2.10 transient ipsec-*.secrets files.
rm -f %{_sysconfdir}/ipsec.d/nm-l2tp-ipsec-*.secrets
rm -f %{_sysconfdir}/strongswan/ipsec.d/nm-l2tp-ipsec-*.secrets
exit 0

%files -f %{name}.lang
%{_libdir}/NetworkManager/libnm-vpn-plugin-l2tp.so
%{_datadir}/dbus-1/system.d/nm-l2tp-service.conf
%{_prefix}/lib/NetworkManager/VPN/nm-l2tp-service.name
%{_libexecdir}/nm-l2tp-service
%{_libdir}/pppd/%{ppp_version}/nm-l2tp-pppd-plugin.so
%ghost %attr(0600 - -) %{_sysconfdir}/ipsec.d/ipsec.nm-l2tp.secrets
%ghost %attr(0600 - -) %{_sysconfdir}/strongswan/ipsec.d/ipsec.nm-l2tp.secrets
%doc AUTHORS README.md NEWS
%license COPYING

%files gnome
%{_libexecdir}/nm-l2tp-auth-dialog
%{_libdir}/NetworkManager/libnm-vpn-plugin-l2tp-editor.so
%{_metainfodir}/network-manager-l2tp.metainfo.xml
%if %with gtk4
%{_libdir}/NetworkManager/libnm-gtk4-vpn-plugin-l2tp-editor.so
%endif

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Dec 24 2024 Douglas Kosovic <doug@uq.edu.au> - 1.20.20-1
- Updated to 1.20.20 release

* Wed Nov 27 2024 Adam Williamson <awilliam@redhat.com> - 1.20.16-3
- Rebuild for ppp 2.5.1

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat May 18 2024 Douglas Kosovic <doug@uq.edu.au> - 1.20.16-1
- Updated to 1.20.16 release

* Sun Apr 14 2024 Douglas Kosovic <doug@uq.edu.au> - 1.20.14-1
- Updated to 1.20.14 release

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Nov 03 2023 Íñigo Huguet <ihuguet@redhat.com> - 1.20.10-3
- Migrated to SPDX license

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon May 01 2023 Douglas Kosovic <doug@uq.edu.au> - 1.20.10-1
- Updated to 1.20.10 release
- Remove redundant ppp related patches
- Use ppp_version macro from NetworkManager

* Tue Apr 18 2023 Adam Williamson <awilliam@redhat.com> - 1.20.8-3
- Rebuild for new ppp

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec 30 2022 Douglas Kosovic <doug@uq.edu.au> - 1.20.8-1
- Updated to 1.20.8 release
- Added conditional recommends for NetworManager-l2tp-gnome and plasma-nm-l2tp
- Added runstatedir=/run

* Sat Oct 29 2022 Douglas Kosovic <doug@uq.edu.au> - 1.20.6-1
- Updated to 1.20.6 release

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 03 2022 Douglas Kosovic <doug@uq.edu.au> - 1.20.4-1
- Updated to 1.20.4 release

* Mon Apr 18 2022 Douglas Kosovic <doug@uq.edu.au> - 1.20.2-1
- Updated to 1.20.2 release
- Conditional gtk4 support added

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Oct 21 2021 Douglas Kosovic <doug@uq.edu.au> - 1.20.0-1
- Updated to 1.20.0 release
- Removed redundant BuildRequires intltool
- Added BuildRequires gcc

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.8.6-7
- Rebuilt with OpenSSL 3.0.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Feb 07 2021 Douglas Kosovic <doug@uq.edu.au> - 1.8.6-5
- Correct EPEL8 conditional

* Sun Feb 07 2021 Douglas Kosovic <doug@uq.edu.au> - 1.8.6-4
- Sync with EPEL8

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan  8 12:30:58 CET 2021 Tomas Hrcka <thrcka@redhat.com> - 1.8.6-2
- rebuilt for new version of ppp

* Tue Nov 03 2020 Douglas Kosovic <doug@uq.edu.au> - 1.8.6-1
- Updated to 1.8.6 release
- Remove redundant libnm_glib conditionals
- explictly recommend libreswan >= 4.0 because of change in NSS DB location.
- AppData file now in %%{_datadir}/metainfo/
- D-Bus policy file now in %%{_datadir}/dbus-1/system.d/

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Mar 26 2020 Douglas Kosovic <doug@uq.edu.au> - 1.8.2-1
- Updated to 1.8.2 release
- Remove redundant patches
- Recommends (libreswan or strongswan) instead of just libreswan

* Thu Feb 27 2020 Douglas Kosovic <doug@uq.edu.au> - 1.8.0-5
- Patch for user certificate support fix

* Wed Feb 26 2020 Douglas Kosovic <doug@uq.edu.au> - 1.8.0-4
- Patch to support libreswan 3.30 which is no longer built with modp1024 support

* Sat Feb 22 2020 Adam Williamson <awilliam@redhat.com> - 1.8.0-3
- Rebuild for new ppp

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 13 2019 Douglas Kosovic <doug@uq.edu.au> - 1.8.0-1
- Updated to 1.8.0 release

* Wed Nov 06 2019 Douglas Kosovic <doug@uq.edu.au> - 1.2.16-1
- Updated to 1.2.16 release

* Tue Oct 08 2019 Douglas Kosovic <doug@uq.edu.au> - 1.2.14-1
- Updated to 1.2.14 release

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar 16 2019 Douglas Kosovic <doug@uq.edu.au> - 1.2.12-1
- Updated to 1.2.12 release
- Use upstream provided xz tarball instead of GitHub generated gz tarball.
- Delete any transient nm-l2tp-ipsec-*.secrets files from versions <= 1.2.10
- %%ghost transient ipsec.nm-l2tp.secrets files.
- Merged EPEL 7 spec file with Fedora spec file.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 20 2018 Douglas Kosovic <doug@uq.edu.au> - 1.2.10-2
- Drop NetworkManager-devel for rawhide

* Tue Mar 20 2018 Douglas Kosovic <doug@uq.edu.au> - 1.2.10-1
- Updated to 1.2.10 release

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 30 2017 Lubomir Rintel <lkundrak@v3.sk> - 1.2.8-4
- Drop libnm-glib for Fedora 28

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 23 2017 Douglas Kosovic <doug@uq.edu.au> - 1.2.8-1
- Updated to 1.2.8 release
- Replaced requires libreswan with weaker recommends libreswan,
  allows uninstalling of libreswan if IPsec support isn't required

* Fri May 19 2017 Douglas Kosovic <doug@uq.edu.au> - 1.2.6-1
- Updated to 1.2.6 release
- Added %%check section

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Nov 20 2016 Douglas Kosovic <doug@uq.edu.au> - 1.2.4-1
- Update to 1.2.4 release
- Remove GTK dependency from base package (rh#1088677)
- Introduce new GTK-free VPN plugin base-library to nm-l2tp package
- Don't require nm-connection-editor anymore
- No need for --enable-more-warnings=yes configure switch anymore

* Mon May 16 2016 Douglas Kosovic <doug@uq.edu.au> - 1.2.2-1
- Updated to 1.2.2 release
- Added NetworkManager-l2tp-gnome RPM for GNOME files
- Updated BuildRequires, Requires, URL and Source
- Replaced filter_provides macro with newer macros

* Sat Apr 23 2016 Lubomir Rintel <lkundrak@v3.sk> - 1.2.0-1
- Update to 1.2.0 release

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-0.3.20151023git3239062
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Oct 27 2015 Lubomir Rintel <lkundrak@v3.sk> - 1.2.0-0.2.20151023git3239062
- Fix el7 build

* Fri Oct 23 2015 Lubomir Rintel <lkundrak@v3.sk> - 1.2.0-0.1.20151023git3239062
- Update to 1.2 git snapshot with libnm-based properties plugin

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Aug 12 2014 Kevin Fenzi <kevin@scrye.com> 0.9.8.7-2
- Rebuild for new ppp version.

* Thu Jul 31 2014 Ivan Romanov <drizt@land.ru> - 0.9.8.7-1
- updated to 0.9.8.7

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 11 2014 Ivan Romanov <drizt@land.ru> - 0.9.8.6-2
- use ppp of any version
- dropped Groups tag

* Thu Feb 27 2014 Ivan Romanov <drizt@land.ru> - 0.9.8.6-1
- updated to 0.9.8.6

* Sun Jan 19 2014 Ivan Romanov <drizt@land.ru> - 0.9.8.5-1
- updated to 0.9.8.5
- dropped patches, went to upstream

* Mon Sep 23 2013 Ivan Romanov <drizt@land.ru> - 0.9.8-4
- added NetworkManager-l2tp-Check-var-run-pluto-ipsec-info patch (#887674)

* Mon Sep 23 2013 Ivan Romanov <drizt@land.ru> - 0.9.8-3
- added NetworkManager-l2tp-noccp-pppd-option patch (#887674)

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr  1 2013 Ivan Romanov <drizt@land.ru> - 0.9.8-1
- a new upstream version

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Dec 25 2012 Ivan Romanov <drizt@land.ru> - 0.9.6-5
- openswan is requires

* Tue Dec 25 2012 Ivan Romanov <drizt@land.ru> - 0.9.6-4
- added openswan to BR

* Sat Dec 15 2012 Ivan Romanov <drizt@land.ru> - 0.9.6-3
- fix F17 dependency error (rh #886773)
- added licensies explanations

* Mon Nov 26 2012 Ivan Romanov <drizt@land.ru> - 0.9.6-2
- corrected License tag. Added LGPLv2+
- use only %%{buildroot}
- use %%config for configuration files
- removed unused scriptlets
- cleaned .spec file
- preserve timestamps when installing
- filtered provides for plugins
- droped zero-length changelog
- use %%global instead of %%define

* Mon Nov 19 2012 Ivan Romanov  <drizt@land.ru> - 0.9.6-1
- initial version based on NetworkManager-pptp 1:0.9.3.997-3

