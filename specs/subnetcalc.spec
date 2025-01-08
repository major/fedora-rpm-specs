Name:           subnetcalc
Version:        2.6.2
Release:        %autorelease
Summary:        IPv4/IPv6 Subnet Calculator
License:        GPL-3.0-or-later
URL:            https://www.nntb.no/~dreibh/subnetcalc/
Source0:        https://www.nntb.no/~dreibh/subnetcalc/download/%{name}-%{version}.tar.xz


BuildRequires:  gcc gcc-c++
BuildRequires:  GeoIP-devel
BuildRequires:  cmake
BuildRequires:  gettext

%description
SubNetCalc is an IPv4/IPv6 subnet address calculator. For given IPv4 or IPv6 
address and netmask or prefix length, it calculates network address, broadcast
address, maximum number of hosts and host address range. Also, it prints the 
addresses in binary format for better understandability. Furthermore, it 
prints useful information on specific address types (e.g. type, scope, 
interface ID, etc.).

%prep
%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install
%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog README.md
%license COPYING
%{_bindir}/subnetcalc
%{_datadir}/bash-completion/completions/subnetcalc
%{_mandir}/man1/subnetcalc.1*

%changelog
%autochangelog
