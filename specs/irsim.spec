%global _hardened_build 1
Name:             irsim
Version:          9.7.104
Release:          17%{?dist}
Summary:          Switch-level simulator used even for VLSI

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:          GPL-2.0-only
URL:              http://opencircuitdesign.com/%{name}
Source0:          http://opencircuitdesign.com/%{name}/archive/%{name}-%{version}.tgz
BuildRequires:    gcc
BuildRequires:    tk-devel m4 libXt-devel
BuildRequires: make

%description
IRSIM is a tool for simulating digital circuits. It is a "switch-level"
simulator; that is, it treats transistors as ideal switches. Extracted
capacitance and lumped resistance values are used to make the switch a little
bit more realistic than the ideal, using the RC time constants to predict the
relative timing of events.

%prep
%autosetup

%build
# The sources heavily rely on implicit ints and implicit function
# declarations and are not compatible with C99.
%global build_type_safety_c 0
%set_build_flags
# ./configure kills CFLAGS
# Invoke scripts/configure directly
(cd scripts && %configure)
%make_build

%install
%make_install
mv %{buildroot}%{_libdir}/%{name}/doc/*.doc doc/
rm -rf %{buildroot}%{_libdir}/%{name}/doc/

%files
%doc COPYRIGHT README VERSION doc/
%{_bindir}/*
%{_libdir}/*
%{_mandir}/man1/%{name}*
%{_mandir}/man5/netchange.5.gz
%{_mandir}/man3/%{name}-analyzer.3.gz

%Changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 9.7.104-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 9.7.104-16
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.7.104-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.7.104-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.7.104-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 16 2023 Florian Weimer <fweimer@redhat.com> - 9.7.104-12
- Set build_type_safety_c to 0 (#2154596)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 9.7.104-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 9.7.104-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 17 2022 Florian Weimer <fweimer@redhat.com> - 9.7.104-9
- Build in C89 mode because of C99 incompatibilities (#2154596)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 9.7.104-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 9.7.104-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9.7.104-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9.7.104-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9.7.104-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9.7.104-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 9.7.104-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 02 2019 Filipe Rosset <rosset.filipe@gmail.com> - 9.7.104-1
- new upstream version 9.7.104, fixes rhbz #1720880

* Sun May 19 2019 Filipe Rosset <rosset.filipe@gmail.com> - 9.7.103-1
- new upstream version 9.7.103, removed upstreamed patch, fixes rhbz #1711635

* Sat May 18 2019 Filipe Rosset <rosset.filipe@gmail.com> - 9.7.102-1
- new upstream version 9.7.102, fixes rhbz #1480209
- added upstram patch to fix tclirsim.so build
- spec cleanup and modernization

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 9.7.100-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 9.7.100-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 09 2018 Filipe Rosset <rosset.filipe@gmail.com> - 9.7.100-1
- new upstream version 9.7.100

* Mon Apr 09 2018 Filipe Rosset <rosset.filipe@gmail.com> - 9.7.96-3
- added gcc as BR

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 9.7.96-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug 07 2017 Filipe Rosset <rosset.filipe@gmail.com> - 9.7.96-1
- Rebuilt for new upstream release 9.7.96, fixes RHBZ#1428358

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9.7.95-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9.7.95-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9.7.95-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Nov 05 2016 Filipe Rosset <rosset.filipe@gmail.com> - 9.7.95-1
- Rebuilt for new upstream release 9.7.95, fixes RHBZ#1377004

* Tue Sep 13 2016 Filipe Rosset <rosset.filipe@gmail.com> - 9.7.94-1
- Rebuilt for new upstream release 9.7.94, fixes RHBZ#1359441

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 9.7.92-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul 20 2015 Filipe Rosset <rosset.filipe@gmail.com> - 9.7.92-1
- Rebuilt for new upstream release 9.7.92

* Thu Jul 16 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 9.7.87-4
- Use scripts/configure instead of configure (Fix F23FTBFS, RHBZ#1239581).

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.7.87-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 09 2014 Filipe Rosset <rosset.filipe@gmail.com> - 9.7.87-1
- Rebuilt for new upstream release 9.7.87 + fix FTBFS, spec cleanup, fixes rhbz #1037137

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.7.68-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 15 2008 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 9.7.68-1
- new upstream release 9.7.68

* Thu Aug 23 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 9.7.50-1
- mass rebuild for fedora 8 - BuildID
- New upstream release

* Tue Apr 24 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 9.7.47-1
- new upstream release 9.7.47

* Thu Feb 22 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 9.7.45-1
- new upstream release 9.7.45

* Mon Feb 05 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 9.7.41-5
- fixed for other binaries - genspktbl, gentbl

* Mon Feb 05 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 9.7.41-4
- dropped patch0 which was used to test analyzer's status
- added README.fedora and screenshots to explain the white-on-white output on analyser

* Mon Feb 05 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 9.7.41-3.1
- Rewrite

* Fri Feb 02 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 9.7.41-3
- Rebuild

* Thu Feb 01 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 9.7.41-2.1
- Once create a directory and expand the source there
  so that all files expanded are removed correctly
- Another way to treat CFLAGS
- Keep timestamps

* Thu Feb 01 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 9.7.41-2
- fix for CFLAGS

* Tue Jan 31 2006 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 9.7.41-1
- Initial package.
