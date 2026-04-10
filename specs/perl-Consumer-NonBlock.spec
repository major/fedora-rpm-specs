Name:           perl-Consumer-NonBlock
Version:        0.003
Release:        1%{?dist}
Summary:        Send data between processes without blocking
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Consumer-NonBlock
Source0:        https://www.cpan.org/authors/id/E/EX/EXODIST/Consumer-NonBlock-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10.0
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Handle) >= 1.27
BuildRequires:  perl(Object::HashBase)
BuildRequires:  perl(Time::HiRes)
# Tests:
BuildRequires:  perl(ok)
BuildRequires:  perl(Test2::V0) >= 0.000127
Requires:       perl(IO::Handle) >= 1.27

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(IO::Handle\\)$

%description
It is very easy to end up in a situation where a producer process produces
data faster than a consumer process can read/process it resulting in the
producer blocking on a full pipe buffer. This module allows 2 processes to
share data similar to a pipe, but without the producer blocking due to full
pipe buffers.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(ok)
Requires:       perl(Test2::V0) >= 0.000127

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n Consumer-NonBlock-%{version}

%build
unset AUTOMATED_TESTING
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
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset CONSUMER_NONBLOCK_DIR
make test

%files tests
%{_libexecdir}/%{name}

%files
%license LICENSE
# README.md is redundant
%doc Changes README
%dir %{perl_vendorlib}/Consumer
%{perl_vendorlib}/Consumer/NonBlock.pm
%{_mandir}/man3/Consumer::NonBlock.*

%changelog
* Wed Apr 08 2026 Petr Pisar <ppisar@redhat.com> - 0.003-1
- 0.003 bump

* Thu Apr 02 2026 Petr Pisar <ppisar@redhat.com> 0.002-1
- 0.002 version packaged
