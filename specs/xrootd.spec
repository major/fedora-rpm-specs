%if %{?fedora}%{!?fedora:0}
%ifarch %{ix86} %{arm}
%global ceph 0
%else
%global ceph 1
%endif
%else
%global ceph 0
%endif

# Needed for EPEL 8
%undefine __cmake_in_source_build

Name:		xrootd
Epoch:		1
Version:	5.7.3
Release:	2%{?dist}
Summary:	Extended ROOT file server
License:	LGPL-3.0-or-later AND BSD-2-Clause AND BSD-3-Clause AND curl AND MIT AND Zlib
URL:		https://xrootd.web.cern.ch
Source0:	%{url}/download/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	make
BuildRequires:	pkgconfig
BuildRequires:	fuse-devel
BuildRequires:	krb5-devel
BuildRequires:	libcurl-devel
BuildRequires:	tinyxml-devel
BuildRequires:	libxml2-devel
BuildRequires:	ncurses-devel
BuildRequires:	openssl-devel
BuildRequires:	perl-generators
BuildRequires:	readline-devel
BuildRequires:	zlib-devel
BuildRequires:	doxygen
BuildRequires:	graphviz
BuildRequires:	selinux-policy-devel
BuildRequires:	systemd-rpm-macros
BuildRequires:	systemd-devel
BuildRequires:	python3-devel
BuildRequires:	python3-pip
BuildRequires:	python3-setuptools
BuildRequires:	python3-wheel
BuildRequires:	python3-sphinx
BuildRequires:	json-c-devel
BuildRequires:	libmacaroons-devel
BuildRequires:	libuuid-devel
BuildRequires:	voms-devel
BuildRequires:	scitokens-cpp-devel
BuildRequires:	davix-devel
BuildRequires:  libxcrypt-devel
%if %{ceph}
BuildRequires:	librados-devel
BuildRequires:	libradosstriper-devel
%endif
%ifnarch %{ix86}
BuildRequires:	isa-l-devel
%endif
BuildRequires:	attr
BuildRequires:	curl
BuildRequires:	davix
BuildRequires:	gtest-devel
BuildRequires:	openssl
BuildRequires:	procps

Requires:	%{name}-server%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}-selinux = %{epoch}:%{version}-%{release}

%description
The Extended root file server consists of a file server called xrootd
and a cluster management server called cmsd.

The xrootd server was developed for the root analysis framework to
serve root files. However, the server is agnostic to file types and
provides POSIX-like access to any type of file.

The cmsd server is the next generation version of the olbd server,
originally developed to cluster and load balance Objectivity/DB AMS
database servers. It provides enhanced capability along with lower
latency and increased throughput.

%package server
Summary:	Xrootd server daemons
Requires:	%{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}-client-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}-server-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	expect
Requires:	logrotate
Requires(pre):	shadow-utils
%{?systemd_requires}

%description server
This package contains the xrootd servers without the SELinux support.
Unless you are installing on a system without SELinux also install the
xrootd-selinux package.

%package selinux
Summary:	SELinux policy module for the xrootd server
BuildArch:	noarch
Requires:	selinux-policy
Requires(post):		policycoreutils
Requires(postun):	policycoreutils

%description selinux
This package contains SELinux policy module for the xrootd server package.

%package libs
Summary:	Libraries used by xrootd servers and clients

%description libs
This package contains libraries used by the xrootd servers and clients.

%package devel
Summary:	Development files for xrootd
Provides:	%{name}-libs-devel = %{epoch}:%{version}-%{release}
Provides:	%{name}-libs-devel%{?_isa} = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-libs-devel < %{epoch}:%{version}-%{release}
Requires:	%{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}

%description devel
This package contains header files and development libraries for xrootd
development.

%package client-libs
Summary:	Libraries used by xrootd clients
Requires:	%{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}

%description client-libs
This package contains libraries used by xrootd clients.

%package client-devel
Summary:	Development files for xrootd clients
Provides:	%{name}-cl-devel = %{epoch}:%{version}-%{release}
Provides:	%{name}-cl-devel%{?_isa} = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-cl-devel < %{epoch}:%{version}-%{release}
Requires:	%{name}-devel%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}-client-libs%{?_isa} = %{epoch}:%{version}-%{release}

%description client-devel
This package contains header files and development libraries for xrootd
client development.

%package server-libs
Summary:	Libraries used by xrootd servers
Requires:	%{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}-client-libs%{?_isa} = %{epoch}:%{version}-%{release}

%description server-libs
This package contains libraries used by xrootd servers.

%package server-devel
Summary:	Development files for xrootd servers
Requires:	%{name}-devel%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}-client-devel%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}-server-libs%{?_isa} = %{epoch}:%{version}-%{release}

%description server-devel
This package contains header files and development libraries for xrootd
server development.

%package private-devel
Summary:	Private xrootd headers
Requires:	%{name}-devel%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}-client-devel%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}-server-devel%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}-client-libs%{?_isa} = %{epoch}:%{version}-%{release}

%description private-devel
This package contains some private xrootd headers. Backward and forward
compatibility between versions is not guaranteed for these headers.

%package client
Summary:	Xrootd command line client tools
Provides:	%{name}-cl = %{epoch}:%{version}-%{release}
Provides:	%{name}-cl%{?_isa} = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-cl < %{epoch}:%{version}-%{release}
Requires:	%{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}-client-libs%{?_isa} = %{epoch}:%{version}-%{release}

%description client
This package contains the command line tools used to communicate with
xrootd servers.

%package fuse
Summary:	Xrootd FUSE tool
Requires:	%{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}-client-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	fuse

%description fuse
This package contains the FUSE (file system in user space) xrootd mount
tool.

%package voms
Summary:	VOMS attribute extractor plugin for XRootD
Provides:	vomsxrd = %{epoch}:%{version}-%{release}
Provides:	%{name}-voms-plugin = %{epoch}:%{version}-%{release}
Provides:	xrdhttpvoms = %{epoch}:%{version}-%{release}
Obsoletes:	vomsxrd < 1:0.6.0-4
Obsoletes:	%{name}-voms-plugin < 1:0.6.0-3
Obsoletes:	xrdhttpvoms < 0.2.5-9
Requires:	%{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}

%description voms
The VOMS attribute extractor plugin for XRootD.

%package scitokens
Summary:	SciTokens authorization support for XRootD
License:	Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause
Requires:	%{name}-server%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}

%description scitokens
This ACC (authorization) plugin for the XRootD framework utilizes the
SciTokens library to validate and extract authorization claims from a
SciToken passed during a transfer. Configured appropriately, this
allows the XRootD server admin to delegate authorization decisions for
a subset of the namespace to an external issuer.

%package -n xrdcl-http
Summary:	HTTP client plugin for XRootD
Requires:	%{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}-client-libs%{?_isa} = %{epoch}:%{version}-%{release}

%description -n xrdcl-http
xrdcl-http is an XRootD client plugin which allows XRootD to interact
with HTTP repositories.

%if %{ceph}
%package ceph
Summary:	XRootD plugin for interfacing with the Ceph storage platform
Requires:	%{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}

%description ceph
The xrootd-ceph is an OSS layer plugin for the XRootD server for
interfacing with the Ceph storage platform.
%endif

%package -n python3-%{name}
Summary:	Python 3 bindings for xrootd
%py_provides	python3-%{name}
Requires:	%{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}-client-libs%{?_isa} = %{epoch}:%{version}-%{release}

%description -n python3-%{name}
This package contains Python 3 bindings for xrootd.

%package doc
Summary:	Developer documentation for the xrootd libraries
BuildArch:	noarch

%description doc
This package contains the API documentation of the xrootd libraries.

%prep
%setup -q

%build
%cmake \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DFORCE_ENABLED:BOOL=ON \
    -DENABLE_TESTS:BOOL=ON \
%if %{ceph}
    -DENABLE_CEPH:BOOL=ON \
%endif
%ifarch %{ix86}
    -DENABLE_XRDEC:BOOL=OFF \
%endif
%if %{?fedora}%{!?fedora:0} || %{?rhel}%{!?rhel:0} >= 9
    -DPIP_OPTIONS="--no-deps --use-pep517 --no-build-isolation --disable-pip-version-check --verbose" \
%else
    -DPIP_OPTIONS="--no-deps --disable-pip-version-check --verbose" \
%endif
    -DXRD_PYTHON_REQ_VERSION=%{python3_version}
%cmake_build

make -C packaging/common -f /usr/share/selinux/devel/Makefile

doxygen Doxyfile
# Use local image instead of remote
sed 's!src=".*/xrootd-logo.png"!src="xrootd-logo.png"!' \
    -i doxydoc/html/index.html
cp -p docs/images/xrootd-logo.png doxydoc/html

%install
%cmake_install

rm -f %{buildroot}%{_libdir}/libXrdCephPosix.so

rm -f %{buildroot}%{_bindir}/xrdshmap

rm -f %{buildroot}%{python3_sitearch}/xrootd-*.*-info/direct_url.json
rm -f %{buildroot}%{python3_sitearch}/xrootd-*.*-info/RECORD
[ -r %{buildroot}%{python3_sitearch}/xrootd-*.*-info/INSTALLER ] && \
    sed s/pip/rpm/ \
    -i %{buildroot}%{python3_sitearch}/xrootd-*.*-info/INSTALLER

LD_LIBRARY_PATH=%{buildroot}%{_libdir} \
PYTHONPATH=%{buildroot}%{python3_sitearch} \
PYTHONDONTWRITEBYTECODE=1 \
make -C bindings/python/docs html

# Service unit files
mkdir -p %{buildroot}%{_unitdir}
install -m 644 packaging/common/xrootd@.service %{buildroot}%{_unitdir}
install -m 644 packaging/common/xrootd@.socket %{buildroot}%{_unitdir}
install -m 644 packaging/common/xrdhttp@.socket %{buildroot}%{_unitdir}
install -m 644 packaging/common/cmsd@.service %{buildroot}%{_unitdir}
install -m 644 packaging/common/frm_xfrd@.service %{buildroot}%{_unitdir}
install -m 644 packaging/common/frm_purged@.service %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_tmpfilesdir}
install -m 644 packaging/rhel/xrootd.tmpfiles %{buildroot}%{_tmpfilesdir}/%{name}.conf

# Server config
mkdir -p %{buildroot}%{_sysconfdir}/%{name}
install -m 644 -p packaging/common/%{name}-clustered.cfg \
    %{buildroot}%{_sysconfdir}/%{name}/%{name}-clustered.cfg
install -m 644 -p packaging/common/%{name}-standalone.cfg \
    %{buildroot}%{_sysconfdir}/%{name}/%{name}-standalone.cfg
install -m 644 -p packaging/common/%{name}-filecache-clustered.cfg \
    %{buildroot}%{_sysconfdir}/%{name}/%{name}-filecache-clustered.cfg
install -m 644 -p packaging/common/%{name}-filecache-standalone.cfg \
    %{buildroot}%{_sysconfdir}/%{name}/%{name}-filecache-standalone.cfg
sed 's!/usr/lib64/!!' packaging/common/%{name}-http.cfg > \
    %{buildroot}%{_sysconfdir}/%{name}/%{name}-http.cfg

# Client config
mkdir -p %{buildroot}%{_sysconfdir}/%{name}/client.plugins.d
install -m 644 -p packaging/common/client.conf \
    %{buildroot}%{_sysconfdir}/%{name}/client.conf
sed 's!/usr/lib/!!' packaging/common/client-plugin.conf.example > \
    %{buildroot}%{_sysconfdir}/%{name}/client.plugins.d/client-plugin.conf.example
sed -e 's!/usr/lib64/!!' -e 's!-5!!' packaging/common/recorder.conf > \
    %{buildroot}%{_sysconfdir}/%{name}/client.plugins.d/recorder.conf
sed 's!/usr/lib64/!!' packaging/common/http.client.conf.example > \
    %{buildroot}%{_sysconfdir}/%{name}/client.plugins.d/xrdcl-http-plugin.conf

chmod 644 %{buildroot}%{_datadir}/%{name}/utils/XrdCmsNotify.pm

sed 's!/usr/bin/env perl!/usr/bin/perl!' -i \
    %{buildroot}%{_datadir}/%{name}/utils/netchk \
    %{buildroot}%{_datadir}/%{name}/utils/XrdCmsNotify.pm \
    %{buildroot}%{_datadir}/%{name}/utils/XrdOlbMonPerf

sed 's!/usr/bin/env bash!/bin/bash!' -i %{buildroot}%{_bindir}/xrootd-config

mkdir -p %{buildroot}%{_sysconfdir}/%{name}/config.d

mkdir -p %{buildroot}%{_localstatedir}/log/%{name}
mkdir -p %{buildroot}%{_localstatedir}/spool/%{name}

mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
install -m 644 -p packaging/common/%{name}.logrotate \
    %{buildroot}%{_sysconfdir}/logrotate.d/%{name}

mkdir -p %{buildroot}%{_datadir}/selinux/packages/%{name}
install -m 644 -p packaging/common/%{name}.pp \
    %{buildroot}%{_datadir}/selinux/packages/%{name}

# Documentation
mkdir -p %{buildroot}%{_pkgdocdir}
cp -pr doxydoc/html %{buildroot}%{_pkgdocdir}

cp -pr bindings/python/docs/build/html %{buildroot}%{_pkgdocdir}/python
rm %{buildroot}%{_pkgdocdir}/python/.buildinfo

%check
# Reduce socket path lengths used during tests
# rpm 4.20 uses a longer path to the build directory than earlier versions
# Tests fail with sockets in the build directory with rpm 4.20
adminpath=$(mktemp -d -p /var/tmp)
sed "s!all.adminpath .*!all.adminpath ${adminpath}!" \
    -i %{_vpath_builddir}/tests/cluster/common.cfg \
       tests/XRootD/common.cfg

touch testfile
if ( setfattr -n user.testattr -v testvalue testfile ) ; then
    %ctest
else
    echo "Extended file attributes not supported by file system"
    echo "Don't run tests that require them"
    exclude="\
XrdCl::FileCopyTest|\
XrdCl::FileSystemTest.PlugInTest|\
XrdCl::FileSystemTest.ServerQueryTest|\
XrdCl::FileSystemTest.XAttrTest|\
XrdCl::FileTest.XAttrTest|\
XrdCl::LocalFileHandlerTest.XAttrTest|\
XrdCl::ThreadingTest|\
XrdCl::WorkflowTest.CheckpointTest|\
XrdCl::WorkflowTest.XAttrWorkflowTest|\
XrdEc::|\
XRootD::cluster::test|\
XRootD::http::test"
    %ctest -- -E $exclude
fi
rm testfile

rm -rf ${adminpath}

%pre server
getent group %{name} >/dev/null || groupadd -r %{name}
getent passwd %{name} >/dev/null || useradd -r -g %{name} -s /sbin/nologin \
  -d %{_localstatedir}/spool/%{name} -c "XRootD runtime user" %{name}

%post server
%tmpfiles_create %{name}.conf

if [ $1 -eq 1 ] ; then
    systemctl daemon-reload >/dev/null 2>&1 || :
fi

%preun server
if [ $1 -eq 0 ] ; then
    for DAEMON in xrootd cmsd frm_purged frm_xfrd; do
	for INSTANCE in `systemctl | grep $DAEMON@ | awk '{print $1;}'`; do
	    systemctl --no-reload disable $INSTANCE > /dev/null 2>&1 || :
	    systemctl stop $INSTANCE > /dev/null 2>&1 || :
	done
    done
fi

%postun server
if [ $1 -ge 1 ] ; then
    systemctl daemon-reload >/dev/null 2>&1 || :
    for DAEMON in xrootd cmsd frm_purged frm_xfrd; do
	for INSTANCE in `systemctl | grep $DAEMON@ | awk '{print $1;}'`; do
	    systemctl try-restart $INSTANCE >/dev/null 2>&1 || :
	done
    done
fi

%post selinux
/usr/sbin/semodule -i %{_datadir}/selinux/packages/%{name}/%{name}.pp >/dev/null 2>&1 || :

%postun selinux
if [ $1 -eq 0 ] ; then
    /usr/sbin/semodule -r %{name} >/dev/null 2>&1 || :
fi

%files
# Empty

%files server
%{_bindir}/cconfig
%{_bindir}/cmsd
%{_bindir}/frm_admin
%{_bindir}/frm_purged
%{_bindir}/frm_xfragent
%{_bindir}/frm_xfrd
%{_bindir}/mpxstats
%{_bindir}/wait41
%{_bindir}/xrdacctest
%{_bindir}/xrdpfc_print
%{_bindir}/xrdpwdadmin
%{_bindir}/xrdsssadmin
%{_bindir}/xrootd
%{_mandir}/man8/cmsd.8*
%{_mandir}/man8/frm_admin.8*
%{_mandir}/man8/frm_purged.8*
%{_mandir}/man8/frm_xfragent.8*
%{_mandir}/man8/frm_xfrd.8*
%{_mandir}/man8/mpxstats.8*
%{_mandir}/man8/xrdpfc_print.8*
%{_mandir}/man8/xrdpwdadmin.8*
%{_mandir}/man8/xrdsssadmin.8*
%{_mandir}/man8/xrootd.8*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/utils
%{_unitdir}/*
%{_tmpfilesdir}/%{name}.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%dir %{_sysconfdir}/%{name}/config.d
%attr(-,xrootd,xrootd) %config(noreplace) %{_sysconfdir}/%{name}/*.cfg
%attr(-,xrootd,xrootd) %{_localstatedir}/log/%{name}
%attr(-,xrootd,xrootd) %{_localstatedir}/spool/%{name}
%ghost %attr(-,xrootd,xrootd) %{_rundir}/%{name}

%files selinux
%dir %{_datadir}/selinux/packages/%{name}
%{_datadir}/selinux/packages/%{name}/%{name}.pp

%files libs
%{_libdir}/libXrdAppUtils.so.*
%{_libdir}/libXrdCrypto.so.*
%{_libdir}/libXrdCryptoLite.so.*
%{_libdir}/libXrdUtils.so.*
%{_libdir}/libXrdXml.so.*
# Plugins
%{_libdir}/libXrdCksCalczcrc32-5.so
%{_libdir}/libXrdCryptossl-5.so
%{_libdir}/libXrdSec-5.so
%{_libdir}/libXrdSecProt-5.so
%{_libdir}/libXrdSecgsi-5.so
%{_libdir}/libXrdSecgsiAUTHZVO-5.so
%{_libdir}/libXrdSecgsiGMAPDN-5.so
%{_libdir}/libXrdSeckrb5-5.so
%{_libdir}/libXrdSecpwd-5.so
%{_libdir}/libXrdSecsss-5.so
%{_libdir}/libXrdSecunix-5.so
%{_libdir}/libXrdSecztn-5.so
%license COPYING* LICENSE

%files devel
%{_bindir}/xrootd-config
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/XProtocol
%{_includedir}/%{name}/Xrd
%{_includedir}/%{name}/XrdCks
%{_includedir}/%{name}/XrdNet
%{_includedir}/%{name}/XrdOuc
%{_includedir}/%{name}/XrdSec
%{_includedir}/%{name}/XrdSys
%{_includedir}/%{name}/XrdXml
%{_includedir}/%{name}/XrdVersion.hh
%{_libdir}/libXrdAppUtils.so
%{_libdir}/libXrdCrypto.so
%{_libdir}/libXrdCryptoLite.so
%{_libdir}/libXrdUtils.so
%{_libdir}/libXrdXml.so
%{_libdir}/cmake/XRootD

%files client-libs
%{_libdir}/libXrdCl.so.*
%ifnarch %{ix86}
%{_libdir}/libXrdEc.so.*
%endif
%{_libdir}/libXrdFfs.so.*
%{_libdir}/libXrdPosix.so.*
%{_libdir}/libXrdPosixPreload.so.*
# This lib may be used for LD_PRELOAD so the .so link needs to be included
%{_libdir}/libXrdPosixPreload.so
%{_libdir}/libXrdSsiLib.so.*
%{_libdir}/libXrdSsiShMap.so.*
# Plugins
%{_libdir}/libXrdClProxyPlugin-5.so
%{_libdir}/libXrdClRecorder-5.so
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/client.conf
%dir %{_sysconfdir}/%{name}/client.plugins.d
%config(noreplace) %{_sysconfdir}/%{name}/client.plugins.d/client-plugin.conf.example
%config(noreplace) %{_sysconfdir}/%{name}/client.plugins.d/recorder.conf

%files client-devel
%{_includedir}/%{name}/XrdCl
%{_includedir}/%{name}/XrdPosix
%{_libdir}/libXrdCl.so
%{_libdir}/libXrdFfs.so
%{_libdir}/libXrdPosix.so

%files server-libs
%{_libdir}/libXrdHttpUtils.so.*
%{_libdir}/libXrdServer.so.*
# Plugins
%{_libdir}/libXrdBlacklistDecision-5.so
%{_libdir}/libXrdBwm-5.so
%{_libdir}/libXrdCmsRedirectLocal-5.so
%{_libdir}/libXrdFileCache-5.so
%{_libdir}/libXrdHttp-5.so
%{_libdir}/libXrdHttpTPC-5.so
%{_libdir}/libXrdMacaroons-5.so
%{_libdir}/libXrdN2No2p-5.so
%{_libdir}/libXrdOfsPrepGPI-5.so
%{_libdir}/libXrdOssCsi-5.so
%{_libdir}/libXrdOssSIgpfsT-5.so
%{_libdir}/libXrdPfc-5.so
%{_libdir}/libXrdPss-5.so
%{_libdir}/libXrdSsi-5.so
%{_libdir}/libXrdSsiLog-5.so
%{_libdir}/libXrdThrottle-5.so
%{_libdir}/libXrdXrootd-5.so

%files server-devel
%{_includedir}/%{name}/XrdAcc
%{_includedir}/%{name}/XrdCms
%{_includedir}/%{name}/XrdHttp
%{_includedir}/%{name}/XrdOfs
%{_includedir}/%{name}/XrdOss
%{_includedir}/%{name}/XrdPfc
%{_includedir}/%{name}/XrdSfs
%{_includedir}/%{name}/XrdXrootd
%{_libdir}/libXrdHttpUtils.so
%{_libdir}/libXrdServer.so

%files private-devel
%{_includedir}/%{name}/private
%ifnarch %{ix86}
%{_libdir}/libXrdEc.so
%endif
%{_libdir}/libXrdSsiLib.so
%{_libdir}/libXrdSsiShMap.so

%files client
%{_bindir}/xrdadler32
%{_bindir}/xrdcks
%{_bindir}/xrdcopy
%{_bindir}/xrdcp
%{_bindir}/xrdcrc32c
%{_bindir}/xrdfs
%{_bindir}/xrdgsiproxy
%{_bindir}/xrdgsitest
%{_bindir}/xrdmapc
%{_bindir}/xrdpinls
%{_bindir}/xrdreplay
%{_mandir}/man1/xrdadler32.1*
%{_mandir}/man1/xrdcopy.1*
%{_mandir}/man1/xrdcp.1*
%{_mandir}/man1/xrdfs.1*
%{_mandir}/man1/xrdgsiproxy.1*
%{_mandir}/man1/xrdgsitest.1*
%{_mandir}/man1/xrdmapc.1*

%files fuse
%{_bindir}/xrootdfs
%{_mandir}/man1/xrootdfs.1*

%files voms
%{_libdir}/libXrdVoms-5.so
%{_libdir}/libXrdHttpVOMS-5.so
%{_libdir}/libXrdSecgsiVOMS-5.so
%doc %{_mandir}/man1/libXrdVoms.1*
%doc %{_mandir}/man1/libXrdSecgsiVOMS.1*
%doc src/XrdVoms/README.md

%files scitokens
%{_libdir}/libXrdAccSciTokens-5.so
%doc src/XrdSciTokens/README.md

%files -n xrdcl-http
%{_libdir}/libXrdClHttp-5.so
%config(noreplace) %{_sysconfdir}/%{name}/client.plugins.d/xrdcl-http-plugin.conf

%if %{ceph}
%files ceph
%{_libdir}/libXrdCeph-5.so
%{_libdir}/libXrdCephXattr-5.so
%{_libdir}/libXrdCephPosix.so.*
%endif

%files -n python3-%{name}
%{python3_sitearch}/xrootd-*.*-info
%{python3_sitearch}/pyxrootd
%{python3_sitearch}/XRootD

%files doc
%doc %{_pkgdocdir}

%changelog
* Sat Feb 01 2025 Björn Esser <besser82@fedoraproject.org> - 1:5.7.3-2
- Add explicit BR: libxcrypt-devel

* Wed Jan 29 2025 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:5.7.3-1
- Update to version 5.7.3
- Drop patches accepted upstream

* Thu Jan 23 2025 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:5.7.2-4
- Use CMAKE_BUILD_TYPE RelWithDebInfo to avoid -Werror in compiler flags

* Sun Jan 19 2025 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:5.7.2-3
- Fix compilation errors with GCC 15

* Sun Dec 08 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:5.7.2-2
- Fix errors in format strings

* Fri Nov 29 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:5.7.2-1
- Update to version 5.7.2
- Drop patches accepted upstream

* Mon Sep 16 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:5.7.1-2
- Workaround doxygen non-reproducibility - make doc package noarch again
- Increase client timeouts for XRootD server tests

* Wed Sep 04 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:5.7.1-1
- Update to version 5.7.1
- Drop patches accepted upstream

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jul 04 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:5.7.0-2
- Fix compilation error due to hidden overloaded virtual
- Make documentation package not noarch due to non-reproducible filenames

* Wed Jul 03 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:5.7.0-1
- Update to version 5.7.0
- Drop patches accepted upstream
- Drop EPEL 7 support from spec file (EOL)

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1:5.6.9-3
- Rebuilt for Python 3.13

* Mon Jun 03 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:5.6.9-2
- Reduce socket path lengths used by tests for rpm 4.20 compatibility
- Avoid test failures due to using the same port numbers in different tests

* Sat Mar 16 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:5.6.9-1
- Update to version 5.6.9

* Sat Feb 24 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:5.6.8-1
- Update to version 5.6.8
- Disable tests that require file attributes if the file system doesn't
  support them

* Tue Feb 06 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:5.6.7-1
- Update to version 5.6.7

* Fri Jan 26 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:5.6.6-1
- Update to version 5.6.6

* Mon Jan 22 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:5.6.5-1
- Update to version 5.6.5
- Drop patches accepted upstream

* Wed Jan 17 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:5.6.4-2
- Fix printf null pointer error

* Mon Dec 11 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:5.6.4-1
- Update to version 5.6.4
- Drop patches accepted upstream or previously backported

* Tue Dec 05 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:5.6.3-3
- Avoid /tmp when running some tests
- Fail gracefully in case of unsupported extended file attributes
- Avoid null bytes in error message strings
- Fix include path in XRootDConfig.cmake
- Avoid dereferencing unaligned pointers
- Support big endian in XrdZip

* Sun Nov 19 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:5.6.3-2
- Enable erasure code support (XrdEc)

* Fri Oct 27 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:5.6.3-1
- Update to version 5.6.3
- Drop patches accepted upstream or previously backported
- Enable tests and add check section

* Mon Sep 18 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:5.6.2-2
- Backport fix for Authfile parsing regression

* Fri Sep 15 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:5.6.2-1
- Update to version 5.6.2

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 12 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:5.6.1-1
- Update to version 5.6.1
- Add --use-pep517 --no-build-isolation to pip options for Fedora and EPEL 9+

* Sun Jul 02 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:5.6.0-1
- Update to version 5.6.0
- Drop patches (changes implemented upstream)

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 1:5.5.5-3
- Rebuilt for Python 3.12

* Sun May 21 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:5.5.5-2
- Fix build failure with latest glibc

* Tue May 09 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:5.5.5-1
- Update to version 5.5.5

* Fri Mar 24 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:5.5.4-1
- Update to version 5.5.4

* Sat Feb 18 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:5.5.3-1
- Update to version 5.5.3

* Thu Feb 09 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:5.5.2-1
- Update to version 5.5.2
- Drop patches accepted upstream or previously backported

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 17 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:5.5.1-2
- Add missing include - fixes build failure with gcc 13
- Fix build failure due to possible large memory allocation

* Wed Oct 19 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:5.5.1-1
- Update to version 5.5.1
- Drop doxygen patch accepted upstream
- Check all sizes (8, 16, 32, 64) in <atomic> check
- Check operator++ in <atomic> check

* Fri Aug 26 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:5.5.0-1
- Update to version 5.5.0
- Drop patches accepted upstream
- Address some warnings from Doxygen
- Build using devtoolset 7 on EPEL 7

* Sun Aug 21 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:5.4.3-4
- Add BR systemd (no longer a dependency of systemd-devel)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 1:5.4.3-2
- Rebuilt for Python 3.11

* Fri Jun 10 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:5.4.3-1
- Update to version 5.4.3
- Drop patches accepted upstream or previously backported
- Add BR python3-pip and python3-wheel

* Sat Apr 23 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:5.4.2-3
- Link with libatomic on some 32-bit architectures
- Fix sphinx doc
- Backport fixes from upstream git master (OpenSSL 3, Python 3.10)

* Sat Mar 19 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:5.4.2-2
- Add BR python3-pip for Fedora 35+

* Fri Mar 04 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:5.4.2-1
- Update to version 5.4.2
- More OpenSSL 3 fixes

* Thu Feb 24 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:5.4.1-1
- Update to version 5.4.1
- Drop patches accepted upstream

* Mon Jan 31 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:5.4.0-5
- Use openssl 3 compatible code on EPEL 9

* Mon Jan 24 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:5.4.0-4
- Fix compiler warnings from gcc 12

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 14 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:5.4.0-2
- Don't use unimplemented regex functions on EPEL 7.
- Add missing include (GNU/Hurd)
- Define ENODATA if not defined (kFreeBSD)

* Fri Dec 10 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:5.4.0-1
- Update to version 5.4.0
- Drop patch accepted upstream: 0001-Do-not-hardcode-error-numbers.patch
- Fix build failure on platforms where char is unsigned
- Fix build failure with regex on EPEL 7

* Tue Nov 30 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:5.3.4-1
- Update to version 5.3.4

* Tue Nov 16 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:5.3.3-1
- Update to version 5.3.3
- Drop patches accepted upstream:
  - 0001-Fix-compilation-failure-on-32-bit-architectures.patch
  - 0001-Fix-build-failure-on-platforms-where-char-is-unsigne.patch

* Tue Nov 02 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:5.3.2-1
- Update to version 5.3.2
- Drop OpenSSL 3 patch accepted upstream
- Fix compilation failure on 32 bit architectures
- Do not hardcode error numbers
- Fix build failure on platforms where char is unsigned

* Sun Sep 26 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:5.3.1-3
- Update code for OpenSSL 3

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1:5.3.1-2
- Rebuilt with OpenSSL 3.0.0

* Thu Jul 29 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:5.3.1-1
- Update to version 5.3.1
- Drop patch xrootd-format.patch (accepted upstream)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 10 2021 Björn Esser <besser82@fedoraproject.org> - 1:5.3.0-2
- Rebuild for versioned symbols in json-c

* Fri Jul 09 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:5.3.0-1
- Update to version 5.3.0

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1:5.2.0-2
- Rebuilt for Python 3.10

* Thu May 20 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:5.2.0-1
- Update to version 5.2.0

* Tue Mar 30 2021 Jonathan Wakely <jwakely@redhat.com> - 1:5.1.1-2
- Rebuilt for removed libstdc++ symbol (#1937698)

* Wed Mar 10 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:5.1.1-1
- Update to version 5.1.1
- Drop patches (accepted upstream)

* Fri Feb 26 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:5.1.0-2
- Remove debug output

* Tue Feb 23 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:5.1.0-1
- Update to version 5.1.0
- Add scitokens plugin package
- Packages xrootd-ceph and xrdcl-http are now built as part of xrootd
  replacing the packages built from separate source rpms
- Drop patches (accepted upstream or previously backported)
- Fix broken library dependency in XrdCeph cmake file
- Fix format error on 32 bit architectures

* Sat Feb 13 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:5.0.3-5
- Drop workaround for false positive warning from gcc 11

* Tue Jan 26 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:5.0.3-4
- Workaround false positive warning from gcc 11 (Fedora 34+)

* Tue Dec 08 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:5.0.3-3
- Fix array length calculation (gcc 11 error)
- Fix uninitialized variable error

* Wed Nov 18 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:5.0.3-2
- Correct plugin version checking to prevent false negatives
- Fix wrong section number in xrootdfs.1 manpage
- Use system tinyxml library (unbundle)

* Thu Nov 12 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:5.0.3-1
- Update to version 5.0.3
- Drop patches (accepted upstream or previously backported)

* Mon Nov 02 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:5.0.2-2
- Fix for XrdPosix failing to compile with glibc 2.33 (2.32.9000)

* Fri Sep 18 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:5.0.2-1
- Update to version 5.0.2
- Drop patches (accepted upstream or previously backported)
- Obsolete xrdhttpvoms in xrootd-voms package

* Thu Aug 27 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:5.0.1-1
- Update to version 5.0.1
- Remove conditionals for building on EPEL 6
- Drop patches (accepted upstream or previously backported)
- Fix 32 bit compilation (format error)
- Fix compilation on ARM, PPC and S390X (char is unsigned)

* Wed Aug 26 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.12.3-5
- Use new CMake macros where available
- Backport minor fixes from upstream git
  - Correct flag reset code for ssq monitor option
  - Fix typo in xrootd-config help
- Prevent deadlock in Python bindings
- Fix plugin path in xrootd-http.cfg for 32 bit architectures

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.12.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 24 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.12.3-3
- Fix one definition rule (ODR) violation for LTO
- Disable LTO for 32 bit architectures due to the POSIX preload code

* Thu Jul 16 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.12.3-2
- Fix a typo in the rpm scriptlets (missing underscore)

* Mon Jul 13 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.12.3-1
- Update to version 4.12.3 (no code changes w.r.t. 4.12.2)
- Backport XrdVoms fixes from upstream git

* Thu Jun 11 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.12.2-3
- Provide/Obsolete xrootd-voms-plugin and vomsxrd

* Tue Jun 09 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.12.2-2
- Remove libXrdSecgsiVOMS-4.so symlink from xrootd-libs

* Fri Jun 05 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.12.2-1
- Update to version 4.12.2
- Add voms attribute extractor plugin package
- Drop patches (accepted upstream)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1:4.12.1-2
- Rebuilt for Python 3.9

* Thu May 21 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.12.1-1
- Update to version 4.12.1
- Fix broken man page

* Fri May 08 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.12.0-1
- Update to version 4.12.0
- Fix empty xrdmapc manpage

* Tue Apr 21 2020 Björn Esser <besser82@fedoraproject.org> - 1:4.11.3-2
- Rebuild (json-c)

* Sat Mar 21 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.11.3-1
- Update to version 4.11.3
- Use libc semaphores for EPEL 7 build
  POSIX compliant semaphores were backported to glibc in RHEL 7.2
- Drop glibc version requirement for semaphores (backported to older version)
- Move libXrdSsi{Lib,ShMap}.so.* to client-libs package (from server-libs)

* Wed Feb 05 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.11.2-1
- Update to version 4.11.2

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 17 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.11.1-1
- Update to version 4.11.1

* Fri Oct 18 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.11.0-1
- Update to version 4.11.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1:4.10.1-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Wed Oct 02 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.10.1-1
- Update to version 4.10.1

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1:4.10.0-2
- Rebuilt for Python 3.8

* Thu Aug 01 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.10.0-1
- Update to version 4.10.0
- Drop the xrootd-ceph package (now in a separate source RPM)

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 07 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.9.1-1
- Update to version 4.9.1
- Drop patch xrootd-fix-compilation-errors.patch (accepted upstream)

* Fri Mar 08 2019 Troy Dawson <tdawson@redhat.com> - 1:4.9.0-2
- Rebuilt to change main python from 3.4 to 3.6

* Fri Feb 22 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.9.0-1
- Update to version 4.9.0
- Drop patches previously backported

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1:4.8.5-7
- Rebuild for readline 8.0

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.8.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.8.5-5
- Fix Fedora Rawhide build (gcc 9)

* Thu Jan 17 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.8.5-4
- Drop ceph support for 32 bit arches in Fedore 30+

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 1:4.8.5-3
- Rebuilt for libcrypt.so.2 (#1666033)

* Wed Nov 14 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.8.5-2
- XrdCl: Handle properly server disconnect

* Sat Nov 03 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.8.5-1
- Update to version 4.8.5
- Drop Python 2 bindings for Fedora 30+
- New subpackage for EPEL7: python36-xrootd

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jul 06 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.8.4-1
- Update to version 4.8.4

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1:4.8.3-2
- Rebuilt for Python 3.7

* Thu May 03 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.8.3-1
- Update to version 4.8.3
- Drop patch xrootd-fix-compiling-errors.patch (accepted upstream)

* Thu Apr 12 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.8.2-2
- Add missing ? in systemd_requires macro

* Thu Apr 12 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.8.2-1
- Update to version 4.8.2
- Drop patch xrootd-missing-header.patch (accepted upstream)

* Wed Feb 28 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1:4.8.1-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb 05 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.8.1-1
- Update to version 4.8.1

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 1:4.8.0-2
- Rebuilt for switch to libxcrypt

* Fri Dec 15 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.8.0-1
- Update to version 4.8.0
- New subpackage for EPEL7: python34-xrootd

* Thu Nov 02 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.7.1-1
- Update to version 4.7.1
- Drop patch xrootd-signed-char.patch (accepted upstream)
- Drop patch xrootd-dcache-compat.patch (previously backported)

* Wed Oct 18 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.7.0-3
- Add two library symlinks to xrootd-private-devel

* Mon Oct 09 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.7.0-2
- Compatibility with older dcache servers

* Mon Aug 28 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.7.0-1
- Update to version 4.7.0
- Drop patch xrootd-ceph12.patch - accepted upstream
- Add python3 sub-package (Python 3 is supported in this release according
  to the release notes)
- Fix comparison always false error

* Thu Aug 10 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.6.1-6
- Rename python sub-package

* Sat Aug 05 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.6.1-5
- Adapt to ceph version 12

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Wed May 10 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.6.1-1
- Update to version 4.6.1
- Drop patches (accepted upstream or previously backported)
- EPEL 5 end-of-life specfile clean-up

* Fri Mar 31 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.6.0-9
- Rebuild for rpm build-id ownership bug (Fedora 27) (rhbz #1432372)

* Mon Mar 13 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.6.0-8
- Absent CRL should not trigger authentication error

* Fri Mar 03 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.6.0-7
- Make sure the effective CA is always defined

* Thu Mar 02 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.6.0-6
- Ignore parameter of discarded old configuration directive

* Wed Mar 01 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.6.0-5
- Fix backward compatibilities in XrdSecXtractor interface
- Allow old configuration directives for file cache
- Use upstream's fixes when different from previous patches
- Backport fixes to CRL handling

* Fri Feb 17 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.6.0-4
- A valid legacy proxy should not trigger an error msg

* Wed Feb 15 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.6.0-3
- Fix for CA chain verification segfault
- Absent CRL should not trigger authentication error

* Fri Feb 10 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.6.0-2
- Fix for CRL verification bug

* Wed Feb 08 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.6.0-1
- Update to version 4.6.0
- Drop patch xrootd-gcc7.patch

* Mon Feb 06 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.5.0-3
- Address compiler errors from GCC 7 (backported from git)

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 1:4.5.0-2
- Rebuild for readline 7.x

* Thu Nov 17 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.5.0-1
- Update to version 4.5.0
- Adapt to OpenSSL 1.1.0

* Wed Oct 05 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.4.1-1
- Update to version 4.4.1

* Fri Jul 29 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.4.0-1
- Update to version 4.4.0
- Drop patch xrootd-deprecated.patch

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.3.0-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Apr 21 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:4.3.0-3
- Backport upstream's fix for the deprecation of readdir_r

* Sat Feb 27 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:4.3.0-2
- Workaround deprecation of readdir_r in glibc 2.24

* Fri Feb 26 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:4.3.0-1
- Update to version 4.3.0
- Drop patches accected upstream or that were previously backported:
  xrootd-selinux.patch, xrootd-pth-cancel.patch, xrootd-link.patch,
  xrootd-c++11.patch, xrootd-doxygen.patch, xrootd-autoptr.patch,
  xrootd-indent.patch, xrootd-throw-dtor.patch and xrootd-sockaddr.patch

* Wed Feb 17 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:4.2.3-6
- Fix strict aliasing issues with struct sockaddr

* Fri Feb 12 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:4.2.3-5
- Use upstream's patch for the pthread segfault
- Backport fixes for gcc 6 from upstream

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 23 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:4.2.3-3
- Fix for c++11 usage in ceph (backport from upstream git)
- Doxygen fixes

* Wed Dec 23 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:4.2.3-2
- Fix segfault due to pthread clean-up functions

* Tue Sep 08 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:4.2.3-1
- Update to version 4.2.3

* Fri Jul 31 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:4.2.2-1
- Update to version 4.2.2
- Drop patch xrootd-narrowing.patch (accepted upstream)

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 02 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:4.2.1-2
- Fix narrowing conversion error on ppc64 (EPEL 7)

* Tue Jun 02 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:4.2.1-1
- Update to version 4.2.1
- New subpackages ceph (F22+) and python

* Fri Apr 17 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:4.1.1-2
- Rebuilt for gcc C++ ABI change

* Mon Dec 08 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:4.1.1-1
- Update to version 4.1.1
- Drop patch xrootd-signed-char.patch (accepted upstream)

* Fri Nov 28 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:4.1.0-1
- Update to version 4.1.0
- Install systemd unit files (F21+, EPEL7+)

* Sat Nov 01 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:4.0.4-1
- Update to version 4.0.4

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Aug 08 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:4.0.3-1
- Update to version 4.0.3

* Fri Jul 11 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:4.0.1-1
- Update to version 4.0.1
- Split main package into server and selinux
- New main package installs server and selinux
- Drop patches accepted upstream (-32bit, -range, -narrowing)

* Sun Jun 29 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:4.0.0-1
- Update to version 4.0.0
- Remove the perl package - no longer part of upstream sources

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 30 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:3.3.6-1
- Update to version 3.3.6

* Tue Dec 03 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:3.3.5-1
- Update to version 3.3.5

* Tue Nov 19 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:3.3.4-1
- Update to version 3.3.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 27 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:3.3.3-1
- Update to version 3.3.3
- Change License tag to LGPLv3+ due to upstream license change

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1:3.3.2-2
- Perl 5.18 rebuild

* Sun Apr 28 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:3.3.2-1
- Update to version 3.3.2

* Wed Mar 06 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:3.3.1-1
- Update to version 3.3.1
- Remove the java package - no longer part of upstream sources
- Drop patches fixed upstream: xrootd-cryptoload.patch, xrootd-init.patch and
  xrootd-perl.patch
- Drop obsolete patch: xrootd-java.patch
- Add private-devel package for deprecated header files

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 17 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:3.2.7-1
- Update to version 3.2.7
- Split libs package into libs, client-libs and server-libs
- Split devel package into devel, client-devel and server-devel

* Fri Oct 12 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:3.2.5-1
- Update to version 3.2.5

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul 11 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:3.2.2-1
- Update to version 3.2.2

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 1:3.2.1-2
- Perl 5.16 rebuild

* Thu May 17 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:3.2.1-1
- Update to version 3.2.1

* Sat Mar 17 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:3.1.1-1
- Update to version 3.1.1

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.0.5-3
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Nov 05 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:3.0.5-1
- Update to version 3.0.5

* Mon Jul 18 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:3.0.4-2.1
- Rebuild for new gridsite (EPEL 5 only)

* Tue Jun 28 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:3.0.4-2
- Add missing BuildRequires ncurses-devel

* Tue Jun 28 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:3.0.4-1.1
- Remove xrootdfs man page on EPEL 4

* Mon Jun 27 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:3.0.4-1
- Update to version 3.0.4
- Drop patches fixed upstream: xrootd-man.patch, xrootd-rhel5-no-atomic.patch
- Drop the remaining man-pages copied from root - now provided by upstream

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1:3.0.3-3
- Perl mass rebuild

* Mon May 02 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:3.0.3-2
- Proper fix for the atomic detection on ppc - no bug in gcc after all

* Sun Apr 24 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:3.0.3-1.1
- Workaround for broken gcc on RHEL5 ppc (rhbz #699149)

* Fri Apr 22 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:3.0.3-1
- Update to version 3.0.3
- Use upstream's manpages where available (new in this release)
- Use upstream's start-up scripts (new in this release)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 30 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:3.0.2-1
- Update to version 3.0.2
- Patch XrdCms makefile to make the Xmi interface public

* Fri Dec 17 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:3.0.0-2
- Rebuilt for updated gridsite package

* Mon Dec 13 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:3.0.0-1
- Update to version 3.0.0
- New subpackage - xrootd-fuse
- New version scheme inroduced by upstream - add epoch

* Wed Sep 01 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 20100315-5
- Disable threads in doxygen - causes memory corruption on ppc

* Wed Sep 01 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 20100315-4
- Add startup scripts for cmsd service that replaces the deprecated
  olbd service

* Fri Jul 09 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 20100315-3
- Fix broken jar

* Mon Jun 14 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 20100315-2
- Add LGPLv2+ to License tag due to man pages
- Better package description

* Wed Jun 09 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 20100315-1
- Initial packaging
