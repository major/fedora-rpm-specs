%define cvsver 20100106
%define codename BlameMichelson

Summary: Controllable Regex Mutilator: multi-method content classifier and filter
Name: crm114
Version: 0
Release: 33.%{cvsver}%{?dist}
URL: http://crm114.sourceforge.net/
# Automatically converted from old format: GPLv3 - review is highly recommended.
License: GPL-3.0-only
Source0: http://crm114.sourceforge.net/tarballs/%{name}-%{cvsver}-%{codename}.src.tar.gz
Patch0: %{name}-rpm.patch
Patch1: %{name}-tre.patch
# fix build with gcc5 (rhbz#1239418)
Patch2: %{name}-gcc5.patch
# fix potential string format overflow caught by gcc
Patch3: %{name}-format-overflow.patch
# fix build with gcc10
Patch4: %{name}-gcc10.patch
BuildRequires: emacs
BuildRequires: gcc
BuildRequires: tre-devel >= 0.8.0
# for tests
BuildRequires: words
BuildRequires: make
Requires: emacs-filesystem >= %{_emacs_version}

%description 
CRM114 is a system to examine incoming e-mail, system log streams,
data files or other data streams, and to sort, filter, or alter the
incoming files or data streams according to the user's wildest
desires. Criteria for categorization of data can be by satisfaction of
regexes, by sparse binary polynomial matching with a Bayesian Chain
Rule evaluator, or by other means.

%prep
%setup -q -n %{name}-%{cvsver}-%{codename}.src
%patch -P0 -p1 -b .r
%patch -P1 -p1 -b .tre
%patch -P2 -p1 -b .gcc5
%patch -P3 -p1 -b .fmt-ovfl
%patch -P4 -p1 -b .gcc10
chmod 644 mailfilter.cf

%build
make OPTFLAGS="$RPM_OPT_FLAGS -fPIE" LDFLAGS="$RPM_LD_FLAGS -fPIE" %{?_smp_mflags}
%{_emacs_bytecompile} %{name}-mode.el

%install
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name},%{_emacs_sitelispdir}/crm114}
make DESTDIR=$RPM_BUILD_ROOT INSTALLFLAGS="-m 755 -p" install
install -pm 755 mail{filter,lib,reaver,trainer}.crm shuffle.crm $RPM_BUILD_ROOT%{_datadir}/%{name}/
install -pm 644 crm114-mode.elc $RPM_BUILD_ROOT%{_emacs_sitelispdir}/crm114
mv $RPM_BUILD_ROOT%{_emacs_sitelispdir}/{%{name}-mode.el,%{name}/}
chmod 644 $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{name}/%{name}-mode.el

%check
make megatest

%files
%doc README *.txt *.recipe *.example mailfilter.cf
%{_bindir}/*
%{_datadir}/%{name}
%{_emacs_sitelispdir}/%{name}

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0-33.20100106
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0-32.20100106
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-31.20100106
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-30.20100106
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-29.20100106
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-28.20100106
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-27.20100106
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-26.20100106
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-25.20100106
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-24.20100106
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-23.20100106
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-22.20100106
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Feb 20 2020 Dominik Mierzejewski <rpm@greysector.net> 0-21.20100106
- fix build with GCC10

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-20.20100106
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-19.20100106
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-18.20100106
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 21 2018 Dominik Mierzejewski <rpm@greysector.net> 0-17.20100106
- Add BR: gcc for https://fedoraproject.org/wiki/Changes/Remove_GCC_from_BuildRoot
- Drop ancient Obsoletes/Provides
- Fix a potential string format overflow caught by gcc

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-16.20100106
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-15.20100106
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-14.20100106
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-13.20100106
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-12.20100106
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-11.20100106
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jul 14 2015 Dominik Mierzejewski <rpm@greysector.net> 0-10.20100106
- fix build with gcc-5.x (rhbz#1239418)
- fix bogus date in changelog and clean up spec
- drop dual release versioning
- comply with Emacs packaging guidelines
- add missing BR: words for megatest

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-9.14.20100106
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-8.14.20100106
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-7.14.20100106
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-6.14.20100106
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-5.14.20100106
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-4.14.20100106
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-3.14.20100106
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-2.14.20100106
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jun 19 2010 Dominik Mierzejewski <rpm@greysector.net> 0-1.14.20100106
- updated to 20100106 "BlameMichelson"

* Sat Jun 19 2010 Dominik Mierzejewski <rpm@greysector.net> 0-1.13.20090807
- patch mailtrainer.crm to look for mailfilter.cf in $HOME/.crm114 by default
  and to allow specifying full path for shuffle.crm
- add full path to shuffle.crm in example mailfilter.cf

* Sun Sep 20 2009 Dominik Mierzejewski <rpm@greysector.net> 0-1.12.20090807
- included missing shuffle.crm (rhbz#520397)
- rebuilt against new tre
- improved Summary:

* Sun Aug 23 2009 Dominik Mierzejewski <rpm@greysector.net> 0-1.11.20090807
- updated to 20090807 "BlameThorstenAndJenny"
- dropped upstreamed patch hunks, rebased patch
- updated source URL
- license changed to GPLv3
- needs release note: .css files format has changed, they must be rebuilt

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-1.10.20080703
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-1.9.20080703
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jul 09 2008 Dominik Mierzejewski <rpm@greysector.net> 0-1.8.20080703
- updated to current "wget" version

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0-1.7.20070810
- Autorebuild for GCC 4.3

* Sat Oct 27 2007 Dominik Mierzejewski <rpm@greysector.net> 0-0.6.20070810
- updated to 20070810 "BlameTheSegfault"
- dropped obsolete patch

* Wed Aug 29 2007 Karol Trzcionka <karlikt at gmail.com> - 0-0.5.20070301
- Rebuild for BuildID

* Tue Apr 17 2007 Dominik Mierzejewski <rpm@greysector.net> 0-0.4.20070301
- fix testsuite on 64bit, patch by Jaakko Hyvätti

* Sun Apr 15 2007 Dominik Mierzejewski <rpm@greysector.net> 0-0.3.20070301
- updated to 20070301 "BlameBaltar"
- added missing quine.crm to testsuite
- no more crashes on x86_64, removed ExcludeArch, fixes #202893

* Tue Aug 29 2006 Dominik Mierzejewski <rpm@greysector.net> 0-0.2.20060704
- mass rebuild

* Wed Aug 16 2006 Dominik Mierzejewski <rpm@greysector.net> 0-0.1.20060704
- FE-compliant versioning
- emacs subpackage should require emacs-el
- simplified file list
- added %%check
- small patch to make 'make megatest' work from current dir
- ExcludeArch: x86_64 until 64bit tre is fixed

* Wed Jul 26 2006 Dominik Mierzejewski <rpm@greysector.net>
- 20060704a release
- added -emacs package with crm mode for emacs
- fixed parallel make build
- use dist tag
- shut up rpmlint

* Sun Feb 19 2006 Dominik Mierzejewski <rpm@greysector.net> 0-0.1.20060118
- FE compliance
- package mailfilter scripts

* Mon Dec 15 2003 Bill Yerazunis <wsy@merl.com>
- removed -RCx stuff, now version contains it.
- updated for version 20031215-RC12
- License is GPL, not Artistic, so I corrected that.

* Sat Dec 13 2003 Kevin Fenzi <kevin-crm114@tummy.com>
- Converted line endings from dos format to unix. 
- Changed BuildPreReq to be 'tre-devel' 
- Fixed install to install into rpm build root. 
- tested on redhat 9 with latest tre. 

* Wed Oct 22 2003 Nico Kadel-Garcia <nkadel@merl.com>
- Created RedHat compatible .spec file
- Added libtre dependency to avoid building second package
- Hard-coded "INSTALL_DIR" in build/install setups
