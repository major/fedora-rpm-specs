Name:           perl-Excel-Writer-XLSX
Version:        1.09
Release:        3%{?dist}
Summary:        Create a new file in the Excel 2007+ XLSX format
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Excel-Writer-XLSX
Source0:        https://cpan.metacpan.org/authors/id/J/JM/JMCNAMARA/Excel-Writer-XLSX-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  glibc-common
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Archive::Zip) >= 1.3
BuildRequires:  perl(autouse)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Date::Calc)
BuildRequires:  perl(Date::Manip)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Temp) >= 0.19
BuildRequires:  perl(integer)
BuildRequires:  perl(IO::File) >= 1.14
BuildRequires:  perl(lib)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
Requires:       perl(Archive::Zip) >= 1.3
Requires:       perl(File::Temp) >= 0.19
Requires:       perl(IO::File) >= 1.14
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:__requires_exclude|}^perl\\(Archive::Zip\\)$
%global __requires_exclude %__requires_exclude|^perl\\(File::Temp\\)$
%global __requires_exclude %__requires_exclude|^perl\\(IO::File\\)$

%description
The Excel::Writer::XLSX module can be used to create an Excel file in the
2007+ XLSX format.

%prep
%setup -q -n Excel-Writer-XLSX-%{version}
iconv --from=ISO-8859-1 --to=UTF-8 README > README.new
touch -r README.new README
mv README.new README

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README examples
%{perl_vendorlib}/*
%{_mandir}/man3/*
%{_mandir}/man1/*
%{_bindir}/*

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.09-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.09-2
- Perl 5.36 rebuild

* Fri Apr 29 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.09-1
- 1.09 bump

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.07-3
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 24 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.07-1
- 1.07 bump

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.03-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.03-3
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 09 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.03-1
- 1.03 bump

* Fri Nov 15 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.02-1
- 1.02 bump

* Wed Oct 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.01-1
- 1.01 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.00-2
- Perl 5.30 rebuild

* Mon Apr 08 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.00
- 1.00 bump

* Thu Feb 28 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.99-1
- 0.99 bump

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.98-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.98-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.98-2
- Perl 5.28 rebuild

* Fri Apr 20 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.98-1
- 0.98 bump

* Fri Apr 13 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.97-1
- 0.97 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.96-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Sep 18 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.96-1
- 0.96 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.95-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.95-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.95-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug 01 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.95-1
- 0.95 bump

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.88-2
- Perl 5.24 rebuild

* Tue Mar 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.88-1
- 0.88 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.86-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.86-1
- 0.86 bump

* Mon Oct 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.85-1
- 0.85 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.84-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.84-2
- Perl 5.22 rebuild

* Tue Apr 28 2015 David Dick <ddick@cpan.org> - 0.84-1
- Update to 0.84

* Thu Mar 19 2015 David Dick <ddick@cpan.org> - 0.83-1
- Update to 0.83

* Sat Nov 08 2014 David Dick <ddick@cpan.org> - 0.81-1
- Update to 0.81

* Sat Oct 18 2014 David Dick <ddick@cpan.org> - 0.79-1
- Update to 0.79

* Tue Sep 30 2014 David Dick <ddick@cpan.org> - 0.78-1
- Update to 0.78

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.77-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.77-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 David Dick <ddick@cpan.org> - 0.77-1
- Update to 0.77

* Sat Feb 01 2014 David Dick <ddick@cpan.org> - 0.76-1
- Initial release
