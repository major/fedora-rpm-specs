%global cpan_version 0.997021

Name:           perl-App-cpm
Version:        0.997.021
Release:        2%{?dist}
Summary:        Fast CPAN module installer
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/App-cpm
Source0:        https://cpan.metacpan.org/authors/id/S/SK/SKAJI/App-cpm-%{cpan_version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(Module::Build::Tiny) >= 0.051
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
# None of them are used at tests.
# BuildRequires:  gzip
# BuildRequires:  perl(Archive::Tar)
# BuildRequires:  perl(Archive::Zip) >= 1.68
# BuildRequires:  perl(Carton::Snapshot)
# BuildRequires:  perl(Command::Runner) >= 0.100
# BuildRequires:  perl(Config)
# BuildRequires:  perl(constant)
# BuildRequires:  perl(CPAN::02Packages::Search) >= 0.100
# BuildRequires:  perl(CPAN::DistnameInfo)
# BuildRequires:  perl(CPAN::Meta)
# BuildRequires:  perl(CPAN::Meta::Prereqs)
# BuildRequires:  perl(CPAN::Meta::Requirements)
# BuildRequires:  perl(CPAN::Meta::YAML)
# BuildRequires:  perl(Cwd)
# BuildRequires:  perl(Digest::MD5)
# BuildRequires:  perl(Exporter)
# BuildRequires:  perl(ExtUtils::Install) >= 2.20
# BuildRequires:  perl(ExtUtils::InstallPaths) >= 0.002
# BuildRequires:  perl(File::Basename)
# BuildRequires:  perl(File::Copy)
# BuildRequires:  perl(File::Copy::Recursive)
# BuildRequires:  perl(File::HomeDir)
# BuildRequires:  perl(File::Path)
# BuildRequires:  perl(File::pushd)
# BuildRequires:  perl(File::Spec)
# BuildRequires:  perl(File::Temp)
# BuildRequires:  perl(File::Which)
# BuildRequires:  perl(Getopt::Long)
# BuildRequires:  perl(HTTP::Tinyish) >= 0.12
# BuildRequires:  perl(IO::Handle)
# BuildRequires:  perl(IPC::Run3)
# BuildRequires:  perl(JSON::PP) >= 2.27300
# BuildRequires:  perl(List::Util)
# BuildRequires:  perl(local::lib)
# BuildRequires:  perl(Menlo::Builder::Static)
# BuildRequires:  perl(Menlo::CLI::Compat) >= 1.9021
# BuildRequires:  perl(Module::CoreList)
# BuildRequires:  perl(Module::CPANfile)
# BuildRequires:  perl(Module::cpmfile) >= 0.001
# BuildRequires:  perl(Module::Metadata)
# BuildRequires:  perl(Parallel::Pipes::App) >= 0.100
# BuildRequires:  perl(parent)
# BuildRequires:  perl(Pod::Text)
# BuildRequires:  perl(POSIX)
# BuildRequires:  perl(Proc::ForkSafe) >= 0.001
# BuildRequires:  perl(Time::HiRes)
# BuildRequires:  perl(version)
# BuildRequires:  perl(YAML::PP) >= 0.026
# Tests only
BuildRequires:  perl(Test::More)
Requires:       gzip
Requires:       perl(Archive::Tar)
Requires:       perl(Archive::Zip) >= 1.68
Requires:       perl(Command::Runner) >= 0.100
Requires:       perl(ExtUtils::Install) >= 2.20
Requires:       perl(ExtUtils::InstallPaths) >= 0.002
Requires:       perl(File::HomeDir)
Requires:       perl(HTTP::Tinyish) >= 0.12
Requires:       perl(JSON::PP) >= 2.27300
Requires:       perl(local::lib)
Requires:       perl(Menlo::CLI::Compat) >= 1.9021
Requires:       perl(Module::CoreList)
Requires:       perl(Module::cpmfile) >= 0.001
Requires:       perl(Parallel::Pipes::App) >= 0.100
Requires:       perl(Parse::PMFile) >= 0.43
Requires:       perl(YAML::PP) >= 0.026
Suggests:       perl(Carton::Snapshot)

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(JSON::PP\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Command::Runner\\)$
%global __requires_exclude %__requires_exclude|^perl\\(ExtUtils::Install\\)$
%global __requires_exclude %__requires_exclude|^perl\\(ExtUtils::InstallPaths\\)$
%global __requires_exclude %__requires_exclude|^perl\\(HTTP::Tinyish\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Menlo::CLI::Compat\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Module::cpmfile\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Parallel::Pipes::App\\)$
%global __requires_exclude %__requires_exclude|^perl\\(YAML::PP\\)$

%description
cpm is a fast CPAN module installer, which uses Menlo::CLI::Compat in
parallel.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n App-cpm-%{cpan_version}
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1' "$F"
    chmod +x "$F"
done

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
find %{buildroot}%{_mandir} -type f -empty -delete
# Correct permissions
%{_fixperms} %{buildroot}/*

# Install tests
mkdir -p %{buildroot}/%{_libexecdir}/%{name}
cp -a t %{buildroot}/%{_libexecdir}/%{name}
cat > %{buildroot}/%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}/%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test

%files
%license LICENSE
%doc Changes
%{_bindir}/cpm
%dir %{perl_vendorlib}/App
%{perl_vendorlib}/App/cpm
%{perl_vendorlib}/App/cpm.pm
%{_mandir}/man1/cpm.*
%{_mandir}/man3/App::cpm.*
%{_mandir}/man3/App::cpm::*

%files tests
%{_libexecdir}/%{name}

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.997.021-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Dec 16 2024 Jitka Plesnikova <jplesnik@redhat.com> - 0.997.021-1
- 0.997021 bump (rhbz#2331685)

* Mon Nov 25 2024 Jitka Plesnikova <jplesnik@redhat.com> - 0.997.020-1
- 0.997020 bump (rhbz#2328540)

* Mon Nov 18 2024 Jitka Plesnikova <jplesnik@redhat.com> - 0.997.019-1
- 0.997019 bump (rhbz#2326667)

* Mon Sep 23 2024 Jitka Plesnikova <jplesnik@redhat.com> - 0.997.018-1
- 0.997018 bump (rhbz#2314192)

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.997.017-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon May 06 2024 Jitka Plesnikova <jplesnik@redhat.com> - 0.997.017-1
- 0.997017 bump (rhbz#2277638)

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.997.015-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.997.015-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 08 2024 Jitka Plesnikova <jplesnik@redhat.com> - 0.997.015-1
- 0.997015 bump (rhbz#2256825)

* Mon Aug 14 2023 Petr Pisar <ppisar@redhat.com> - 0.997.014-1
- 0.997014 bump

* Wed Aug 09 2023 Jitka Plesnikova <jplesnik@redhat.com> - 0.997.013-1
- 0.997013 bump (rhbz#2229332)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.997.012-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 17 2023 Jitka Plesnikova <jplesnik@redhat.com> - 0.997.012-1
- 0.997012 bump (rhbz#2221342)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.997.011-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.997.011-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.997.011-2
- Perl 5.36 rebuild

* Wed Apr 27 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.997.011-1
- 0.997011 bump

* Tue Apr 19 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.997.010-1
- 0.997010 bump

* Wed Mar 02 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.997.009-1
- 0.997009 bump

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.997.007-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Sep 24 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.997.007-1
- 0.997007 bump

* Tue Aug 03 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.997.006-1
- 0.997006 bump

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.997.004-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 14 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.997.004-1
- 0.997004 bump

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.997.003-2
- Perl 5.34 rebuild

* Wed Feb 24 2021 Petr Pisar <ppisar@redhat.com> - 0.997.003-1
- 0.997003 bump
- Package tests

* Tue Jan 26 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.997.002-1
- 0.997002 bump

* Fri Jan 08 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.997.000-1
- 0.997000 bump

* Mon Dec 07 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.996-1
- 0.996 bump

* Mon Nov 30 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.995-1
- 0.995 bump

* Mon Nov 09 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.994-1
- 0.994 bump

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.993-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.993-2
- Perl 5.32 rebuild

* Wed May 13 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.993-1
- 0.993 bump

* Mon May 11 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.992-1
- 0.992 bump

* Tue Apr 14 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.991-1
- 0.991 bump

* Fri Mar 27 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.990-1
- 0.990 bump

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.989-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 11 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.989-1
- 0.989 bump

* Fri Nov 01 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.988-1
- 0.988 bump

* Thu Oct 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.987-1
- 0.987 bump

* Mon Oct 14 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.986-1
- 0.986 bump

* Mon Sep 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.985-1
- 0.985 bump

* Fri Sep 27 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.984-1
- 0.984 bump

* Mon Aug 12 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.983-1
- 0.983 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.982-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 22 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.982-1
- 0.982 bump

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.980-2
- Perl 5.30 rebuild

* Fri Apr 26 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.980-1
- 0.980 bump

* Mon Mar 18 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.979-1
- 0.979 bump

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.978-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 02 2018 Petr Pisar <ppisar@redhat.com> - 0.978-2
- Do not package empty manual pages

* Thu Aug 02 2018 Petr Pisar <ppisar@redhat.com> - 0.978-1
- 0.978 bump
- Remove useless dependencies on Capture::Tiny and HTTP::Tiny
  (upstream bug #135)

* Mon Jul 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.977-1
- 0.977 bump

* Fri Jul 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.976-1
- 0.976 bump

* Mon Jul 16 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.975-1
- 0.975 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.974-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.974-2
- Perl 5.28 rebuild

* Wed May 02 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.974-1
- 0.974 bump

* Mon Apr 23 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.970-1
- 0.970 bump

* Fri Apr 20 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.965-1
- 0.965 bump

* Thu Apr 19 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.964-1
- 0.964 bump

* Mon Mar 26 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.963-1
- 0.963 bump

* Mon Mar 05 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.962-1
- 0.962 bump

* Mon Feb 26 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.960-1
- 0.960 bump

* Mon Feb 12 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.958-1
- 0.958 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.957-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Petr Pisar <ppisar@redhat.com> - 0.957-1
- 0.957 bump

* Mon Dec 11 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.955-1
- 0.955 bump

* Mon Oct 16 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.953-1
- 0.953 bump

* Tue Oct 10 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.951-1
- 0.951 bump

* Mon Oct 02 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.914-1
- 0.914 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.912-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 24 2017 Petr Pisar <ppisar@redhat.com> - 0.912-1
- 0.912 bump

* Mon Jul 17 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.911-1
- 0.911 bump

* Wed Jun 28 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.901-1
- 0.901 bump

* Mon Jun 26 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.900-1
- 0.900 bump

* Mon Jun 12 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.350-1
- 0.350 bump

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.304-2
- Perl 5.26 rebuild

* Tue May 30 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.304-1
- 0.304 bump

* Mon May 15 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.302-1
- 0.302 bump

* Fri Mar 24 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.301-1
- 0.301 bump

* Mon Mar 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.300-1
- 0.300 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.299-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 30 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.299-1
- 0.299 bump

* Mon Jan 16 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.298-1
- 0.298 bump

* Sun Jan 01 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.297-1
- 0.297 bump

* Wed Dec 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.294-1
- 0.294 bump

* Mon Dec 12 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.293-1
- 0.293 bump

* Wed Nov 09 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.214-1
- 0.214 bump

* Tue Nov 08 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.213-1
- 0.213 bump

* Thu Nov 03 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.212-1
- 0.212 bump

* Mon Oct 31 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.211-1
- 0.211 bump

* Mon Aug 08 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.118-1
- 0.118 bump

* Mon Jul 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.117-1
- 0.117 bump

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.116-2
- Perl 5.24 rebuild

* Mon May 16 2016 Petr Pisar <ppisar@redhat.com> - 0.116-1
- 0.116 bump

* Sun Feb 28 2016 Petr Šabata <contyk@redhat.com> - 0.115-1
- 0.115 bump

* Mon Feb 08 2016 Petr Šabata <contyk@redhat.com> - 0.114-1
- 0.114 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.113-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Petr Šabata <contyk@redhat.com> - 0.113-1
- 0.113 bump

* Mon Dec 21 2015 Petr Šabata <contyk@redhat.com> - 0.112-1
- 0.112 bump

* Tue Dec 08 2015 Petr Šabata <contyk@redhat.com> 0.111-1
- Initial packaging
