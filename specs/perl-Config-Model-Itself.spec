Name:           perl-Config-Model-Itself
Version:        2.023
Release:        10%{?dist}
Summary:        Model editor for Config::Model
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://metacpan.org/release/Config-Model-Itself
Source0:        https://cpan.metacpan.org/authors/id/D/DD/DDUMONT/Config-Model-Itself-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  bash-completion
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(App::Cmd::Tester)
BuildRequires:  perl(App::Cme) >= 1.002
BuildRequires:  perl(App::Cme::Common)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config::Model) >= 2.142
BuildRequires:  perl(Config::Model::Tester::Setup)
BuildRequires:  perl(Config::Model::TkUI) >= 1.370
BuildRequires:  perl(Config::Model::Value)
BuildRequires:  perl(Data::Compare)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::testlib)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy::Recursive)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(lib)
BuildRequires:  perl(Log::Log4perl) >= 1.11
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Mouse)
BuildRequires:  perl(Mouse::Util::TypeConstraints)
BuildRequires:  perl(Path::Tiny) >= 0.062
BuildRequires:  perl(Pod::POM)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::File::Contents)
BuildRequires:  perl(Test::Memory::Cycle)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Text::Diff)
BuildRequires:  perl(Tk)
BuildRequires:  perl(warnings)
BuildRequires:  perl(YAML::XS)
BuildRequires:  sed
Requires:       bash-completion
Requires:       perl(App::Cme) >= 1.002
Requires:       perl(Config::Model::TkUI) >= 1.370

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Config::Model\\)\s*$
%global __requires_exclude %__requires_exclude|^perl\\(Config::Model\\) >= 2.064\s*$
%global __requires_exclude %__requires_exclude|^perl\\(Config::Model::TkUI\\)\s*$
%global __requires_exclude %__requires_exclude|^perl\\(Log::Log4perl\\)\s*$
%global __requires_exclude %__requires_exclude|^perl\\(App::Cme\\)\s*$

%description
Config::Itself module and its model files provide a model of Config:Model
(hence the Itself name).

%prep
%setup -q -n Config-Model-Itself-%{version}

%build
/usr/bin/perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

# Install bash_completion script
install -D -m 0644 contrib/bash_completion.cme_meta %{buildroot}%{_sysconfdir}/bash_completion.d/cme_meta

%check
./Build test

%files
%license LICENSE
%doc Changes CONTRIBUTING.md data README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*
%config(noreplace) %{_sysconfdir}/bash_completion.d/cme_meta

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.023-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 2.023-9
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.023-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.023-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.023-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.023-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.023-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.023-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.023-2
- Perl 5.36 rebuild

* Thu Apr 28 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.023-1
- 2.023 bump

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.022-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.022-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 22 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.022-3
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.022-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.022-1
- Update to 2.022

* Sun Jan 17 2021 Emmanuel Seyman <emmanuel@seyman.fr> - 2.021-1
- Update to 2.021

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.020-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.020-3
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.020-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec 29 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 2.020-1
- Update to 2.020

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.018-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.018-2
- Perl 5.30 rebuild

* Tue May 28 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.018-1
- 2.018 bump

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.016-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 19 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.016-1
* 2.016 bump

* Tue Aug 07 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.014-1
- 2.014 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.013-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.013-3
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.013-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov 21 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.013-1
- 2.013 bump

* Sun Oct 01 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 2.012-1
- Update to 2.012

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.011-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 13 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.011-1
- 2.011 bump

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.010-2
- Perl 5.26 rebuild

* Mon May 22 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 2.010-1
- Update to 2.010

* Sun May 07 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 2.009-1
- Update to 2.009

* Sun Mar 19 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 2.008-1
- Update to 2.008
- Properly mark /etc/bash_completion.d/cme_meta as a config file

* Thu Mar 09 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 2.007-1
- Update to 2.007

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.006-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Sep 29 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.006-1
- 2.006 bump

* Tue Aug 23 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.005-1
- 2.005 bump

* Mon May 23 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.004-1
- 2.004 bump

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.003-2
- Perl 5.24 rebuild

* Tue Mar 01 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.003-1
- 2.003 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.002-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.002-1
- 2.002 bump

* Mon Jul 20 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.245-1
- 1.245 bump
- Modernize spec

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.227-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.227-9
- Perl 5.22 rebuild

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.227-8
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.227-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Aug 05 2013 Petr Pisar <ppisar@redhat.com> - 1.227-6
- Perl 5.18 rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.227-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.227-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.227-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jul 01 2012 Petr Pisar <ppisar@redhat.com> - 1.227-2
- Perl 5.16 rebuild

* Sat Nov 26 2011 David Hannequin david.hannequin@gmail.com 1.227-1
- Updated to a new upstream version.

* Fri Mar 04 2011 David Hannequin david.hannequin@gmail.com 1.222-1
- Updated to a new upstream version.

* Mon Oct 04 2010 David Hannequin david.hannequin@gmail.com 1.218-1
- Updated to a new upstream version.

* Fri Jun 25 2010 David Hannequin david.hannequin@gmail.com 1.215-2
- Add missing build require

* Sun Jun 20 2010 David Hannequin david.hannequin@gmail.com 1.215-1
- Updated to a new upstream version.

* Sun Aug 02 2009 David Hannequin david.hannequin@gmail.com 1.211-1
- First Release 
