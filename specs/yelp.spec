%global libhandy_version 1.5.0

%global tarball_version %%(echo %{version} | tr '~' '.')

Name:          yelp
Epoch:         2
Version:       49~rc
Release:       %autorelease
Summary:       Help browser for the GNOME desktop

# Automatically converted from old format: LGPLv2+ and ASL 2.0 and GPLv2+ - review is highly recommended.
License:       LicenseRef-Callaway-LGPLv2+ AND Apache-2.0 AND GPL-2.0-or-later
URL:           https://wiki.gnome.org/Apps/Yelp
Source:        https://download.gnome.org/sources/%{name}/49/%{name}-%{tarball_version}.tar.xz

BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(liblzma)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(libexslt)
BuildRequires: pkgconfig(libxslt)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(webkitgtk-6.0)
BuildRequires: pkgconfig(yelp-xsl)
BuildRequires: desktop-file-utils
BuildRequires: bzip2-devel
BuildRequires: gcc
BuildRequires: gettext-devel
BuildRequires: itstool
BuildRequires: meson
Requires:      yelp-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:      yelp-xsl

%description
Yelp is the help browser for the GNOME desktop. It is designed
to help you browse all the documentation on your system in
one central tool, including traditional man pages, info pages and
documentation written in DocBook.

%package libs
Summary: Libraries for yelp

%description libs
This package contains libraries used by the yelp help browser.

%package devel
Summary: Development files for yelp-libs
Requires: %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}

%description devel
This package contains header files for the libraries in the yelp-libs package.

%prep
%autosetup -p1 -n %{name}-%{tarball_version}

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name}

%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.Yelp.desktop

%files -f %{name}.lang
%doc AUTHORS NEWS README.md
%license COPYING
%{_bindir}/*
%{_datadir}/applications/org.gnome.Yelp.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.yelp.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Yelp.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Yelp-symbolic.svg
%{_datadir}/metainfo/org.gnome.Yelp.metainfo.xml
%{_datadir}/yelp/
%{_datadir}/yelp-xsl/xslt/common/domains/yelp.xml

%files libs
%{_libdir}/libyelp-1.so.0{,.*}
%dir %{_libdir}/yelp-1
%dir %{_libdir}/yelp-1/web-process-extensions
%{_libdir}/yelp-1/web-process-extensions/libyelpwebprocessextension.so

%files devel
%{_libdir}/pkgconfig/libyelp-1.pc
%{_libdir}/libyelp-1.so
%{_includedir}/libyelp-1


%changelog
%autochangelog
