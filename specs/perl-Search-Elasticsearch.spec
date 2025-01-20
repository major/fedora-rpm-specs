Name:           perl-Search-Elasticsearch
Version:        8.12
Release:        3%{?dist}
Summary:        Official client for Elasticsearch
License:        Apache-2.0

URL:            https://metacpan.org/release/Search-Elasticsearch
Source0:        https://cpan.metacpan.org/authors/id/E/EZ/EZIMUEL/Search-Elasticsearch-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl(Any::URI::Escape)
BuildRequires:  perl(Cpanel::JSON::XS)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Hijk)
BuildRequires:  perl(HTTP::Headers)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Tiny)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(IO::Socket::SSL)
BuildRequires:  perl(IO::Uncompress::Inflate)
BuildRequires:  perl(JSON)
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(JSON::XS)
BuildRequires:  perl(lib)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Log::Any)
BuildRequires:  perl(Log::Any::Adapter)
BuildRequires:  perl(Log::Any::Adapter::Callback)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(Net::IP)
BuildRequires:  perl(overload)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::SharedFork)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::Escape::XS)
BuildRequires:  perl(warnings)
Requires:       perl(IO::Socket::SSL)
Requires:       perl(IO::Uncompress::Inflate)
Requires:       perl(JSON::XS)
Requires:       perl(MIME::Base64)
Requires:       perl(URI::Escape::XS)

%{?perl_default_filter}

%description
Search::Elasticsearch is the official Perl client for Elasticsearch,
supported by elasticsearch.com. Elasticsearch itself is a flexible and
powerful open source, distributed real-time search and analytics engine for
the cloud. You can read more about it on elasticsearch.org.

%prep
%setup -q -n Search-Elasticsearch-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/Search*
%{_mandir}/man3/Search*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 8.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Feb 04 2024 Emmanuel Seyman <emmanuel@seyman.fr> - 8.12-1
- Update to 8.12
- Convert license to SPDX.

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.00-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.00-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.00-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.00-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Jan 15 2023 Emmanuel Seyman <emmanuel@seyman.fr> - 8.00-1
- Update to 8.00

* Sun Jul 31 2022 Emmanuel Seyman <emmanuel@seyman.fr> - 7.717-1
- Update to 7.717

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.715-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 7.715-3
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.715-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Nov 14 2021 Emmanuel Seyman <emmanuel@seyman.fr> - 7.715-1
- Update to 7.715

* Sun Sep 26 2021 Emmanuel Seyman <emmanuel@seyman.fr> - 7.714-1
- Update to 7.714

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.30-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 22 2021 Jitka Plesnikova <jplesnik@redhat.com> - 7.30-3
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Sep 20 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 7.30-1
- Update to 7.30

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.81-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 29 2020 Jitka Plesnikova <jplesnik@redhat.com> - 6.81-2
- Perl 5.32 re-rebuild updated packages

* Sun Jun 28 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 6.81-1
- Update to 6.81

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 6.80-2
- Perl 5.32 rebuild

* Sun Apr 05 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 6.80-1
- Update to 6.80
- Replace calls to %%{__perl} with /usr/bin/perl
- Replace calls to "make install" with %%{make_install}
- Replace calls to make with %%{make_build}

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.00-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.00-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 6.00-6
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.00-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.00-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 6.00-3
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.00-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Nov 19 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 6.00-1
- Update to 6.00

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.02-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 5.02-2
- Perl 5.26 rebuild

* Sun Apr 09 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 5.02-1
- Update to 5.02

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.01-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Dec 25 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 5.01-1
- Update to 5.01

* Tue May 31 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 2.03-1
- Update to 2.03

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.02-2
- Perl 5.24 rebuild

* Thu Apr 28 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 2.02-1
- Update to 2.02

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.00-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Oct 31 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 2.00-1
- Update to 2.00

* Sun Aug 30 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 1.99-1
- Update to 1.99

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.20-2
- Perl 5.22 rebuild

* Sun May 17 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 1.20-1
- Update to 1.20

* Sun Jan 18 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 1.19-1
- Update to 1.19

* Sun Jan 04 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 1.17-1
- Update to 1.17

* Sat Nov 22 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 1.16-1
- Update to 1.16
- Drop Group tag
- Add %%license tag
- Tighten file listing

* Sun Nov 09 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 1.15-1
- Update to 1.15

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.14-2
- Perl 5.20 rebuild

* Sun Aug 03 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 1.14-1
- Update to 1.14

* Sun Jun 15 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 1.13-1
- Update to 1.13

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 29 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 1.12-1
- Update to 1.12

* Wed Apr 23 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 1.10-3
- Take into account other comments

* Sun Apr 20 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 1.10-2
- Take into account review comments (#1087988)

* Sun Mar 09 2014 Emmanuel Seyman <emmanuel@seyman.fr> 1.10-1
- Specfile autogenerated by cpanspec 1.78, with changes.
