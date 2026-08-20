%global girname LangTag
%global girapiversion 0.6
%global soversion 1
%global soversion_gobject 0

Name: liblangtag
Version: 0.6.8
Release: %autorelease
Summary: An interface library to access tags for identifying languages

License: LGPL-3.0-or-later OR MPL-2.0
URL: https://bitbucket.org/tagoh/liblangtag/
Source0: https://bitbucket.org/tagoh/%{name}/downloads/%{name}-%{version}.tar.bz2
Patch0: liblangtag-noparallel-gir.patch

Requires: %{name}-data = %{version}-%{release}

BuildRequires: glibc-common
%if ! 0%{?flatpak}
BuildRequires: gtk-doc
%endif
BuildRequires: pkgconfig(check)
BuildRequires: pkgconfig(gobject-2.0)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: make
BuildRequires: gcc

%description
%{name} is an interface library to access tags for identifying
languages.

Features:
* several subtag registry database supports:
  - language
  - extlang
  - script
  - region
  - variant
  - extension
  - grandfathered
  - redundant
* handling of the language tags
  - parser
  - matching
  - canonicalizing

%package data
Summary: %{name} data files
License: Unicode-DFS-2015
BuildArch: noarch

%description data
The %{name}-data package contains data files for %{name}.

%package gobject
Summary: GObject introspection for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description gobject
The %{name}-gobject package contains files for GObject introspection for
%{name}.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-gobject%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package doc
Summary: Documentation of %{name} API
BuildArch: noarch

%description doc
The %{name}-doc package contains documentation files for %{name}.

%prep
%autosetup -p1

%build
%configure \
%if 0%{?flatpak}
    --disable-gtk-doc \
%endif
    --disable-silent-rules --disable-static --enable-shared --enable-introspection
sed -i \
    -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    libtool
export LD_LIBRARY_PATH=`pwd`/liblangtag/.libs:`pwd`/liblangtag-gobject/.libs${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
%make_build

%install
%make_install
rm -f %{buildroot}/%{_libdir}/*.la %{buildroot}/%{_libdir}/%{name}/*.la

%ldconfig_scriptlets

%ldconfig_scriptlets gobject

%check
export LD_LIBRARY_PATH=`pwd`/liblangtag/.libs:`pwd`/liblangtag-gobject/.libs${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
%make_build check

%files
%doc AUTHORS NEWS README
%{_libdir}/%{name}.so.%{soversion}
%{_libdir}/%{name}.so.%{soversion}.*
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*.so

%files data
%license COPYING
%{_datadir}/%{name}

%files gobject
%{_libdir}/%{name}-gobject.so.%{soversion_gobject}
%{_libdir}/%{name}-gobject.so.%{soversion_gobject}.*
%{_libdir}/girepository-1.0/%{girname}-%{girapiversion}.typelib

%files devel
%{_includedir}/%{name}
%{_libdir}/%{name}.so
%{_libdir}/%{name}-gobject.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/pkgconfig/%{name}-gobject.pc
%{_datadir}/gir-1.0/%{girname}-%{girapiversion}.gir

%files doc
%license COPYING
%{_datadir}/gtk-doc/html/%{name}

%changelog
%autochangelog
