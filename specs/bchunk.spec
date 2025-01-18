%global _hardened_build 1
%global debug_package %{nil}

Summary: CD image format converter from .bin/.cue to .iso/.cdr
Name: bchunk
Version: 1.2.2
Release: 18%{?dist}
URL: http://he.fi/bchunk/
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
Source0: http://he.fi/bchunk/bchunk-%{version}.tar.gz
Patch0: bchunk-1.2.2-CFLAGS.patch

BuildRequires: gcc
BuildRequires: make

%description
The bchunk package contains a UNIX/C rewrite of the BinChunker program.
BinChunker converts a CD image in a .bin/.cue format (sometimes .raw/.cue)
into a set of .iso and .cdr tracks.  The .bin/.cue format is used by some
non-UNIX CD-writing software, but is not supported on most other
CD-writing programs.

%prep
%autosetup

%build
%make_build

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m 755 bchunk $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -p -m 644 bchunk.1 $RPM_BUILD_ROOT%{_mandir}/man1

%files
%doc ChangeLog README
%license COPYING
%{_bindir}/bchunk
%{_mandir}/man1/bchunk.1.gz

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.2.2-17
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 19 2018 Conrad Meyer <cemeyer@uw.edu> - 1.2.2-3
- Add gcc BR after removal from buildroot

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 28 2018 Filipe Rosset <rosset.filipe@gmail.com> - 1.2.2-1
- spec cleanup, silent rpmlint
- remove upstreamed patches, fixes rhbz #1507577
- update to 1.2.2

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Aug 12 2009 Conrad Meyer <konrad@tylerc.org> - 1.2.0-9
- Add Debian's patch to fix wrong file size calculations.

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 08 2008 Michael Schwendt <mschwendt@fedoraproject.org>
- rebuilt for GCC 4.3 as requested by Fedora Release Engineering

* Tue Aug 21 2007 Michael Schwendt <mschwendt@fedoraproject.org>
- rebuilt

* Thu Aug  2 2007 Michael Schwendt <mschwendt@fedoraproject.org> - 1.2.0-5
- Clarify licence (GPLv2+).

* Mon Aug 28 2006 Michael Schwendt <mschwendt@fedoraproject.org>
- rebuilt

* Sat Feb 25 2006 Michael Schwendt <mschwendt@fedoraproject.org> - 1.2.0-3
- rebuilt for FC5

* Thu Apr  7 2005 Michael Schwendt <mschwendt@fedoraproject.org>
- rebuilt

* Wed Jun 30 2004 Michael Schwendt <mschwendt@fedoraproject.org> - 0:1.2.0-0.fdr.1
- Update to 1.2.0 (very minor feature add.)
- A few spec updates.

* Tue May  6 2003 Michael Schwendt <mschwendt@fedoraproject.org> - 0:1.1.1-0.fdr.3
- Don't strip-install files.
- Patch1: CFLAGS were hardcoded in the Makefile.

* Mon May  5 2003 Michael Schwendt <mschwendt@fedoraproject.org> - 0:1.1.1-0.fdr.1
- Update Red Hat's 1.0.0-7 rpm, adhere to Fedora package guidelines.

