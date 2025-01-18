Summary: Utility to display new messages of a logfile since last run
Name: fetchlog
Version: 1.4
Release: 29%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
Url: http://sourceforge.net/projects/fetchlog
Source: http://dl.sf.net/sourceforge/fetchlog/fetchlog-%{version}.tar.gz

Buildrequires: gcc
BuildRequires: make

Patch0: fetchlog-build.patch
Patch1: fetchlog-unusedvar.patch
Patch2: fetchlog-1.4-write.patch
Patch3: fetchlog-1.4-tests.patch
Patch4: fetchlog-1.4-printf.patch

%description
The fetchlog utility displays the last new messages of a logfile. It is
similar like tail (1) but offers some extra functionality for output
formatting. To show only the new messages appeared since the last call
fetchlog uses a bookmark to remember which messages have been fetched.

%prep
%setup -q 
%patch -P0
%patch -P1 -p1
%patch -P2 -p0
%patch -P3 -p1
%patch -P4 -p1

%build
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
install -d %{buildroot}/%{_bindir}
install -d %{buildroot}/%{_mandir}/man1
install -m755 %{name} %{buildroot}/%{_bindir}
install -m644 %{name}.1 %{buildroot}/%{_mandir}/man1

%check
make test
make testall

%files 
%{_bindir}/%{name}
%doc CHANGES LICENSE README README.Nagios README.SNMP
%{_mandir}/*/*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.4-28
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Paul Wouters <pwouters@redhat.com> - 1.4-13
- Resolves: rhbz#1582773 FTBFS in Fedora 28 (Fix for -Werror=format-security errors with fprintf)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul  3 2012 Paul Wouters <pwouters@redhat.com> - 1.4-2
- Updated to 1.4-1 (rhbz#608241)
- Added patch for -Wunused and patch for bad CFLAGS
- write() patch with test case fixups

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 11 2009 Paul Wouters <paul@xelerance.com> - 1.2-1
- Updated to new upstream

* Mon Nov 24 2008 Paul Wouters <paul@xelerance.com> - 1.0-11
- Updates summary as per Richard Hughes guidelines

* Fri Jul 18 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.0-10
- fix license tag

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0-9
- Autorebuild for GCC 4.3

* Thu Sep  7 2006 Paul Wouters <paul@xelerance.com> - 1.0-8
- Rebuild requested for PT_GNU_HASH support from gcc

* Mon Mar  3 2006 Paul Wouters <paul@xelerance.com> - 1.0-7
- Bump version. this time cause of old .cvsignore

* Mon Mar  3 2006 Paul Wouters <paul@xelerance.com> - 1.0-6
- Bump version again :(

* Mon Mar  3 2006 Paul Wouters <paul@xelerance.com> - 1.0-5
- Bump version for build system

* Mon Feb  6 2006 Paul Wouters <paul@xelerance.com> - 1.0-4
- Bump version due to make tag error

* Mon Feb  6 2006 Paul Wouters <paul@xelerance.com> - 1.0-3
- Fixes by Ville Skyttä to honour $RPM_OPT_FLAGS and run make test

* Mon Jan 17 2006 Paul Wouters <paul@xelerance.com> - 1.0-2
- Fixed install target for man page and cleaning before install

* Mon Jan 16 2006 Paul Wouters <paul@xelerance.com> - 1.0-1
- Initial version for Fedora Extras
