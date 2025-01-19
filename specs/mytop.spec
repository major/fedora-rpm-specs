%global         git b737f60
Summary:        A top clone for MySQL
Name:           mytop
Version:        1.7
Release:        32.%{git}%{?dist}
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://jeremy.zawodny.com/mysql/mytop
# Tarball created by
# $ git clone git://github.com/jzawodn/mytop.git
# $ cd mytop
# $ git archive --format=tar --prefix=mytop-1.7/ %{git} | xz > mytop-1.7-%{git}.tar.xz
Source0:        mytop-%{version}-%{git}.tar.xz
Patch01:        mytop-1.7-long.patch
Patch02:        mytop-1.7-undef-resolv.patch
Requires:       perl(DBD::mysql) >= 1
Requires:       perl(Term::ReadKey) >= 2.1
Requires:       perl(Term::ANSIColor) perl(Time::HiRes)
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl(DBD::mysql) >= 1
BuildRequires:  perl(DBI) >= 1.13
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Term::ReadKey) >= 2.1
BuildArch:      noarch

%description 
mytop is a console-based tool for monitoring the threads and overall
performance of MySQL servers. The user interface is modeled after
familiar top application.

%prep
%autosetup -p1

%build
%{__perl} Makefile.PL
make

%install
install -D -m 0644 blib/man1/mytop.1 %{buildroot}%{_mandir}/man1/mytop.1
install -D -m 0755 mytop %{buildroot}%{_bindir}/mytop

%check
make test

%files
%doc Changes README
%{_bindir}/mytop
%{_mandir}/man1/mytop.1*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-32.b737f60
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 1.7-31.b737f60
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-30.b737f60
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 30 2024 Terje Rosten <terje.rosten@ntnu.no> - 1.7-29.b737f60
- Some minor fixes

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-28.b737f60
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-27.b737f60
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-26.b737f60
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-25.b737f60
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-24.b737f60
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-23.b737f60
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-22.b737f60
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-21.b737f60
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-20.b737f60
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-19.b737f60
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-18.b737f60
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-17.b737f60
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-16.b737f60
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-15.b737f60
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-14.b737f60
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-13.b737f60
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-12.b737f60
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-11.b737f60
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-10.b737f60
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-9.b737f60
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 24 2013 Petr Pisar <ppisar@redhat.com> - 1.7-8.b737f60
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-7.b737f60
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-6.b737f60
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-5.b737f60
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-4.b737f60
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun May 09 2010 Terje Rosten <terje.rosten@ntnu.no> - 1.7-3.b737f60
- add patch to fix #589366

* Mon May 03 2010 Terje Rosten <terje.rosten@ntnu.no> - 1.7-2.b737f60
- add patch to fix #584602

* Sat Mar 27 2010 Terje Rosten <terje.rosten@ntnu.no> - 1.7-1.b737f60
- 1.7 (from github), fixing bz #577528

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-4
- rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-3
- rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Dec 30 2007 Terje Rosten <terje.rosten@ntnu.no> - 1.6-2
- remove explicit req on dbi, let rpm to the job

* Wed Dec 26 2007 Terje Rosten <terje.rosten@ntnu.no> - 1.6-1
- initial package
