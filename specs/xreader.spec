# Filter provides from plugins.
%global __provides_exclude_from ^%{_libdir}/%{name}/.*$

Name:		xreader
Version:	4.6.9
Release:	%autorelease
Summary:	Simple document viewer

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		https://github.com/linuxmint/%{name}
Source0:	%{url}/archive/%{version}/%{name}-%{version}.tar.gz

ExcludeArch:    %{ix86}

BuildSystem:   meson
BuildOption(conf): -Ddeprecated_warnings=false
BuildOption(conf): -Ddjvu=true
BuildOption(conf): -Ddvi=true
BuildOption(conf): -Dt1lib=true
BuildOption(conf): -Dpixbuf=true
BuildOption(conf): -Dcomics=true
BuildOption(conf): -Dintrospection=true
BuildOption(conf): -Dhelp_files=true
BuildRequires:	gcc-c++
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	libappstream-glib
BuildRequires:	pkgconfig(ddjvuapi)
BuildRequires:	pkgconfig(gail-3.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gthread-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gtk+-unix-print-3.0)
BuildRequires:	pkgconfig(kpathsea)
BuildRequires:	pkgconfig(libgxps)
BuildRequires:	pkgconfig(libsecret-1)
BuildRequires:	pkgconfig(libspectre)
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(poppler-glib)
BuildRequires:	pkgconfig(sm)
BuildRequires:	pkgconfig(xapp) >= 1.4.0
BuildRequires:	pkgconfig(zlib)
BuildRequires:  python3-packaging
BuildRequires:	texlive
BuildRequires:	t1lib-devel

Requires:	shared-mime-info%{?_isa}
Requires:	gsettings-desktop-schemas%{?_isa}
Requires:	xapps%{?_isa}
Requires:   xapp-symbolic-icons
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

Recommends:	yelp%{?_isa}
Recommends: %{name}-thumbnailer%{?_isa} = %{version}-%{release}

%description
X-Apps Document Reader is a document viewer capable of displaying
multiple and single page document formats like PDF and PostScript.

%package libs
Summary:    xreader document viewer libraries
Requires:	%{name}-data = %{version}-%{release}

%description libs
This package contains the shared library files for %{name}.

%package devel
Summary:	Development files for %{name}
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

%description devel
This package contains the development files for %{name}.


%package doc
Summary:	Documentation files for %{name}
BuildArch:	noarch

%description doc
This package contains the documentation files for %{name}.

%package data
Summary: Support files for the %{name} document viewer
BuildArch: noarch

%description data
This package contains icons and other support files used by the
%{name} application and libraries.

%package thumbnailer
Summary: System thumbnailer using %{name} libraries
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description thumbnailer
This package adds configuration to use %{name} as a thumbnailer.


%prep
%autosetup -p1

%install -a
sed -i -e '/.*<project_group>.*/d' \
	%{buildroot}%{_metainfodir}/%{name}.appdata.xml

%find_lang %{name}

%check
# Validate desktop-files.
%{_bindir}/desktop-file-validate    \
	%{buildroot}%{_datadir}/applications/%{name}.desktop

# Validate AppData-files.
%{_bindir}/appstream-util validate-relax --nonet    \
	%{buildroot}%{_metainfodir}/%{name}.appdata.xml

%ldconfig_scriptlets

%files -f %{name}.lang
%license AUTHORS COPYING debian/copyright
%doc ChangeLog README.md debian/changelog
%{_bindir}/%{name}
%{_bindir}/%{name}-previewer
%{_datadir}/applications/%{name}.desktop
%{_metainfodir}/%{name}.appdata.xml
%{_datadir}/dbus-1/services/*
%{_datadir}/glib-2.0/schemas/*
%{_datadir}/help/*/%{name}/
%{_datadir}/icons/hicolor/*/*/*
%{_libexecdir}/xreaderd
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/%{name}-previewer.1*

%files libs
%{_libdir}/girepository-1.0/*
%{_libdir}/*.so.*
%{_libdir}/%{name}/

%files data
%{_datadir}/%{name}/

%files thumbnailer
%{_bindir}/%{name}-thumbnailer
%{_datadir}/thumbnailers/%{name}.thumbnailer
%{_mandir}/man1/%{name}-thumbnailer.1*

%files devel
%{_datadir}/gir-1.0/*
%{_includedir}/%{name}/
%{_libdir}/*.so
%{_libdir}/pkgconfig/xreader-document-1.5.pc
%{_libdir}/pkgconfig/xreader-view-1.5.pc

%files doc
%license %{_datadir}/licenses/%{name}*
%doc %{_datadir}/doc/%{name}*

%changelog
%autochangelog