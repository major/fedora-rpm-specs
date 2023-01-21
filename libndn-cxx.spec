Name:       libndn-cxx
Version:    0.7.1
Release:    10%{?dist}
Summary:    C++ library implementing Named Data Networking primitives
License:    LGPLv3+ and (BSD or LGPLv3+) and (GPLv3+ or LGPLv3+)
URL:        http://named-data.net
Source0:    http://named-data.net/downloads/ndn-cxx-%{version}.tar.bz2
Patch0:     ndn-cxx-boost176-bind.patch

BuildRequires:  sqlite-devel cryptopp-devel boost-devel pkgconfig openssl-devel
BuildRequires:  python3-devel gcc-c++

%description
libndn-cxx is a C++ library that implements NDN primitives.

%package  devel
Summary:  Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -qn ndn-cxx-%{version}
%patch0 -p1


%build
CXXFLAGS="%{optflags} -std=c++11" \
LINKFLAGS="-Wl,--as-needed" \
#%{__python3} ./waf --enable-shared --disable-static --with-tests \
# --prefix=%{_prefix} --bindir=%{_bindir} --libdir=%{_libdir} \
# --datadir=%{_datadir} --sysconfdir=%{_sysconfdir} configure

%{__python3} ./waf --enable-shared --disable-static \
 --prefix=%{_prefix} --bindir=%{_bindir} --libdir=%{_libdir} \
 --datadir=%{_datadir} --sysconfdir=%{_sysconfdir} configure

%{__python3} ./waf -v %{?_smp_mflags}

%install
%{__python3} ./waf install --destdir=%{buildroot} --prefix=%{_prefix} \
 --bindir=%{_bindir} --libdir=%{_libdir}

%check
export LD_LIBRARY_PATH=$PWD/build
#build/unit-tests

%ldconfig_scriptlets

%files
%{_libdir}/libndn-cxx.so.%{version}
%doc AUTHORS.md  README-dev.md  README.md
%dir %{_sysconfdir}/ndn
%license COPYING.md
%{_bindir}/*
%config(noreplace) %{_sysconfdir}/ndn/client.conf.sample

%files devel
%{_includedir}/ndn-cxx/
%{_libdir}/libndn-cxx.so
%{_libdir}/pkgconfig/libndn-cxx.pc

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 24 2022 Jonathan Wakely <jwakely@redhat.com> - 0.7.1-8
- Remove obsolete boost-python3-devel build dependency (#2100748)

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 0.7.1-7
- Rebuilt for Boost 1.78

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 0.7.1-5
- Rebuilt with OpenSSL 3.0.0

* Mon Aug 09 2021 Jonathan Wakely <jwakely@redhat.com> - 0.7.1-4
- Patched and rebuilt for Boost 1.76

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Feb 20 2021 Miro Hrončok <mhroncok@redhat.com> - 0.7.1-2
- Remove redundant BuildRequires on Python 2
- Fixes: rhbz#1807516

* Wed Feb 10 2021 Susmit Shannigrahi <susmit@fedoraproject.org> - 0.7.1-1
- Update version

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 0.6.6-5
- Rebuilt for Boost 1.75

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 31 2020 Jonathan Wakely <jwakely@redhat.com> - 0.6.6-3
- Rebuilt for Boost 1.73

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 2 2019 Susmit Shannigrahi <susmit at cs.colostate.edu> - 0.6.6-1
- Update to 0.6.6

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 19 2018 Susmit Shannigrahi <susmit at cs.colostate.edu> - 0.6.1-5
- Update python dependency for F29 release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.6.1-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 23 2018 Rex Dieter <rdieter@fedoraproject.org> - 0.6.1-2
- rebuild (cryptopp)

* Mon Feb 19 2018 Susmit Shannigrahi <susmit at cs.colostate.edu> - 0.6.1-1
- Package for 0.6.1 release

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Susmit Shannigrahi <susmit at cs.colostate.edu> - 0.6.0-1
- Package for 0.6.0 release

* Tue Apr 05 2016 Susmit Shannigrahi <susmit at cs.colostate.edu> - 0.4.1-3
- Package for 0.4.1 release

* Sun Jan 24 2016 Susmit Shannigrahi <susmit at cs.colostate.edu> - 0.4.0-2
- Rebuild for boost missing dependency

* Fri Jan 8 2016 Susmit Shannigrahi <susmit at cs.colostate.edu> - 0.4.0-1
- Package for 0.4.0 release

* Thu Nov 26 2015 Marcin Juszkiewicz <mjuszkiewicz@redhat.com> - 0.3.4-6
- Fix build on AArch64 with upstream fix

* Tue Nov 10 2015 Marcin Juszkiewicz <mjuszkiewicz@redhat.com> - 0.3.4-5
- Fix FTBFS on AArch64. Developer assumed that memcmp() returns -1/0/1 instead
  of reading what C/C++ standard says about it.

* Thu Oct 15 2015 Susmit Shannigrahi <susmit at cs.colostate.edu> - 0.3.4-4
- Fix unused-direct-shlib-dependency warning
- Add missing sysconfigdir

* Thu Oct 1 2015 Susmit Shannigrahi <susmit at cs.colostate.edu> - 0.3.4-3
- Add patch for boost 1.59 semicolon bug

* Thu Sep 24 2015 Susmit Shannigrahi <susmit at cs.colostate.edu> - 0.3.4-2
- Fix licencing
- Address reviewer's comments

* Wed Sep 16 2015 Susmit Shannigrahi <susmit at cs.colostate.edu> - 0.3.4-1
- Repackage for 0.3.4

* Tue Sep 08 2015 Susmit Shannigrahi <susmit at cs.colostate.edu> - 0.3.3-2
- Use waf to install files
- Fix review comments

* Fri Aug 21 2015 Susmit Shannigrahi <susmit at cs.colostate.edu> - 0.3.3-1
- Update package for 0.3.3

* Thu Feb 5 2015 Susmit Shannigrahi <susmit at cs.colostate.edu> - 0.3.0-1
- Initial Packaging

