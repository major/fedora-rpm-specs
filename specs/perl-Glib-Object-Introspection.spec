Name:           perl-Glib-Object-Introspection
Version:        0.051
Release:        5%{?dist}
Summary:        Dynamically create Perl language bindings
License:        LGPL-2.1-or-later
URL:            https://metacpan.org/release/Glib-Object-Introspection
Source0:        https://cpan.metacpan.org/authors/id/X/XA/XAOC/Glib-Object-Introspection-%{version}.tar.gz
Patch1:         perl-Glib-Object-Introspection_lib_pattern.patch
# Use system-wide compiler flags when building test libraries. It's silents
# annocheck gating tests, CPAN RT#147466, proposed to the upstream.
Patch4:         Glib-Object-Introspection-0.050-Use-CFLAGS-and-LDFLAGS-from-the-envirnoment-for-buil.patch
# https://gitlab.gnome.org/GNOME/perl-glib-object-introspection/-/issues/7
Patch5:         Glib-Object-Introspection-0.051-Handle-pointer-types.patch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::Depends) >= 0.3
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(ExtUtils::PkgConfig) >= 1
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Glib::MakeHelper)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 0.10.0
BuildRequires:  pkgconfig(gmodule-2.0) >= 2.0.0
BuildRequires:  pkgconfig(libffi) >= 3.0.0
BuildRequires:  perl(Cairo::GObject)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(Glib) >= 1.320
BuildRequires:  perl(overload)
BuildRequires:  perl(XSLoader)
# Tests
BuildRequires:  perl(Glib::Object::Subclass)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(utf8)
# Optional tests
BuildRequires:  pkgconfig(cairo-gobject)
BuildRequires:  pkgconfig(gio-2.0)
Requires:       perl(Glib) >= 1.320

%{?perl_default_filter}
# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Glib\\)$
# Remove private libraries
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^(libgimarshallingtests|libregress).so\\(\\)
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(Glib::Object::Introspection::Install::Files\\)

%description
Glib::Object::Introspection uses the gobject-introspection and libffi projects
to dynamically create Perl bindings for a wide variety of libraries.  Examples
include gtk+, webkit, libsoup and many more.

%package -n perli11ndoc
Summary:        GObject Introspection documentation viewer
Requires:       %{name} = %{version}-%{release}
Recommends:     perl(Gtk3)
Requires:       perl(Text::Wrap)
# Subpackaged from perl-Glib-Object-Introspection-0.048-2.fc33, bug #1749126
Conflicts:      perl-Glib-Object-Introspection < 0.048-3
BuildArch:      noarch

%description -n perli11ndoc
This is a documentation viewer for GObject Introspection (GIR) files. With
perl(Gtk3), it provides an interactive graphical browser.

%package tests
Summary:        Tests for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%autosetup -p1 -n Glib-Object-Introspection-%{version}
# Help generators to recognize Perl scripts
for F in t/*.t t/inc/setup.pl; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
# If LANG is not set to UTF8, then when later running the test
# suite, you will see multiple failures handling UTF8 data
export LANG=C.UTF-8
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a build t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:build
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
LANG=C.UTF-8 make test

%files
%doc NEWS README.md
%license LICENSE
%dir %{perl_vendorarch}/auto/Glib
%dir %{perl_vendorarch}/auto/Glib/Object
%{perl_vendorarch}/auto/Glib/Object/Introspection
%dir %{perl_vendorarch}/Glib
%dir %{perl_vendorarch}/Glib/Object
%{perl_vendorarch}/Glib/Object/Introspection
%{perl_vendorarch}/Glib/Object/Introspection.pm
%{_mandir}/man3/Glib::Object::Introspection.*

%files -n perli11ndoc
%{_bindir}/perli11ndoc
%{_mandir}/man1/perli11ndoc.*

%files tests
%{_libexecdir}/%{name}

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.051-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Oct 18 2024 Michal Josef Špaček <mspacek@redhat.com> - 0.051-4
- Fix handling of pointer types (#2310793)

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.051-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 11 2024 Jitka Plesnikova <jplesnik@redhat.com> - 0.051-2
- Perl 5.40 rebuild

* Sun Feb 18 2024 Sérgio Basto <sergio@serjux.com> - 0.051-1
- Update perl-Glib-Object-Introspection to 0.051 (#2235533)

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.050-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.050-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.050-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 0.050-4
- Perl 5.38 rebuild

* Fri Mar 31 2023 Petr Pisar <ppisar@redhat.com> - 0.050-3
- Use system-wide compiler flags when building test libraries

* Thu Mar 30 2023 Petr Pisar <ppisar@redhat.com> - 0.050-2
- Fix handling empty closure callbacks (#2181971)
- Convert a license to an SPDX format
- Package tests in perl-Glib-Object-Introspection-tests package

* Mon Mar 27 2023 Sérgio Basto <sergio@serjux.com> - 0.050-1
- Update perl-Glib-Object-Introspection to 0.050 (#2181971)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.049-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 04 2023 Sérgio Basto <sergio@serjux.com> - 0.049-10
- Drop dependency perl-Cairo-GObject only need for an optional test

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.049-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.049-8
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.049-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Jan 08 2022 Miro Hrončok <mhroncok@redhat.com> - 0.049-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/LIBFFI34

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.049-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 22 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.049-4
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.049-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Oct 23 2020 Sérgio Basto <sergio@serjux.com> - 0.049-2
- A less-strict template (#1749132)

* Wed Oct 21 2020 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 0.049-1
- Update to 0.049 (#1890253)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.048-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.048-4
- Perl 5.32 rebuild

* Mon May 11 2020 Petr Pisar <ppisar@redhat.com> - 0.048-3
- Subpackage perli11ndoc tool (bug #1749126)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.048-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 11 2019 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 0.048-1
- Update to 0.048 (#1782378)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.047-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.047-2
- Perl 5.30 rebuild

* Thu Feb 28 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.047-1
- 0.047 bump

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.046-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 19 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.046-2
- Use C.UTF-8 locale
  See https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Thu Oct 11 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.046-1
- 0.046 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.045-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.045-2
- Perl 5.28 rebuild

* Tue Jun 05 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.045-1
- 0.045 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.044-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Nov 10 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.044-1
- 0.044 bump

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.043-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.043-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 20 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.043-1
- 0.043 bump

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.042-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.042-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 19 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.042-1
- 0.042 bump

* Wed Dec 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.041-1
- 0.041 bump

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.040-2
- Perl 5.24 rebuild

* Tue Mar 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.040-1
- 0.040 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.032-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 11 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.032-1
- 0.032 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.029-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.029-2
- Perl 5.22 rebuild

* Thu May 28 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.029-1
- 0.029 bump

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.024-3
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.024-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Aug 08 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.024-1
- 0.024 bump

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.022-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 02 2014 Petr Pisar <ppisar@redhat.com> - 0.022-1
- 0.022 bump

* Tue Oct  1 2013 Daniel P. Berrange <berrange@redhat.com> - 0.016-1
- Update to 0.016 release (rhbz #1013534)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.015-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 21 2013 Petr Pisar <ppisar@redhat.com> - 0.015-2
- Perl 5.18 rebuild

* Mon Mar  4 2013 Daniel P. Berrange <berrange@redhat.com> - 0.015-1
- Update to 0.015 release (rhbz #917609)

* Mon Feb  4 2013 Daniel P. Berrange <berrange@redhat.com> - 0.014-1
- Update to 0.014 release (rhbz #907381)

* Tue Dec 18 2012 Daniel P. Berrange <berrange@redhat.com> - 0.013-1
- Update to 0.013 release (rhbz #844966)

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.010-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 09 2012 Petr Pisar <ppisar@redhat.com> - 0.010-2
- Perl 5.16 rebuild

* Mon Jul  9 2012 Daniel P. Berrange <berrange@redhat.com> - 0.010-1
- Update to 0.010 release (rh bz #828220)

* Fri Jun 22 2012 Petr Pisar <ppisar@redhat.com> - 0.009-2
- Perl 5.16 rebuild

* Wed Jun 20 2012 Petr Pisar <ppisar@redhat.com> - 0.009-1
- 0.009 bump

* Wed Jun 13 2012 Petr Pisar <ppisar@redhat.com> - 0.008-2
- Perl 5.16 rebuild

* Mon Apr 30 2012 Daniel P. Berrange <berrange@redhat.com> - 0.008-1
- Update to 0.008 release (rhbz #817256)

* Thu Mar  1 2012 Daniel P. Berrange <berrange@redhat.com> - 0.007-1
- Update to 0.007 release (rhbz #798962)

* Tue Feb  7 2012 Daniel P. Berrange <berrange@redhat.com> - 0.006-2
- Add Cairo::GObject BR for tests

* Mon Jan 30 2012 Daniel P. Berrange <berrange@redhat.com> - 0.006-1
- Update to 0.006 release (rhbz #785363)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.004-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 23 2011 Daniel P. Berrange <berrange@redhat.com> - 0.004-1
- Import after Fedora review (rhbz #754749)
- Update to 0.004
- Add BR on cairo to ensure tests are built
- Use custom perl filter for auto-provides
- Fix license to be LGPLv2+

* Mon Nov 21 2011 Daniel P. Berrange <berrange@redhat.com> - 0.003-2
- Add missing BRs on Test::More Glib::MakeHelper & gobject-introspection-devel
- Add requires on perl MODULE_COMPAT
- Add comment about UTF8 requirement

* Fri Nov 04 2011 Daniel P. Berrange <berrange@redhat.com> 0.003-1
- Specfile autogenerated by cpanspec 1.78.
