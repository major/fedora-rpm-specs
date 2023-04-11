%{?mingw_package_header}
%define pkgname json-glib
%define glib2_version 2.54.0

Name:           mingw-%{pkgname}
Version:        1.6.6
Release:        %autorelease
Summary:        MinGW compiled library for JavaScript Object Notation format

License:        LGPL-2.1-or-later
URL:            https://wiki.gnome.org/Projects/JsonGlib
Source0:        https://download.gnome.org/sources/%{pkgname}/1.6/%{pkgname}-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  gettext

BuildRequires:  mingw32-filesystem >= 104
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-glib2 >= %{glib2_version}
#BuildRequires:  mingw32-gobject-introspection

BuildRequires:  mingw64-filesystem >= 104
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-glib2 >= %{glib2_version}
#BuildRequires:  mingw64-gobject-introspection

%description
%{name} is a library providing serialization and deserialization support
for the JavaScript Object Notation (JSON) format, compiled using MinGW.


# Win32
%package -n mingw32-%{pkgname}
Summary:       MinGW compiled %{pkgname} library for the Win32 target

%description -n mingw32-%{pkgname}
MinGW compiled %{pkgname} library for the Win32 target.


# Win64
%package -n mingw64-%{pkgname}
Summary:       MinGW compiled %{pkgname} library for the Win64 target

%description -n mingw64-%{pkgname}
MinGW compiled %{pkgname} library for the Win64 target.


%{?mingw_debug_package}


%prep
%setup -q -n %{pkgname}-%{version}


%build
%mingw_meson -Dintrospection=disabled
%mingw_ninja


%install
export DESTDIR=%{buildroot}
%mingw_ninja install

%mingw_find_lang json-glib-1.0


# Win32
%files -n mingw32-%{pkgname} -f mingw32-json-glib-1.0.lang
%license COPYING
%{mingw32_bindir}/json-glib-format.exe
%{mingw32_bindir}/json-glib-validate.exe
%{mingw32_bindir}/lib%{pkgname}*.dll
%{mingw32_includedir}/%{pkgname}-1.0/
%{mingw32_libdir}/lib%{pkgname}*.dll.a
#{mingw32_libdir}/girepository-1.0/Json-1.0.typelib
%{mingw32_libdir}/pkgconfig/%{pkgname}-1.0.pc
#{mingw32_datadir}/gir-1.0/Json-1.0.gir
%{mingw32_libexecdir}/installed-tests/
%{mingw32_datadir}/installed-tests/


# Win64
%files -n mingw64-%{pkgname} -f mingw64-json-glib-1.0.lang
%license COPYING
%{mingw64_bindir}/json-glib-format.exe
%{mingw64_bindir}/json-glib-validate.exe
%{mingw64_bindir}/lib%{pkgname}*.dll
%{mingw64_includedir}/%{pkgname}-1.0/
%{mingw64_libdir}/lib%{pkgname}*.dll.a
#{mingw64_libdir}/girepository-1.0/Json-1.0.typelib
%{mingw64_libdir}/pkgconfig/%{pkgname}-1.0.pc
#{mingw64_datadir}/gir-1.0/Json-1.0.gir
%{mingw64_libexecdir}/installed-tests/
%{mingw64_datadir}/installed-tests/


%changelog
%autochangelog
