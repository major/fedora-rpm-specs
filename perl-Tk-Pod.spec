%global use_x11_tests 1

Name:           perl-Tk-Pod
Version:        0.9943
Release:        21%{?dist}
Summary:        Pod browser top-level widget
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Tk-Pod
Source0:        https://cpan.metacpan.org/authors/id/S/SR/SREZIC/Tk-Pod-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Pod::Simple) >= 2.05
BuildRequires:  perl(Tk) >= 800.004
# Run-time:
# AnyDBM_File not used at tests
BuildRequires:  perl(base)
BuildRequires:  perl(Benchmark)
BuildRequires:  perl(blib)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Struct)
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
# Data::Dumper not used at tests
BuildRequires:  perl(Exporter)
# Fcntl not used at tests
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
# File::HomeDir never used
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Getopt::Long)
# I18N::Langinfo is optional
BuildRequires:  perl(IO::Socket)
# Module::Refresh not used at tests
# PerlIO::gzip is optional
# Pod::Functions not used at tests
BuildRequires:  perl(Pod::Simple) >= 2.05
BuildRequires:  perl(Pod::Simple::PullParser)
# Pod::Simple::PullParserEndToken not used at tests
# Pod::Simple::PullParserStartToken not used at tests
# Pod::Simple::PullParserTextToken not used at tests
# Pod::Simple::RTF is never used
# Pod::Simple::Text is never used
# Pod::Usage not used at tests
BuildRequires:  perl(POSIX)
# Proc::ProcessTable is optional
BuildRequires:  perl(Safe)
BuildRequires:  perl(Storable)
BuildRequires:  perl(strict)
# Text::English not used at tests
# Text::Wrap is never used
# Tk::App::Debug is optional
# Tk::App::Reloader is optional
BuildRequires:  perl(Tk::BrowseEntry)
# Tk::Compound is optional and not needed wih Tk >= 804
BuildRequires:  perl(Tk::Derived)
# Tk::DialogBox not used at tests
# Tk::FileSelect not used at tests
BuildRequires:  perl(Tk::Frame)
# Tk::HistEntry is optional
# Tk::HList is not needed wih Tk >= 800.024012
BuildRequires:  perl(Tk::ItemStyle)
BuildRequires:  perl(Tk::LabEntry)
# Tk::Listbox is not needed wih Tk >= 800.024012
BuildRequires:  perl(Tk::ROText)
# Tk::ToolBar is optional
BuildRequires:  perl(Tk::Toplevel)
BuildRequires:  perl(Tk::Tree)
BuildRequires:  perl(Tk::Widget)
# URI::Escape is optional
BuildRequires:  perl(vars)
# Win32 is never used
# Win32Util is never used
# Tests:
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Devel::Hide)
BuildRequires:  perl(ExtUtils::Command::MM)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
# Optional tests:
BuildRequires:  perl(Test)
#BuildRequires:  perl(Tk::HistEntry) >= 0.4
%if %{use_x11_tests}
# X11 tests:
BuildRequires:  xorg-x11-server-Xvfb
BuildRequires:  xorg-x11-xinit
BuildRequires:  font(:lang=en)
%endif
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Benchmark)
Requires:       perl(blib)
Requires:       perl(File::Temp)
Requires:       perl(Module::Refresh)
Requires:       perl(Pod::Functions)
Requires:       perl(Pod::Simple) >= 2.05
Requires:       perl(Pod::Simple::PullParserEndToken)
Requires:       perl(Pod::Simple::PullParserStartToken)
Requires:       perl(Pod::Simple::PullParserTextToken)
Requires:       perl(Pod::Usage)
Requires:       perl(POSIX)
Requires:       perl(Safe)
Requires:       perl(Storable)
Requires:       perl(Tk) >= 800.004
Requires:       perl(Tk::BrowseEntry)
Requires:       perl(Tk::DialogBox)
Requires:       perl(Tk::FileSelect)
Requires:       perl(Tk::LabEntry)
Requires:       perl(Tk::ROText)
Requires:       perl(Tk::Widget)
# URI::Escape is optional but usefull to escape URIs properly
Requires:       perl(URI::Escape)

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Tk(::Pod)?\\)\\s*$

%description
Simple Pod browser with hypertext capabilities in a Toplevel widget.

%prep
%setup -q -n Tk-Pod-%{version}
chmod -x Pod_usage.pod

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%if %{use_x11_tests}
    xvfb-run -a make test
%else
    make test
%endif

%files
%doc Changes README TODO
%{perl_vendorlib}/*
%{_bindir}/*
%{_mandir}/man3/*
%{_mandir}/man1/*

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9943-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.9943-20
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9943-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9943-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.9943-17
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9943-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9943-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.9943-14
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9943-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9943-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.9943-11
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9943-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9943-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.9943-8
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9943-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9943-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.9943-5
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9943-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.9943-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9943-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Petr Pisar <ppisar@redhat.com> - 0.9943-1
- 0.9943 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9942-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.9942-5
- Perl 5.22 rebuild

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.9942-4
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9942-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jan 27 2014 Petr Pisar <ppisar@redhat.com> - 0.9942-2
- Enable dependency on Text::English

* Tue Nov 19 2013 Petr Pisar <ppisar@redhat.com> - 0.9942-1
- 0.9942 bump

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9941-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 21 2013 Petr Pisar <ppisar@redhat.com> - 0.9941-3
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9941-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec 03 2012 Petr Pisar <ppisar@redhat.com> - 0.9941-1
- 0.9941 bump

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9940-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 13 2012 Petr Pisar <ppisar@redhat.com> - 0.9940-2
- Perl 5.16 rebuild

* Wed Mar 14 2012 Petr Pisar <ppisar@redhat.com> - 0.9940-1
- 0.9940 bump

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9939-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 21 2011 Petr Pisar <ppisar@redhat.com> 0.9939-1
- Specfile autogenerated by cpanspec 1.78.
- Remove BuildRoot and defattr from spec code
