%global apiversion 0.3

Name: libmwaw
Version: 0.3.22
Release: %autorelease
Summary: A library for import of many old Mac document formats

License: LGPL-2.1-or-later OR MPL-2.0
URL: http://sourceforge.net/projects/libmwaw/
Source: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz

BuildRequires: doxygen
BuildRequires: gcc-c++
BuildRequires: help2man
BuildRequires: pkgconfig(librevenge-0.0)
BuildRequires: pkgconfig(librevenge-generators-0.0)
BuildRequires: pkgconfig(librevenge-stream-0.0)
BuildRequires: make

%description
%{name} is a library for import of old Mac documents. It supports many
kinds of text documents, spreadsheets, databases, vector and bitmap
images. Supported are, for example, documents created by BeagleWorks,
ClarisWorks, MacPaint, MacWrite or Microsoft Word for Mac. A full list
of supported formats is available at
https://sourceforge.net/p/libmwaw/wiki/Home/ .

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
Summary: Tools to transform the supported formats into other formats
Requires: %{name}%{?_isa} = %{version}-%{release}

%description tools
Tools to transform the supported document formats into other formats.
Supported output formats are CSV, HTML, SVG, plain text and raw.

%prep
%autosetup -p1

%build
%configure --disable-static --disable-werror --disable-zip --enable-docs
sed -i \
    -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    libtool
%make_build

export LD_LIBRARY_PATH=`pwd`/src/lib/.libs${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
help2man -N -n 'convert Mac spreadsheet into CSV' -o mwaw2csv.1 ./src/conv/csv/.libs/mwaw2csv
help2man -N -n 'debug the conversion library' -o mwaw2raw.1 ./src/conv/raw/.libs/mwaw2raw
help2man -N -n 'convert Mac text document into HTML' -o mwaw2html.1 ./src/conv/html/.libs/mwaw2html
help2man -N -n 'convert Mac drawing into SVG' -o mwaw2svg.1 ./src/conv/svg/.libs/mwaw2svg
help2man -N -n 'convert Mac text document into plain text' -o mwaw2text.1 ./src/conv/text/.libs/mwaw2text

%install
%make_install
rm -f %{buildroot}/%{_libdir}/*.la
# it seems this tool is only useful on MacOS
rm -f %{buildroot}/%{_bindir}/mwawFile
# rhbz#1001297 we install API docs directly from build
rm -rf %{buildroot}/%{_docdir}/%{name}

install -m 0755 -d %{buildroot}/%{_mandir}/man1
install -m 0644 mwaw2*.1 %{buildroot}/%{_mandir}/man1

%ldconfig_scriptlets

%files
%doc CHANGES README
%license COPYING.*
%{_libdir}/%{name}-%{apiversion}.so.*

%files devel
%doc HACKING
%{_includedir}/%{name}-%{apiversion}
%{_libdir}/%{name}-%{apiversion}.so
%{_libdir}/pkgconfig/%{name}-%{apiversion}.pc

%files doc
%license COPYING.*
%doc docs/doxygen/html

%files tools
%{_bindir}/mwaw2csv
%{_bindir}/mwaw2html
%{_bindir}/mwaw2raw
%{_bindir}/mwaw2svg
%{_bindir}/mwaw2text
%{_mandir}/man1/mwaw2csv.1*
%{_mandir}/man1/mwaw2html.1*
%{_mandir}/man1/mwaw2raw.1*
%{_mandir}/man1/mwaw2svg.1*
%{_mandir}/man1/mwaw2text.1*

%changelog
%autochangelog
