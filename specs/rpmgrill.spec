Name:           rpmgrill
Version:        0.34
Release:        19%{?dist}
Summary:        A utility for catching problems in koji builds
License:        Artistic-2.0
Source0:        https://github.com/default-to-open/%{name}/archive/%{version}.tar.gz
URL:            https://github.com/default-to-open/rpmgrill
BuildArch:      noarch
Requires:       perl(Module::Pluggable)

# For the antivirus plugin
Requires: clamav
Requires: data(clamav)

# For checking desktop/icon files using /usr/bin/desktop-file-validate
Requires: /usr/bin/desktop-file-validate

# For LibGather, Rpath : need eu-readelf & associated tools
Requires: elfutils

# The SecurityPolicy plugin uses xsltproc to validate polkit files.
Requires: /usr/bin/xsltproc

# The SecurityPolicy plugin checks for vulnerabilities in Ruby gems;
# the database is cached locally using git.
Requires: git

# The SecurityPolicy plugin uses strings
Requires: binutils

# Not strictly necessary for rpmgrill, but rpmgrill-fetch-build uses it
# to download Fedora builds.
Requires: koji

# Test dependencies
BuildRequires:  perl(CGI)
BuildRequires:  perl(Digest::SHA1)
BuildRequires:  perl(File::LibMagic)
BuildRequires:  perl(File::Slurp)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(File::Copy::Recursive)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(IPC::Run)
BuildRequires:  perl(JSON::XS)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Pluggable)
BuildRequires:  perl(Net::DNS)
BuildRequires:  perl(Sort::Versions)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(Test::LongString)
BuildRequires:  perl(Test::MockModule)
BuildRequires:  perl(Test::MockObject)
BuildRequires:  perl(Test::Perl::Critic)
BuildRequires:  perl(Test::Simple)
BuildRequires:  perl(Time::ParseDate)
BuildRequires:  perl(Time::Piece)
BuildRequires:  perl(XML::Simple)
BuildRequires:  perl(YAML)
BuildRequires:  perl(YAML::Syck)
BuildRequires:  perl(boolean)
BuildRequires:  perl(open)
BuildRequires:  perl-generators
BuildRequires:  clamav
BuildRequires:  clamav-data
BuildRequires: /usr/bin/xsltproc
BuildRequires: /usr/bin/desktop-file-validate

%description
rpmgrill runs a series of tests against a set of RPMs, reporting problems
that may require a developer's attention.  For instance: unapplied patches,
multilib incompatibilities.

%prep
%setup -q -n %{name}-%{version}

%build
%{__perl} Build.PL --installdirs vendor
./Build

%install
./Build pure_install --destdir %{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;

%{_fixperms} %{buildroot}/*

%files
%doc README.asciidoc LICENSE AUTHORS
%{perl_vendorlib}/*
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_datadir}/%{name}/*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.34-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.34-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Apr 20 2024 Miroslav Suchý <msuchy@redhat.com> - 0.34-17
- convert license to SPDX

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.34-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.34-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.34-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.34-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.34-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.34-11
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.34-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.34-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.34-8
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.34-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.34-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.34-5
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.34-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.34-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.34-2
- Perl 5.30 rebuild

* Wed Apr 17 2019 Róman Joost <roman@bromeco.de> - 0.34-1
- Includes upstream pull request #27 contributed by Petr Pisar

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.33-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.33-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.33-2
- Perl 5.28 rebuild

* Mon Jun 04 2018 Róman Joost <rjoost@redhat.com> - 0.33-1
- Includes upstream pull requests #23, #24 contributed by Adam
  Williamson

* Thu May 24 2018 Adam Williamson <awilliam@redhat.com> - 0.32-4
- Require clamav itself again (0.32-2 inadvertently dropped the dep)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Feb 01 2018 Róman Joost <rjoost@redhat.com> - 0.32-2
- bz1520003 - Do not hard require clamav-data

* Fri Nov 03 2017 Róman Joost <rjoost@redhat.com> - 0.32-1
- Includes upstream pull request #22
  (https://github.com/default-to-open/rpmgrill/pull/22) based on a patch
  contributed by Colin Walters

* Tue Sep 05 2017 Róman Joost <rjoost@redhat.com> - 0.31-1
- bz1478470 - Full RELRO now checks new dtags
- bz1478387 - deprecate rpmgrill-unpack-rpms, rpmgrill-fetch-build commands

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.30-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.30-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 06 2017 Róman Joost <rjoost@redhat.com> 0.30-1
- bz1410050: fixes exception in use of experimental Perl feature

* Tue Jan 03 2017 Róman Joost <rjoost@redhat.com> 0.29-1
- bz1199960: fixes missing entries for armv7hl
- bz1202633: allow to specify subtests

* Tue Aug 23 2016 Róman Joost <rjoost@redhat.com> 0.28-2
- bz1356477: fixes missing runtime dependency for binutils

* Fri May 27 2016 Róman Joost <rjoost@redhat.com> 0.28-1
- bz1202634: fixes fetch-build has a hardcoded koji URL
- bz1213228: new test for suspicious PATH

* Wed Dec 10 2014 Ed Santiago <santiago@redhat.com> 0.27-1
- bz1172584: missing deps on Module::Pluggable, koji
- bz1160153: fill in rpmgrill POD
- new rpmgrill-analyze-local tool

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.26-3
- Perl 5.20 rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Oct 22 2013 Ed Santiago <santiago@redhat.com> 0.26-1
- bz1021298: Handle UnversionedDocdirs change in F20
- internal fixes for updated perl-Encode module

* Thu Sep 12 2013 Ed Santiago <santiago@redhat.com> 0.25-2
- Don't just include License file in tarball, package it.

* Wed Sep 11 2013 Ed Santiago <santiago@redhat.com> 0.25-1
- Manifest: include License file, missing selftests

* Mon Sep  9 2013 Ed Santiago <santiago@redhat.com> 0.24-1
- test suite: clamav output differs between f17 & f19
- specfile: fix bad date in changelog; re-update some Requires

* Tue Jul 23 2013 Ed Santiago <santiago@redhat.com> 0.23-1
- package missing RPM::Grill::Util module
- more review feedback; thanks again to Christopher Meng

* Mon Jul  8 2013 Ed Santiago <santiago@redhat.com> 0.22-2
- specfile: remove unnecessary BuildRoot definition

* Wed Jul  3 2013 Ed Santiago <santiago@redhat.com> 0.22-1
- incorporate Fedora review feedback; Thanks to Christopher Meng

* Wed Jul  3 2013 Ed Santiago <santiago@redhat.com> 0.21-1
- bz966075: ManPages test: deal with file in noarch, man pages in arch
