Name:           libzdb
Version:        3.4.0
Release:        3%{?dist}
Summary:        Small, easy to use Database Connection Pool Library
# Automatically converted from old format: GPLv3+ and MIT - review is highly recommended.
License:        GPL-3.0-or-later AND LicenseRef-Callaway-MIT
URL:            http://www.tildeslash.com/libzdb/
Source0:        http://www.tildeslash.com/%{name}/dist/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  flex
BuildRequires:  mariadb-connector-c-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  libpq-devel
BuildRequires:  sqlite-devel >= 3.6.12
BuildRequires: make

%description
The Zild C Database Library implements a small, fast, and easy to use database
API with thread-safe connection pooling. The library can connect transparently
to multiple database systems, has zero configuration and connections are
specified via a standard URL scheme.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

# Errant file
rm -f doc/api-docs/._*

%build
%configure --disable-static --enable-protected --enable-sqliteunlock
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%ldconfig_scriptlets

%files
%doc AUTHORS CHANGES COPYING README
%{_libdir}/%{name}.so.*

%files devel
%{_includedir}/zdb/
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/zdb.pc
%doc doc/api-docs

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 3.4.0-2
- convert license to SPDX

* Thu Aug 22 2024 Julien Enselme - 3.4.0-1
- Update to 3.4.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec 30 2022 Julien Enselme <jujens@jujens.eu> - 3.2.3-1
- Update to 3.2.3

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jun 18 2022 Julien Enselme <jujens@jujens.eu> - 3.2.2-1
- Update to 3.2.2

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Feb 08 2021 Pavel Raiskup <praiskup@redhat.com> - 3.2-6
- rebuild for libpq ABI fix rhbz#1908268

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 13 2019 Julien Enselme <jujens@jujens.eu> - 3.2-1
- Update to 3.2

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Sep 26 2017 Julien Enselme <jujens@jujens.eu> - 3.1-5
- Rely on mariadb-connector-c-devel instead of mysql-devel

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Oct 23 2016 Julien Enselme <jujens@jujens.eu> - 3.1-1
- Update to 3.1
- Unretire package

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar 20 2014 Christopher Meng <rpm@cicku.me> - 3.0-2
- Enable SQLite unlock notification API support.

* Thu Mar 13 2014 Bernard Johnson <bjohnson@symetrix.com> - 3.0-1
- v 3.0 (bz #1049219)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 05 2011 Bernard Johnson <bjohnson@symetrix.com> - 2.8.1-1
- bump to 2.8.1 which fixes a Oracle driver transaction memory leak

* Wed Mar 23 2011 Dan Horák <dan@danny.cz> - 2.8-2
- rebuilt for mysql 5.5.10 (soname bump in libmysqlclient)

* Tue Feb 22 2011 Bernard Johnson <bjohnson@symetrix.com> - 2.8-1
- v 2.8

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 08 2010 Bernard Johnson <bjohnson@symetrix.com> - 2.7-1
- v 2.7
- change BR from flex to flex-static for F15 (bz #660879)

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 2.6-3
- rebuilt with new openssl

* Thu Jul 30 2009 Jesse Keating <jkeating@redhat.com> - 2.6-2
- Bump for F12 mass rebuild

* Sun Jul 05 2009 Bernard Johnson <bjohnson@symetrix.com> - 2.6-1
- v 2.6

* Thu Jun 04 2009 Bernard Johnson <bjohnson@symetrix.com> - 2.5-1
- remove EXCEPTIONS notice
- v 2.5

* Sat Mar 07 2009 Bernard Johnson <bjohnson@symetrix.com> - 2.4-3
- fix typo in requires
- bz #474044

* Wed Feb 25 2009 Bernard Johnson <bjohnson@symetrix.com> - 2.4-2
- add a notice to EXCEPTIONS that dual licensing is not available in Fedora

* Mon Feb 16 2009 Bernard Johnson <bjohnson@symetrix.com> - 2.4-1
- v 2.4
- remove patches required for 2.3
- drop EXCEPTIONS as noted in review ticket

* Thu Feb 05 2009 Bernard Johnson <bjohnson@symetrix.com> - 2.3-1
- v 2.3

* Thu Dec 04 2008 Bernard Johnson <bjohnson@symetrix.com> - 2.2.3-2
- disable static build by default
- remove release version from soname
- move headers to %%{_includedir}/libzdb/

* Thu Nov 13 2008 Bernard Johnson <bjohnson@symetrix.com> - 2.2.3-1
- initial build
