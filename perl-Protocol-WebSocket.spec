Name:           perl-Protocol-WebSocket
Version:        0.26
Release:        13%{?dist}
Summary:        WebSocket protocol
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Protocol-WebSocket
Source0:        https://cpan.metacpan.org/authors/id/V/VT/VTI/Protocol-WebSocket-%{version}.tar.gz
# includes Test::More with a higher version than available for epel6
Patch1:         test_simple_include.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Encode)
%if 0%{?el6}
BuildRequires:  perl(Exporter)
%endif
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(lib)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Module::Build::Tiny) >= 0.35
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
%if 0%{?el6}
BuildRequires:  perl(vars)
%endif
BuildRequires:  sed

%{?perl_default_filter}

%description
Client/server WebSocket message and frame parser/constructor. This module
does not provide a WebSocket server or client, but is made for using in
http servers or clients to provide WebSocket support.

%prep
%setup -q -n Protocol-WebSocket-%{version}
%{__sed} -i 's|\r||' ./examples/reflex.pl
%if 0%{?el6}
%patch1 -p1
%endif
# Upstream is okay with wsconsole being made available as a binary for Fedora/EPEL
# Module::Build::Tiny requires that all executables must be in script/
%{__mv} util script
%{__sed} -i -e '1s|#!/usr/bin/env perl|%(perl -MConfig -e 'print $Config{startperl}')|' script/* examples/*

%build
%{__perl} Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0

%{_fixperms} $RPM_BUILD_ROOT/*

%check
%if 0%{?el6}
PERL5LIB=test_simple_patch/lib ./Build test
%else
./Build test
%endif

%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc Changes examples
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_bindir}/*

%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.26-11
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.26-8
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.26-5
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.26-2
- Perl 5.30 rebuild

* Wed Mar 13 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.26-1
- 0.26 bump

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.24-3
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.24-1
- 0.24 bump

* Wed Jan 03 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.23-1
- 0.23 bump

* Mon Dec 11 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.22-1
- 0.22 bump

* Wed Sep 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.21-1
- 0.21 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.20-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 09 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.20-1
- 0.20 bump

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.19-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.19-1
- 0.19 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.18-3
- Perl 5.22 rebuild

* Wed Sep 03 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.18-2
- Perl 5.20 rebuild

* Wed Sep 03 2014 David Dick <ddick@cpan.org> - 0.18-1
- depend on Digest::SHA instead of Digest::SHA1

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.17-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Apr 12 2014 David Dick <ddick@cpan.org> - 0.17-1
- Initial release
