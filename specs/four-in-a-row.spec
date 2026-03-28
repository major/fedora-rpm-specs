Name:           four-in-a-row
Version:        3.38.1
Release:        %autorelease
Summary:        GNOME Four-in-a-row game

License:        GPL-3.0-or-later AND CC-BY-SA-3.0
URL:            https://wiki.gnome.org/Apps/Four-in-a-row
Source0:        https://download.gnome.org/sources/four-in-a-row/3.38/four-in-a-row-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  desktop-file-utils
BuildRequires:  gettext-devel
BuildRequires:  itstool
BuildRequires:  gtk3-devel >= 3.13.2
BuildRequires:  gsound-devel
BuildRequires:  librsvg2-devel
BuildRequires:  meson
BuildRequires:  zlib-devel
BuildRequires:  vala


%description
The objective of Four-in-a-row is to build a line of four of your marbles
while trying to stop your opponent (human or computer) building a line
of his or her own.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name} --all-name --with-gnome


%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.Four-in-a-row.desktop


%files -f %{name}.lang
%license COPYING
%{_bindir}/four-in-a-row
%{_datadir}/metainfo/org.gnome.Four-in-a-row.appdata.xml
%{_datadir}/applications/org.gnome.Four-in-a-row.desktop
%{_datadir}/dbus-1/services/org.gnome.Four-in-a-row.service
%{_datadir}/four-in-a-row
%{_datadir}/glib-2.0/schemas/org.gnome.Four-in-a-row.gschema.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.Four-in-a-row*
%{_mandir}/man6/four-in-a-row.6*


%changelog
%autochangelog
