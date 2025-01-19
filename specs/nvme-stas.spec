Name:    nvme-stas
Summary: NVMe STorage Appliance Services
Version: 2.3.1
Release: 6%{?dist}
License: Apache-2.0
URL:     https://github.com/linux-nvme/nvme-stas
Source0: %{url}/archive/v%{version_no_tilde}/%{name}-%{version_no_tilde}.tar.gz

BuildArch:     noarch

BuildRequires: meson >= 0.57.0
BuildRequires: glib2-devel
BuildRequires: libnvme-devel >= 1.5
BuildRequires: libxslt
BuildRequires: docbook-style-xsl
BuildRequires: systemd-devel
BuildRequires: systemd-rpm-macros

BuildRequires: python3-devel
%if (0%{?rhel} == 0)
BuildRequires: python3-pyflakes
BuildRequires: python3-pylint
BuildRequires: pylint
%endif

BuildRequires: python3-libnvme
BuildRequires: python3-dasbus
BuildRequires: python3-pyudev
BuildRequires: python3-systemd
BuildRequires: python3-gobject-devel
BuildRequires: python3-lxml

Requires:      avahi
Requires:      python3-libnvme >= 1.5
Requires:      python3-dasbus
Requires:      python3-pyudev
Requires:      python3-systemd
Requires:      python3-gobject
Requires:      python3-lxml

%description
nvme-stas is a Central Discovery Controller (CDC) client for Linux. It
handles Asynchronous Event Notifications (AEN), Automated NVMe subsystem
connection controls, Error handling and reporting, and Automatic (zeroconf)
and Manual configuration. nvme-stas is composed of two daemons:
stafd (STorage Appliance Finder) and stacd (STorage Appliance Connector).

%prep
%autosetup -p1 -n %{name}-%{version_no_tilde}

%build
%meson -Dman=true -Dhtml=true
%meson_build

%install
%meson_install
mv %{buildroot}/%{_sysconfdir}/stas/sys.conf.doc %{buildroot}/%{_sysconfdir}/stas/sys.conf

%post
%systemd_post stacd.service
%systemd_post stafd.service

%preun
%systemd_preun stacd.service
%systemd_preun stafd.service

%postun
%systemd_postun_with_restart stacd.service
%systemd_postun_with_restart stafd.service

%files
%license LICENSE
%doc README.md
%dir %{_sysconfdir}/stas
%config(noreplace) %{_sysconfdir}/stas/stacd.conf
%config(noreplace) %{_sysconfdir}/stas/stafd.conf
%config(noreplace) %{_sysconfdir}/stas/sys.conf
%{_datadir}/dbus-1/system.d/org.nvmexpress.*.conf
%{_bindir}/stacctl
%{_bindir}/stafctl
%{_bindir}/stasadm
%{_sbindir}/stacd
%{_sbindir}/stafd
%{_unitdir}/stacd.service
%{_unitdir}/stafd.service
%{_unitdir}/stas-config.target
%{_unitdir}/stas-config@.service
%dir %{python3_sitelib}/staslib
%{python3_sitelib}/staslib/*
%doc %{_pkgdocdir}/html
%{_mandir}/man1/sta*.1*
%{_mandir}/man5/*.5*
%{_mandir}/man7/nvme*.7*
%{_mandir}/man8/sta*.8*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 16 2024 Python Maint <python-maint@redhat.com> - 2.3.1-4
- Rebuilt for Python 3.13

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Nov 29 2023 Tomas Bzatek <tbzatek@redhat.com> - 2.3.1-1
- Upstream v2.3.1 release

* Fri Sep 22 2023 Tomas Bzatek <tbzatek@redhat.com> - 2.3-1
- Upstream v2.3 release

* Thu Aug 17 2023 Tomas Bzatek <tbzatek@redhat.com> - 2.3~rc4-1
- Upstream v2.3 Release Candidate 4

* Tue Aug 01 2023 Tomas Bzatek <tbzatek@redhat.com> - 2.3~rc3-1
- Upstream v2.3 Release Candidate 3

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3~rc2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 18 2023 Tomas Bzatek <tbzatek@redhat.com> - 2.3~rc2-1
- Upstream v2.3 Release Candidate 2

* Mon Jul 10 2023 Python Maint <python-maint@redhat.com> - 2.3~rc1-2
- Rebuilt for Python 3.12

* Tue Jul 04 2023 Tomas Bzatek <tbzatek@redhat.com> - 2.3~rc1-1
- Upstream v2.3 Release Candidate 1

* Sun Jul 02 2023 Python Maint <python-maint@redhat.com> - 2.2.1-2
- Rebuilt for Python 3.12

* Mon Apr 03 2023 Tomas Bzatek <tbzatek@redhat.com> - 2.2.1-1
- Upstream v2.2.1 release

* Wed Feb 01 2023 Tomas Bzatek <tbzatek@redhat.com> - 2.1.2-1
- Upstream v2.1.2 release

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Nov 04 2022 Tomas Bzatek <tbzatek@redhat.com> - 2.0-1
- Upstream v2.0 release

* Tue Nov 01 2022 Tomas Bzatek <tbzatek@redhat.com> - 2.0~rc5-1
- Upstream v2.0 Release Candidate 5

* Fri Sep 16 2022 Tomas Bzatek <tbzatek@redhat.com> - 1.2~rc3-1
- Upstream v1.2 Release Candidate 3

* Fri Jul 22 2022 Tomas Bzatek <tbzatek@redhat.com> - 1.1.6-1
- Upstream v1.1.6 release

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 28 2022 Tomas Bzatek <tbzatek@redhat.com> - 1.1.5-1
- Upstream v1.1.5 release

* Fri Jun 17 2022 Python Maint <python-maint@redhat.com> - 1.1.4-2
- Rebuilt for Python 3.11

* Fri Jun 17 2022 Tomas Bzatek <tbzatek@redhat.com> - 1.1.4-1
- Upstream v1.1.4 release

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.1.3-3
- Rebuilt for Python 3.11

* Mon Jun 13 2022 Tomas Bzatek <tbzatek@redhat.com> - 1.1.3-2
- Upstream v1.1.3 updated release (git tag f24b4b5)

* Thu Jun 09 2022 Tomas Bzatek <tbzatek@redhat.com> - 1.1.3-1
- Upstream v1.1.3 release

* Mon May 23 2022 Tomas Bzatek <tbzatek@redhat.com> - 1.1.1-1
- Upstream v1.1.1 release

* Thu May 19 2022 Tomas Bzatek <tbzatek@redhat.com> - 1.1-1
- Upstream v1.1 release

* Wed Apr 20 2022 Tomas Bzatek <tbzatek@redhat.com> - 1.0-1
- Upstream v1.0 official release

* Tue Apr 05 2022 Tomas Bzatek <tbzatek@redhat.com> - 1.0~rc7-1
- Upstream v1.0 Release Candidate 7

* Fri Mar 25 2022 Tomas Bzatek <tbzatek@redhat.com> - 1.0~rc5-1
- Upstream v1.0 Release Candidate 5

* Mon Mar 07 2022 Tomas Bzatek <tbzatek@redhat.com> - 1.0~rc3-1
- Upstream v1.0 Release Candidate 3
