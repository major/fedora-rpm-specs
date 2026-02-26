%global tarball_version %%(echo %{version} | tr '~' '.')
%define major_version %(c=%{version}; echo $c | cut -d. -f1 | cut -d~ -f1)

Name:           d-spy
Version:        50~rc
Release:        %autorelease
Summary:        D-Bus explorer

License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/GNOME/d-spy
Source0:        https://download.gnome.org/sources/d-spy/%{major_version}/d-spy-%{tarball_version}.tar.xz

BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libdex-1)
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/desktop-file-validate

Obsoletes:      d-spy-libs < 48~
Obsoletes:      d-spy-devel < 48~

%description
D-Spy is a tool to explore and test end-points and interfaces on the System or
Session D-Bus. You can also connect to D-Bus peers by address. D-Spy was
originally part of GNOME Builder.


%prep
%autosetup -n d-spy-%{tarball_version} -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang d-spy


%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.gnome.dspy.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.dspy.desktop


%files -f d-spy.lang
%license COPYING
%doc NEWS
%{_bindir}/d-spy
%{_datadir}/applications/org.gnome.dspy.desktop
%{_datadir}/dbus-1/services/org.gnome.dspy.service
%{_datadir}/glib-2.0/schemas/org.gnome.dspy.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.dspy*.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.dspy-symbolic.svg
%{_datadir}/metainfo/org.gnome.dspy.metainfo.xml


%changelog
%autochangelog
