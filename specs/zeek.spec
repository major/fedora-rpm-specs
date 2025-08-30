%if 0%{?el8}
%undefine __cmake_in_source_build
%endif

%global binpac_so_majver 0
%global binpac_soversion 0.61
# yes, I know this is very nonsensical
%global broker_so_majver 4
%global broker_soversion 2.6

Name:           zeek
Version:        6.0.4
Release:        %autorelease
Summary:        Powerful framework for network analysis and security monitoring

License:        BSD-3-Clause AND Apache-2.0 AND BSL-1.0 AND ISC AND LGPL-3.0-or-later AND MIT AND NCSA 
URL:            https://zeek.org
Source:         https://download.zeek.org/%{name}-%{version}.tar.gz
Source:         %{name}.sysusers
Requires:       zeek-core%{?_isa} = %{version}-%{release}
Requires:       zeek-zkg%{?_isa} = %{version}-%{release}

BuildRequires:  bison
BuildRequires:  chrpath
BuildRequires:  cmake
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  gperftools-devel
BuildRequires:  jemalloc-devel
BuildRequires:  krb5-devel
BuildRequires:  libmaxminddb-devel
BuildRequires:  libpcap-devel
BuildRequires:  openssl-devel
BuildRequires:  python3-devel
BuildRequires:  readline-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  swig
BuildRequires:  zlib-devel
Provides: bundled(bifcl)
Provides: bundled(binpac)
Provides: bundled(broker)
Provides: bundled(btest)
Provides: bundled(genzam)
Provides: bundled(highwayhash)
Provides: bundled(libkqueue)
Provides: bundled(netcontrol-connectors)
Provides: bundled(package-manager)
Provides: bundled(paraglob)
Provides: bundled(rapidjson)
Provides: bundled(zeek-archiver)
Provides: bundled(zeek-aux)
Provides: bundled(zeekctl)
Provides: bundled(paraglob)

%global _description %{expand:
Zeek is a powerful network analysis framework that is much different from the
typical IDS you may know.  While focusing on network security monitoring, Zeek
provides a comprehensive platform for more general network traffic analysis as
well. Well grounded in more than 15 years of research, Zeek has successfully
bridged the traditional gap between academia and operations since its
inception. Today, it is relied upon operationally in particular by many
scientific environments for securing their cyberinfrastructure. Zeek's user
community includes major universities, research labs, supercomputing centers,
and open-science communities.}

%description %{_description}

%package -n zeek-core
Summary:        The core zeek installation without zeekctl
Requires:   systemd

%description -n zeek-core %{_description}

%package -n zeek-devel
Summary:        Development files for Zeek
Requires:       libbroker-devel%{?_isa} = %{version}-%{release}
Requires:       libpcap-devel
Requires:       openssl-devel
Requires:       zlib-devel

%description -n zeek-devel %{_description}
Development files for Zeek; these files are needed when building binary packages
for Zeek.

%package -n libbroker
Summary:        Zeek's Messaging Library

%description -n libbroker
The Broker library implements Zeek's high-level communication patterns.

%package -n libbroker-devel
Summary:        Development files for Zeek's Messaging Library

%description -n libbroker-devel
The Broker library implements Zeek's high-level communication patterns. This
package bundles the library files and headers that were used during the Zeek
build process; they may be needed when building packages for Zeek.

%package -n     libbinpac
Summary:        Zeek binpac library

%description -n libbinpac
Zeek binpac library

%package -n zeekctl
Summary:        Zeek Control
Requires:       python3
Requires:       zeek-core%{?_isa} = %{version}-%{release}

%description -n zeekctl
ZeekControl is Zeek's interactive shell for operating Zeek installations.

%package zkg
Summary:       The Zeek Package Manager
Requires:      python3
Requires:      zeek-core%{?_isa} = %{version}-%{release}
Requires:      zeekctl%{?_isa} = %{version}-%{release}
Requires:      zeek-btest%{?_isa} = %{version}-%{release}

%description zkg
Zkg is Zeek's package manager.

%package btest
Summary:       The BTest test framework
Requires:      python3
Requires:      zeek-btest-data = %{version}-%{release}

%description btest
A Generic Driver for Powerful System Tests

%package btest-data
Summary:       Data for testing
BuildArch:     noarch

%description btest-data
This package contains test data in the form of pcaps that can he helpful when
writing btests.


%prep
%autosetup -p1
for f in \
  .cmake-format.json \
  .pre-commit-config.yaml \
; do
  find . -name $f -delete
done

%build
%cmake \
  -DZEEK_ETC_INSTALL_DIR=%{_sysconfdir}/%{name} \
  -DZEEK_LOCAL_STATE_DIR=%{_localstatedir}/lib/%{name} \
  -DDISABLE_SPICY=ON \
  -DINSTALL_BTEST=ON \
  -DINSTALL_BTEST_PCAPS=ON \
  -DINSTALL_ZEEK_ARCHIVER=ON \
  -DINSTALL_ZEEK_CLIENT=OFF \
  -DINSTALL_AUX_TOOLS=ON \
  -DINSTALL_ZEEKCTL=ON \
  -DINSTALL_ZKG=ON \
  -DZEEK_SPOOL_DIR=%{_localstatedir}/log/%{name}/spool \
  -DZEEK_LOG_DIR=%{_localstatedir}/log/%{name}/logs
%cmake_build

%install
%cmake_install
mkdir -p %{buildroot}%{_libdir}/zeek/plugins/packages
mkdir -p %{buildroot}%{_datadir}/zeek/site/packages
mkdir -p %{buildroot}%{_localstatedir}/log/zeek/spool
mkdir -p %{buildroot}%{_localstatedir}/log/zeek/logs
rm %{buildroot}%{_datadir}/zeekctl/scripts/zeekctl-config.sh
rm %{buildroot}%{_libdir}/{broctl,libparaglob.a}
install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/zeek.conf

for f in \
  %{buildroot}%{_bindir}/{bifcl,binpac,broker-benchmark,capstats,gen-zam,paraglob-test,zeek{,-archiver}} \
  %{buildroot}%{_libdir}/libbinpac.so.%{binpac_soversion} \
  %{buildroot}%{_libdir}/libbroker.so.%{broker_soversion} \
; do
  chrpath --delete ${f}
done

for f in \
  zeek/python/_SubnetTree.so \
  zeek/python/broker/_broker.so \
; do
  chrpath --delete %{buildroot}%{_libdir}/${f}
done

%files -n zeek-core
%license COPYING COPYING-3rdparty
%doc NEWS README
%dir %{_datadir}/zeek
%dir %{_libdir}/zeek
%dir %{_libdir}/zeek/plugins
%{_bindir}/zeek
%{_bindir}/zeek-archiver
%{_bindir}/zeek-cut
%{_bindir}/paraglob-test
%{_bindir}/broker-benchmark
%{_datadir}/zeek/base
%{_datadir}/zeek/builtin-plugins
%{_datadir}/zeek/policy
%{_datadir}/zeek/zeekygen
%{_datadir}/zeek/test-all-policy.zeek
%{_mandir}/man1/zeek-cut.1*
%{_mandir}/man8/zeek.8*
%{_sysusersdir}/zeek.conf
%defattr(0664,root,zeek,2775)
%dir %{_datadir}/zeek/site
%dir %{_localstatedir}/log/zeek
%dir %{_localstatedir}/log/zeek/spool
%dir %{_localstatedir}/log/zeek/logs
%{_datadir}/zeek/site/local.zeek

%files -n libbroker
%license COPYING COPYING-3rdparty
%{_libdir}/libbroker.so.%{broker_so_majver}
%{_libdir}/libbroker.so.%{broker_soversion}

%files -n libbinpac
%license COPYING COPYING-3rdparty
%{_libdir}/libbinpac.so.%{binpac_so_majver}
%{_libdir}/libbinpac.so.%{binpac_soversion}

%files -n zeekctl
%dir %{_datadir}/zeek
%dir %{_libdir}/zeek/python
%{_bindir}/zeekctl
%{_bindir}/capstats
%{_bindir}/trace-summary
%{_datadir}/zeekctl
%{_datadir}/zeek/zeekctl
%{_libdir}/zeek/python/*Subnet*
%{_libdir}/zeek/python/zeekctl
%{_libdir}/zeek/python/broker
%{_mandir}/man8/zeekctl.8*
%{_mandir}/man1/trace-summary.1*
%defattr(0664,root,zeek,2775)
%dir %{_sysconfdir}/zeek
%config(noreplace) %{_sysconfdir}/zeek/*.cfg
%{_localstatedir}/log/zeek/spool/zeekctl-config.sh


%files devel
%dir %{_datadir}/zeek
%{_bindir}/bifcl
%{_bindir}/binpac
%{_bindir}/gen-zam
%{_bindir}/zeek-config
%{_includedir}/binpac
%{_includedir}/zeek
%{_includedir}/paraglob
%{_libdir}/libbinpac.so
%{_datadir}/zeek/cmake

%files -n libbroker-devel
%{_includedir}/broker
%{_libdir}/cmake/Broker
%{_libdir}/libbroker.so

%files zkg
%{_bindir}/zkg
%dir %{_sysconfdir}/zeek/zkg
%config(noreplace) %{_sysconfdir}/zeek/zkg/config
%{_libdir}/zeek/python/zeekpkg
%{_mandir}/man1/zkg.1*
%dir %{_libdir}/zeek/plugins
%dir %{_libdir}/zeek/plugins/packages
%dir %{_libdir}/zeek/python
%dir %{_datadir}/zeek
%defattr(0664,root,zeek,2775)
%dir %{_datadir}/zeek/site
%dir %{_datadir}/zeek/site/packages

%files btest
%dir %{_libdir}/zeek/python
%dir %{_datadir}/btest
%{_bindir}/btest
%{_bindir}/btest-*
%{_libdir}/zeek/python/btest-*
%{_datadir}/btest/scripts

%files btest-data
%license COPYING COPYING-3rdparty
%dir %{_datadir}/btest
%{_datadir}/btest/data

%changelog
%autochangelog
