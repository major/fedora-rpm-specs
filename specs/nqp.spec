Name:           nqp
Version:        2025.12
Release:        %autorelease
Summary:        Perl 6 compiler implementation that runs on MoarVM
License:        Artistic-2.0
URL:            https://github.com/Raku/nqp
Source0:        %{url}/releases/download/%{version}/nqp-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl
BuildRequires:  moarvm-devel >= %{version}

%description
This is "Not Quite Perl" -- a lightweight Raku-like environment for virtual
machines. The key feature of NQP is that it's designed to be a very small
environment (as compared with, say, raku or Rakudo) and is focused on being
a high-level way to create compilers and libraries for virtual machines like
MoarVM, the JVM, and others.

%prep
%autosetup

%build
%{__perl} Configure.pl --backends=moar --prefix=%{_prefix}
%make_build

%install
%make_install

%check
make test

%files
%license LICENSE
%doc README.pod
%{_bindir}/nqp
%{_bindir}/nqp-m
%{_datadir}/nqp/lib/*.moarvm
%{_datadir}/nqp/lib/profiler

%changelog
%autochangelog
