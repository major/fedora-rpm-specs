Name:           rpmreaper
Version:        0.2.0
Release:        35%{?dist}
Summary:        A tool for removing packages from system

License:        GPL-2.0-or-later
URL:            https://github.com/mlichvar/rpmreaper
Source0:        https://github.com/mlichvar/rpmreaper/archive/v%{version}/%{name}-%{version}.tar.gz
Patch1:         rpmreaper-provfilename.patch
Patch2:         rpmreaper-warnings.patch

BuildRequires: make
BuildRequires:  gcc ncurses-devel rpm-devel
Requires:       less rpm

%description
rpmreaper is a simple ncurses application with a mutt-like interface that
allows removing unnecessary packages and their dependencies from the system.

%prep
%setup -q
%patch -P1 -p1 -b .provfilename
%patch -P2 -p1 -b .warnings

%build
make %{?_smp_mflags} EXTRA_CFLAGS="$RPM_OPT_FLAGS"

%install
%makeinstall

%files
%doc COPYING NEWS README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri May 19 2023 Petr Pisar <ppisar@redhat.com> - 0.2.0-30
- Rebuild against rpm-4.19 (https://fedoraproject.org/wiki/Changes/RPM-4.19)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jul 26 2022 Miroslav Lichvar <mlichvar@redhat.com> 0.2.0-28
- fix compiler warnings

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-23
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 10 22:13:23 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.0-19
- Rebuild for RPM 4.15

* Mon Jun 10 15:42:05 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.0-18
- Rebuild for RPM 4.15

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 16 2018 Miroslav Lichvar <mlichvar@redhat.com> 0.2.0-16
- add gcc to build requirements

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Aug 11 2017 Kalev Lember <klember@redhat.com> - 0.2.0-13
- Rebuilt for RPM soname bump, take 3

* Thu Aug 10 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.2.0-12
- Rebuilt for RPM soname bump

* Thu Aug 10 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.2.0-11
- Rebuilt for RPM soname bump

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jul 28 2015 Miroslav Lichvar <mlichvar@redhat.com> 0.2.0-6
- rebuild for new rpm

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 06 2014 Miroslav Lichvar <mlichvar@redhat.com> 0.2.0-2
- canonize also provided filenames for symlinked system dirs

* Tue Apr 22 2014 Miroslav Lichvar <mlichvar@redhat.com> 0.2.0-1
- update to 0.2.0

* Wed Dec 04 2013 Miroslav Lichvar <mlichvar@redhat.com> 0.1.6-14
- fix building with -Werror=format-security (#1037309)
- remove obsolete macros
- fix weekdays in changelog

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Mar 23 2012 Miroslav Lichvar <mlichvar@redhat.com> 0.1.6-10
- rebuild for new rpm

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jun 01 2011 Miroslav Lichvar <mlichvar@redhat.com> 0.1.6-8
- call rpmcliFini() only on exit (#709421)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 31 2011 Miroslav Lichvar <mlichvar@redhat.com> 0.1.6-6
- fix reading of package provides

* Fri Jan 21 2011 Miroslav Lichvar <mlichvar@redhat.com> 0.1.6-5
- rebuild for new rpm
- use RPMDBI_PACKAGES index when iterating rpmdb (#671149)

* Tue Aug 24 2010 Miroslav Lichvar <mlichvar@redhat.com> 0.1.6-4
- print F2 as help key in help line (#472039)
- require less (#599183)

* Mon Feb 15 2010 Miroslav Lichvar <mlichvar@redhat.com> 0.1.6-3
- fix linking with --no-add-needed (#564724)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Apr 02 2009 Miroslav Lichvar <mlichvar@redhat.com> 0.1.6-1
- update to 0.1.6

* Fri Mar 06 2009 Jesse Keating <jkeating@redhat.com> - 0.1.5-3
- Rebuild for new rpm

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Sep 19 2008 Miroslav Lichvar <mlichvar@redhat.com> 0.1.5-1
- update to 0.1.5

* Mon Jul 14 2008 Miroslav Lichvar <mlichvar@redhat.com> 0.1.4-2
- fix building with new rpm (Panu Matilainen)

* Wed Jun 25 2008 Miroslav Lichvar <mlichvar@redhat.com> 0.1.4-1
- update to 0.1.4

* Tue Jun 03 2008 Miroslav Lichvar <mlichvar@redhat.com> 0.1.3-1
- initial release
