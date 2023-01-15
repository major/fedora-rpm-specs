%global major                   28
%global cppmajor                12

# Notes about rpmlint
# - crypto-policy-non-compliance-gnutls-{1,2} fixed with patch
#   libprelude-5.2.0-gnutls_priority_set_direct.patch

Name:           libprelude
Version:        5.2.0
Release:        16%{?dist}
Summary:        Secure Connections between all Sensors and the Prelude Manager
License:        LGPL-2.1+
URL:            https://www.prelude-siem.org/
Source0:        https://www.prelude-siem.org/pkg/src/5.2.0/%{name}-%{version}.tar.gz
# See BZ 1908783
Source1:        config.h.patch
# https://www.prelude-siem.org/issues/860
Patch0:         libprelude-5.2.0-ruby_vendorarchdir.patch
# https://www.prelude-siem.org/issues/862
Patch1:         libprelude-5.2.0-gnutls_priority_set_direct.patch
# https://www.prelude-siem.org/issues/863
Patch2:         libprelude-5.2.0-fsf_address.patch
# https://www.prelude-siem.org/issues/865
Patch3:         libprelude-5.2.0-fix_timegm.patch
# https://www.prelude-siem.org/issues/885
Patch4:         libprelude-5.2.0-fix_pthread_atfork.patch
# https://www.prelude-siem.org/issues/887
Patch5:         libprelude-5.2.0-fix_prelude_tests_timer.patch
Patch6:         libprelude-5.2.0-fix_gtkdoc_1.32.patch
Patch7:         libprelude-5.2.0-linking.patch
Patch8:         libprelude-5.2.0-fix_libprelude-error_on_gnu.patch
Patch9:         libprelude-5.2.0-disable_test-poll_on_kfreebsd.patch
Patch10:        libprelude-5.2.0-fix-test_rwlock1.patch
# https://github.com/swig/swig/issues/1689
# https://github.com/swig/swig/pull/1692
# For now, add a minimum patch to support ruby2.7
Patch11:        libprelude-5.2.0-ruby27.patch
# Remove unneded libraries from libprelude-config --libs (bz#1830473)
Patch12:        libprelude-5.2.0-clean_libprelude-config.patch
# #1973946
Patch13:        libprelude-5.2.0-fix-PyIOBase_Type.patch
Patch14:        libprelude-configure-c99.patch
BuildRequires: make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  bison
BuildRequires:  chrpath
BuildRequires:  flex
BuildRequires:  gtk-doc
BuildRequires:  glib2-devel
BuildRequires:  swig
BuildRequires:  libgpg-error-devel
BuildRequires:  libtool-ltdl-devel
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  python3-devel
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(lua) >= 5.2
BuildRequires:  pkgconfig(ruby)
BuildRequires:  pkgconfig(zlib)

%ifnarch s390 ppc64 ppc64le
BuildRequires:  valgrind
%endif

# Upstream do not use explicit version of gnulib, just checkout
# and update files. In libprelude 5.2.0, the checkout has been done
# on 2018-09-03
Provides:       bundled(gnulib) = 20180903

%description
Libprelude is a collection of generic functions providing communication
between all Sensors, like IDS (Intrusion Detection System), and the Prelude
Manager. It provides a convenient interface for sending and receiving IDMEF
(Information and Event Message Exchange Format) alerts to Prelude Manager with
transparent SSL, fail-over and replication support, asynchronous events and
timer interfaces, an abstracted configuration API (hooking at the command-line,
the configuration line, or wide configuration, available from the Manager), and
a generic plugin API. It allows you to easily turn your favorite security
program into a Prelude sensor.

%package devel
Summary:        Libraries and headers for developing Prelude sensors
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libtool-ltdl-devel
Requires:       pkgconfig(gnutls)
Provides:       prelude-devel = %{version}-%{release}

%description devel
Libraries and headers you can use to develop Prelude sensors using the Prelude
Library. Libprelude is a collection of generic functions providing
communication between all Sensors, like IDS (Intrusion Detection System),
and the Prelude Manager. It provides a convenient interface for sending and
receiving IDMEF (Information and Event Message Exchange Format) alerts to
Prelude Manager with transparent SSL, fail-over and replication support,
asynchronous events and timer interfaces, an abstracted configuration API
(hooking at the command-line, the configuration line, or wide configuration,
available from the Manager), and a generic plugin API. It allows you to easily
turn your favorite security program into a Prelude sensor.

%package -n prelude-tools
Summary:        Command-line tools for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n prelude-tools
Provides a convenient interface for sending alerts to Prelude
Manager.

%package -n python3-prelude
Summary:        Python 3 bindings for prelude
Requires:       %{name}%{?_isa} = %{version}-%{release}
%{?python_provide:%python_provide python3-prelude}

%description -n python3-prelude
Provides python 3 bindings for prelude.

%package -n perl-prelude
Summary:        Perl bindings for prelude
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n perl-prelude
Provides perl bindings for prelude.

%package -n ruby-prelude
Summary:        Ruby bindings for prelude
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n ruby-prelude
Provides ruby bindings for prelude.

%package -n lua-prelude
Summary:        Lua bindings for prelude
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       lua

%description -n lua-prelude
Provides Lua bindings for prelude generated by SWIG.

%package doc
Summary:        Documentation for prelude
BuildArch:      noarch

%description doc
Provides documentation for prelude generated by gtk-doc.

%prep
%autosetup -p1

%build
%configure \
    --without-included-ltdl \
    --disable-static \
    --enable-shared \
    --with-swig \
    --without-python2 \
    --with-python3 \
    --with-ruby \
    --with-lua \
    --with-perl-installdirs=vendor \
    --without-included-regex \
    --includedir=%{_includedir}/%{name} \
    --enable-gtk-doc \
    --disable-rpath \
    --with-html-dir=%{_docdir}/%{name}-devel
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
%make_build

%install
%make_install

#chrpath -d %{buildroot}%{_libdir}/*.so.*
chmod 755 %{buildroot}%{_libdir}/perl5/vendor_perl/auto/Prelude/Prelude.so
chrpath -d %{buildroot}%{_libdir}/perl5/vendor_perl/auto/Prelude/Prelude.so

find %{buildroot} -name '*.la' -delete
find %{buildroot} -name 'perllocal.pod' -delete
find %{buildroot} -name '.packlist' -delete

patch -d %{buildroot}%{_includedir}/libprelude/ -p0 < %SOURCE1

# Enable test again after fixing #1629893
#%check
#make check

%ldconfig_scriptlets -n %{name}

%files
%{_libdir}/%{name}.so.%{major}
%{_libdir}/%{name}.so.%{major}.*
%{_libdir}/%{name}cpp.so.%{cppmajor}
%{_libdir}/%{name}cpp.so.%{cppmajor}.*
%license COPYING LICENSE.README HACKING.README
%doc AUTHORS README NEWS

%files devel
%{_datadir}/%{name}
%{_bindir}/%{name}-config
%{_libdir}/%{name}.so
%{_libdir}/%{name}cpp.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}
%{_datadir}/aclocal/%{name}.m4
%{_mandir}/man1/%{name}-config.1.gz

%files -n prelude-tools
# Force default attrs because libprelude force others
%defattr(- , root, root, 755)
%{_bindir}/prelude-adduser
%{_bindir}/prelude-admin
%{_mandir}/man1/prelude-admin.1.gz
%dir %{_sysconfdir}/prelude
%dir %{_sysconfdir}/prelude/default
%dir %{_sysconfdir}/prelude/profile
%config(noreplace) %{_sysconfdir}/prelude/default/client.conf
%config(noreplace) %{_sysconfdir}/prelude/default/global.conf
%config(noreplace) %{_sysconfdir}/prelude/default/idmef-client.conf
%config(noreplace) %{_sysconfdir}/prelude/default/tls.conf
%dir %{_var}/spool/prelude

%files -n python3-prelude
%{python3_sitearch}/_prelude.*so
%{python3_sitearch}/__pycache__/prelude.cpython-%{python3_version_nodots}.*pyc
%{python3_sitearch}/prelude-%{version}-py%{python3_version}.egg-info
%{python3_sitearch}/prelude.py

%files -n perl-prelude
%{perl_vendorarch}/Prelude.pm
%dir %{perl_vendorarch}/auto/Prelude
# Force attrs because libprelude set it to 555
%attr(755, root, root) %{perl_vendorarch}/auto/Prelude/Prelude.so

%files -n ruby-prelude
%{ruby_vendorarchdir}/Prelude.so

%files -n lua-prelude
%{_libdir}/lua/*/prelude.so

%files doc
%{_docdir}/%{name}-devel
%license COPYING LICENSE.README HACKING.README
%doc AUTHORS ChangeLog README NEWS

%changelog
* Wed Jan 04 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 5.2.0-16
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.2

* Fri Nov 25 2022 Florian Weimer <fweimer@redhat.com> - 5.2.0-15
- Port configure script to C99 (#2148366)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 5.2.0-13
- Rebuilt for Python 3.11

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 5.2.0-12
- Perl 5.36 rebuild

* Thu Jan 27 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 5.2.0-11
- F-36: rebuild against ruby31

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Aug 13 2021 Thomas Andrejak <thomas.andrejak@gmail.com> - 5.2.0-9
- Fix BZ 1973946

* Thu Aug 05 2021 Gwyn Ciesla <gwync@protonmail.com> - 5.2.0-8
- Fix BZ 1908783

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 5.2.0-6
- Rebuilt for Python 3.10

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 5.2.0-5
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 07 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 5.2.0-3
- F-34: rebuild against ruby 3.0

* Fri Sep 18 2020 Orion Poplawski <orion@nwra.com> - 5.2.0-2
- Add patch to remove unneeded libraries from libprelude-config --libs (bz#1830473)

* Thu Sep 17 2020 Thomas Andrejak <thomas.andrejak@gmail.com> - 5.2.0-1
- Bump version 5.2.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 5.1.1-6
- Perl 5.32 rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 5.1.1-5
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 5.1.1-3
- Add a minimum patch to support ruby 2.7

* Sun Nov 10 2019 Thomas Andrejak <thomas.andrejak@gmail.com> - 5.1.1-2
- Add missing patches

* Fri Nov 08 2019 Thomas Andrejak <thomas.andrejak@gmail.com> - 5.1.1-1
- Bump version 5.1.1

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 5.0.0-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 5.0.0-6
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 12 2019 Thomas Andrejak <thomas.andrejak@gmail.com> - 5.0.0-4
- Fix FTBFS with awk 5
- Fix FTBFS with Python 3.8 (#1706042)

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 5.0.0-3
- Perl 5.30 rebuild

* Tue May 21 2019 Jitka Plesnikova <jplesnik@redhat.com> - 5.0.0-2
- Fix build with SWIG 4.0.0 (#1707412)
* Tue Feb 26 2019 Thomas Andrejak <thomas.andrejak@gmail.com> - 5.0.0-1
- Bump version 5.0.0, Fixing #1629893

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Vít Ondruch <vondruch@redhat.com> - 4.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.6

* Sun Sep 23 2018 Thomas Andrejak <thomas.andrejak@gmail.com> - 4.1.0-8
- Remove Python2 packages

* Tue Jul 24 2018 Thomas Andrejak <thomas.andrejak@gmail.com> - 4.1.0-7
- Fix FTBFS, #1604644

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 03 2018 Petr Pisar <ppisar@redhat.com> - 4.1.0-5
- Perl 5.28 rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 4.1.0-4
- Perl 5.28 rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 4.1.0-3
- Rebuilt for Python 3.7

* Sun Mar 11 2018 Thomas Andrejak <thomas.andrejak@gmail.com> - 4.1.0-2
- Missing Require in libprelude-devel, see #1508816

* Sat Mar 10 2018 Thomas Andrejak <thomas.andrejak@gmail.com> - 4.1.0-1
- Bump version 4.1.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 05 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.0.0-5
- F-28: rebuild for ruby25

* Wed Dec 06 2017 Rex Dieter <rdieter@fedoraproject.org> - 4.0.0-4
- -devel: drop bogus Provides: libprelude%%{?_isa}-devel

* Mon Oct 9 2017 Thomas Andrejak <thomas.andrejak@gmail.com> - 4.0.0-3
- Fix compatibility with GnuTLS 3.6

* Wed Sep 27 2017 Thomas Andrejak <thomas.andrejak@gmail.com> - 4.0.0-2
- Fix compatibility with gtk-doc-1.26

* Sat Sep 16 2017 Thomas Andrejak <thomas.andrejak@gmail.com> - 4.0.0-1
- Bump version 4.0.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.1.0-32
- Perl 5.26 rebuild

* Thu Feb 02 2017 Thomas Andrejak <thomas.andrejak@gmail.com> - 3.1.0-30
- Fix GnuTLS patch

* Sat Jan 14 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.0-29
- F-26: again rebuild for ruby24

* Thu Jan 12 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.0-28
- F-26: rebuild for ruby24

* Thu Dec 22 2016 Miro Hrončok <mhroncok@redhat.com> - 3.1.0-27
- Rebuild for Python 3.6

* Wed Oct 19 2016 Thomas Andrejak <thomas.andrejak@gmail.com> - 3.1.0-26
- Bump version

* Sun Mar 10 2013 Steve Grubb <sgrubb@redhat.com> - 1:1.0.0-17
- Rebuild with new gnutls

* Thu Sep 06 2012 Steve Grubb <sgrubb@redhat.com> - 1:1.0.0-16
- Add provides bundled gnulib

* Wed Aug 08 2012 Petr Pisar <ppisar@redhat.com> - 1:1.0.0-15
- Fix building with glibc-2.16.6 (bug #839602)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 07 2012 Petr Pisar <ppisar@redhat.com> - 1:1.0.0-13
- Perl 5.16 rebuild

* Tue Mar 13 2012 Steve Grubb <sgrubb@redhat.com> - 1:1.0.0-12
- Drop support for ruby

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1:1.0.0-10
- Perl mass rebuild

* Fri Jun 24 2011 Steve Grubb <sgrubb@redhat.com> - 1:1.0.0-9
- Fix gcc 4.6 C++ bug (#715983)

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1:1.0.0-8
- Perl mass rebuild

* Thu Jun 09 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1:1.0.0-7
- Perl 5.14 mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 1:1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Tue Jun 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 1:1.0.0-4
- Mass rebuild with perl-5.12.0

* Sun May 02 2010 Steve Grubb <sgrubb@redhat.com> - 1.0.0-3
- Fix requires statements

* Fri Apr 30 2010 Steve Grubb <sgrubb@redhat.com> - 1.0.0-2
- New upstream release

* Sat Jan 30 2010 Steve Grubb <sgrubb@redhat.com> - 1.0.0rc1-1
- New upstream release
