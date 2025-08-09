%global gtksourceview_version 5.3.0
%global libadwaita_version 1.6~beta

%global tarball_version %%(echo %{version} | tr '~' '.')

Name:           gnome-calculator
Version:        49~beta
Release:        %autorelease
Summary:        A desktop calculator

License:        GPL-3.0-or-later AND CC-BY-SA-3.0 AND CC0-1.0
URL:            https://wiki.gnome.org/Apps/Calculator
Source0:        https://download.gnome.org/sources/%{name}/49/%{name}-%{tarball_version}.tar.xz

BuildRequires:  blueprint-compiler
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  itstool
BuildRequires:  libmpc-devel
BuildRequires:  meson
BuildRequires:  mpfr-devel
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gtksourceview-5) >= %{gtksourceview_version}
BuildRequires:  pkgconfig(libadwaita-1) >= %{libadwaita_version}
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  vala
BuildRequires:  /usr/bin/appstream-util

Requires:       gtksourceview5%{?_isa} >= %{gtksourceview_version}
Requires:       libadwaita%{?_isa} >= %{libadwaita_version}

%description
gnome-calculator is a powerful graphical calculator with financial,
logical and scientific modes. It uses a multiple precision package
to do its arithmetic to give a high degree of accuracy.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1 -n %{name}-%{tarball_version}


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{name} --with-gnome --all-name


%check
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/org.gnome.Calculator.metainfo.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.gnome.Calculator.desktop


%files -f %{name}.lang
%doc NEWS README.md
%license COPYING
%{_bindir}/gcalccmd
%{_bindir}/gnome-calculator
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/GCalc-2.typelib
%{_libdir}/girepository-1.0/GCi-1.typelib
%{_libdir}/libgcalc-2.so.1*
%{_libdir}/libgci-1.so.0*
%{_libexecdir}/gnome-calculator-search-provider
%{_datadir}/applications/org.gnome.Calculator.desktop
%{_datadir}/dbus-1/services/org.gnome.Calculator.SearchProvider.service
%{_datadir}/glib-2.0/schemas/org.gnome.calculator.gschema.xml
%{_datadir}/gnome-shell/
%{_datadir}/icons/hicolor/*/apps/org.gnome.Calculator.*
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Calculator-symbolic.svg
%{_metainfodir}/org.gnome.Calculator.metainfo.xml
%{_mandir}/man1/gnome-calculator.1*
%{_mandir}/man1/gcalccmd.1*

%files devel
%{_includedir}/gci-2/
%{_includedir}/gcalc-2/
%{_libdir}/libgcalc-2.so
%{_libdir}/libgci-1.so
%{_libdir}/pkgconfig/gcalc-2.pc
%{_libdir}/pkgconfig/gci-1.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/GCalc-2.gir
%{_datadir}/gir-1.0/GCi-1.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/gcalc-2.deps
%{_datadir}/vala/vapi/gcalc-2.vapi
%{_datadir}/vala/vapi/gci-1.deps
%{_datadir}/vala/vapi/gci-1.vapi


%changelog
%autochangelog
