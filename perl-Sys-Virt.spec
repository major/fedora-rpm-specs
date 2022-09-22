Name:           perl-Sys-Virt
Version:        8.5.0
Release:        1%{?dist}
Summary:        Represent and manage a libvirt hypervisor connection
License:        GPLv2+ or Artistic
URL:            https://metacpan.org/release/Sys-Virt
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DANBERR/Sys-Virt-v%{version}.tar.gz
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  libvirt-devel >= %{version}
BuildRequires:  perl-devel
%if 0%{?fedora} || 0%{?rhel} > 7
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
%endif
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Module::Build)
BuildRequires:  sed
# Runtime
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
# Tests only
BuildRequires:  perl(base)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(XML::XPath)
BuildRequires:  perl(XML::XPath::XMLParser)
# Optional tests
%if ! 0%{?rhel}
BuildRequires:  perl(Test::CPAN::Changes)
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.00
%endif
Requires:       perl(:MODULE_COMPAT_%(eval "$(perl -V:version)"; echo $version))

%description
The Sys::Virt module provides a Perl XS binding to the libvirt virtual
machine management APIs. This allows machines running within arbitrary
virtualization containers to be managed with a consistent API.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}-%{version}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%autosetup -S git -n Sys-Virt-v%{version}

# Help file to recognise the Perl scripts and normalize shebangs
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*

# Install tests
mkdir -p %{buildroot}/%{_libexecdir}/%{name}
cp -a t %{buildroot}/%{_libexecdir}/%{name}
rm -f %{buildroot}/%{_libexecdir}/%{name}/t/*-pod*.t
rm -f %{buildroot}/%{_libexecdir}/%{name}/t/015-changes.t
cat > %{buildroot}/%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}/%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test

%files
%license LICENSE
%doc AUTHORS Changes README examples/
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Sys*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
* Mon Jul 25 2022 Jitka Plesnikova <jplesnik@redhat.com> - 8.5.0-1
- 8.5.0 bump

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Jitka Plesnikova <jplesnik@redhat.com> - 8.4.0-1
- 8.4.0 bump

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 8.3.0-2
- Perl 5.36 rebuild

* Wed May 04 2022 Jitka Plesnikova <jplesnik@redhat.com> - 8.2.0-1
- 8.3.0 bump

* Wed Mar 02 2022 Jitka Plesnikova <jplesnik@redhat.com> - 8.1.0-1
- 8.1.0 bump

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 17 2022 Jitka Plesnikova <jplesnik@redhat.com> - 8.0.0-1
- 8.0.0 bump

* Thu Dec 02 2021 Jitka Plesnikova <jplesnik@redhat.com> - 7.10.0-1
- 7.10.0 bump

* Tue Nov 02 2021 Jitka Plesnikova <jplesnik@redhat.com> - 7.9.0-1
- 7.9.0 bump

* Sun Oct 03 2021 Jitka Plesnikova <jplesnik@redhat.com> - 7.8.0-1
- 7.8.0 bump

* Fri Sep 03 2021 Jitka Plesnikova <jplesnik@redhat.com> - 7.7.0-1
- 7.7.0 bump

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jul 02 2021 Jitka Plesnikova <jplesnik@redhat.com> - 7.5.0-1
- 7.5.0 bump

* Fri Jun 04 2021 Jitka Plesnikova <jplesnik@redhat.com> - 7.4.0-1
- 7.4.0 bump

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 7.3.0-2
- Perl 5.34 rebuild

* Tue May 04 2021 Jitka Plesnikova <jplesnik@redhat.com> - 7.3.0-1
- 7.3.0 bump

* Tue Apr 06 2021 Jitka Plesnikova <jplesnik@redhat.com> - 7.2.0-1
- 7.2.0 bump

* Tue Mar 02 2021 Jitka Plesnikova <jplesnik@redhat.com> - 7.1.0-1
- 7.1.0 bump
- Package tests

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 15 2021 Petr Pisar <ppisar@redhat.com> - 7.0.0-1
- 7.0.0 bump

* Tue Dec 01 2020 Jitka Plesnikova <jplesnik@redhat.com> - 6.10.0-1
- 6.10.0 bump

* Mon Oct  5 2020 Daniel P. Berrangé <berrange@redhat.com> - 6.8.0-1
- Update to 6.8.0 release

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 6.3.0-2
- Perl 5.32 rebuild

* Tue May 05 2020 Cole Robinson <crobinso@redhat.com> - 6.3.0-1
- Update to version 6.3.0

* Tue Mar 10 2020 Jitka Plesnikova <jplesnik@redhat.com> - 6.1.0-1
- Update to version 6.1.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 16 2020 Jitka Plesnikova <jplesnik@redhat.com> - 6.0.0-1
- Update to version 6.0.0
