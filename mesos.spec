%global skiptests   1
%global mesos_user mesos
%global mesos_group mesos

Name:    mesos
Version: 1.8.1
Release: 11%{?dist}
Summary: Cluster manager for sharing distributed application frameworks
# The entire source code is ASL 2.0 except:
# - ConcurrentQueue: Dual licensed with BSD License (two clause) and 
#   Boost Software License Version 1.0.
# - GoogleTest: BSD License (no advertising)
License: ASL 2.0 and BSD and Boost
URL:     http://mesos.apache.org/

ExclusiveArch: x86_64

Source0: %{name}-%{version}-clean.tar.gz
# The upstream Apache Mesos source release
# https://dist.apache.org/repos/dist/release/mesos/<version>/mesos-<version>.tar.gz
# contains non-free code that we cannot ship. Therefore we use
# this script to remove the non-free code before shipping it.
# Download the upstream tarball and invoke this script while in the
# tarball's directory:
# Usage: sh mesos-generate-tarball.sh MAJOR.MINOR.PATCH
# Usage example: sh mesos-generate-tarball.sh 1.8.1
Source1: %{name}-tmpfiles.conf
Source2: %{name}-master.service
Source3: %{name}-slave.service
Source4: %{name}-master
Source5: %{name}-slave
Source6: %{name}
Source7: %{name}-init-wrapper
Source8: mesos-generate-tarball.sh

Patch0:  nobundled-integ.patch
Patch1:  disable-nvml-isolator.patch

BuildRequires: make
BuildRequires: apache-resource-bundles
BuildRequires: apr-devel
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: boost-devel
BuildRequires: codehaus-parent
BuildRequires: cyrus-sasl-devel
BuildRequires: cyrus-sasl-md5
BuildRequires: elfio-devel
BuildRequires: exec-maven-plugin
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: gflags-devel
BuildRequires: glog-devel
BuildRequires: gmock-devel
BuildRequires: grpc-devel  
BuildRequires: grpc-plugins
BuildRequires: gtest-devel
BuildRequires: http-parser-devel
BuildRequires: java-devel
BuildRequires: leveldb-devel
BuildRequires: libarchive-devel
BuildRequires: libcurl-devel
BuildRequires: libev-devel
BuildRequires: libevent-devel
BuildRequires: libev-source
BuildRequires: libtool
BuildRequires: maven-clean-plugin
BuildRequires: maven-dependency-plugin
BuildRequires: maven-local
BuildRequires: maven-plugin-build-helper
BuildRequires: maven-plugin-bundle
BuildRequires: maven-remote-resources-plugin
BuildRequires: maven-shade-plugin
BuildRequires: maven-source-plugin
BuildRequires: maven-wagon
BuildRequires: mojo-parent
BuildRequires: openssl-devel
BuildRequires: picojson-devel
BuildRequires: protobuf-devel
BuildRequires: protobuf-java
BuildRequires: python3-devel
BuildRequires: rapidjson-devel
BuildRequires: subversion-devel
BuildRequires: systemd
BuildRequires: systemd-rpm-macros
BuildRequires: which
BuildRequires: xfsprogs-devel
BuildRequires: zlib-devel
BuildRequires: zookeeper-devel

Requires: cyrus-sasl-md5
Requires: docker
Requires: ntpdate

Requires(pre): shadow-utils

# https://github.com/cameron314/concurrentqueue
Provides: bundled(concurrentqueue) = 7b69a8f
# Container Storage Interface (CSI) Specification
# https://github.com/container-storage-interface/spec/releases
Provides: bundled(csi-spec) = 1.1.0

%description
Apache Mesos is a cluster manager that provides efficient resource isolation and
sharing across distributed applications, or frameworks. It can run Hadoop, MPI, 
Hypertable, Spark, and other applications on a dynamically shared pool of nodes.

%package -n mesos-devel
Summary:  Mesos developer package
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n mesos-devel
This package provides files for developing Apache Mesos frameworks/modules.

%prep
%autosetup -p1

# - Google Test is used in build time for testing. This library is not bundled
#   in this package.
# - Nvidia GPU deployment kit nvml.h header file. Not bundled in this package
#   only for building time.

cd 3rdparty
tar xzf concurrentqueue-7b69a8f.tar.gz
tar xzf googletest-release-1.8.0.tar.gz
cd ..

%build
export MAVEN_HOME=/usr/share/xmvn
%pom_remove_plugin :maven-gpg-plugin src/java/mesos.pom.in

autoreconf -vfi
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:`pwd`/src/.libs:`pwd`/3rdparty/libprocess/
%configure \
    --disable-bundled \
    --with-concurrentqueue=${PWD}/3rdparty/concurrentqueue-7b69a8f \
    --with-gmock=${PWD}/3rdparty/googletest-release-1.8.0/googlemock \
    --with-libprocess=${PWD}/3rdparty/libprocess/include \
    --with-stout=${PWD}/3rdparty/stout/include \
    --with-nvml=${PWD}/3rdparty/nvml-352.79 \
    --enable-optimize \
    --enable-install-module-dependencies \
    --enable-launcher-sealing \
    --enable-libevent \
    --enable-ssl \
    --enable-hardening \
    --disable-use-nvml \
    --disable-python

# Python build will be enabled when is ready this issue:
# https://issues.apache.org/jira/browse/MESOS-8882

%make_build V=1

%check
# Skipping tests, possible mock issues 
%if ! %skiptests
  export LD_LIBRARY_PATH=`pwd`/src/.libs
  make check
%endif

%install

%make_install
# fedora guidelines no .a|.la
find %{buildroot} -name '*.a' -o -name '*.la' -delete

# Remove help scripts based on Python2
rm -f %{buildroot}%{_bindir}/mesos-cat
rm -f %{buildroot}%{_bindir}/mesos-ps
rm -f %{buildroot}%{_bindir}/mesos-scp
rm -f %{buildroot}%{_bindir}/mesos-tail

mkdir -p -m0755 %{buildroot}%{_bindir}
mkdir -p -m0755 %{buildroot}%{_sysconfdir}/default
mkdir -p -m0755 %{buildroot}%{_sysconfdir}/%{name}
mkdir -p -m0755 %{buildroot}%{_sysconfdir}/%{name}-master
mkdir -p -m0755 %{buildroot}%{_sysconfdir}/%{name}-agent
mkdir -p -m0755 %{buildroot}%{_tmpfilesdir}
mkdir -p -m0755 %{buildroot}/%{_localstatedir}/log/%{name}
mkdir -p -m0755 %{buildroot}/%{_sharedstatedir}/%{name}
mkdir -p -m0755 %{buildroot}%{_unitdir}/
mkdir -p -m0755 %{buildroot}%{_datadir}/java

echo zk://localhost:2181/mesos > %{buildroot}%{_sysconfdir}/mesos/zk
echo %{_var}/lib/%{name}       > %{buildroot}%{_sysconfdir}/mesos-master/work_dir
echo %{_var}/lib/%{name}       > %{buildroot}%{_sysconfdir}/mesos-agent/work_dir
echo 1                         > %{buildroot}%{_sysconfdir}/mesos-master/quorum

install -p -m 0755 %{SOURCE7} %{buildroot}%{_bindir}/
install -p -m 0644 %{SOURCE4} %{SOURCE5} %{SOURCE6} %{buildroot}%{_sysconfdir}/default
install -p -m 0644 %{SOURCE1} %{buildroot}%{_tmpfilesdir}/%{name}.conf
install -p -m 0644 %{SOURCE2} %{SOURCE3} %{buildroot}%{_unitdir}/
install -p -m 0644 src/java/target/mesos-*.jar %{buildroot}%{_datadir}/java/

make clean
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -raf src/examples/ %{buildroot}%{_datadir}/%{name}

# Remove examples based on Python2
find %{buildroot} -name '*.py' -delete

# Some files got mangling shebang, we fix them after everything else is done
for i in $(find %{buildroot} -type f -exec grep -Iq . {} \; -print);do
    for j in $(grep -l '^#!/usr/bin/env bash' $i);do 
        pathfix.py -pni "/usr/bin/bash" $j
    done
done

# remove shebang as in other template files.
sed -i 1d %{buildroot}/%{_sysconfdir}/%{name}/mesos-deploy-env.sh.template 

# remove zero length files
find %{buildroot} -size 0 -delete

# remove build time templates
find %{buildroot} -name '*.in' -delete

%files
%license LICENSE
%doc NOTICE
%{_libdir}/*.so
%{_libdir}/%{name}/modules/*.so
%{_bindir}/mesos*
%{_sbindir}/mesos-*
%{_datadir}/%{name}/
%exclude %{_datadir}/%{name}/examples
%{_libexecdir}/%{name}/
%{_tmpfilesdir}/%{name}.conf
%attr(0755,%{mesos_user},%{mesos_group}) %{_var}/log/%{name}/
%attr(0755,%{mesos_user},%{mesos_group}) %{_var}/lib/%{name}/
%config(noreplace) %{_sysconfdir}/%{name}*
%config(noreplace) %{_sysconfdir}/default/%{name}*
%{_unitdir}/%{name}*.service

%files devel
%{_includedir}/%{name}
%{_includedir}/stout
%{_includedir}/process
%{_includedir}/csi
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/java/%{name}-*.jar
%{_datadir}/%{name}/examples/*

%pre
getent group %{mesos_group} >/dev/null || groupadd -r %{mesos_group}
getent passwd %{mesos_user} >/dev/null || \
    useradd -r -g %{mesos_group} -d %{_sharedstatedir}/%{name} -s /sbin/nologin \
    -c "%{name} daemon account" %{mesos_user}
exit 0

%post
%systemd_post %{name}-slave.service %{name}-master.service

%preun
%systemd_preun %{name}-slave.service %{name}-master.service

%postun
%systemd_postun_with_restart %{name}-slave.service %{name}-master.service

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 27 2019 Javi Roman <javiroman@apache.org> - 1.8.1-5
- Properly named mesos-generate-tarball ouput, and updated comment
  for noticing non-free code.

* Thu Sep 26 2019 Javi Roman <javiroman@apache.org> - 1.8.1-4
- Patent code sanity clean up with mesos-generate-tarball.sh helper

* Wed Sep 25 2019 Javi Roman <javiroman@apache.org> - 1.8.1-3
- Disable nvml.h usage according MESOS-9978

* Tue Sep 24 2019 Javi Roman <javiroman@apache.org> - 1.8.1-2
- Remove obsolete maven plugins: site and pgp

* Sat Sep 21 2019 Javi Roman <javiroman@apache.org> - 1.8.1-1
- Rebuilt for latest release, and rebooting the package with Apache Mesos
  Release based on ASF's official release infrastructure.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.0-0.4ce5475.11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 0.23.0-0.4ce5475.10
- Rebuilt for switch to libxcrypt
