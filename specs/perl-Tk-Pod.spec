%global use_x11_tests 1
%if 0%{?rhel} >= 10
%define test_with_wayland 1
%else
%define test_with_wayland 0
%endif

Name:           perl-Tk-Pod
Version:        0.9943
Release:        29%{?dist}
Summary:        Pod browser top-level widget
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Tk-Pod
Source0:        https://cpan.metacpan.org/authors/id/S/SR/SREZIC/Tk-Pod-%{version}.tar.gz
# Adapt tests for checking installed scripts, proposed to the upstream,
# <https://github.com/eserte/tk-pod/pull/1>
Patch0:         Tk-Pod-0.9943-Allow-t-cmdline.t-to-test-installed-scripts.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
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
%if %{test_with_wayland}
BuildRequires:  mesa-dri-drivers
BuildRequires:  mutter
BuildRequires:  xwayland-run
%else
BuildRequires:  font(:lang=en)
BuildRequires:  xorg-x11-server-Xvfb
%endif
%endif
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
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Tk(::Pod)?\\)\\s*$
# Hide private modules
%global __requires_exclude %{__requires_exclude}|^perl\\(TkTest\\)
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(TkTest\\)

%description
Simple Pod browser with hypertext capabilities in a Toplevel widget.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl(File::Temp)
Requires:       perl(Test)
Requires:       perl(Test::More)
Requires:       perl(Tk) >= 800.004
%if %{use_x11_tests}
# X11 tests:
%if %{test_with_wayland}
BuildRequires:  mesa-dri-drivers
BuildRequires:  mutter
BuildRequires:  xwayland-run
%else
Requires:       xorg-x11-server-Xvfb
Requires:       font(:lang=en)
%endif
%endif

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%autosetup -p1 -n Tk-Pod-%{version}
chmod -x Pod_usage.pod

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
# Install tests
mkdir -p $RPM_BUILD_ROOT%{_libexecdir}/%{name}
cp -a t $RPM_BUILD_ROOT%{_libexecdir}/%{name}
cat > $RPM_BUILD_ROOT%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
%if %{use_x11_tests}
%if %{test_with_wayland}
cd %{_libexecdir}/%{name} && exec xwfb-run -c mutter -- prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
%else
cd %{_libexecdir}/%{name} && exec xvfb-run -d prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
%endif
%else
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
%endif
EOF
chmod +x $RPM_BUILD_ROOT%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
%if %{use_x11_tests}
%if %{test_with_wayland}
    xwfb-run -c mutter -- make test
%else
    xvfb-run -d make test
%endif
%else
    make test
%endif

%files
%doc Changes README TODO
%dir %{perl_vendorlib}/Tk
%{perl_vendorlib}/Tk/More.pm
%{perl_vendorlib}/Tk/Pod
%{perl_vendorlib}/Tk/Pod.pm
%{perl_vendorlib}/Tk/Pod_usage.pod
%{_bindir}/tkmore
%{_bindir}/tkpod
%{_mandir}/man3/Tk::More.*
%{_mandir}/man3/Tk::Pod.*
%{_mandir}/man3/Tk::Pod::*
%{_mandir}/man3/Tk::Pod_usage.*
%{_mandir}/man1/tkmore.*
%{_mandir}/man1/tkpod.*

%files tests
%{_libexecdir}/%{name}

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9943-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 25 2024 Petr Pisar <ppisar@redhat.com> - 0.9943-28
- Modernize a spec file
- Package the tests

* Tue Aug 06 2024 Miroslav Suchý <msuchy@redhat.com> - 0.9943-27
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9943-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9943-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9943-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9943-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9943-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

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
