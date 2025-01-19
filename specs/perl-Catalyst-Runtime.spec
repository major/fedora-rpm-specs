Name:           perl-Catalyst-Runtime
Summary:        Catalyst Framework Runtime
Version:        5.90132
Release:        2%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

Source0:        https://cpan.metacpan.org/authors/id/J/JJ/JJNAPIORK/Catalyst-Runtime-%{version}.tar.gz
URL:            https://metacpan.org/release/Catalyst-Runtime
BuildArch:      noarch

BuildRequires:  groff
BuildRequires:  /usr/bin/perldoc
BuildRequires:  make
BuildRequires:  perl-doc
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(attributes)
BuildRequires:  perl(base)
BuildRequires:  perl(bytes)
BuildRequires:  perl(Carp)
# CGI::Simple::Cookie >= 1.109 is required, the latest version is 1.15
BuildRequires:  perl(CGI::Simple::Cookie) >= 1.11
BuildRequires:  perl(CGI::Struct)
BuildRequires:  perl(Class::Accessor)
BuildRequires:  perl(Class::Accessor::Fast)
BuildRequires:  perl(Class::C3::Adopt::NEXT) >= 0.07
BuildRequires:  perl(Class::Load) >= 0.12
BuildRequires:  perl(Class::MOP) >= 0.95
BuildRequires:  perl(Class::MOP::Object)
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dump)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Data::OptList)
BuildRequires:  perl(Devel::Cycle)
BuildRequires:  perl(Devel::InnerPackage)
BuildRequires:  perl(Encode) >= 2.21
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Copy::Recursive)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Spec::Unix)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Hash::MultiValue)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(HTML::HeadParser)
BuildRequires:  perl(HTTP::Body) >= 1.06
BuildRequires:  perl(HTTP::Body::OctetStream)
BuildRequires:  perl(HTTP::Headers) >= 1.64
BuildRequires:  perl(HTTP::Headers::Util)
BuildRequires:  perl(HTTP::Message::PSGI)
BuildRequires:  perl(HTTP::Request) >= 5.814
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(HTTP::Response) >= 5.813
BuildRequires:  perl(HTTP::Status)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(lib)
BuildRequires:  perl(List::Util) >= 1.45
# LWP::UserAgent not used at tests
# Module::Pluggable::Object version from Module::Pluggable in META
BuildRequires:  perl(Module::Pluggable::Object) >= 4.7
BuildRequires:  perl(Moose) >= 1.03
BuildRequires:  perl(Moose::Meta::Class)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(MooseX::Emulate::Class::Accessor::Fast) >= 0.00903
BuildRequires:  perl(MooseX::Getopt) >= 0.30
BuildRequires:  perl(MooseX::MethodAttributes)
BuildRequires:  perl(MooseX::MethodAttributes::Role)
BuildRequires:  perl(MooseX::MethodAttributes::Role::AttrContainer::Inheritable) >= 0.24
BuildRequires:  perl(MooseX::Role::Parameterized)
BuildRequires:  perl(mro)
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(namespace::autoclean) >= 0.28
BuildRequires:  perl(namespace::clean) >= 0.23
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(Path::Class) >= 0.09
BuildRequires:  perl(Path::Class::Dir)
BuildRequires:  perl(Path::Class::File)
BuildRequires:  perl(PerlIO::utf8_strict)
BuildRequires:  perl(Plack::App::File)
BuildRequires:  perl(Plack::Builder)
BuildRequires:  perl(Plack::Loader)
BuildRequires:  perl(Plack::Middleware)
BuildRequires:  perl(Plack::Middleware::Conditional)
BuildRequires:  perl(Plack::Middleware::ContentLength)
BuildRequires:  perl(Plack::Middleware::FixMissingBodyInRedirect) >= 0.09
BuildRequires:  perl(Plack::Middleware::Head)
BuildRequires:  perl(Plack::Middleware::HTTPExceptions)
BuildRequires:  perl(Plack::Middleware::IIS6ScriptNameFix)
BuildRequires:  perl(Plack::Middleware::IIS7KeepAliveFix)
BuildRequires:  perl(Plack::Middleware::LighttpdScriptNameFix)
BuildRequires:  perl(Plack::Middleware::MethodOverride) >= 0.12
BuildRequires:  perl(Plack::Middleware::RemoveRedundantBody) >= 0.03
BuildRequires:  perl(Plack::Middleware::ReverseProxy) >= 0.04
BuildRequires:  perl(Plack::Middleware::Static)
# Plack::Request version from Plack in META
BuildRequires:  perl(Plack::Request) >= 0.9991
BuildRequires:  perl(Plack::Request::Upload)
BuildRequires:  perl(Plack::Test)
BuildRequires:  perl(Plack::Test::ExternalServer)
BuildRequires:  perl(Plack::Util)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Safe::Isa)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Socket) >= 1.96
BuildRequires:  perl(Stream::Buffered)
BuildRequires:  perl(strict)
BuildRequires:  perl(String::RewritePrefix) >= 0.004
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Text::SimpleTable) >= 0.03
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Tree::Simple) >= 1.15
BuildRequires:  perl(Tree::Simple::Visitor::FindByPath)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(Type::Library)
BuildRequires:  perl(Type::Utils)
BuildRequires:  perl(Types::Standard)
BuildRequires:  perl(URI) >= 1.35
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(URI::http)
BuildRequires:  perl(URI::https)
BuildRequires:  perl(URI::QueryParam)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)

# Optional tests:
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(FCGI)
BuildRequires:  perl(MooseX::Daemonize)
BuildRequires:  perl(Plack::Handler::Starman)
# Proc::ProcessTable not used without TEST_MEMLEAK=1
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(Type::Tiny) >= 1.000005


Requires:       perl(B::Hooks::EndOfScope) >= 0.08
# CGI::Simple::Cookie >= 1.109 is required, the latest version is 1.15
Requires:       perl(CGI::Simple::Cookie) >= 1.11
Requires:       perl(Class::C3::Adopt::NEXT) >= 0.07
Requires:       perl(Class::Load) >= 0.12
Requires:       perl(Class::MOP) >= 0.95
Requires:       perl(HTML::HeadParser)
Requires:       perl(HTTP::Body) >= 1.06
Requires:       perl(HTTP::Headers) >= 1.64
Requires:       perl(HTTP::Request) >= 5.814
Requires:       perl(HTTP::Response) >= 5.813
Requires:       perl(List::Util) >= 1.45
Requires:       perl(LWP::UserAgent)
Requires:       perl(Module::Pluggable::Object) >= 4.7
Requires:       perl(Moose) >= 1.03
Requires:       perl(MooseX::Emulate::Class::Accessor::Fast) >= 0.00903
Requires:       perl(MooseX::Getopt) >= 0.30
Requires:       perl(MooseX::MethodAttributes::Role::AttrContainer::Inheritable) >= 0.24
Requires:       perl(MooseX::Role::WithOverloading) >= 0.09
Requires:       perl(namespace::clean) >= 0.23
Requires:       perl(Path::Class) >= 0.09
Requires:       perl(Plack::Middleware::MethodOverride) >= 0.12
Requires:       perl(Plack::Middleware::ReverseProxy) >= 0.04
# Plack::Request version from Plack in META
Requires:       perl(Plack::Request) >= 0.9991
Requires:       perl(Plack::Test::ExternalServer)
Requires:       perl(Socket) >= 1.96
Requires:       perl(String::RewritePrefix) >= 0.004
Requires:       perl(Text::SimpleTable) >= 0.03
Requires:       perl(Tree::Simple) >= 1.15
Requires:       perl(URI) >= 1.35

# obsolete/provide Unicode encoding plugin (folded into runtime)
Provides:       perl-Catalyst-Plugin-Unicode-Encoding = 99.0
Obsoletes:      perl-Catalyst-Plugin-Unicode-Encoding <= 1.9

%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(CGI::Simple::Cookie\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Class::C3::Adopt::NEXT\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Class::Load\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Class::MOP\\)$
%global __requires_exclude %__requires_exclude|^perl\\(HTTP::Body\\)$
%global __requires_exclude %__requires_exclude|^perl\\(HTTP::Headers\\)$
%global __requires_exclude %__requires_exclude|^perl\\(HTTP::Request\\)$
%global __requires_exclude %__requires_exclude|^perl\\(List::Util\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Module::Pluggable::Object\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Moose\\)$
%global __requires_exclude %__requires_exclude|^perl\\(MooseX::Getopt\\)$
%global __requires_exclude %__requires_exclude|^perl\\(MooseX::MethodAttributes::Role::AttrContainer::Inheritable\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Path::Class\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Plack::Middleware::MethodOverride\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Plack::Middleware::ReverseProxy\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Plack::Request\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Socket\\)$
%global __requires_exclude %__requires_exclude|^perl\\(String::RewritePrefix\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Text::SimpleTable\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Tree::Simple\\)$
%global __requires_exclude %__requires_exclude|^perl\\(URI\\)$
%global __requires_exclude %__requires_exclude|^perl\\(namespace::autoclean\\)$
%global __requires_exclude %__requires_exclude|^perl\\(namespace::clean\\)$

%description
This is the primary class for the Catalyst-Runtime distribution.  It provides
the core of any runtime Catalyst instance.
 
%package        scripts
Summary:        Scripts for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       perl(Catalyst::Devel) >= 1.0

%description    scripts

The %{name}-scripts package contains scripts distributed with
%{name} but generally used for developing Catalyst applications.


%prep
%setup -q -n Catalyst-Runtime-%{version}

# something like this seems to beg for explicitness
perldoc perlgpl      > COPYING.gpl
perldoc perlartistic > COPYING.artistic

find .  -type f -exec chmod -c -x {} +
find t/ -type f -exec /usr/bin/perl -pi -e 's|^#!perl|#!/usr/bin/perl|' {} +

%build
PERL5_CPANPLUS_IS_RUNNING=1 /usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
# note that some of the optional tests we're enabling here will be skipped
# anyways, due to deps on Catalyst::Devel, etc.  We cannot depend on
# Catalyst::Devel, however, as it depends on us, and circular dep loops are
# never fun.  (Well, maybe to Zeno.)
#
# See also http://rt.cpan.org/Public/Bug/Display.html?id=27123

export TEST_LIGHTTPD=1
export TEST_HTTP=0

# see https://rt.cpan.org/Public/Bug/Display.html?id=42540
#export TEST_MEMLEAK=1

export TEST_POD=1
export TEST_STRESS=1

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
make clean

%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files scripts
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.90132-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Nov 10 2024 Emmanuel Seyman <emmanuel@seyman.fr> - 5.90132-1
- Update to 5.90132

* Mon Aug 05 2024 Miroslav Suchý <msuchy@redhat.com> - 5.90131-5
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.90131-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.90131-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.90131-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jul 24 2023 Emmanuel Seyman <emmanuel@seyman.fr> - 5.90131-1
- Update to 5.90131

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.90130-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.90130-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Nov 10 2022 Emmanuel Seyman <emmanuel@seyman.fr> - 5.90130-1
- Update to 5.90130

* Tue Sep 27 2022 Petr Pisar <ppisar@redhat.com> - 5.90129-2
- Specify all dependencies

* Sun Jul 31 2022 Emmanuel Seyman <emmanuel@seyman.fr> - 5.90129-1
- Update to 5.90129

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.90128-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 06 2022 Jitka Plesnikova <jplesnik@redhat.com> - 5.90128-2
- Perl 5.36 re-rebuild of bootstrapped packages

* Sun Jun 05 2022 Emmanuel Seyman <emmanuel@seyman.fr> - 5.90128-1
- Update to 5.90128
- Set TEST_HTTP to 0 since certain tests require Catalyst::Devel

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 5.90126-10
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.90126-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.90126-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 5.90126-7
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.90126-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.90126-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 5.90126-4
- Perl 5.32 rebuild

* Tue Mar 24 2020 Jitka Plesnikova <jplesnik@redhat.com> - 5.90126-3
- Add perl-doc for build

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.90126-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 20 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 5.90126-1
- Update to 5.90126
- Replace calls to %%{__perl} with /usr/bin/perl
- Replace calls to "make pure_install" with %%{make_install}
- Replace calls to make with %%{make_build}

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.90124-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 5.90124-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.90124-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jan 20 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 5.90124-1
- Update to 5.90124

* Sun Dec 02 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 5.90123-1
- Update to 5.90123

* Sun Nov 11 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 5.90122-1
- Update to 5.90122

* Sun Oct 21 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 5.90120-1
- Update to 5.90120

* Sun Sep 30 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 5.90119-1
- Update to 5.90119

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.90118-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 5.90118-2
- Perl 5.28 rebuild

* Sun May 06 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 5.90118-1
- Update to 5.90118
- Drop upstreamed patch

* Mon Apr 16 2018 Jitka Plesnikova <jplesnik@redhat.com> - 5.90117-5
- Update list of run-requires

* Fri Apr 13 2018 Jitka Plesnikova <jplesnik@redhat.com> - 5.90117-4
- Change version condition for CGI::Simple::Cookie

* Sun Mar 11 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 5.90117-3
- Apply patch to fix Time::HiRes assumptions

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.90117-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 28 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 5.90117-1
- Update to 5.90117
- Remove INC patch (no longer needed)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.90115-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 5.90115-3
- Perl 5.26 rebuild

* Wed May 24 2017 Jitka Plesnikova <jplesnik@redhat.com> - 5.90115-2
- Fix building on Perl without '.' in @INC

* Sun May 07 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 5.90115-1
- Update to 5.90115

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.90114-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Dec 25 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 5.90114-1
- Update to 5.90114

* Sun Aug 07 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 5.90112-1
- Update to 5.90112

* Sat Jul 23 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 5.90111-1
- Update to 5.90111

* Sun Jul 10 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 5.90106-1
- Update to 5.90106

* Fri Jun 10 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 5.90105-1
- Update to 5.90105

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 5.90104-2
- Perl 5.24 rebuild

* Tue Apr 05 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 5.90104-1
- Update to 5.90104

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.90103-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Nov 14 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 5.90103-1
- Update to 5.90103

* Sat Oct 31 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 5.90102-1
- Update to 5.90102

* Wed Sep 09 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 5.90101-1
- Update to 5.90101

* Sun Aug 30 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 5.90100-1
- Update to 5.90100
- Remove tests subpackage

* Thu Jul 30 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 5.90097-1
- Update to 5.90097

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.90093-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 5.90093-2
- Perl 5.22 rebuild

* Sun Jun 07 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 5.90093-1
- Update to 5.90093

* Sun May 24 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 5.90092-1
- Update to 5.90092

* Thu May 14 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 5.90091-1
- Update to 5.90091

* Sun Feb 22 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 5.90083-1
- Update to 5.90083

* Thu Feb 05 2015 Petr Pisar <ppisar@redhat.com> - 5.90082-3
- Remove unneeded dependency on Test::WWW::Mechanize::Catalyst causing a build
  cycle

* Thu Feb 05 2015 Petr Pisar <ppisar@redhat.com> - 5.90082-2
- Remove unneeded dependency on Catalyst::Action::RenderView causing a build
  cycle

* Sun Jan 11 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 5.90082-1
- Update to 5.90082

* Sun Jan 04 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 5.90079-1
- Update to 5.90079

* Thu Jan 01 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 5.90078-1
- Update to 5.90078

* Sun Dec 14 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 5.90077-2
- Obsolete/provide Unicode encoding plugin (folded into runtime)
- Fix upstream URL

* Fri Nov 28 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 5.90077-1
- Update to 5.90077

* Tue Sep 02 2014 Jitka Plesnikova <jplesnik@redhat.com> - 5.90019-6
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.90019-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Aug 05 2013 Petr Pisar <ppisar@redhat.com> - 5.90019-4
- Perl 5.18 rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.90019-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.90019-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Dec 07 2012 Iain Arnell <iarnell@gmail.com> 5.90019-1
- update to latest upstream version

* Sat Oct 27 2012 Iain Arnell <iarnell@gmail.com> 5.90018-1
- update to latest upstream version

* Sat Oct 20 2012 Iain Arnell <iarnell@gmail.com> 5.90017-1
- update to latest upstream version

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.90015-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 03 2012 Petr Pisar <ppisar@redhat.com> - 5.90015-2
- Perl 5.16 rebuild

* Tue Jul 03 2012 Iain Arnell <iarnell@gmail.com> 5.90015-1
- update to latest upstream version

* Sun Jul 01 2012 Petr Pisar <ppisar@redhat.com> - 5.90012-2
- Perl 5.16 rebuild

* Sat May 19 2012 Iain Arnell <iarnell@gmail.com> 5.90012-1
- update to latest upstream version

* Fri Mar 09 2012 Iain Arnell <iarnell@gmail.com> 5.90011-1
- update to latest upstream version
- resolves RHBZ#800241

* Sat Feb 18 2012 Iain Arnell <iarnell@gmail.com> 5.90010-1
- update to latest upstream version

* Sun Jan 22 2012 Iain Arnell <iarnell@gmail.com> 5.90007-2
- drop tests subpackage; move tests to main package documentation

* Thu Jan 12 2012 Iain Arnell <iarnell@gmail.com> 5.90007-1
- update to latest upstream version
- BR perldoc

* Sun Oct 30 2011 Iain Arnell <iarnell@gmail.com> 5.90006-1
- update to latest upstream version
- remove unnecessary explicit requires

* Mon Aug 29 2011 Iain Arnell <iarnell@gmail.com> 5.90002-1
- update to latest upstream version

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 5.80032-2
- Perl mass rebuild

* Mon Mar 07 2011 Iain Arnell <iarnell@gmail.com> 5.80032-1
- update to latest upstream version
- clean up spec for modern rpmbuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.80030-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 08 2011 Iain Arnell <iarnell@gmail.com> 5.80030-1
- update to latest upstream version
- update R/BR perl(MooseX::MethodAttributes::Inheritable) >= 0.24
- drop R perl(Class::Data::Inheritable)

* Sat Oct 09 2010 Iain Arnell <iarnell@gmail.com> 5.80029-1
- update by Fedora::App::MaintainerTools 0.006
- updating to latest GA CPAN version (5.80029)
- added a new br on perl(HTML::HeadParser) (version 0)
- altered br on perl(MooseX::Getopt) (0.25 => 0.30)
- added a new req on perl(HTML::HeadParser) (version 0)
- altered req on perl(MooseX::Getopt) (0.25 => 0.30)
- disable auto_install

* Sat Aug 28 2010 Iain Arnell <iarnell@gmail.com> 5.80025-1
- update by Fedora::App::MaintainerTools 0.006
- updating to latest GA CPAN version (5.80025)
- altered br on perl(CGI::Simple::Cookie) (0 => 1.109)
- added a new br on perl(Data::OptList) (version 0)
- altered br on perl(HTTP::Body) (1.04 => 1.06)
- altered br on perl(Moose) (0.93 => 1.03)
- altered req on perl(CGI::Simple::Cookie) (0 => 1.109)
- added a new req on perl(Class::Data::Inheritable) (version 0)
- added a new req on perl(Data::OptList) (version 0)
- altered req on perl(HTTP::Body) (1.04 => 1.06)
- altered req on perl(Moose) (0.93 => 1.03)
- dropped br on perl(Test::MockObject)

* Fri Jul  9 2010 Marcela Mašláňová <mmaslano@redhat.com> - 5.80021-3
- 590961 add missing BR (warnings about nroff in buil log)

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 5.80021-2
- Mass rebuild with perl-5.12.0

* Sun Mar 07 2010 Chris Weyl <cweyl@alumni.drew.edu> 5.80021-1
- update by Fedora::App::MaintainerTools 0.004
- PERL_INSTALL_ROOT => DESTDIR
- updating to latest GA CPAN version (5.80021)
- altered br on perl(Class::MOP) (0.83 => 0.95)
- altered br on perl(HTTP::Request) (0 => 5.814)
- altered br on perl(HTTP::Request::AsCGI) (0.8 => 1.0)
- altered br on perl(HTTP::Response) (0 => 5.813)
- altered br on perl(Moose) (0.90 => 0.93)
- added a new br on perl(MooseX::Getopt) (version 0.25)
- altered br on perl(MooseX::MethodAttributes::Inheritable) (0.16 => 0.19)
- added a new br on perl(MooseX::Role::WithOverloading) (version 0.05)
- added a new br on perl(MooseX::Types) (version 0)
- added a new br on perl(MooseX::Types::Common::Numeric) (version 0)
- altered br on perl(Test::More) (0 => 0.88)
- altered br on perl(namespace::clean) (0 => 0.13)
- dropped old BR on perl(Test::Pod::Coverage)
- altered req on perl(Class::MOP) (0.83 => 0.95)
- altered req on perl(HTTP::Request) (0 => 5.814)
- altered req on perl(HTTP::Request::AsCGI) (0.8 => 1.0)
- altered req on perl(HTTP::Response) (0 => 5.813)
- altered req on perl(Moose) (0.90 => 0.93)
- added a new req on perl(MooseX::Getopt) (version 0.25)
- altered req on perl(MooseX::MethodAttributes::Inheritable) (0.16 => 0.19)
- added a new req on perl(MooseX::Role::WithOverloading) (version 0.05)
- added a new req on perl(MooseX::Types) (version 0)
- added a new req on perl(MooseX::Types::Common::Numeric) (version 0)
- altered req on perl(namespace::clean) (0 => 0.13)
- dropped old requires on perl(Class::Accessor::Fast)
- dropped old requires on perl(Class::Data::Inheritable)
- dropped old requires on perl(File::Modified)

* Sat Sep 26 2009 Chris Weyl <cweyl@alumni.drew.edu> 5.80013-2
- dis-enable certain optional tests until a couple RT tix are resolved

* Sat Sep 26 2009 Chris Weyl <cweyl@alumni.drew.edu> 5.80013-1
- auto-update to 5.80013 (by cpan-spec-update 0.01)
- altered br on perl(Moose) (0.78 => 0.90)
- altered br on perl(MooseX::Emulate::Class::Accessor::Fast) (0.00801 => 0.00903)
- altered br on perl(MooseX::MethodAttributes::Inheritable) (0.15 => 0.16)
- altered br on perl(namespace::autoclean) (0 => 0.09)
- altered req on perl(Moose) (0.78 => 0.90)
- altered req on perl(MooseX::Emulate::Class::Accessor::Fast) (0.00801 => 0.00903)
- altered req on perl(MooseX::MethodAttributes::Inheritable) (0.15 => 0.16)
- altered req on perl(namespace::autoclean) (0 => 0.09)

* Tue Aug 25 2009 Chris Weyl <cweyl@alumni.drew.edu> 5.80011-1
- switch filtering system
- auto-update to 5.80011 (by cpan-spec-update 0.01)
- added a new br on perl(List::MoreUtils) (version 0)
- altered br on perl(Module::Pluggable) (3.01 => 3.9)
- altered br on perl(MooseX::MethodAttributes::Inheritable) (0.12 => 0.15)
- added a new req on perl(List::MoreUtils) (version 0)
- altered req on perl(Module::Pluggable) (3.01 => 3.9)
- altered req on perl(MooseX::MethodAttributes::Inheritable) (0.12 => 0.15)

* Mon Jul 27 2009 Chris Weyl <cweyl@alumni.drew.edu> 5.80007-1
- auto-update to 5.80007 (by cpan-spec-update 0.01)
- added a new br on perl(String::RewritePrefix) (version 0.004)
- added a new br on perl(Task::Weaken) (version 0)
- added a new br on perl(namespace::autoclean) (version 0)
- added a new req on perl(String::RewritePrefix) (version 0.004)
- added a new req on perl(Task::Weaken) (version 0)
- added a new req on perl(namespace::autoclean) (version 0)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.80005-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Jun 14 2009 Chris Weyl <cweyl@alumni.drew.edu> 5.80005-3
- flesh out to full requires list (from upstream metadata)
- auto-update to 5.80005 (by cpan-spec-update 0.01)
- added a new req on perl(Text::Balanced) (version 0)
- added a new req on perl(HTTP::Response) (version 0)
- added a new req on perl(LWP::UserAgent) (version 0)
- added a new req on perl(Scalar::Util) (version 0)
- added a new req on perl(CGI::Simple::Cookie) (version 0)
- added a new req on perl(Class::C3::Adopt::NEXT) (version 0.07)
- added a new req on perl(Class::MOP) (version 0.83)
- added a new req on perl(Time::HiRes) (version 0)
- added a new req on perl(MRO::Compat) (version 0)
- added a new req on perl(File::Modified) (version 0)
- added a new req on perl(HTTP::Headers) (version 1.64)
- added a new req on perl(Sub::Exporter) (version 0)
- added a new req on perl(Tree::Simple) (version 1.15)
- added a new req on perl(B::Hooks::EndOfScope) (version 0.08)
- added a new req on perl(namespace::clean) (version 0)
- added a new req on perl(HTML::Entities) (version 0)
- added a new req on perl(Moose) (version 0.78)
- added a new req on perl(Data::Dump) (version 0)
- added a new req on perl(Tree::Simple::Visitor::FindByPath) (version 0)
- added a new req on perl(Module::Pluggable) (version 3.01)
- added a new req on perl(Text::SimpleTable) (version 0.03)
- altered req on perl(HTTP::Request::AsCGI) (0.5 => 0.8)
- added a new req on perl(HTTP::Request) (version 0)
- added a new req on perl(HTTP::Body) (version 1.04)
- added a new req on perl(Path::Class) (version 0.09)
- added a new req on perl(MooseX::MethodAttributes::Inheritable) (version 0.12)
- added a new req on perl(URI) (version 1.35)
- added a new req on perl(Carp) (version 0)

* Sat Jun 13 2009 Iain Arnell <iarnell@gmail.com> 5.80005-2
- requires perl(MooseX::Emulate::Class::Accessor::Fast)

* Tue Jun 09 2009 Chris Weyl <cweyl@alumni.drew.edu> 5.80005-1
- auto-update to 5.80005 (by cpan-spec-update 0.01)
- altered br on perl(MooseX::MethodAttributes::Inheritable) (0.10 => 0.12)

* Fri May 29 2009 Chris Weyl <cweyl@alumni.drew.edu> 5.80004-1
- drop Catalyst::Manual exclusions (no longer present)
- streamline req/prov filtering
- auto-update to 5.80004 (by cpan-spec-update 0.01)
- added a new br on perl(Scalar::Util) (version 0)
- added a new br on perl(Class::MOP) (version 0.83)
- added a new br on perl(Time::HiRes) (version 0)
- added a new br on perl(MRO::Compat) (version 0)
- added a new br on perl(Sub::Exporter) (version 0)
- added a new br on perl(B::Hooks::EndOfScope) (version 0.08)
- added a new br on perl(namespace::clean) (version 0)
- added a new br on perl(Moose) (version 0.78)
- added a new br on perl(MooseX::MethodAttributes::Inheritable) (version 0.10)
- added a new br on perl(Carp) (version 0)
- added a new br on perl(Text::Balanced) (version 0)
- added a new br on perl(Class::C3::Adopt::NEXT) (version 0.07)
- altered br on perl(ExtUtils::MakeMaker) (0 => 6.42)
- added a new br on perl(Test::MockObject) (version 1.07)
- altered br on perl(HTTP::Request::AsCGI) (0.5 => 0.8)
- added a new br on perl(MooseX::Emulate::Class::Accessor::Fast) (version 0.00801)

* Sat Apr 11 2009 Chris Weyl <cweyl@alumni.drew.edu> 5.71001-2
- return Catalyst::Manual perl-Catalyst-Manual

* Thu Apr 02 2009 Chris Weyl <cweyl@alumni.drew.edu> 5.71001-1
- update to 5.71001

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.71000-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 25 2009 Chris Weyl <cweyl@alumni.drew.edu> 5.71000-1
- update to 5.71000

* Thu Oct 23 2008 Chris Weyl <cweyl@alumni.drew.edu> 5.7015-1
- update to 5.7015

* Mon Jun 23 2008 Chris Weyl <cweyl@alumni.drew.edu> 5.7014-3
- Quiet STDERR somewhat on build

* Sat May 31 2008 Chris Weyl <cweyl@alumni.drew.edu> 5.7014-2
- pull catalyst.pl back from perl-Catalyst-Devel, put into subpackage: too
  much of a headache to keep this bit of -Runtime in -Devel
- pull in tests
- deal with perl-Catalyst-Manual issues

* Sat May 31 2008 Chris Weyl <cweyl@alumni.drew.edu> 5.7014-1
- update to 5.7014

* Thu Mar 27 2008 Chris Weyl <cweyl@alumni.drew.edu> 5.7012-3
- nuke Catalyst/Manual.pm from this dist -- handled in perl-Catalyst-Manual

* Wed Mar 05 2008 Tom "spot" Callaway <tcallawa@redhat.com> 5.7012-2
- rebuild for new perl

* Sat Mar 01 2008 Chris Weyl <cweyl@alumni.drew.edu> 5.7012-1
- update to 5.7012

* Sun Oct 28 2007 Chris Weyl <cweyl@alumni.drew.edu> 5.7011-1
- update to 5.7011

* Mon May 14 2007 Chris Weyl <cweyl@alumni.drew.edu> 5.7007-4
- bump

* Mon May 14 2007 Chris Weyl <cweyl@alumni.drew.edu> 5.7007-3
- additional br's

* Fri Apr 27 2007 Chris Weyl <cweyl@alumni.drew.edu> 5.7007-2
- exclude catalyst.pl from this package -- it depends on
  perl(Catalyst::Helper), which is provided by perl-Catalyst-Devel (but which
  has a buildreq on this package).  We will provide catalyst.pl in
  perl-Catalyst-Devel instead.

* Tue Apr 10 2007 Chris Weyl <cweyl@alumni.drew.edu> 5.7007-1
- Specfile autogenerated by cpanspec 1.70.
