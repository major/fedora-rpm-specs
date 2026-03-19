%global glib2_version 2.44
%global gtk3_version 3.20

%global major_minor_version %%(echo %%{version} | cut -d "." -f 1-2)

Name:           gspell
Version:        1.14.3
Release:        %autorelease
Summary:        Spell-checking library for GTK+

License:        LGPL-2.1-or-later
URL:            https://wiki.gnome.org/Projects/gspell
Source0:        https://download.gnome.org/sources/%{name}/%{major_minor_version}/%{name}-%{version}.tar.xz

BuildRequires:  gettext
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  pkgconfig(enchant-2)
BuildRequires:  pkgconfig(glib-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(gtk+-3.0) >= %{gtk3_version}
BuildRequires:  pkgconfig(iso-codes)

Requires:       glib2%{?_isa} >= %{glib2_version}
Requires:       gtk3%{?_isa} >= %{gtk3_version}
Requires:       iso-codes

%description
gspell provides a flexible API to implement the spell checking
in a GTK+ application.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        tests
Summary:        Installed tests for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    tests
The %{name}-tests package contains tests that can be used to verify
the functionality of the installed %{name} package.


%package        doc
Summary:        API documentation for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description    doc
This package contains the full API documentation for %{name}.


%prep
%setup -q


%build
%meson
%meson_build


%install
%meson_install

%find_lang gspell-1


%ldconfig_scriptlets


%files -f gspell-1.lang
%license LICENSES/LGPL-2.1-or-later.txt
%doc NEWS README.md
%{_libdir}/girepository-1.0/
%{_libdir}/libgspell-1.so.3*

%files devel
%{_bindir}/gspell-app1
%{_includedir}/gspell-1/
%{_libdir}/libgspell-1.so
%{_libdir}/pkgconfig/gspell-1.pc
%{_datadir}/gir-1.0/
%{_datadir}/vala/

%files doc
%{_datadir}/gtk-doc/

%files tests
%{_libexecdir}/installed-tests/
%{_datadir}/installed-tests/


%changelog
%autochangelog
