Name:           cpanspec
Version:        1.78
Release:        54%{?dist}
Summary:        RPM spec file generation utility
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            http://cpanspec.sourceforge.net/
Source0:        http://sourceforge.net/downloads/%{name}/%{name}/%{version}/%{name}-%{version}.tar.gz
Patch0:         %{name}-1.78-Change-optimize-to-optflags.patch
Patch1:         %{name}-1.78-Strip-any-version-comparison-operator-from-the-perl-BR.patch
Patch2:         %{name}-1.78-Escape-slashes-in-filters.patch
Patch3:         %{name}-1.78-Prefer-dnf-over-repoquery.patch
Patch4:         %{name}-1.78-Fix-build-arguments-for-Build.PL-spec-conformance.patch
Patch5:         %{name}-1.78-Update-licenses-to-SPDX-form.patch
Patch6:         %{name}-1.78-Update_to_actual_fedora_rules.patch
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build)
Requires:       /usr/bin/curl
Requires:       /usr/bin/dnf
Requires:       rpm-build

%description
cpanspec generates spec files (and, optionally, source or even binary
packages) for Perl modules from CPAN for Fedora.  The quality of the spec
file is our primary concern.  It is assumed that maintainers will need to
do some (hopefully small) amount of work to clean up the generated spec
file to make the package build and to verify that all of the information
contained in the spec file is correct.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} %{buildroot}/*

%files
%{!?_licensedir:%global license %%doc}
%license Artistic COPYING
%doc BUGS Changes TODO
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.78-54
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Dec 05 2024 Michal Josef Špaček <mspacek@redhat.com> - 1.78-53
- Update to actual Fedora rules

* Fri Nov 08 2024 Michal Josef Špaček <mspacek@redhat.com> - 1.78-52
- Update licenses to SPDX form

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.78-51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Feb 09 2024 Michal Josef Špaček <mspacek@redhat.com> - 1.78-50
- Fix dnf repoquery --whatprovides
- Remove warnings with %patch macro

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.78-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.78-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.78-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 22 2023 Michal Josef Špaček <mspacek@redhat.com> - 1.78-46
- Update license to SPDX format

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.78-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.78-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.78-43
- Perl 5.36 rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.78-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.78-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.78-40
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.78-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.78-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.78-37
- Perl 5.32 rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.78-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.78-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.78-34
- Perl 5.30 rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.78-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.78-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.78-31
- Perl 5.28 rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.78-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.78-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.78-28
- Perl 5.26 rebuild

* Tue May 30 2017 Petr Šabata <contyk@redhat.com> - 1.78-27
- Include a Module::Build::Tiny compatibility fix, ghpr#5

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.78-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.78-25
- Perl 5.24 rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.78-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Sep 03 2015 Petr Šabata <contyk@redhat.com> - 1.78-23
- Prefer dnf over repoquery

* Thu Jun 25 2015 Petr Šabata <contyk@redhat.com> - 1.78-22
- Correct the dep list
- Modernize and clean the spec a bit

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.78-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.78-20
- Perl 5.22 rebuild

* Mon Dec 01 2014 Petr Šabata <contyk@redhat.com> - 1.78-19
- Escape slashes in filters (#544738)

* Thu Nov 06 2014 Petr Šabata <contyk@redhat.com> - 1.78-18
- Use %%{optflags} instead of %%{optimize} (#739461, b0bdaf23)
- Strip META perl version BR (#708377, c4069558)

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.78-17
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.78-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.78-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.78-14
- Perl 5.18 rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.78-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.78-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 07 2012 Petr Pisar <ppisar@redhat.com> - 1.78-11
- Perl 5.16 rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.78-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.78-9
- Perl mass rebuild

* Thu Jun 09 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.78-8
- Perl 5.14 mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.78-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jun 22 2010 Petr Pisar <ppisar@redhat.com> - 1.78-6
- Rebuild against perl-5.12
- Fix Source0 URL

* Fri Jun 11 2010 Mike McGrath <mmcgrath@redhat.com> - 1.78-5
- Release bump to fix broken perl(IO::Uncompress::Bunzip2)

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 1.78-4
- rebuild against perl 5.10.1

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.78-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.78-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 16 2009 Steven Pritchard <steve@kspei.com> 1.78-1
- Update to 1.78.

* Mon Jun 16 2008 Steven Pritchard <steve@kspei.com> 1.77-1
- Update to 1.77.

* Mon Jun 16 2008 Steven Pritchard <steve@kspei.com> 1.76-1
- Update to 1.76.

* Thu Jun 12 2008 Steven Pritchard <steve@kspei.com> 1.75-2
- Require rpm-build.

* Mon May 05 2008 Steven Pritchard <steve@kspei.com> 1.75-1
- Update to 1.75 (which really fixes BZ#437804).
- Require curl instead of wget (BZ#438245).
- Update description.

* Mon Mar 17 2008 Steven Pritchard <steve@kspei.com> 1.74-3
- Fix to work properly with 5.10.0 (BZ#437804).

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.74-2
- Rebuild for new perl

* Tue Dec 11 2007 Steven Pritchard <steve@kspei.com> 1.74-1
- Update to 1.74.
- Update License tag.

* Sun Jul 22 2007 Steven Pritchard <steve@kspei.com> 1.73-1
- Update to 1.73.

* Fri Jul 13 2007 Steven Pritchard <steve@kspei.com> 1.72-1
- Update to 1.72.

* Fri Jun 29 2007 Steven Pritchard <steve@kspei.com> 1.71-1
- Update to 1.71.
- Remove "Extras" from the description.
- Use the __perl macro instead of calling perl directly.

* Mon Mar 12 2007 Steven Pritchard <steve@kspei.com> 1.70-1
- Update to 1.70.

* Mon Oct 16 2006 Steven Pritchard <steve@kspei.com> 1.69.1-1
- Update to 1.69.1.

* Tue Oct 03 2006 Steven Pritchard <steve@kspei.com> 1.69-1
- Update to 1.69.
- Use _fixperms macro instead of our own chmod incantation.

* Sat Sep 16 2006 Steven Pritchard <steve@kspei.com> 1.68-2
- Fix find option order.

* Thu Jul 20 2006 Steven Pritchard <steve@kspei.com> 1.68-1
- Update to 1.68.
- Include Changes.

* Thu Jul 13 2006 Steven Pritchard <steve@kspei.com> 1.67-1
- Update to 1.67.

* Thu May 18 2006 Steven Pritchard <steve@kspei.com> 1.66-1
- Update to 1.66.
- Drop regex patch.
- cpanspec now uses repoquery.

* Thu May 04 2006 Steven Pritchard <steve@kspei.com> 1.65-2
- Add cpanspec-1.65-regex.patch (fix broken regex, from 1.66 CVS).

* Wed Apr 26 2006 Steven Pritchard <steve@kspei.com> 1.65-1
- Update to 1.65.
- cpanget requires wget.

* Sat Mar 25 2006 Steven Pritchard <steve@kspei.com> 1.64-1
- Update to 1.64.

* Fri Mar 24 2006 Steven Pritchard <steve@kspei.com> 1.63-1
- Update to 1.63.

* Wed Mar 22 2006 Steven Pritchard <steve@kspei.com> 1.62-1
- Update to 1.62.

* Sat Mar 11 2006 Steven Pritchard <steve@kspei.com> 1.61-1
- Update to 1.61.

* Tue Mar 07 2006 Steven Pritchard <steve@kspei.com> 1.60-1
- Update to 1.60.

* Wed Feb 01 2006 Steven Pritchard <steve@kspei.com> 1.59-2
- URL/Source0 on SourceForge.
- Use a more appropriate Group.

* Tue Sep 20 2005 Steven Pritchard <steve@kspei.com> 1.59-1
- Update to 1.59.

* Mon Sep 19 2005 Steven Pritchard <steve@kspei.com> 1.58-1
- Update to 1.58.
- Comment out bogus URL and Source0 URL.

* Fri Sep 16 2005 Steven Pritchard <steve@kspei.com> 1.55-1
- Update to 1.55.
- Include man page.
- Drop explicit module dependencies.  (rpmbuild will figure it out.)

* Fri Sep 16 2005 Steven Pritchard <steve@kspei.com> 1.54-1
- Update to 1.54.

* Mon Sep 05 2005 Steven Pritchard <steve@kspei.com> 1.49-1
- Update to 1.49.
- Remove unneeded BuildRequires (no tests).
- Remove explicit core module requirements.

* Sat Sep 03 2005 Steven Pritchard <steve@kspei.com> 1.46-1
- Initial rpm release.
