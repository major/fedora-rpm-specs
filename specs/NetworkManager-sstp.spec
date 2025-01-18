#global snapshot .20220407git182a55b9
#global snapshot_full_commit_hash 182a55b942cb43fdbf398ade2d8862d83157ed4e
%global ppp_version %(pkg-config --modversion pppd 2>/dev/null || echo bad)

%if 0%{?fedora} < 28 && 0%{?rhel} < 8
%bcond_without libnm_glib
%else
# Disable the legacy version by default
%bcond_with libnm_glib
%endif

# Requires ppp >= 2.4.9
%if 0%{?fedora} >= 33
%bcond_without pppd_auth_notify_support
%else
%bcond_with pppd_auth_notify_support
%endif

%if 0%{?fedora} >= 36
%bcond_without gtk4
%else
%bcond_with gtk4
%endif

Summary:   NetworkManager VPN plugin for SSTP
Name:      NetworkManager-sstp
Epoch:     1
Version:   1.3.1
Release:   11%{?snapshot}%{?dist}
License:   GPL-2.0-or-later
URL:       https://gitlab.gnome.org/GNOME/network-manager-sstp

%if "%{?snapshot:1}" == "1"
Source:    https://gitlab.gnome.org/GNOME/network-manager-sstp/-/archive/%{snapshot_full_commit_hash}/network-manager-sstp-%{snapshot_full_commit_hash}.tar.bz2
%else
Source:    https://download.gnome.org/sources/%{name}/1.3/%{name}-%{version}.tar.xz
%endif
# backport from upstream to fix build against ppp 2.5.0
Patch0: 0001-Support-to-compile-against-pppd-2.5.0.patch

BuildRequires: make
%if %{with gtk4}
BuildRequires: gtk4-devel
BuildRequires: libnma-gtk4-devel
%else
BuildRequires: gtk3-devel
%endif
BuildRequires: dbus-devel
%if %{with libnm_glib}
BuildRequires: NetworkManager-glib-devel >= 1.2.0
BuildRequires: libnm-gtk-devel >= 1.2.0
%else
BuildRequires: NetworkManager-libnm-devel >= 1.2.0
%endif
BuildRequires: sstp-client-devel
BuildRequires: glib2-devel
BuildRequires: pkgconfig
BuildRequires: ppp-devel >= 2.5.0
# ppp 2.5.0 patches require autoreconf, drop this when a new version
# is released and those patches are dropped
BuildRequires: autoconf automake gettext-devel
BuildRequires: libtool intltool gettext
BuildRequires: libsecret-devel
BuildRequires: libnma-devel >= 1.2.0
BuildRequires: gnutls-devel

Requires: dbus-common
Requires: NetworkManager >= 1.2.0
Requires: sstp-client
Requires: ppp = %{ppp_version}

Recommends: (NetworkManager-sstp-gnome if gnome-shell)

%global __provides_exclude ^libnm-.*\\.so

%description
This package contains software for integrating VPN capabilities using
the SSTP server with NetworkManager.

%package -n NetworkManager-sstp-gnome
Summary: NetworkManager VPN plugin for SSTP - GNOME files

Requires: NetworkManager-sstp%{?_isa} = %{epoch}:%{version}-%{release}
Requires: nm-connection-editor

%description -n NetworkManager-sstp-gnome
This package contains software for integrating VPN capabilities with
the SSTP server with NetworkManager (GNOME files).

%prep
%if "%{?snapshot:1}" == "1"
%autosetup -p1 -n network-manager-sstp-%{snapshot_full_commit_hash}
%else
%autosetup -p1
%endif

%build
# for ppp 2.5.0 patches
autoreconf -if
%if "%{?snapshot:1}" == "1"
./autogen.sh
%endif

%configure \
    --disable-static \
    --enable-more-warnings=yes \
    %{?without_libnm_glib:--without-libnm-glib} \
    %{?with_pppd_auth_notify_support:--with-pppd-auth-notify-support} \
    %{?with_gtk4:--with-gtk4} \
    --with-pppd-plugin-dir=%{_libdir}/pppd/%{ppp_version}
%make_build

%install
%make_install

rm -f %{buildroot}%{_libdir}/NetworkManager/lib*.la
rm -f %{buildroot}%{_libdir}/pppd/%{ppp_version}/*.la

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS README ChangeLog
%license COPYING
%{_datadir}/dbus-1/system.d/nm-sstp-service.conf
%{_libexecdir}/nm-sstp-service
%{_libexecdir}/nm-sstp-auth-dialog
%{_libdir}/pppd/%{ppp_version}/nm-sstp-pppd-plugin.so
# TODO: rpmlint doesn't like it, however, it is used in all similar NM-related projects
%{_prefix}/lib/NetworkManager/VPN/nm-sstp-service.name

%files -n NetworkManager-sstp-gnome
%doc AUTHORS README ChangeLog
%license COPYING
%{_libdir}/NetworkManager/lib*.so*
%{_datadir}/metainfo/network-manager-sstp.metainfo.xml

%if %with libnm_glib
%{_sysconfdir}/NetworkManager/VPN/nm-sstp-service.name
%endif

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Nov 27 2024 Adam Williamson <awilliam@redhat.com> - 1.3.1-10
- Rebuild for ppp 2.5.1

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Nov 03 2023 Íñigo Huguet <ihuguet@redhat.com> - 1:1.3.1-6
- Migrated to SPDX license

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Apr 18 2023 Adam Williamson <awilliam@redhat.com> - 1:1.3.1-4
- Rebuild for new ppp

* Fri Apr 14 2023 Florian Weimer <fweimer@redhat.com> - 1:1.3.1-3
- Port to C99

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Sep 25 2022 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 1:1.3.1-1
- Update to 1.3.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Apr 23 2022 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 1:1.3.0-3
- NetworkManager-sstp-gnome is recommended for NetworkManager-sstp (only if gnome-shell is already installed)

* Fri Apr 22 2022 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 1:1.3.0-2
- Switch build/install to macros
- Mention upstream changes for 1.3.0 ↓↓↓
- Fixes for IPv6 handling
- Support for EAP authentication
  - EAP-MSCHAPv2 is now supported in pppd >= 2.4.9
  - EAP-TLS is supported in pppd 2.4.9, but patches for MPPE keys may be needed
- Added support to configure TLS authentication
- Improved support for handling of MPPE during authentication.
- New Translation updates supported by the Gnome community
- Added support for GTK4
- Lots of bug fixes

* Thu Apr 21 2022 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 1:1.3.0-1
- Update to 1.3.0 final (formerly 1.2.7)

* Thu Apr 07 2022 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 1:1.2.7-0.20220407git182a55b9
- Update to 1.2.7-SNAPSHOT
- Build gtk4 variant for Fedora 36+ (BZ #2064985)
- Enable pppd_auth_notify_support for ppp >= 2.4.9

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.2.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.2.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Feb 15 2021 Lubomir Rintel <lkundrak@v3.sk> - 1:1.2.6-8
- Move dbus service file into /usr/share/dbus-1

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.2.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.2.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Feb 22 2020 Kevin Fenzi <kevin@scrye.com> - 1.2.6-6
- Rebuild for new ppp

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Apr 15 2018 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 1:1.2.6-1
- Update to 1.2.6

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 30 2017 Lubomir Rintel <lkundrak@v3.sk> - 1.2.0-5
- Drop libnm-glib for Fedora 28

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Aug 16 2016 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 1:1.2.0-1
- Switch to 1.2.0 tarball

* Thu Jun 30 2016 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 1:1.2.0-0.20160529git72e50bf2
- Fix issue with broken dependency due to missing epoch
- Update to Git commit with 1.2.0 final

* Fri Jun 24 2016 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 1:1.2.0-0.20160514git86c2737d
- Upgrade to Git snapshot from 1.2.0 branch
- Specification enhancements by Lubomir Rintel

* Thu Feb 04 2016 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 1:0.9.10-6
- Apply remarks after package review by Christopher Meng
- Specify minimal required ppp version to >= 2.4.6

* Wed Jun 24 2015 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 1:0.9.10-5
- Change doc macro to license macro for COPYING file
- Change URL to plugin project page instead if NetworkManager itself

* Thu Jun 11 2015 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 1:0.9.10-4
- Specify minimum required NetworkManager version - 0.9.10

* Mon Jun 08 2015 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 1:0.9.10-3
- Minor changes to adjust configuration to Fedora requirements
- Remove redundant Obsoletes tag 

* Tue Jun 02 2015 Eivind Naess <eivnaes@yahoo.com> - 1:0.9.10-2
- Taking suggested changes for Gateway validation from George Joseph

* Fri May 29 2015 Eivind Naess <eivnaes@yahoo.com> - 1:0.9.10-1
- Upgraded the network-manager-sstp package to reflect mainstream 
  changes made to the network-manager-pptp counter part.

* Fri Oct 12 2012 Eivind Naess <eivnaes@yahoo.com> - 1:0.9.4-2
- Fixed a bug that caused connection to be aborted with the message:
  "Connection was aborted, value of attribute is incorrect"

* Sat May 05 2012 Eivind Naess <eivnaes@yahoo.com> - 1:0.9.4-1
- Compiled against the latest network manager 0.9.4 sources.

* Sat Mar 03 2012 Eivind Naess <eivnaes@yahoo.com> - 1:0.9.1-4
- Added back the 'refuese-eap=yes' by default in the configuration.

* Wed Feb 08 2012 Eivind Naess <eivnaes@yahoo.com> - 1:0.9.1-3
- Changed the pppd plugin to send MPPE keys on ip-up

* Sun Nov 20 2011 Eivind Naess <eivnaes@yahoo.com> - 1:0.9.1-2
- Added proxy support

* Sun Oct 02 2011 Eivind Naess <eivnaes@yahoo.com> - 1:0.9.0-1
- Initial release
