%global tarball_version %%(echo %%{version} | tr '~' '.')
%global major_version %%(echo %%{tarball_version} | cut -d "." -f 1)

Name:           tali
Version:        40.9
Release:        %autorelease
Summary:        GNOME Tali game

License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND CC0-1.0
URL:            https://wiki.gnome.org/Apps/Tali
Source0:        https://download.gnome.org/sources/%{name}/%{major_version}/%{name}-%{tarball_version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libgnome-games-support-1)

%description
Sort of poker with dice and less money. An ancient Roman game.

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
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/*.desktop

%files -f %{name}.lang
%doc NEWS
%license COPYING
%{_bindir}/tali
%{_datadir}/applications/org.gnome.Tali.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.Tali.gschema.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.Tali.*
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Tali-symbolic.svg
%{_datadir}/metainfo/org.gnome.Tali.appdata.xml
%{_datadir}/tali/
%{_mandir}/man6/tali.6*


%changelog
%autochangelog
