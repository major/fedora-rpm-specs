%global appname com.github.johnfactotum.Foliate

Name:           foliate
Version:        2.6.4
Release:        %autorelease
Summary:        Simple and modern GTK eBook reader

License:        GPL-3.0-or-later
URL:            https://johnfactotum.github.io/foliate/
Source0:        https://github.com/johnfactotum/foliate/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  meson >= 0.40

BuildRequires:  pkgconfig(gjs-1.0) >= 1.52
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(iso-codes) >= 3.67
BuildRequires:  pkgconfig(webkit2gtk-4.1)

Requires:       gjs
Requires:       hicolor-icon-theme
Requires:       webkit2gtk4.1

# For text-to-speech (TTS) support
Recommends:     espeak-ng

# Support for viewing .mobi, .azw, and .azw3 files
Recommends:     python3 >= 3.4

# Alternative text-to-speech (TTS) engines
Suggests:       espeak
Suggests:       festival

%description
A simple and modern GTK eBook viewer, built with GJS and Epub.js.

%prep
%autosetup -p1
# https://fedoraproject.org/wiki/Changes/Remove_webkit2gtk-4.0_API_Version
# libsoup is not used directly
sed -i -e '/WebKit2/s/4\.0/4.1/' src/main.js
# do not use flatpak-spawn for runtime deps
sed -i -e 's/flatpak-spawn/do-not-use-&/' src/utils.js


%build
%meson
%meson_build


%install
%meson_install

# Ambiguous python shebang
find %{buildroot}%{_datadir}/%{appname}/assets/KindleUnpack/ -type f -name "*.py" -exec sed -e 's@/usr/bin/env python@/usr/bin/python3@g' -i "{}" \;
find %{buildroot}%{_datadir}/%{appname}/assets/KindleUnpack/ -type f -name "mobiml2xhtml.py" -exec sed -e 's@/usr/bin/python@/usr/bin/python3@g' -i "{}" \;

%find_lang %{appname}


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files -f %{appname}.lang
%license COPYING
%doc README.md
%{_bindir}/%{appname}
%{_datadir}/%{appname}/
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/apps/*.svg
%{_metainfodir}/*.xml


%changelog
%autochangelog
