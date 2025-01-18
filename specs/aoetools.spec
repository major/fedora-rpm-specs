Name:           aoetools
Version:        36
Release:        32%{?dist}
Summary:        ATA over Ethernet Tools
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://aoetools.sourceforge.net
Source0:        http://downloads.sourceforge.net/aoetools/%{name}-%{version}.tar.gz
Source1:        60-aoe.rules
Patch0:         %{name}-makefile.patch
BuildRequires:  gcc
BuildRequires:  systemd
BuildRequires: make

%description
The aoetools are programs that assist in using ATA over Ethernet on 
systems with version 2.6 and newer Linux kernels.

%prep
%autosetup -p1

%build
%make_build

%install
%{!?_udevrulesdir: %global _udevrulesdir %{_sysconfdir}/udev/rules.d}

%make_install
mkdir -pm 755 %{buildroot}/%{_udevrulesdir}
install -pm 644 %{SOURCE1} %{buildroot}/%{_udevrulesdir}

%files
%doc COPYING HACKING NEWS README devnodes.txt
%{_sbindir}/aoe*
%{_sbindir}/coraid-update
%{_mandir}/man8/aoe*.8*
%{_mandir}/man8/coraid-update.8*
%config(noreplace) %{_udevrulesdir}/*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 36-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 36-31
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 36-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 36-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 36-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 36-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 36-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 36-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 36-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 36-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 36-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 36-21
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 36-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 36-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 36-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 36-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Sep 15 2018 Filipe Rosset <rosset.filipe@gmail.com> - 36-16
- rebuilt to fix FTBFS + spec cleanup

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 36-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 36-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 36-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 36-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 36-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 36-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jul 03 2015 Ed Cashin <ed.cashin@acm.org> - 36-9
- Use buildrequires systemd for udevrulesdir on newer systems

* Mon Jun 29 2015 Ed Cashin <ed.cashin@acm.org> - 36-8
- Use global instead of define

* Sat Jun 20 2015 Ed Cashin <ed.cashin@acm.org> - 36-7
- Updated to use _udevrulesdir when present, falling back to old rules dir

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 36-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 36-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 36-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Sep 10 2013 Ed Cashin <ecashin@coraid.com> - 36-3
- Do not store udev rules in lookaside cache
- Revert accidental change to spec file changelog

* Tue Sep 10 2013 Christopher Meng <rpm@cicku.me> - 36-2
- Cleanup the spec.
- Add noreplace flag for udev rules file.
- Preserve the timestamp.

* Mon Sep 09 2013 Ed Cashin <ecashin@coraid.com> - 36-1
- New upstream release (aoe-sancheck and bugfixes)
- Update package description: aoetools supports 2.6+ kernels
- Include udev rules needed for creation of aoe character devices

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 30-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 30-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 30-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 30-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Aug 30 2010 Patrick "Jima" Laughton <jima@fedoraproject.org> 30-1
- New upstream release
- Added coraid-update binary/manual

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 13 2008 Patrick "Jima" Laughton <jima@beer.tclug.org> 23-1
- New upstream release

* Fri Nov 30 2007 Patrick "Jima" Laughton <jima@beer.tclug.org> 21-1
- New upstream release

* Wed Aug 22 2007 Patrick "Jima" Laughton <jima@beer.tclug.org> 18-1
- New upstream release
- License clarification

* Tue Jun 12 2007 Patrick "Jima" Laughton <jima@beer.tclug.org> 16-1
- New upstream release (bugfix)

* Mon Apr 09 2007 Patrick "Jima" Laughton <jima@beer.tclug.org> 15-1
- Figures, NOW I notice the new version
- Adapted/removed patches (most fixes moved upstream, thanks!)

* Mon Apr 09 2007 Patrick "Jima" Laughton <jima@beer.tclug.org> 14-3
- Added devnodes.txt to %%doc
- Importing into CVS

* Sat Apr 07 2007 Patrick "Jima" Laughton <jima@beer.tclug.org> 14-2
- Added CFLAGS="$RPM_OPT_FLAGS" to building (thanks Chris!)

* Wed Apr 04 2007 Patrick "Jima" Laughton <jima@beer.tclug.org> 14-1
- Initial Fedora RPM
