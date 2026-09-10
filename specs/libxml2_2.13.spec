Name:           libxml2_2.13
Version:        2.13.9
Release:        %autorelease
Summary:        Library providing XML and HTML support

# list.c, dict.c and few others use ISC-Veillard
# the conformance and test suite data in
# Source1, Source2 and Source3 is covered by W3C
License:        MIT AND ISC-Veillard AND W3C
URL:            https://gitlab.gnome.org/GNOME/libxml2/-/wikis/home
Source0:        https://download.gnome.org/sources/libxml2/2.13/libxml2-%{version}.tar.xz
# https://www.w3.org/XML/Test/xmlconf-20080827.html
Source1:        https://www.w3.org/XML/Test/xmlts20080827.tar.gz
# https://www.w3.org/XML/2004/xml-schema-test-suite/index.html
Source2:        https://www.w3.org/XML/2004/xml-schema-test-suite/xmlschema2002-01-16/xsts-2002-01-16.tar.gz
Source3:        https://www.w3.org/XML/2004/xml-schema-test-suite/xmlschema2004-01-14/xsts-2004-01-14.tar.gz
Patch0:         libxml2-multilib.patch
# Patch from openSUSE.
# See:  https://bugzilla.gnome.org/show_bug.cgi?id=789714
Patch1:         libxml2-2.12.0-python3-unicode-errors.patch

BuildRequires:  cmake-rpm-macros
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(liblzma)

%description
This library allows to manipulate XML files. It includes support
to read, modify and write XML and HTML files. There is DTDs support
this includes parsing and validation even with complex DtDs, either
at parse time or later once the document has been modified. The output
can be a simple SAX stream or and in-memory DOM like representations.
In this case one can use the built-in XPath and XPointer implementation
to select sub nodes or ranges. A flexible Input/Output mechanism is
available, with existing HTTP and FTP modules and combined to an
URI library.

%package devel
Summary:        Libraries, includes, etc. to develop XML and HTML applications
Conflicts:      libxml2-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       zlib-devel%{?_isa}
Requires:       xz-devel%{?_isa}

%description devel
Libraries, include files, etc you can use to develop XML applications.
This library allows to manipulate XML files. It includes support
to read, modify and write XML and HTML files. There is DTDs support
this includes parsing and validation even with complex DtDs, either
at parse time or later once the document has been modified. The output
can be a simple SAX stream or and in-memory DOM like representations.
In this case one can use the built-in XPath and XPointer implementation
to select sub nodes or ranges. A flexible Input/Output mechanism is
available, with existing HTTP and FTP modules and combined to an
URI library.

%prep
%autosetup -p1 -C
find doc -type f -executable -print -exec chmod 0644 {} ';'

%build
# see https://bugzilla.redhat.com/show_bug.cgi?id=2139546 , several
# of these options are needed to (mostly) retain ABI compatibility
# with earlier versions
%configure \
    --with-legacy \
    --with-ftp \
    --without-python
%make_build

%install
%make_install

# multiarch crazyness on timestamp differences or Makefile/binaries for examples
touch -m --reference=%{buildroot}%{_includedir}/libxml2/libxml/parser.h %{buildroot}%{_bindir}/xml2-config

find %{buildroot} -type f -name '*.la' -print -delete
rm -vrf %{buildroot}%{_datadir}/doc/
gzip -9 -c doc/libxml2-api.xml >doc/libxml2-api.xml.gz

%check
# Tests require the XML conformance suite.
tar -xzvf %{SOURCE1}
%make_build check
rm -rf xmlconf
# Schema tests use the schema test suite.
cp %{SOURCE2} %{SOURCE3} xstc/
pushd xstc
mkdir Tests
%make_build tests
popd

%ldconfig_scriptlets

%files
%license Copyright
%doc NEWS README.md
%{_libdir}/libxml2.so.2*
%exclude %{_bindir}/xmlcatalog
%exclude %{_bindir}/xmllint
%exclude %{_mandir}/man1/xmlcatalog.1*
%exclude %{_mandir}/man1/xmllint.1*

%files devel
%doc doc/*.html
%doc doc/libxml2-api.xml.gz
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/aclocal/libxml.m4
%{_datadir}/gtk-doc/html/libxml2/
%{_includedir}/libxml2/
%{_libdir}/libxml2.so
%{_libdir}/pkgconfig/libxml-2.0.pc
%{_libdir}/cmake/libxml2/
%{_bindir}/xml2-config
%{_mandir}/man1/xml2-config.1*

%changelog
%autochangelog
