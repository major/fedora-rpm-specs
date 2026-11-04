Name:		log-for-linux
Version:	0.4.0
Release:	%autorelease
Summary:	Native GTK4/libadwaita ham radio logbook for Linux
License:	GPL-3.0-or-later AND MIT
URL:		https://github.com/OK1BR/%{name}
Source:		%{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:	meson
BuildRequires:	ninja-build
BuildRequires:	gtk4-devel
BuildRequires:	libadwaita-devel
BuildRequires:	glib2-devel
BuildRequires:	sqlite-devel
BuildRequires:	libwebsockets-devel
BuildRequires:	gcc
BuildRequires:	desktop-file-utils
BuildRequires:	libappstream-glib
BuildRequires:	hicolor-icon-theme
Requires:	hicolor-icon-theme
Requires:	adwaita-icon-theme

%description
A native GTK4/libadwaita ham radio logbook for Linux.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

desktop-file-validate %{buildroot}%{_datadir}/applications/cz.ok1br.log_for_linux.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/cz.ok1br.log_for_linux.metainfo.xml

# drop redundant license file
rm -f %{buildroot}%{_datadir}/log-for-linux/cty.dat.LICENSE

# unbundle adwaita icons
rm -f %{buildroot}%{_datadir}/log-for-linux/icons/*
rmdir %{buildroot}%{_datadir}/log-for-linux/icons

%check
%meson_test

%files
%doc README.md
#%%doc README.md CONTRIBUTING.md
%license LICENSE data/cty.dat.LICENSE
%{_sbindir}/log-for-linux
%{_datadir}/log-for-linux
%{_datadir}/icons/hicolor/scalable/apps/cz.ok1br.log_for_linux.svg
%{_datadir}/icons/hicolor/symbolic/apps/cz.ok1br.log_for_linux-symbolic.svg
%{_datadir}/applications/cz.ok1br.log_for_linux.desktop
%{_metainfodir}/cz.ok1br.log_for_linux.metainfo.xml

%changelog
%autochangelog
