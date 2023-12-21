%global srcname mail
%global appname io.elementary.mail

%global __provides_exclude_from ^%{_libdir}/%{appname}/webkit2/.*\\.so$

Name:           elementary-mail
Summary:        Mail app designed for elementary
Version:        6.4.0
Release:        %autorelease
License:        GPLv3+

URL:            https://github.com/elementary/mail
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# include upstream patch to fix compilation with vala 0.55+
Patch0:         %{url}/commit/c3aa61d.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(camel-1.2) >= 3.28
BuildRequires:  pkgconfig(folks)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite) >= 6.0.0
BuildRequires:  pkgconfig(libedataserver-1.2) >= 3.28
BuildRequires:  pkgconfig(libedataserverui-1.2) >= 3.28
BuildRequires:  pkgconfig(libhandy-1) >= 1.1.90
BuildRequires:  pkgconfig(webkit2gtk-4.0) >= 2.28
BuildRequires:  pkgconfig(webkit2gtk-web-extension-4.0) >= 2.28

Requires:       hicolor-icon-theme

%description
%{summary}.


%prep
%autosetup -n %{srcname}-%{version} -p1


%build
%meson
%meson_build


%install
%meson_install

# remove @2 scaled icons that aren't properly supported by hicolor-icon-theme:
# * https://github.com/elementary/tasks/issues/321
# * https://gitlab.freedesktop.org/xdg/default-icon-theme/-/issues/2
# * https://bugzilla.redhat.com/show_bug.cgi?id=1537318
# * https://src.fedoraproject.org/rpms/hicolor-icon-theme/pull-request/2
rm -r %{buildroot}/%{_datadir}/icons/hicolor/*@2/

%find_lang %{appname}


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

desktop-file-validate \
    %{buildroot}/%{_sysconfdir}/xdg/autostart/%{appname}-daemon.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f %{appname}.lang
%license COPYING
%doc README.md

%config(noreplace) %{_sysconfdir}/xdg/autostart/%{appname}-daemon.desktop

%{_bindir}/%{appname}

%{_libdir}/%{appname}/

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{appname}.svg
%{_datadir}/metainfo/%{appname}.appdata.xml


%changelog
%autochangelog
