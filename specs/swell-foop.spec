%global tarball_version %%(echo %%{version} | tr '~' '.')
%global major_version %%(echo %%{tarball_version} | cut -d "." -f 1)

Name:           swell-foop
Version:        50.0
Release:        %autorelease
Summary:        GNOME colored tiles puzzle game

License:        GPL-2.0-or-later AND CC-BY-SA-4.0
URL:            https://wiki.gnome.org/Apps/Swell%20Foop
Source0:        https://download.gnome.org/sources/%{name}/%{major_version}/%{name}-%{tarball_version}.tar.xz

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(librsvg-2.0)

BuildRequires:  desktop-file-utils
BuildRequires:  gettext-devel
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  yelp-tools


%description
Clear the screen by removing groups of colored and shaped tiles

%prep
# check for human errors
if [ `echo "%{version}" | grep -cE "\.alpha|\.beta|\.rc"` = "1" ]; then echo "Error: Use tilde in Version field in front of alpha/beta/rc; checked '%{version}'" 1>&2; exit 1; fi

%autosetup -p1 -n %{name}-%{tarball_version}

%build
%meson
%meson_build


%install
%meson_install

%find_lang %{name} --all-name --with-gnome


%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.SwellFoop.desktop


%files -f %{name}.lang
%license COPYING
%doc NEWS
%{_bindir}/swell-foop
%{_datadir}/applications/org.gnome.SwellFoop.desktop
%{_datadir}/dbus-1/services/org.gnome.SwellFoop.service
%{_datadir}/glib-2.0/schemas/org.gnome.SwellFoop.gschema.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.SwellFoop*
%{_datadir}/metainfo/org.gnome.SwellFoop.metainfo.xml


%changelog
%autochangelog
