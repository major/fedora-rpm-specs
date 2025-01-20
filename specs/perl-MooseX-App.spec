%global cpan_version 1.43

Name:           perl-MooseX-App
# Keep 2-digit precision
Version:        %(echo '%{cpan_version}' | sed 's/\(\...\)\(.\)/\1.\2/')
Release:        5%{?dist}
Summary:        Write user-friendly command line apps with even less suffering
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MooseX-App
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MAROS/MooseX-App-%{cpan_version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(base)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(ExtUtils::MM_Unix)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Config::Any)
BuildRequires:  perl(Encode)
BuildRequires:  perl(File::HomeDir)
BuildRequires:  perl(I18N::Langinfo)
BuildRequires:  perl(if)
BuildRequires:  perl(IO::Interactive)
BuildRequires:  perl(List::Util) >= 1.44
BuildRequires:  perl(Module::Pluggable::Object)
BuildRequires:  perl(Moose) >= 2.00
BuildRequires:  perl(Moose::Exporter)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(MooseX::Types::Path::Class)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(overload)
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(Pod::Elemental)
BuildRequires:  perl(Pod::Elemental::Selectors)
BuildRequires:  perl(Pod::Elemental::Transformer::Nester)
BuildRequires:  perl(Pod::Elemental::Transformer::Pod5)
BuildRequires:  perl(Pod::Perldoc)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Term::ANSIColor)
BuildRequires:  perl(Term::ReadKey)
BuildRequires:  perl(Text::WagnerFischer)
BuildRequires:  perl(utf8)
# Tests only
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(lib)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Most)
BuildRequires:  perl(Test::NoWarnings)
Requires:       perl(I18N::Langinfo)
Requires:       perl(Moose) >= 2.00

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Moose\\)$

%description
MooseX-App is a highly customisable helper to write user-friendly command
line applications without having to worry about most of the annoying things
usually involved. Just take any existing Moose class, add a single line
(use MooseX-App qw(PluginA PluginB ...);) and create one class for each
command in an underlying namespace. Options and positional parameters can
be defined as simple Moose accessors.

%prep
%autosetup -p1 -n MooseX-App-%{cpan_version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
unset APP_DEVELOPER
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
%{make_build} test

%files
%license LICENSE
%doc Changes README.md TODO
%dir %{perl_vendorlib}/MooseX
%{perl_vendorlib}/MooseX/App
%{perl_vendorlib}/MooseX/App.pm
%{_mandir}/man3/MooseX::App.*
%{_mandir}/man3/MooseX::App::*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.43-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.43-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.43-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.43-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Oct 29 2023 Emmanuel Seyman <emmanuel@seyman.fr> - 1.43-1
- Update to 1.43
- Drop upstreamed patch
- Use LICENSE file instead of LICENCE

* Tue Aug 08 2023 Petr Pisar <ppisar@redhat.com> - 1.42-7
- Adapt to Perl 5.38.0 (bug #2223530)
- Convert a license tag to SPDX

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.42-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.42-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.42-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.42-3
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.42-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Aug 29 2021 Emmanuel Seyman <emmanuel@seyman.fr> - 1.42-1
- Update to 1.42
- Remove upsteamed patch

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.41-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 22 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.41-10
- Perl 5.34 rebuild

* Sun Feb 28 2021 Emmanuel Seyman <emmanuel@seyman.fr> - 1.41-9
- Patch and re-enable failing test (#1914227)
- Use %%{make_install} instead of "make pure_install"
- Use %%{make_build} instead of make
- Pass NO_PERLLOCAL to Makefile.PL

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.41-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 11 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.41-7
- Temporary remove the failing test

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.41-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.41-5
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.41-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.41-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.41-2
- Perl 5.30 rebuild

* Sun May 19 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 1.41-1
- Update to 1.41

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.39-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.39-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.39-3
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.39-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Sep 24 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 1.39-1
- Update to 1.39

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.38-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.38-2
- Perl 5.26 rebuild

* Tue May 23 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.38-1
- Update 1.38

* Mon Mar 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.37.01-1
- Update to 1.3701

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.37-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Nov 20 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 1.37-1
- Update to 1.37

* Sun Oct 16 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 1.36-1
- Update to 1.36

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.35-2
- Perl 5.24 rebuild

* Tue Apr 05 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 1.35-1
- Update to 1.35

* Mon Feb 22 2016 Petr Šabata <contyk@redhat.com> - 1.34-1
- 1.34 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.33-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.33-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.33-2
- Perl 5.22 rebuild

* Tue Apr 21 2015 Petr Šabata <contyk@redhat.com> - 1.33-1
- 1.33 bump

* Sun Mar 22 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 1.32-1
- Update to 1.32

* Tue Feb 10 2015 Petr Šabata <contyk@redhat.com> - 1.31-1
- 1.31 bump

* Tue Dec 02 2014 Petr Šabata <contyk@redhat.com> - 1.30-2
- Fix build issues pointed out in the review

* Thu Nov 27 2014 Petr Šabata <contyk@redhat.com> 1.30-1
- Initial packaging
