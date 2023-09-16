Summary: Gamerzilla GObject Introspection Library
Name: gamerzillagobj
Version: 0.1.2
Release: %autorelease
License: zlib
URL: https://github.com/dulsi/gamerzillagobj
Source0: http://www.identicalsoftware.com/gamerzilla/%{name}-%{version}.tgz

BuildRequires: gcc
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  make
BuildRequires: libgamerzilla-devel

%description
GamerzillaGObj is a gobject based introspection library to allow
shell-extensions to use Gamerzilla.

%package devel
Summary:        Development files for GamerzillaGObj

Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development libraries and header files for GamerzillaGObj.

%prep
%setup -q

%build
%make_build

%install
%make_install PREFIX=%{_prefix} LIB=%{_lib}

%files
%license LICENSE
%{_libdir}/libgamerzillagobj.so.0
%{_libdir}/libgamerzillagobj.so.0.0.0
%{_libdir}/girepository-1.0/Gamerzilla-0.1.typelib

%files devel
%{_libdir}/libgamerzillagobj.so
%{_datadir}/gir-1.0/Gamerzilla-0.1.gir

%changelog
%autochangelog
