Name:           yaz
Version:        5.34.3
Release:        2%{?dist}
Summary:        Z39.50/SRW/SRU toolkit
# SPDX confirmed
License:        BSD-3-Clause
URL:            http://www.indexdata.com/yaz/
Source0:        http://ftp.indexdata.com/pub/yaz/yaz-%{version}.tar.gz
# https://github.com/indexdata/yaz/issues/133
# Avoid keyword bool usage on C23
Patch0:		yaz-5.34.3-c23-keyword.patch

BuildRequires:  gcc
BuildRequires:  bison
BuildRequires:  make

# When autoreconf is needed:
%if 0
BuildRequires:  autoconf
BuildRequires:  automake
%endif

BuildRequires:  pkgconfig(libexslt)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(hiredis)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(libmemcached)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libxslt)

BuildRequires:  ncurses-devel
BuildRequires:  readline-devel
BuildRequires:  /usr/bin/tclsh

Requires:       lib%{name}%{?_isa} = %{version}-%{release}

%description
YAZ is a programmers toolkit supporting the development of Z39.50/SRW/SRU 
clients and servers. Z39.50-2003 (version 3) as well as SRW/SRU version 1.1 
are supported in both the client and server roles. The SOLR webservice is 
supported in the client role through the ZOOM API.

The current version of YAZ includes support for the industry standard ZOOM 
API for Z39.50. This API vastly simplifies the process of writing new clients 
using YAZ, and it reduces your dependency on any single toolkit. YAZ can be 
used by itself to build Z39.50 applications in C.For programmers preferring 
another language, YAZ has three language bindings to commonly used application
development languages.

This package contains both a test-server and clients (normal & ssl).

%package -n     lib%{name}
Summary:        Shared libraries for %{name}

%description -n lib%{name}
This packages contains shared libraries for %{name}.

%package -n     lib%{name}-devel
Summary:        Development files for %{name}
Requires:       lib%{name}%{?_isa} = %{version}-%{release}

%description -n lib%{name}-devel
This package contains libraries and header files for
developing applications that use lib%{name}.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description    doc
This package contains documentation for %{name}, a Z39.50 protocol
server and client.

%prep
%setup -q
%patch -P0 -p1 -b .c23

%build
sed -i.rpath configure \
	-e 's|hardcode_libdir_flag_spec=|hardcode_libdir_flag_spec_goodby=|' \
	-e '\@sys_lib_dlsearch_path_spec=@s|/lib /usr/lib|/lib /usr/lib %{_libdir} /%{_lib}|' \
	%{nil}

%configure \
        --enable-shared \
        --with-memcached \
        --with-redis \
        --disable-static \
        %{nil}

%make_build

%install
%make_install

# Remove cruft
find %{buildroot} -name '*.*a' -delete -print

%check
make check

%ldconfig_scriptlets -n lib%{name}

%ldconfig_scriptlets -n lib%{name}

%files
%doc NEWS
%doc README.md
%license LICENSE
%{_bindir}/yaz-client
%{_bindir}/yaz-iconv
%{_bindir}/yaz-icu
%{_bindir}/yaz-illclient
%{_bindir}/yaz-json-parse
%{_bindir}/yaz-marcdump
%{_bindir}/yaz-record-conv
%{_bindir}/yaz-url
%{_bindir}/yaz-ztest
%{_bindir}/zoomsh
%{_mandir}/man1/yaz-client.*
%{_mandir}/man1/yaz-iconv.*
%{_mandir}/man1/yaz-icu.*
%{_mandir}/man1/yaz-illclient.*
%{_mandir}/man1/yaz-json-parse.*
%{_mandir}/man7/yaz-log.*
%{_mandir}/man1/yaz-marcdump.*
%{_mandir}/man1/yaz-record-conv.*
%{_mandir}/man1/yaz-url.*
%{_mandir}/man8/yaz-ztest.*
%{_mandir}/man1/zoomsh.*

%files -n lib%{name}
%license LICENSE
%{_libdir}/libyaz.so.5*
%{_libdir}/libyaz_icu.so.5*
%{_libdir}/libyaz_server.so.5*
%{_mandir}/man7/yaz.*
%{_mandir}/man7/bib1-attr.*

%files -n lib%{name}-devel
%doc NEWS README.md
%{_bindir}/yaz-asncomp
%{_bindir}/yaz-config
%{_libdir}/pkgconfig/*
%{_libdir}/*.so
%{_includedir}/%{name}/
%{_datadir}/yaz/
%{_datadir}/aclocal/*
%{_mandir}/man1/yaz-asncomp.*
%{_mandir}/man1/yaz-config.*

%files -n %{name}-doc
%{_pkgdocdir}

%changelog
* Tue Jan 14 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 5.34.3-2
- Fix compilation with C23 with bool keyword

* Thu Jan 09 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 5.34.3-1
- 5.34.3

* Mon Dec 09 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 5.34.2-2
- Explicitly add icu-uc pkgconf deps for yaz-icu

* Fri Sep 20 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 5.34.2-1
- 5.34.2

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.34.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 19 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 5.34.1-1
- 5.34.1

* Sat May 11 2024 Kevin Fenzi <kevin@scrye.com> - 5.34.0-9
- rebuild for hiredis soname bump

* Wed Jan 31 2024 Pete Walter <pwalter@fedoraproject.org> - 5.34.0-8
- Rebuild for ICU 74

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.34.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 5.34.0-6
- Use %%ldconfig_scriptlets instead of /usr/sbin/ldconfig
  (ref: DNF5 file deps change: bug 2180842)

* Mon Nov 20 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 5.34.0-5
- Fix header file inclusion for libxml2 2.12.0
- Fix header file inclusion for glibc 2.39

* Sat Jul 22 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 5.34.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 František Zatloukal <fzatlouk@redhat.com> - 5.34.0-3
- Rebuilt for ICU 73.2

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.34.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jan 13 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 5.34.0-1
- 5.34.0

* Sat Dec 31 2022 Pete Walter <pwalter@fedoraproject.org> - 5.33.0-2
- Rebuild for ICU 72

* Wed Dec 14 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 5.33.0-1
- 5.33.0

* Mon Aug 01 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 5.32.0-3
- Rebuilt for ICU 71.1

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.32.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 5.32.0-1
- 5.32.0

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.31.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 18 2022 Kevin Fenzi <kevin@scrye.com> - 5.31.1-3
- Rebuild for hiredis 1.0.2

* Thu Dec 23 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 5.31.1-2
- Make yaz binary rpm Requires libyaz rpm

* Mon Dec 20 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 5.31.1-1
- 5.31.1

* Tue Nov  2 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 5.31.0-1
- 5.31.0

* Tue Nov  2 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 5.14.11-27
- Remove rpath harder, don't use chrpath

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.14.11-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu May 20 2021 Pete Walter <pwalter@fedoraproject.org> - 5.14.11-25
- Rebuild for ICU 69

* Wed May 19 2021 Pete Walter <pwalter@fedoraproject.org> - 5.14.11-24
- Rebuild for ICU 69

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.14.11-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.14.11-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 15 2020 Pete Walter <pwalter@fedoraproject.org> - 5.14.11-21
- Rebuild for ICU 67

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.14.11-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 01 2019 Pete Walter <pwalter@fedoraproject.org> - 5.14.11-19
- Rebuild for ICU 65

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.14.11-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 5.14.11-17
- Rebuild for readline 8.0

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.14.11-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Pete Walter <pwalter@fedoraproject.org> - 5.14.11-15
- Rebuild for ICU 63

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.14.11-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Pete Walter <pwalter@fedoraproject.org> - 5.14.11-13
- Rebuild for ICU 62

* Mon Apr 30 2018 Pete Walter <pwalter@fedoraproject.org> - 5.14.11-12
- Rebuild for ICU 61.1

* Tue Mar 27 2018 Till Maas <opensource@till.name> - 5.14.11-11
- rebuilt to drop tcp_wrappers dependency
  https://bugzilla.redhat.com/show_bug.cgi?id=1518798

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.14.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 30 2017 Pete Walter <pwalter@fedoraproject.org> - 5.14.11-9
- Rebuild for ICU 60.1

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.14.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.14.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.14.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 5.14.11-5
- Rebuild for readline 7.x

* Fri Apr 15 2016 David Tardon <dtardon@redhat.com> - 5.14.11-4
- rebuild for ICU 57.1

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.14.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 28 2015 David Tardon <dtardon@redhat.com> - 5.14.11-2
- rebuild for ICU 56.1

* Sat Oct 24 2015 Christopher Meng <rpm@cicku.me> - 5.14.11-1
- Update to 5.14.11

* Tue Sep 15 2015 Christopher Meng <rpm@cicku.me> - 5.14.9-1
- Update to 5.14.9

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 07 2015 Christopher Meng <rpm@cicku.me> - 5.13.0-1
- Update to 5.13.0

* Thu Feb 26 2015 Christopher Meng <rpm@cicku.me> - 5.9.1-2
- Drop openssl-devel from libyaz-devel as yaz is linked with gnutls already

* Thu Feb 26 2015 Guido Grazioli <guido.grazioli@gmail.com> - 5.9.1-1
- Update to 5.9.1
- Remove rpaths with chrpath

* Wed Feb 04 2015 Petr Machata <pmachata@redhat.com> - 5.8.1-2
- Bump for rebuild.

* Mon Feb 02 2015 Christopher Meng <rpm@cicku.me> - 5.8.1-1
- Update to 5.8.1

* Mon Jan 26 2015 David Tardon <dtardon@redhat.com> - 5.6.0-2
- rebuild for ICU 54.1

* Tue Nov 18 2014 Christopher Meng <rpm@cicku.me> - 5.6.0-1
- Update to 5.6.0

* Tue Aug 26 2014 David Tardon <dtardon@redhat.com> - 5.4.1-2
- rebuild for ICU 53.1

* Fri Aug 22 2014 Christopher Meng <rpm@cicku.me> - 5.4.1-1
- Update to 5.4.1

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jul 18 2014 Christopher Meng <rpm@cicku.me> - 5.3.0-2
- Enable GnuTLS support.

* Thu Jul 17 2014 Christopher Meng <rpm@cicku.me> - 5.3.0-1
- Update to 5.3.0

* Mon Jun 30 2014 Christopher Meng <rpm@cicku.me> - 5.2.1-1
- Update to 5.2.1

* Sun Jun 15 2014 Christopher Meng <rpm@cicku.me> - 5.2.0-1
- Update to 5.2.0

* Mon Jun 09 2014 Christopher Meng <rpm@cicku.me> - 5.1.3-1
- Update to 5.1.3

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 05 2014 Christopher Meng <rpm@cicku.me> - 5.1.1-1
- Update to 5.1.1

* Sun Apr 20 2014 Christopher Meng <rpm@cicku.me> - 5.1.0-1
- Update to 5.1.0

* Tue Mar 25 2014 Christopher Meng <rpm@cicku.me> - 5.0.21-1
- Update to 5.0.21
- Build with memcached support for ZOOM caching.
- SPEC cleanup, dependencies cleanup, redundant files cleanup.

* Fri Feb 14 2014 David Tardon <dtardon@redhat.com> - 4.2.56-4
- rebuild for new ICU

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.56-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr 30 2013 Dan Horák <dan[at]danny.cz> 4.2.56-2
- add upstream fix for platforms where the char type is unsigned by default

* Mon Apr 29 2013 Peter Robinson <pbrobinson@fedoraproject.org> 4.2.56-1
- Update to 4.2.56

* Tue Apr 02 2013 Guido Grazioli <guido.grazioli@gmail.com> - 4.2.51-1
- Update to 4.2.51
- Remove unneeded patch

* Fri Feb 01 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 4.2.33-3
- Rebuild for icu 50

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.33-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 14 2012 Guido Grazioli <guido.grazioli@gmail.com> - 4.2.33-1
- Update to 4.2.33

* Mon Apr 23 2012 Guido Grazioli <guido.grazioli@gmail.com> - 4.2.29-2
- Rebuilt for icu soname bump

* Mon Apr 09 2012 Guido Grazioli <guido.grazioli@gmail.com> - 4.2.29-1
- Update to 4.2.29

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Sep 30 2011 Guido Grazioli <guido.grazioli@gmail.com> - 4.2.17-1
- Update to 4.2.17 (minor bugfixes)

* Mon Sep 12 2011 Guido Grazioli <guido.grazioli@gmail.com> - 4.2.14-1
- Upstream 4.2.14

* Mon Sep 12 2011 Guido Grazioli <guido.grazioli@gmail.com> - 4.2.4-2
- Rebuild against icu 4.8.1

* Tue Jul 19 2011 Guido Grazioli <guido.grazioli@gmail.com> - 4.2.4-1
- Upstream 4.2.4

* Mon May 09 2011 Guido Grazioli <guido.grazioli@gmail.com> - 4.1.7-1
- Upstream 4.1.7 
- Improved description

* Mon Mar 07 2011 Caolán McNamara <caolanm@redhat.com> - 4.0.12-3
- Rebuild against icu 4.6

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Nov 06 2010 Guido Grazioli <guido.grazioli@gmail.com> - 4.0.12-1
- Upstream 4.0.12 (various bugfixes)
- Remove unused patch, fixed upstream

* Sun Apr 04 2010 Guido Grazioli <guido.grazioli@gmail.com> - 4.0.2-1
- Upstream 4.0.2 (major version release)
- Add patch for explicit DSO linking
- Split documentation to -doc subpackage

* Fri Apr 02 2010 Caolán McNamara <caolanm@redhat.com> - 3.0.49-2
- Rebuild against icu 4.4

* Thu Oct 01 2009 Guido Grazioli <guido.grazioli@gmail.com> - 3.0.49-1
- Upstream 3.0.49 (bugfixes and feature enhancements)
- Require pkgconfig for libyaz-devel (guidelines MUST)

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.46-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jun 27 2009 Konstantin Ryabitsev <icon@fedoraproject.org> - 3.0.46-1
- Update to 3.0.46 (miscellaneous bugfixes)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.41-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 29 2008 Konstantin Ryabitsev <icon@fedoraproject.org> - 3.0.41-1
- Upstream 3.0.41
- Always use system libtool
- Remove TODO from docs
- Package bib1-attr.7 with libyaz

* Mon Jun 30 2008 Konstantin Ryabitsev <icon@fedoraproject.org> - 3.0.34-1
- Upstream 3.0.34

* Sat May 10 2008 Konstantin Ryabitsev <icon@fedoraproject.org> - 3.0.26-1
- Upstream 3.0.26

* Sat Feb 02 2008 Konstantin Ryabitsev <icon@fedoraproject.org> - 3.0.24-1
- Upstream 3.0.24
- Remove ziffy, as it's no longer part of this package
- Build with icu, available since 3.0.10

* Fri Aug 17 2007 Konstantin Ryabitsev <icon@fedoraproject.org> - 3.0.8-1
- New upstream 3.0.8

* Fri Jun 15 2007 Konstantin Ryabitsev <icon@fedoraproject.org> - 3.0.6-1
- New major upstream version 3.0.6

* Sun Apr 01 2007 Konstantin Ryabitsev <icon@fedoraproject.org> - 2.1.54-1
- Upstream 2.1.54

* Sat Jan 27 2007 Konstantin Ryabitsev <icon@fedoraproject.org> - 2.1.48-1
- Upstream 2.1.48

* Sun Dec 17 2006 Konstantin Ryabitsev <icon@fedoraproject.org> - 2.1.40-1
- Upstream 2.1.40

* Sat Oct 28 2006 Konstantin Ryabitsev <icon@fedoraproject.org> - 2.1.36-1
- Upstream 2.1.36

* Sun Sep 03 2006 Konstantin Ryabitsev <icon@fedoraproject.org> - 2.1.26-1.1
- Mass rebuild for FC6

* Tue Aug 15 2006 Konstantin Ryabitsev <icon@fedoraproject.org> - 2.1.26-1
- Version 2.1.26
- Kill all tabs

* Tue Jun 20 2006 Konstantin Ryabitsev <icon@fedoraproject.org> - 2.1.22-1
- Version 2.1.22
- Libtoolize correctly
- BuildRequire libxslt
- BuildRequire tcp_wrappers
- Enable pth in configure
- Add %%check routine

* Mon Dec 12 2005 Konstantin Ryabitsev <icon@fedoraproject.org> - 2.1.10-1
- Initial packaging
