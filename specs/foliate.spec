%global appid com.github.johnfactotum.Foliate
%global libadwaita_version 1.7
%global webkitgtk_version 2.40.1

# Git submodules
#   * foliate-js
%global commit1 052123beafed921a9a2a45ef6330c235289a634e
%global shortcommit1 %(c=%{commit1}; echo ${c:0:7})

Name:           foliate
Version:        3.3.0
Release:        %autorelease
Summary:        Simple and modern GTK eBook reader

License:        GPL-3.0-or-later
URL:            https://johnfactotum.github.io/foliate/
Source0:        https://github.com/johnfactotum/foliate/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/johnfactotum/foliate-js/archive/%{commit1}/%{name}-js-%{shortcommit1}.tar.gz

BuildArch:      noarch

BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  meson >= 0.59
BuildRequires:  pkgconfig(gjs-1.0) >= 1.76
BuildRequires:  pkgconfig(gtk4) >= 4.12
BuildRequires:  pkgconfig(iso-codes) >= 3.67
BuildRequires:  pkgconfig(libadwaita-1) >= %{libadwaita_version}
BuildRequires:  pkgconfig(webkitgtk-6.0) >= %{webkitgtk_version}

Requires:       gjs >= 1.76
Requires:       hicolor-icon-theme
Requires:       libadwaita >= %{libadwaita_version}
Requires:       webkitgtk6.0 >= %{webkitgtk_version}

# For text-to-speech (TTS) support
Recommends:     espeak-ng

# Support for viewing .mobi, .azw, and .azw3 files
Recommends:     python3 >= 3.4

# Alternative text-to-speech (TTS) engines
Suggests:       espeak
Suggests:       festival

Provides:       bundled(%{name}-js) = 0~git%{shortcommit1}

%description
A simple and modern GTK eBook viewer, built with GJS and Epub.js.


%prep
%autosetup -p1
%autosetup -p1 -a1
mv %{name}-js-%{commit1}/* src/%{name}-js


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{appid}


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
# https://github.com/johnfactotum/foliate/issues/1111
%dnl desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files -f %{appid}.lang
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_datadir}/%{appid}/
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/apps/*.svg
%{_metainfodir}/*.xml


%changelog
%autochangelog
