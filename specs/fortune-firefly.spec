Name:		fortune-firefly
Version:	2.1.2
Release:        37%{?dist}
Summary:	Quotes from the TV series "Firefly"

# No version specified, only attribution is spec file, but maintainer is upstream.
License:	GPL-1.0-or-later
URL:		http://www.daughtersoftiresias.org/progs/firefly/
#Source0:	http://www.daughtersoftiresias.org/progs/firefly/%{name}-%{version}.tar.bz2
Source1:	http://www.daughtersoftiresias.org/progs/firefly/fortune-firefly-%{version}/firefly
Source2:	http://www.daughtersoftiresias.org/progs/firefly/fortune-firefly-%{version}/README
BuildArch:	noarch
BuildRequires:	%{_bindir}/strfile

Requires:	fortune-mod

%description
Fortune-firefly provides a set of quotes from the popular television series
"Firefly", and its movie "Serenity", by Joss Whedon.  

Quote authors include Tim Minear, Joss Whedon, Ben Edulund, Jane Esperson,
Drew Z. Greenberg, Jose Molina, Cheryl Cain, and Brent Matthews.

%prep
%setup -T -c
cp %{SOURCE1} ./firefly
cp %{SOURCE2} ./README

%build
# generate the firefly.dat file
%{_bindir}/strfile firefly

%install
rm -rf $RPM_BUILD_ROOT
install -d m755 $RPM_BUILD_ROOT%{_datadir}/games/fortune
install -m644 firefly $RPM_BUILD_ROOT%{_datadir}/games/fortune/
install -m644 firefly.dat $RPM_BUILD_ROOT%{_datadir}/games/fortune/

%files
%doc README
%{_datadir}/games/fortune/firefly
%{_datadir}/games/fortune/firefly.dat


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 17 2024 Miroslav Suchý <msuchy@redhat.com> - 2.1.2-35
- convert license to SPDX

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Feb 08 2020 Bruno Wolff III <bruno@wolff.to> - 2.1.2-25
- strfile has moved from sbin to bin

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.1.2-20
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jul 18 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.1.2-6
- fix license tag

* Sun Jan 20 2008 Karen Pease <meme@daughtersoftiresias.org> - 2.1.2.5
- Upping tag to sync builds.

* Mon Jul 09 2007 Karen Pease <meme@daughtersoftiresias.org> - 2.1.2.4
- Upping tag to sync builds.

* Mon Jul 09 2007 Karen Pease <meme@daughtersoftiresias.org> - 2.1.2.3
- Upping tag to sync builds.

* Mon May 07 2007 Karen Pease <meme@daughtersoftiresias.org> - 2.1.2.2
- Upping tag to sync builds.

* Mon May 07 2007 Karen Pease <meme@daughtersoftiresias.org> - 2.1.2
- Spelling fixes

* Fri Sep 15 2006 Karen Pease <meme@daughtersoftiresias.org> - 2.1.1.2
- Rebuild

* Fri Apr 07 2006 Karen Pease <meme@daughtersoftiresias.org> - 2.1.1
- Manually merged in some fixes from Robert Mohr (mohr.42@osu.edu)

* Mon Jan 08 2006 Karen Pease <meme@daughtersoftiresias.org> - 2.1.0
- Incorporated some great organization and labeling by John Bianchi (John.Bianchi@usa.net)
- Added quotes from unfilmed episode, "Dead or Alive"
- Added quotes from deleted scenes
- Added quotes from outtakes

* Mon Dec 05 2005 Karen Pease <meme@daughtersoftiresias.org> - 2.0.1
- Incorporated some typo corrections from Zack Elan (zackelan@gmail.com)
- Changed the versioning style

* Wed Oct 12 2005 Karen Pease <meme@daughtersoftiresias.org> - 2.0
- Fixed some quotes, added one more.

* Wed Oct 12 2005 Karen Pease <meme@daughtersoftiresias.org> - 2.0
- Someone who wanted to remain anonymous graciously offered his time to
  correct Serenity quotes using a Visual Companion, which contains the
  shooting script.  TZOO-foo nee, doncoat!

* Tue Oct 11 2005 Karen Pease <meme@daughtersoftiresias.org> - 1.9.2 and 1.9.3
- Upped the release to fix a broken CVS tag

* Mon Oct 10 2005 Karen Pease <meme@daughtersoftiresias.org> - 1.9.1
- Fixed/added quotes

* Wed Oct 05 2005 Karen Pease <meme@daughtersoftiresias.org> - 1.8.2
- Modified Source1 and Source2 to use URLs
- Minor quote corrections

* Tue Oct 04 2005 Michael A. Peters <mpeters@mac.com> - 1.8.1
- build .dat file in rpm
- install in %%{_datadir}/games/fortune
- no need to use a tarball for two text files

* Tue Oct 04 2005 Karen Pease <meme@daughtersoftiresias.org> - 1.8.1
- Took in some requested user-contributed quote corrections

* Mon Oct  3 2005 Karen Pease <meme@daughtersoftiresias.org> - 1.7.2
- Added in README
- Repackaged without a nested tarball
- Incorporated specfile suggestions from Brian Pepple

* Mon Oct  3 2005 Karen Pease <meme@daughtersoftiresias.org> - 1.7.1
- Corrected/expanded some quotes

* Mon Oct  3 2005 Brian Pepple <bdpepple@ameritech.net> - 1.6-2
- Use some macros.
- Add fortune-mod requirement.
- Install into %%prefix, instead of %%datadir.
- Add prep, install, and clean sections.
- Add buildroot.

* Mon Oct 03 2005 Karen Pease <meme@daughtersoftiresias.org>
- Updated RPM package as per Fedora suggestions.

* Sat Oct 01 2005 Karen Pease <meme@daughtersoftiresias.org>
- Created RPM package; submitted to Fedora Extras.

* Fri Sep 30 2005 Karen Pease <meme@daughtersoftiresias.org>
- Added in preliminary quotes from Serenity; to be refined after transcripts are released.


