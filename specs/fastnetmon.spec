%global  fastnetmon_attackdir      %{_localstatedir}/log/fastnetmon_attacks
%global  fastnetmon_user           fastnetmon
%global  fastnetmon_group          %{fastnetmon_user}
%global  fastnetmon_config_path    %{_sysconfdir}/fastnetmon.conf

# We use commit version as we're still in progress of testing FastNetMon on Fedora.
# We're planning to cut next stable release in next few weeks
%global  commit0 420e7b873253fdc1b52b517d9c28db39bf384427
%global  shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global  date 20220528

Name:              fastnetmon
Version:           1.2.1
Release:           21.%{date}git%{shortcommit0}%{?dist}

Summary:           DDoS detection tool with sFlow, Netflow, IPFIX and port mirror support
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:           GPL-2.0-only
URL:               https://fastnetmon.com

Source0:           https://github.com/pavel-odintsov/fastnetmon/archive/%{commit0}.tar.gz
Source1:           fastnetmon.sysusers
# https://github.com/pavel-odintsov/fastnetmon/pull/968
# Adding missing header for g++13
Patch0:            fastnetmon-pr968-g++13-header.patch

BuildRequires:     make
BuildRequires:     gcc
BuildRequires:     gcc-c++
BuildRequires:     boost-devel
BuildRequires:     log4cpp-devel
BuildRequires:     ncurses-devel
BuildRequires:     boost-thread
BuildRequires:     boost-regex
BuildRequires:     libpcap-devel
BuildRequires:     gpm-devel
BuildRequires:     cmake
BuildRequires:     capnproto-devel
BuildRequires:     capnproto
BuildRequires:     grpc-devel
BuildRequires:     grpc-cpp
BuildRequires:     abseil-cpp-devel
BuildRequires:     grpc-plugins
BuildRequires:     mongo-c-driver-devel
BuildRequires:     json-c-devel
BuildRequires:     systemd
BuildRequires:     systemd-rpm-macros

Requires(pre):     shadow-utils

%{?systemd_requires}

%description
DDoS detection tool with sFlow, Netflow, IPFIX and port mirror support.

%prep
%autosetup -n %{name}-%{commit0} -p1

%build
# https://fedoraproject.org/wiki/Changes/OpensslDeprecateEngine
# https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/H3OOWA43BGEBTSM2GRBYDN3SLUTETFL5/
CXXFLAGS="${CXXFLAGS} -DOPENSSL_NO_ENGINE"

%cmake -DENABLE_CUSTOM_BOOST_BUILD=FALSE -DDO_NOT_USE_SYSTEM_LIBRARIES_FOR_BUILD=FALSE -DCMAKE_SKIP_BUILD_RPATH=TRUE -DLINK_WITH_ABSL=TRUE -S src

%cmake_build

%install
# install systemd unit file
install -p -D -m 0644 src/packaging/fedora/fastnetmon.service %{buildroot}%{_unitdir}/fastnetmon.service

# install daemon binary
install -p -D -m 0755 %__cmake_builddir/fastnetmon %{buildroot}%{_sbindir}/fastnetmon

# install client binary 
install -p -D -m 0755 %__cmake_builddir/fastnetmon_client %{buildroot}%{_bindir}/fastnetmon_client

# install api client binary
install -p -D -m 0755 %__cmake_builddir/fastnetmon_api_client %{buildroot}%{_bindir}/fastnetmon_api_client

# install config
install -p -D -m 0644 src/fastnetmon.conf %{buildroot}%{fastnetmon_config_path}

# Create log folder
install -p -d -m 0700 %{buildroot}%{fastnetmon_attackdir}

# Create sysuser manifest to create dynamic user for us
install -D -p -m 0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/fastnetmon.conf

%pre
%sysusers_create_compat %{SOURCE1}

%post
%systemd_post fastnetmon.service

%preun
%systemd_preun fastnetmon.service

%postun
%systemd_postun_with_restart fastnetmon.service 

%files

%{_unitdir}/fastnetmon.service

%{_sysusersdir}/fastnetmon.conf

# Binary daemon
%{_sbindir}/fastnetmon
%{_bindir}/fastnetmon_client
%{_bindir}/fastnetmon_api_client

%config(noreplace) %{fastnetmon_config_path}
%attr(700,%{fastnetmon_user},%{fastnetmon_group}) %dir %{fastnetmon_attackdir}

%license LICENSE
%doc README.md SECURITY.md THANKS.md

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-21.20220528git420e7b8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Aug 25 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 1.2.1-20.20220528git420e7b8
- Rebuilt for abseil-cpp-20240722.0

* Sat Aug 17 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 1.2.1-19.20220528git420e7b8
- Disable deprecated-in-Fedora OpenSSL engine support in Boost.Asio

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 1.2.1-18.20220528git420e7b8
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-17.20220528git420e7b8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Feb 04 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 1.2.1-16.20220528git420e7b8
- Rebuilt for abseil-cpp-20240116.0

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-15.20220528git420e7b8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-14.20220528git420e7b8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 17 2024 Jonathan Wakely <jwakely@redhat.com> - 1.2.1-13.20220528git420e7b8
- Rebuilt for Boost 1.83

* Sat Sep 16 2023 Benjamin A. Beasley <code@musicinmybrain.net> - 1.2.1-12.20220528git420e7b8
- Bump the release number to keep F40 from downgrading F39

* Fri Sep 08 2023 Neal Gompa <ngompa@fedoraproject.org> - 1.2.1-11.20220528git420e7b8
- Rebuild for capnproto 1.0.1

* Wed Aug 30 2023 Benjamin A. Beasley <code@musicinmybrain.net> - 1.2.1-10.20220528git420e7b8
- Rebuilt for abseil-cpp 20230802.0

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-9.20220528git420e7b8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 22 2023 Benjamin A. Beasley <code@musicinmybrain.net> - 1.2.1-8.20220528git420e7b8
- Rebuilt for abseil-cpp 20230125.1

* Tue Feb 28 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.1-7.20220528git420e7b8
- Add missing header for g++13

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-6.20220528git420e7b8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec 02 2022 Fabio Valentini <decathorpe@gmail.com> - 1.2.1-5.20220528git420e7b8
- Rebuild for capnproto 0.10.3 / CVE-2022-46149

* Tue Nov 29 2022 Neal Gompa <ngompa@fedoraproject.org> - 1.2.1-4.20220528git420e7b8
- Rebuild for capnproto 0.10.2

* Tue Aug 23 2022 Benjamin A. Beasley <code@musicinmybrain.net> - 1.2.1-3.20220528git420e7b8
- Rebuilt for abseil-cpp 20220623.0 and grpc 1.48.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2.20220528git420e7b8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat May 28 2022 Pavel Odintsov <pavel.odintsov@gmail.com> - 1.2.1-1.20220528git420e7b8
- First RPM package release

