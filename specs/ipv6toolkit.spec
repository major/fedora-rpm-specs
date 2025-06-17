Summary:        Security assessment and troubleshooting tools for IPv6 protocols
Name:           ipv6toolkit
Version:        2.2
Release:        2%{?dist}
License:        GPL-3.0-or-later AND GFDL-1.3-no-invariants-or-later AND MPL-2.0
# ipv6toolkit itself is GPL-3.0-or-later but uses other source codes, breakdown:
# GFDL-1.3-no-invariants-or-later: manuals/*.[157]
# MPL-2.0: data/public_suffix_list.dat
URL:            https://www.si6networks.com/research/tools/ipv6toolkit/
Source0:        https://github.com/fgont/%{name}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  libpcap-devel
BuildRequires:  perl-generators
# Tests
BuildRequires:  perl-interpreter
BuildRequires:  perl(Crypt::X509)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Net::DNS)
BuildRequires:  perl(Net::IP)
BuildRequires:  perl(Socket)
BuildRequires:  perl(constant)
Requires:       curl

%description
The SI6 Networks IPv6 toolkit is a suite of IPv6 security assessment and
troubleshooting tools. It can be used to assess the security of IPv6
networks, evaluate the resilience of IPv6 devices by subjecting them to
real-world attacks, and troubleshoot IPv6 networking issues. The toolkit
comprises tools ranging from packet-crafting tools for sending arbitrary
Neighbor Discovery packets to a comprehensive IPv6 network scanning tool.

%prep
%setup -q
for file in *.TXT; do mv -f ${file} $(basename ${file} .TXT); done

%build
export CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS"
%make_build PREFIX=%{_prefix}

%install
%make_install PREFIX=%{_prefix} MANPREFIX=%{_datadir} \
%if 0%{?fedora} >= 42 || 0%{?rhel} >= 11
  SBINPATH=$RPM_BUILD_ROOT%{_sbindir}
%endif

%check
make unit_tests

# Catch Perl syntax errors and new run-time Perl dependencies during build-time
for tool in tools/*; do if grep -q -E '^#!/.*perl' ${tool}; then perl -c ${tool}; fi; done

%files
%license LICENSE
%doc CHANGES CREDITS
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_bindir}/addr6
%{_sbindir}/blackhole6
%{_sbindir}/flow6
%{_sbindir}/frag6
%{_sbindir}/icmp6
%{_sbindir}/jumbo6
%{_sbindir}/messi
%{_sbindir}/mldq6
%{_sbindir}/na6
%{_sbindir}/ni6
%{_sbindir}/ns6
%{_sbindir}/path6
%{_sbindir}/ra6
%{_sbindir}/rd6
%{_sbindir}/rs6
%{_sbindir}/scan6
%{_sbindir}/script6
%{_sbindir}/tcp6
%{_sbindir}/udp6
%{_datadir}/%{name}/
%{_mandir}/man1/addr6.1*
%{_mandir}/man1/blackhole6.1*
%{_mandir}/man1/flow6.1*
%{_mandir}/man1/frag6.1*
%{_mandir}/man1/icmp6.1*
%{_mandir}/man1/jumbo6.1*
%{_mandir}/man1/mldq6.1*
%{_mandir}/man1/na6.1*
%{_mandir}/man1/ni6.1*
%{_mandir}/man1/ns6.1*
%{_mandir}/man1/path6.1*
%{_mandir}/man1/ra6.1*
%{_mandir}/man1/rd6.1*
%{_mandir}/man1/rs6.1*
%{_mandir}/man1/scan6.1*
%{_mandir}/man1/script6.1*
%{_mandir}/man1/tcp6.1*
%{_mandir}/man1/udp6.1*
%{_mandir}/man5/ipv6toolkit.conf.5*
%{_mandir}/man7/ipv6toolkit.7*

%changelog
* Fri May 16 2025 Robert Scheck <robert@fedoraproject.org> 2.2-2
- License correction and breakdown in spec file (#2366587 #c4)

* Thu May 15 2025 Robert Scheck <robert@fedoraproject.org> 2.2-1
- Upgrade to 2.2 (#2366587)

* Sun May 01 2022 Robert Scheck <robert@fedoraproject.org> 2.0-1
- Upgrade to 2.0
- Initial spec file for Fedora and Red Hat Enterprise Linux
