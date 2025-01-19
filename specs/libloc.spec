Name:       libloc
Version:    0.9.17
Release:    7%{?dist}
Summary:    Library to determine a location of an IP address in the Internet
# bash-completion/location: LGPL-2.1-or-later
# COPYING:                  LGPL-2.1 text
# data/database.db:         CC-BY-SA-4.0
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
## Unbundled, then used only at build-time, not in any binary package
# m4/ax_prog_perl_modules.m4:   FSFAP
# m4/ld-version-script.m4:  FSFULLR
## Not used and not in any binary package
# debian/copyright:         LGPL-2.1-or-later
# src/cron/location-update.in:  LGPL-2.1-or-later
License:    LGPL-2.1-or-later
URL:        https://location.ipfire.org/
Source0:    https://source.ipfire.org/releases/%{name}/%{name}-%{version}.tar.gz
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
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  pkgconf-m4
# pkgconf-pkg-config for pkg-config program
BuildRequires:  pkgconf-pkg-config
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(python) >= 3.4
# pkgconfig(systemd) not needed, we configure a value from systemd-rpm-macros
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
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n perl-%{name}
Location is a Perl interface to libloc, a library to determine an IP address
location in the Internet.

%package -n python3-%{name}
Summary:        Python interface to libloc library
License:        LGPL-2.1-or-later AND CC-BY-SA-4.0
Requires:       %{name}%{?_isa} = %{version}-%{release}
%py_provides python3-location

%description -n python3-%{name}
This is Python binding to libloc, a library to determine an IP adress location
in the Internet.

%package tools
Summary:        Tools for downloading and querying IPFire Location database
BuildArch:      noarch
Requires:       python3-%{name} = %{version}-%{release}
Recommends:     %{name}-tools-bash-completion = %{version}-%{release}

%description tools
"location" program retrieves information from the location database. This data
can be used to determine a location of an IP address in the Internet and for
building firewall rules to block access from certain autonomous systems or
countries. There is also an integration with systemd which helps updating the
location database periodically.

%package tools-bash-completion
Summary:        Bash completion support for IPFire location tools
BuildArch:      noarch
Requires:       bash-completion
Requires:       %{name}-tools = %{version}-%{release}

%description tools-bash-completion
This package implements Bash completion scripts for IPFire location tools.

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
    --enable-bash-completion \
    --with-database-path=%{default_database_file} \
    --enable-debug \
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
unset LOC_LOG
make check %{?_smp_mflags}

%post tools
%systemd_post location-update.service

%preun tools
%systemd_preun location-update.service

%postun tools
%systemd_postun_with_restart location-update.service

%files -f %{name}.lang
%license COPYING
%doc debian/changelog
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
# The default path is compiled into _location.so Python module. Not into
# C libloc.so. Thus the database belongs here, to Python package.
%dir %{_sharedstatedir}/location
%{_sharedstatedir}/location/signing-key.pem
# User can update the database later from the Internet.
%attr(0444, root, root) %verify(not size filedigest mtime) %{default_database_file}

%files tools
%{_bindir}/location*
%{_mandir}/man1/location.1*
%{_unitdir}/location-update.*

%files tools-bash-completion
%{_datadir}/bash-completion/completions/location

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.17-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.17-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 12 2024 Jitka Plesnikova <jplesnik@redhat.com> - 0.9.17-5
- Perl 5.40 rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.9.17-4
- Rebuilt for Python 3.13

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Aug 01 2023 Petr Pisar <ppisar@redhat.com> - 0.9.17-1
- 0.9.17 bump

* Mon Jul 24 2023 Petr Pisar <ppisar@redhat.com> - 0.9.16-6
- Fix "location list-networks-by-as --format ipset" output
  (upstream bug #12897)
- Fix string escaping with Python 3.12 (upstream bug #13188)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 0.9.16-4
- Perl 5.38 rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 0.9.16-3
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Oct 31 2022 Petr Pisar <ppisar@redhat.com> - 0.9.16-1
- 0.9.16 bump
- A database snapshot from 2022-10-20T06:27:23 is included

* Wed Oct 19 2022 Petr Pisar <ppisar@redhat.com> - 0.9.15-2
- Enable enabling debuging messages
- Fix make dependencies for Perl

* Tue Oct 04 2022 Petr Pisar <ppisar@redhat.com> - 0.9.15-1
- 0.9.15 packaged

