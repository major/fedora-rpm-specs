Name:           pogo
Version:        1.0.1
Release:        %autorelease
Summary:        Probably the simplest and fastest audio player for Linux
Summary(de):    Möglicherweise der einfachste und schnellste Audioplayer für Linux

License:        GPL-2.0-or-later
URL:            https://github.com/jendrikseipp/pogo
Source:         https://github.com/jendrikseipp/%{name}/archive/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  python3-devel

Requires:       python3-dbus
Requires:       python3-gobject
Requires:       python3-gstreamer1
Requires:       python3-inotify
Requires:       python3-mutagen
Requires:       python3-pillow

Provides:       pogo-zeitgeist = %{version}-%{release}
Obsoletes:      pogo-zeitgeist < %{version}

%description
Pogo's elementary-inspired design uses the screen-space very efficiently. It is
especially well-suited for people who organize their music by albums on the
hard drive. The main interface components are a directory tree and a playlist
that groups albums in an innovative way.
Pogo is a fork of Decibel Audio Player.

%description -l de
Das Elementary-inspirierte Design von Pogo nutzt den Platz auf dem Bildschirm
effizient. Es richtet sich speziell an Benutzer, die Ihre Musik nach Alben
auf der Festplatte verwalten. Die Hauptkomponenten der Benutzeroberfläche
sind ein Ordnerbaum und eine Wiedergabeliste, die Alben auf innovative
Weise gruppiert.
Pogo ist ein Fork des Decibel Audio Players.

%prep
%autosetup
# Remove shebang from __main__.py
sed -i '1{/^#!/d}' pogo/__main__.py

%build
#nothing to build

%install
%make_install

%find_lang %{name}

# AppData / MetaInfo
install -D -p -m644 %{name}.appdata.xml %{buildroot}%{_metainfodir}/%{name}.metainfo.xml

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.metainfo.xml

%files -f %{name}.lang
%license LICENSE.txt
%doc README.md NEWS.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/
%{_datadir}/pixmaps/%{name}.png
%{_metainfodir}/%{name}.metainfo.xml
%{_mandir}/man1/%{name}.1.*

%changelog
%autochangelog
