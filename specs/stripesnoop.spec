Name:		stripesnoop
Version:	1.5
Release:	41%{?dist}
License:	GPL-1.0-or-later
Summary:	Magnetic Stripe Reader
URL:		http://stripesnoop.sourceforge.net
Source0:	http://download.sourceforge.net/stripesnoop/ss-%{version}-src.zip
Patch0:		stripesnoop-1.5-rpmoptflags.patch
Patch1:		stripesnoop-1.5-deflinux.patch
Patch2:		stripesnoop-1.5-asmio.patch
Patch3:		stripesnoop-1.5-pathing.patch
Provides:	stripesnoop-devel = %{version}-%{release}
Obsoletes:	stripesnoop-devel
# ppc and other arches have no inb/outb
# https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=240499
ExclusiveArch:	%{ix86} x86_64
BuildRequires: make
BuildRequires:	gcc, gcc-c++

%description
Stripe Snoop is a suite of research tools that captures, modifies, validates, 
generates, analyzes, and shares data from magstripe cards. Numerous readers 
are supported to gather this information. In addition to simply displaying 
the raw characters that are encoded on the card, Stripe Snoop has a database 
of known card formats. It uses this to give you more detailed information 
about the card.

%prep
%setup -q -c %{name}-%{version}
%patch -P0 -p1
%patch -P1 -p1
%ifarch ppc
%patch -P2 -p1
%endif
%patch -P3 -p1
chmod -x cards.txt ChangeLog.txt COPYING.txt README.txt visa-pre.txt \
	 hardware/* samples/*

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{name}
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
install -m0644 dl-iin.csv visa-pre.txt $RPM_BUILD_ROOT/%{_datadir}/%{name}
install -m0755 bitgen mod10 $RPM_BUILD_ROOT/%{_bindir}
install -m0755 ss $RPM_BUILD_ROOT/%{_bindir}/stripesnoop

%files
%doc ChangeLog.txt COPYING.txt README.txt hardware/ samples/
%{_bindir}/stripesnoop
%{_bindir}/bitgen
%{_bindir}/mod10
%{_datadir}/%{name}/

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 17 2024 Miroslav Suchý <msuchy@redhat.com> - 1.5-39
- convert license to SPDX

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 23 2018 Tom Callaway <spot@fedoraproject.org> - 1.5-27
- add BuildRequires: gcc, gcc-c++

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 24 2015 Tom Callaway <spot@fedoraproject.org> - 1.5-20
- rename 'ss' binary to 'stripesnoop' to avoid conflicts with x2goserver (bz1249328)

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-19.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.5-18.4
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-17.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-16.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-15.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-14.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-13.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-12.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Oct 17 2011 Dan Horák <dan[at]danny.cz> - 1.5-11.4
- only x86 arches have inb/outb

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-11.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-10.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-9.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.5-8.3
- Autorebuild for GCC 4.3

* Mon Aug 27 2007 Tom "spot" Callaway <tcallawa@redhat.com> 1.5-7.3
- license tag fix
- rebuild for BuildID

* Thu Aug  2 2007 Tom "spot" Callaway <tcallawa@redhat.com> 1.5-7.2
- correct license

* Thu May 17 2007 Tom "spot" Callaway <tcallawa@redhat.com> 1.5-7.1
- ppc64 won't work here either

* Fri Sep 15 2006 Tom "spot" Callaway <tcallawa@redhat.com> 1.5-7
- bump for fc6

* Thu Jun  8 2006 Tom "spot" Callaway <tcallawa@redhat.com> 1.5-6
- ppc has no inb/outb, thus the ExcludeArch

* Sun Apr 23 2006 Tom "spot" Callaway <tcallawa@redhat.com> 1.5-5
- provide/obsolete old -devel package to keep the repo clean

* Fri Aug  5 2005 Tom "spot" Callaway <tcallawa@redhat.com> 1.5-4
- only use asm/io.h for ppc
- get rid of devel package (unnecessary)
- fix path for dl-iin.csv, visa-pre.txt

* Thu Aug  4 2005 Tom "spot" Callaway <tcallawa@redhat.com> 1.5-3
- use asm/io.h to enable ppc to build

* Thu Aug  4 2005 Tom "spot" Callaway <tcallawa@redhat.com> 1.5-2
- fix devel requires typo

* Thu Aug  4 2005 Tom "spot" Callaway <tcallawa@redhat.com> 1.5-1
- initial package for Fedora Extras
