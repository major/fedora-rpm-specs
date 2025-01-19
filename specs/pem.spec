Name:           pem
Version:        0.7.9
Release:        29%{?dist}
Summary:        Personal Expenses Manager

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only 
URL:            http://pjp.dgplug.org/tools/ 
Source0:        http://pjp.dgplug.org/tools/%{name}-%{version}.tar.gz 

BuildArch:      noarch
BuildRequires: make
BuildRequires:      perl-generators
Requires:       perl-interpreter

%description
GNU Pem, is a personal expenses manager. Pem lets keep track of
personal income and expense in an extremely elegant manner.
On Linux like systems, Pem works by storing the details in
a CSV file, placed in the  ~/.pem directory under your $HOME
directory; On Windows, the same file is placed in pem directory,
under the USERPROFILE directory. Each such file is named after
the current month, and is automatically created by Pem when you
enter the first record  for the month. It is not advisable to
edit these files by hand.

%prep
%setup -q


%build
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT/%{_infodir}/dir

%files
%doc README COPYING
%{_bindir}/pem
%{_mandir}/man1/pem.*
%{_infodir}/pem.*
%{_datadir}/pem/pem.txt


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.9-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.7.9-28
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.9-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.9-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.9-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.9-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.9-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.9-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.9-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.9-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.9-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.9-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.9-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.9-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.9-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.9-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 13 2017 Petr Pisar <ppisar@redhat.com> - 0.7.9-11
- perl dependency renamed to perl-interpreter
  <https://fedoraproject.org/wiki/Changes/perl_Package_to_Install_Core_Modules>

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 0.7.9-5
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Sep 16 2011 P J P <pj.pandit@yahoo.co.in> - 0.7.9-1
- New option -b --bare to generate daily report for small(40x15) screen of
  NanoNote - http://en.qi-hardware.com/wiki/Ben_NanoNote.

* Fri Jun 03 2011 P J P <pj.pandit@yahoo.co.in> - 0.7.8-1
- Pem became an official GNU package.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 13 2009 P J P <pj.pandit@yahoo.co.in> - 0.7.7-1
- Fixed a minor bug and did few changes recommended by PBP.

* Wed May 27 2009 P J P <pj.pandit@yahoo.co.in> - 0.7.6-1
- pem now uses `-M <mm>' value while showing monthly report
  with option `-m'. And new option -N <mm> to see reports between
  two given months.

* Tue May 12 2009 Kushal Das <kushal@fedoraproject.org> - 0.7.5-1
- New pem release, mostly bugfix

* Mon May 11 2009 Kushal Das <kushal@fedoraproject.org> - 0.7.4-1
- New pem release

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jul 29 2008 P J P <pj.pandit@yahoo.co.in> - 0.7.3-1
- Changed the ..share/info/dir menu entry of pem, in pem.texi.

* Mon Jul 21 2008 Kushal Das <kushal@fedoraproject.org> - 0.7.2-3
- Bumping the release

* Mon Jul 21 2008 Kushal Das <kushal@fedoraproject.org> - 0.7.2-2
- Fixing Info dir problem

* Wed Jul 2 2008 Kushal Das <kushal@fedoraproject.org> - 0.7.2-1
- New release of pem

* Sun May 4 2008 Kushal Das <kushal@fedoraproject.org> - 0.7.1-4
- Fixed the description

* Wed Apr 30 2008 Kushal Das <kushal@fedoraproject.org> - 0.7.1-3
- Changed the summery as suggested in #fedora-devel

* Wed Apr 30 2008 Kushal Das <kushal@fedoraproject.org> - 0.7.1-2
- Fixed all small errors as came in review

* Tue Apr 29 2008 Kushal Das <kushal@fedoraproject.org> - 0.7.1-1
- First spec
