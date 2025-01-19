Name:           perl-File-Map
Version:        0.71
Release:        9%{?dist}
Summary:        Memory mapping made simple and safe
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/File-Map
Source0:        https://cpan.metacpan.org/authors/id/L/LE/LEONT/File-Map-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl-interpreter >= 0:5.008
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(PerlIO::Layers)
BuildRequires:  perl(Sub::Exporter::Progressive) >= 0.001005
BuildRequires:  perl(subs)
BuildRequires:  perl(XSLoader)
# Tests
BuildRequires:  perl(Config)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(open)
# Pod::Coverage::TrustPod 1.08 not used
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
# Test::Pod 1.41 not used
# Test::Pod::Coverage 1.08 not used
BuildRequires:  perl(Test::Warnings) >= 0.005
BuildRequires:  perl(threads)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(utf8)

%{?perl_default_filter}

%description
File::Map maps files or anonymous memory into perl variables.


%prep
%setup -q -n File-Map-%{version}
chmod -x examples/fastsearch.pl


%build
/usr/bin/perl Build.PL installdirs=vendor optimize="$RPM_OPT_FLAGS"
./Build


%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*


%check
./Build test


%files
%license LICENSE
%doc Changes examples README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/File*
%{_mandir}/man3/*


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.71-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Aug 06 2024 Miroslav Suchý <msuchy@redhat.com> - 0.71-8
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.71-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 11 2024 Jitka Plesnikova <jplesnik@redhat.com> - 0.71-6
- Perl 5.40 rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.71-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.71-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.71-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 0.71-2
- Perl 5.38 rebuild

* Sun Apr 16 2023 Emmanuel Seyman <emmanuel@seyman.fr> - 0.71-1
- Update to 0.71

* Sun Apr 02 2023 Emmanuel Seyman <emmanuel@seyman.fr> - 0.70-1
- Update to 0.70

* Sun Mar 26 2023 Emmanuel Seyman <emmanuel@seyman.fr> - 0.68-1
- Update to 0.68

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.67-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.67-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.67-8
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.67-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.67-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.67-5
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.67-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.67-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 29 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.67-2
- Perl 5.32 re-rebuild updated packages

* Sun Jun 28 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 0.67-1
- Replace %%{__perl} with /usr/bin/perl
- Update to 0.67

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.66-6
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.66-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.66-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.66-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.66-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Dec 23 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 0.66-1
- Update to 0.66

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.65-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.65-4
- Perl 5.28 rebuild

* Fri Mar 02 2018 Petr Pisar <ppisar@redhat.com> - 0.65-3
- Adapt to removing GCC from a build root (bug #1547165)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.65-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Nov 04 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 0.65-1
- Update to 0.65

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.64-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.64-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.64-5
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.64-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.64-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.64-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jul 23 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.64-1
- Update to 0.64

* Mon Jun 22 2015 Petr Pisar <ppisar@redhat.com> - 0.63-4
- Specify all dependencies (bug #1234359)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.63-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.63-2
- Perl 5.22 rebuild

* Sun Sep 14 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 0.63-1
- Update to 0.63

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.62-3
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.62-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Aug 17 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 0.62-1
- Update to 0.62
- Use %%license

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.61-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Oct 06 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 0.61-1
- Update to 0.61

* Wed Aug 14 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 0.60-1
- Update to 0.60

* Sat Aug 10 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 0.59-1
- Update to 0.59

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.57-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 27 2013 Petr Pisar <ppisar@redhat.com> - 0.57-2
- Perl 5.18 rebuild

* Sun May 26 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 0.57-1
- Update to 0.57

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.56-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Dec 23 2012 Emmanuel Seyman <emmanuel@seyman.fr> - 0.56-1
- Update to 0.56
- Remove the Group macro (no longer used)

* Sun Dec 16 2012 Emmanuel Seyman <emmanuel@seyman.fr> - 0.55-1
- Update to 0.55

* Sun Nov 11 2012 Emmanuel Seyman <emmanuel@seyman.fr> - 0.53-1
- Update to 0.53

* Sat Oct 06 2012 Emmanuel Seyman <emmanuel@seyman.fr> - 0.52-1
- Update to 0.52
- Clean up spec file

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.51-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 21 2012 Petr Pisar <ppisar@redhat.com> - 0.51-2
- Perl 5.16 rebuild

* Tue Jun 19 2012 Petr Pisar <ppisar@redhat.com> - 0.51-1
- 0.51 bump

* Thu Jun 14 2012 Petr Pisar <ppisar@redhat.com> - 0.31-8
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.31-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.31-6
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.31-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Nov 05 2010 Lubomir Rintel (GoodData) <lubo.rintel@gooddata.com> 0.31-4
- Fix a BR typo

* Wed Nov 03 2010 Lubomir Rintel (GoodData) <lubo.rintel@gooddata.com> 0.31-3
- Drop el5 secific patches
- Add more BuildRequires (Petr Pisar)

* Mon Oct 11 2010 Lubomir Rintel (GoodData) <lubo.rintel@gooddata.com> 0.31-2
- Fix build on el5

* Fri Oct 08 2010 Lubomir Rintel (GoodData) <lubo.rintel@gooddata.com> 0.31-1
- Fix POD
- Specfile autogenerated by cpanspec 1.78.
