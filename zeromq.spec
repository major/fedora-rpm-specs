%bcond_without pgm
%bcond_without unwind

Name:           zeromq
Version:        4.3.4
Release:        9%{?dist}
Summary:        Software library for fast, message-based applications

License:        LGPL-3.0-or-later AND BSD-3-Clause AND MIT
URL:            https://zeromq.org
Source0:        https://github.com/%{name}/libzmq/archive/v%{version}/libzmq-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  asciidoc
BuildRequires:  xmlto
BuildRequires:  libsodium-devel

%if %{with unwind}
BuildRequires:  libunwind-devel
%endif

%if %{with pgm}
BuildRequires:  openpgm-devel
BuildRequires:  krb5-devel
%endif

%description
The 0MQ lightweight messaging kernel is a library which extends the
standard socket interfaces with features traditionally provided by
specialized messaging middle-ware products. 0MQ sockets provide an
abstraction of asynchronous message queues, multiple messaging
patterns, message filtering (subscriptions), seamless access to
multiple transport protocols and more.

This package contains the ZeroMQ shared library.


%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}


%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1 -n libzmq-%{version}

# Remove bundled code.
rm -rf external/wepoll

# Fix permissions.
chmod -x src/xsub.hpp


%build
autoreconf -fi
%configure \
%if %{with pgm}
            --with-pgm \
            --with-libgssapi_krb5 \
%endif
            --with-libsodium \
%if %{with unwind}
            --enable-libunwind \
%endif
            --disable-Werror \
            --disable-static
%make_build


%install
%make_install

# remove *.la
rm %{buildroot}%{_libdir}/libzmq.la


%check
%ifarch s390x
make check V=1 || ( cat test-suite.log && exit 1 )
%endif


%ldconfig_scriptlets


%files
%doc README.md AUTHORS NEWS
%license COPYING COPYING.LESSER
%{_bindir}/curve_keygen
%{_libdir}/libzmq.so.5*
%{_mandir}/man3/zmq_*
%{_mandir}/man7/zmq_*
%{_mandir}/man7/zmq.*

%files devel
%{_libdir}/libzmq.so
%{_libdir}/pkgconfig/libzmq.pc
%{_includedir}/zmq*.h


%changelog
* Thu Oct 05 2023 Remi Collet <remi@remirepo.net> - 4.3.4-9
- rebuild for new libsodium

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed May 17 2023 David Cantrell <dcantrell@redhat.com> - 4.3.4-7
- Convert License tag to SPDX identifiers

* Tue Mar 7 2023 Ben Woodard <woodard@redhat.com> - 4.3.4-6
- disable building with libunwind to fix C++ exceptions when a C applicaion loads
  a module written in C++ #2175966

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jan 30 2021 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 4.3.4-1
- Upstream upgrade
- Fixes #1921879, #1921972, #1921973, #1921975, #1921976, #1921979, #1921981,
- #1921983, #1921983, #1921985, #1921987, #1921989, #1921992, #1921994

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 15 2020 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 4.3.3-1
- Upstream upgrade
- Fixes #1876738 and #1876689

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr 15 2020 Dan Horák <dan[at]danny.cz> - 4.3.2-3
- libunwind is available on all Fedora arches

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Sep 08 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 4.3.2-1
- Update to latest version
- Fix CVE-2019-13132 (#1729830)

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 16 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 4.3.1-3
- Disable libunwind on unsupported arches (#1676262)

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 22 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 4.3.1-1
- Update to latest version of libzmq and cppzmq
- Split cppzmq subpackage into its own package

* Mon Jan 21 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 4.1.6-11
- Backport patches to fix test failures in build
- Cleanup spec a little
- Use explicit soname version in file list

* Tue Aug 28 2018 Pavel Zhukov <landgraf@fedoraproject.org> - 4.1.6-10
- Add gcc-c++ BR

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.1.6-7
- Switch to %%ldconfig_scriptlets

* Mon Oct 02 2017 Remi Collet <remi@fedoraproject.org> - 4.1.6-6
- rebuild for libsodium

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Nov 13 2016 Thomas Spura <tomspur@fedoraproject.org> - 4.1.6-1
- update to 4.1.6

* Mon Mar 07 2016 Remi Collet <remi@fedoraproject.org> - 4.1.4-5
- rebuild for new libsodium soname

* Sun Feb 14 2016 Thomas Spura <tomspur@fedoraproject.org> - 4.1.4-4
- Remove Werror from compile flags

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 24 2016 Thomas Spura <tomspur@fedoraproject.org> - 4.1.4-2
- Enable krb5 and fix building of pgm (#1301197)

* Sat Dec 19 2015 Thomas Spura <tomspur@fedoraproject.org> - 4.1.4-1
- update to 4.1.4 (#1292814)
- refresh zmq.hpp

* Mon Aug 24 2015 Thomas Spura <tomspur@fedoraproject.org> - 4.1.3-1
- update to 4.1.3 (#1256209)
- ipv6 patch included upstream
- refresh zmq.hpp

* Tue Jun 23 2015 Thomas Spura <tomspur@fedoraproject.org> - 4.1.2-1
- update to 4.1.2
- add upstream patch to fix problem with ipv6

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Thomas Spura <tomspur@fedoraproject.org> - 4.0.5-4
- Add zmq.hpp, which originally belonged to zeromq:
  https://github.com/zeromq/cppzmq/issues/48

* Tue May 19 2015 Thomas Spura <tomspur@fedoraproject.org> - 4.0.5-3
- Cherry-pick patch for protocol downgrade attack (#1221666, CVE-2014-9721)
- Remove Obsoletes:zeromq-utils
- Remove %%defattr

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 4.0.5-2
- Rebuilt for GCC 5 C++11 ABI change

* Mon Nov 17 2014 Thomas Spura <tomspur@fedoraproject.org> - 4.0.5-1
- update to 4.0.5

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 17 2013 Thomas Spura <tomspur@fedoraproject.org> - 2.2.0-7
- Rebuilt for openpm-5.2 and sed correct version into configure (#963894)

* Wed Mar 27 2013 Thomas Spura <tomspur@fedoraproject.org> - 2.2.0-6
- run autoreconf before configure so aarch64 is supported (#926859)

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 14 2013 Thomas Spura <tomspur@fedoraproject.org> - 2.2.0-4
- delete foreign files with dubious license in %%prep (#892111)

* Mon Dec 24 2012 Thomas Spura <tomspur@fedoraproject.org> - 2.2.0-3
- add bcond_without pgm macro (Jose Pedro Oliveira, #867182)
- remove bundled pgm
- build against openpgm

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Apr 26 2012 Thomas Spura <tomspur@fedoraproject.org> - 2.2.0-1
- update to 2.2.0

* Sat Jan  7 2012 Thomas Spura <tomspur@fedoraproject.org> - 2.1.11-1
- update to 2.1.11 (as part of rebuilding with gcc-4.7)

* Tue Sep 20 2011 Thomas Spura <tomspur@fedoraproject.org> - 2.1.9-1
- update to 2.1.9
- add check section

* Wed Apr  6 2011 Thomas Spura <tomspur@fedoraproject.org> - 2.1.4-1
- update to new version (#690199)

* Wed Mar 23 2011 Thomas Spura <tomspur@fedoraproject.org> - 2.1.3-1
- update to new version (#690199)
- utils subpackage was removed upstream
  (obsolete it)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 13 2011 Pavel Zhukov <pavel@zhukoff.net> - 2.0.10-1
- update version
- add rpath delete
- change includedir filelist

* Fri Aug 27 2010 Thomas Spura <tomspur@fedoraproject.org> - 2.0.8-1
- update to new version

* Fri Jul 23 2010 Thomas Spura <tomspur@fedoraproject.org> - 2.0.7-4
- upstream VCS changed
- remove buildroot / %%clean
- change descriptions

* Tue Jul 20 2010 Thomas Spura <tomspur@fedoraproject.org> - 2.0.7-3
- move binaries to seperate utils package

* Sat Jun 12 2010 Thomas Spura <tomspur@fedoraproject.org> - 2.0.7-2
- remove BR: libstdc++-devel
- move man3 to the devel package
- change group to System Environment/Libraries

* Sat Jun 12 2010 Thomas Spura <tomspur@fedoraproject.org> - 2.0.7-1
- initial package (based on upstreams example one)
