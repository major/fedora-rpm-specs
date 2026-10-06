%global forgeurl https://github.com/intel/openlldp
%global version0 1.2.0
%forgemeta

Name:               lldpad
Version:            %forgeversion
Release:            %autorelease
Summary:            Link Layer Discovery Protocol (LLDP) Agent
License:            GPL-2.0-only
URL:                %forgeurl
Source0:            %forgesource

BuildRequires:      automake autoconf libtool
BuildRequires:      flex >= 2.5.33
BuildRequires:      kernel-headers >= 2.6.32
BuildRequires:      libconfig-devel >= 1.3.2
BuildRequires:      libnl3-devel
BuildRequires:      readline-devel
BuildRequires:      systemd
BuildRequires:      make

# weak_readline.c dlopen()s libhistory.so and libreadline.so,
# with no version suffix. They are in the -devel package.
Recommends:         readline-devel

%{?systemd_requires}

%description
This package contains lldpad, a userspace daemon and configuration tool
that implements the Link Layer Discovery Protocol (LLDP, IEEE 802.1AB).
It also supports Data Center Bridging (DCB) extensions such as ETS and
Priority Flow Control (802.1Qaz/802.1Qbb) for negotiating enhanced
Ethernet parameters with switches.

%package            devel
Summary:            Development files for %{name}
Requires:           %{name}%{?_isa} = %{version}-%{release}
Provides:           dcbd-devel = %{version}-%{release}
Obsoletes:          dcbd-devel < 0.9.26

%description devel
The %{name}-devel package contains header files for developing applications
that use %{name}.

%prep
%forgeautosetup -p1

%build
./bootstrap.sh
CFLAGS=${CFLAGS:-%optflags -Wno-error -fcommon}; export CFLAGS;
%configure --disable-static
%make_build

%install
%make_install
mkdir -p %{buildroot}%{_sharedstatedir}/%{name}
rm -f %{buildroot}%{_libdir}/liblldp_clif.la

%post
%systemd_post %{name}.service %{name}.socket

%preun
%systemd_preun %{name}.service %{name}.socket

%postun
%systemd_postun_with_restart %{name}.service %{name}.socket

%files
%license COPYING
%doc README ChangeLog
%{_sbindir}/*
%{_libdir}/liblldp_clif.so.*
%dir %{_sharedstatedir}/%{name}
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}.socket
%{_sysconfdir}/bash_completion.d/*
%{_mandir}/man3/*
%{_mandir}/man8/*

%files devel
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
%{_libdir}/liblldp_clif.so

%changelog
%autochangelog
