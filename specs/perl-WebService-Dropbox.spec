Name:           perl-WebService-Dropbox
Version:        2.09
Release:        11%{?dist}
Summary:        Perl interface to Dropbox API
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/WebService-Dropbox
Source0:        https://cpan.metacpan.org/authors/id/A/AS/ASKADNA/WebService-Dropbox-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

# for running Build.PL
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(CPAN::Meta::Prereqs)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(utf8)

# Furl is optional, not yet available in Fedora
#BuildRequires:  perl(Furl) >= 3.11
BuildRequires:  perl(IO::Socket::SSL) >= 2.048
BuildRequires:  perl(HTTP::Message) >= 6.11
BuildRequires:  perl(JSON) >= 2.94
# optional
#BuildRequires:  perl(JSON::XS) >= 3.03
BuildRequires:  perl(LWP::Protocol::https) >= 6.07
BuildRequires:  perl(LWP::UserAgent) >= 6.26
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Build::Tiny) >= 0.035
BuildRequires:  perl(Net::OAuth) >= 0.28
BuildRequires:  perl(Software::License)
BuildRequires:  perl(URI) >= 1.71
# for tests
BuildRequires:  perl(Test::More) >= 1.302085
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Test::CPAN::Meta)
# not yet available in Fedora
#BuildRequires:  perl(Test::MinimumVersion::Fast) >= 0.04
BuildRequires:  perl(Test::Pod) >= 1.41
BuildRequires:  perl(Test::Spellunker) >= 0.2.7

# optional package, not yet available in Fedora
#Requires:       perl(Furl) >= 3.11
Requires:       perl(IO::Socket::SSL) >= 2.048
Requires:       perl(HTTP::Message) >= 6.11
Requires:       perl(JSON) >= 2.94
# optional
#Requires:       perl(JSON::XS) >= 3.03
Requires:       perl(LWP::Protocol::https) >= 6.07
Requires:       perl(LWP::UserAgent) >= 6.26
Requires:       perl(Net::OAuth) >= 0.28
Requires:       perl(Software::License)
Requires:       perl(URI) >= 1.71
Requires:       perl(HTTP::Request)
Obsoletes:      perl-Net-Dropbox-API <= 1.9

%description
This package provides a Perl interface to Dropbox API with following features:
- Support Dropbox v1 REST API
- Support Furl (Fast!!!)
- Streaming IO (Low Memory)
- Default URI Escape (The specified path is UTF-8 decoded string)

%prep
%setup -q -n WebService-Dropbox-%{version}

%build
%{__perl} Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -type f -name .packlist -delete

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README.md example HOW_TO_DEVELOPMENT.md
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.09-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Aug 06 2024 Miroslav Suchý <msuchy@redhat.com> - 2.09-10
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.09-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.09-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.09-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.09-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.09-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.09-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.09-3
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.09-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Nov 15 2021 Martin Gansser <martinkg@fedoraproject.org> - 2.09-1
- Update to 2.09

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.07-14
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.07-13
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.07-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.07-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.07-10
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.07-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.07-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.07-7
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.07-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.07-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.07-4
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.07-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.07-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 15 2017 Robin Lee <cheeselee@fedoraproject.org> - 2.07-1
- Update to 2.07

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.05-4
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.05-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug 22 2016 Li Rui Bin <lirb@winhong.com> - 2.05-2
- Obsoletes perl-Net-Dropbox-API for smooth upgrade path (BZ#1368854)

* Sun Jul 17 2016 Robin Lee <cheeselee@fedoraproject.org> - 2.05-1
- Update to 2.05 (BZ#1357222)
- BR added: perl(IO::Socket::SSL), perl(Module::Build::Tiny),
  perl(Test::CPAN::Meta), perl(Test::Pod), perl(Test::Spellunker)
- Requires added: perl(IO::Socket::SSL)

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.22-6
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.22-3
- Perl 5.22 rebuild

* Sat Oct 18 2014 Robin Lee <cheeselee@fedoraproject.org> - 1.22-2
- BR added: perl(CPAN::Meta), perl(CPAN::Meta::Prereqs), perl(File::Basename),
  perl(File::Spec), perl(utf8), perl(Data::Dumper), perl(Encode),
  perl(File::Temp), perl(HTTP::Request), perl(IO::File)
- BR removed: perl(IO::Socket::SSL)
- Requires added: perl(HTTP::Request)
- Removed version restriction of perl BR
- Description updated
- Remove useless documents

* Sun Oct 12 2014 Robin Lee <cheeselee@fedoraproject.org> 1.22-1
- Specfile autogenerated by cpanspec 1.78.
