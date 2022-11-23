%global apiversion 0.1

Name: libe-book
Version: 0.1.3
Release: %autorelease
Summary: A library for import of reflowable e-book formats

License: MPL-2.0
URL: https://sourceforge.net/projects/libebook/
Source: http://downloads.sourceforge.net/libebook/%{name}-%{version}.tar.xz

BuildRequires: boost-devel
BuildRequires: doxygen
BuildRequires: gcc-c++
BuildRequires: gperf
BuildRequires: help2man
BuildRequires: make
BuildRequires: pkgconfig(cppunit)
BuildRequires: pkgconfig(icu-i18n)
BuildRequires: pkgconfig(liblangtag)
BuildRequires: pkgconfig(librevenge-0.0)
BuildRequires: pkgconfig(librevenge-generators-0.0)
BuildRequires: pkgconfig(librevenge-stream-0.0)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(zlib)

Patch0: 0001-fix-build-with-ICU-68.patch

%description
%{name} is a library for import of reflowable e-book formats.
Currently supported are PalmDoc, TealDoc, Plucker eBook, eReader eBook,
FictionBook v.2, TCR, zTXT and Broad Band eBook (LRF).

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
Summary: Tools to transform e-books into other formats
Requires: %{name}%{?_isa} = %{version}-%{release}

%description tools
Tools to transform e-books into other formats.
Currently supported: XHTML, raw, text.

%prep
%autosetup -p1

%build
%configure --disable-silent-rules --disable-static
sed -i \
    -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    libtool
%make_build

%install
%make_install
rm -f %{buildroot}/%{_libdir}/*.la
# we install API docs directly from build
rm -rf %{buildroot}/%{_docdir}/%{name}

# generate and install man pages
export LD_LIBRARY_PATH=%{buildroot}/%{_libdir}${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
for tool in ebook2html ebook2raw ebook2text; do
    help2man -N -S '%{name} %{version}' -o ${tool}.1 %{buildroot}%{_bindir}/${tool}
done
install -m 0755 -d %{buildroot}/%{_mandir}/man1
install -m 0644 ebook2*.1 %{buildroot}/%{_mandir}/man1

%ldconfig_scriptlets

%check
export LD_LIBRARY_PATH=%{buildroot}/%{_libdir}${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
%make_build check

%files
%doc AUTHORS NEWS README
%license COPYING
%{_libdir}/%{name}-%{apiversion}.so.*

%files devel
%doc ChangeLog
%{_includedir}/%{name}-%{apiversion}
%{_libdir}/%{name}-%{apiversion}.so
%{_libdir}/pkgconfig/%{name}-%{apiversion}.pc

%files doc
%license COPYING
%doc docs/doxygen/html

%files tools
%{_bindir}/ebook2raw
%{_bindir}/ebook2text
%{_bindir}/ebook2html
%{_mandir}/man1/ebook2html.1*
%{_mandir}/man1/ebook2raw.1*
%{_mandir}/man1/ebook2text.1*

%changelog
%autochangelog
