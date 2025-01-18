%global glib2_minver 2.72

Name:           btrfsd
Version:        0.2.2
Release:        3%{?dist}
Summary:        Tiny Btrfs maintenance daemon

License:        LGPL-2.1-or-later
URL:            https://github.com/ximion/btrfsd
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  docbook-style-xsl
BuildRequires:  btrfs-progs
BuildRequires:  meson >= 0.60
BuildRequires:  gcc
BuildRequires:  pkgconfig(glib-2.0) >= %{glib2_minver}
BuildRequires:  pkgconfig(gobject-2.0) >= %{glib2_minver}
BuildRequires:  pkgconfig(gio-2.0) >= %{glib2_minver}
BuildRequires:  pkgconfig(json-glib-1.0) >= 1.6.2
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(mount)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  systemd-rpm-macros
BuildRequires:  /usr/bin/xsltproc
Requires:       btrfs-progs
%{?systemd_ordering}

%description
Btrfsd is a lightweight daemon that takes care of all Btrfs filesystems
on a Linux system.

It will:

* Check stats for errors and broadcast a warning if any were found
* Perform scrub periodically if system is not on battery
* Run balance (rarely, if system is not on battery)

The daemon is explicitly designed to be run on any system, from a
small notebook to a large storage server. Depending on the system,
it should make the best possible decision for running maintenance jobs,
but may also be tweaked by the user. If no Btrfs filesystems are found,
the daemon will be completely inert.


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install


%check
%meson_test


%preun
%systemd_preun %{name}.timer


%post
%systemd_post %{name}.timer


%postun
%systemd_postun %{name}.timer


%files
%license LICENSE
%doc README.md NEWS.md
%{_libexecdir}/%{name}
%{_mandir}/man8/%{name}.8*
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/settings.conf
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}.timer


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jun 27 2024 Packit <hello@packit.dev> - 0.2.2-1
- Update to version 0.2.2
- Resolves: rhbz#2244228

* Mon Apr 22 2024 Neal Gompa <ngompa@fedoraproject.org> - 0.2.1-1
- Update to 0.2.1

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Sep 24 2023 Neal Gompa <ngompa@fedoraproject.org> - 0.2.0-1
- Update to 0.2.0

* Thu Aug 24 2023 Neal Gompa <ngompa@fedoraproject.org> - 0.1.0-1
- Initial packaging
