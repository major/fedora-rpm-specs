%global use_x11_tests 1

Name:           perl-Gtk3
Version:        0.038
Release:        15%{?dist}
Summary:        Perl interface to the 3.x series of the GTK+ toolkit
License:        LGPL-2.1-or-later
URL:            https://metacpan.org/release/Gtk3
Source0:        https://cpan.metacpan.org/authors/id/X/XA/XAOC/Gtk3-%{version}.tar.gz
# Fix the tests to pass from a read-only location, CPAN RT#147461,
# proposed to an upstream.
Patch0:         Gtk3-0.038-Create-temporary-files-for-tests-in-HOME.patch
BuildArch:      noarch
BuildRequires:  gtk3
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Cairo::GObject) >= 1.000
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
# Glib::Object::Introspection version for
# Glib::Object::Introspection:convert_flags_to_sv(), CPAN RT#122761
BuildRequires:  perl(Glib::Object::Introspection) >= 0.043
BuildRequires:  perl(overload)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
# Tests
# Config used only on FreeBSD
BuildRequires:  perl(constant)
BuildRequires:  perl(Encode)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Glib)
BuildRequires:  perl(Glib::Object::Subclass)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(utf8)
%if 0%{?fedora} >= 41
# XPM loading for tests:
BuildRequires:  gdk-pixbuf2-modules-extra
%endif
%if %{use_x11_tests}
# X11 tests:
BuildRequires:  xorg-x11-server-Xvfb
BuildRequires:  font(:lang=en)
%endif
Requires:       gtk3
Requires:       perl(Cairo::GObject) >= 1.000
# Glib::Object::Introspection version for
# Glib::Object::Introspection:convert_flags_to_sv(), CPAN RT#122761
Requires:       perl(Glib::Object::Introspection) >= 0.043
Requires:       perl(POSIX)

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Cairo::GObject|Glib::Object::Introspection)\\)$

%description
The Gtk3 module allows a Perl developer to use the GTK+ graphical user
interface library. Find out more about GTK+ at <http://www.gtk.org/>.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%if 0%{?fedora} >= 41
# XPM loading for tests:
Requires:       gdk-pixbuf2-modules-extra
%endif
%if %{use_x11_tests}
# X11 tests:
Requires:       xorg-x11-server-Xvfb
Requires:       font(:lang=en)
%endif

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%autosetup -p1 -n Gtk3-%{version}
# Help generators to recognize Perl scripts
for F in t/*.t t/inc/setup.pl; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_install}

%install
%{make_install}
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec %{?use_x11_tests:xvfb-run -d }prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
%if %{use_x11_tests}
    xvfb-run -d make test
%else
    make test
%endif

%files
%license LICENSE
%doc NEWS README
%{perl_vendorlib}/Gtk3.pm
%{_mandir}/man3/Gtk3.*

%files tests
%{_libexecdir}/%{name}

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.038-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Aug 08 2024 Petr Pisar <ppisar@redhat.com> - 0.038-14
- gdk-pixbuf2-modules-extra is needed for the packaged tests (rhbz#2278602)

* Fri Jul 26 2024 Benjamin Gilbert <bgilbert@backtick.net> - 0.038-13
- BR gdk-pixbuf2-modules-extra on F41+ to fix XPM tests (rhbz#2278602)

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.038-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.038-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.038-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.038-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Mar 31 2023 Petr Pisar <ppisar@redhat.com> - 0.038-8
- Convert a license to an SPDX format
- Package tests into perl-Gtk3-tests package

* Thu Feb  9 2023 Tom Callaway <spot@fedoraproject.org> - 0.038-7.1
- rebuild for new epel macros

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.038-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.038-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.038-5
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.038-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.038-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 22 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.038-2
- Perl 5.34 rebuild

* Tue Feb 16 2021 Sérgio Basto <sergio@serjux.com> - 0.038-1
- Update perl-Gtk3 to 0.038 (#1918130)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.037-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.037-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.037-2
- Perl 5.32 rebuild

* Mon Apr 06 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.037-1
- 0.037 bump

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.036-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 03 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.036-1
- 0.036 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.035-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.035-2
- Perl 5.30 rebuild

* Tue May 28 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.035-1
- 0.35 bump

* Fri Feb 15 2019 Daniel P. Berrangé <berrange@redhat.com> - 0.034-6
- Re-enable tests skipped from previous build

* Tue Feb 12 2019 Daniel P. Berrange <berrange@redhat.com> - 0.034-5
- Fix for GdkPixdata gir split (rhbz #1675630)
- Temporarily disable tests broken by rhbz #1676474

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.034-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.034-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.034-2
- Perl 5.28 rebuild

* Tue Jun 05 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.034-1
- 0.034 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.033-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Nov 10 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.033-1
- 0.033 bump

* Thu Aug 10 2017 Petr Pisar <ppisar@redhat.com> - 0.032-2
- Correct minimal Glib::Object::Introspection version (CPAN RT#122761)

* Thu Aug 10 2017 Petr Pisar <ppisar@redhat.com> - 0.032-1
- 0.032 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.030-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.030-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.030-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.030-1
- 0.030 bump

* Mon Oct 03 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.029-1
- 0.029 bump

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.026-3
- Perl 5.24 rebuild

* Thu May 05 2016 Petr Pisar <ppisar@redhat.com> - 0.026-2
- Adjust tests to gtk3-3.21.1 (bug #1332962)

* Fri Apr 01 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.026-1
- 0.026 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.025-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 24 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.025-1
- 0.025 bump

* Fri Sep 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.023-1
- 0.023 bump

* Mon Jul 13 2015 Petr Pisar <ppisar@redhat.com> - 0.022-1
- 0.022 bump

* Wed Jun 17 2015 Daniel P. Berrange <berrange@redhat.com> - 0.021-1
- Update to 0.021 release

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.019-2
- Perl 5.22 rebuild

* Wed Dec 03 2014 Petr Pisar <ppisar@redhat.com> - 0.019-1
- 0.019 bump

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.017-3
- Perl 5.20 rebuild

* Tue Aug 12 2014 Petr Pisar <ppisar@redhat.com> - 0.017-2
- Run X11 tests using xvfb-run (bug #1129395)

* Wed Aug 06 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.017-1
- 0.017 bump

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.015-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Dec 10 2013 Daniel P. Berrange <berrange@redhat.com> - 0.015-1
- Update to 0.015 release (rhbz #1021207)

* Tue Oct  1 2013 Daniel P. Berrange <berrange@redhat.com> - 0.013-1
- Update to 0.013 release (rhbz #1003379)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.009-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 23 2013 Petr Pisar <ppisar@redhat.com> - 0.009-2
- Perl 5.18 rebuild

* Fri Feb 15 2013 Daniel P. Berrange <berrange@redhat.com> - 0.009-1
- Update to 0.009 release (rhbz #829260)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.008-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Dec 18 2012 Daniel P. Berrange <berrange@redhat.com> - 0.008-1
- Update to 0.008 release (rhbz #829260)

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.007-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul  9 2012 Daniel P. Berrange <berrange@redhat.com> - 0.007-1
- Update to 0.007 release (rhbz #829260)

* Fri Jun 22 2012 Petr Pisar <ppisar@redhat.com> - 0.006-2
- Perl 5.16 rebuild

* Wed Jun 20 2012 Petr Pisar <ppisar@redhat.com> - 0.006-1
- 0.006 bump

* Thu Jun 14 2012 Petr Pisar <ppisar@redhat.com> - 0.005-2
- Perl 5.16 rebuild

* Mon Apr 23 2012 Daniel P. Berrange <berrange@redhat.com> - 0.005-1
- Update to 0.005 release

* Mon Mar 19 2012 Daniel P. Berrange <berrange@redhat.com> - 0.004-1
- Update to 0.004 release

* Wed Feb  8 2012 Daniel P. Berrange <berrange@redhat.com> - 0.003-2
- Add Cairo::GObject BR

* Mon Jan 30 2012 Daniel P. Berrange <berrange@redhat.com> - 0.003-1
- Update to 0.003 release (rhbz #785532)

* Thu Jan  5 2012 Daniel P. Berrange <berrange@redhat.com> - 0.002-2
- Use xvfb to run test suite
- Fix capitalization of GTK+
- Remove dist.ini & perl-Gtk3.doap
- Remove defattr from files section
- Add missing BuildRequires for test suite
- Add trailing / into URIs

* Thu Dec 15 2011 Daniel P. Berrange <berrange@redhat.com> - 0.002-1
- Update to 0.002 release

* Mon Nov 28 2011 Daniel P. Berrange <berrange@redhat.com> - 0.001-2
- Add Test::More BR
- Disable overrides.t test (rt #72773)
- Comment about running test without $DISPLAY available

* Fri Nov 04 2011 Daniel P Berrange <berrange@redhat.com> 0.001-1
- Specfile autogenerated by cpanspec 1.78.
