Name:           perl-Dancer
Version:        1.3521
Release:        6%{?dist}
Summary:        Lightweight yet powerful web application framework
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Dancer
Source0:        http://cpan.metacpan.org/authors/id/Y/YA/YANICK/Dancer-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(base)
BuildRequires:  perl(blib)
BuildRequires:  perl(bytes)
BuildRequires:  perl(Carp)
BuildRequires:  perl(CGI)
BuildRequires:  perl(Clone)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Hash::Merge::Simple)
BuildRequires:  perl(HTTP::Body) >= 1.07
BuildRequires:  perl(HTTP::Date)
BuildRequires:  perl(HTTP::Headers)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Server::Simple::PSGI) >= 0.11
BuildRequires:  perl(HTTP::Tiny) >= 0.014
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(JSON)
BuildRequires:  perl(lib)
BuildRequires:  perl(LWP)
BuildRequires:  perl(MIME::Types) >= 2.17
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(Plack::Builder)
BuildRequires:  perl(Pod::Coverage)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(strict)
BuildRequires:  perl(Template)
BuildRequires:  perl(Test::LongString)
BuildRequires:  perl(Test::More) >= 0.94
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(Test::Output)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Test::TCP)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Try::Tiny) >= 0.09
BuildRequires:  perl(URI) >= 1.59
BuildRequires:  perl(XML::Simple)
BuildRequires:  perl(YAML)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Run-time for tests:
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dump)
BuildRequires:  perl(Devel::Hide)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::stat)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(HTTP::CookieJar) >= 0.008
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(mro)
BuildRequires:  perl(Plack::Handler::FCGI)
BuildRequires:  perl(Plack::Runner)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(URI::Escape)
# Optional tests:
BuildRequires:  perl(HTTP::Parser::XS)
%if 0%{!?perl_bootstrap:1}
BuildRequires:  perl(Dancer::Session::Cookie) >= 0.14
%endif
Requires:       perl(HTTP::Body) >= 1.07
Requires:       perl(HTTP::Server::Simple::PSGI) >= 0.11
Requires:       perl(HTTP::Tiny) >= 0.014
Requires:       perl(MIME::Types) >= 2.17
Requires:       perl(Try::Tiny) >= 0.09
Requires:       perl(URI) >= 1.59
Requires:       perl(YAML)

%{?perl_default_filter}

# Do not export under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(HTTP::Body\\)\\s*$
%global __requires_exclude %{?__requires_exclude}|perl\\(HTTP::Server::Simple::PSGI\\)\\s*$
%global __requires_exclude %{?__requires_exclude}|perl\\(HTTP::Tiny\\)\\s*$
%global __requires_exclude %{?__requires_exclude}|perl\\(MIME::Types\\)\\s*$
%global __requires_exclude %{?__requires_exclude}|perl\\(Try::Tiny\\)\\s*$
%global __requires_exclude %{?__requires_exclude}|perl\\(URI\\)\\s*$

# Filter modules bundled for tests
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(t::lib.*\\)
%global __requires_exclude %{__requires_exclude}|^perl\\(EasyMocker\\)
%global __requires_exclude %{__requires_exclude}|^perl\\(FromDataApp\\)
%global __requires_exclude %{__requires_exclude}|^perl\\(LinkBlocker\\)
%global __requires_exclude %{__requires_exclude}|^perl\\(TestApp.*\\)
%global __requires_exclude %{__requires_exclude}|^perl\\(TestPlugin.*\\)
%global __requires_exclude %{__requires_exclude}|^perl\\(TestUtils\\)

%description
Dancer is a web application framework designed to be as effortless as
possible for the developer, taking care of the boring bits as easily as
possible, yet staying out of your way and letting you get on with writing
your code.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Dancer::Session::Cookie)
Requires:       perl(HTTP::Parser::XS)
Requires:       perl(JSON)
Requires:       perl(Template)
Requires:       perl(Test::Output)
Requires:       perl(Test::TCP)
Requires:       perl(XML::Simple)

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n Dancer-%{version}
# Temporary remove the test based on GH issue
# https://github.com/PerlDancer/Dancer/issues/1239
rm t/14_serializer/04_request_xml.t
perl -i -ne 'print $_ unless m{^t/14_serializer/04_request_xml.t}' MANIFEST

# Help generators to recognize Perl scripts
for F in `find t -name *.t`; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}/bin
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/author*
rm %{buildroot}%{_libexecdir}/%{name}/t/pod.t
rm %{buildroot}%{_libexecdir}/%{name}/t/00_base/08_pod_coverage_dancer.t
ln -s %{_bindir}/dancer %{buildroot}%{_libexecdir}/%{name}/bin
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# Some tests write into temporary files/directories. The solution is to
# copy the tests into a writable directory and execute them from there.
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
prove -I . -r -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset AUTHOR_TESTING
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc AUTHORS Changes examples
%{_bindir}/dancer
%{perl_vendorlib}/*
%{_mandir}/man1/dancer.1*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3521-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3521-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3521-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3521-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3521-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Feb 09 2023 Jitka Plesnikova <jplesnik@redhat.com> - 1.3521-1
- 1.3521 bump

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3520-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 03 2023 Jitka Plesnikova <jplesnik@redhat.com> - 1.3520-1
- 1.3520 bump
- Package tests

* Tue Nov 15 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.3513-15
- Stop executing the test 10_error_dumper_without_clone.t (BZ#2139414)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3513-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 03 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.3513-13
- Perl 5.36 re-rebuild of bootstrapped packages

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.3513-12
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3513-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3513-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 24 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.3513-9
- Perl 5.34 re-rebuild of bootstrapped packages

* Mon May 24 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.3513-8
- Perl 5.34 re-rebuild of bootstrapped packages

* Sat May 22 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.3513-7
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3513-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3513-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.3513-4
- Perl 5.32 re-rebuild of bootstrapped packages

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.3513-3
- Perl 5.32 rebuild

* Thu Mar 12 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.3513-2
- Add BR: perl(blib)

* Wed Feb 05 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.3513-1
- 1.3513 bump

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3512-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3512-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 02 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.3512-3
- Perl 5.30 re-rebuild of bootstrapped packages

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.3512-2
- Perl 5.30 rebuild

* Mon Apr 01 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.3512-1
- 1.3512 bump

* Wed Mar 20 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.3510-1
- 1.3510 bump

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3500-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 15 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.3500-1
- 1.3500 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3400-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 01 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.3400-3
- Perl 5.28 re-rebuild of bootstrapped packages

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.3400-2
- Perl 5.28 rebuild

* Mon Jun 18 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.3400-1
- 1.3400 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3202-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3202-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.3202-7
- Perl 5.26 re-rebuild of bootstrapped packages

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.3202-6
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3202-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed May 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.3202-4
- Perl 5.24 re-rebuild of bootstrapped packages

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.3202-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3202-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.3202-1
- 1.3202 bump

* Tue Sep 15 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.3142-1
- 1.3142 bump

* Tue Jul 07 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.3140-1
- 1.3140 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3138-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 15 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.3138-1
- 1.3138 bump

* Wed Jun 10 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.3136-3
- Perl 5.22 re-rebuild of bootstrapped packages

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.3136-2
- Perl 5.22 rebuild

* Mon May 25 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.3136-1
- 1.3136 bump

* Thu Apr 23 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.3135-1
- 1.3135 bump

* Mon Feb 23 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.3134-1
- 1.3134 bump

* Tue Oct 21 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.3132-1
- 1.3132 bump

* Thu Sep 18 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.3130-1
- 1.3130 bump

* Thu Sep 11 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.3129-1
- 1.3129 bump

* Sun Sep 07 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.3126-3
- Perl 5.20 re-rebuild of bootstrapped packages

* Tue Sep 02 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.3126-2
- Perl 5.20 rebuild

* Thu Jul 17 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.3126-1
- 1.3126 bump

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3124-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.3124-1
- 1.3124 bump

* Mon Apr 14 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.3123-1
- 1.3123 bump

* Thu Feb 06 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.3121-1
- 1.3121 bump

* Thu Jan 02 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.3120-1
- 1.3120 bump

* Tue Oct 29 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.3119-1
- 1.3119 bump

* Mon Sep 02 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.3118-1
- 1.3118 bump

* Wed Aug 14 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.3117-2
- Perl 5.18 re-rebuild of bootstrapped packages

* Thu Aug 08 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.3117-1
- 1.3117 bump

* Mon Aug 05 2013 Petr Pisar <ppisar@redhat.com> - 1.3116-3
- Perl 5.18 rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3116-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 08 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.3116-1
- 1.3116 bump

* Mon Jun 10 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.3115-1
- 1.3115 bump

* Tue Jun 04 2013 Petr Pisar <ppisar@redhat.com> - 1.3114-1
- 1.3114 bump

* Mon Jun 03 2013 Petr Pisar <ppisar@redhat.com> - 1.3113-2
- Fix CVE-2012-5572 (cookie name CR-LF injection) (bug #880330)

* Mon May 13 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.3113-1
- 1.3113 bump

* Tue May 07 2013 Petr Pisar <ppisar@redhat.com> - 1.3112-2
- Return proper exit code on dancer tool failure (bug #960184)

* Thu Apr 11 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.3112-1
- 1.3112 bump

* Thu Feb 28 2013 Petr Pisar <ppisar@redhat.com> - 1.3111-1
- 1.3111 bump

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3110-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Oct 08 2012 Petr Šabata <contyk@redhat.com> - 1.3110-1
- 1.3110 bump

* Mon Aug 27 2012 Petr Šabata <contyk@redhat.com> - 1.3100-1
- 1.3100 bump

* Thu Aug 23 2012 Petr Šabata <contyk@redhat.com> - 1.3099-1
- 1.3099 bump

* Mon Jul 30 2012 Jitka Plesnikova <jplesnik@redhat.com> 1.3098-1
- 1.3098 bump

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3097-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul 11 2012 Jitka Plesnikova <jplesnik@redhat.com> 1.3097-1
- 1.3097 bump

* Tue Jul 10 2012 Petr Pisar <ppisar@redhat.com> - 1.3095-3
- Perl 5.16 re-rebuild of bootstrapped packages

* Sat Jun 30 2012 Petr Pisar <ppisar@redhat.com> - 1.3095-2
- Perl 5.16 rebuild

* Tue Apr 10 2012 Marcela Mašláňová <mmaslano@redhat.com> - 1.3095-1
- 1.3095 bump
- 810865 bootstrap macro for test only BR

* Thu Mar 01 2012 Petr Šabata <contyk@redhat.com> - 1.3093-1
- 1.3093 bump

* Mon Jan 30 2012 Petr Šabata <contyk@redhat.com> - 1.3092-1
- 1.3092 bump
- Package examples

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3091-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jan 03 2012 Petr Pisar <ppisar@redhat.com> - 1.3091-2
- Enable optional tests requiring perl(Dancer::Session::Cookie).

* Mon Dec 19 2011 Petr Pisar <ppisar@redhat.com> - 1.3091-1
- 1.3091 bump

* Wed Dec 14 2011 Petr Šabata <contyk@redhat.com> - 1.3090-1
- 1.3090 bump

* Wed Oct 26 2011 Marcela Mašláňová <mmaslano@redhat.com> 1.3080-1
- 1.3080 bump

* Wed Aug 24 2011 Petr Sabata <contyk@redhat.com> - 1.3072-1
- 1.3072 bump

* Wed Aug 10 2011 Marcela Mašláňová <mmaslano@redhat.com> 1.3071-1
- update
- add filter for RPM 4.8

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 1.3040-3
- Perl mass rebuild

* Mon May 16 2011 Marcela Mašláňová <mmaslano@redhat.com> 1.3040-2
- add tests BR: CGI, YAML, Template, Clone

* Fri May 13 2011 Marcela Mašláňová <mmaslano@redhat.com> 1.3040-1
- Specfile autogenerated by cpanspec 1.79.
