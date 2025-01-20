Name:           perl-Mojolicious-Plugin-AssetPack
Version:        2.15
Release:        2%{?dist}
Summary:        Compress and convert CSS, Less, Sass, JavaScript and CoffeeScript files
License:        Artistic-2.0

URL:            https://metacpan.org/release/Mojolicious-Plugin-AssetPack
Source0:        https://cpan.metacpan.org/authors/id/S/SR/SRI/Mojolicious-Plugin-AssetPack-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  sed
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(constant)
BuildRequires:  perl(CSS::Minifier::XS)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(Imager::File::PNG)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IPC::Run3)
BuildRequires:  perl(JavaScript::Minifier::XS)
BuildRequires:  perl(Mojo::Base)
BuildRequires:  perl(Mojo::ByteStream)
BuildRequires:  perl(Mojo::EventEmitter)
BuildRequires:  perl(Mojo::JSON)
BuildRequires:  perl(Mojolicious)
BuildRequires:  perl(Mojolicious::Lite)
BuildRequires:  perl(Mojolicious::Types)
BuildRequires:  perl(Mojolicious::Plugin)
BuildRequires:  perl(Mojo::UserAgent)
BuildRequires:  perl(Mojo::Util)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::Mojo)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(overload)
BuildRequires:  perl(warnings)
Requires:       perl(Imager::File::PNG)
Requires:       perl(Mojo::UserAgent)

%{?perl_default_filter}

%description
Mojolicious::Plugin::AssetPack is a Mojolicious plugin which can be used to
cram multiple assets of the same type into one file. This means that if you
have a lot of CSS files (.css, .less, .sass, ...) as input, the AssetPack
can make one big CSS file as output. This is good, since it will often
speed up the rendering of your page. The output file can even be minified,
meaning you can save bandwidth and browser parsing time.

%prep
%setup -q -n Mojolicious-Plugin-AssetPack-%{version}
for PL in not-found.pl sprites.pl rollup.pl; do
    /usr/bin/sed -i -e '1s,#!.*perl,#!/usr/bin/perl,' examples/"$PL"
done
/usr/bin/sed -i -e '1s,#!.*node,,' lib/Mojolicious/Plugin/AssetPack/Pipe/*.js

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%doc Changes examples README.md
%{perl_vendorlib}/Mojolicious*
%{_mandir}/man3/Mojolicious*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Dec 08 2024 Emmanuel Seyman <emmanuel@seyman.fr> - 2.15-1
- Update to 2.15

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Apr 20 2024 Miroslav Suchý <msuchy@redhat.com> - 2.14-6
- convert license to SPDX

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun May 07 2023 Emmanuel Seyman <emmanuel@seyman.fr> - 2.14-2
- Remove BuildRequire on coffee-script (#2186425)

* Sun Feb 05 2023 Emmanuel Seyman <emmanuel@seyman.fr> - 2.14-1
- Update to 2.14

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.13-5
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.13-2
- Perl 5.34 rebuild

* Sun Mar 21 2021 Emmanuel Seyman <emmanuel@seyman.fr> - 2.13-1
- Update to 2.13

* Sun Feb 21 2021 Emmanuel Seyman <emmanuel@seyman.fr> - 2.11-1
- Update to 2.11

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 13 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 2.10-1
- Update to 2.10
- Replace %%{__perl} with /usr/bin/perl
- Use %%{make_install} instead of "make pure_install"
- Use %%{make_build} instead of make
- Pass NO_PERLLOCAL to Makefile.PL

* Sun Oct 04 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 2.09-1
- Update to 2.09 (#1876287)
- Drop nodejs-less dependency, no longer in Fedora (#1884161)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.08-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.08-5
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.08-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.08-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.08-2
- Perl 5.30 rebuild

* Sun May 12 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 2.08-1
- Update to 2.08

* Sun May 05 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 2.07-1
- Update to 2.07

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Sep 09 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 2.06-1
- Update to 2.06

* Sun Aug 05 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 2.05-1
- Update to 2.05
- Remove no-longer-needed Obsoletes tag

* Sun Jul 29 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 2.04-1
- Update to 2.04

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.03-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.03-2
- Perl 5.28 rebuild

* Sun Apr 29 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 2.03-1
- Update to 2.03

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Feb 04 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 2.02-1
- Update to 2.02

* Sun Nov 12 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 2.01-1
- Update to 2.01

* Sat Nov 04 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 1.48-1
- Update to 1.48

* Sun Oct 15 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 1.47-1
- Update to 1.47

* Sun Oct 01 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 1.46-1
- Update to 1.46

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.45-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 25 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 1.45-1
- Update to 1.45

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.44-2
- Perl 5.26 rebuild

* Mon May 22 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 1.44-1
- Update to 1.44

* Sun May 14 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 1.43-1
- Update to 1.43

* Sun May 07 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 1.42-1
- Update to 1.42

* Sun Mar 19 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 1.41-1
- Update to 1.41

* Mon Feb 06 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 1.40-1
- Update to 1.40

* Sun Jan 29 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 1.39-1
- Update to 1.39

* Tue Jan 24 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 1.38-1
- Update to 1.38

* Sun Jan 08 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 1.31-1
- Update to 1.31

* Sun Dec 25 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 1.30-1
- Update to 1.30

* Sun Nov 27 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 1.28-1
- Update to 1.28

* Sun Nov 20 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 1.27-1
- Update to 1.27

* Mon Oct 31 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 1.25-1
- Update to 1.25

* Sun Sep 18 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 1.24-1
- Update to 1.24

* Sat Sep 03 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 1.22-1
- Update to 1.22

* Fri Aug 26 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 1.20-1
- Update to 1.20

* Sun Aug 14 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 1.19-1
- Update to 1.19

* Sun Aug 07 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 1.18-1
- Update to 1.18

* Sat Jul 23 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 1.17-1
- Update to 1.17

* Sat Jul 16 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 1.16-1
- Update to 1.16

* Mon Jun 27 2016 Adam Williamson <awilliam@redhat.com> - 1.15-1
- bump to latest upstream release (backwards incompatible)
- obsolete now-deprecated (i.e. broken) Bootstrap3 module

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.69-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.69-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Dec 06 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.69-1
- Update to 0.69

* Tue Sep 29 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.68-2
- Take into account review comments (#1267036)

* Mon Sep 28 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.68-1
- Update to 0.68

* Fri Sep 25 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.64-1
- Update to 0.64

* Tue Aug 25 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.61-1
- Update to 0.61

* Sun Aug 16 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.58-1
- Specfile autogenerated by cpanspec 1.78.
