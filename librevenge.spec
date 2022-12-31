%global apiversion 0.0

Name: librevenge
Version: 0.0.5
Release: %autorelease
Summary: A base library for writing document import filters

# src/lib/RVNGOLEStream.{h,cpp} are BSD
License: ( LGPL-2.1-or-later OR MPL-2.0 ) AND BSD-3-Clause
URL: http://sourceforge.net/p/libwpd/wiki/librevenge/
Source: http://downloads.sourceforge.net/libwpd/%{name}-%{version}.tar.xz

BuildRequires: boost-devel
BuildRequires: doxygen
BuildRequires: gcc-c++
BuildRequires: pkgconfig(cppunit)
BuildRequires: pkgconfig(zlib)
BuildRequires: python3-devel
BuildRequires: make

%description
%{name} is a base library for writing document import filters. It has
interfaces for text documents, vector graphics, spreadsheets and
presentations.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package doc
Summary: Documentation of %{name} API
BuildArch: noarch

%description doc
The %{name}-doc package contains documentation files for %{name}.

%if ! 0%{?flatpak}
%package gdb
Summary: gdb pretty printers for %{name}
Requires: gdb
Requires: python3-six
Requires: %{name}%{?_isa} = %{version}-%{release}
Supplements: %{name}-debuginfo%{?_isa} = %{version}-%{release}

%description gdb
The %{name}-devel package contains gdb pretty printers that help with
debugging applications that use %{name}.
%endif

%prep
%autosetup -p1

%build
%configure \
    --disable-silent-rules \
    --disable-static \
%if ! 0%{?flatpak}
    --enable-pretty-printers
%endif

sed -i \
    -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    libtool
%make_build

%install
%make_install

rm -f %{buildroot}%{_libdir}/*.la
# we install API docs directly from build
rm -rf %{buildroot}%{_docdir}/%{name}

%py_byte_compile %{python3} %{buildroot}%{_datadir}

%ldconfig_scriptlets

%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
%make_build check

%files
%license COPYING.*
%doc README NEWS
%{_libdir}/%{name}-%{apiversion}.so.*
%{_libdir}/%{name}-generators-%{apiversion}.so.*
%{_libdir}/%{name}-stream-%{apiversion}.so.*

%files devel
%doc ChangeLog
%{_includedir}/%{name}-%{apiversion}
%{_libdir}/%{name}-%{apiversion}.so
%{_libdir}/%{name}-generators-%{apiversion}.so
%{_libdir}/%{name}-stream-%{apiversion}.so
%{_libdir}/pkgconfig/%{name}-%{apiversion}.pc
%{_libdir}/pkgconfig/%{name}-generators-%{apiversion}.pc
%{_libdir}/pkgconfig/%{name}-stream-%{apiversion}.pc

%files doc
%license COPYING.*
%doc docs/doxygen/html

%if ! 0%{?flatpak}
%files gdb
%{_datadir}/gdb/auto-load%{_libdir}/%{name}-%{apiversion}-gdb.py*
%{_datadir}/gdb/auto-load%{_libdir}/%{name}-stream-%{apiversion}-gdb.py*
%{_datadir}/gdb/auto-load%{_libdir}/__pycache__
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/python
%endif

%changelog
%autochangelog
