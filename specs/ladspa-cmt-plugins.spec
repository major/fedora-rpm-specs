Name:           ladspa-cmt-plugins
Version:        1.16
Release:        33%{?dist}
Summary:        A collection of LADSPA plugins
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.ladspa.org/
Source0:        http://www.ladspa.org/download/cmt_src_%{version}.tgz
Source1:        cmt.rdf
Patch1:         cmt-1.15-addnoise.patch
Patch2:         cmt-1.15-dontdenormal.patch
Patch3:         cmt-1.15-nostrip.patch
BuildRequires:  gcc-c++
BuildRequires:  ladspa-devel
BuildRequires: make
Requires:       ladspa
Obsoletes:      cmt <= 1.15-4
Provides:       cmt = %{version}-%{release}

%description
The Computer Music Toolkit (CMT) is a collection of LADSPA plugins for
use with software synthesis and recording packages on Linux. See the
license before use.

The CMT is developed primarily by Richard W.E. Furse the principle
designer of the LADSPA standard, with additional plugins by Jezar and
David Bartold. If you are a programmer or can write documentation and
would like to help out, please feel free to contact Richard.


%prep
%setup -q -n cmt
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%{__chmod} -x doc/plugins.html src/freeverb/Components/tuning.h
# Enforce Fedora link flags
sed -i "s|-shared|-shared $RPM_LD_FLAGS|" src/makefile
mv doc/COPYING .

%build
%{__make} -C src %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS -fPIC" 


%install
%{__mkdir} -p %{buildroot}%{_libdir}/ladspa
%{__mkdir} -p %{buildroot}%{_datadir}/ladspa/rdf
%{__make} -C src INSTALL_PLUGINS_DIR="%{buildroot}%{_libdir}/ladspa/" \
                 install
%{__install} -p -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/ladspa/rdf



%files
%doc README doc/*
%license COPYING
%{_libdir}/ladspa/*.so
%{_datadir}/ladspa/rdf/*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.16-32
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 12 2018 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 1.16-17
- Use Fedora link flags
- Add BR: gcc-c++
- Some cleanup

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.16-10
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Apr 01 2009 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 1.16-1
- New upstream bugfix release

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.15-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.15-7
- Autorebuild for GCC 4.3

* Sun Sep 16 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.15-6
- Various specfile improvements to match the Fedora Packaging Guidelines
- Submit for review for Fedora inclusion

* Fri Nov 24 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.15-5
- change name of package to ladspa-cmt-plugins, spec file tweaks
- install plugins in the right directory even for x86_64

* Fri Jun 24 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 
- remove -Wall on fc4, gcc4 fails otherwise

* Fri Jan 29 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.15-4
- after many tests I added white noise to the freeverb inputs so that
  denormals don't have a chance to appear. The output of freeverb 
  viewed on bitscope shows the background "noise" to be down to -300db,
  so it should be fine. See:
  http://www.musicdsp.org/files/denormal.pdf
- disable the built-in undernomal #define

* Wed Dec 22 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 
- spec file cleanups

* Sun Jul 11 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.15-3
- added rpm compilation flags to support multiple architectures, 
  kept the original O3 optimization level

* Thu Jul  8 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 
- fixed denormal problem that affects freeverb on newer versions of gcc
- added rdf description file from Steve Harris' web site

* Mon May 10 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 
- added buildrequires, erased old ladspa-sdk dependency

* Wed Feb 18 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.15-2
- changed name of ladspa package, do not depend on it explicitly

* Fri Nov  7 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.15-1
- added release tags

* Wed Feb 12 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.15-1
- updated to 1.15

* Thu Oct 31 2002 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu>
- initial build.

