Name:           perl-Tk-Getopt
Version:        0.51
Release:        18%{?dist}
Summary:        User configuration window for Tk with interface to Getopt::Long
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Tk-Getopt
Source0:        https://cpan.metacpan.org/authors/id/S/SR/SREZIC/Tk-Getopt-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Safe)
BuildRequires:  perl(Tk) >= 804
# Optional      perl(Tk::Balloon)
BuildRequires:  perl(Tk::BrowseEntry)
BuildRequires:  perl(Tk::CmdLine)
# Optional fall back  perl(Tk::DirSelect)
BuildRequires:  perl(Tk::DirTree)
# Optional  perl(Tk::FileDialog) is old and buggy. Tk::FileSelect is fall-back
BuildRequires:  perl(Tk::FileSelect)
BuildRequires:  perl(Tk::Font)
# Optional not yet packaged  perl(Tk::FontDialog)
# Optional      perl(Tk::NoteBook)
BuildRequires:  perl(Tk::Optionmenu)
# Optional not yet packaged  perl(Tk::PathEntry)
BuildRequires:  perl(Tk::Photo)
BuildRequires:  perl(Tk::Pixmap)
BuildRequires:  perl(Tk::Tiler)
# Tests
BuildRequires:  perl(Test::More)
# Optional tests
BuildRequires:  perl(File::Temp)
# Optional not yet packaged  perl(Tk::Dial)
Requires:       perl(Cwd)
Requires:       perl(Data::Dumper)
Requires:       perl(File::Basename)
Requires:       perl(File::Spec)
Requires:       perl(Getopt::Long)
Requires:       perl(Safe)
Requires:       perl(Tk) >= 804
# Optional      perl(Tk::Balloon)
Requires:       perl(Tk::BrowseEntry)
Requires:       perl(Tk::CmdLine)
# Optional fall back  perl(Tk::DirSelect)
Requires:       perl(Tk::DirTree)
# Optional  perl(Tk::FileDialog) is old and buggy. Tk::FileSelect is fall-back
Requires:       perl(Tk::FileSelect)
Requires:       perl(Tk::Font)
# Optional not yet packaged  perl(Tk::FontDialog)
# Optional      perl(Tk::NoteBook)
Requires:       perl(Tk::Optionmenu)
# Optional not yet packaged  perl(Tk::PathEntry)
Requires:       perl(Tk::Photo)
Requires:       perl(Tk::Pixmap)
Requires:       perl(Tk::Tiler)

# Filter optional not yet packaged  perl(Tk::PathEntry)
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Tk::PathEntry\\)

%description
Tk::Getopt provides an interface to access command line options via
Getopt::Long and editing with a graphical user interface via a Tk window.

%prep
%setup -q -n Tk-Getopt-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes demos README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.51-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.51-17
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.51-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.51-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.51-14
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.51-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.51-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.51-11
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.51-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.51-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.51-8
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.51-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.51-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.51-5
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.51-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.51-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.51-2
- Perl 5.26 rebuild

* Mon Apr 24 2017 Petr Pisar <ppisar@redhat.com> - 0.51-1
- 0.51 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.50-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.50-13
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.50-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 23 2015 Petr Pisar <ppisar@redhat.com> - 0.50-11
- Correct dependency filter
- Specify all dependencies

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.50-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.50-9
- Perl 5.22 rebuild

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.50-8
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.50-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.50-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 0.50-5
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.50-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.50-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 0.50-2
- Perl 5.16 rebuild

* Wed Feb 22 2012 Petr Pisar <ppisar@redhat.com> 0.50-1
- Specfile autogenerated by cpanspec 1.78.
