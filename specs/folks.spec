%global folks_module_version 26

Name:           folks
Epoch:          1
Version:        0.15.12
Release:        %autorelease
Summary:        GObject contact aggregation library

License:        LGPL-2.1-or-later
URL:            https://wiki.gnome.org/Projects/Folks
Source0:        https://download.gnome.org/sources/folks/0.15/folks-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gobject-introspection-devel
BuildRequires:  meson
BuildRequires:  python3-dbusmock
BuildRequires:  python3-devel
BuildRequires:  readline-devel
BuildRequires:  telepathy-glib-vala
BuildRequires:  vala
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gee-0.8) >= 0.8.4
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(libedataserver-1.2) >= 3.33.2
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(telepathy-glib)

%description
libfolks is a library that aggregates people from multiple sources (e.g.
Telepathy connection managers and eventually evolution data server,
Facebook, etc.) to create meta-contacts.

%package        telepathy
Summary:        Folks telepathy backend
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description    telepathy
%{name}-telepathy contains the folks telepathy backend.

%package        tools
Summary:        Tools for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description    tools
%{name}-tools contains a database and import tool.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       %{name}-tools%{?_isa} = %{epoch}:%{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS
%{_libdir}/libfolks-dummy.so.26*
%{_libdir}/libfolks-eds.so.26*
%{_libdir}/libfolks.so.26*
%dir %{_libdir}/folks
%dir %{_libdir}/folks/%{folks_module_version}
%dir %{_libdir}/folks/%{folks_module_version}/backends
%{_libdir}/folks/%{folks_module_version}/backends/bluez/
%{_libdir}/folks/%{folks_module_version}/backends/dummy/
%{_libdir}/folks/%{folks_module_version}/backends/eds/
%{_libdir}/folks/%{folks_module_version}/backends/key-file/
%{_libdir}/folks/%{folks_module_version}/backends/ofono/
%{_libdir}/girepository-1.0/Folks-0.7.typelib
%{_libdir}/girepository-1.0/FolksDummy-0.7.typelib
%{_libdir}/girepository-1.0/FolksEds-0.7.typelib
%{_datadir}/GConf/gsettings/folks.convert
%{_datadir}/glib-2.0/schemas/org.freedesktop.folks.gschema.xml

%files telepathy
%{_libdir}/libfolks-telepathy.so.26*
%{_libdir}/folks/%{folks_module_version}/backends/telepathy
%{_libdir}/girepository-1.0/FolksTelepathy-0.7.typelib

%files tools
%{_bindir}/%{name}-import
%{_bindir}/%{name}-inspect

%files devel
%{_includedir}/folks
%{_libdir}/*.so
%{_libdir}/pkgconfig/folks*.pc
%{_datadir}/gir-1.0/Folks-0.7.gir
%{_datadir}/gir-1.0/FolksDummy-0.7.gir
%{_datadir}/gir-1.0/FolksEds-0.7.gir
%{_datadir}/gir-1.0/FolksTelepathy-0.7.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/%{name}*

%changelog
%autochangelog
