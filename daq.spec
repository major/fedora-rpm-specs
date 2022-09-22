# Warning:
# Anyone editing this spec file please make sure the same spec file
# works on other fedora and epel releases, which are supported by this software.
# No quick Rawhide-only fixes will be allowed.

%global upstream_name daq

%if 0%{?el7}
# el7/{ppc64,ppc64le} Error: No Package found for libdnet-devel
ExclusiveArch:	x86_64 aarch64
%endif

Summary:	Data Acquisition Library
Name:		daq
Version:	2.0.6
Release:	14%{?dist}
# sfbpf is BSD (various versions)
License:	GPLv2 and BSD
URL:		https://www.snort.org
Source0:	https://www.snort.org/downloads/snort/%{upstream_name}-%{version}.tar.gz

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	libtool
BuildRequires:	libdnet-devel
BuildRequires:	libnetfilter_queue-devel
BuildRequires:	libpcap-devel
BuildRequires: make

# handle license on el{6,7}: global must be defined after the License field above
%{!?_licensedir: %global license %doc}


%description
Snort 2.9 introduces the DAQ, or Data Acquisition library, for packet I/O.  The
DAQ replaces direct calls to libpcap functions with an abstraction layer that
facilitates operation on a variety of hardware and software interfaces without
requiring changes to Snort.


%package modules
Summary:	Dynamic DAQ modules

%description modules
Dynamic DAQ modules.


%package devel
Summary:	Development libraries and headers for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Development libraries and headers for %{name}.


%prep
%autosetup -n %{upstream_name}-%{version}
autoreconf -ivf -Wobsolete


%build
%{configure} --enable-static=no
# get rid of rpath
%{__sed} -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
%{__sed} -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%{__make}


%install
%{make_install}
# get rid of la files
find $RPM_BUILD_ROOT -type f -name "*.la" -delete -print
# get rid of static libraries
find $RPM_BUILD_ROOT -type f -name "*.a" -delete -print


%ldconfig_scriptlets


%files
%{_libdir}/libdaq.so.2
%{_libdir}/libdaq.so.2.0.4
%{_libdir}/libsfbpf.so.0
%{_libdir}/libsfbpf.so.0.0.1
%doc ChangeLog README
%license COPYING


%files devel
%{_bindir}/daq-modules-config
%{_includedir}/daq.h
%{_includedir}/daq_api.h
%{_includedir}/daq_common.h
%{_includedir}/sfbpf.h
%{_includedir}/sfbpf_dlt.h
%{_libdir}/libdaq.so
%{_libdir}/libsfbpf.so


%files modules
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/daq_afpacket.so
%{_libdir}/%{name}/daq_dump.so
%{_libdir}/%{name}/daq_nfq.so
%{_libdir}/%{name}/daq_ipfw.so
%{_libdir}/%{name}/daq_pcap.so
%license COPYING


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Nov 12 2016 Marcin Dulak <Marcin.Dulak@gmail.com> - 2.0.6-1
- initial version, based on Lawrence R. Rogers's daq.spec from forensics.cert.org
