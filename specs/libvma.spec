%{!?configure_options: %global configure_options %{nil}}

Name: libvma
Version: 9.8.80
Release: %autorelease
Summary: A library for boosting TCP and UDP traffic (over RDMA hardware)

License: GPL-2.0-only OR BSD-2-Clause
Url: https://github.com/Mellanox/libvma
Source0: https://github.com/Mellanox/libvma/archive/%{version}/%{name}-%{version}.tar.gz

# libvma currently supports only the following architectures
ExclusiveArch: x86_64 ppc64le ppc64 aarch64

BuildRequires: pkgconfig
BuildRequires: automake
BuildRequires: autoconf
BuildRequires: libtool
BuildRequires: gcc-c++
BuildRequires: rdma-core-devel
BuildRequires: systemd-rpm-macros
BuildRequires: pkgconfig(libnl-3.0)
BuildRequires: pkgconfig(libnl-route-3.0)
BuildRequires: make

%description
libvma is a LD_PRELOAD-able library that boosts performance of TCP and
UDP traffic. It allows application written over standard socket API to
handle fast path data traffic from user space over Ethernet and/or
Infiniband with full network stack bypass and get better throughput,
latency and packets/sec rate.

No application binary change is required for that.
libvma is supported by RDMA capable devices that support "verbs"
IBV_QPT_RAW_PACKET QP for Ethernet and/or IBV_QPT_UD QP for IPoIB.

%package devel
Summary: Header files required to develop with libvma
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package includes headers for building programs with libvma's
interfaces.

%package utils
Summary: Utilities used with libvma
Requires: %{name}%{?_isa} = %{version}-%{release}

%description utils
This package contains the tool for collecting and analyzing libvma statistic.

%prep
%autosetup -p1

%build
export revision=1
if [ ! -e configure ] && [ -e autogen.sh ]; then
    PRJ_RELEASE=1 ./autogen.sh
fi

%configure %{?configure_options}
%{make_build}

%install
%{make_install}

find $RPM_BUILD_ROOT%{_libdir} -name '*.la' -delete
install -D -m 644 contrib/scripts/vma.service $RPM_BUILD_ROOT/%{_prefix}/lib/systemd/system/vma.service
rm -f $RPM_BUILD_ROOT/%{_sysconfdir}/init.d/vma

%post
%systemd_post vma.service

%preun
%systemd_preun vma.service

%postun
%systemd_postun_with_restart vma.service

%files
%{_libdir}/%{name}.so*
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README
%doc %{_pkgdocdir}/CHANGES
%config(noreplace) %{_sysconfdir}/libvma.conf
%{_sbindir}/vmad
%{_prefix}/lib/systemd/system/vma.service
%license LICENSE
%{_mandir}/man7/vma.*
%{_mandir}/man8/vmad.*

%files devel
%dir %{_includedir}/mellanox
%{_includedir}/mellanox/vma_extra.h

%files utils
%{_bindir}/vma_stats
%{_mandir}/man8/vma_stats.*

%changelog
%autochangelog
