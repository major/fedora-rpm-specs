%define upstream_name    Games-Solitaire-Verify

Name:       perl-%{upstream_name}
Version:    0.2601
Release:    2%{?dist}

Summary:    Process and verify solitaire games
License:    MIT
Url:        https://metacpan.org/release/%{upstream_name}
Source0:    https://www.cpan.org/modules/by-module/Games/%{upstream_name}-%{version}.tar.gz

BuildRequires: findutils
BuildRequires: perl-generators
BuildRequires: perl-interpreter
BuildRequires: perl(Carp)
BuildRequires: perl(Class::XSAccessor)
BuildRequires: perl(Data::Dumper)
BuildRequires: perl(Dir::Manifest)
BuildRequires: perl(Exception::Class)
BuildRequires: perl(File::Spec)
BuildRequires: perl(Getopt::Long)
BuildRequires: perl(IO::Handle)
BuildRequires: perl(IPC::Open3)
BuildRequires: perl(List::Util)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Path::Tiny)
BuildRequires: perl(Pod::Usage)
BuildRequires: perl(POSIX)
BuildRequires: perl(Test::Differences)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Trap)
BuildRequires: perl(autodie)
BuildRequires: perl(blib)
BuildRequires: perl(parent)
BuildRequires: perl(strict)
BuildRequires: perl(warnings)
BuildArch:  noarch

%description
This is a CPAN Perl module that verifies the solutions of various variants
of card Solitaire. It does not aim to try to be a solver for them, because
this is too CPU intensive to be adequately done using perl5 (as of
perl-5.10.0). If you're interested in the latter, look at:

* https://fc-solve.shlomifish.org/

* https://fc-solve.shlomifish.org/links.html#other_solvers

%prep
%setup -q -n %{upstream_name}-%{version}

%build
%__perl Build.PL --installdirs=vendor

./Build CFLAGS="%{optflags}"

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
chmod 755 %{buildroot}/%{_bindir}/*

%files
%license COPYING LICENSE
%doc Changes README examples
%{_bindir}/expand-solitaire-multi-card-moves
%{_bindir}/verify-solitaire-solution
%{_mandir}/man1/*
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2601-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Dec 05 2024 Shlomi Fish <shlomif@shlomifish.org> 0.2601-1
- New upstream version

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2600-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Apr 06 2024 Shlomi Fish <shlomif@cpan.org> 0.2600-1
- New upstream version

* Wed Jan 31 2024 Shlomi Fish <shlomif@cpan.org> 0.2500-1
- New upstream version

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2403-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2403-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2403-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2403-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2403-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.2403-8
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2403-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2403-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.2403-5
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2403-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2403-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.2403-2
- Perl 5.32 rebuild

* Wed Apr 22 2020 Shlomi Fish <shlomif@cpan.org> - 0.2303-1
- New upstream version

* Fri Mar 20 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.2300-1
- Add perl(blib) for tests

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2202-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2202-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.2201-2
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1900-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 05 2018 Shlomi Fish <shlomif@cpan.org> 0.1900-1
- Forked from the Mageia package and adapted for Fedora
