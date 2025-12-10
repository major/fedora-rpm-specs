# it crashes with lto enabled on StringsetParser::parsers first modification
%define _lto_cflags %{nil}

Name:           ethq
Version:        0.7.0
Release:        %autorelease
Summary:        Ethernet NIC Queue stats viewer

%global gitver %{lua:gv,n=string.gsub(macros.version, '[.]', '_');print(gv)}

License:        MPL-2.0
URL:            https://github.com/isc-projects/ethq
Source0:        %{url}/archive/v%{gitver}/%{name}-%{version}.tar.gz


BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  ncurses-devel

%description
Displays an auto-updating per-second count of the number of packets and
bytes being handled by each specified NIC, and on multi-queue NICs shows
the per-queue statistics too.

%prep
%autosetup -n %{name}-%{gitver}


%build
%make_build CXXFLAGS="${CXXFLAGS}" LDFLAGS="${LDFLAGS}"


%install
# TODO: contribute make install target
%dnl %make_install CFLAGS="${CFLAGS}" LDFLAGS="${LDFLAGS}"
mkdir -p %{buildroot}%{_sbindir}
install ethq %{buildroot}%{_sbindir}


%check
./%{name} -h
./%{name}_test generic < /dev/null


%files
%license LICENSE
%doc README.md
%{_sbindir}/%{name}



%changelog
%autochangelog
