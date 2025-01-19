#global prever r821

Name:           grfcodec
Version:        6.0.6
Release:        26%{?prever}%{?dist}
Summary:        A suite of programs to modify Transport Tycoon Deluxe's GRF files
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://dev.openttdcoop.org/projects/grfcodec
Source0:        http://binaries.openttd.org/extra/grfcodec/%{version}/grfcodec-%{version}-source.tar.xz
#Source0:        http://binaries.openttd.org/extra/grfcodec-nightly/%{prever}/grfcodec-nightly-%{prever}-source.tar.xz
Patch0:         gcc10.patch
BuildRequires:  gcc-c++
BuildRequires:  boost-devel libpng-devel
BuildRequires: make


%description
A suite of programs to modify Transport Tycoon Deluxe's GRF files.


%prep
%setup -q
%patch -P0 -p1


%build
cat << EOF >> Makefile.local
STRIP=true
V=1
CXXFLAGS=-std=c++14 %{optflags}
prefix=%{_prefix}
DO_NOT_INSTALL_DOCS=1
DO_NOT_INSTALL_CHANGELOG=1
DO_NOT_INSTALL_LICENSE=1
EOF

make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}



%files
%doc changelog.txt COPYING
%doc docs/*.txt
%{_bindir}/grf*
%{_bindir}/nforenum
%{_mandir}/man1/grf*.1.gz
%{_mandir}/man1/nforenum.1.gz


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.6-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 6.0.6-25
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.6-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.6-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.6-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.6-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.6-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.6-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.6-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 18 2020 Jeff Law <law@redhat.com> - 6.0.6-15
- Force C++14 as this code is not C++17 ready

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 14 2019 Jeff Law <law@redhat.com> - 6.0.6-12
- Fix narrowing conversion problem caught by gcc-10

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Jonathan Wakely <jwakely@redhat.com> - 6.0.6-5
- Rebuilt for Boost 1.64

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 6.0.6-3
- Rebuilt for Boost 1.63

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 6.0.6-2
- Rebuilt for Boost 1.63

* Thu Jun 30 2016 Felix Kaechele <heffer@fedoraproject.org> - 6.0.6-1
- update to 6.0.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 6.0.5-6
- Rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 6.0.5-5
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 6.0.5-3
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 18 2015 Felix Kaechele <heffer@fedoraproject.org> - 6.0.5-1
- update to 6.0.5

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 6.0.4-6
- Rebuilt for GCC 5 C++11 ABI change

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 6.0.4-5
- Rebuild for boost 1.57.0

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 6.0.4-2
- Rebuild for boost 1.55.0

* Fri Apr 04 2014 Felix Kaechele <heffer@fedoraproject.org> - 6.0.4-1
- update 6.0.4

* Thu Aug 29 2013 Felix Kaechele <heffer@fedoraproject.org> - 6.0.3-1
- update to 6.0.3
- remove old Obsoletes/Provides (BZ #1002133)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 6.0.2-2
- Rebuild for boost 1.54.0

* Thu Mar 14 2013 Felix Kaechele <heffer@fedoraproject.org> - 6.0.2-1
- update to 6.0.2

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Oct 02 2012 Felix Kaechele <heffer@fedoraproject.org> - 6.0.1-1
- update to 6.0.1
- switch to xz tarball

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Mar 29 2012 Felix Kaechele <heffer@fedoraproject.org> - 6.0.0-1
- update to 6.0.0

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.2-4
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 5.1.2-2
- Rebuild for new libpng

* Sun Oct 23 2011 Felix Kaechele <heffer@fedoraproject.org> - 5.1.2-1
- update to 5.1.2

* Sun Jun 12 2011 Felix Kaechele <heffer@fedoraproject.org> - 5.1.1-1
- update to final 5.1.1 release

* Wed Feb 09 2011 Felix Kaechele <heffer@fedoraproject.org> - 5.1.1-0.1.r821
- update to new snapshot with png support

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-0.2.r772
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Sep 21 2010 Felix Kaechele <heffer@fedoraproject.org> - 1.0.1-0.1.r772
- update to latest nightly build for support of latest grfcodec features
- nforenum is now part of grfcodec

* Fri Aug 27 2010 Felix Kaechele <heffer@fedoraproject.org> - 1.0.0-1
- update to new upstream release
- contains mostly fixes for downstream packagers (like us)

* Sat Mar 20 2010 Iain Arnell <iarnell@gmail.com> 0.9.11-0.4.r2306
- update to r2306 (fixes off-by-one error in byte escape)

* Fri Jan 15 2010 Iain Arnell <iarnell@gmail.com> 0.9.11-0.4.r2294
- update to r2294
- drop compile.patch fixes for gcc 4.4

* Mon Aug 24 2009 Iain Arnell <iarnell@gmail.com> 0.9.11-0.4.r2177
- update to current svn revision to remove "status updates"

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.11-0.3.r2111
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun May 03 2009 Iain Arnell <iarnell@gmail.com> 0.9.11-0.2.r2111
- fix license tag (GPLv2+)
- don't pass -O3 to gcc
- doesn't BR subversion

* Sat May 02 2009 Iain Arnell <iarnell@gmail.com> 0.9.11-0.1.r2111
- initial release
