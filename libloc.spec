Name:       libloc
Version:    0.9.15
Release:    1%{?dist}
Summary:    Library to determine a location of an IP address in the Internet
# COPYING:                  LGPL-2.1 text
# man/libloc.txt:           LGPL-2.1-or-later
# po/de.po:                 "same as libloc"
# src/address.c:            LGPL-2.1-or-later
# src/as.c:                 LGPL-2.1-or-later
# src/as-list.c:            LGPL-2.1-or-later
# src/country.c:            LGPL-2.1-or-later
# src/country-list.c:       LGPL-2.1-or-later
# src/database.c:           LGPL-2.1-or-later
# src/libloc.c:             LGPL-2.1-or-later
# src/libloc/address.h:     LGPL-2.1-or-later
# src/libloc/as.h:          LGPL-2.1-or-later
# src/libloc/as-list.h:     LGPL-2.1-or-later
# src/libloc/compat.h:      LGPL-2.1-or-later
# src/libloc/country.h:     LGPL-2.1-or-later
# src/libloc/country-list.h:    LGPL-2.1-or-later
# src/libloc/database.h:    LGPL-2.1-or-later
# src/libloc/format.h:      LGPL-2.1-or-later
# src/libloc/libloc.h:      LGPL-2.1-or-later
# src/libloc/network.h:     LGPL-2.1-or-later
# src/libloc/network-list.h:    LGPL-2.1-or-later
# src/libloc/private.h:     LGPL-2.1-or-later
# src/libloc/resolv.h:      LGPL-2.1-or-later
# src/libloc/stringpool.h:  LGPL-2.1-or-later
# src/libloc/writer.h:      LGPL-2.1-or-later
# src/network.c:            LGPL-2.1-or-later
# src/network-list.c:       LGPL-2.1-or-later
# src/perl/lib/Location.pm: GPL-1.0-or-later OR Artistic-1.0-Perl
# src/python/as.h:          LGPL-2.1-or-later
# src/python/country.c:     LGPL-2.1-or-later
# src/python/country.h:     LGPL-2.1-or-later
# src/python/database.c:    LGPL-2.1-or-later
# src/python/database.h:    LGPL-2.1-or-later
# src/python/location/__init__.py:      LGPL-2.1-or-later
# src/python/location/downloader.py:    LGPL-2.1-or-later
# src/python/location/export.py:    LGPL-2.1-or-later
# src/python/location/i18n.py:      LGPL-2.1-or-later
# src/python/location/importer.py:  LGPL-2.1-or-later
# src/python/location/logger.py:    LGPL-2.1-or-later
# src/python/locationmodule.c:  LGPL-2.1-or-later
# src/python/locationmodule.h:  LGPL-2.1-or-later
# src/python/network.c      LGPL-2.1-or-later
# src/python/network.h:     LGPL-2.1-or-later
# src/python/writer.c:      LGPL-2.1-or-later
# src/python/writer.h:      LGPL-2.1-or-later
# src/resolv.c:             LGPL-2.1-or-later
# src/scripts/location.in:  LGPL-2.1-or-later
# src/scripts/location-importer.in: LGPL-2.1-or-later
# src/stringpool.c:         LGPL-2.1-or-later
# src/writer.c:             LGPL-2.1-or-later
# tests/python/test-database.py:    LGPL-2.1-or-later
# tests/python/test-export.py:      LGPL-2.1-or-later
## Used at build-time but not in any binary package
# m4/attributes.m4:         GPL-2.0-or-later WITH Autoconf-exception-2.0 (?)
# src/perl/Makefile.PL:     "lgpl" (probably a mistake)
# src/test-address.c:       GPL-2.0-or-later
# src/test-as.c:            GPL-2.0-or-later
# src/test-country.c:       GPL-2.0-or-later
# src/test-database.c:      GPL-2.0-or-later
# src/test-libloc.c:        GPL-2.0-or-later
# src/test-network.c:       GPL-2.0-or-later
# src/test-network-list.c:  GPL-2.0-or-later
# src/test-signature.c:     GPL-2.0-or-later
# src/test-stringpool.c:    GPL-2.0-or-later
# tests/data/location-2022-03-30.db:    CC-BY-SA-4.0
## Unbundled, then used only at build-time, not in any binary package
# m4/ax_prog_perl_modules.m4:   FSFAP
# m4/ld-version-script.m4:  FSFULLR
## Not used and not in any binary package
# debian/copyright:         LGPL-2.1-or-later
# src/cron/location-update.in:  LGPL-2.1-or-later
License:    LGPL-2.1-or-later
URL:        https://location.ipfire.org/
Source0:    https://source.ipfire.org/releases/%{name}/%{name}-%{version}.tar.gz
# Install Python files into site Python module path, in upstream after 0.9.15
Patch0:     libloc-0.9.15-Makefile-Reset-Python-path.patch
# Install Perl files vendor Perl module path, proposed to the upstream,
# <https://bugzilla.ipfire.org/show_bug.cgi?id=12954>
Patch1:     libloc-0.9.15-Install-Perl-files-to-Perl-vendor-directory.patch
# Remove empty RPATH, proposed to the upstream,
# <https://bugzilla.ipfire.org/show_bug.cgi?id=12955>
Patch2:     libloc-0.9.15-Revert-perl-Remove-RPATH.patch
# Remove shebangs from Python modules, proposed to the upstream,
# <https://bugzilla.ipfire.org/show_bug.cgi?id=12956>
Patch3:     libloc-0.9.15-Remove-shebangs-from-Python-modules.patch
# Move location(8) to location(1), proposed to the upstream,
# <https://bugzilla.ipfire.org/show_bug.cgi?id=12957>
Patch4:     libloc-0.9.15-Move-location-manual-from-section-8-to-section-1.patch
BuildRequires:  asciidoc
BuildRequires:  autoconf >= 2.60
# autoconf-archive for unbundled m4/ax_prog_perl_modules.m4
BuildRequires:  autoconf-archive
BuildRequires:  automake >= 1.11
BuildRequires:  coreutils
# DocBook XSLT URL used in Makefile.am is redirected to local file sytem by
# an XML catalog of docbook-style-xsl.
BuildRequires:  docbook-style-xsl
BuildRequires:  findutils
BuildRequires:  gcc
# grep is called from po/Makefile supplied with intltool
BuildRequires:  grep
# gnulib-devel for unbundled m4/ld-version-script.m4
BuildRequires:  gnulib-devel
BuildRequires:  intltool >= 0.40.0
BuildRequires:  libtool
# libxslt for xsltproc program
BuildRequires:  libxslt
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  pkgconf-m4
# pkgconf-pkg-config for pkg-config program
BuildRequires:  pkgconf-pkg-config
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(python) >= 3.4
# pkgconfig(systemd) no needed, we configure a value from systemd-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  sed
BuildRequires:  systemd-rpm-macros
# Run-time:
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
# python3-psycopg2 not used at tests
# Tests:
BuildRequires:  perl(Test::More)

%description
This is a lightweight library which can be used to query the IPFire Location
database.

%package devel
Summary:        Developmental files for libloc C library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains header files and other files helpful when developing
applications using libloc library.

%package -n perl-%{name}
Summary:        Perl interface to libloc library
License:        LGPL-2.1-or-later AND (GPL-1.0-or-later OR Artistic-1.0-Perl)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description -n perl-%{name}
Location is a Perl interface to libloc, a library to determine an IP address
location in the Internet.

%package -n python3-%{name}
Summary:        Python interface to libloc library
%py_provides python3-location

%description -n python3-%{name}
This is Python binding to libloc, a library to determine an IP adress location
in the Internet.

%package tools
Summary:        Tools for downloading and querying IPFire Location database
BuildArch:      noarch
Requires:       python3-%{name} = %{version}-%{release}

%description tools
"location" program retrieves information from the location database. This data
can be used to determine a location of an IP address in the Internet and for
building firewall rules to block access from certain autonomous systems or
countries. There is also an integration with systemd which helps updating the
location database periodically.

%prep
%autosetup -p1
# Unbundle m4 macros
rm m4/ax_prog_perl_modules.m4 m4/ld-version-script.m4

%build
autoreconf -fi -I%{_datadir}/gnulib/m4
# Upstream moved to /var/lib/location/database.db in
# 14e821d483017d86d9e12486c9d9a289f4e99b0e.
%global default_database_file %{_sharedstatedir}/location/database.db
%{configure} \
    --disable-analyzer \
    --with-database-path=%{default_database_file} \
    --disable-debug \
    --enable-largefile \
    --enable-ld-version-script \
    --enable-man_pages \
    --enable-nls \
    --enable-perl \
    --enable-shared \
    --disable-silent-rules \
    --disable-static \
    --with-systemd \
    --with-systemdsystemunitdir=%{_unitdir}
%{make_build}

%install
%{make_install}
# Remove libtool archives
find %{buildroot} -name '*.la' -delete
# Correct Perl permissions
%{_fixperms} %{buildroot}/*
# Create Python dist-info metadata
install -d -m 0755 %{buildroot}/%{python3_sitelib}/%{name}-%{version}.dist-info
cat <<'EOF' >%{buildroot}/%{python3_sitelib}/%{name}-%{version}.dist-info/WHEEL
Wheel-Version: 1.0
Generator: handmade
Root-Is-Purelib: false
Tag: py3-none-any
EOF
chmod 0644 %{buildroot}/%{python3_sitelib}/%{name}-%{version}.dist-info/WHEEL
cat <<'EOF' >%{buildroot}/%{python3_sitelib}/%{name}-%{version}.dist-info/METADATA
Metadata-Version: 2.1
Name: %{name}
Version: %{version}
Home-page: %{url}
Requires-Dist: psycopg2
EOF
chmod 0644 %{buildroot}/%{python3_sitelib}/%{name}-%{version}.dist-info/METADATA
# Gather NLS files
%find_lang %{name}

%check
make check %{?_smp_mflags}

%post tools
%systemd_post location-update.service

%preun tools
%systemd_preun location-update.service

%postun tools
%systemd_postun_with_restart location-update.service

%files -f %{name}.lang
%license COPYING
%{_libdir}/libloc.so.1*

%files devel
%{_includedir}/libloc
%{_libdir}/libloc.so
%{_libdir}/pkgconfig
%{_mandir}/man3/libloc.3*
%{_mandir}/man3/loc_*.3*

%files -n perl-%{name}
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Location*
%{_mandir}/man3/Location.3pm*

%files -n python3-%{name}
%doc examples/python/*
%{python3_sitelib}/location
%{python3_sitelib}/%{name}-%{version}.dist-info
%{python3_sitearch}/_location.so
# TODO: writable for a dedicated, non-root user
# The default path is compiled into _location.so Python module. Not into
# C libloc.so. Thus the database belongs here, to Python package.
%{_sharedstatedir}/location
%ghost %attr(0444, root, root) %{default_database_file}

%files tools
%{_bindir}/location*
%{_mandir}/man1/location.1*
%{_unitdir}/*

%changelog
* Tue Oct 04 2022 Petr Pisar <ppisar@redhat.com> - 0.9.15-1
- 0.9.15 packaged

