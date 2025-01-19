Name:           ncmpcpp
Version:        0.10.1
Release:        3%{?dist}
Summary:        Featureful ncurses based MPD client inspired by ncmpc
License:        GPL-2.0-or-later
URL:            http://ncmpcpp.rybczak.net/
Source0:        https://github.com/%{name}/%{name}/archive/refs/tags/%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  curl-devel
BuildRequires:  taglib-devel
BuildRequires:  ncurses-devel
BuildRequires:  libmpdclient-devel
BuildRequires:  boost-devel
BuildRequires:  fftw-devel
BuildRequires:  readline-devel
BuildRequires:  autoconf automake libtool


%description
A featureful ncurses based MPD client inspired by ncmpc. The main features are:

- tag editor
- playlist editor
- easy to use search engine
- media library
- music visualizer
- ability to fetch artist info from last.fm
- new display mode
- alternative user interface
- ability to browse and add files from outside of MPD music directory

.. and a lot more minor functions.

%prep
%autosetup
autoreconf -fiv

%build
BOOST_LIB_SUFFIX=""; export BOOST_LIB_SUFFIX ;
%configure --disable-static --enable-clock --with-taglib --with-fftw --enable-visualizer --enable-outputs
%make_build


%install
%make_install

# Remove dupe
rm -f %{buildroot}/%{_docdir}/%{name}/COPYING


%files
%doc doc/config doc/bindings AUTHORS CHANGELOG.md README.md
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Dec 08 2024 Pete Walter <pwalter@fedoraproject.org> - 0.10.1-2
- Rebuild for ICU 76

* Mon Oct 28 2024 Dominic Hopf <dmaphy@fedoraproject.org> - 0.10.1-1
- New upstream release: 0.10.1 (RHBZ#2309481)

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.9.2-20
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 31 2024 Pete Walter <pwalter@fedoraproject.org> - 0.9.2-18
- Rebuild for ICU 74

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Jonathan Wakely <jwakely@redhat.com> - 0.9.2-15
- Rebuilt for Boost 1.83

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 František Zatloukal <fzatlouk@redhat.com> - 0.9.2-13
- Rebuilt for ICU 73.2

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 0.9.2-12
- Rebuilt for Boost 1.81

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 31 2022 Pete Walter <pwalter@fedoraproject.org> - 0.9.2-10
- Rebuild for ICU 72

* Mon Aug 01 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 0.9.2-9
- Rebuilt for ICU 71.1

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 0.9.2-7
- Rebuilt for Boost 1.78

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Aug 07 2021 Jonathan Wakely <jwakely@redhat.com> - 0.9.2-5
- Rebuilt for Boost 1.76

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu May 20 2021 Pete Walter <pwalter@fedoraproject.org> - 0.9.2-3
- Rebuild for ICU 69

* Wed May 19 2021 Pete Walter <pwalter@fedoraproject.org> - 0.9.2-2
- Rebuild for ICU 69

* Tue Jan 26 2021 Dominic Hopf <dmaphy@fedoraproject.org> - 0.9.2-1
- Update to 0.9.2 (RHBZ#1920130)

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 0.9.1-2
- Rebuilt for Boost 1.75

* Thu Dec 24 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.9.1-1
- Update to latest release

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 28 2020 Jonathan Wakely <jwakely@redhat.com> - 0.8.2-15
- Rebuilt for Boost 1.73

* Sat May 16 2020 Pete Walter <pwalter@fedoraproject.org> - 0.8.2-14
- Rebuild for ICU 67

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 14 2019 Jeff Law <law@redhat.com> - 0.8.2-12
- Fix missing #include for gcc-10

* Sun Nov 03 2019 Dominic Hopf <dmaphy@fedoraproject.org> - 0.8.2-2
- Enable fftw support (RHBZ#1639480)

* Fri Nov 01 2019 Pete Walter <pwalter@fedoraproject.org> - 0.8.2-10
- Rebuild for ICU 65

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.2-8
- Rebuild for readline 8.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 0.8.2-6
- Rebuilt for Boost 1.69

* Wed Jan 23 2019 Pete Walter <pwalter@fedoraproject.org> - 0.8.2-5
- Rebuild for ICU 63

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Pete Walter <pwalter@fedoraproject.org> - 0.8.2-3
- Rebuild for ICU 62

* Mon Apr 30 2018 Pete Walter <pwalter@fedoraproject.org> - 0.8.2-2
- Rebuild for ICU 61.1

* Thu Apr 12 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.8.2-1
- Update to latest upstream release

* Sat Mar 10 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.8.1-5
- Add g++ to BR

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 0.8.1-3
- Rebuilt for Boost 1.66

* Thu Nov 30 2017 Pete Walter <pwalter@fedoraproject.org> - 0.8.1-2
- Rebuild for ICU 60.1

* Mon Oct 23 2017 Dominic Hopf <dmaphy@fedoraproject.org> - 0.8.1-1
- Update to lastest upstream release: ncmpcpp 0.8.1

* Mon Aug 07 2017 Adrian Reber <adrian@lisas.de> - 0.8-6
- Rebuilt for new libmpdclient

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Jonathan Wakely <jwakely@redhat.com> - 0.8-3
- Rebuilt for s390x binutils bug

* Mon Jul 03 2017 Jonathan Wakely <jwakely@redhat.com> - 0.8-2
- Rebuilt for Boost 1.64

* Tue May 23 2017 Dominic Hopf <dmaphy@fedoraproject.org> - 0.8-1
- Update to lastest upstream release: ncmpcpp 0.8

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 0.7.7-3
- Rebuilt for Boost 1.63

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.7.7-2
- Rebuild for readline 7.x

* Thu Nov 24 2016 Dominic Hopf <dmaphy@fedoraproject.org> - 0.7.7-1
- Update to lastest upstream release: ncmpcpp 0.7.7

* Sat Aug 27 2016 Dominic Hopf <dmaphy@fedoraproject.org> - 0.7.4-1
- Update to lastest upstream release: ncmpcpp 0.7.4

* Tue May 17 2016 Jonathan Wakely <jwakely@redhat.com> - 0.7.3-5
- Rebuilt for linker errors in boost (#1331983)

* Fri Apr 15 2016 David Tardon <dtardon@redhat.com> - 0.7.3-4
- rebuild for ICU 57.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.7.3-2
- Bump spec for boost 1.6 rebuild

* Thu Jan 21 2016 Dominic Hopf <dmaphy@fedoraproject.org> - 0.7.3-1
- Update to lastest upstream release: ncmpcpp 0.7.3

* Mon Jan 18 2016 Dominic Hopf <dmaphy@fedoraproject.org> - 0.7.2-1
- Update to lastest upstream release: ncmpcpp 0.7.2

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 0.7.1-3
- Rebuilt for Boost 1.60

* Fri Jan 08 2016 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.7.1-2
- Update summary and description

* Sun Jan 03 2016 Dominic Hopf <dmaphy@fedoraproject.org> - 0.7.1-1
- Update to lastest upstream release: ncmpcpp 0.7.1 (RHBZ#1280519)

* Tue Sep 15 2015 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.6.7-1
- Update to lastest upstream release

* Tue Sep 08 2015 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.6.6-1
- Update to latest upstream release

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 0.6.4-6
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.4-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 0.6.4-4
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 06 2015 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.6.4-2
- autogen was breaking the build on f22 somehow.

* Wed May 06 2015 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.6.4-1
- Update to latest upstream release

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.6.3-2
- Rebuilt for GCC 5 C++11 ABI change

* Tue Mar 10 2015 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.6.3-1
- Update to latest upstream release

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Nov 28 2013 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.5.10-6
- Fix FTBFS because of doc dir

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jun 29 2013 Dominic Hopf <dmaphy@fedoraproject.org> - 0.5.10-4
- fix bogus date in changelog
- update upstream urls

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr 02 2012 Dominic Hopf <dmaphy@fedoraproject.org> - 0.5.10-1
- New upstream release: ncmpcpp 0.5.10

* Thu Mar 29 2012 Dominic Hopf <dmaphy@fedoraproject.org> - 0.5.9-1
- New upstream release: ncmpcpp 0.5.9

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.8-3
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Oct 15 2011 Dominic Hopf <dmaphy@fedoraproject.org> - 0.5.8-1
- New upstream release: ncmpcpp 0.5.8

* Mon Jun 13 2011 Dominic Hopf <dmaphy@fedoraproject.org> - 0.5.7-1
- New upstream release: ncmpcpp 0.5.7

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 07 2011 Dominic Hopf <dmaphy@fedoraproject.org> - 0.5.6-1
- New upstream release: ncmpcpp 0.5.6

* Tue Jun 08 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 0.5.4-1
- update to 0.5.4
- enable visualizer option. Resolves rhbz#593205
- enable outputs screen
- update spec to match current guidelines

* Sat Feb 27 2010 Michal Nowak <mnowak@redhat.com> - 0.5.2-1
- 0.5.2

* Wed Jan  6 2010 Michal Nowak <mnowak@redhat.com> - 0.5-1
- 0.5
- dependency on libmpdclient (version 2.1+)

* Mon Oct  5 2009 Michal Nowak <mnowak@redhat.com> - 0.4.1-1
- 0.4.1

* Fri Sep 11 2009 Michal Nowak <mnowak@redhat.com> - 0.4-1
- 0.4

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jun 24 2009 Michal Nowak <mnowak@redhat.com> - 0.3.5-1
- 0.3.5
- new feature: custom command execution on song change
- new feature: allow for physical files and directories deletion
- new feature: add local directories recursively
- new feature: add random songs to playlist
- new feature: mouse support
- new screen: outputs
- text scrolling in header was made optional
- some bugfixes

* Sat Jun 13 2009 Michal Nowak <mnowak@redhat.com> - 0.3.4-1
- 0.3.4

* Mon Apr 06 2009 Michal Nowak <mnowak@redhat.com> - 0.3.3-1
- dumped ncmpcpp-0.3.2-charset.patch -- upstream already 
- 0.3.3

* Wed Mar 18 2009 Michal Nowak <mnowak@redhat.com> - 0.3.2-1
- 0.3.2
- added ncmpcpp man page

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 23 2009 Michal Nowak <mnowak@redhat.com> 0.3.1-1
- 0.3.1

* Tue Feb  3 2009 Michal Nowak <mnowak@redhat.com> 0.3-1
- 0.3
- enable clock

* Thu Jan 15 2009 Michal Nowak <mnowak@redhat.com> 0.2.5-4
- disable building static archives

* Tue Jan 13 2009 Michal Nowak <mnowak@redhat.com> 0.2.5-3
- minor SPEC file changes

* Thu Dec 11 2008 Michal Nowak <mnowak@redhat.com> 0.2.5-2
- added ncurses-devel as BuildRequires

* Tue Dec  9 2008 Michal Nowak <mnowak@redhat.com> 0.2.5-1
- 0.2.5

