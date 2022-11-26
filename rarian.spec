
Name: rarian
Version: 0.8.1
Release: %{autorelease}
License: LGPL-2.1-or-later AND Zlib
Summary: Documentation meta-data library
URL: http://rarian.freedesktop.org/
Source: http://download.gnome.org/sources/rarian/0.8/rarian-%{version}.tar.bz2
Source1: scrollkeeper-omf.dtd

### Patch ###

# RH bug #453342
Patch1: rarian-0.8.1-categories.patch

### Dependencies ###

Requires(post): libxml2
Requires(postun): libxml2
# for /usr/bin/xmlcatalog

Requires: libxslt
# for /usr/bin/xsltproc
Requires: coreutils, util-linux, gawk
# for basename, getopt, awk, etc

### Build Dependencies ###

BuildRequires: make
BuildRequires: gcc-c++

%description
Rarian is a documentation meta-data library that allows access to documents,
man pages and info pages.  It was designed as a replacement for scrollkeeper.

%package compat
License: GPL-2.0-or-later
Summary: Extra files for compatibility with scrollkeeper
Requires: rarian = %{version}-%{release}
Requires(post): rarian
# The scrollkeeper version is arbitrary.  It just
# needs to be greater than what we're obsoleting.
Provides: scrollkeeper = 0.4
Obsoletes: scrollkeeper <= 0.3.14

%description compat
This package contains files needed to maintain backward-compatibility with
scrollkeeper.

%package devel
Summary: Development files for Rarian
License: LGPL-2.1-or-later AND Zlib
Requires: rarian = %{version}-%{release}
Requires: pkgconfig

%description devel
This package contains files required to develop applications that use the
Rarian library ("librarian").

%prep
%setup -q
%patch1 -p1 -b .categories

%build
%configure --disable-skdb-update
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build

%install
%make_install

mkdir -p %buildroot%{_datadir}/xml/scrollkeeper/dtds
cp %{SOURCE1} %buildroot%{_datadir}/xml/scrollkeeper/dtds

rm -rf %buildroot%{_libdir}/librarian.a
rm -rf %buildroot%{_libdir}/librarian.la

%ldconfig_scriptlets

%post compat
%{_bindir}/rarian-sk-update

# Add OMF DTD to XML catalog.
CATALOG=/etc/xml/catalog
/usr/bin/xmlcatalog --noout --add "rewriteSystem" \
  "http://scrollkeeper.sourceforge.net/dtds/scrollkeeper-omf-1.0/scrollkeeper-omf.dtd" \
  "/usr/share/xml/scrollkeeper/dtds/scrollkeeper-omf.dtd" $CATALOG >& /dev/null || :
/usr/bin/xmlcatalog --noout --add "rewriteURI" \
  "http://scrollkeeper.sourceforge.net/dtds/scrollkeeper-omf-1.0/scrollkeeper-omf.dtd" \
  "/usr/share/xml/scrollkeeper/dtds/scrollkeeper-omf.dtd" $CATALOG >& /dev/null || :

%postun compat

# Delete OMF DTD from XML catalog.
if [ $1 = 0 ]; then
  CATALOG=/etc/xml/catalog
  /usr/bin/xmlcatalog --noout --del \
    "/usr/share/xml/scrollkeeper/dtds/scrollkeeper-omf.dtd" $CATALOG >& /dev/null || :
fi

%files
%license COPYING COPYING.LIB COPYING.UTILS
%doc README ChangeLog NEWS AUTHORS
%{_bindir}/rarian-example
%{_libdir}/librarian.so.*
%{_datadir}/librarian
%{_datadir}/help

%files compat
%{_bindir}/rarian-sk-*
%{_bindir}/scrollkeeper-*
%{_datadir}/xml/scrollkeeper

%files devel
%{_includedir}/rarian
%{_libdir}/librarian.so
%{_libdir}/pkgconfig/rarian.pc

%changelog
%autochangelog
