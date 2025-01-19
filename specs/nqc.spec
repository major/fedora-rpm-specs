Name:           nqc
Version:        3.1.7
Release:        38%{?dist}
Summary:        Not Quite C compiler

# Automatically converted from old format: MPLv1.0 - review is highly recommended.
License:        LicenseRef-Callaway-MPLv1.0
URL:            http://bricxcc.sourceforge.net/nqc/
Source0:        http://bricxcc.sourceforge.net/nqc/release/nqc-3.1.r6.tgz
Source1:        60-legousbtower.rules
Source2:        http://bricxcc.sourceforge.net/nqc/doc/faq.html
Source3:        http://bricxcc.sourceforge.net/nqc/doc/NQC_Manual.pdf
Source4:        http://bricxcc.sourceforge.net/nqc/doc/NQC_Guide.pdf
Source5:        http://bricxcc.sourceforge.net/nqc/doc/NQC_Tutorial.pdf
Source6:        http://bricxcc.sourceforge.net/nqc/doc/NQCTutorialSamples.zip
Source7:        http://people.cs.uu.nl/markov/lego/tutorial_n.doc
Source8:        http://people.cs.uu.nl/markov/lego/tutorial_d.doc
Source9:        http://people.cs.uu.nl/markov/lego/tutorial_j.pdf
Source10:       http://people.cs.uu.nl/markov/lego/tutorial_s.doc
Source11:       http://people.cs.uu.nl/markov/lego/tutorial_i.doc
Source12:       http://people.cs.uu.nl/markov/lego/tutorial_t.doc
Source13:       http://people.cs.uu.nl/markov/lego/tutorial_p.pdf
Patch0:         nqc-3.1.6-linux.patch
Patch1:         nqc-3.1.6.gcc47.patch
Patch2:         nqc-3.1.6-unistd.patch
BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  flex >= 2.5 
BuildRequires:  byacc
Requires(pre):  %{_sbindir}/groupadd

%description
Not Quite C is a simple language with a C-like syntax that can be used to
program Lego's RCX programmable brick (from the Mindstorms set).

%package        doc
Summary:        English Documentation for NQC
Supplements:    (%{name} = %{version}-%{release} and langpacks-en)

%description    doc
English Documentation for NQC

%package        doc-nl
Summary:        Dutch Documentation for NQC
Supplements:    (%{name} = %{version}-%{release} and langpacks-nl)

%description	doc-nl
Dutch Documentation for NQC

%package        doc-de
Summary:        German Documentation for NQC
Supplements:    (%{name} = %{version}-%{release} and langpacks-de)

%description	doc-de
German Documentation for NQC

%package        doc-ja
Summary:        Japanese Documentation for NQC
Supplements:    (%{name} = %{version}-%{release} and langpacks-ja)

%description	doc-ja
Japanese Documentation for NQC

%package        doc-es
Summary:        Spanish Documentation for NQC
Supplements:    (%{name} = %{version}-%{release} and langpacks-es)

%description	doc-es
Spanish Documentation for NQC

%package        doc-it
Summary:        Italian Documentation for NQC
Supplements:    (%{name} = %{version}-%{release} and langpacks-it)

%description	doc-it
Italian Documentation for NQC

%package        doc-th
Summary:        Thai Documentation for NQC
Supplements:    (%{name} = %{version}-%{release} and langpacks-th)

%description	doc-th
Thai Documentation for NQC

%package        doc-pt
Summary:        Portuguese Documentation for NQC
Supplements:    (%{name} = %{version}-%{release} and langpacks-pt)

%description	doc-pt
Portuguese Documentation for NQC

%prep
%setup -c -q -n nqc-3.1.r6
%patch -P0 -p1
%patch -P1 -p0
%patch -P2 -p0 -b .isatty

for i in %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5}; do
  %{__cp} --preserve=timestamps $i .
done

%{__cp} --preserve=timestamps %{SOURCE7} ./nqc-tutorial-nl.doc
%{__cp} --preserve=timestamps %{SOURCE8} ./nqc-tutorial-de.doc
%{__cp} --preserve=timestamps %{SOURCE9} ./nqc-tutorial-ja.pdf
%{__cp} --preserve=timestamps %{SOURCE10} ./nqc-tutorial-es.doc
%{__cp} --preserve=timestamps %{SOURCE11} ./nqc-tutorial-it.doc
%{__cp} --preserve=timestamps %{SOURCE12} ./nqc-tutorial-th.doc
%{__cp} --preserve=timestamps %{SOURCE13} ./nqc-tutorial-pt.pdf

%{__mkdir} tutorial_files
%{__unzip} -qq -a %{SOURCE6} -d tutorial_files


# This piece of software seems to come from the Dark Side. Fix permissions and
# line endings.
find -type f -exec chmod 644 {} \; -exec perl -pi -e 's/\r\n/\n/g' {} \;


%build
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install PREFIX=%{buildroot}%{_prefix} MANDIR=%{buildroot}%{_mandir}/man1
%{__rm} %{buildroot}%{_bindir}/mkdata
%{__install} -p -m 644 -D %{SOURCE1} %{buildroot}/lib/udev/rules.d/60-legousbtower.rules


%pre
if [ $1 -eq 1 ]; then
  %{_sbindir}/groupadd -f -r lego &>/dev/null || :
fi


%files
%{_bindir}/nqc
%{_mandir}/man1/nqc.1.gz
/lib/udev/rules.d/60-legousbtower.rules
%doc readme.txt LICENSE

%files doc
%doc scout.txt history.txt test.nqc
%doc faq.html NQC_Manual.pdf NQC_Guide.pdf NQC_Tutorial.pdf tutorial_files/

%files doc-nl
%lang(nl) %doc nqc-tutorial-nl.doc

%files doc-de
%lang(de) %doc nqc-tutorial-de.doc

%files doc-ja
%lang(ja) %doc nqc-tutorial-ja.pdf

%files doc-es
%lang(es) %doc nqc-tutorial-es.doc

%files doc-it
%lang(it) %doc nqc-tutorial-it.doc

%files doc-th
%lang(th) %doc nqc-tutorial-th.doc

%files doc-pt
%lang(pt) %doc nqc-tutorial-pt.pdf

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 3.1.7-37
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Mar 12 2016 Parag Nemade <pnemade AT redhat DOT com> - 3.1.7-18
- Add Supplements: for https://fedoraproject.org/wiki/Packaging:Langpacks guidelines

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 3.1.7-15
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Feb 23 2013 Rich Mattes <richmattes@gmail.com> - 3.1.7-11
- Fixed isatty() link error by using unistd.h

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 17 2012 Rich Mattes <richmattes@gmail.com> - 3.1.7-9
- Fixed udev rules and install directory (rhbz#748203)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Nov 19 2009 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> - 3.1.6-7
- Changed bison BR to byacc

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed May 20 2009 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> - 3.1.6-5
- Added lang(xx) directives to international files

* Wed Apr  1 2009 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> - 3.1.6-4
- Added multi-lingual doc packages and split English docs into their own package
- Added -p to udev rules file on install
- Added preserve timestamps to docs

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 3.1.6-2
- Autorebuild for GCC 4.3

* Wed Sep 20 2007 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> - 3.1.6-1
- Updated license to reflect specific MPL version
- New upstream release
- Added NQC tutorial and samples to docs
- Added -c option to setup to create top-level directory

* Sat Feb 03 2007 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> - 3.1.4-6
- Added RPM_OPTS to Makefile in patch

* Sun Aug 27 2006 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> - 3.1.4-5
- Readded BuildRequires for bison

* Sun Aug 27 2006 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> - 3.1.4-4
- Bump release for mass rebuild

* Sun Aug 20 2006 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> - 3.1.4-3
- Added BuildRequires for bison

* Sun Aug 20 2006 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> - 3.1.4-2
- Removed groupdel lego
- Added faq, manual and guide docs
- Added flex BuildRequires and groupadd Requires(pre)
- Added -f option to groupadd (success if group exists)

* Sat Aug 19 2006 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> - 3.1.4-1
- Removed alpha from version
- Changed make, rm and RPMBUILDROOT to macro forms
- Removed x86_64 exclude arch
- Added x86_64 + usb build patch
- Added lego group
- Added udev legousbtower rules

* Fri Mar 17 2006 Simon Perreault <nomis80@nomis80.org> - 3.1.r4-2
- Exclude x86_64: doesn't build and fix isn't trivial.

* Sat Mar 11 2006 Simon Perreault <nomis80@nomis80.org> - 3.1.r4-1
- Initial release.
