Name:           perl-Mo
Version:        0.40
Release:        27%{?dist}
Summary:        Perl micro-object system
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Mo
Source0:        https://cpan.metacpan.org/authors/id/T/TI/TINITA/Mo-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Class::XSAccessor)
BuildRequires:  perl(constant)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::All)
BuildRequires:  perl(lib)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Mouse)
BuildRequires:  perl(Mouse::Role)
BuildRequires:  perl(Mouse::Util::MetaRole)
BuildRequires:  perl(PPI)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

%description
Mo provides the bare-minimum for a Perl object system, compared to other similar
systems such as Moose, Mouse and Moo.

%package Golf
Summary:        Mo minimization support module
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description Golf
%{summary}.

%package Moose
Summary:        Use Moose instead of Mo
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl(Moose)
Requires:       perl(Moose::Role)

%description Moose
%{summary}.

%package Mouse
Summary:        Use Mouse instead of Mo
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl(Mouse)
Requires:       perl(Mouse::Role)
Requires:       perl(Mouse::Util::MetaRole)

%description Mouse
%{summary}.

%prep
%setup -q -n Mo-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%exclude %{perl_vendorlib}/Mo/Golf.pm
%exclude %{perl_vendorlib}/Mo/Moose.pm
%exclude %{perl_vendorlib}/Mo/Mouse.pm
%{_mandir}/man3/*
%exclude %{_mandir}/man3/Mo::Golf.3pm.*
%exclude %{_mandir}/man3/Mo::Moose.3pm.*
%exclude %{_mandir}/man3/Mo::Mouse.3pm.*
%{_bindir}/*

%files Golf
%license LICENSE
%{perl_vendorlib}/Mo/Golf.pm
%{_mandir}/man3/Mo::Golf.3pm.*

%files Moose
%license LICENSE
%{perl_vendorlib}/Mo/Moose.pm
%{_mandir}/man3/Mo::Moose.3pm.*

%files Mouse
%license LICENSE
%{perl_vendorlib}/Mo/Mouse.pm
%{_mandir}/man3/Mo::Mouse.3pm.*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 26 2022 Emmanuel Seyman <emmanuel@seyman.fr> - 0.40-21
- Remove EL6 support (EL6 is EOL)
- Use %%{make_build} and %%{make_install} macros
- Replace %%{__perl} with /usr/bin/perl
+ Pass NO_PACKLIST and NO_PERLLOCAL to Makefile.PL

* Tue Dec 20 2022 Michal Josef Špaček <mspacek@redhat.com> - 0.40-20
- Split Mouse/Moose and Golf parts to separate packages
- Update license to SPDX format
- Use %%license macro

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.40-18
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.40-15
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.40-12
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.40-9
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.40-6
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.40-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Aug 25 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.40-1
- 0.40 bump

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.39-6
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.39-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.39-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.39-3
- Perl 5.22 rebuild

* Fri Nov 14 2014 David Dick <ddick@cpan.org> - 0.39-2
- Patch for EPEL6 distribution

* Sat Sep 13 2014 David Dick <ddick@cpan.org> - 0.39-1
- Upgrade to 0.39

* Wed Sep 03 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.38-2
- Perl 5.20 rebuild

* Thu Aug 21 2014 David Dick <ddick@cpan.org> - 0.38-1
- Initial release
