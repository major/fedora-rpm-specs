Name:           perl-Server-Starter
Version:        0.35
Release:        21%{?dist}
Summary:        Superdaemon for hot-deploying server programs
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Server-Starter
Source0:        https://cpan.metacpan.org/authors/id/K/KA/KAZUHO/Server-Starter-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(base)
BuildRequires:  perl(Config)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Socket::UNIX)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Socket)
# Tests:
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(IO::Socket::IP)
BuildRequires:  perl(lib)
BuildRequires:  perl(Net::EmptyPort)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Test::SharedFork)
BuildRequires:  perl(Test::TCP) >= 2.08

# Remove under-specified depenendencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Test::TCP\\)$

%description
It is often a pain to write a server program that supports graceful
restarts, with no resource leaks. Server::Starter, solves the problem by
splitting the task into two. One is start_server, a script provided as a
part of the module, which works as a superdaemon that binds to zero or
more TCP ports, and repeatedly spawns the server program that actually
handles the necessary tasks (for example, responding to incoming
connections). The spawned server programs under Server::Starter call
accept(2) and handle the requests.

%package start_server
Summary:        perl-Server-Starter start_server script
Requires:       perl-Server-Starter = %{version}-%{release}

%description start_server
perl-Server-Starter's start_server script.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(IO::Socket::IP)
Requires:       perl(Test::TCP) >= 2.08

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n Server-Starter-%{version}
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done
chmod 0755 t/*.pl

%build
unset RELEASE_TESTING
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
unset AUTO_RESTART_INTERVAL ENABLE_AUTO_RESTART ENVDIR KILL_OLD_DELAY \
    SERVER_STARTER_GENERATION SERVER_STARTER_PORT
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset AUTO_RESTART_INTERVAL ENABLE_AUTO_RESTART ENVDIR KILL_OLD_DELAY \
    SERVER_STARTER_GENERATION SERVER_STARTER_PORT
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test

%files
%doc Changes README.md
%license LICENSE
%dir %{perl_vendorlib}/Server
%{perl_vendorlib}/Server/Starter
%{perl_vendorlib}/Server/Starter.pm
%{_mandir}/man3/Server::Starter.*

%files start_server
%{_bindir}/start_server
%{_mandir}/man1/start_server.*

%files tests
%{_libexecdir}/%{name}

%changelog
* Thu Jul 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_45_Mass_Rebuild

* Mon Jun 22 2026 Petr Pisar <ppisar@redhat.com> - 0.35-20
- Modernize a spec file
- Package the tests

* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 28 2022 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.35-11
- Convert license to SPDX.

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.35-9
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.35-6
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.35-3
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 25 2019 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.35-1
- Upstream update to 0.35.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.34-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.34-5
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.34-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.34-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.34-2
- Perl 5.28 rebuild

* Thu Mar 01 2018 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.34-1
- Upstream update to 0.34.
- Drop Server-Starter-0.33-Fix-building-on-Perl-without-.-in-INC.patch
  (Adopted by upstream).

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.33-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.33-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.33-3
- Perl 5.26 rebuild

* Thu May 18 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.33-2
- Add Server-Starter-0.33-Fix-building-on-Perl-without-.-in-INC.patch
  (RHBZ#1451638).

* Wed Mar 01 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.33-1
- Upstream update.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.32-4
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 31 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.32-2
- Modernize spec.

* Wed Aug 26 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.32-1
- Upstream update.

* Sun Jul 26 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.31-1
- Upstream update.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 11 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.30-1
- Upstream update.

* Thu Jun 11 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.29-1
- Upstream update.

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.28-2
- Perl 5.22 rebuild

* Sat May 30 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.28-1
- Upstream update.

* Fri May 01 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.27-1
- Upstream update.
- Reflect upstream having dropped bundling modules.
- Reflect upstream having re-added LICENCE.
- Reflect upstream having switched to Module::Build.

* Tue Apr 07 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.25-1
- Upstream update.
- Rework spec.
- Remove bundled modules.
- Drop Fedora/RH-patches.

* Tue Sep 09 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.17-9
- Perl 5.20 mass

* Tue Sep 09 2014 Petr Pisar <ppisar@redhat.com> - 0.17-8
- Fix a race between t/06-autorestart.t and t/05-killolddelay-echod.pl
  (bug #1100158)

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.17-7
- Perl 5.20 rebuild

* Thu Aug 21 2014 Petr Pisar <ppisar@redhat.com> - 0.17-6
- Fix t/05-killolddelay.t race (bug #1100158)

* Fri Aug 08 2014 Petr Pisar <ppisar@redhat.com> - 0.17-5
- Fix t/01-starter.t race (bug #1100158)

* Thu Jul 10 2014 Petr Pisar <ppisar@redhat.com> - 0.17-4
- Fix t/06-autorestart.t race (bug #1100158)

* Tue Jun 17 2014 Petr Pisar <ppisar@redhat.com> - 0.17-3
- Fix races in t/07-envdir.t test (bug #1100158)
- Load the environment directory just before restartin a server (bug #1100158)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Dec 30 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.17-1
- Upstream update.

* Sun Nov 24 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.16-1
- Upstream update.

* Tue Aug 27 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.15-1
- Upstream update.
- Minor spec cleanup.

* Fri Aug 16 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.14-1
- Upstream update.
- BR: perl(Test::TCP) >= 2.00.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 26 2013 Petr Pisar <ppisar@redhat.com> - 0.12-3
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Sep 26 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.12-1
- Upstream update.
- Modernize spec.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 19 2012 Petr Pisar <ppisar@redhat.com> - 0.11-6
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.11-4
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 24 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.11-2
- Add "Requires: perl-Server-Starter = %%{version}-%%{release}"
  per reviewer's demand.

* Thu Jan 20 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.11-1
- Upstream update.
- Reflect package review.

* Wed Dec 22 2010 Ralf Corsépius <corsepiu@fedoraproject.org> 0.09-2
- Put start_server into separate subpackage.

* Wed Dec 22 2010 Ralf Corsépius <corsepiu@fedoraproject.org> 0.09-1
- Initial Fedora package.
