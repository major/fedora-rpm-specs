# If the emacs-el package has installed a pkgconfig file, use that to determine
# install locations and Emacs version at build time, otherwise set defaults.
%if %($(pkg-config emacs) ; echo $?)
%global emacs_version 22.1
%global emacs_lispdir  %{_datadir}/emacs/site-lisp
%global emacs_startdir %{_datadir}/emacs/site-lisp/site-start.d
%else
%global emacs_version  %{expand:%(pkg-config emacs --modversion)}
%global emacs_lispdir  %{expand:%(pkg-config emacs --variable sitepkglispdir)}
%global emacs_startdir %{expand:%(pkg-config emacs --variable sitestartdir)}
%endif

Name:           perl-SystemC-Vregs
Version:        1.470
Release:        30%{?dist}
Summary:        Utility routines used by vregs

License:        LGPLv3+ or Artistic 2.0
URL:            https://metacpan.org/release/SystemC-Vregs
Source0:        https://cpan.metacpan.org/authors/id/W/WS/WSNYDER/SystemC-Vregs-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  readline-devel
# Tests are disabled
# Run-time:
# perl(base)
# perl(Bit::Vector)
# perl(Bit::Vector::Overload)
# perl(Data::Dumper)
# File::Basename
# FindBin
# perl(Getopt::Long)
# perl(HTML::Entities)
# perl(HTML::TableExtract)
# perl(IO::File)
# perl(lib)
# perl(Pod::Usage)
# strict
# vars
# perl(Verilog::Language) >= 2.1
# warnings
# Tests:
# Config
# ExtUtils::Manifest
# perl(Test)

Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Verilog::Language) >= 2.1

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Verilog::Language\\)$

%description
A Vregs object contains a documentation "package" containing enumerations,
definitions, classes, and registers.


%package -n     emacs-vregs-mode
Summary:        Elisp source files for systemc-vregs under GNU Emacs
BuildRequires:  emacs-el
BuildRequires:  emacs
Requires:       emacs(bin) >= %{emacs_version}

%description -n emacs-vregs-mode
This package provides emacs support for systemc-vregs

%prep
%setup -q -n SystemC-Vregs-%{version}

# fixing error: ‘strchr’ was not declared in this scope
perl -pi -e 's|#include <stdlib.h>|#include <stdlib.h>\n#include <string.h>|' \
  include/VregsRegInfo.cpp


%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" \
    NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete

emacs -batch -f batch-byte-compile vregs-mode.el
install -d %{buildroot}%{emacs_lispdir}
install -pm 0644 vregs-mode.el vregs-mode.elc %{buildroot}%{emacs_lispdir}/

%{_fixperms} %{buildroot}/*

%check
# make test

%files
%license COPYING
%doc Changes README vregs_spec.doc vregs_spec.htm
%{_bindir}/vreg*

%dir %{perl_vendorlib}/SystemC
%{perl_vendorlib}/SystemC/Vregs.pm
%{perl_vendorlib}/SystemC/vregs_spec__rules.pl

%dir %{perl_vendorlib}/SystemC/Vregs
%{perl_vendorlib}/SystemC/Vregs/*
%{_mandir}/man?/*

%files -n emacs-vregs-mode
%license COPYING
%{emacs_lispdir}/vregs-mode.el*

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.470-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.470-29
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.470-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.470-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.470-26
- Perl 5.34 rebuild

* Fri May 14 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.470-25
- Modernize spec

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.470-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.470-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.470-22
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.470-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.470-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.470-19
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.470-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.470-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.470-16
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.470-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.470-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.470-13
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.470-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.470-11
- Perl 5.24 rebuild

* Tue Feb 02 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.470-10
- Replace %%define by %%global

* Fri Oct 23 2015 Petr Pisar <ppisar@redhat.com> - 1.470-9
- Correct dependency filter
- Specify all dependencies
- Package COPYING as a license

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.470-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.470-7
- Perl 5.22 rebuild

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.470-6
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.470-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.470-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 25 2013 Petr Pisar <ppisar@redhat.com> - 1.470-3
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.470-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Oct 17 2012 Shakthi Kannan <shakthimaan@fedoraproject.org> - 1.470-1
- Updated to upstream 1.470

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.463-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 27 2012 Petr Pisar <ppisar@redhat.com> - 1.463-9
- Perl 5.16 rebuild
- Specify all dependencies

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.463-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 1.463-7
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.463-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 22 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.463-5
- 661697 rebuild for fixing problems with vendorach/lib

* Thu May 06 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.463-4
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.463-3
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.463-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu May 21 2009 Chitlesh GOORAH <chitlesh [AT] fedoraproject DOT org> 1.463-1
- new upstream release

* Wed Mar 04 2009 Chitlesh GOORAH <chitlesh [AT] fedoraproject DOT org> 1.462-1
- new upstream release

* Fri Jan 09 2009 Chitlesh GOORAH <chitlesh [AT] fedoraproject DOT org> 1.461-1
- new upstream release

* Sun Dec 28 2008 Chitlesh GOORAH <chitlesh [AT] fedoraproject DOT org> 1.460-2
- spec file revisited upon request : #476449c1

* Sun Dec 14 2008 Chitlesh GOORAH <chitlesh [AT] fedoraproject DOT org> 1.460-1
- Specfile autogenerated by cpanspec 1.77.
