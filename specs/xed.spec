# Filter provides from plugins.
%global __provides_exclude_from ^%{_libdir}/%{name}/plugins/.*$

Name:		xed
Version:	3.9.0
Release:	%autorelease
Summary:	X-Apps [Text] Editor (Cross-DE, backward-compatible, GTK3, traditional UI)

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		https://github.com/linuxmint/%{name}
Source0:	%{url}/archive/%{version}/%{name}-%{version}.tar.gz

ExcludeArch:   %{ix86}

BuildSystem:	meson
BuildOption(conf): -Ddocs=true
BuildOption(conf): -Ddeprecated_warnings=false
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	gnome-common
# Required for meson's gnome.generate_gir
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	libappstream-glib
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gspell-1)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gtksourceview-4)
BuildRequires:	pkgconfig(libpeas-gtk-1.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	python3-gobject-devel
BuildRequires:	python3-gobject-base
BuildRequires:	pkgconfig(sm)
BuildRequires:	pkgconfig(xapp) >= 1.4.0
BuildRequires:	python%{python3_pkgversion}-devel

Requires:	iso-codes
Requires:	libpeas1-loader-python3%{?_isa}
Requires:	python%{python3_pkgversion}-gobject%{?_isa}
Requires:	xapps%{?_isa}
Requires:	xapp-symbolic-icons
Suggests:	hunspell-en

%description
Xed is a small, but powerful text editor.  It has most standard text
editor functions and fully supports international text in Unicode.
Advanced features include syntax highlighting and automatic indentation
of source code, printing and editing of multiple documents in one window.

Xed is extensible through a plugin system, which currently includes
support for spell checking, comparing files, viewing CVS ChangeLogs, and
adjusting indentation levels.

%package devel
Summary:	Files needed to develop plugins for %{name}
Requires:	%{name}%{?_isa}	== %{version}-%{release}

%description devel
This package contains files needed to develop plugins for %{name}.

%package doc
Summary:	Documentation files for %{name}
BuildArch:	noarch

%description doc
This package contains the documentation files for %{name}.

%prep
%autosetup -p1

# Use 'classic'-theme by default.
%{__sed} -i -e 's!xed!classic!g' data/org.x.editor.gschema.xml.in

# Make source-files noexec.
%{_bindir}/find . -type f -name '*.c' | %{_bindir}/xargs %{__chmod} -c 0644
%{_bindir}/find . -type f -name '*.h' | %{_bindir}/xargs %{__chmod} -c 0644

%install -a
%{__sed} -i -e '/.*<project_group>.*/d'				\
	%{buildroot}%{_metainfodir}/org.x.editor.metainfo.xml

%find_lang %{name} --with-gnome

%check
# Validate desktop-files.
%{_bindir}/desktop-file-validate				\
	%{buildroot}%{_datadir}/applications/org.x.editor.desktop

# Validate AppData-files.
%{_bindir}/appstream-util validate-relax --nonet		\
	%{buildroot}%{_metainfodir}/org.x.editor.metainfo.xml

%files -f %{name}.lang
%license AUTHORS COPYING debian/copyright
%doc ChangeLog README.md debian/changelog
%exclude %{_datadir}/%{name}/gir-1.0
%exclude %{_datadir}/%{name}/gir-1.0/*
%{_bindir}/%{name}
%{_metainfodir}/org.x.editor.metainfo.xml
%{_datadir}/applications/org.x.editor.desktop
%{_datadir}/dbus-1/services/org.x.editor.*service
%{_datadir}/glib-2.0/schemas/org.x.editor.*gschema.xml
%{_datadir}/gtksourceview-4/styles/xed.xml
%{_datadir}/%{name}/
%{_libdir}/%{name}/
%{_mandir}/man1/%{name}.1*

%files devel
%{_datadir}/%{name}/gir-1.0/
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/%{name}.pc

%files doc
%license %{_datadir}/licenses/%{name}*
%doc %{_datadir}/doc/%{name}*
%doc %{_datadir}/gtk-doc/*

%changelog
%autochangelog