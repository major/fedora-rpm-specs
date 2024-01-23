Name:           perl-Growl-GNTP
Version:        0.21
Release:        23%{?dist}
Summary:        Perl implementation of GNTP Protocol (Client Part)
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Growl-GNTP
Source:         https://cpan.metacpan.org/authors/id/M/MA/MATTN/Growl-GNTP-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  perl-generators
BuildRequires:  perl(Crypt::CBC) >= 2.29
BuildRequires:  perl(Data::UUID) >= 0.149
BuildRequires:  perl(Digest::MD5) >= 2.36
BuildRequires:  perl(Digest::SHA) >= 5.45
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.36
BuildRequires:  perl(Filter::Util::Call)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Test::More)


%description
Growl::GNTP is Perl implementation of GNTP Protocol (Client Part).

%prep
%autosetup -p1 -n Growl-GNTP-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0

find %{buildroot} -type f -name .packlist -exec rm -f {} \;

%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes README.md
%license LICENSE
%dir %{perl_vendorlib}/Growl/
%{perl_vendorlib}/Growl/GNTP.pm
%{_mandir}/man3/Growl::GNTP*

%changelog
* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.21-19
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.21-16
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.21-13
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.21-10
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.21-7
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.21-4
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.21-2
- Perl 5.24 rebuild

* Sun Apr 10 2016 Miro Hrončok <mhroncok@redhat.com> - 0.21-1
- New upstream release (#1325567)
- removed dependency of IO::Socket::PortState
- Use Module::Build::Tiny instead of Module::Build
- add -- for options, otherwise it doesn't work

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.20-6
- Perl 5.22 rebuild

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.20-5
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 0.20-2
- Perl 5.18 rebuild

* Thu Jun 13 2013 Miro Hrončok <mhroncok@redhat.com> - 0.20-1
- New upstream release (#910272)
- Upstream changed the installation process to ExtUtils::MakeMaker
- Corrected bogus date in %%changelog

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 11 2013 Miro Hrončok <mhroncok@redhat.com> - 0.16-1
- New version

* Tue Nov 20 2012 Miro Hrončok <miro@hroncok.cz> - 0.15-4
- perl(inc::Module::Install) to perl(Module::Install)

* Mon Nov 19 2012 Miro Hrončok <miro@hroncok.cz> - 0.15-3
- Removed local inc and xs directories
- Patched source so it doesn't need them
- Removed lots of BR (builds in mock)

* Fri Nov 16 2012 Miro Hrončok <miro@hroncok.cz> - 0.15-2
- Removed BRs provided by perl package
- Removed useless perl autofilter
- Using dos2unix

* Fri Sep 28 2012 Miro Hrončok <miro@hroncok.cz> 0.15-1
- Specfile autogenerated by cpanspec 1.78 and revised.
