%global newname         htcondor
%global srcver          8_8_15

%ifarch %{arm} %{ix86} x86_64
%global with_mongodb    1
%endif

# disable plumage (and need for mongodb)
%global with_mongodb   0

# enable aviary
%global with_aviary    0

# enable BOSCO
%global with_bosco     0

# enable CREAM gahp
%global with_cream_gahp    0

#######################
Name:           condor
Version:        8.8.15
Release:        12%{?dist}
Summary:        HTCondor: High Throughput Computing
License:        ASL 2.0
URL:            http://research.cs.wisc.edu/htcondor/
##############################################################
# NOTE: If you wish to setup a debug build either add a patch
# or adjust the URL to a private github location
##############################################################
Source0:        https://github.com/htcondor/htcondor/archive/V%{srcver}/%{newname}-%{version}.tar.gz
Source1:        %{name}-tmpfiles.conf
Source2:        %{name}.service
Source3:        00personal_condor.config

Patch1:         condor-gahp.patch
# turn off the cmake regex-replace hack that removes "-Werror", as it 
# breaks the new cflag "-Werror=format-security" passed in from build system:
Patch2:         Werror_replace.patch
Patch5:         python-scripts.patch
Patch6:         boost-python38.patch
Patch7:         doc-conf.patch

#######################
BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: flex
BuildRequires: byacc
BuildRequires: pcre-devel
BuildRequires: openssl-devel
BuildRequires: krb5-devel
BuildRequires: libvirt-devel
BuildRequires: bind-utils
BuildRequires: m4
BuildRequires: libX11-devel
BuildRequires: libcurl-devel
BuildRequires: expat-devel
BuildRequires: openldap-devel
BuildRequires: python3-setuptools
BuildRequires: python3-sphinx
BuildRequires: python3-sphinx_rtd_theme
BuildRequires: boost-devel
BuildRequires: boost-python3
BuildRequires: libuuid-devel
BuildRequires: sqlite-devel
# needed for param table generator
BuildRequires: perl-generators
BuildRequires: perl(Data::Dumper)

# Globus GSI build requirements
BuildRequires: globus-gssapi-gsi-devel
BuildRequires: globus-gass-server-ez-devel
BuildRequires: globus-gass-transfer-devel
BuildRequires: globus-gram-client-devel
BuildRequires: globus-rsl-devel
BuildRequires: globus-gram-protocol
BuildRequires: globus-io-devel
BuildRequires: globus-xio-devel
BuildRequires: globus-gssapi-error-devel
BuildRequires: globus-gss-assist-devel
BuildRequires: globus-gsi-proxy-core-devel
BuildRequires: globus-gsi-credential-devel
BuildRequires: globus-gsi-callback-devel
BuildRequires: globus-gsi-sysconfig-devel
BuildRequires: globus-gsi-cert-utils-devel
BuildRequires: globus-openssl-module-devel
BuildRequires: globus-gsi-openssl-error-devel
BuildRequires: globus-gsi-proxy-ssl-devel
BuildRequires: globus-callout-devel
BuildRequires: globus-common-devel
BuildRequires: globus-ftp-client-devel
BuildRequires: globus-ftp-control-devel
BuildRequires: libtool-ltdl-devel
BuildRequires: munge-devel
BuildRequires: voms-devel
# support for aviary
%if 0%{?with_aviary}
BuildRequires: wso2-wsf-cpp-devel
BuildRequires: wso2-axis2-devel
%endif
# support for plumage
%if 0%{?with_mongodb}
BuildRequires: mongodb-devel
%endif
# support for cream (glite-ce-cream-client-devel doesn't exist in Fedora)
#BuildRequires: glite-ce-cream-client-devel
#BuildRequires: glite-lbjp-common-gsoap-plugin-devel
#BuildRequires: glite-ce-cream-utils
#BuildRequires: log4cpp-devel
#BuildRequires: gridsite-devel

# we now need to request the python libs and includes explicitly:
BuildRequires: python3-devel
BuildRequires: python3-libs

# Added by B.DeKnuydt (Jan 2020)
BuildRequires: zlib zlib-devel
BuildRequires: libxml2 libxml2-devel
#BuildRequires: libcgroup libcgroup-devel
BuildRequires: pam-devel
BuildRequires: make

#######################
# Installation requirements.
Requires: mailx
Requires: python3
Requires: condor-classads = %{version}-%{release}
Requires: condor-procd = %{version}-%{release}
Requires: voms

# doesn't exist in fedora
#Requires: blahp
#Requires: glexec

%description
HTCondor is a workload management system for high-throughput and
high-performance jobs. Like other full-featured batch systems, HTCondor
provides a job queuing mechanism, scheduling policy, priority scheme,
resource monitoring, and resource management. Users submit their
serial or parallel jobs to HTCondor, HTCondor places them into a queue,
chooses when and where to run the jobs based upon a policy, carefully
monitors their progress, and ultimately informs the user upon
completion.

#######################
%package procd
Summary: HTCondor Process tracking Daemon
%description procd
A daemon for tracking child processes started by a parent.
Part of HTCondor, but able to be stand-alone

#######################
%if 0%{?with_aviary}
%package aviary-common
Summary: HTCondor Aviary development components
Requires: %name = %version-%release
Requires: python2-suds

%description aviary-common
Components to develop against simplified WS interface to HTCondor.

%package aviary
Summary: HTCondor Aviary components
Requires: %name = %version-%release
Requires: condor = %{version}-%{release}
Requires: condor-aviary-common = %{version}-%{release}

%description aviary
Components to provide simplified WS interface to HTCondor.

%package aviary-hadoop-common
Summary: HTCondor Aviary Hadoop development components
Requires: %name = %version-%release
Requires: python2-suds
Requires: condor-aviary-common = %{version}-%{release}
Requires: tar

%description aviary-hadoop-common
Components to develop against simplified WS interface to HTCondor.

%package aviary-hadoop
Summary: HTCondor Aviary Hadoop components
Requires: %name = %version-%release
Requires: condor-aviary = %{version}-%{release}
Requires: condor-aviary-hadoop-common = %{version}-%{release}

%description aviary-hadoop
Aviary Hadoop plugin and components.
%endif

#######################
%if 0%{?with_mongodb}
%package plumage
Summary: HTCondor Plumage components
Requires: %name = %version-%release
Requires: condor-classads = %{version}-%{release}
Requires: mongodb
Requires: pymongo
Requires: python2-dateutil

%description plumage
Components to provide a NoSQL operational data store for HTCondor.
%endif

#######################
%package kbdd
Summary: HTCondor Keyboard Daemon
Requires: %name = %version-%release
Requires: condor = %{version}-%{release}

%description kbdd
The condor_kbdd monitors logged in X users for activity. It is only
useful on systems where no device (e.g. /dev/*) can be used to
determine console idle time.

#######################
%package vm-gahp
Summary: HTCondor's VM Gahp
Requires: %name = %version-%release
Requires: libvirt
Requires: condor = %{version}-%{release}

%description vm-gahp
The condor_vm-gahp enables the Virtual Machine Universe feature of
HTCondor. The VM Universe uses libvirt to start and control VMs under
HTCondor's Startd.

#######################
%package openstack-gahp
Summary: HTCondor's OpenStack Gahp
Requires: %name = %version-%release
Requires: condor = %{version}-%{release}

%description openstack-gahp
The openstack_gahp enables HTCondor's ability to manage jobs run on
resources exposed by the OpenStack API.

#######################
%package classads
Summary: HTCondor's classified advertisement language
Obsoletes: classads <= 1.0.8
Obsoletes: classads-static <= 1.0.8

%description classads
Classified Advertisements (classads) are the lingua franca of
HTCondor. They are used for describing jobs, workstations, and other
resources. They are exchanged by HTCondor processes to schedule
jobs. They are logged to files for statistical and debugging
purposes. They are used to enquire about current state of the system.

A classad is a mapping from attribute names to expressions. In the
simplest cases, the expressions are simple constants (integer,
floating point, or string). A classad is thus a form of property
list. Attribute expressions can also be more complicated. There is a
protocol for evaluating an attribute expression of a classad vis a vis
another ad. For example, the expression "other.size > 3" in one ad
evaluates to true if the other ad has an attribute named size and the
value of that attribute is (or evaluates to) an integer greater than
three. Two classads match if each ad has an attribute requirements
that evaluates to true in the context of the other ad. Classad
matching is used by the HTCondor central manager to determine the
compatibility of jobs and workstations where they may be run.

#######################
%package classads-devel
Summary: Headers for HTCondor's classified advertisement language
Requires: %name-classads = %version-%release
Requires: pcre-devel
Obsoletes: classads-devel <= 1.0.8

%description classads-devel
Header files for HTCondor's ClassAd Library, a powerful and flexible,
semi-structured representation of data.

#######################
%if 0%{?with_cream_gahp}
%%package cream-gahp
Summary: Allows Condor to act as a client to CREAM.
Requires: %%name = %%version-%%release

%%description cream-gahp
The cream_gahp enables the Condor grid universe to communicate with a remote
CREAM server.
%endif

#######################
%package -n python3-condor
Summary: Python bindings for Condor.
Requires: %name = %version-%release
%{?python_provide:%python_provide python3-condor}

%description -n python3-condor
The python bindings allow one to directly invoke the C++ implementations of
the ClassAd library and HTCondor from python

#######################
%package -n minicondor
Summary: Configuration for a single-node HTCondor
Requires: %name = %version-%release
Requires: python3-condor = %version-%release

%description -n minicondor
This example configuration is good for trying out HTCondor for the first time.
It only configures the IPv4 loopback address, turns on basic security, and
shortens many timers to be more responsive.

#######################
# The bosco subpkg is currently dropping file that breaks the out-of-box condor
# configuration (60-campus_factory.config).  The file looks somewhat site-
# specific.  I'm going to disable bosco until it can be made more generic for
# fedora, and/or not break default condor config out of box.
%if 0%{?with_bosco}
%package bosco
Summary: BOSCO, a Condor overlay system for managing jobs at remote clusters
Url: http://bosco.opensciencegrid.org
Requires: %name = %version-%release

%description bosco
BOSCO allows a locally-installed Condor to submit jobs to remote clusters,
using SSH as a transit mechanism.  It is designed for cases where the remote
cluster is using a different batch system such as PBS, SGE, LSF, or another
Condor system.

BOSCO provides an overlay system so the remote clusters appear to be a Condor
cluster.  This allows the user to run their workflows using Condor tools across
multiple clusters.
%endif

#######################
%package annex-ec2
Summary: Configuration and scripts to make an EC2 image annex-compatible.
Requires: %name = %version-%release
Requires(post): /sbin/chkconfig
Requires(preun): /sbin/chkconfig

%description annex-ec2
Configures HTCondor to make an EC2 image annex-compatible.  Do NOT install
on a non-EC2 image.

%files annex-ec2
%_libexecdir/condor/condor-annex-ec2
%{_unitdir}/condor-annex-ec2.service
%config(noreplace) %_sysconfdir/condor/config.d/50ec2.config
%config(noreplace) %_sysconfdir/condor/master_shutdown_script.sh

%post annex-ec2
/bin/systemctl enable condor-annex-ec2

%preun annex-ec2
if [ $1 == 0 ]; then
    /bin/systemctl disable condor-annex-ec2
fi

%pre
getent group %{name} >/dev/null || groupadd -r %{name}
getent passwd %{name} >/dev/null || \
  useradd -r -g condor -d %{_sharedstatedir}/%{name} -s /sbin/nologin \
    -c "Owner of HTCondor Daemons" %{name}
exit 0

%prep
%setup -q -n %{newname}-%{srcver}
%patch1 -p1
%patch2 -p1
%patch5 -p1
%patch7 -p1
cp %{SOURCE1} %{name}-tmpfiles.conf
cp %{SOURCE2} %{name}.service
cp %{SOURCE3} .

%build
make -C docs man
%cmake -DNO_PHONE_HOME:BOOL=TRUE \
       -DBUILD_TESTING:BOOL=FALSE \
       -DBUILDID:STRING=RH-%{version}-%{release} \
       -D_VERBOSE:BOOL=TRUE \
       -DCMAKE_SKIP_RPATH:BOOL=TRUE \
       -DHAVE_BACKFILL:BOOL=FALSE \
       -DHAVE_BOINC:BOOL=FALSE \
       -DWITH_GSOAP:BOOL=FALSE \
       -DWITH_POSTGRESQL:BOOL=FALSE \
       -DHAVE_KBDD:BOOL=TRUE \
       -DHAVE_HIBERNATION:BOOL=TRUE \
       -DWANT_LEASE_MANAGER:BOOL=FALSE \
       -DWANT_HDFS:BOOL=FALSE \
       -DWANT_QUILL:BOOL=FALSE \
       -DWITH_QPID:BOOL=FALSE \
       -DWITH_ZLIB:BOOL=FALSE \
       -DWITH_POSTGRESQL:BOOL=FALSE \
       -DWANT_CONTRIB:BOOL=ON \
       -DWITH_BOSCO:BOOL=FALSE \
       -DWITH_PIGEON:BOOL=FALSE \
       -DWITH_MANAGEMENT:BOOL=FALSE \
%if 0%{?with_mongodb}
       -DWITH_PLUMAGE:BOOL=TRUE \
%endif
%if 0%{?with_aviary}
       -DWITH_AVIARY:BOOL=TRUE \
%endif
       -DWANT_FULL_DEPLOYMENT:BOOL=TRUE \
       -DBLAHP_FOUND=/usr/libexec/BLClient \
       -DWITH_BLAHP:BOOL=TRUE \
       -DWITH_CREAM:BOOL=FALSE \
       -DWANT_GLEXEC:BOOL=TRUE \
       -DWANT_MAN_PAGES:BOOL=TRUE \
       -DWITH_LIBDELTACLOUD:BOOL=TRUE \
       -DWITH_GLOBUS:BOOL=TRUE \
       -DWITH_PYTHON_BINDINGS:BOOL=TRUE \
       -DWITH_LIBCGROUP:BOOL=FALSE

%cmake_build

%install
# installation happens into a temporary location, this function is
# useful in moving files into their final locations
function populate {
  _dest="$1"; shift; _src="$*"
  mkdir -p "%{buildroot}/$_dest"
  mv $_src "%{buildroot}/$_dest"
}

rm -rf %{buildroot}
%cmake_install

# The install target puts etc/ under usr/, let's fix that.
mv %{buildroot}/usr/etc %{buildroot}/%{_sysconfdir}

populate %_sysconfdir/condor %{buildroot}/%{_usr}/lib/condor_ssh_to_job_sshd_config_template

# Things in /usr/lib really belong in /usr/share/condor
populate %{_datadir}/condor %{buildroot}/%{_usr}/lib/*
# Except for the shared libs
populate %{_libdir}/ %{buildroot}/%{_datadir}/condor/libclassad.s*
populate %{_libdir}/ %{buildroot}/%{_datadir}/condor/libcondor_utils*.so
populate %{_libdir}/ %{buildroot}/%{_datadir}/condor/libpy3classad%{python3_version}_%{srcver}.so
# and python site-packages
if [ -d %{buildroot}/%{_datadir}/condor/python3.* ]; then
    mv %{buildroot}/%{_datadir}/condor/python3.* %{buildroot}/%{_libdir}/
fi
rm -f %{buildroot}/%{_datadir}/condor/libclassad.a

# Remove the small shadow if built
rm -f %{buildroot}/%{_sbindir}/condor_shadow_s

# It is proper to put HTCondor specific libexec binaries under libexec/condor/
populate %_libexecdir/condor %{buildroot}/usr/libexec/*

# man pages
mkdir -p %{buildroot}/%{_mandir}
mv %{buildroot}/usr/man %{buildroot}/%{_mandir}/man1

mkdir -p %{buildroot}/%{_sysconfdir}/condor
# the default condor_config file is not architecture aware and thus
# sets the LIB directory to always be /usr/lib, we want to do better
# than that. this is, so far, the best place to do this
# specialization. we strip the "lib" or "lib64" part from _libdir and
# stick it in the LIB variable in the config.
LIB=$(echo %{?_libdir} | sed -e 's:/usr/\(.*\):\1:')
if [ "$LIB" = "%_libdir" ]; then
  echo "_libdir does not contain /usr, sed expression needs attention"
  exit 1
fi
sed -e "s:^LIB\s*=.*:LIB = \$(RELEASE_DIR)/$LIB/condor:" \
  %{buildroot}/etc/examples/condor_config.generic.redhat \
  > %{buildroot}/%{_sysconfdir}/condor/condor_config

# Install the basic configuration, a Personal HTCondor config. Allows for
# yum install condor + service condor start and go.
#mkdir -m0755 %{buildroot}/%{_sysconfdir}/condor/config.d
install -m 0644 00personal_condor.config %{buildroot}/%{_sysconfdir}/condor/config.d/00personal_condor.config

populate %_sysconfdir/condor/config.d %{buildroot}/etc/examples/00-minicondor
populate %_sysconfdir/condor/config.d %{buildroot}/etc/examples/50ec2.config

%if 0%{?with_aviary}
populate %_sysconfdir/condor/config.d %{buildroot}/etc/examples/61aviary.config
populate %_sysconfdir/condor/config.d %{buildroot}/etc/examples/63aviary-hadoop.config

mkdir -p %{buildroot}/%{_var}/lib/condor/aviary
populate %{_var}/lib/condor/aviary %{buildroot}/usr/axis2.xml
populate %{_var}/lib/condor/aviary %{buildroot}/usr/services/

populate %{_libdir}/condor/plugins %{buildroot}/%{_usr}/libexec/condor/*-plugin.so
populate %{_libdir}/ %{buildroot}/%{_datadir}/condor/libaviary_*
%endif


%if 0%{?with_mongodb}
# Install condor-plumage's base plugin configuration
populate %_sysconfdir/condor/config.d %{buildroot}/etc/examples/62plumage.config
%endif
rm -f %{buildroot}/%{_bindir}/ods_job_etl_tool
rm -f %{buildroot}/%{_sbindir}/ods_job_etl_server
mkdir -p -m0755 %{buildroot}/%{_var}/lib/condor/ViewHist

mkdir -p -m0755 %{buildroot}/%{_var}/run/condor
mkdir -p -m0755 %{buildroot}/%{_var}/log/condor
mkdir -p -m0755 %{buildroot}/%{_var}/lock/condor
mkdir -p -m1777 %{buildroot}/%{_var}/lock/condor/local
mkdir -p -m0755 %{buildroot}/%{_var}/lib/condor/spool
mkdir -p -m1777 %{buildroot}/%{_var}/lib/condor/execute

# not packaging standard universe
rm %{buildroot}/%{_mandir}/man1/condor_compile.1
rm %{buildroot}/%{_mandir}/man1/condor_checkpoint.1

# not packaging configure/install scripts
rm %{buildroot}/%{_mandir}/man1/condor_configure.1

# Remove junk
rm -r %{buildroot}/%{_sysconfdir}/sysconfig
rm -r %{buildroot}/%{_sysconfdir}/init.d

# install tmpfiles.d/condor.conf
mkdir -p %{buildroot}%{_tmpfilesdir}/tmpfiles.d
install -m 0644 %{name}-tmpfiles.conf %{buildroot}%{_tmpfilesdir}/%{name}.conf

install -Dp -m0755 %{buildroot}/etc/examples/condor-annex-ec2 %{buildroot}%{_libexecdir}/condor/condor-annex-ec2

mkdir -p %{buildroot}%{_unitdir}
install -m 0644 %{buildroot}/etc/examples/condor-annex-ec2.service %{buildroot}%{_unitdir}/condor-annex-ec2.service

mkdir -p %{buildroot}%{_localstatedir}/run/
install -d -m 0710 %{buildroot}%{_localstatedir}/run/%{name}/

mkdir -p %{buildroot}%{_unitdir}
install -m 0644 %{name}.service %{buildroot}%{_unitdir}/condor.service

mv %{buildroot}%{python3_sitearch}/py3htcondor.so %{buildroot}%{python3_sitearch}/htcondor.so
mv %{buildroot}%{python3_sitearch}/py3classad.so %{buildroot}%{python3_sitearch}/classad.so

# Remove stuff that comes from the full-deploy
rm -rf %{buildroot}%{_sbindir}/cleanup_release
rm -rf %{buildroot}%{_sbindir}/condor_cleanup_local
rm -rf %{buildroot}%{_sbindir}/condor_cold_start
rm -rf %{buildroot}%{_sbindir}/condor_cold_stop
rm -rf %{buildroot}%{_sbindir}/condor_config_bind
rm -rf %{buildroot}%{_sbindir}/condor_configure
rm -rf %{buildroot}%{_sbindir}/condor_credd
rm -rf %{buildroot}%{_sbindir}/condor_install
rm -rf %{buildroot}%{_sbindir}/condor_install_local
rm -rf %{buildroot}%{_sbindir}/condor_local_start
rm -rf %{buildroot}%{_sbindir}/condor_local_stop
rm -rf %{buildroot}%{_sbindir}/condor_startd_factory
rm -rf %{buildroot}%{_sbindir}/condor_vm-gahp-vmware
rm -rf %{buildroot}%{_sbindir}/condor_vm_vmwar*
rm -rf %{buildroot}%{_sbindir}/filelock_midwife
rm -rf %{buildroot}%{_sbindir}/filelock_undertaker
rm -rf %{buildroot}%{_sbindir}/install_release
rm -rf %{buildroot}%{_sbindir}/uniq_pid_command
rm -rf %{buildroot}%{_sbindir}/uniq_pid_midwife
rm -rf %{buildroot}%{_sbindir}/uniq_pid_undertaker
rm -rf %{buildroot}%{_datadir}/condor/*.pm
rm -rf %{buildroot}%{_datadir}/condor/Chirp.jar
rm -rf %{buildroot}%{_usrsrc}/chirp/chirp_*
rm -rf %{buildroot}%{_usrsrc}/startd_factory
rm -rf %{buildroot}/usr/DOC
rm -rf %{buildroot}/usr/INSTALL
rm -rf %{buildroot}/usr/LICENSE-2.0.txt
rm -rf %{buildroot}/usr/NOTICE.txt
rm -rf %{buildroot}/usr/README
rm -rf %{buildroot}/usr/examples/
rm -rf %{buildroot}%{_includedir}/MyString.h
rm -rf %{buildroot}%{_includedir}/chirp_client.h
rm -rf %{buildroot}%{_includedir}/compat_classad*
rm -rf %{buildroot}%{_includedir}/condor_classad.h
rm -rf %{buildroot}%{_includedir}/condor_constants.h
rm -rf %{buildroot}%{_includedir}/condor_event.h
rm -rf %{buildroot}%{_includedir}/condor_header_features.h
rm -rf %{buildroot}%{_includedir}/condor_holdcodes.h
rm -rf %{buildroot}%{_includedir}/file_lock.h
rm -rf %{buildroot}%{_includedir}/iso_dates.h
rm -rf %{buildroot}%{_includedir}/read_user_log.h
rm -rf %{buildroot}%{_includedir}/stl_string_utils.h
rm -rf %{buildroot}%{_includedir}/user_log.README
rm -rf %{buildroot}%{_includedir}/user_log.c++.h
rm -rf %{buildroot}%{_includedir}/write_user_log.h
rm -rf %{buildroot}%{_libexecdir}/condor/bgp_*
rm -rf %{buildroot}%{_datadir}/condor/libchirp_client.*
rm -rf %{buildroot}%{_datadir}/condor/libcondorapi.a
rm -rf %{buildroot}%{_datadir}/condor/python/{htcondor,classad}.so
rm -rf %{buildroot}%{_datadir}/condor/{libpy*classad_*,htcondor,classad}.so
rm %{buildroot}%{_libexecdir}/condor/condor_schedd.init
rm -rf %{buildroot}%{_libexecdir}/condor/pandad
rm -rf %{buildroot}%{_libexecdir}/condor/libclassad_python*_user.so

# Install BOSCO
%if 0%{?with_bosco}
mv %{buildroot}%{_libexecdir}/condor/campus_factory/share/condor/condor_config.factory %{buildroot}%{_sysconfdir}/condor/config.d/60-campus_factory.config
mv %{buildroot}%{_libexecdir}/condor/campus_factory/etc/campus_factory.conf %{buildroot}%{_sysconfdir}/condor/
mv %{buildroot}%{_libexecdir}/condor/campus_factory/share %{buildroot}%{_datadir}/condor/campus_factory
%endif
rm -rf %{buildroot}%{_libexecdir}/condor/campus_factory
rm -rf %{buildroot}/%{_sbindir}/bosco_install
rm -rf %{buildroot}/%{_sbindir}/campus_factory
rm -rf %{buildroot}/%{_sbindir}/condor_ft-gahp
rm -rf %{buildroot}/%{_sbindir}/glidein_creation
rm -rf %{buildroot}/%{_sbindir}/runfactory
rm -rf %{buildroot}/%{_mandir}/man1/bosco*

# we must place the config examples in builddir
cp -rf %{buildroot}/etc/examples %{_builddir}/%{name}-%{tarball_version}
rm -rf %{buildroot}/etc/examples

%files
%doc LICENSE-2.0.txt NOTICE.txt
%config(noreplace) %_sysconfdir/bash_completion.d/condor
%dir %_sysconfdir/condor/
%config(noreplace) %_sysconfdir/condor/condor_config
%config(noreplace) %{_tmpfilesdir}/%{name}.conf
%{_unitdir}/condor.service
%dir %_datadir/condor/
%_datadir/condor/CondorJavaInfo.class
%_datadir/condor/CondorJavaWrapper.class
%_datadir/condor/scimark2lib.jar
%dir %_sysconfdir/condor/config.d/
%dir %_sysconfdir/condor/ganglia.d
%config(noreplace) %_sysconfdir/condor/ganglia.d/00_default_metrics
%config(noreplace) %_sysconfdir/condor/config.d/00personal_condor.config
%config(noreplace) %_sysconfdir/condor/condor_ssh_to_job_sshd_config_template
%dir %_libexecdir/condor/
%_libexecdir/condor/condor_chirp
%_libexecdir/condor/condor_ssh
%_libexecdir/condor/sshd.sh
%_libexecdir/condor/get_orted_cmd.sh
%_libexecdir/condor/orted_launcher.sh
%_libexecdir/condor/condor_job_router
%_libexecdir/condor/condor_gangliad
%_libexecdir/condor/condor_glexec_setup
%_libexecdir/condor/condor_glexec_run
%_libexecdir/condor/condor_glexec_job_wrapper
%_libexecdir/condor/condor_glexec_update_proxy
%_libexecdir/condor/condor_glexec_cleanup
%_libexecdir/condor/condor_glexec_kill
%_libexecdir/condor/glite/bin/*
%_libexecdir/condor/condor_limits_wrapper.sh
%_libexecdir/condor/condor_rooster
%_libexecdir/condor/condor_ssh_to_job_shell_setup
%_libexecdir/condor/condor_ssh_to_job_sshd_setup
%_libexecdir/condor/condor_power_state
%_libexecdir/condor/condor_kflops
%_libexecdir/condor/condor_mips
%_libexecdir/condor/data_plugin
%_libexecdir/condor/curl_plugin
%_libexecdir/condor/multifile_curl_plugin
%_libexecdir/condor/condor_shared_port
%_libexecdir/condor/condor_sinful
%_libexecdir/condor/condor_testingd
%_libexecdir/condor/test_user_mapping
%_libexecdir/condor/condor_glexec_wrapper
%_libexecdir/condor/glexec_starter_setup.sh
%_libexecdir/condor/condor_defrag
%_libexecdir/condor/interactive.sub
%_libexecdir/condor/linux_kernel_tuning
%_libexecdir/condor/condor_dagman_metrics_reporter
%_libexecdir/condor/condor_pid_ns_init
%_libexecdir/condor/condor_urlfetch
%_libexecdir/condor/test_user_mapping
%_mandir/man1/condor_advertise.1.gz
%_mandir/man1/condor_annex.1.gz
%_mandir/man1/condor_check_userlogs.1.gz
%_mandir/man1/condor_chirp.1.gz
%_mandir/man1/condor_convert_history.1*
%_mandir/man1/condor_cod.1.gz
%_mandir/man1/condor_config_val.1.gz
%_mandir/man1/condor_dagman.1.gz
%_mandir/man1/condor_fetchlog.1.gz
%_mandir/man1/condor_findhost.1.gz
%_mandir/man1/condor_history.1.gz
%_mandir/man1/condor_hold.1.gz
%_mandir/man1/condor_master.1.gz
%_mandir/man1/condor_off.1.gz
%_mandir/man1/condor_on.1.gz
%_mandir/man1/condor_preen.1.gz
%_mandir/man1/condor_prio.1.gz
%_mandir/man1/condor_q.1.gz
%_mandir/man1/condor_qedit.1.gz
%_mandir/man1/condor_reconfig.1.gz
%_mandir/man1/condor_release.1.gz
%_mandir/man1/condor_reschedule.1.gz
%_mandir/man1/condor_restart.1.gz
%_mandir/man1/condor_rm.1.gz
%_mandir/man1/condor_run.1.gz
%_mandir/man1/condor_set_shutdown.1.gz
%_mandir/man1/condor_stats.1.gz
%_mandir/man1/condor_status.1.gz
%_mandir/man1/condor_store_cred.1.gz
%_mandir/man1/condor_submit.1.gz
%_mandir/man1/condor_submit_dag.1.gz
%_mandir/man1/condor_top.1.gz
%_mandir/man1/condor_transfer_data.1.gz
%_mandir/man1/condor_updates_stats.1.gz
%_mandir/man1/condor_userlog.1.gz
%_mandir/man1/condor_userprio.1.gz
%_mandir/man1/condor_vacate.1.gz
%_mandir/man1/condor_vacate_job.1.gz
%_mandir/man1/condor_version.1.gz
%_mandir/man1/condor_wait.1.gz
%_mandir/man1/condor_router_history.1.gz
%_mandir/man1/condor_continue.1.gz
%_mandir/man1/condor_suspend.1.gz
%_mandir/man1/condor_router_q.1.gz
%_mandir/man1/condor_ssh_to_job.1.gz
%_mandir/man1/condor_power.1.gz
%_mandir/man1/condor_gather_info.1.gz
%_mandir/man1/condor_router_rm.1.gz
%_mandir/man1/condor_qsub.1.gz
%_mandir/man1/condor_drain.1.gz
%_mandir/man1/condor_install.1.gz
%_mandir/man1/condor_ping.1.gz
%_mandir/man1/condor_rmdir.1.gz
%_mandir/man1/condor_tail.1.gz
%_mandir/man1/condor_who.1.gz
%_mandir/man1/condor_now.1.gz
%_mandir/man1/condor_dagman_metrics_reporter.1.gz
%_mandir/man1/condor_gpu_discovery.1.gz
%_mandir/man1/condor_pool_job_report.1.gz
%_mandir/man1/condor_sos.1.gz
%_mandir/man1/condor_urlfetch.1.gz
%_mandir/man1/condor_job_router_info.1.gz
%_mandir/man1/condor_update_machine_ad.1.gz
%_mandir/man1/condor_transform_ads.1.gz
# bin/condor is a link for checkpoint, reschedule, vacate
%_libdir/libcondor_utils*.so
%_libexecdir/condor/panda-plugin.so
%_libexecdir/condor/libcollector_python3_plugin.so
%_bindir/condor_submit_dag
%_bindir/condor_who
%_bindir/condor_now
%_bindir/condor_prio
%_bindir/condor_transfer_data
%_bindir/condor_check_userlogs
%_bindir/condor_q
%_libexecdir/condor/condor_transferer
%_bindir/condor_cod
%_bindir/condor_docker_enter
%_bindir/condor_qedit
%_bindir/condor_userlog
%_bindir/condor_release
%_bindir/condor_userlog_job_counter
%_bindir/condor_config_val
%_bindir/condor_reschedule
%_bindir/condor_userprio
%_bindir/condor_dagman
%_bindir/condor_rm
%_bindir/condor_vacate
%_bindir/condor_run
%_bindir/condor_router_history
%_bindir/condor_router_q
%_bindir/condor_router_rm
%_bindir/condor_vacate_job
%_bindir/condor_findhost
%_bindir/condor_stats
%_bindir/condor_transform_ads
%_bindir/condor_version
%_bindir/condor_history
%_bindir/condor_status
%_bindir/condor_wait
%_bindir/condor_hold
%_bindir/condor_submit
%_bindir/condor_ssh_to_job
%_bindir/condor_power
%_bindir/condor_gather_info
%_bindir/condor_continue
%_bindir/condor_suspend
%_bindir/condor_test_match
%_bindir/condor_drain
%_bindir/condor_ping
%_bindir/condor_qsub
%_bindir/condor_tail
%_bindir/condor_pool_job_report
%_bindir/condor_job_router_info
%_bindir/condor_update_machine_ad
%_bindir/condor_annex
%_bindir/condor_nsenter
%_sbindir/condor_advertise
%_sbindir/condor_aklog
%_sbindir/condor_c-gahp
%_sbindir/condor_c-gahp_worker_thread
%_sbindir/condor_collector
%_sbindir/condor_convert_history
%_sbindir/condor_fetchlog
%_sbindir/condor_had
%_sbindir/condor_master
%_sbindir/condor_negotiator
%_sbindir/condor_off
%_sbindir/condor_on
%_sbindir/condor_preen
%_sbindir/condor_reconfig
%_sbindir/condor_replication
%_sbindir/condor_restart
%_sbindir/condor_schedd
%_sbindir/condor_set_shutdown
%_sbindir/condor_shadow
%_sbindir/condor_startd
%_sbindir/condor_starter
%_sbindir/condor_store_cred
%_sbindir/condor_transferd
%_sbindir/condor_updates_stats
%_sbindir/ec2_gahp
%_sbindir/condor_gridmanager
%_sbindir/condor_gridshell
%_sbindir/gahp_server
%_sbindir/grid_monitor
%_sbindir/grid_monitor.sh
%_sbindir/remote_gahp
%_sbindir/nordugrid_gahp
%_sbindir/AzureGAHPServer
%_sbindir/condor_sos
%_sbindir/condor_testwritelog
%_sbindir/gce_gahp
#%%_bindir/condor_ping
%_libexecdir/condor/condor_gpu_discovery
%_libexecdir/condor/condor_gpu_utilization
%defattr(-,condor,condor,-)
%dir %_var/lib/condor/
%dir %_var/lib/condor/execute/
%dir %_var/log/condor/
%dir %_var/lib/condor/spool/
%ghost %dir %_var/lock/condor/
%dir %_var/run/condor/
%_libexecdir/condor/accountant_log_fixer
%_datadir/condor/libcondorapi.so

#################
%files procd
%_sbindir/condor_procd
%_sbindir/gidd_alloc
%_sbindir/procd_ctl
%_mandir/man1/procd_ctl.1.gz
%_mandir/man1/gidd_alloc.1.gz
%_mandir/man1/condor_procd.1.gz

#################
%if 0%{?with_aviary}
%files aviary-common
%doc LICENSE-2.0.txt NOTICE.txt
%dir %_datadir/condor/aviary
%_datadir/condor/aviary/jobcontrol.py*
%_datadir/condor/aviary/jobquery.py*
%_datadir/condor/aviary/submissions.py*
%_datadir/condor/aviary/submission_ids.py*
%_datadir/condor/aviary/subinventory.py*
%_datadir/condor/aviary/submit.py*
%_datadir/condor/aviary/setattr.py*
%_datadir/condor/aviary/jobinventory.py*
%_datadir/condor/aviary/locator.py*
%_datadir/condor/aviary/collector_tool.py*
%dir %_datadir/condor/aviary/dag
%_datadir/condor/aviary/dag/diamond.dag
%_datadir/condor/aviary/dag/dag-submit.py*
%_datadir/condor/aviary/dag/job.sub
%dir %_datadir/condor/aviary/module
%_datadir/condor/aviary/module/aviary/util.py*
%_datadir/condor/aviary/module/aviary/https.py*
%_datadir/condor/aviary/module/aviary/__init__.py*
%_datadir/condor/aviary/README
%dir %_var/lib/condor/aviary
%_var/lib/condor/aviary/axis2.xml
%dir %_var/lib/condor/aviary/services
%dir %_var/lib/condor/aviary/services/job
%_var/lib/condor/aviary/services/job/services.xml
%_var/lib/condor/aviary/services/job/aviary-common.xsd
%_var/lib/condor/aviary/services/job/aviary-job.xsd
%_var/lib/condor/aviary/services/job/aviary-job.wsdl
%dir %_var/lib/condor/aviary/services/query
%_var/lib/condor/aviary/services/query/services.xml
%_var/lib/condor/aviary/services/query/aviary-common.xsd
%_var/lib/condor/aviary/services/query/aviary-query.xsd
%_var/lib/condor/aviary/services/query/aviary-query.wsdl
%dir %_var/lib/condor/aviary/services/locator
%_var/lib/condor/aviary/services/locator/services.xml
%_var/lib/condor/aviary/services/locator/aviary-common.xsd
%_var/lib/condor/aviary/services/locator/aviary-locator.xsd
%_var/lib/condor/aviary/services/locator/aviary-locator.wsdl
%dir %_var/lib/condor/aviary/services/collector
%_var/lib/condor/aviary/services/collector/services.xml
%_var/lib/condor/aviary/services/collector/aviary-common.xsd
%_var/lib/condor/aviary/services/collector/aviary-collector.xsd
%_var/lib/condor/aviary/services/collector/aviary-collector.wsdl

#################
%files aviary
%doc LICENSE-2.0.txt NOTICE.txt
%_sysconfdir/condor/config.d/61aviary.config
%_libdir/libaviary_axis_provider.so
%_libdir/libaviary_wso2_common.so
%dir %_libdir/condor/plugins
%_libdir/condor/plugins/AviaryScheddPlugin-plugin.so
%_libdir/condor/plugins/AviaryLocatorPlugin-plugin.so
%_libdir/condor/plugins/AviaryCollectorPlugin-plugin.so
%_sbindir/aviary_query_server
%_var/lib/condor/aviary/services/job/libaviary_job_axis.so
%_var/lib/condor/aviary/services/query/libaviary_query_axis.so
%_var/lib/condor/aviary/services/locator/libaviary_locator_axis.so
%_var/lib/condor/aviary/services/collector/libaviary_collector_axis.so

#################
%files aviary-hadoop-common
%doc LICENSE-2.0.txt NOTICE.txt
%_var/lib/condor/aviary/services/hadoop/services.xml
%_var/lib/condor/aviary/services/hadoop/aviary-common.xsd
%_var/lib/condor/aviary/services/hadoop/aviary-hadoop.xsd
%_var/lib/condor/aviary/services/hadoop/aviary-hadoop.wsdl
%_datadir/condor/aviary/hadoop_tool.py*

#################
%files aviary-hadoop
%doc LICENSE-2.0.txt NOTICE.txt
%_var/lib/condor/aviary/services/hadoop/libaviary_hadoop_axis.so
%_libdir/condor/plugins/AviaryHadoopPlugin-plugin.so
%_sysconfdir/condor/config.d/63aviary-hadoop.config
%_datadir/condor/aviary/hdfs_datanode.sh
%_datadir/condor/aviary/hdfs_namenode.sh
%_datadir/condor/aviary/mapred_jobtracker.sh
%_datadir/condor/aviary/mapred_tasktracker.sh
%endif

#################
%if 0%{?with_mongodb}
%files plumage
%doc LICENSE-2.0.txt NOTICE.txt
%_sysconfdir/condor/config.d/62plumage.config
%dir %_libdir/condor/plugins
%_libdir/condor/plugins/PlumageCollectorPlugin-plugin.so
%dir %_datadir/condor/plumage
%_sbindir/plumage_job_etl_server
%_bindir/plumage_history_load
%_bindir/plumage_stats
%_bindir/plumage_history
%_datadir/condor/plumage/README
%_datadir/condor/plumage/SCHEMA
%_datadir/condor/plumage/plumage_accounting
%_datadir/condor/plumage/plumage_scheduler
%_datadir/condor/plumage/plumage_utilization
%defattr(-,condor,condor,-)
%endif

#################
%files kbdd
%doc LICENSE-2.0.txt NOTICE.txt
%_sbindir/condor_kbdd

#################
%files vm-gahp
%doc LICENSE-2.0.txt NOTICE.txt
%_sbindir/condor_vm-gahp
%_libexecdir/condor/libvirt_simple_script.awk

#################
%files openstack-gahp
%doc LICENSE-2.0.txt NOTICE.txt
%_sbindir/openstack_gahp

#################
%files classads
%doc LICENSE-2.0.txt NOTICE.txt
%_libdir/libclassad.so.*

#################
%files classads-devel
%doc LICENSE-2.0.txt NOTICE.txt
%_bindir/classad_functional_tester
%_bindir/classad_version
%_libdir/libclassad.so
%dir %_includedir/classad/
%_includedir/classad/attrrefs.h
%_includedir/classad/cclassad.h
%_includedir/classad/classad_distribution.h
%_includedir/classad/classadErrno.h
%_includedir/classad/classad.h
%_includedir/classad/classadItor.h
%_includedir/classad/classadCache.h
%_includedir/classad/classad_stl.h
%_includedir/classad/collectionBase.h
%_includedir/classad/collection.h
%_includedir/classad/common.h
%_includedir/classad/debug.h
%_includedir/classad/exprList.h
%_includedir/classad/exprTree.h
%_includedir/classad/fnCall.h
%_includedir/classad/jsonSink.h
%_includedir/classad/jsonSource.h
%_includedir/classad/indexfile.h
%_includedir/classad/lexer.h
%_includedir/classad/lexerSource.h
%_includedir/classad/literals.h

%_includedir/classad/matchClassad.h
%_includedir/classad/operators.h
%_includedir/classad/query.h
%_includedir/classad/sink.h
%_includedir/classad/source.h
%_includedir/classad/transaction.h
%_includedir/classad/util.h
%_includedir/classad/value.h
%_includedir/classad/view.h
%_includedir/classad/xmlLexer.h
%_includedir/classad/xmlSink.h
%_includedir/classad/xmlSource.h

#################
%if 0%{?with_cream_gahp}
%files cream-gahp
%doc LICENSE-2.0.txt NOTICE.txt
%_sbindir/cream_gahp
%endif

#################
%files -n python3-condor
%_bindir/condor_top
%{python3_sitearch}/classad.so
%{python3_sitearch}/htcondor.so
%{_libdir}/libpy3classad%{python3_version}_%{srcver}.so

#################
%files -n minicondor
%config(noreplace) %_sysconfdir/condor/config.d/00-minicondor

#################
%if 0%{?with_bosco}
%files bosco
%config(noreplace) %_sysconfdir/condor/campus_factory.conf
%config(noreplace) %_sysconfdir/condor/config.d/60-campus_factory.config
%_libexecdir/condor/shellselector
%_libexecdir/condor/campus_factory
%_sbindir/bosco_install
%_sbindir/campus_factory
%_sbindir/condor_ft-gahp
%_sbindir/runfactory
%_bindir/bosco_cluster
%_bindir/bosco_ssh_start
%_bindir/bosco_start
%_bindir/bosco_stop
%_bindir/bosco_findplatform
%_bindir/bosco_uninstall
%_bindir/bosco_quickstart
%_bindir/htsub
%_sbindir/glidein_creation
%_datadir/condor/campus_factory
%_mandir/man1/bosco_cluster.1.gz
%_mandir/man1/bosco_findplatform.1.gz
%_mandir/man1/bosco_install.1.gz
%_mandir/man1/bosco_ssh_start.1.gz
%_mandir/man1/bosco_start.1.gz
%_mandir/man1/bosco_stop.1.gz
%_mandir/man1/bosco_uninstall.1.gz
%endif

#################
%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun -n condor
%systemd_postun_with_restart %{name}.service 
/sbin/ldconfig

%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.8.15-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 8.8.15-11
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.8.15-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.8.15-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 24 2022 Jonathan Wakely <jwakely@redhat.com> - 8.8.15-8
- Remove obsolete boost-python3-devel build dependency (#2100748)

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 8.8.15-7
- Rebuilt for Python 3.11

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 8.8.15-6
- Rebuilt for Boost 1.78

* Tue Apr 12 2022 Tim Theisen <ttheisen@fedoraproject.org> - 8.8.15-5
- Temporarily build without cgroup support to ease f37 transition

* Fri Mar 18 2022 Nikola Forró <nforro@redhat.com> - 8.8.15-4
- Rebuilt for libcgroup.so.2

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.8.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 8.8.15-2
- Rebuilt with OpenSSL 3.0.0

* Mon Aug 23 2021 Tim Theisen <ttheisen@fedoraproject.org> - 8.8.15-2
- Adjust for Python 3.10 on 32-bit platforms

* Mon Aug 23 2021 Tim Theisen <ttheisen@fedoraproject.org> - 8.8.15-1
- Update to latest upstream 8.8.15
- Fix for security issue
- https://research.cs.wisc.edu/htcondor/security/vulnerabilities/HTCONDOR-2021-0003.html

* Fri Aug 06 2021 Jonathan Wakely <jwakely@redhat.com> - 8.8.10-8
- Rebuilt for Boost 1.76

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.8.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 8.8.10-6
- Rebuilt for Python 3.10

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 8.8.10-5
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.8.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 8.8.10-3
- Rebuilt for Boost 1.75

* Mon Oct 05 2020 Ben Cotton <bcotton@fedoraproject.org> - 8.8.10-2
- Add explicit BR for python3-setuptools

* Thu Aug 06 2020 Ben Cotton <bcotton@fedoraproject.org> - 8.8.10-1
- Update to latest upstream 8.8.10

* Mon Aug 03 2020 Ben Cotton <bcotton@fedoraproject.org> 8.8.8-7
- Fix cmake build issues

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.8.8-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.8.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 29 2020 Jonathan Wakely <jwakely@redhat.com> - 8.8.8-4
- Rebuilt for Boost 1.73

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 8.8.8-3
- Rebuilt for Python 3.9

* Tue May 12 2020 Tim Theisen <ttheisen@fedoraproject.org> - 8.8.8-2
- Account for python 3.9 and future rhbz#1791764

* Thu Apr 09 2020 Tim Theisen <ttheisen@fedoraproject.org> - 8.8.8-1
- Update to latest upstream 8.8.8

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.8.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 8.8.4-2
- Rebuilt for Python 3.8

* Tue Jul 30 2019 Tim Theisen <ttheisen@fedoraproject.org> - 8.8.4-1
- Update to latest upstream 8.8.4

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 18 2019 Ben Cotton <bcotton@fedoraproject.org> 8.6.13-1
- Update to latest upstream 8.6.13

* Mon Jun 17 2019 Ben Cotton <bcotton@fedoraproject.org> 8.6.11-5
- Fix FTBFS

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.6.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.6.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Ben Cotton <bcotton@fedoraproject.org> - 8.6.11-2
- Remove unnecessary ldconfig call in %post

* Thu Jun 07 2018 Tim Theisen <ttheisen@fedoraproject.org> - 8.6.11-1
- Update to latest upstream 8.6.11
- Add shared port patch rhbz#1575974

* Tue May 01 2018 Jonathan Wakely <jwakely@redhat.com> - 8.6.10-2
- Add BuildRequires: boost-python2-devel to fix build with boost-1.66.0-7.fc29

* Tue Mar 20 2018 Tim Theisen <ttheisen@fedoraproject.org> - 8.6.10-1
- Update to latest upstream 8.6.10

* Sun Feb 18 2018 Ben Cotton <bcotton@fedoraproject.org> - 8.6.9-4
- Add BuildRequires for gcc and g++

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.6.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Feb 02 2018 Tim Theisen <ttheisen@fedoraproject.org> - 8.6.9-2
- Rebuilt for Boost 1.66

* Fri Jan 12 2018 Tim Theisen <ttheisen@fedoraproject.org> - 8.6.9-1
- Update to latest upstream 8.6.9

* Mon Nov 13 2017 Tim Theisen <ttheisen@fedoraproject.org> - 8.6.8-1
- Update to latest upstream 8.6.8

* Thu Nov 02 2017 Tim Theisen <ttheisen@fedoraproject.org> - 8.6.7-1
- Update to latest upstream 8.6.7

* Wed Sep 13 2017 Ben Cotton <bcotton@fedoraproject.org> - 8.6.6-1
- Update to latest upstream 8.6.6

* Sun Aug 20 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 8.6.5-3
- Add Provides for the old name without %%_isa

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 8.6.5-2
- Python 2 binary package renamed to python2-condor
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Aug 03 2017 Ben Cotton <bcotton@fedoraproject.org> - 8.6.5-1
- Update to latest upstream 8.6.5

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.6.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Kalev Lember <klember@redhat.com> - 8.6.4-2
- Rebuilt for Boost 1.64

* Fri Jul 07 2017 Ben Cotton <bcotton@fedoraproject.org> - 8.6.4-1
- Update to latest upstream 8.6.4

* Wed May 17 2017 Tim Theisen <ttheisen@fedoraproject.org> - 8.6.3-1
- Update to latest upstream 8.6.3

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Tue Apr 25 2017 Ben Cotton <bcotton@fedoraproject.org> - 8.6.2-1
- Update to latest upstream 8.6.2
- Drop patch glexec_privsep_helper.patch which was incorporated upstream

* Wed Apr 05 2017 Ben Cotton <bcotton@fedoraproject.org> - 8.6.1-2
- Update a patch to match guidance from upstream project

* Thu Mar 23 2017 Ben Cotton <bcotton@fedoraproject.org> - 8.6.1-1
- Update to latest source 8.6.1
- Remove the deltacloud package (removed upstream)
- Add additional files generated by new upstream release

* Thu Mar 09 2017 Ben Cotton <bcotton@fedoraproject.org> - 8.5.2-5
- Add a BuildRequires for boost-python

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug 22 2016 Ben Cotton <bcotton@fedoraproject.org> - 8.5.2-3
- Add an explicit requirement for the voms package

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.5.2-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Feb 19 2016 Ben Cotton <bcotton@fedoraproject.org> - 8.5.2-1
- Update to latest source 8.5.2
- Enable HTCondor's Ganglia daemon
- Add package for openstack_gahp

* Wed Feb 17 2016 Ben Cotton <bcotton@fedoraproject.org> - 8.5.1-4
- Remove aviary to fix FTBFS issues
- Correct the location of the panda plugin

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 8.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 8.5.1-2
- Rebuilt for Boost 1.60

* Tue Dec 22 2015 Ben Cotton <bcotton@fedoraproject.org> - 8.5.1-1
- Update to latest source 8.5.1
- Drop patch for aarch64 (rhbz#1259666), since it is included upstream now

* Wed Oct 14 2015 Ben Cotton <bcotton@fedoraproject.org> - 8.5.0-1
- Update to latest source 8.5.0

* Thu Oct 01 2015 Ben Cotton <bcotton@fedoraproject.org> - 8.3.8-1
- Update to latest source 8.3.8
- Create /var/run/condor at install time - rhbz#1213472
- Correct the specification of the perl(Data::Dumper) build requirement - rhbz#1260602
- Put the libclassad Python library in the right place - rhbz#1201389 (thanks to Matt Williams <matt@milliams.com>)

* Thu Sep 03 2015 Marcin Juszkiewicz <mjuszkiewicz@redhat.com> - 8.3.6-4
- fix typedef conflict resulting in ftbfs on aarch64 - rhbz#1259666

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 8.3.6-3
- Rebuilt for Boost 1.59

* Tue Jul 28 2015 Adam Williamson <awilliam@redhat.com> - 8.3.6-2
- backport fix for compile error caused by change in globus-gsi-credential 7.9

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com>
- rebuild for Boost 1.58

* Thu Jun 25 2015 Ben Cotton <bcotton@fedoraproject.org> - 8.3.6-1
- Update to latest source 8.3.6
- Re-enable aviary

* Wed Jun 17 2015 Matthew Farrellee <matt@redhat> - 8.3.5-1
- Update to latest source 8.3.5
- Disable aviary
- Moved 00personal_condor.config to SOURCES, removed upstream

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 8.3.1-3
- Rebuilt for GCC 5 C++11 ABI change

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 8.3.1-2
- Rebuild for boost 1.57.0

* Sat Nov 22 2014 Matthew Farrellee <matt@redhat> - 8.3.1-1
- Update to latests source 8.3.1
- Build from tag instead of commit SHA
- Disabled plumage (mongodb dep)
- New require perl-Data-Dumper for param table generator
- Updated libpyclassad lib version to 8.3.1
- No longer stripping condor_load_history or config_fetch, removed upstream
- Now including condor_pool_job_report and associated man pages

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.1.4-7.a1a7df5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Aug 14 2014 Dan Horák <dan[at]danny.cz> - 8.1.4-6.a1a7df5
- mongodb exists only on selected arches

* Sun Jun 29 2014 Peter Robinson <pbrobinson@fedoraproject.org> 8.1.4-5.a1a7df5
- don't build plumage on aarch64 as we don't (yet) have v8/mongodb

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.1.4-4.a1a7df5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 8.1.4-3.a1a7df5
- Rebuild for boost 1.55.0

* Fri May 23 2014 David Tardon <dtardon@redhat.com> - 8.1.4-2.a1a7df5
- rebuild for boost 1.55.0

* Thu Mar  6 2014 <eerlands@redhat.com> - 8.1.4-1.a1a7df5
- Update to latest source 8.1.4
- Added new bosco man pages and quickstart, however commented bosco out until the config it drops no longer breaks general condor config
- new man pages for condor_{drain, install, ping, rmdir, tail, who}
- Added condor_{dagman_metrics_reporter, history_helper, pid_ns_init, fetch, urlfetch, sos, testwritelog}
- gce_gahp
- libpyclassad2.7_8_1_4.so
- disabling new ganglia support for a rev or two
- Overhaul and cleanup spec file
- turned off management, no support for qmf: -DWITH_MANAGEMENT:BOOL=FALSE
- added patch Werror_replace.patch, to turn off the cmake regex-replace hack that removes "-Werror", as it breaks the new cflag "-Werror=format-security" passed in from build system
- BuildRequires for python-devel and python-libs
- turned off SMP for make until doc build stops breaking with it
- Archived legacy history

* Sat Jun 22 2013 <tstclair@redhat.com> - 8.1.0-0.2
- Fix for aviary hadoop field swap

* Wed Jun 19 2013 <tstclair@redhat.com> - 8.1.0-0.1
- Update to latest uw/master

* Fri Mar 15 2013 <tstclair@redhat.com> - 7.9.5-0.2
- Update build dependencies

* Thu Feb 28 2013 <tstclair@redhat.com> - 7.9.5-0.1
- Fast forward to 7.9.5 pre-release

* Thu Feb 14 2013 Brian Bockelman <bbockelm@cse.unl.edu> - 7.9.5-0.1.4e2a2ef.git
- Re-sync with master.
- Use upstream python bindings.

* Sun Feb 10 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 7.9.1-0.1.5
- Rebuild for Boost-1.53.0

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 7.9.1-0.1.4
- Rebuild for Boost-1.53.0

* Sat Feb  2 2013 Brian Bockelman <bbockelm@cse.unl.edu> - 7.9.4-0.4.d028b17.git
- Re-sync with master.

* Wed Jan  2 2013 Brian Bockelman <bbockelm@cse.unl.edu> - 7.9.4-0.1.dce3324.git
- Add support for python bindings.

* Thu Dec  6 2012 Brian Bockelman <bbockelm@cse.unl.edu> - 7.9.3-0.6.ce12f50.git
- Fix compile for CREAM.

* Thu Dec  6 2012 Brian Bockelman <bbockelm@cse.unl.edu> - 7.9.3-0.5.ce12f50.git
- Merge code which has improved blahp file cleanup.

* Tue Oct 30 2012 Brian Bockelman <bbockelm@cse.unl.edu> - 7.9.2-0.2.b714b0e.git
- Re-up to the latest master.
- Add support for syslog.

* Thu Oct 11 2012 Brian Bockelman <bbockelm@cse.unl.edu> - 7.9.1-0.14.b135441.git
- Re-up to the latest master.
- Split out a separate package for BOSCO.

* Tue Sep 25 2012 Brian Bockelman <bbockelm@cse.unl.edu> - 7.9.1-0.13.c7df613.git
- Rebuild to re-enable blahp.

* Mon Sep 24 2012 Brian Bockelman <bbockelm@cse.unl.edu> - 7.9.1-0.12.c7df613.git
- Update to capture the latest security fixes.
- CGAHP scalability fixes have been upstreamed.

* Thu Aug 16 2012 <tstclair@redhat.com> - 7.9.1-0.1
- Fast forward to 7.9.1 pre-release
- Fix CVE-2012-3416

* Wed Aug 15 2012 Brian Bockelman <bbockelm@cse.unl.edu> - 7.9.1-0.11.ecc9193.git
- Fixes to the JobRouter configuration.

* Tue Aug 14 2012 Brian Bockelman <bbockelm@cse.unl.edu> - 7.9.1-0.10.9e05bd9.git
- Update to latest trunk so we can get the EditInPlace JobRouter configs.

* Tue Aug 14 2012 Brian Bockelman <bbockelm@cse.unl.edu> - 7.9.1-0.9.70b9542.git
- Fix to IP-verify from ZKM.

* Tue Jul 24 2012 Brian Bockelman <bbockelm@cse.unl.edu> - 7.9.1-0.6.ceb6a0a.git
- Fix per-user condor config to be more useful.  See gt3158

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.9.0-0.1.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 16 2012 Brian Bockelman <bbockelm@cse.unl.edu> - 7.9.1-0.5.ceb6a0a.git
- Upstreaming of many of the custom patches.

* Mon Jul 16 2012 Brian Bockelman <bbockelm@cse.unl.edu> - 7.9.1-0.4.ceb6a0a.git
- Integrate CREAM support from OSG.
- Create CREAM sub-package.

* Fri Jul 13 2012 Brian Bockelman <bbockelm@cse.unl.edu> - 7.9.1-0.2.013069b.git
- Hunt down segfault bug.

* Fri Jul 13 2012 Brian Bockelman <bbockelm@cse.unl.edu> - 7.9.1-0.1.013069b.git
- Update to latest master.

* Tue Jun 19 2012 Brian Bockelman <bbockelm@cse.unl.edu> - 7.9.0-0.14.888a81cgit
- Fix DNS-based hostname checks for GSI.
- Add the user lock directory to the file listing.

* Sun Jun 17 2012 Brian Bockelman <bbockelm@cse.unl.edu> - 7.9.0-0.13.888a81cgit
- Patch for C-GAHP client scalability.

* Fri Jun 15 2012 Brian Bockelman <bbockelm@cse.unl.edu> - 7.9.0-0.12.888a81cgit
- Fix re-acquisition of routed jobs on JR restart.
- Allow DNS-based hostname checks for GSI.
- Allow the queue super-user to impersonate any other user.

* Sat Jun 2 2012 Brian Bockelman <bbockelm@cse.unl.edu> - 7.9.0-0.11.888a81cgit
- Fix proxy handling for Condor-C submissions.

* Wed May 30 2012 Brian Bockelman <bbockelm@cse.unl.edu> - 7.9.0-0.10.888a81cgit
- Fix blahp segfault and GLOBUS_LOCATION.
- Allow a 2-schedd setup for JobRouter.

* Mon May 28 2012 Brian Bockelman <bbockelm@cse.unl.edu> - 7.9.0-0.8.257bc70git
- Re-enable blahp

* Thu May 17 2012 Brian Bockelman <bbockelm@cse.unl.edu> - 7.9.0-0.7.257bc70git
- Fix reseting of cgroup statistics.

* Wed May 16 2012 Brian Bockelman <bbockelm@cse.unl.edu> - 7.9.0-0.6.257bc70git
- Fix for procd when there is no swap accounting.
- Allow condor_defrag to cancel draining when it is happy with things.

* Fri May 11 2012 Brian Bockelman <bbockelm@cse.unl.edu> - 7.9.0-0.5.257bc70git
- Fix for autofs support.

* Fri Apr 27 2012 <tstclair@redhat.com> - 7.9.0-0.1
- Fast forward to 7.9.0 pre-release

* Mon Apr 09 2012 Brian Bockelman <bbockelm@cse.unl.edu> - 7.9.0-0.1.2693346git.1
- Update to the 7.9.0 branch.
