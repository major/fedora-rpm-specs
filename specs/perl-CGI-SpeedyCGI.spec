# Module Magic Number
%{!?_httpd_mmn: %global _httpd_mmn %(cat %{_includedir}/httpd/.mmn 2> /dev/null || echo 0-0)}

%global pkgname CGI-SpeedyCGI

Summary:        Speed up perl scripts by running them persistently
Name:           perl-CGI-SpeedyCGI
Version:        2.22
Release:        57%{?dist}
License:        GPL-2.0-or-later
URL:            https://metacpan.org/release/%{pkgname}
Source0:        https://cpan.metacpan.org/modules/by-authors/id/H/HO/HORROCKS/%{pkgname}-%{version}.tar.gz
Source1:        10-speedycgi.conf
Source2:        example.conf
Patch0:         perl-CGI-SpeedyCGI-2.22-documentation.patch
Patch1:         perl-CGI-SpeedyCGI-2.22-empty_param.patch
Patch2:         perl-CGI-SpeedyCGI-2.22-strerror.patch
Patch3:         perl-CGI-SpeedyCGI-2.22-brigade_foreach.patch
Patch4:         perl-CGI-SpeedyCGI-2.22-exit_messages.patch
Patch5:         perl-CGI-SpeedyCGI-2.22-perl_510.patch
Patch6:         perl-CGI-SpeedyCGI-2.22-c99_inline.patch
Patch7:         CGI-SpeedyCGI-2.22-Fix-building-on-Perl-without-dot-in-INC.patch
# Fix building with GCC 10, bug #1793916, CPAN RT#131596
Patch8:         CGI-SpeedyCGI-2.22-Fix-building-with-GCC-10.patch
Patch9:         perl-CGI-SpeedyCGI-c99.patch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-interpreter >= 5.8.0
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(ExtUtils::Embed)
BuildRequires:  perl(strict)
BuildRequires:  sed

%description
SpeedyCGI is a way to run perl scripts persistently, which can make
them run much more quickly. After the script is initially run, instead
of exiting, the perl interpreter is kept running. During subsequent
runs, this interpreter is used to handle new executions instead of
starting a new perl interpreter each time. It is a very fast frontend
program, written in C, is executed for each request.

%package -n mod_speedycgi
Summary:        SpeedyCGI module for the Apache HTTP Server
BuildRequires:  httpd-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}, httpd >= 2.0.40
Requires:       httpd-mmn = %{_httpd_mmn}

%description -n mod_speedycgi
The SpeedyCGI module for the Apache HTTP Server. It can be used to run
perl scripts for web application persistently to make them more quickly.

%prep
%autosetup -p1 -n %{pkgname}-%{version}
cp -pf %{SOURCE2} .

%build
sed -i 's@apxs -@%{_httpd_apxs} -@g' Makefile.PL src/SpeedyMake.pl \
  mod_speedycgi/t/ModTest.pm mod_speedycgi/t/mod_perl.t
sed -i 's@APXS=apxs@APXS=%{_httpd_apxs}@g' mod_speedycgi/Makefile.tmpl

echo yes | perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
make OPTIMIZE="$RPM_OPT_FLAGS -Wno-incompatible-pointer-types" # doesn't understand %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

%if 0%{?rhel} && 0%{?rhel} <= 7
find $RPM_BUILD_ROOT \( -name perllocal.pod -o -name .packlist \) -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -empty -exec rm -f {} ';'
%endif
chmod -R u+w $RPM_BUILD_ROOT/*

install -D -p -m 0755 mod_speedycgi2/mod_speedycgi.so $RPM_BUILD_ROOT%{_httpd_moddir}/mod_speedycgi.so
install -D -p -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_httpd_modconfdir}/10-speedycgi.conf

%files
%license COPYING
%doc Changes README docs/*
%{_bindir}/speedy*
%{perl_vendorlib}/CGI

%files -n mod_speedycgi
%doc example.conf
%{_httpd_moddir}/mod_speedycgi.so
%config(noreplace) %{_httpd_modconfdir}/*.conf

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.22-57
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.22-56
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 10 2024 Jitka Plesnikova <jplesnik@redhat.com> - 2.22-55
- Perl 5.40 rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.22-54
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.22-53
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.22-52
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 2.22-51
- Perl 5.38 rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.22-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 10 2023 Florian Weimer <fweimer@redhat.com> - 2.22-49
- C99 compatibility fix

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.22-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.22-47
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.22-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.22-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.22-44
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.22-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.22-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.22-41
- Perl 5.32 rebuild

* Wed Jan 29 2020 Petr Pisar <ppisar@redhat.com> - 2.22-40
- Fix building with GCC 10 (bug #1793916)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.22-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.22-38
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.22-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.22-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.22-35
- Add build-require gcc

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.22-34
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.22-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 2.22-32
- Rebuilt for switch to libxcrypt

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.22-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.22-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.22-29
- Perl 5.26 rebuild

* Tue May 16 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.22-28
- Fix building on Perl without '.' in @INC

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.22-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.22-26
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.22-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.22-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.22-23
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.22-22
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.22-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.22-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 23 2014 Joe Orton <jorton@redhat.com> - 2.22-19
- fix _httpd_mmn expansion in absence of httpd-devel

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.22-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 2.22-17
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.22-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.22-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 2.22-14
- Perl 5.16 rebuild

* Wed Apr 18 2012 Joe Orton <jorton@redhat.com> - 2.22-13
- update for httpd 2.4 (with Jan Kaluza, #810133)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.22-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 2.22-11
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.22-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.22-9
- 661697 rebuild for fixing problems with vendorach/lib

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.22-8
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 2.22-7
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.22-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Robert Scheck <robert@fedoraproject.org> 2.22-5
- Rebuild against gcc 4.4 and rpm 4.6

* Thu Oct 30 2008 Robert Scheck <robert@fedoraproject.org> 2.22-4
- Fixed default configuration file reading loadmodule (#448320)

* Sun Oct 12 2008 Robert Scheck <robert@fedoraproject.org> 2.22-3
- Work around C99 inline issues caused by C99 inline support in
  newer GCC versions (#464963, thanks to Andreas Thienemann)

* Sun May 04 2008 Robert Scheck <robert@fedoraproject.org> 2.22-2
- Changes to match with Fedora Packaging Guidelines (#429609)

* Mon Jan 21 2008 Robert Scheck <robert@fedoraproject.org> 2.22-1
- Upgrade to 2.22
- Initial spec file for Fedora and Red Hat Enterprise Linux
