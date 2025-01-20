Name:           perl-Module-Metadata-Changes
Version:        2.12
Release:        25%{?dist}
Summary:        Manage a module's machine-readable Changes/CHANGES file
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Module-Metadata-Changes
Source0:        https://cpan.metacpan.org/authors/id/R/RS/RSAVAGE/Module-Metadata-Changes-%{version}.tgz
# Search templates and CSS in the system directories
Patch0:         Module-Metadata-Changes-2.06-Search-assets-in-system-directories.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  sed
BuildRequires:  web-assets-devel
# Run-time:
BuildRequires:  perl(Config::IniFiles) >= 2.88
# DateTime nowhere used
BuildRequires:  perl(DateTime::Format::HTTP) >= 0.42
BuildRequires:  perl(DateTime::Format::Strptime) >= 1.73
BuildRequires:  perl(DateTime::Format::W3CDTF) >= 0.06
BuildRequires:  perl(File::Slurper) >= 0.008
# Getopt::Long not used at tests
# Upstream requires bogus HTML::Entities::Interpolate 1.06 version,
# CPAN RT#109480
BuildRequires:  perl(HTML::Entities::Interpolate) >= 1.05
BuildRequires:  perl(HTML::Template) >= 2.95
BuildRequires:  perl(Moo) >= 2.000002
# Pod::Usage not used at tests
BuildRequires:  perl(strict)
BuildRequires:  perl(Try::Tiny) >= 0.24
BuildRequires:  perl(Types::Standard) >= 1.000005
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More) >= 1.001002
Requires:       perl(Config::IniFiles) >= 2.88
Requires:       perl(DateTime::Format::HTTP) >= 0.42
Requires:       perl(DateTime::Format::Strptime) >= 1.73
Requires:       perl(DateTime::Format::W3CDTF) >= 0.06
# Upstream requires bogus HTML::Entities::Interpolate 1.06 version,
# CPAN RT#109480
Requires:       perl(HTML::Entities::Interpolate) >= 1.05
Requires:       perl(HTML::Template) >= 2.95
Requires:       perl(File::Slurper) >= 0.008
Requires:       perl(Moo) >= 2.000002
Requires:       perl(Try::Tiny) >= 0.24
Requires:       perl(Types::Standard) >= 1.000005
Requires:       web-assets-filesystem

%{?perl_default_filter}

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Config::IniFiles|DateTime::Format::W3CDTF|File::Slurper|HTML::Entities::Interpolate|HTML::Template|Moo|Try::Tiny|Types::Standard)\\)$

%description
Module::Metadata::Changes is a pure Perl module. It allows you to convert
old-style Changes/CHANGES files, and to read and write Changelog.ini files.

%prep
%setup -q -n Module-Metadata-Changes-%{version}
%patch -P0 -p1
chmod -x scripts/report.names.pl
sed -i -e '1 s|^#!.*|%(perl -MConfig -e 'print $Config{startperl}')|' \
    bin/ini.report.pl scripts/report.names.pl

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

# Install templates
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/templates/module/metadata/changes
install -m 0644 \
    -t $RPM_BUILD_ROOT%{_datadir}/%{name}/templates/module/metadata/changes \
    htdocs/assets/templates/module/metadata/changes/*

# Install web assets
install -d $RPM_BUILD_ROOT%{_webassetdir}/%{name}/css/module/metadata/changes
install -m 0644 \
    -t $RPM_BUILD_ROOT%{_webassetdir}/%{name}/css/module/metadata/changes \
    htdocs/assets/css/module/metadata/changes/*

%check
make test

%files
%license LICENSE
# The Changelog.ini is an example for ini.report.pl tool
%doc Changelog.ini Changes README scripts
%{_bindir}/*
%{perl_vendorlib}/*
%{_datadir}/%{name}
%{_webassetdir}/%{name}
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Aug 06 2024 Miroslav Suchý <msuchy@redhat.com> - 2.12-24
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.12-17
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 22 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.12-14
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.12-11
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.12-8
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.12-5
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.12-2
- Perl 5.26 rebuild

* Tue Apr 18 2017 Petr Pisar <ppisar@redhat.com> - 2.12-1
- 2.12 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Sep 05 2016 Petr Pisar <ppisar@redhat.com> - 2.11-1
- 2.11 bump

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.10-2
- Perl 5.24 rebuild

* Fri May 06 2016 Petr Pisar <ppisar@redhat.com> - 2.10-1
- 2.10 bump

* Tue May 03 2016 Petr Pisar <ppisar@redhat.com> - 2.09-1
- 2.09 bump

* Mon May 02 2016 Petr Pisar <ppisar@redhat.com> - 2.08-1
- 2.08 bump
- License changed to (GPL+ or Artistic)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 23 2015 Petr Pisar <ppisar@redhat.com> - 2.06-1
- 2.06 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.05-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.05-2
- Perl 5.22 rebuild

* Thu Feb 19 2015 Petr Pisar <ppisar@redhat.com> 2.05-1
- Specfile autogenerated by cpanspec 1.78.
