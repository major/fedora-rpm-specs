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
Release: %autorelease
Summary: Virtual Machine Viewer
License: GPL-2.0-or-later
URL: https://gitlab.com/virt-viewer/virt-viewer
Source0: https://virt-manager.org/download/sources/%{name}/%{name}-%{version}.tar.xz
Patch: 0001-data-remove-bogus-param-for-meson-i18n.merge_file.patch
Patch: 0001-Read-oVirt-CA-and-pass-it-to-gtk-vnc.patch
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
BuildRequires: pkgconfig(gtk-vnc-2.0) >= 1.5.0
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
%autochangelog
