%global pkgname Text-Xslate

Name:           perl-%{pkgname}
Version:        3.5.9
Release:        12%{?dist}
Summary:        Scalable template engine
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            http://xslate.org/
Source0:        https://cpan.metacpan.org/authors/id/S/SK/SKAJI/%{pkgname}-v%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(base)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Module::Build) >= 0.4005
BuildRequires:  perl(Module::Build::XSUtil)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(B)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Data::MessagePack) >= 0.38
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Encode) >= 2.26
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Path) >= 2.07
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Mouse) >= 2.5.0
BuildRequires:  perl(Mouse::Role)
BuildRequires:  perl(Mouse::Util::TypeConstraints)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent) >= 0.221
BuildRequires:  perl(Scalar::Util) >= 1.14
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(version)
BuildRequires:  perl(XSLoader) >= 0.02
# Tests:
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Data::Section::Simple)
BuildRequires:  perl(Devel::StackTrace) >= 1.30
BuildRequires:  perl(Fatal)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Copy::Recursive)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::stat)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(if)
BuildRequires:  perl(lib)
BuildRequires:  perl(Plack) >= 0.99
BuildRequires:  perl(Plack::Builder)
BuildRequires:  perl(Plack::Response)
BuildRequires:  perl(Plack::Test)
BuildRequires:  perl(SelectSaver)
# Template not used
BuildRequires:  perl(Template::Plugin::Math)
BuildRequires:  perl(Template::Plugin::String)
BuildRequires:  perl(Test::LeakTrace)
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(threads)
BuildRequires:  perl(Tie::Array)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Time::localtime)
BuildRequires:  perl(utf8)
Requires:       perl(B)
Requires:       perl(Data::Dumper)
Requires:       perl(Data::MessagePack) >= 0.38
Requires:       perl(Digest::MD5)
Requires:       perl(Encode) >= 2.26
Requires:       perl(File::Path)
Requires:       perl(Mouse) >= 2.5.0
Requires:       perl(parent) >= 0.221
Requires:       perl(Scalar::Util) >= 1.14
Requires:       perl(XSLoader) >= 0.02

# Filter under-specified Symbols
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Data::MessagePack|Mouse|parent|Scalar::Util)\\)$
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(Text::Xslate\\)$

%description
Xslate is a template engine, tuned for persistent applications, safe as an
HTML generator, and with rich features.

%prep
%setup -qn %{pkgname}-v%{version}

%build
perl Build.PL --installdirs=vendor --optimize="%{optflags}"
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%license LICENSE
%doc Changes example HACKING
%{_bindir}/xslate
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Text*
%{_mandir}/man1/xslate.1*
%{_mandir}/man3/*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 11 2024 Jitka Plesnikova <jplesnik@redhat.com> - 3.5.9-10
- Perl 5.40 rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 3.5.9-6
- Perl 5.38 rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 3.5.9-3
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Nov 01 2021 Jitka Plesnikova <jplesnik@redhat.com> - 3.5.9-1
- 3.5.9 bump

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 22 2021 Jitka Plesnikova <jplesnik@redhat.com> - 3.5.8-5
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 3.5.8-2
- Perl 5.32 rebuild

* Tue Jun 02 2020 Jitka Plesnikova <jplesnik@redhat.com> - 3.5.8-1
- 3.5.8 bump

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 26 2019 Jitka Plesnikova <jplesnik@redhat.com> - 3.5.7-1
- 3.5.7 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 3.5.6-6
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.5.6-3
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.5.6-1
- 3.5.6 bump

* Fri Jan 05 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.5.5-1
- 3.5.5 bump

* Wed Dec 20 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.5.4-1
- 3.5.4 bump

* Tue Dec 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.5.3-1
- 3.5.3 bump

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.4.0-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 20 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.4.0-1
- 3.4.0 bump

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 3.3.9-2
- Perl 5.24 rebuild

* Mon Feb 29 2016 Jitka Plesnikova <jplesnik@redhat.com> - 3.3.9-1
- 3.3.9 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 09 2015 Jitka Plesnikova <jplesnik@redhat.com> - 3.3.7-1
- 3.3.7 bump

* Fri Jun 26 2015 Petr Pisar <ppisar@redhat.com> - 3.3.4-1
- 3.3.4 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 3.2.5-5
- Perl 5.22 rebuild

* Tue Dec 02 2014 Petr Pisar <ppisar@redhat.com> - 3.2.5-4
- Build-require Devel::PPPort (bug #1169661)

* Tue Sep 02 2014 Jitka Plesnikova <jplesnik@redhat.com> - 3.2.5-3
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 16 2014 Christopher Meng <rpm@cicku.me> - 3.2.5-1
- Update to 3.2.5

* Tue Jul 01 2014 Christopher Meng <rpm@cicku.me> - 3.2.4-1
- Update to 3.2.4

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Feb 20 2014 Christopher Meng <rpm@cicku.me> - 3.1.2-2
- Satisfy the test section.

* Thu Feb 20 2014 Christopher Meng <rpm@cicku.me> - 3.1.2-1
- Update to 3.1.2

* Fri Jan 24 2014 Christopher Meng <rpm@cicku.me> - 3.1.1-1
- Update to 3.1.1
- Remove unneeded requires.

* Tue Nov 26 2013 Christopher Meng <rpm@cicku.me> - 3.1.0-1
- Update to 3.1.0

* Tue Jul 23 2013 Christopher Meng <rpm@cicku.me> - 2.0009-1
- New version.
- BRs/Rs fix.

* Mon Jul 15 2013 Christopher Meng <rpm@cicku.me> - 2.0007-2
- SPEC cleanup.

* Fri Jun 21 2013 Christopher Meng <rpm@cicku.me> - 2.0007-1
- Initial Package.
