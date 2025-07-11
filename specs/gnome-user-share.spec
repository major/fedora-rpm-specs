%global tarball_version %%(echo %{version} | tr '~' '.')

Name:           gnome-user-share
Version:        48.1
Release:        1%{?dist}
Summary:        Gnome user file sharing

# * gnome-tour source code is GPL-2.0-or-later
# * rust crate dependencies are:
# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# Apache-2.0 OR MIT
# MIT
# MIT OR Apache-2.0
# Unlicense OR MIT
License:        GPL-2.0-or-later AND MIT AND Unicode-DFS-2016 AND (Apache-2.0 OR MIT) AND (Unlicense OR MIT)
# LICENSE.dependencies contains a full license breakdown

URL:            https://gitlab.gnome.org/GNOME/gnome-user-share
Source0:        http://download.gnome.org/sources/%{name}/48/%{name}-%{tarball_version}.tar.xz

BuildRequires:  cargo-rpm-macros
BuildRequires:  clang
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  systemd-rpm-macros

BuildRequires:  httpd
BuildRequires:  mod_dnssd
BuildRequires:  systemd-devel
BuildRequires:  pkgconfig(libselinux)

Requires:       httpd
Requires:       mod_dnssd

%description
gnome-user-share is a small package that binds together various free
software projects to bring easy to use user-level file sharing to the
masses.

The program is meant to run in the background when the user is logged
in, and when file sharing is enabled a webdav server is started that
shares the $HOME/Public folder. The share is then published to all
computers on the local network using mDNS/rendezvous, so that it shows
up in the Network location in GNOME.

%prep
%autosetup -p1 -n %{name}-%{tarball_version}
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires -a

%build
%meson
%meson_build
%{cargo_license_summary -a}
%{cargo_license -a} > LICENSE.dependencies

%install
%meson_install

%find_lang gnome-user-share --with-gnome

%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/gnome-user-share-webdav.desktop

%post
%systemd_user_post gnome-user-share-webdav.service

%preun
%systemd_user_preun gnome-user-share-webdav.service

%postun
%systemd_user_postun_with_restart gnome-user-share-webdav.service

%files -f gnome-user-share.lang
%license COPYING
%license LICENSE.dependencies
%doc README.md NEWS
%{_libexecdir}/gnome-user-share-webdav
%{_datadir}/GConf/gsettings/gnome-user-share.convert
%{_datadir}/applications/gnome-user-share-webdav.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.file-sharing.gschema.xml
%{_datadir}/gnome-user-share/
%{_userunitdir}/gnome-user-share-webdav.service

%changelog
%autochangelog
