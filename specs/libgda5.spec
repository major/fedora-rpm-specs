%bcond_without bdb
%bcond_without ldap
%bcond_without mysql
%bcond_without postgres
%bcond_without mdb
%ifarch %{java_arches}
%bcond_without java
%else
%bcond_with java
%endif

%global apiver  5.0
%global libgda4_obsoletes_version 1:4.2.13-3
%global upstream libgda

Name:           libgda5
Epoch:          1
Version:        5.2.10
Release:        23%{?dist}
Summary:        Library for writing gnome database programs

License:        LGPL-2.1-or-later
URL:            http://www.gnome-db.org/
Source:         http://ftp.gnome.org/pub/GNOME/sources/%{upstream}/5.2/%{upstream}-%{version}.tar.xz

# Patches for building against mdbtools >= 0.9.0
# https://gitlab.gnome.org/GNOME/libgda/-/merge_requests/178
Patch1:         0001-mdb-provider-Remove-no-op-mdb_init-and-mdb_exit-call.patch
Patch2:         0002-mdb-provider-Store-filename-used-to-open-the-DB-in-o.patch
Patch3:         0003-mdb-provider-Pass-MdbHandle-to-the-mdb_set_date_fmt-.patch
# Upstream fix commit 9859479884fad5f39e6c37e8995e57c28b11b1b9
Patch4:         libgda-5.2.10-mysql-bool-fix.patch
Patch5:         bebdffb4de586fb43fd07ac549121f4b22f6812d.patch
Patch6:         libgda5-configure-c99.patch
Patch7:         libgda5-gtksourceview-c99.patch
Patch8:         libgda5-configure-c99-2.patch
Patch9:         libgda5-c99-2.patch
Patch10:        libgda5-c99-3.patch
Patch11:        libgda5-c99-4.patch
Patch12:        pointer-types.patch

BuildRequires:    gcc
BuildRequires:    gcc-c++
BuildRequires:    pkgconfig >= 0.8
BuildRequires:    glade-devel
BuildRequires:    glib2-devel >= 2.28.0
BuildRequires:    gtk3-devel >= 3.0.0
BuildRequires:    gtksourceview3-devel
BuildRequires:    goocanvas2-devel
BuildRequires:    graphviz-devel >= 2.26.0
BuildRequires:    iso-codes-devel
BuildRequires:    itstool
BuildRequires:    libxslt-devel >= 1.0.9
BuildRequires:    sqlite-devel >= 3.10.2
BuildRequires:    libgcrypt-devel
BuildRequires:    libgee-devel
BuildRequires:    gobject-introspection-devel >= 0.6.5
BuildRequires:    libxml2-devel readline-devel json-glib-devel
BuildRequires:    gtk-doc intltool gettext flex bison perl(XML::Parser)
BuildRequires:    libsecret-devel
BuildRequires:    libsoup-devel
BuildRequires:    openssl-devel
BuildRequires:    yelp-tools
BuildRequires:    vala
BuildRequires:    make
BuildRequires:    gnome-common
%{?with_bdb:BuildRequires:    libdb-devel}
%{?with_ldap:BuildRequires:    openldap-devel}
%{?with_mysql:BuildRequires:    mariadb-connector-c-devel}
%{?with_postgres:BuildRequires:    libpq-devel}
%{?with_mdb:BuildRequires:    mdbtools-devel}
%{?with_java:BuildRequires:    java-devel >= 1:1.6.0}

%description
%{upstream} is a library that eases the task of writing Gtk3-based database
programs.

%package        devel
Summary:        Development files for %{upstream}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Obsoletes:      libgda-java-devel < %{libgda4_obsoletes_version}
Obsoletes:      libgda-ldap-devel < %{libgda4_obsoletes_version}
Obsoletes:      libgda-mdb-devel < %{libgda4_obsoletes_version}
Obsoletes:      libgda-mysql-devel < %{libgda4_obsoletes_version}
Obsoletes:      libgda-postgres-devel < %{libgda4_obsoletes_version}
Obsoletes:      libgda-sqlcipher-devel < %{libgda4_obsoletes_version}
Obsoletes:      libgda-sqlite-devel < %{libgda4_obsoletes_version}
Obsoletes:      libgda-web-devel < %{libgda4_obsoletes_version}

%description    devel
The %{upstream}-devel package contains libraries and header files for
developing applications that use %{upstream}.

%package ui
Summary:         UI extensions for %{upstream}
Requires:        %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description ui
%{upstream}-ui extends %{upstream} providing graphical widgets (Gtk+).

%package        ui-devel
Summary:        Development files for %{upstream}-ui
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       %{name}-ui%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       gtk3-devel%{?_isa} >= 3.0.0

%description    ui-devel
The %{upstream}-ui-devel package contains libraries and header files for
developing applications that use %{upstream}-ui.

%package tools
Summary:         Graphical tools for %{upstream}
Requires:        %{name}-ui%{?_isa} = %{epoch}:%{version}-%{release}

%description tools
This %{upstream}-tools package provides graphical tools for %{upstream}.

%package sqlite
Summary:        SQLite provider for %{upstream}
Requires:       %{name}%{?isa} = %{epoch}:%{version}-%{release}
Requires:       sqlite-libs%{?isa} >= 3.10.2

%description sqlite
This %{upstream}-sqlite includes the %{upstream} SQLite provider.

%if 0%{with bdb}
%package bdb
Summary:        Berkeley DB provider for %{upstream}
Requires:       %{name}%{?isa} = %{epoch}:%{version}-%{release}

%description bdb
This %{upstream}-bdb includes the %{upstream} Berkeley DB provider.
%endif

%if 0%{with ldap}
%package ldap
Summary:        Ldap provider for %{upstream}
Requires:       %{name}%{?isa} = %{epoch}:%{version}-%{release}

%description ldap
This %{upstream}-ldap includes the %{upstream} Ldap provider.
%endif

%package sqlcipher
Summary:        SQLiteCipher provider for %{upstream}
Requires:       %{name}%{?isa} = %{epoch}:%{version}-%{release}

%description sqlcipher
This %{upstream}-sqlcipher includes the %{upstream} SQLiteCipher provider.
%package web
Summary:        Web provider for %{upstream}
Requires:       %{name}%{?isa} = %{epoch}:%{version}-%{release}

%description web
This %{upstream}-web includes the %{upstream} Web provider.

%if 0%{with mysql}
%package mysql
Summary:        Mysql provider for %{upstream}
Requires:       %{name}%{?isa} = %{epoch}:%{version}-%{release}

%description mysql
This %{upstream}-mysql includes the %{upstream} Mysql provider.
%endif

%if 0%{with postgres}
%package postgres
Summary:        Postgres provider for %{upstream}
Requires:       %{name}%{?isa} = %{epoch}:%{version}-%{release}

%description postgres
This %{upstream}-postgres includes the %{upstream} PostgreSQL provider.
%endif

%if 0%{with mdb}
%package mdb
Summary:        Mdb provider for %{upstream}
Requires:       %{name}%{?isa} = %{epoch}:%{version}-%{release}

%description mdb
This %{upstream}-mdb includes the %{upstream} Mdb provider.
%endif

%if 0%{with java}
%package java
Summary:        Java provider for %{upstream}
Requires:       %{name}%{?isa} = %{epoch}:%{version}-%{release}

%description java
This %{upstream}-java includes the %{upstream} Java JDBC provider.
%endif


%prep
%autosetup -p1 -n %{upstream}-%{version}
# Workaround to detect JRE 17 (java 17)
sed -i.java m4/java.m4 \
	-e 's|JRE11.0|JRE[[1-9]][[0-9]].0|' -e 's|Sun JRE 11.0|Sun \$JVERSION|'
NOCONFIGURE=1 srcdir=. gnome-autogen.sh

# AUTHORS not in UTF-8
iconv --from=ISO-8859-1 --to=UTF-8 AUTHORS > AUTHORS.new && \
touch -r AUTHORS AUTHORS.new && mv AUTHORS.new AUTHORS

%build
# set LD_LIBRARY_PATH manually since it fails to find libjvm with java7
%if 0%{with java}
# this list should match the setup in java-1.7.0-openjdk.spec
# or getsp.java should be fixed
%ifarch x86_64
%global archinstall amd64
%endif
%ifarch %{ix86}
%global archinstall i386
%endif
%ifarch ppc
%global archinstall ppc
%endif
%ifarch ppc64
%global archinstall ppc64
%endif
%ifarch ppc64le
%global archinstall ppc64le
%endif
%ifarch ia64
%global archinstall ia64
%endif
%ifarch s390
%global archinstall s390
%endif
%ifarch s390x
%global archinstall s390x
%endif
%ifarch %{arm}
%global archinstall arm
%endif
# 32 bit sparc, optimized for v9
%ifarch sparcv9
%global archinstall sparc
%endif
# 64 bit sparc
%ifarch sparc64
%global archinstall sparcv9
%endif
%ifarch aarch64
%global archinstall aarch64
%endif
export LD_LIBRARY_PATH=%{_jvmdir}/java/jre/lib/%{archinstall}/server:$LD_LIBRARY_PATH
%endif
%configure --disable-static --enable-vala \
           --with-libsoup  --with-gnome-keyring \
           --with-ui --with-gtksourceview \
           --with-goocanvas --with-graphviz \
           --enable-system-sqlite=yes \
           %{?with_bdb:--with-bdb=%{_prefix} --with-bdb-libdir-name=%{_lib}} \
           %{!?with_ldap:--with-ldap=no} \
           %{!?with_mysql:--with-mysql=no} \
           %{!?with_postgres:--with-postgresql=no} \
           %{!?with_mdb:--with-mdb=no} \
           %{!?with_java:--with-java=no}
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'
rm %{buildroot}/%{_sysconfdir}/%{upstream}-%{apiver}/sales_test.db

%find_lang libgda-5.0
%find_lang gda-browser --with-gnome

%files -f libgda-5.0.lang
%license COPYING
%doc AUTHORS ChangeLog README NEWS
%dir %{_sysconfdir}/%{upstream}-%{apiver}/
%config(noreplace) %{_sysconfdir}/%{upstream}-%{apiver}/config
%{_libdir}/%{upstream}-%{apiver}.so.*
%{_libdir}/%{upstream}-report-%{apiver}.so.*
%{_libdir}/%{upstream}-xslt-%{apiver}.so.*
%dir %{_libdir}/%{upstream}-%{apiver}/
%dir %{_libdir}/%{upstream}-%{apiver}/plugins/
%dir %{_libdir}/%{upstream}-%{apiver}/providers/
%{_libdir}/girepository-1.0/Gda-%{apiver}.typelib
%{_mandir}/man1/*
%dir %{_datadir}/%{upstream}-%{apiver}/
%dir %{_datadir}/%{upstream}-%{apiver}/dtd/
%{_datadir}/%{upstream}-%{apiver}/dtd/libgda-*.dtd
%{_datadir}/%{upstream}-%{apiver}/import_encodings.xml
%{_datadir}/%{upstream}-%{apiver}/information_schema.xml

%files devel
%dir %{_datadir}/gtk-doc/
%dir %{_datadir}/gtk-doc/html/
%doc %{_datadir}/gtk-doc/html/%{upstream}-%{apiver}
%{_datadir}/gir-1.0/Gda-%{apiver}.gir
%dir %{_includedir}/%{upstream}-%{apiver}/
%{_includedir}/%{upstream}-%{apiver}/%{upstream}
%{_includedir}/%{upstream}-%{apiver}/%{upstream}-xslt
%{_includedir}/%{upstream}-%{apiver}/%{upstream}-report
%{_libdir}/%{upstream}-%{apiver}.so
%{_libdir}/%{upstream}-report-%{apiver}.so
%{_libdir}/%{upstream}-xslt-%{apiver}.so
%{_libdir}/pkgconfig/%{upstream}-%{apiver}.pc
%{_libdir}/pkgconfig/%{upstream}-*-%{apiver}.pc
%exclude %{_libdir}/pkgconfig/%{upstream}-ui-%{apiver}.pc
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/libgda-%{apiver}.vapi

%files ui
%{_libdir}/%{upstream}-ui-%{apiver}.so.*
%{_libdir}/%{upstream}-%{apiver}/plugins/*.xml
%{_libdir}/%{upstream}-%{apiver}/plugins/%{upstream}-ui-plugins.so
%{_libdir}/girepository-1.0/Gdaui-%{apiver}.typelib
%{_datadir}/%{upstream}-%{apiver}/pixmaps
%{_datadir}/%{upstream}-%{apiver}/dtd/gdaui-layout.dtd
%{_datadir}/%{upstream}-%{apiver}/ui/
%{_datadir}/%{upstream}-%{apiver}/icons/
%{_datadir}/%{upstream}-%{apiver}/server_operation.glade
%{_datadir}/%{upstream}-%{apiver}/language-specs/gda-sql.lang

%files ui-devel
%{_includedir}/%{upstream}-%{apiver}/%{upstream}-ui
%{_libdir}/%{upstream}-ui-%{apiver}.so
%{_bindir}/gdaui-demo-%{apiver}
%{_libdir}/pkgconfig/%{upstream}-ui-%{apiver}.pc
%{_datadir}/%{upstream}-%{apiver}/demo/
%{_datadir}/gir-1.0/Gdaui-%{apiver}.gir
%{_datadir}/glade/
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/libgda-ui-%{apiver}.vapi

%files tools -f gda-browser.lang
%doc %{_datadir}/gtk-doc/html/gda-browser/
%{_bindir}/gda-*
%{_datadir}/%{upstream}-%{apiver}/gda_trml2html
%{_datadir}/%{upstream}-%{apiver}/gda_trml2pdf
%{_datadir}/appdata/*.appdata.xml
%{_datadir}/applications/gda-browser-%{apiver}.desktop
%{_datadir}/applications/gda-control-center-%{apiver}.desktop
%{_datadir}/pixmaps/gda-browser-5.0.png
%{_datadir}/icons/hicolor/*

%files sqlite
%{_libdir}/%{upstream}-%{apiver}/providers/%{upstream}-sqlite.so
%{_datadir}/%{upstream}-%{apiver}/sqlite_specs*.xml

%if 0%{with bdb}
%files bdb
%{_libdir}/libgda-%{apiver}/providers/libgda-bdb.so
%{_datadir}/%{upstream}-%{apiver}/bdb_specs*.xml
%endif

%if 0%{with ldap}
%files ldap
%{_libdir}/%{upstream}-%{apiver}/providers/%{upstream}-ldap.so
%{_datadir}/%{upstream}-%{apiver}/ldap_specs*.xml
%endif

%files sqlcipher
%{_libdir}/%{upstream}-%{apiver}/providers/%{upstream}-sqlcipher.so
%{_datadir}/%{upstream}-%{apiver}/sqlcipher_specs*.xml

%files web
%{_libdir}/%{upstream}-%{apiver}/providers/%{upstream}-web.so
%{_datadir}/%{upstream}-%{apiver}/php/
%{_datadir}/%{upstream}-%{apiver}/web/
%{_datadir}/%{upstream}-%{apiver}/web_specs*.xml

%if 0%{with mysql}
%files mysql
%{_libdir}/libgda-%{apiver}/providers/libgda-mysql.so
%{_datadir}/%{upstream}-%{apiver}/mysql_specs*.xml
%endif

%if 0%{with postgres}
%files postgres
%{_libdir}/libgda-%{apiver}/providers/libgda-postgres.so
%{_datadir}/%{upstream}-%{apiver}/postgres_specs*.xml
%endif

%if 0%{with mdb}
%files mdb
%{_libdir}/libgda-%{apiver}/providers/libgda-mdb.so
%{_datadir}/%{upstream}-%{apiver}/mdb_specs*.xml
%endif

%if 0%{with java}
%files java
%{_libdir}/libgda-%{apiver}/providers/%{upstream}-jdbc.so
%{_libdir}/libgda-%{apiver}/providers/gdaprovider-%{apiver}.jar
%{_datadir}/%{upstream}-%{apiver}/jdbc_specs*.xml
%endif

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.2.10-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.2.10-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 30 2024 Gwyn Ciesla <gwync@protonmail.com> - 1:5.2.10-21
- Patch for modern C.

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.2.10-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.2.10-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Nov 29 2023 Florian Weimer <fweimer@redhat.com> - 1:5.2.10-18
- Further C compatibility fixes (still incomplete)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.2.10-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Mar 23 2023 Hans de Goede <hdegoede@redhat.com> - 1:5.2.10-16
- Rebuild for new mdbtools

* Tue Mar 07 2023 Gwyn Ciesla <gwync@protonmail.com> - 1:5.2.10-15
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.2.10-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec  5 2022 Florian Weimer <fweimer@redhat.com> - 1:5.2.10-13
- Port to C99

* Thu Aug 18 2022 Gwyn Ciesla <gwync@protonmail.com> - 1:5.2.10-12
0 Dep fix

* Mon Aug 15 2022 Gwyn Ciesla <gwync@protonmail.com> - 1:5.2.10-11
- Rebuild

* Fri Aug 05 2022 Gwyn Ciesla <gwync@protonmail.com> - 1:5.2.10-10
- Dependency fixes

* Mon Aug 01 2022 Gwyn Ciesla <gwync@protonmail.com> - 1:5.2.10-9
- Only build Java package on supported platforms.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.2.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Feb 11 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1:5.2.10-7
- Workaround to detect JRE 17 (java 17)

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1:5.2.10-6
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.2.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 22 2021 Gwyn Ciesla <gwync@protonmail.com> - 1:5.2.10-4
- Patch for CVE-2021-39359

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1:5.2.10-3
- Rebuilt with OpenSSL 3.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 10 2021 Hans de Goede <hdegoede@redhat.com> - 1:5.2.10-1
- New upstream bugfix release 5.2.10
- gda_trml2html/2pdf scripts have been ported to python3, restore them
- Rebuild against new mdbtools-libs

* Mon Feb 08 2021 Pavel Raiskup <praiskup@redhat.com> - 1:5.2.9-8
- rebuild for libpq ABI fix rhbz#1908268

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.2.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.2.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 1:5.2.9-5
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.2.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep 12 2019 Fabio Valentini <decathorpe@gmail.com> - 1:5.2.9-3
- Remove report converter functionality that relies on ancient python2 scripts.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 08 2019 Kalev Lember <klember@redhat.com> - 1:5.2.9-1
- Update to 5.2.9

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1:5.2.8-4
- Rebuild for readline 8.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jan 06 2019 Björn Esser <besser82@fedoraproject.org> - 1:5.2.8-2
- Add patch to use explicit python2 shebangs, fixes FTBFS

* Mon Dec 03 2018 Kalev Lember <klember@redhat.com> - 5.2.8-1
- Update to 5.2.8
- Move libgda-ui-plugins to correct subpackage
- Drop appdata override as the appdata file is now upstream
- Drop various rpm scriptlets that are no longer needed these days
- Use make_build and make_install macros
- Use license macro for COPYING
- Enable vala vapi generation
- BR mariadb-connector-c-devel instead of mysql-devel (#1494068)
- Drop bdbsql provider that doesn't build

* Sun Sep 16 2018 Haïkel Guémar <hguemar@fedoraproject.org> - 1:5.2.4-1
- Upstream 5.2.4

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.2.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.2.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.2.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.2.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.2.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 1:5.2.2-12
- Rebuild for readline 7.x

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jul 02 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 1:5.2.2-10
- Add libgda-5.2.2-geninclude.pl.patch (Fix FTBFS).

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:5.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 1:5.2.2-8
- Add an AppData file for the software center

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:5.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 1:5.2.2-6
- Rebuilt for gobject-introspection 1.41.4

* Mon Jun 16 2014 Marcin Juszkiewicz <mjuszkiewicz@redhat.com> - 1:5.2.2-5
- Handle AArch64 as well

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:5.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Brent Baude <baude@us.ibm.com> - 1:5.2.2-3
- Adding ppc64le arch description to spec

* Sun May 18 2014 Peter Robinson <pbrobinson@fedoraproject.org> 1:5.2.2-2
- Rebuild (mdbtools)

* Sat May 17 2014 Kalev Lember <kalevlember@gmail.com> - 1:5.2.2-1
- Update to 5.2.2
- Fix FTBFS with -Werror=format-security (#1037160)
- Fix the build with JRE 1.8
- Install the gdaui Glade catalog

* Wed Apr 23 2014 Tomáš Mráz <tmraz@redhat.com> - 1:5.1.2-5
- Rebuild for new libgcrypt

* Tue Aug  6 2013 Haïkel Guémar <hguemar@fedoraproject.org> - 1:5.1.2-4
- fix FTBFS (RHBZ #992077)
- cleanup rpm conditionals

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:5.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Mar 26 2013 Kalev Lember <kalevlember@gmail.com> - 1:5.1.2-2
- Rebuilt for gtksourceview3 soname bump

* Tue Mar 19 2013 Haïkel Guémar <hguemar@fedoraproject.org> - 1:5.1.2-1
- upstream 5.1.2
- dropped upstreamed patches

* Sun Feb 24 2013 Haïkel Guémar <hguemar@fedoraproject.org> - 1:5.1.1-6
- rebuilt against newer graphviz (RHBZ #914131)
- remove deprecated graphviz API calls in gda-browser
- build system workaround (RHBZ #904790)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:5.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Oct 25 2012 Dan Horák <dan[at]danny.cz> - 1:5.1.1-4
- fix Java detection on secondary arches

* Wed Oct 24 2012 Kalev Lember <kalevlember@gmail.com> - 1:5.1.1-3
- Enable introspection (#869072)

* Mon Oct 22 2012 Kalev Lember <kalevlember@gmail.com> - 1:5.1.1-2
- Add back the epoch
- Build without scrollkeeper support
- Properly obsolete subpackages that got removed in v4->v5 transition
- Fix some rpm directory ownership issues
- Add icon cache scriptlets

* Sun Oct 21 2012 Haïkel Guémar <hguemar@fedoraproject.org> - 5.1.1-1
- upstream 5.1.1 based on libgda5 review (RHBZ #788569)

* Sun Aug  5 2012 Haïkel Guémar <hguemar@fedoraproject.org> - 1:4.2.13-1
- upstream 4.2.13
- bug fixes to MySQL and MDB providers and various minor issues

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.2.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat May 05 2012 Kalev Lember <kalevlember@gmail.com> - 1:4.2.12-3
- switch to libdb-devel
- fix the build with OpenJDK7

* Sun Jan 22 2012 Haïkel Guémar <hguemar@fedoraproject.org> - 1:4.2.12-2
- fix gobject-introspection support
- clean up spec (removed old obsoletes)

* Sun Jan 22 2012 Haïkel Guémar <hguemar@fedoraproject.org> - 1:4.2.12-1
- upstream 4.2.12

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.2.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Nov 26 2011 Haïkel Guémar <hguemar@fedoraproject.org> - 1:4.2.11-1
- upstream 4.1.11
- sqlite provider can load sqlite extensions using "SELECT load_extension ('xxx')"
- remove unused BR

* Thu Aug 25 2011 Haïkel Guémar <hguemar@fedoraproject.org> - 1:4.2.8-1
- upstream 4.2.8
- ldap read-only support is back

* Mon Jul  4 2011 Mark Chappell <tremble@fedoraproject.org> - 1:4.2.5-2
- Rebuild for graphviz so name bump.

* Sun Apr 10 2011 Haïkel Guémar <hguemar@fedoraproject.org> - 1:4.2.5-1
- upstream 4.2.5

* Wed Mar 23 2011 Dan Horák <dan@danny.cz> - 1:4.2.4-3
- rebuilt for mysql 5.5.10 (soname bump in libmysqlclient)

* Tue Feb 22 2011 Haïkel Guémar <hguemar@fedoraproject.org> - 1:4.2.4-2
- fix sqlite loading (RHBZ #673809)

* Thu Feb 17 2011 Haïkel Guémar <hguemar@fedoraproject.org> - 1:4.2.4-1
- upstream 4.2.4

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan  8 2011  <builder@zangetsu.seireitei> - 1:4.2.2-2
- drop sqlite patch: should be fixed in latest xulrunner package

* Tue Nov 30 2010 Haïkel Guémar <hguemar@fedoraproject.org> - 1:4.2.2-1
- Upstream 4.2.2
- Cleaned spec from deprecated providers support
- Fix sqlite3 shared library loading (RHBZ #658471)

* Tue Oct 26 2010 Haïkel Guémar <hguemar@fedoraproject.org> - 1:4.2.0-1
- Update to upstream 4.2.0
- New provider: sqlcipher (SQLite encryption extension)
- New patch fixing 4.2.0 build issue
- Disable GObject introspection since it's broken

* Wed Jun 16 2010 Haïkel Guémar <hguemar@fedoraproject.org> - 1:4.1.6-1
- Update to upstream 4.1.6
- Add new BR: gnome-doc-utils
- Dropped BR: gir-repository

* Tue Apr 27 2010 Haïkel Guémar <hguemar@fedoraproject.org> - 1:4.1.4-1
- Update to upstream 4.1.4 (required by Glom)
- Added web provider and ui subpackages
- Added new BR (gtk2, unique, goocanvas, graphviz) for libgda-ui

* Thu Apr 22 2010 Haïkel Guémar <hguemar@fedoraproject.org> - 1:4.0.8-2
- add gir descriptions files

* Thu Apr 22 2010 Haïkel Guémar <hguemar@fedoraproject.org> - 1:4.0.8-1
- Update to upstream 4.0.8

* Thu Feb 18 2010 Denis Leroy <denis@poolshark.org> - 1:4.0.7-1
- Update to upstream 4.0.7

* Mon Jan 18 2010 Denis Leroy <denis@poolshark.org> - 1:4.0.6-1
- Update to upstream 4.0.6
- Added Java JDBC provider subpackage

* Sat Nov  7 2009 Denis Leroy <denis@poolshark.org> - 1:4.0.5-1
- Update to upstream 4.0.5
- Source URL fix

* Tue Sep 15 2009 Denis Leroy <denis@poolshark.org> - 1:4.0.4-1
- Update to upstream version 4.0.4

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 1:4.0.2-3
- rebuilt with new openssl

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jun 25 2009 Denis Leroy <denis@poolshark.org> - 1:4.0.2-1
- Update to upstream 4.0.2
- Use system sqlite library

* Mon Mar 23 2009  <denis@poolshark.org> - 1:4.0.0-1
- Update to upstream 4.0.0

* Wed Mar  4 2009 Denis Leroy <denis@poolshark.org> - 1:3.99.12-1
- Update to upstream 3.99.12

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.99.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Feb 14 2009 Denis Leroy <denis@poolshark.org> - 1:3.99.11-1
- Update to 3.99.11 (many bug fixes)

* Fri Jan 16 2009 Denis Leroy <denis@poolshark.org> - 1:3.99.8-1
- Switch to 4.0 ABI
- Update to upstream 3.99.8
- Patch updates (upstreamed and ported)
- Added JAVA package flag, currently disabled

* Mon Oct 27 2008 Denis Leroy <denis@poolshark.org> - 1:3.1.2-6
- Added patch to fix providers path on x86_64 (#468510)

* Thu Jul 10 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1:3.1.2-5
- Rebuild against new db4-4.7

* Tue Jun 17 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 1:3.1.2-4
- Rebuild against new freetds

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1:3.1.2-3
- Autorebuild for GCC 4.3

* Sat Jan 26 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 1:3.1.2-2
- Rebuid now that the system sqlite has column metadata enabled, so that we
  use the system version instead of our own private copy (bz 430258)

* Fri Jan 25 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 1:3.1.2-1
- New upstream release 3.1.2 (needed for new gnumeric)
- Drop upstreamed / no longer needed patches

* Thu Dec 06 2007 Release Engineering <rel-eng at fedoraproject dot org> - 3.0.1-6
- Rebuild for deps

* Sun Oct 21 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1:3.0.1-5
- Rebuild to fix untranslated strings on x86_64 in
  /usr/share/libgda-3.0/sqlite_specs_drop_index.xml
  which caused multilib problems (bz 342101)

* Fri Aug 17 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1:3.0.1-4
- Fix building on ppc64 again (patch configure not configure.in, now we are
  no longer running autoconf)

* Wed Aug 15 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1:3.0.1-3
- Enable microsoft access (mdb) support now that mdbtools is in Fedora
- Enable xBase (dBase, Clipper, FoxPro) support, it seems that xbase has been
  available for quite a while now
- Switch from using mysqlclient10 to using mysql-libs for the msql provider

* Wed Aug  8 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1:3.0.1-2
- Build against system sqlite instead of own private copy (this is possible now
  that the system sqlite is of a high enough version)
- Enable FreeTDS provider (FreeTDS is in Fedora now)
- Update License tag for new Licensing Guidelines compliance

* Sun May 27 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1:3.0.1-1
- New upstream release 3.0.1
- Remove mono bindings sub-package as upstream no longer includes them

* Thu May 10 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1:1.9.100-12
- Don't build mono/sharp bits on ppc64
- Fixup packaging of sharp bindings to match the mono packaging guidelines

* Fri Dec 15 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1:1.9.100-11
- Rebuild for new postgres

* Mon Aug 28 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1:1.9.100-10
- FE6 Rebuild

* Tue Jun 20 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1:1.9.100-9
- Add BuildRequires: libtool hopefully _really_ fixing building with the new
  stripped mock config. (Drop BR: autoconf which is implied by BR: automake).

* Thu Jun 15 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1:1.9.100-8
- Add BuildRequires: automake, autoconf to fix building with the new even more
  stripped mock config.

* Sat Jun 10 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1:1.9.100-7
- Add BuildRequires: gettext, bison, flex, gamin-devel to fix building with
  new stripped mock config.

* Thu May 11 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1:1.9.100-6
- Move Obsoletes and Provides for plugins out of the plugins %%description,
  so that they actually Obsolete and Provide instead of showing up in rpm -qi
  (bug 191213).

* Thu May  4 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1:1.9.100-5
- Add patch3 fixing a couple of x86_64 bugs (bz 190366)

* Mon Feb 13 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1:1.9.100-4
- Bump release and rebuild for new gcc4.1 and glibc.
- Make sqlite plugin use system sqlite not build in version
- Make sqlite plugin a seperate package again
- Attempt to properly install C-sharp/mono bindings
- Add %%{?dist} for consistency with my other packages
- Remove static lib from -devel package

* Tue Jan 17 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1:1.9.100-3
- Make -sharp package Require the main package.

* Mon Jan 16 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1:1.9.100-2
- Remove unneeded requires (.so reqs are automaticly picked up by rpm).
- Add BuildRequires for building libgda-sharp

* Sun Nov 27 2005 Hans de Goede <j.w.r.degoede@hhs.nl> 1:1.9.100-1
- New upstream version
- Drop 4 intergrated patches
- Removed sqlite configurability, it is now an internal part of the upstream
  sources.

* Fri Aug  5 2005 Hans de Goede <j.w.r.degoede@hhs.nl> 1:1.2.0-8
- Remove libgda.la file from devel package.

* Sat Jun 25 2005 Hans de Goede <j.w.r.degoede@hhs.nl> 1:1.2.0-7
- Added Patch4: libgda-1.2.0-libdir.patch which fixes loading of
  database providers on platforms with a lib64 dir. Thanks to:
  Bas Driessen <bas.driessen@xobas.com> for the patch.
- Enabled building of libgda-ldap and libgda-sqlite by default.

* Tue Jun 21 2005 Hans de Goede <j.w.r.degoede@hhs.nl> 1:1.2.0-6
- rebuild so that we depend on the proper version of libpq.so (#160917)
- change names of database providers from gda-xxx to libgda-xxx (#160917)

* Wed Mar  2 2005 Caolan McNamara <caolanm@redhat.com> 1:1.2.0-5
- rebuild with gcc4

* Fri Feb 11 2005 Caolan McNamara <caolanm@redhat.com> 1:1.2.0-4
- well, that was moronic

* Thu Feb 10 2005 Caolan McNamara <caolanm@redhat.com> 1:1.2.0-3
- bandaid

* Wed Feb  9 2005 Jeremy Katz <katzj@redhat.com> - 1:1.2.0-2
- rebuild to try to fix broken dep

* Fri Feb 4 2005 Caolan McNamara <caolanm@redhat.com> 1:1.2.0-1
- bump to latest version
- drop integrated break warning patch
- update configure patch

* Wed Jan 12 2005 Tim Waugh <twaugh@redhat.com> 1:1.0.4-5
- Rebuilt for new readline.

* Sat Oct 30 2004 Caolan McNamara <caolanm@redhat.com> 1:1.0.4-4
- Use mysqlclient10

* Fri Oct  8 2004 Caolan McNamara <caolanm@redhat.com> 1:1.0.4-3
- #rh135043# Extra BuildRequires

* Thu Sep  9 2004 Bill Nottingham <notting@redhat.com> 1:1.0.4-2
- %%defattr

* Thu Aug 12 2004 Caolan McNamara <caolanm@redhat.com> 1:1.0.4-1
- Initial Red Hat import
- patch for missing break statement
- fixup devel package requirement pickiness
- autoconf patch to pick up correct mysql path from mysql_config (e.g. x64)
- autoconf patch to just look in the normal place for postgres first

* Tue Mar 11 2003 David Hollis <dhollis@davehollis.com>
- Fix --with-tds & --without-tds to match what configure wants

* Tue Jan 28 2003 Yanko Kaneti <yaneti@declera.com>
- Remove the idl path
- Include gda-config man page
- add --without-* for disabled providers
- package and use the omf/scrollkeeper bits

* Tue Dec 31 2002 David Hollis <dhollis@davehollis.com>
- Added sqlite-devel buildreq
- Include gda-config-tool man page

* Mon Aug 19 2002 Ben Liblit <liblit@acm.org>
- Fixed version number substitutions

- Removed some explicit "Requires:" prerequisites that RPM will figure
  out on its own.  Removed explicit dependency on older MySQL client
  libraries

- Required that the ODBC development package be installed if we are
  building the ODBC provider

- Created distinct subpackages for each provider, conditional on that
  provider actually being enabled; some of these will need to be
  updated as the family of available providers changes

- Updated files list to match what "make install" actually installs

- Added URL tag pointing to GNOME-DB project's web site

* Tue Feb 26 2002 Chris Chabot <chabotc@reviewboard.com>
- Added defines and configure flags for all supported DB types

* Mon Feb 25 2002 Chris Chabot <chabotc@reviewboard.com>
- Cleaned up formatting
- Added Requirements
- Added defines for postgres, mysql, odbc support

* Thu Feb 21 2002 Chris Chabot <chabotc@reviewboard.com>
- Initial spec file
