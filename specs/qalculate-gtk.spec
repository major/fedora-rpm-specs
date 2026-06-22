
# This spec file uses tab uniformly. If you touch this spec, ensure that
# you use tab in your changes.

%global srcnm Qalculate

Summary:	A multi-purpose desktop calculator for GNU/Linux
Name:		qalculate-gtk
Version:	5.11.0
Release:	%autorelease
# The entire source code is GPL-2.0-or-later except:
# GFDL-1.1-or-later
#   doc/C/legal.xml
License:	GPL-2.0-or-later and GFDL-1.1-or-later

%global	forgeurl https://github.com/%{srcnm}/%{name}
%global	tag v%{version}
%forgemeta

URL:		https://qalculate.github.io/
Source0:	%{forgesource}

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	make
BuildRequires:	gcc-c++
BuildRequires:	gtk3-devel
BuildRequires:	libqalculate-devel >= %{version}
BuildRequires:	gettext
BuildRequires:	desktop-file-utils
BuildRequires:	perl(XML::Parser)
BuildRequires:	pkgconfig
BuildRequires:	intltool
BuildRequires:	libappstream-glib
BuildRequires:	mpfr-devel
Requires:	gnuplot

%description
Qalculate! is a multi-purpose desktop calculator for GNU/Linux. It is
small and simple to use but with much power and versatility underneath.
Features include customizable functions, units, arbitrary precision, plotting.
This package provides a (GTK+) graphical interface for Qalculate! 

%prep
%forgeautosetup -p1
autoreconf -fiv
sed -i 's/<i>//' data/qalculate-gtk.appdata.xml.in
sed -i 's/<\/i>//' data/qalculate-gtk.appdata.xml.in

%conf
%configure

%build
%make_build

%install
%make_install

pushd doc
cp -pr html %{buildroot}/%{_datadir}/doc/%{name}
popd

desktop-file-install --delete-original			\
	--remove-category Application			\
	--dir %{buildroot}%{_datadir}/applications	\
	--mode 0644					\
	%{buildroot}%{_datadir}/applications/qalculate-gtk.desktop

appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/*.appdata.xml

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog TODO
%{_pkgdocdir}/html/*
%{_bindir}/qalculate-gtk
%{_datadir}/applications/qalculate-gtk.desktop
%{_datadir}/icons/hicolor/*/*/qalculate*
%{_libexecdir}/qalculate-search-provider
%{_datadir}/dbus-1/services/io.github.Qalculate.SearchProvider.service
%{_datadir}/gnome-shell/search-providers/io.github.Qalculate.search-provider.ini
%{_metainfodir}/%{name}.appdata.xml
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
