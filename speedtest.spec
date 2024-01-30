%global forgeurl https://github.com/Ketok4321/%{name}

%global rdnsappid xyz.ketok.Speedtest

Name:           speedtest
Version:        1.3.0
Release:        %autorelease
Summary:        A graphical librespeed client written using gtk4 + libadwaita

%forgemeta

License:        GPL-3.0-or-later
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildArch:      noarch

BuildRequires:  blueprint-compiler >= 0.10.0
BuildRequires:  desktop-file-utils
BuildRequires:  git-core
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  meson >= 0.62.0
BuildRequires:  python3-devel

BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(aiohttp)

BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)

Requires:       hicolor-icon-theme
Requires:       libadwaita
Requires:       python3-gobject
Requires:       python3dist(aiohttp)

%description
%{summary}


%prep
%forgeautosetup -p1


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{name}


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files -f %{name}.lang
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.svg
%{_metainfodir}/*.xml


%changelog
%autochangelog
