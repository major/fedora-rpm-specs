Name:		glabels
Version:	3.4.1
Release:	26%{?dist}
Summary:	A program for creating labels and business cards for GNOME
License:	GPL-3.0-or-later AND LGPL-3.0-or-later AND CC-BY-NC-SA-3.0 AND X11
URL:		https://www.glabels.org
Source0:	https://download.gnome.org/sources/glabels/3.4/glabels-%{version}.tar.xz
Patch01:	glabels-externs.patch
Patch02:	incompatible-pointer-types.patch
Patch03:	xml2-changes.patch

BuildRequires:	autoconf automake
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	libappstream-glib
BuildRequires:	libtool
BuildRequires:	make
BuildRequires:	yelp-tools

## TODO: GNU Barcode unfortunately only provides a static library at this
## If/when Barcode provides a shared library in the future, we'll
## use that package here instead of barcode-static.
BuildRequires:	barcode-static
%if ! 0%{?flatpak}
BuildRequires:	pkgconfig(libebook-1.2) >= 3.45.1
%endif
BuildRequires:	pkgconfig(glib-2.0) >= 2.42.0
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.14.0
BuildRequires:	pkgconfig(libxml-2.0) >= 2.9.0
BuildRequires:	pkgconfig(librsvg-2.0) >= 2.39.0
BuildRequires:	pkgconfig(libiec16022) >= 0.2.4
BuildRequires:	pkgconfig(libqrencode) >= 3.1.0
# https://github.com/jimevins/glabels/issues/60
#BuildRequires:	zint-devel < 2.7.0

Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
Requires:	%{name}-templates = %{version}-%{release}
Obsoletes:	%{name}-doc < 3.4.1-20


%description
gLabels is a lightweight program for creating labels and
business cards for the GNOME desktop environment.
It is designed to work with various laser/ink-jet peel-off
label and business card sheets that you'll find at most office
supply stores.


%package	devel
Summary:	Development files and documentation for %{name}
License:	LGPL-3.0-or-later
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

%description	devel
This package contains the header files and development documentation for
libglabels. 


%package 	libs
License:	LGPL-3.0-or-later
Summary:	Development files and documentation for %{name}
Requires:	%{name}-templates = %{version}-%{release}

%description	libs
This package contains the shared libraries for %{name}. 


%package 	templates
License:	MIT
Summary:	The %{name} template database 
BuildArch:	noarch

%description	templates
This package contains the template database for %{name}.


%prep
%autosetup -p1
autoreconf -fiv


%build
%configure --enable-gtk-doc --disable-static
%make_build


%install
%make_install

%if 0%{?rhel} && 0%{?rhel} < 10
find %{buildroot}%{_libdir} -name '*.la' -delete
%endif

desktop-file-validate %{buildroot}%{_datadir}/applications/glabels-3.0.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/glabels-3.appdata.xml

%find_lang glabels-3.0


%files -f glabels-3.0.lang
%doc AUTHORS ChangeLog NEWS README TODO
%license COPYING COPYING.README_FIRST COPYING-DOCS
%{_bindir}/glabels-3*
%{_datadir}/appdata/glabels-3.appdata.xml
%{_datadir}/applications/*glabels-3.0.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.glabels-3.gschema.xml
%doc %{_datadir}/help/*/glabels-3.0/
%{_datadir}/icons/hicolor/*/apps/glabels-3.0.*
%{_datadir}/icons/hicolor/*/mimetypes/application-x-glabels.*
%{_datadir}/mime/packages/glabels-3.0.xml
%{_mandir}/man?/glabels-3*

%files	devel
%doc AUTHORS
%license COPYING-DOCS COPYING-LIBS
%{_includedir}/libglabels-3.0/
%{_includedir}/libglbarcode-3.0/
%{_libdir}/libglabels-3.0.so
%{_libdir}/libglbarcode-3.0.so
%{_libdir}/pkgconfig/libglabels-3.0.pc
%{_libdir}/pkgconfig/libglbarcode-3.0.pc
%{_datadir}/gtk-doc/html/libglabels-3.0/
%{_datadir}/gtk-doc/html/libglbarcode-3.0/

%files	libs
%doc AUTHORS
%license COPYING-LIBS
%{_datadir}/glabels-3.0/
%{_libdir}/libglabels-3.0.so.*
%{_libdir}/libglbarcode-3.0.so.*

%files templates
%doc AUTHORS
%license COPYING-TEMPLATES
%dir %{_datadir}/libglabels-3.0/
%{_datadir}/libglabels-3.0/dtd/
%{_datadir}/libglabels-3.0/templates/


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

%autochangelog
