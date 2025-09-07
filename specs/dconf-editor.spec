%global dconf_version 0.26.1
%global glib2_version 2.56.0
%global gtk3_version 3.22.27

%global tarball_version %%(echo %{version} | tr '~' '.')

Name:           dconf-editor
Version:        49~rc
Release:        %autorelease
Summary:        Configuration editor for dconf

License:        GPL-3.0-or-later AND CC0-1.0
URL:            https://wiki.gnome.org/Projects/dconf
Source0:        https://download.gnome.org/sources/dconf-editor/49/dconf-editor-%{tarball_version}.tar.xz
Source1:        https://raw.githubusercontent.com/flathub/ca.desrt.dconf-editor/master/start-dconf-editor.sh

BuildRequires:  /usr/bin/appstream-util
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  pkgconfig(dconf) >= %{dconf_version}
BuildRequires:  pkgconfig(glib-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= %{gtk3_version}
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  vala

Requires:       dconf%{?_isa} >= %{dconf_version}
Requires:       glib2%{?_isa} >= %{glib2_version}
Requires:       gtk3%{?_isa} >= %{gtk3_version}

%description
Graphical tool for editing the dconf configuration database.

%prep
%autosetup -p1 -n %{name}-%{tarball_version}

%build
%meson
%meson_build

%install
%meson_install

%if 0%{?flatpak}
install -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/start-dconf-editor
%endif

%find_lang dconf-editor

%check
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_datadir}/metainfo/ca.desrt.dconf-editor.metainfo.xml
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/ca.desrt.dconf-editor.desktop

%files -f dconf-editor.lang
%license COPYING
%{_bindir}/dconf-editor
%if 0%{?flatpak}
%{_bindir}/start-dconf-editor
%endif
%{_datadir}/applications/ca.desrt.dconf-editor.desktop
%{_datadir}/bash-completion/
%{_datadir}/dbus-1/services/ca.desrt.dconf-editor.service
%{_datadir}/glib-2.0/schemas/ca.desrt.dconf-editor.gschema.xml
%{_datadir}/icons/hicolor/scalable/actions/ca.desrt.dconf-editor.big-rows-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/ca.desrt.dconf-editor.small-rows-symbolic.svg
%{_datadir}/icons/hicolor/scalable/apps/ca.desrt.dconf-editor.Devel.svg
%{_datadir}/icons/hicolor/scalable/apps/ca.desrt.dconf-editor.svg
%{_datadir}/icons/hicolor/symbolic/apps/ca.desrt.dconf-editor-symbolic.svg
%{_datadir}/metainfo/ca.desrt.dconf-editor.metainfo.xml
%{_mandir}/man1/dconf-editor.1*

%changelog
%autochangelog
