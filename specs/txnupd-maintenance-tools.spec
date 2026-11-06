
Name:           txnupd-maintenance-tools
Version:        1.1
Release:        1%{?dist}
Summary:        Update Notifier and Maintenance Tools

License:        GPL-3.0-or-later
URL:            https://codeberg.org/KalpaDesktop/txnupd-maintenance-tools
Source0:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.zst

BuildRequires:  cmake
BuildRequires:  dbus-common
BuildRequires:  python3dist(pytest)
BuildRequires:  scdoc
BuildRequires:  systemd-rpm-macros

Requires:       btrfsmaintenance
Requires:       python3 >= 3.11
Requires:       python3-dbus
Requires:       python3-gobject
Requires:       libnotify
Requires:       tukit
Requires:       tukitd

BuildArch:      noarch


%description
D-Bus notifier daemon/client for both transactional-update and
dnf5-txnupd transactional systems, and snapshot/system maintenance
tools for transactional systems


%prep
%autosetup -C -p1

%conf
%cmake \
  -DINSTALL_SYSTEMD_PRESET=OFF \
  -DWITH_PBL=OFF

%build
%cmake_build


%install
%cmake_install

%preun
%systemd_user_preun txnupd-notifier.service

%post
%systemd_user_post txnupd-notifier.service

%postun
%systemd_user_postun txnupd-notifier.service

%check
python3 -m pytest -v

%files
%license LICENSE
%doc README.md
%{_bindir}/transactional-update-notifier
%{_bindir}/txnupd-maint
%{_bindir}/txnupd-notifier
%{_bindir}/txnupd-notifier-client
%{_datadir}/%{name}/txnupd-notifier.conf
%{_datadir}/dbus-1/system.d/org.opensuse.tukit.Updated.conf
%{_mandir}/man?/txnupd*
%{_userunitdir}/txnupd-notifier.service


%changelog
* Thu Nov 05 2026 Shawn W Dunn <sfalken@kalpadesktop.org> - 1.1-1
- Update to 1.1 release

* Sun Aug 23 2026 Shawn W Dunn <sfalken@kalpadesktop.org> - 1.1.beta-1
- Update to 1.1.beta

* Sun Jun 21 2026 Shawn W Dunn <sfalken@kalpadesktop.org> - 1.0.beta-4
- rebuilt

* Sun Jun 21 2026 Shawn W Dunn <sfalken@kalpadesktop.org> - 1.0.beta-3
- rebuilt

* Sun Jun 21 2026 Shawn W Dunn <sfalken@kalpadesktop.org> - 1.0.beta-2
- rebuilt

* Fri Jun 19 2026 Shawn W Dunn <sfalken@kalpadesktop.org> - 1.0.beta-1
- Initial Packaging

