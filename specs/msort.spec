Summary:       Sort files in sophisticated ways
Name:          msort
Version:       8.53
Release:       57%{?dist}
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:       GPL-3.0-only
URL:           http://billposer.org/Software/msort.html
Source0:       http://billposer.org/Software/Downloads/msort-%{version}.tar.bz2
Patch0:        msort-8.53-dso.patch
Patch1:        msort-8.53-format.patch
Patch2:        msort-8.53-mlimits.patch
Patch3:        msort-configure-c99.patch
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc
BuildRequires: gmp-devel
BuildRequires: libicu-devel
BuildRequires: libuninum-devel >= 2.5
BuildRequires: make
BuildRequires: tre-devel >= 0.8.0
Requires:      iwidgets
%description
Msort is a program for sorting files in sophisticated ways. Records
need not be single lines. Key fields may be selected by position, tag,
or character range. For each key, distinct exclusions, multigraphs,
substitutions. and a sort order may be defined. Comparisons may be
lexicographic, numeric, by string length, date, or time. Optional keys
are supported. Msort uses the Unicode character set and provides full
Unicode case-folding. The basic program has a somewhat complex command
line interface, but may be driven by an optional GUI.

%prep
%autosetup -p1

%build
aclocal
automake --add-missing --copy
autoconf
export LDFLAGS="%{__global_ldflags} -fPIC"
export CFLAGS="%{optflags}"
%configure --disable-utf8proc
make %{?_smp_mflags} CFLAGS="%{optflags} -fPIC" LDFLAGS="%{__global_ldflags} -fPIC"

%install
make DESTDIR=%{buildroot} install
install -p -m 0644 -D msort.1 %{buildroot}%{_mandir}/man1/msort.1

%check
touch hybrid-ips.txt
./msort -ql -t SRC= -c h -t DST= -c h hybrid-ips.txt
rm hybrid-ips.txt

%files
%license COPYING
%doc AUTHORS ChangeLog Doc/* NEWS README TODO
%{_bindir}/msg
%{_bindir}/msort
%{_mandir}/man1/msort.1*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 8.53-57
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Dec 08 2024 Pete Walter <pwalter@fedoraproject.org> - 8.53-56
- Rebuild for ICU 76

* Wed Aug 07 2024 Miroslav Suchý <msuchy@redhat.com> - 8.53-55
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.53-54
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 31 2024 Pete Walter <pwalter@fedoraproject.org> - 8.53-53
- Rebuild for ICU 74

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.53-52
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.53-51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.53-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 František Zatloukal <fzatlouk@redhat.com> - 8.53-49
- Rebuilt for ICU 73.2

* Fri Jan 27 2023 Florian Weimer <fweimer@redhat.com> - 8.53-48
- Port configure script to C99 (#2164988)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.53-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 31 2022 Pete Walter <pwalter@fedoraproject.org> - 8.53-46
- Rebuild for ICU 72

* Mon Aug 01 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 8.53-45
- Rebuilt for ICU 71.1

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.53-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.53-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Oct 12 2021 Terje Rosten <terje.rosten@ntnu.no> - 8.53-42
- Add simple sanity check

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.53-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu May 20 2021 Pete Walter <pwalter@fedoraproject.org> - 8.53-40
- Rebuild for ICU 69

* Wed May 19 2021 Pete Walter <pwalter@fedoraproject.org> - 8.53-39
- Rebuild for ICU 69

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.53-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.53-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 15 2020 Pete Walter <pwalter@fedoraproject.org> - 8.53-36
- Rebuild for ICU 67

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.53-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 01 2019 Pete Walter <pwalter@fedoraproject.org> - 8.53-34
- Rebuild for ICU 65

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.53-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.53-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Pete Walter <pwalter@fedoraproject.org> - 8.53-31
- Rebuild for ICU 63

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.53-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Pete Walter <pwalter@fedoraproject.org> - 8.53-29
- Rebuild for ICU 62

* Mon Apr 30 2018 Pete Walter <pwalter@fedoraproject.org> - 8.53-28
- Rebuild for ICU 61.1

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.53-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 30 2017 Pete Walter <pwalter@fedoraproject.org> - 8.53-26
- Rebuild for ICU 60.1

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.53-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.53-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.53-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Apr 15 2016 David Tardon <dtardon@redhat.com> - 8.53-22
- rebuild for ICU 57.1

* Mon Feb 08 2016 Terje Rosten <terje.rosten@ntnu.no> - 8.53-21
- Fix one more build issue

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 8.53-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 28 2015 David Tardon <dtardon@redhat.com> - 8.53-19
- rebuild for ICU 56.1

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.53-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 09 2015 Terje Rosten <terje.rosten@ntnu.no> - 8.53-17
- Fix build issue

* Mon Jan 26 2015 David Tardon <dtardon@redhat.com> - 8.53-16
- rebuild for ICU 54.1

* Tue Aug 26 2014 David Tardon <dtardon@redhat.com> - 8.53-15
- rebuild for ICU 53.1

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.53-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.53-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Feb 14 2014 David Tardon <dtardon@redhat.com> - 8.53-12
- rebuild for new ICU

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.53-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 01 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 8.53-10
- Rebuild for icu 50
- spec cleanup as per recent guidelines changes

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.53-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr 23 2012 Terje Rosten <terje.rosten@ntnu.no> - 8.53-8
- Re-enable msg
- New icu

* Sun Feb 12 2012 Terje Rosten <terje.rosten@ntnu.no> - 8.53-7
- Remove msg for now

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.53-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Sep 12 2011 Terje Rosten <terje.rosten@ntnu.no> - 8.53-5
- rebuilt for new icu

* Sun Mar 13 2011 Terje Rosten <terje.rosten@ntnu.no> - 8.53-4
- rebuilt for new icu 4.4

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.53-3
- rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Apr 02 2010 Caolán McNamara <caolanm@redhat.com> - 8.53-2
- rebuilt for new icu 4.4

* Wed Feb 10 2010 Terje Rosten <terje.rosten@ntnu.no> - 8.53-1
- 8.53
- add DSO patch

* Sun Dec 06 2009 Dominik Mierzejewski <rpm@greysector.net> - 8.46-5
- rebuilt for new tre

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.46-4
- rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.46-3
- rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jun 03 2008 Caolán McNamara <caolanm@redhat.com> - 8.46-2
- rebuild for new icu

* Thu May 29 2008 Terje Rosten <terje.rosten@ntnu.no> - 8.46-1
- 8.46

* Tue May 20 2008 Terje Rosten <terje.rosten@ntnu.no> - 8.45-1
- 8.45
- random cleanup
- build with libicu
- add req on iwidgets

* Sun Jun 17 2007 Dries Verachtert - 8.40-1
- rebuild against libuninum 2.5.

* Tue Oct 18 2005 Dries Verachtert - 8.9-1
- initial package.
