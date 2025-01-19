Name:           ladspa-caps-plugins
Version:        0.9.24
Release:        22%{?dist}
Summary:        The C* Audio Plugin Suite
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://quitte.de/dsp/caps.html
Source0:        http://quitte.de/dsp/caps_%{version}.tar.bz2
Patch0:         caps-0.9.10-nostrip.patch
Patch1:         caps-0.9.24-gcc6.patch
Patch2:         caps-pow-exp.patch
BuildRequires:  gcc-c++
BuildRequires:  ladspa-devel
BuildRequires: make
Requires:       ladspa
Obsoletes:      caps <= 0.3.0-2
Provides:       caps = %{version}-%{release}

%description
caps, the C* Audio Plugin Suite, is a collection of refined LADSPA
units including instrument amplifier emulation, stomp-box classics,
versatile 'virtual analog' oscillators, fractal oscillation, reverb,
equalization and others.


%prep
%setup -q -n caps-%{version}
%patch -P0 -p1 -z .nostrip
%patch -P1 -p1
%patch -P2 -p1
# use the system version of ladspa.h
rm ladspa.h


%build
make %{?_smp_mflags} OPTS="$RPM_OPT_FLAGS -fPIC" LDFLAGS="$RPM_LD_FLAGS -shared"


%install
%make_install DEST=%{_libdir}/ladspa


%files
%doc CHANGES README*
%license COPYING
%{_libdir}/ladspa/*.so
%{_datadir}/ladspa/rdf/*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.24-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.9.24-21
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.24-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.24-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.24-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.24-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.24-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.24-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.24-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.24-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.24-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.24-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.24-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.24-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.24-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.24-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 12 2018 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.24-6
- Use Fedora link flags
- Add BR: gcc-c++

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.24-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.24-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Feb 20 2016 Hans de Goede <hansdegoede@redhat.com> - 0.9.24-1
- Update to latest upstream release 0.9.24
- Fix FTBFS (rhbz#1307707)
- Drop bundled html docs, upstream is no longer shipping them, goto:
  http://quitte.de/dsp/caps.html to view them

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.9.10-4
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Aug 22 2013 Brendan Jones <brendan.jones.it@gmail.com> 0.9.10-1
- Update to latest release 0.9.10

* Fri Aug  2 2013 Hans de Goede <hansdegoede@redhat.com> - 0.9.7-1
- Update to latest upstream release 0.9.7 (rhbz#901363)
- Various specfile improvements

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Mar 24 2009 Hans de Goede <hdegoede@redhat.com> 0.4.2-4
- Remove -ffast-math from CFLAGS, as it causes errors in the output (#491636)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.4.2-2
- Autorebuild for GCC 4.3

* Sun Sep 16 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.4.2-1
- Various specfile improvements to match the Fedora Packaging Guidelines
- Update to latest upstream release 0.4.2
- Submit for review for Fedora inclusion

* Fri Nov 24 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2.3-3
- change package name to caps-ladspa-plugins
- spec file tweaks
- added -fPIC build option

* Mon Jul  3 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2.3-2
- make sure the plugin shared library is executable (thanks to
  Michael Tiemann for finding this problem)

* Mon May  1 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2.3-1
- update to 0.3.0
- install rdf files (see README.ardour)

* Wed Jun 29 2005 Mario Torre <mppr_kris@tiscali.it>
- patch for gcc4

* Sun Jun  5 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2.3-1
- updated to 0.2.3
- added html documentation file in doc section

* Sun Dec 26 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 
- spec file cleanup

* Fri Dec  3 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2.0-1
- updated to 0.2.0, added proper build flags

* Tue Mar 30 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.1.11-1
- updated to 0.1.11

* Tue Feb 24 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.1.8-1
- initial build
