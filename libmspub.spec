%global apiversion 0.1

Name: libmspub
Version: 0.1.4
Release: %autorelease
Summary: A library for import of Microsoft Publisher documents

License: MPL-2.0
URL: http://wiki.documentfoundation.org/DLP/Libraries/libmspub
Source: http://dev-www.libreoffice.org/src/%{name}/%{name}-%{version}.tar.xz

Patch0: gcc10.patch

BuildRequires: boost-devel
BuildRequires: doxygen
BuildRequires: gcc-c++
BuildRequires: help2man
BuildRequires: pkgconfig(icu-i18n)
BuildRequires: pkgconfig(librevenge-0.0)
BuildRequires: pkgconfig(librevenge-generators-0.0)
BuildRequires: pkgconfig(librevenge-stream-0.0)
BuildRequires: pkgconfig(zlib)
BuildRequires: make

%description
Libmspub is library providing ability to interpret and import Microsoft
Publisher content into various applications. You can find it being used
in libreoffice.

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

%package tools
Summary: Tools to transform Microsoft Publisher documents into other formats
Requires: %{name}%{?_isa} = %{version}-%{release}

%description tools
Tools to transform Microsoft Publisher documents into other formats.
Currently supported: XHTML, raw.

%prep
%autosetup -p1

%build
%configure --disable-static --disable-silent-rules
sed -i \
    -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    libtool
%make_build

%install
%make_install
rm -f %{buildroot}/%{_libdir}/*.la
# rhbz#1001245 we install API docs directly from build
rm -rf %{buildroot}/%{_docdir}/%{name}

# generate and install man pages
 export LD_LIBRARY_PATH=%{buildroot}%{_libdir}${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
 for tool in pub2raw pub2xhtml; do
     help2man -N -S '%{name} %{version}' -o ${tool}.1 %{buildroot}%{_bindir}/${tool}
 done
install -m 0755 -d %{buildroot}/%{_mandir}/man1
install -m 0644 pub2*.1 %{buildroot}/%{_mandir}/man1

%ldconfig_scriptlets

%files
%doc AUTHORS NEWS README
%license COPYING.MPL
%{_libdir}/%{name}-%{apiversion}.so.*

%files devel
%doc ChangeLog
%{_includedir}/%{name}-%{apiversion}
%{_libdir}/%{name}-%{apiversion}.so
%{_libdir}/pkgconfig/%{name}-%{apiversion}.pc

%files doc
%license COPYING.MPL
%doc docs/doxygen/html

%files tools
%{_bindir}/pub2raw
%{_bindir}/pub2xhtml
%{_mandir}/man1/pub2raw.1*
%{_mandir}/man1/pub2xhtml.1*

%changelog
%autochangelog
