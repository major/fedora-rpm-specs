Name:           perl-Gtk3-ImageView
Version:        12
Release:        2%{?dist}
Summary:        Image viewer widget for GTK 3
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://github.com/DarthGandalf/gtk3-imageview
Source0:        https://cpan.metacpan.org/authors/id/A/AS/ASOKOLOV/Gtk3-ImageView-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Cairo)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Glib) >= 1.2100
BuildRequires:  perl(Glib::Object::Subclass)
BuildRequires:  perl(Gtk3)
BuildRequires:  perl(if)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Readonly)
BuildRequires:  perl(Scalar::Util)
# Tests:
BuildRequires:  perl(Carp::Always)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Image::Magick)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::MockObject)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  xorg-x11-server-Xvfb
# Optional tests:
# CPAN::Meta not helpful
# CPAN::Meta::Prereqs not helpful
Requires:       perl(if)
Requires:       perl(Glib) >= 1.2100

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Glib\\)$

%description
The Gtk3::ImageView widget allows the user to zoom, pan and select the
specified image and provides hooks to allow additional tools, e.g. painter,
to be created and used.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Glib) >= 1.2100
Requires:       xorg-x11-server-Xvfb

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%autosetup -p1 -n Gtk3-ImageView-%{version}
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec xvfb-run -d prove -I . -j 1
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
# Not parallel-safe
xvfb-run -d make test

%files
%license LICENSE
%doc README.md
%dir %{perl_vendorlib}/Gtk3
%{perl_vendorlib}/Gtk3/ImageView
%{perl_vendorlib}/Gtk3/ImageView.pm
%{_mandir}/man3/Gtk3::ImageView.*

%files tests
%{_libexecdir}/%{name}

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Oct 17 2024 Petr Pisar <ppisar@redhat.com> - 12-1
- 12 version bump

* Wed Oct 02 2024 Petr Pisar <ppisar@redhat.com> - 11-1
- 11 version bump

* Thu Aug 01 2024 Petr Pisar <ppisar@redhat.com> - 10-11
- Adapt to changes in Perl 5.38 (upstream GH#30)

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Feb 08 2023 Petr Pisar <ppisar@redhat.com> - 10-6
- Convert a license tag to an SPDX format

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 10-3
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 04 2021 Petr Pisar <ppisar@redhat.com> - 10-1
- Version 10 bump (bug #2010062)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 22 2021 Jitka Plesnikova <jplesnik@redhat.com> - 9-2
- Perl 5.34 rebuild

* Mon May 17 2021 Petr Pisar <ppisar@redhat.com> - 9-1
- 9 version bump

* Mon May 10 2021 Petr Pisar <ppisar@redhat.com> - 8-1
- 8 version bump
- Package the tests

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 18 2020 Petr Pisar <ppisar@redhat.com> - 6-1
- Version 6 bump

* Mon Nov 02 2020 Petr Pisar <ppisar@redhat.com> 4-1
- Specfile autogenerated by cpanspec 1.78.
