Name:           SIBsim4
Version:        0.20
Release:        31%{?dist}
Summary:        Align expressed RNA sequences on a DNA template
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://sibsim4.sourceforge.net
Source0:        http://downloads.sourceforge.net/sibsim4/%{name}-%{version}.tar.gz
BuildRequires: make
BuildRequires:  gcc


%description
SIBsim4 is a modified version of the sim4 program, which is a
similarity-based tool for aligning an expressed DNA sequence (EST,
mRNA) with a genomic sequence.


%prep
%setup -q


%build
make %{?_smp_mflags} OPT="$RPM_OPT_FLAGS"


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1
install -m 755 SIBsim4 $RPM_BUILD_ROOT/%{_bindir}/
install -m 644 SIBsim4.1 $RPM_BUILD_ROOT/%{_mandir}/man1


%files
%doc COPYRIGHT
%{_bindir}/*
%{_mandir}/man1/*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.20-30
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-20
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 23 2018 Christian Iseli <Christian.Iseli@unil.ch> - 0.20-15
- Fix FTBFS by adding BuildRequires for gcc (bz 1603320)
- Fix couple rpmlint warnings, bogus date in changelog

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Apr 19 2010 Christian Iseli <Christian.Iseli@licr.org> 0.20-1
- Version 0.20.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed May 07 2008 Christian Iseli <Christian.Iseli@licr.org> 0.17-1
- Version 0.17.

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.16-2
- Autorebuild for GCC 4.3

* Fri Nov 30 2007 Christian Iseli <Christian.Iseli@licr.org> 0.16-1
- Version 0.16.

* Thu Aug 16 2007 Christian Iseli <Christian.Iseli@licr.org> 0.15-2
- Fix License tag to GPLv2+.

* Tue Apr 24 2007 Christian Iseli <Christian.Iseli@licr.org> 0.15-1
- Version 0.15.
- Set Source0 according to Packaging/SourceURL

* Tue Nov  7 2006 Christian Iseli <Christian.Iseli@licr.org> 0.14-0
- Version 0.14.
- Source is .gz instead of .bz2.

* Tue Sep  5 2006 Christian Iseli <Christian.Iseli@licr.org> 0.13-2
- Rebuild for FC 6.

* Mon Jun 19 2006 Christian Iseli <Christian.Iseli@licr.org> 0.13-1
- Version 0.13.
- No longer needs math lib.

* Fri Jun  9 2006 Christian Iseli <Christian.Iseli@licr.org> 0.12-1
- Version 0.12.

* Thu Mar  9 2006 Christian Iseli <Christian.Iseli@licr.org> 0.11-1
- Version 0.11.

* Tue Feb 21 2006 Christian Iseli <Christian.Iseli@licr.org> 0.10-1
- Version 0.10.

* Wed Feb 15 2006 Christian Iseli <Christian.Iseli@licr.org> 0.9-2
- Rebuild for FE 5.

* Wed Jan 18 2006 Christian Iseli <Christian.Iseli@licr.org> 0.9-1
- Add LIBS=-lm.

* Fri Jan 13 2006 Christian Iseli <Christian.Iseli@licr.org> 0.9-0
- Version 0.9.

* Fri Aug 27 2004 Christian Iseli <Christian.Iseli@licr.org>
- Version 0.8.

* Wed Jun 23 2004 Christian Iseli <Christian.Iseli@licr.org>
- Version 0.7.

* Thu May 27 2004 Christian Iseli <Christian.Iseli@licr.org>
- Version 0.6.

* Fri Apr 30 2004 Christian Iseli <Christian.Iseli@licr.org>
- Initial RPM release.
