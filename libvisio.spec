%global apiversion 0.1

Name: libvisio
Version: 0.1.7
Release: %autorelease
Summary: A library for import of Microsoft Visio diagrams

License: MPL-2.0
URL: http://wiki.documentfoundation.org/DLP/Libraries/libvisio
Source: http://dev-www.libreoffice.org/src/%{name}/%{name}-%{version}.tar.xz

BuildRequires: boost-devel
BuildRequires: doxygen
BuildRequires: gcc-c++
BuildRequires: gperf
BuildRequires: help2man
BuildRequires: perl-interpreter
BuildRequires: pkgconfig(cppunit)
BuildRequires: pkgconfig(icu-uc)
BuildRequires: pkgconfig(librevenge-0.0)
BuildRequires: pkgconfig(librevenge-generators-0.0)
BuildRequires: pkgconfig(librevenge-stream-0.0)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: make

%description
%{name} is library providing ability to interpret and import
Microsoft Visio diagrams into various applications. You can find it
being used in LibreOffice.

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
Summary: Tools to transform Microsoft Visio diagrams into other formats
Requires: %{name}%{?_isa} = %{version}-%{release}

%description tools
Tools to transform Microsoft Visio diagrams into other formats.
Currently supported: XHTML, raw, plain text.

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
# rhbz#1001240 we install API docs directly from build
rm -rf %{buildroot}/%{_docdir}/%{name}

# generate and install man pages
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
for tool in vsd2raw vss2text vsd2xhtml vss2raw vsd2text vss2xhtml; do
    help2man -N -S '%{name} %{version}' -o ${tool}.1 %{buildroot}%{_bindir}/${tool}
done
install -m 0755 -d %{buildroot}/%{_mandir}/man1
install -m 0644 vsd2*.1 vss2*.1 %{buildroot}/%{_mandir}/man1

%ldconfig_scriptlets

%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
make check %{?_smp_mflags}

%files
%doc AUTHORS README NEWS
%license COPYING.*
%{_libdir}/%{name}-%{apiversion}.so.*

%files devel
%doc ChangeLog
%{_includedir}/%{name}-%{apiversion}
%{_libdir}/%{name}-%{apiversion}.so
%{_libdir}/pkgconfig/%{name}-%{apiversion}.pc

%files doc
%license COPYING.*
%doc docs/doxygen/html

%files tools
%{_bindir}/vsd2raw
%{_bindir}/vsd2text
%{_bindir}/vsd2xhtml
%{_bindir}/vss2raw
%{_bindir}/vss2text
%{_bindir}/vss2xhtml
%{_mandir}/man1/vsd2raw.1*
%{_mandir}/man1/vsd2text.1*
%{_mandir}/man1/vsd2xhtml.1*
%{_mandir}/man1/vss2raw.1*
%{_mandir}/man1/vss2text.1*
%{_mandir}/man1/vss2xhtml.1*

%changelog
%autochangelog
