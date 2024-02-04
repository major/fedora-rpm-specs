# first two digits of version
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')

Name:           grilo
Version:        0.3.16
Release:        %autorelease
Summary:        Content discovery framework

License:        LGPL-2.1-or-later
URL:            https://wiki.gnome.org/Projects/Grilo
Source0:        https://download.gnome.org/sources/grilo/%{release_version}/grilo-%{version}.tar.xz

BuildRequires:  meson
BuildRequires:  git
BuildRequires:  chrpath
BuildRequires:  gettext
BuildRequires:  vala >= 0.27.1
BuildRequires:  gtk-doc
BuildRequires:  gobject-introspection-devel >= 0.9.0
BuildRequires:  libxml2-devel
BuildRequires:  libsoup3-devel
BuildRequires:  glib2-devel

# For the test UI
BuildRequires:  gtk3-devel
%if 0%{?fedora}
BuildRequires:  liboauth-devel
%endif
BuildRequires:  totem-pl-parser-devel

%description
Grilo is a framework that provides access to different sources of
multimedia content, using a pluggable system.
This package contains the core library and elements.

%package devel
Summary:        Libraries/include files for Grilo framework
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Grilo is a framework that provides access to different sources of
multimedia content, using a pluggable system.
This package contains the core library and elements, as well as
general and API documentation.

%prep
%autosetup -p1 -S git

%build
%meson \
    -Denable-gtk-doc=true

%meson_build

%install
%meson_install

mkdir -p $RPM_BUILD_ROOT%{_libdir}/grilo-%{release_version}/
mkdir -p $RPM_BUILD_ROOT%{_datadir}/grilo-%{release_version}/plugins/

%find_lang grilo

%files -f grilo.lang
%license COPYING
%doc AUTHORS NEWS README.md TODO
%{_libdir}/libgrilo-%{release_version}.so.0*
%{_libdir}/libgrlnet-%{release_version}.so.0*
%{_libdir}/libgrlpls-%{release_version}.so.0*
%{_libdir}/girepository-1.0/
%{_bindir}/grl-inspect-%{release_version}
%{_bindir}/grl-launch-%{release_version}
%{_bindir}/grilo-test-ui-%{release_version}
%{_libdir}/grilo-%{release_version}/
%{_datadir}/grilo-%{release_version}/
%{_mandir}/man1/grilo-test-ui-%{release_version}.1*
%{_mandir}/man1/grl-inspect-%{release_version}.1*
%{_mandir}/man1/grl-launch-%{release_version}.1*

%files devel
%{_datadir}/gtk-doc/html/%{name}
%{_includedir}/%{name}-%{release_version}/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/
%{_datadir}/vala/

%changelog
%autochangelog
