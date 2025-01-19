Name:           ladspa-blop-plugins
Version:        0.2.8
Release:        41%{?dist}
Summary:        Bandlimited LADSPA Oscillator Plugins
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://blop.sourceforge.net/
Source:         http://downloads.sourceforge.net/blop/blop-%{version}.tar.gz
Patch1:         ladspa-blop-plugins-configure-c99.patch
BuildRequires:  gcc
BuildRequires:  ladspa-devel
BuildRequires: make
Requires:       ladspa
Obsoletes:      blop <= 0.2.8-1
Provides:       blop = %{version}-%{release}

%description
BLOP comprises a set of LADSPA plugins that generate bandlimited
sawtooth, square, variable pulse and slope-variable triangle waves,
for use in LADSPA hosts, principally for use with one of the many
modular software synthesisers available.

They are wavetable based, and are designed to produce output with
harmonic content as high as possible over a wide pitch range.


%prep
%autosetup -p1 -n blop-%{version}
chmod -x src/lp4pole_filter.c src/include/lp4pole_filter.h
# Enable optimiziation
sed -i 's|-O0||g' src/Makefile.in


%build
export LDADD="$RPM_LD_FLAGS"
%configure
# note, we must pass CFLAGS as for some reason they do not get propagated
# by configure
%{__make} %{?_smp_mflags} ladspa_plugin_dir="%{_libdir}/ladspa" \
  CFLAGS="$RPM_OPT_FLAGS -ffast-math -D_GNU_SOURCE -DNO_DEBUG -DPIC -fPIC"


%install
%{__mkdir} -p %{buildroot}%{_libdir}/ladspa
%{__mkdir} -p %{buildroot}%{_datadir}/ladspa/rdf
%{__make} DESTDIR="%{buildroot}" \
          ladspa_plugin_dir="%{_libdir}/ladspa" install
%find_lang blop

# install the rdf description
%{__install} -p -m 644 doc/blop.rdf %{buildroot}%{_datadir}/ladspa/rdf



%files -f blop.lang
%doc AUTHORS NEWS README THANKS TODO doc/*.txt
%license COPYING
%{_libdir}/ladspa/*.so
%{_libdir}/ladspa/blop_files
%{_datadir}/ladspa/rdf/*.rdf


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.2.8-40
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Nov 29 2023 Florian Weimer <fweimer@redhat.com> - 0.2.8-36
- Update spec file to actually apply ladspa-blop-plugins-configure-c99.patch

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Feb 10 2023 Florian Weimer <fweimer@redhat.com> - 0.2.8-34
- Port configure script to C99

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 12 2018 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.2.8-23
- Use Fedora optimization and link flags
- Add BR: gcc
- Some cleanup

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.8-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.8-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.8-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Apr  3 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.2.8-7
- Fix missing prototype compiler warnings

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.2.8-6
- Autorebuild for GCC 4.3

* Thu Sep 20 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.2.8-5
- Preserve timestamp when install rdf file

* Tue Sep 18 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.2.8-4
- Make compile honor RPM_OPT_FLAGS

* Sun Sep 16 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.2.8-3
- Various specfile improvements to match the Fedora Packaging Guidelines
- Submit for review for Fedora inclusion

* Fri Nov 24 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2.8-2
- spec file tweaks, add %%{?dist} to release

* Sun Dec 19 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 
- spec file cleanup
- do not include ladspa directory in file list

* Mon Jun 21 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2.8-1
- updated to 0.2.8, fixed file list and added translations

* Sat May  8 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 
- added proper buildrequires

* Wed Feb 18 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2.7-2
- changed name of ladspa package, do not depend on it explicitly

* Fri Nov  7 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2.7-1
- added release tags

* Thu May  8 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2.7-1
- updated to 0.2.7

* Fri Feb 21 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2.6
- initial build
