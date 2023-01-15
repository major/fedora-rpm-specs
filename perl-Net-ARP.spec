%define real_name Net-ARP

Name:       perl-Net-ARP
Version:    1.0.12
Release:    %autorelease
Summary:    Create and Send ARP Packets
License:    GPLv2
URL:        https://metacpan.org/release/%{real_name}
Source0:    https://cpan.metacpan.org/authors/id/C/CR/CRAZYDJ/%{real_name}-%{version}.tar.gz
BuildRequires: make
BuildRequires: gcc
BuildRequires: perl-devel
BuildRequires: perl-generators
BuildRequires: perl(ExtUtils::MakeMaker)


%{?perl_default_filter}

%description
This module is a Perl extension to create and send ARP packets and lookup
local or remote mac addresses. You do not need to install any additional 
libraries like Libnet to compile this extension. It uses kernel header files 
to create the packets.

%prep
%setup -q -n %{real_name}-%{version}
chmod -x README *.pm *.c *.h

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -type d -depth -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%check
# The tests for this package require root privileges and network access,
# therefore for automated building we need to leave it out.
#
#make test
#

%files
%doc Changes README
%{perl_vendorarch}/Net/
%{_mandir}/man3/Net::ARP.3pm*
%{perl_vendorarch}/auto/Net/

%changelog
%autochangelog
