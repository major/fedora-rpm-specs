Name:           perl-Atomic-Pipe
Version:        0.023
Release:        1%{?dist}
Summary:        Send atomic messages from multiple writers across a POSIX pipe
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Atomic-Pipe
Source0:        https://www.cpan.org/authors/id/E/EX/EXODIST/Atomic-Pipe-%{version}.tar.gz
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
BuildRequires:  perl(bytes)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Fcntl)
# IO version from IO::Handle in META
BuildRequires:  perl(IO) >= 1.27
BuildRequires:  perl(List::Util) >= 1.44
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
# Tests:
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test2::IPC)
BuildRequires:  perl(Test2::Util)
BuildRequires:  perl(Test2::V0) >= 0.000127
# threads never used
BuildRequires:  perl(Time::HiRes)
Requires:       perl(IO) >= 1.27
Requires:       perl(List::Util) >= 1.44
Requires:       perl(POSIX)

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((IO|List::Util|Test2::V0))$

%description
Normally if you write to a pipe from multiple processes/threads, the
messages will come mixed together unpredictably. Some messages may be
interrupted by parts of messages from other writers. This module takes
advantage of some POSIX specifications to allow multiple writers to send
arbitrary data down a pipe in atomic chunks to avoid the issue.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Test2::V0) >= 0.000127
Requires:       perl(warnings)

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n Atomic-Pipe-%{version}

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
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
# README.md is redundand to README.
%doc Changes README
%dir %{perl_vendorlib}/Atomic
%{perl_vendorlib}/Atomic/Pipe.pm
%{_mandir}/man3/Atomic::Pipe.*

%files tests
%{_libexecdir}/%{name}

%changelog
* Thu Apr 02 2026 Petr Pisar <ppisar@redhat.com> 0.023-1
- 0.023 version packaged
