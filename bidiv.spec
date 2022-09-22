Summary: Display logical Hebrew on unidirectional terminals
Name: bidiv
Version: 1.5
Release: 32%{?dist}
URL: http://ftp.ivrix.org.il/pub/ivrix/src/cmdline/
Source: http://ftp.ivrix.org.il/pub/ivrix/src/cmdline/%{name}-%{version}.tgz
Patch0: nostrip.patch.gz
Patch1: fribidi-0.19.patch.gz
License: GPLv2
BuildRequires:  gcc
BuildRequires: fribidi-devel
BuildRequires: make

%description
Bidiv (BiDirectional Viewer) is a simple utility for converting logical-Hebrew
input to visual-Hebrew output. This is useful for reading Hebrew mail messages,
viewing Hebrew texts, etc.

%prep
%setup -q -n bidiv
%patch -P 0
%patch -P 1

%build
make PREFIX=%{buildroot} CC_OPT_FLAGS="$RPM_OPT_FLAGS" %{?_smp_mflags}

%install
rm -rf %{buildroot}
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1
make PREFIX=%{buildroot}%{_prefix} \
     MAN_PATH=%{buildroot}%{_mandir} install

%files
%doc README COPYING
%{_prefix}/bin/bidiv
%{_mandir}/man1/bidiv.1*
# and what about %{_mandir}/he/man1/bidiv.1 ? ;)

%changelog
* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-28
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jul 14 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.5-7
- fix license tag

* Mon Feb 19 2008 Dan Kenigsberg <danken@cs.technion.ac.il> 1.5-6
- compile against fribidi-0.19.1
* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.5-5
- Autorebuild for GCC 4.3
* Tue Feb 28 2006 Dan Kenigsberg <danken@cs.technion.ac.il> 1.5-4
- Rebuild for Fedora Extras 6
* Tue Feb 28 2006 Dan Kenigsberg <danken@cs.technion.ac.il> 1.5-3
- Rebuild for Fedora Extras 5
* Sun Feb  5 2006 Dan Kenigsberg <danken@cs.technion.ac.il> 1.5-2
- remove `strip' from Makefile, to have meaningful debuginfo (BUG #180104)
* Sat Jan  7 2006 Dan Kenigsberg <danken@cs.technion.ac.il> 1.5-1
- new upstream version.
* Mon Dec 26 2005 Dan Kenigsberg <danken@cs.technion.ac.il> 1.4-3
- smp_flags and GPL text added, Provides removed
* Thu Nov 17 2005 Dan Kenigsberg <danken@cs.technion.ac.il> 1.4-2
- beautification for Fedora Extras
* Mon Feb 19 2001 Tzafrir Cohen <tzafrir@technion.ac.il> 1.4-1
- initial spec file
