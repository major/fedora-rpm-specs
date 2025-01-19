Name:           kcbench
Version:        0.9.11
Release:        2%{?dist}
Summary:        Benchmark that compiles a Linux kernel

License:        MIT:Modern Style with sublicense
URL:            https://gitlab.com/knurd42/kcbench
Source0:        https://gitlab.com/knurd42/kcbench/-/archive/v%{version}/kcbench-v%{version}.tar.bz2

BuildArch:      noarch

BuildRequires:  make

# needed for compiling a modern Linux kernels:
Requires:       make
Requires:       gcc
Requires:       binutils
Requires:       bison
Requires:       flex
Requires:       %{_bindir}/awk
Requires:       %{_bindir}/time
Requires:       %{_bindir}/bc
Requires:       %{_bindir}/lscpu
Requires:       %{_bindir}/pkill
Requires:       /usr/bin/pkg-config
Requires:       elfutils-libelf-devel
Requires:       openssl-devel
Requires:       curl
Requires:       perl-interpreter

%description
Compiles a Linux kernel to benchmark a system or test its stability.


%prep
%setup -q -n %{name}-v%{version}
echo "Nothing to prep"


%build
echo "Nothing to build"


%install
%{make_install} PREFIX=/usr/


%files
%{_bindir}/kcbench
%{_bindir}/kcbenchrate
%{_mandir}/man1/*
%{_docdir}/kcbench/

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Oct 16 2024 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0.9.11-1
- Update to 0.9.11

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Mar 13 2024 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0.9.10-1
- Update to 0.9.10

* Mon Mar 4 2024 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0.9.9-1
- Update to 0.9.9
- migrated to SPDX license

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Dec 12 2023 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0.9.8-1
- Update to 0.9.8

* Fri Sep 22 2023 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0.9.7-1
- Update to 0.9.7

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Mar 19 2023 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0.9.6-1
- Update to 0.9.6

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Feb 06 2022 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0.9.5-1
- Update to 0.9.5

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 18 2022 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0.9.3-1
- Update to 0.9.3

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Apr 07 2021 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0.9.2-1
- Update to 0.9.2

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 06 2020 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0.9.1-1
- Update to 0.9.1

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0.9.0-1
- brown paper bag release: rebuild with increased release value for proper
  update path

* Mon Jun 22 2020 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0.9.0-0
- Update to 0.9.0 and update list of requires

* Tue Jun 09 2020 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0.9.0-0.beta2.1
- Update to 0.9-beta.2

* Tue May 05 2020 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0.9.0-0.beta1.1
- Update to 0.9-beta.1

* Tue Apr 21 2020 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0.5.0-0.beta2.1
- Update to beta2 of 0.5

* Wed Apr 15 2020 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0.5.0-0.beta.1
- Update to beta1 of 0.5

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar 30 2019 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0.4-1
- Update to 0.4.1

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Oct 07 2018 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0.4-0.1
- Update to 0.4 and drop kcbench-data dep

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jul 03 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.3-14
- Add dist-tag (RHBZ #1237172).
- Modernize spec.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-13.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-12.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-11.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-10.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-9.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-8.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-7.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 04 2010 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0.3-6
- use type (bash built in) instead of which to check if all tools are available

* Mon May 24 2010 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0.3-5
- a few small adjutments
-- a few output format adjustments
-- fix cleaning up buildir
-- create compiledir properly if specified manually

* Sat Apr 24 2010 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0.3-4.1
- fix two typos -- one fixes #565325

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 10 2008 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]org> - 0.3-1
- update kcbench to 0.3:
-- fix typo
-- improve some comments

* Mon Dec 03 2007 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]org> - 0.2-1
- update to 0.2, which includes a ChangeLog and a manpage now

* Sat Oct 13 2007 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]org> - 0.1-2
- require make gcc and binutils, needed for kernel compile
- require /usr/bin/{time,bc} for kcbench
- include a README file

* Mon Oct 01 2007 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]org> - 0.1-1
- initial package
