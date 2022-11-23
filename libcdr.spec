%global apiversion 0.1

Name: libcdr
Version: 0.1.7
Release: %autorelease
Summary: A library for import of CorelDRAW drawings

# the only Public Domain source is src/lib/CDRColorProfiles.h
License: MPL-2.0 AND LicenseRef-Fedora-Public-Domain
URL: http://wiki.documentfoundation.org/DLP/Libraries/libcdr
Source: http://dev-www.libreoffice.org/src/%{name}/%{name}-%{version}.tar.xz

BuildRequires: boost-devel
BuildRequires: doxygen
BuildRequires: gcc-c++
BuildRequires: help2man
BuildRequires: make
BuildRequires: pkgconfig(cppunit)
BuildRequires: pkgconfig(icu-i18n)
BuildRequires: pkgconfig(lcms2)
BuildRequires: pkgconfig(librevenge-0.0)
BuildRequires: pkgconfig(librevenge-generators-0.0)
BuildRequires: pkgconfig(librevenge-stream-0.0)
BuildRequires: pkgconfig(zlib)

%description
Libcdr is library providing ability to interpret and import CorelDRAW
drawings into various applications. You can find it being used in
libreoffice.

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
Summary: Tools to transform CorelDRAW drawings into other formats
Requires: %{name}%{?_isa} = %{version}-%{release}

%description tools
Tools to transform CorelDRAW drawings into other formats.
Currently supported: XHTML, text, raw.

%prep
%setup -q

%build
%configure --disable-silent-rules --disable-static --disable-werror
sed -i \
    -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    libtool
%make_build

%install
%make_install
rm -f %{buildroot}/%{_libdir}/*.la
# rhbz#1001251 we install API docs directly from build
rm -rf %{buildroot}/%{_docdir}/%{name}

# generate and install man pages
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
for tool in cdr2raw cmx2raw cdr2xhtml cmx2xhtml cdr2text cmx2text; do
    help2man -N -S '%{name} %{version}' -o ${tool}.1 %{buildroot}%{_bindir}/${tool}
done
mkdir -p %{buildroot}/%{_mandir}/man1
install -m 0644 cdr2*.1 cmx2*.1 %{buildroot}/%{_mandir}/man1

%ldconfig_scriptlets

%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
%make_build check

%files
%doc AUTHORS ChangeLog README
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
%{_bindir}/cdr2raw
%{_bindir}/cdr2text
%{_bindir}/cdr2xhtml
%{_bindir}/cmx2raw
%{_bindir}/cmx2text
%{_bindir}/cmx2xhtml
%{_mandir}/man1/cdr2raw.1*
%{_mandir}/man1/cdr2text.1*
%{_mandir}/man1/cdr2xhtml.1*
%{_mandir}/man1/cmx2raw.1*
%{_mandir}/man1/cmx2text.1*
%{_mandir}/man1/cmx2xhtml.1*

%changelog
%autochangelog
