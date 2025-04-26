%global app_id  com.github.tchx84.Flatseal

Name:           flatseal
Version:        2.3.1
Release:        %autorelease
Summary:        Manage Flatpak permissions

License:        GPL-3.0-or-later
URL:            https://github.com/tchx84/Flatseal
Source:         %{url}/archive/v%{version}/Flatseal-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  gjs
BuildRequires:  pkgconfig(appstream) >= 1.0
BuildRequires:  pkgconfig(libadwaita-1) >= 1.5
BuildRequires:  pkgconfig(webkitgtk-6.0) >= 2.40
BuildRequires:  meson >= 0.59.0
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

Requires:       gjs
# loaded by imports.gi
Requires:       appstream >= 1.0
Requires:       gtk4
Requires:       libadwaita >= 1.5
Requires:       webkitgtk6.0 >= 2.40

BuildArch:      noarch

%description
Flatseal is a graphical utility to review and modify permissions from your
Flatpak applications.


%prep
%autosetup -n Flatseal-%{version} -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{name} --with-gnome


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{app_id}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/%{app_id}.appdata.xml


%files -f %{name}.lang
%license COPYING
%doc CHANGELOG.md DOCUMENTATION.md README.md
%{_bindir}/%{app_id}
%{_datadir}/%{name}
%{_datadir}/appdata/%{app_id}.appdata.xml
%{_datadir}/applications/%{app_id}.desktop
%{_datadir}/glib-2.0/schemas/%{app_id}*
%{_datadir}/icons/hicolor/*/*/%{app_id}*


%changelog
%autochangelog
