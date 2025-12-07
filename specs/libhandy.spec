%bcond glade %[!(0%{?rhel} >= 10)]

Name:           libhandy
Version:        1.8.3
Release:        %autorelease
Summary:        Building blocks for modern adaptive GNOME apps
License:        LGPL-2.1-or-later

URL:            https://gitlab.gnome.org/GNOME/libhandy
%global majmin %(echo %{version} | cut -d . -f -2)
Source0:        https://download.gnome.org/sources/%{name}/%{majmin}/%{name}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  gi-docgen
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  pkgconfig(gio-2.0)
%if %{with glade}
BuildRequires:  pkgconfig(gladeui-2.0)
%endif
BuildRequires:  pkgconfig(glib-2.0) >= 2.44
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.24.1
# Support graphical tests in non-graphical environment
BuildRequires:  xwayland-run
BuildRequires:  mesa-dri-drivers
BuildRequires:  mutter
BuildRequires:  rsvg-pixbuf-loader

# Retired in F34
Obsoletes:      libhandy1 < 1.1.90-2
Conflicts:      libhandy1 < 1.1.90-2
Provides:       libhandy1 = %{version}-%{release}
Provides:       libhandy1%{?_isa} = %{version}-%{release}

%description
libhandy provides GTK+ widgets and GObjects to ease developing
applications for mobile phones.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
# Because web fonts from upstream are not bundled in the gi-docgen package,
# packages containing documentation generated with gi-docgen should depend on
# this metapackage to ensure the proper system fonts are present.
Recommends:     gi-docgen-fonts
# Retired in F34
Obsoletes:      libhandy1-devel < 1.1.90-2
Conflicts:      libhandy1-devel < 1.1.90-2
Provides:       libhandy1-devel = %{version}-%{release}
Provides:       libhandy1-devel%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1


%build
%meson -Dgtk_doc=true -Dexamples=false \
%if %{without glade}
    -Dglade_catalog=disabled \
%endif
    %{nil}
%meson_build


%install
%meson_install

%find_lang libhandy


%check
export NO_AT_BRIDGE=1
%{shrink:xwfb-run -c mutter -- %meson_test}


%files -f libhandy.lang
%license COPYING
%doc AUTHORS HACKING.md NEWS README.md
%{_libdir}/girepository-1.0/
%{_libdir}/libhandy-1.so.0

%files devel
%{_includedir}/libhandy-1/
%{_libdir}/libhandy-1.so
%{_libdir}/pkgconfig/libhandy-1.pc
%{_datadir}/gir-1.0/
%if %{with glade}
%{_libdir}/glade/
%{_datadir}/glade/
%endif
%doc %{_datadir}/doc/libhandy-1/
%{_datadir}/vala/


%changelog
%autochangelog
