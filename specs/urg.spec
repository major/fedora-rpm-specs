Name:           urg
Version:        0.8.18
Release:        35%{?dist}
Summary:        Library to access Hokuyo URG laser range finders

# Automatically converted from old format: LGPLv3 - review is highly recommended.
License:        LGPL-3.0-only
URL:            http://www.hokuyo-aut.jp/cgi-bin/urg_programs_en/
Source0:        http://www.hokuyo-aut.jp/02sensor/07scanner/download/urg_programs_en/urg-%{version}.zip
Patch0:         urg-0.8.18-missing-includes.patch
Patch1:         urg-0.8.18-fixes.patch
%if 0%{?fedora} > 27
Patch2:         urg-0.8.18-unique-ptr.patch
%endif

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  autoconf automake libtool
BuildRequires:  SDL_net-devel
BuildRequires:  boost-devel >= 1.33.1

%description
This library uses the SCIP2.0 protocol to provide access to devices of
Hokuyo URG laser range finder series.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       boost-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q
%patch -P0 -p1 -b .missing-includes
%patch -P1 -p1 -b .fixes
%if 0%{?fedora} > 27
%patch -P2 -p1 -b .unique-ptr
%endif


%build
# autoreconf required for supporting aarch64 see rhbz #926685
autoreconf -i -f
%configure --disable-static
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%ldconfig_scriptlets


%files
%doc ChangeLog AUTHORS COPYING README
%{_libdir}/*.so.*

%files devel
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*.so


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.18-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.8.18-34
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.18-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.18-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.18-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.18-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.18-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.18-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.18-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.18-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.18-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.18-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.18-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.18-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.18-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 13 2018 Tim Niemueller <tim@niemueller.de> - 0.8.18-20
- Add patch to replace auto_ptr with unique_ptr
  (easy since auto_ptr is only used as private member and not exposed)
- Add patch with fixes for ppc and arm platforms (narrowing, format fixes)
- Tested with URG-04LX-UG01 model (on x86_64 though, no other arch available)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.18-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.18-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.18-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.18-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov 08 2016 Filipe Rosset <rosset.filipe@gmail.com> - 0.8.18-15
- Rebuilt to fix FTBFS rhbz #1308211

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.18-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 16 2016 Jonathan Wakely <jwakely@redhat.com> - 0.8.18-13
- Rebuilt for Boost 1.60

* Fri Aug 28 2015 Jonathan Wakely <jwakely@redhat.com> - 0.8.18-12
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.18-11
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 0.8.18-10
- rebuild for Boost 1.58

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.18-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.8.18-8
- Rebuilt for GCC 5 C++11 ABI change

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 0.8.18-7
- Rebuild for boost 1.57.0

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.18-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Petr Machata <pmachata@redhat.com> - 0.8.18-4
- Rebuild for boost 1.55.0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 0.8.18-2
- Rebuild for boost 1.54.0

* Tue Jul 09 2013 Mat Booth <fedora@matbooth.co.uk> - 0.8.18-1
- Fix FTBFS rhbz #913842
- Fix aarch64 support rhbz #926685
- Update to latest upstream and drop unneeded patches

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.8.11-7
- Rebuild for Boost-1.53.0

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Mar  4 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.8.11-5
- Fix gcc 4.7 FTBFS

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.11-4
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Feb 11 2011 Tim Niemueller <tim@niemueller.de> - 0.8.11-2
- Added patch for GCC 4.6 compatibility

* Thu Feb 10 2011 Tim Niemueller <tim@niemueller.de> - 0.8.11-1
- Update to 0.8.11
- Remove upstreamed patches

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Feb 06 2011 Thomas Spura <tomspur@fedoraproject.org> - 0.8.7-5
- rebuild for new boost

* Tue Sep 07 2010 Dan Horák <dan[at]danny.cz> - 0.8.7-4
- fix build on 64-bit architectures

* Thu Aug 05 2010 Tim Niemueller <tim@niemueller.de> - 0.8.7-3
- Rebuild for new Boost

* Sun Jan 31 2010 Tim Niemueller <tim@niemueller.de> - 0.8.7-2
- Fixes from review request #560322: source set to direct file URL,
  revised norpath patch to completely remove references to /usr/lib,
  added boost-devel as requirement for devel sub-package

* Sat Jan 30 2010 Tim Niemueller <tim@niemueller.de> - 0.8.7-1
- Update to 0.8.7 which contains another upstreamed patch
  (separate m4 dir for macros, Boost macros separated)
- Exclude ppc64, does not compile atm
- Add patch to remove rpath, submitted upstream awaiting inclusion
- Add patch to require only Boost 1.33.1 (RHEL/CentOS)
- Add patch to require only Autoconf 2.59 (RHEL/CentOS)
- Add patch to remove some forward declarations (RHEL/CentOS)

* Mon Jan 25 2010 Tim Niemueller <tim@niemueller.de> - 0.8.6-1
- Update to 0.8.6 which contains my upstreamed patches
  (fixes for 64bit and GCC 4.4, renaming and placing of libs)

* Fri Nov 27 2009 Tim Niemueller <tim@niemueller.de> - 0.7.3-1
- Initial package

