Name:           perl-Alien-SDL
Version:        1.446
Release:        31%{?dist}
Summary:        Finding and using SDL binaries
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Alien-SDL
Source0:        https://cpan.metacpan.org/authors/id/F/FR/FROGGS/Alien-SDL-%{version}.tar.gz
# Do not set unnecessary rpath, not suitable for an upstream
Patch0:         Alien-SDL-1.446-Do-not-set-rpath-on-Linux.patch
# Place temporary files into a writable location,
# <https://github.com/PerlGameDev/SDL/issues/297>
Patch1:         Alien-SDL-1.446-Place-temporary-files-into-a-writable-location.patch
# Keep full-arch because Alien::SDL::ConfigData stores architecture-specific
# paths.
%global debug_package %{nil}
BuildRequires:  coreutils
BuildRequires:  freetype-devel
BuildRequires:  gcc
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Archive::Extract)
# Not needed (https://github.com/PerlGameDev/SDL/issues/234):
# Archive::Tar
# Archive::Zip
BuildRequires:  perl(base)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::Command)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Fetch) >= 0.24
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path) >= 2.08
BuildRequires:  perl(File::ShareDir) >= 1.00
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(Text::Patch) >= 1.4
BuildRequires:  perl(warnings)
BuildRequires:  sdl12-compat-devel
BuildRequires:  SDL_gfx-devel
BuildRequires:  SDL_image-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  SDL_Pango-devel
BuildRequires:  SDL_ttf-devel
# Run-time:
BuildRequires:  perl(Capture::Tiny)
# Data::Dumper not used at tests
# Tests only:
BuildRequires:  perl(Test::More)
Requires:       perl(Data::Dumper)
Requires:       perl(ExtUtils::CBuilder)
Requires:       perl(File::ShareDir) >= 1.00
Requires:       perl(Module::Build)
Requires:       sdl12-compat-devel
Suggests:       SDL_gfx-devel
Suggests:       SDL_image-devel
Suggests:       SDL_mixer-devel
Suggests:       SDL_Pango-devel
Suggests:       SDL_ttf-devel

%{?perl_default_filter}
%global __requires_exclude %__requires_exclude|^perl\\(File::ShareDir\\)$

%description
In short Alien::SDL can be used to detect and get configuration settings from 
an installed SDL and related libraries.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
# t/002_config.t checks that the optional files cached in
# Alien::SDL::config(ld_shared_libs) exist.
Requires:       SDL_gfx-devel
Requires:       SDL_image-devel
Requires:       SDL_mixer-devel
Requires:       SDL_Pango-devel
Requires:       SDL_ttf-devel

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%autosetup -p1 -n Alien-SDL-%{version}
rm t/release-pod-*
perl -i -ne 'print $_ unless m{\At/release-pod-}' MANIFEST

%build
perl Build.PL installdirs=vendor --travis
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}/*
# Move Alien::SDL::ConfigData to perl_vendorarch
install -d %{buildroot}%{perl_vendorarch}/Alien
mv %{buildroot}%{perl_vendorlib}/Alien/SDL %{buildroot}%{perl_vendorarch}/Alien
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test

%files
%license LICENSE
%doc Changes README TODO
%{perl_vendorarch}/*
%{perl_vendorlib}/*
%{_mandir}/man3/*
%{_bindir}/*

%files tests
%{_libexecdir}/%{name}

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.446-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.446-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.446-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.446-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.446-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.446-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.446-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.446-24
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.446-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.446-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 10 2021 Petr Pisar <ppisar@redhat.com> - 1.446-21
- Modernize a spec file
- Run-require SDL developmental package
- Alien::SDL::ConfigData is architecture-specific
- Specify all dependencies
- Do not set unnecessary rpath
- Package the tests

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.446-20
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.446-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.446-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.446-17
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.446-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.446-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.446-14
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.446-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.446-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.446-11
- Perl 5.28 rebuild

* Mon Feb 19 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.446-10
- Add build-require gcc

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.446-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.446-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.446-7
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.446-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.446-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.446-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.446-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.446-2
- Perl 5.22 rebuild

* Mon Feb 23 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.446-1
- 1.446 bump

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.444-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.444-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Petr Pisar <ppisar@redhat.com> - 1.444-1
- 1.444 bump

* Thu Apr 24 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.442-1
- 1.442 bump

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.440-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 23 2013 Petr Pisar <ppisar@redhat.com> - 1.440-2
- Perl 5.18 rebuild

* Wed Apr 17 2013 Petr Pisar <ppisar@redhat.com> - 1.440-1
- 1.440 bump

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.438-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Sep 10 2012 Jitka Plesnikova <jplesnik@redhat.com> - 1.438-1
- 1.438 bump

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.436-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 28 2012 Petr Pisar <ppisar@redhat.com> - 1.436-2
- Perl 5.16 rebuild

* Mon Jun 25 2012 Jitka Plesnikova <jplesnik@redhat.com> - 1.436-1
- 1.436 bump

* Sun Jun 17 2012 Petr Pisar <ppisar@redhat.com> - 1.434-2
- Perl 5.16 rebuild

* Thu Jun 07 2012 Petr Pisar <ppisar@redhat.com> - 1.434-1
- 1.434 bump

* Mon Jan 16 2012 Marcela Mašláňová <mmaslano@redhat.com> 1.430-1
- update to 1.430

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.428-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Aug 01 2011 Marcela Mašláňová <mmaslano@redhat.com> 1.428-1
- Specfile autogenerated by cpanspec 1.79.
