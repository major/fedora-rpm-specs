Name:           qrtr
Version:        1.0
Release:        %autorelease
Summary:        Service listing daemon for Qualcomm IPC Router

# src/map.c is BSD-2-Clause, the rest is BSD-3-Clause
License:        BSD-3-Clause AND BSD-2-Clause
URL:            https://github.com/andersson/qrtr
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# Makefile: allow $(CFLAGS), $(LDFLAGS) override
Patch:          %{url}/commit/a4398c8bf271f90338f95e1230373dde977d9cff.patch
# lookup: add Snapdragon Sensor Core service
Patch:          %{url}/commit/d0d471c96e7d112fac6f48bd11f9e8ce209c04d2.patch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  systemd-rpm-macros

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description
This package provides the userspace component for the Qualcomm IPC Router
protocol, which maintains a service listing and allows peforming lookups.

%package        libs
Summary:        Shared libraries for %{name}

%description    libs
This packages provides shared libraries for %{name}.

%package        devel
Summary:        Development headers and libraries for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
This packages provides development headers and libraries for %{name}.

%prep
%autosetup -p1

%build
%make_build prefix="%{_prefix}" libdir="%{_libdir}"

%install
%make_install prefix="%{_prefix}" libdir="%{_libdir}"

%post
%systemd_post qrtr-ns.service

%preun
%systemd_preun qrtr-ns.service

%postun
%systemd_postun_with_restart qrtr-ns.service

%files
%{_bindir}/qrtr-cfg
%{_bindir}/qrtr-lookup
%{_bindir}/qrtr-ns
%{_unitdir}/qrtr-ns.service

%files devel
%{_includedir}/libqrtr.h
%{_libdir}/libqrtr.so

%files libs
%license LICENSE
%{_libdir}/libqrtr.so.1*

%changelog
%autochangelog
