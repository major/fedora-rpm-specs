# -*- rpm-spec -*-

%if 0%{?rhel} >= 9
%global with_govirt 0
%global with_spice 0
%else
# Disabled since it is still stuck on soup2
%global with_govirt 0
%global with_spice 1
%endif

Name: virt-viewer
Version: 11.0
Release: 11%{?dist}
Summary: Virtual Machine Viewer
License: GPL-2.0-or-later
URL: https://gitlab.com/virt-viewer/virt-viewer
Source0: https://virt-manager.org/download/sources/%{name}/%{name}-%{version}.tar.xz
Patch: 0001-data-remove-bogus-param-for-meson-i18n.merge_file.patch
Requires: openssh-clients

# Our bash completion script uses virsh to list domains
Requires: libvirt-client

BuildRequires: gcc
BuildRequires: meson
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(libvirt)
BuildRequires: pkgconfig(libvirt-glib-1.0)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(gtk-vnc-2.0)
BuildRequires: pkgconfig(vte-2.91)
%if %{with_spice}
BuildRequires: pkgconfig(spice-client-gtk-3.0)
BuildRequires: pkgconfig(spice-protocol)
%endif
BuildRequires: perl-podlators
BuildRequires: gettext
%if %{with_govirt}
BuildRequires: pkgconfig(govirt-1.0)
BuildRequires: pkgconfig(rest-0.7)
%endif
BuildRequires: pkgconfig(bash-completion)


%description
Virtual Machine Viewer provides a graphical console client for connecting
to virtual machines. It uses the GTK-VNC or SPICE-GTK widgets to provide
the display, and libvirt for looking up VNC/SPICE server details.

%prep
%autosetup -p1

%build

%define buildid_opt -Dbuild-id=%{release}

%if !%{with_govirt}
%define ovirt_opt -Dovirt=disabled
%endif

%if !%{with_spice}
%define spice_opt -Dspice=disabled
%endif

%if 0%{?rhel} > 0
%define osid_opt -Dos-id=rhel%{?rhel}
%endif

%meson %{buildid_opt} %{?ovirt_opt} %{?spice_opt} %{?osid_opt}
%meson_build

%install
%meson_install

%find_lang %{name}

%files -f %{name}.lang
%doc README.md COPYING AUTHORS NEWS
%{_bindir}/%{name}
%{_bindir}/remote-viewer
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/applications/remote-viewer.desktop
%{_datadir}/metainfo/remote-viewer.appdata.xml
%{_datadir}/mime/packages/virt-viewer-mime.xml
%{_mandir}/man1/virt-viewer.1*
%{_mandir}/man1/remote-viewer.1*
%{_datadir}/bash-completion/completions/virt-viewer

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 11.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 11.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jul  9 2024 Daniel P. Berrangé <berrange@redhat.com> - 11.0-9
- Tweak pod2man dep to suit flatpak builds better

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 11.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 11.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 11.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Aug 22 2022 Daniel P. Berrangé <berrange@redhat.com> - 11.0-5
- Disable govirt since it is still stuck on soup2 (rhbz#2119727)

* Tue Aug  2 2022 Daniel P. Berrangé <berrange@redhat.com> - 11.0-4
- Fix meson parameter error (rhbz #2113755)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 30 2021 Daniel P. Berrangé <berrange@redhat.com> - 11.0-1
- Rebase to 11.0 release
- Fixes often disabled send-key menu (rhbz#2020872)

* Thu Nov 25 2021 Daniel P. Berrangé <berrange@redhat.com> - 10.0-6
- Add missing dep on libvirt-clients for bash completion
- Refactor setting build-id opt

* Tue Nov 16 2021 Tom Stellard <tstellar@redhat.com> - 10.0-5
- Backport fix for uninitialized variable

* Wed Aug 11 2021 Daniel P. Berrangé <berrange@redhat.com> - 10.0-4
- Fix build with newer glib (rhbz#1988037)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Apr 26 2021 Daniel P. Berrangé <berrange@redhat.com> - 10.0-2
- Explicitly disable spice/ovirt

* Tue Apr 20 2021 Daniel P. Berrangé <berrange@redhat.com> - 10.0-1
- Update to 10.0 release

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May  1 2020 Daniel P. Berrangé <berrange@redhat.com> - 9.0-1
- Update to 9.0 release

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild
