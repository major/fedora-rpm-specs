Name:           libxml2
Version:        2.15.4
Release:        %autorelease
Summary:        Library providing XML and HTML support

# list.c, dict.c and few others use ISC-Veillard
# the conformance and test suite data in
# Source1, Source2 and Source3 is covered by W3C
License:        MIT AND ISC-Veillard AND W3C
URL:            https://gitlab.gnome.org/GNOME/libxml2/-/wikis/home
Source0:        https://download.gnome.org/sources/%{name}/2.15/%{name}-%{version}.tar.xz
Patch0:         libxml2-multilib.patch

BuildRequires:  cmake-rpm-macros
BuildRequires:  docbook-style-xsl
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  meson
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  /usr/bin/xsltproc

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

%package static
Summary:        Static library for libxml2

%description static
Static library for libxml2 provided for specific uses or shaving a few
microseconds when parsing, do not link to them for generic purpose packages.

%package -n python3-%{name}
Summary:        Python 3 bindings for the libxml2 library
BuildRequires:  python3-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      %{name}-python3 < %{version}-%{release}
Provides:       %{name}-python3 = %{version}-%{release}
# Will be removed upstream in 2.16.
Provides:       deprecated()

%description -n python3-%{name}
The libxml2-python3 package contains a Python 3 module that permits
applications written in the Python programming language, version 3, to use the
interface supplied by the libxml2 library to manipulate XML files.

This library allows to manipulate XML files. It includes support
to read, modify and write XML and HTML files. There is DTDs support
this includes parsing and validation even with complex DTDs, either
at parse time or later once the document has been modified.

%prep
%autosetup -p1
find doc -type f -executable -print -exec chmod 0644 {} ';'

%conf
%meson -Ddefault_library=both

%build
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license Copyright
%doc NEWS README.md
%{_libdir}/libxml2.so.16{,.*}
%{_bindir}/xmlcatalog
%{_bindir}/xmllint
%{_mandir}/man1/xmlcatalog.1*
%{_mandir}/man1/xmllint.1*

%files devel
%doc %{_docdir}/libxml2/*.html
%doc %{_docdir}/libxml2/html/
%doc example
%{_includedir}/libxml2/
%{_libdir}/libxml2.so
%{_libdir}/pkgconfig/libxml-2.0.pc
%{_libdir}/cmake/libxml2/
%{_bindir}/xml2-config
%{_mandir}/man1/xml2-config.1*

%files static
%license Copyright
%{_libdir}/libxml2.a

%files -n python3-%{name}
%{python3_sitearch}/libxml2mod.*.so
%{python3_sitelib}/libxml2.py
%{python3_sitelib}/__pycache__/libxml2.*
%{python3_sitelib}/drv_libxml2.py
%{python3_sitelib}/__pycache__/drv_libxml2.*

%changelog
%autochangelog
