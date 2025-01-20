Name:		perl-Mock-Quick
Version:	1.111
Release:	25%{?dist}
Summary:	Quickly mock objects and classes, side-effect free
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Mock-Quick
Source0:	http://cpan.metacpan.org/authors/id/E/EX/EXODIST/Mock-Quick-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(Module::Build) >= 0.42
# Module Runtime
BuildRequires:	perl(base)
BuildRequires:	perl(Carp)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(Exporter::Declare) >= 0.103
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(Fennec::Lite) >= 0.004
BuildRequires:	perl(Path::Class)
BuildRequires:	perl(Test::Exception) >= 0.29
BuildRequires:	perl(Test::More) >= 0.88
# Dependencies
# (none)

%description
Mock-Quick is here to solve the current problems with Mocking libraries.

There are a couple of Mocking libraries available on CPAN. The primary problems
with these libraries include verbose syntax, and most importantly side-effects.
Some Mocking libraries expect you to mock a specific class, and will unload it
then redefine it. This is particularly a problem if you only want to override
a class on a lexical level.

Mock-Object provides a declarative mocking interface that results in a very
concise, but clear syntax. There are separate facilities for mocking object
instances, and classes. You can quickly create an instance of an object with
custom attributes and methods. You can also quickly create an anonymous class,
optionally inheriting from another, with whatever methods you desire.

Mock-Object also provides a tool that provides an OO interface to overriding
methods in existing classes. This tool also allows for the restoration of the
original class methods. Best of all, this is a localized tool: when your
control object falls out of scope, the original class is restored.

%prep
%setup -q -n Mock-Quick-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} -c %{buildroot}

%check
./Build test

%files
%doc Changes README
%{perl_vendorlib}/Mock/
%{perl_vendorlib}/Object/
%{_mandir}/man3/Mock::Quick.3*
%{_mandir}/man3/Mock::Quick::Class.3*
%{_mandir}/man3/Mock::Quick::Method.3*
%{_mandir}/man3/Mock::Quick::Object.3*
%{_mandir}/man3/Mock::Quick::Object::Control.3*
%{_mandir}/man3/Mock::Quick::Util.3*
%{_mandir}/man3/Object::Quick.3*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.111-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.111-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.111-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.111-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.111-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.111-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.111-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.111-18
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.111-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.111-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.111-15
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.111-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.111-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.111-12
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.111-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.111-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.111-9
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.111-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.111-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.111-6
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.111-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.111-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.111-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.111-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu May 26 2016 Paul Howarth <paul@city-fan.org> - 1.111-1
- Update to 1.111
  - Documentation fixes
- BR: perl-generators
- Drop redundant Group: tag

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.110-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.110-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Sep  2 2015 Paul Howarth <paul@city-fan.org> - 1.110-1
- Update to 1.110
  - Fix #16, overloading + compare warning

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.108-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.108-3
- Perl 5.22 rebuild

* Sun Sep 07 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.108-2
- Perl 5.20 rebuild

* Sat Sep  6 2014 Paul Howarth <paul@city-fan.org> - 1.108-1
- Update to 1.108
  - Fix some warnings
  - Fix some typos

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.107-4
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.107-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Aug 15 2013 Paul Howarth <paul@city-fan.org> - 1.107-2
- Sanitize for Fedora submission

* Wed Aug 14 2013 Paul Howarth <paul@city-fan.org> - 1.107-1
- Initial RPM version
