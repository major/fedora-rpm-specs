%global uuid com.github.maoschanz.%{name}

Name: drawing
Version: 1.0.2
Release: %autorelease
Summary: Simple image editor for Linux
BuildArch: noarch

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License: GPL-3.0-or-later
URL: https://github.com/maoschanz/drawing
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: desktop-file-utils
BuildRequires: itstool
BuildRequires: libappstream-glib
BuildRequires: meson >= 0.50.0
BuildRequires: python3-cairo
BuildRequires: python3-devel
BuildRequires: python3-gobject

BuildRequires: pkgconfig(gtk+-3.0)

Requires: gtk3
Requires: hicolor-icon-theme
Requires: python3-cairo
Requires: python3-gobject

%description
This simple image editor, similar to Microsoft Paint, is aiming at the GNOME
desktop.

PNG, JPEG and BMP files are supported.

Besides GNOME, the app is well integrated in traditional-looking desktops, as
well as elementaryOS.

It should also be compatible with the Pinephone and Librem 5 smartphones.


%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{name} --with-gnome


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files -f %{name}.lang
%license LICENSE
%doc README.md CONTRIBUTING.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/icons/hicolor/scalable/*/*.svg
%{_metainfodir}/*.xml


%changelog
%autochangelog
