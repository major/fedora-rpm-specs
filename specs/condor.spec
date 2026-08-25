# Set the version and release here
%global condor_version 25.13.2
%global condor_release 1

# set uw_build to 0 for downstream (Fedora or EPEL)
# UW build includes stuff for testing and tarballs
%global uw_build 0

# We need to define the dist for SUSE
%if 0%{?suse_version}
%global _libexecdir %{_exec_prefix}/libexec
%if %{suse_version} == 1500
# Hard code this special case
%if "%{os_release_id}" == "sles"
%global dist .sles15sp5
%else
%global dist .leap15
%endif
%endif
%if %{suse_version} == 1600
%global dist .leap16
%endif
%endif

#######################
Name: condor
Version: %{condor_version}
%global version_ %(tr . _ <<< %{version})
Release: %{condor_release}%{?dist}
Summary: HTCondor: High Throughput Computing
License: Apache-2.0
URL: https://htcondor.org/
Source0: %{name}-%{condor_version}.tar.gz
Source1: %{name}.sysusers.conf
%if %uw_build
Source2: htcondor.pp
%endif

Patch1: turn-off-warnings-as-errors.patch

ExcludeArch: %{ix86}

# Special arch for AlmaLinux 10
%if 0%{?x86_64_v2}
BuildArch: x86_64_v2
%endif

%if 0%{?rhel} == 8 || 0%{?rhel} == 9 || 0%{?rhel} == 10
# Use gcc-toolset 15 for EL 8, 9, and 10
%global gcctoolset 15
%endif

# Do not check .so files in condor's library directory
# We have an LD_PRELOAD for condor_ssh_to_job there
%global __provides_exclude_from ^%{_libdir}/%{name}/.*\\.so.*$

BuildRequires: cmake >= 3.20
BuildRequires: pcre2-devel
BuildRequires: openssl-devel
BuildRequires: krb5-devel
%if ! 0%{?amzn} && "%{os_release_id}" != "sles"
BuildRequires: libvirt-devel
%endif
BuildRequires: bind-utils
BuildRequires: libX11-devel
%if ! ( 0%{?rhel} >= 10 ) && "%{os_release_id}" != "sles"
BuildRequires: libXScrnSaver-devel
%endif
%if 0%{?suse_version}
BuildRequires: openldap2-devel
%else
BuildRequires: openldap-devel
%endif
BuildRequires: python3-devel
BuildRequires: python3-setuptools
%if 0%{?suse_version}
BuildRequires: rpm-config-SUSE
%else
BuildRequires: redhat-rpm-config
%endif
BuildRequires: sqlite-devel
BuildRequires: perl(Data::Dumper)

BuildRequires: glibc-static
BuildRequires: gcc-c++
BuildRequires: libuuid-devel
BuildRequires: patch
BuildRequires: pam-devel
%if 0%{?suse_version}
BuildRequires: mozilla-nss-devel
%else
BuildRequires: nss-devel
%endif
BuildRequires: openssl-devel
%if 0%{?suse_version}
BuildRequires: libexpat-devel
BuildRequires: dbus-1-devel
%else
BuildRequires: expat-devel
BuildRequires: dbus-devel
%endif
BuildRequires: perl(Archive::Tar)
BuildRequires: perl(XML::Parser)
BuildRequires: perl(Digest::MD5)
BuildRequires: python3-devel
BuildRequires: libcurl-devel

# Authentication build requirements
%if ! 0%{?amzn} && "%{os_release_id}" != "sles"
BuildRequires: voms-devel
%endif
%if "%{os_release_id}" != "sles"
BuildRequires: munge-devel
BuildRequires: scitokens-cpp-devel
%endif

%if 0%{?devtoolset}
BuildRequires: which
BuildRequires: devtoolset-%{devtoolset}-toolchain
%endif

%if 0%{?gcctoolset}
BuildRequires: which
BuildRequires: gcc-toolset-%{gcctoolset}
BuildRequires: gcc-toolset-%{gcctoolset}-gcc-plugin-annobin
%endif

%if 0%{?amzn}
BuildRequires: which
BuildRequires: gcc14
BuildRequires: gcc14-c++
# Unfortunately, the annobin plugin is not provided for gcc 14 on amzn
%undefine _annotated_build
%endif

%if 0%{?suse_version}
%if %{suse_version} == 1500
BuildRequires: gcc12
BuildRequires: gcc12-c++
%endif
%if %{suse_version} == 1600
BuildRequires: gcc15
BuildRequires: gcc15-c++
%endif
%endif

BuildRequires: libuuid-devel
%if 0%{?suse_version}
Requires: libuuid1
%else
Requires: libuuid
%endif

BuildRequires: systemd-devel
%if 0%{?fedora} >= 42 || 0%{?rhel} >= 10 || 0%{?suse_version} >= 1600
BuildRequires:  systemd-rpm-macros
%endif
%if 0%{?suse_version}
BuildRequires: systemd
%else
BuildRequires: systemd-units
%endif
Requires: systemd

%if 0%{?rhel} || 0%{?amzn} || 0%{?fedora}
BuildRequires: python3-sphinx python3-sphinx_rtd_theme
%endif

%if 0%{?suse_version}
BuildRequires: python3-Sphinx python3-sphinx_rtd_theme
%endif

# openssh-server needed for condor_ssh_to_job
Requires: openssh-server

# net-tools needed to provide netstat for condor_who
Requires: net-tools

# cryptsetup needed for encrypted LVM execute partitions
Requires: cryptsetup

Requires: /usr/sbin/sendmail

# Docker credential processing uses json query
Requires: jq

# Useful tools are using the Python bindings
Requires: python3-condor = %{version}-%{release}
Requires: python3-requests

Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%if 0%{?suse_version}
Requires(pre): shadow
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
%else
Requires(pre): shadow-utils
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units
%endif

Requires(post): python3-policycoreutils
%if ! 0%{?suse_version}
Requires(post): selinux-policy-targeted
%endif

# Require libraries that we dlopen
# Ganglia is optional as well as nVidia and cuda libraries
%if ! 0%{?amzn} && "%{os_release_id}" != "sles"
%if 0%{?suse_version}
%if "%{os_release_id}" != "sles"
Requires: libvomsapi1
%endif
%else
Requires: voms
%endif
%endif
%if 0%{?suse_version}
Requires: krb5
Requires: libcom_err2
%if "%{os_release_id}" != "sles"
Requires: libmunge2
%endif
%if %{suse_version} == 1500
Requires: libopenssl1_1
%endif
%if %{suse_version} == 1600
Requires: libopenssl3
%endif
%if "%{os_release_id}" != "sles"
Requires: libSciTokens0
%endif
Requires: libsystemd0
%else
Requires: krb5-libs
Requires: libcom_err
Requires: munge-libs
Requires: openssl-libs
Requires: scitokens-cpp
Requires: systemd-libs
%endif
Requires: rsync

%if %uw_build
# Require tested Pelican packages
Requires: (pelican >= 7.26.0 or pelican-debug >= 7.26.0)
Requires: pelican-osdf-compat >= 7.26.0
%endif

%if ! 0%{?amzn} && "%{os_release_id}" != "sles"
# Require tested Apptainer
%if 0%{?suse_version} == 1500
# Unfortunately, Apptainer is lagging behind on openSUSE 15
Requires: apptainer >= 1.4.5
%else
Requires: apptainer >= 1.5.3
%endif
%endif

# Ensure that our bash completions work
Recommends: bash-completion

#From /usr/share/doc/setup/uidgid (RPM: setup-2.12.2-11)
%if 0%{?fedora} >= 42
# The RPM macros already makes virtual Provides for user and group
%else
Provides: user(condor) = 64
Provides: group(condor) = 64
%endif

%if 0%{?rhel} <= 8
# external-libs package discontinued as of 8.9.9
Obsoletes: %{name}-external-libs < 8.9.9
Provides: %{name}-external-libs = %{version}-%{release}

# Bosco package discontinued as of 9.5.0
Obsoletes: %{name}-bosco < 9.5.0
Provides: %{name}-bosco = %{version}-%{release}

# Blahp provided by condor-blahp as of 9.5.0
Provides: blahp = %{version}-%{release}
Obsoletes: blahp < 9.5.0
%endif

%if 0%{?rhel} <= 9
# externals package discontinued as of 10.8.0
Obsoletes: %{name}-externals < 10.8.0
Provides: %{name}-externals = %{version}-%{release}

# blahp package discontinued as of 10.8.0
Obsoletes: %{name}-blahp < 10.8.0
Provides: %{name}-blahp = %{version}-%{release}

# procd package discontinued as of 10.8.0
Obsoletes: %{name}-procd < 10.8.0
Provides: %{name}-procd = %{version}-%{release}

# all package discontinued as of 10.8.0
Obsoletes: %{name}-all < 10.8.0
Provides: %{name}-all = %{version}-%{release}

# classads package discontinued as of 10.8.0
Obsoletes: %{name}-classads < 10.8.0
Provides: %{name}-classads = %{version}-%{release}

# classads-devel package discontinued as of 10.8.0
Obsoletes: %{name}-classads-devel < 10.8.0
Provides: %{name}-classads-devel = %{version}-%{release}
%endif

%if 0%{?rhel} <= 10
# upgrade-checks package discontinued as of 24.9.0
Obsoletes: %{name}-upgrade-checks < 24.9.0
Provides: %{name}-upgrade-checks = %{version}-%{release}
%endif

%if 0%{?suse_version}
%if %{suse_version} == 1500
%debug_package
%endif
%endif

%description
HTCondor is a specialized workload management system for
compute-intensive jobs. Like other full-featured batch systems, HTCondor
provides a job queuing mechanism, scheduling policy, priority scheme,
resource monitoring, and resource management. Users submit their
serial or parallel jobs to HTCondor, HTCondor places them into a queue,
chooses when and where to run the jobs based upon a policy, carefully
monitors their progress, and ultimately informs the user upon
completion.

#######################
%package devel
Summary: Development files for HTCondor

%description devel
Development files for HTCondor

%if %uw_build
#######################
%package tarball
Summary: Files needed to build an HTCondor tarball
BuildArch: noarch

%description tarball
Files needed to build an HTCondor tarball

%endif

#######################
%package kbdd
Summary: HTCondor Keyboard Daemon
Requires: %name = %version-%release

%description kbdd
The condor_kbdd monitors logged in X users for activity. It is only
useful on systems where no device (e.g. /dev/*) can be used to
determine console idle time.

#######################
%if ! 0%{?amzn} && "%{os_release_id}" != "sles"
%package vm-gahp
Summary: HTCondor's VM Gahp
Requires: %name = %version-%release
Requires: libvirt
%if 0%{?fedora} >= 35 || 0%{?rhel} >= 9 || 0%{?suse_version} >= 1600
Requires: passt
%endif

%description vm-gahp
The condor_vm-gahp enables the Virtual Machine Universe feature of
HTCondor. The VM Universe uses libvirt to start and control VMs under
HTCondor's Startd.

%endif

#######################
%package test
Summary: HTCondor Self Tests
Requires: %name = %version-%release

%description test
A collection of tests to verify that HTCondor is operating properly.

#######################
%package -n python3-condor
Summary: Python bindings for HTCondor
Requires: %name = %version-%release
Requires: python3
Requires: python3-cryptography

%description -n python3-condor
The python bindings allow one to directly invoke the C++ implementations of
the ClassAd library and HTCondor from python


#######################
%package credmon-local
Summary: Local issuer credmon for HTCondor
BuildArch: noarch
Requires: %name = %version-%release
Requires: python3-condor = %{version}-%{release}
Requires: python3-cryptography
Requires: python3-scitokens
Conflicts: %name-credmon-vault

%description credmon-local
The local issuer credmon allows users to obtain credentials from an
admin-configured private SciToken key on the access point and to use those
credentials securely inside running jobs.


#######################
%package credmon-oauth
Summary: OAuth2 credmon for HTCondor
BuildArch: noarch
Requires: %name = %version-%release
Requires: condor-credmon-local = %{version}-%{release}
Requires: python3-requests-oauthlib
Requires: python3-flask
Requires: python3-mod_wsgi
Requires: httpd

%description credmon-oauth
The OAuth2 credmon allows users to obtain credentials from configured
OAuth2 endpoints and to use those credentials securely inside running jobs.


#######################
%package credmon-vault
Summary: Vault credmon for HTCondor
BuildArch: noarch
Requires: %name = %version-%release
Requires: python3-condor = %{version}-%{release}
Requires: python3-cryptography
Requires: python3-urllib3
%if %uw_build
# Although htgettoken is only needed on the submit machine and
#  condor-credmon-vault is needed on both the submit and credd machines,
#  htgettoken is small so it doesn't hurt to require it in both places.
Requires: htgettoken >= 1.1
%endif
Conflicts: %name-credmon-local

%description credmon-vault
The Vault credmon allows users to obtain credentials from Vault using
htgettoken and to use those credentials securely inside running jobs.
Install this package when exclusively using Vault for all HTCondor
credential management.


#######################
%package credmon-multi
Summary: Multi-credmon support for HTCondor
BuildArch: noarch
Requires: %name = %version-%release
Requires: condor-credmon-local = %{version}-%{release}
Requires: python3-urllib3
Requires: htgettoken >= 1.1

%description credmon-multi
Provides concurrent support for the Vault credmon alongside the Local
and (optional) OAuth credmons. This package should be installed instead
of condor-credmon-vault when concurrent support is needed.


#######################
%package -n minicondor
Summary: Configuration for a single-node HTCondor
BuildArch: noarch
Requires: %name = %version-%release
Requires: python3-condor = %version-%release

%description -n minicondor
This example configuration is good for trying out HTCondor for the first time.
It only configures the IPv4 loopback address, turns on basic security, and
shortens many timers to be more responsive.

#######################
%package ap
Summary: Configuration for an Access Point
BuildArch: noarch
Requires: %name = %version-%release
Requires: python3-condor = %version-%release

%description ap
This example configuration is good for installing an Access Point.
After installation, one could join a pool or start an annex.

#######################
%package ep
Summary: Configuration for an Execution Point
BuildArch: noarch
Requires: %name = %version-%release
Requires: python3-condor = %version-%release

%description ep
This example configuration is good for installing an Execution Point.
After installation, one could join a pool or start an annex.

#######################
%package annex-ec2
Summary: Configuration and scripts to make an EC2 image annex-compatible
BuildArch: noarch
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
%if 0%{?fedora} >= 42
# RPM handles user creation automagically in these versions
%else
getent group condor >/dev/null || groupadd --system --gid 64 condor
getent passwd condor >/dev/null || \
  useradd --system --uid 64 --gid condor --home-dir /var/lib/condor \
  --shell /usr/sbin/nologin --comment "Owner of HTCondor Daemons" condor
exit 0
%endif


%prep
# For release tarballs
%setup -q -n %{name}-%{condor_version}
%patch 1 -p1

# fix errant execute permissions
find src -perm /a+x -type f -name "*.[Cch]" -exec chmod a-x {} \;


%build

%if 0%{?suse_version}
%if %{suse_version} == 1500
export CC=/usr/bin/gcc-12
export CXX=/usr/bin/g++-12
%endif
%if %{suse_version} == 1600
export CC=/usr/bin/gcc-15
export CXX=/usr/bin/g++-15
%endif
%endif

%if 0%{?devtoolset}
. /opt/rh/devtoolset-%{devtoolset}/enable
export CC=$(which cc)
export CXX=$(which c++)
%endif

%if 0%{?gcctoolset}
%if 0%{?rhel} <= 9
. /opt/rh/gcc-toolset-%{gcctoolset}/enable
%else
. /usr/lib/gcc-toolset/%{gcctoolset}-env.source
%endif
export CC=$(which cc)
export CXX=$(which c++)
%endif

%if 0%{?amzn}
export CC=$(which gcc14-gcc)
export CXX=$(which gcc14-g++)
%endif

%if 0%{?x86_64_v2}
export CFLAGS="${CFLAGS} -march=x86-64-v2"
export CXXFLAGS="${CXXFLAGS} -march=x86-64-v2"
export FFLAGS="${FFLAGS} -march=x86-64-v2"
export FCFLAGS="${FCFLAGS} -march=x86-64-v2"
%endif

# build man files
%if 0%{?amzn}
# if this environment variable is set, sphinx-build cannot import markupsafe
env -u RPM_BUILD_ROOT make -C docs man
%else
make -C docs man
%endif

%if %uw_build
%global condor_build_id UW_development
%global condor_git_sha -1
%endif

# Any changes here should be synchronized with
# ../debian/rules 

%if 0%{?suse_version} || 0%{?fedora} >= 44
%cmake \
%else
%cmake3 \
%endif
%if %uw_build
       -DBUILDID:STRING=%condor_build_id \
       -DPLATFORM:STRING=${NMI_PLATFORM:-unknown} \
%if "%{condor_git_sha}" != "-1"
       -DCONDOR_GIT_SHA:STRING=%condor_git_sha \
%endif
       -DBUILD_TESTING:BOOL=TRUE \
%else
       -DBUILD_TESTING:BOOL=FALSE \
%endif
%if 0%{?suse_version}
       -DCMAKE_SHARED_LINKER_FLAGS="%{?build_ldflags} -Wl,--as-needed -Wl,-z,now" \
%endif
%if 0%{?rhel} == 8 || 0%{?suse_version} >= 1600
       -DPython3_EXECUTABLE=%__python3 \
%endif
       -DCMAKE_SKIP_RPATH:BOOL=TRUE \
       -DPACKAGEID:STRING=%{version}-%{condor_release} \
       -DCONDOR_PACKAGE_BUILD:BOOL=TRUE \
       -DCONDOR_RPMBUILD:BOOL=TRUE \
%if 0%{?amzn} || "%{os_release_id}" == "sles"
       -DWITH_LIBVIRT:BOOL=FALSE \
       -DWITH_VOMS:BOOL=FALSE \
%endif
%if "%{os_release_id}" == "sles"
       -DWITH_MUNGE:BOOL=FALSE \
       -DWITH_SCITOKENS:BOOL=FALSE \
%endif
       -DCMAKE_INSTALL_PREFIX:PATH=/

%if 0%{?amzn}
cd amazon-linux-build
%else
%if 0%{?rhel} >= 9 || 0%{?fedora} && 0%{?fedora} < 44
cd redhat-linux-build
%endif
%endif

%if 0%{?fedora} >= 44
%cmake_build
%if %uw_build
%cmake_build -t tests
%endif
%else
make %{?_smp_mflags}
%if %uw_build
make %{?_smp_mflags} tests
%endif
%endif

%install
%if 0%{?amzn}
cd amazon-linux-build
%else
%if 0%{?rhel} >= 9 || 0%{?fedora} && 0%{?fedora} < 44
cd redhat-linux-build
%endif
%endif
# installation happens into a temporary location, this function is
# useful in moving files into their final locations
function populate {
  _dest="$1"; shift; _src="$*"
  mkdir -p "%{buildroot}/$_dest"
  mv $_src "%{buildroot}/$_dest"
}

rm -rf %{buildroot}
echo ---------------------------- makefile ---------------------------------
%if 0%{?suse_version}
cd build
%endif
%if 0%{?fedora} >= 44
%cmake_install
%else
make install DESTDIR=%{buildroot}
%endif

# TODO: Fix up cmake and remove this hack
%ifarch s390x
mv %{buildroot}/usr/lib/* %{buildroot}/usr/%{_lib}
%endif

%if %uw_build
%if 0%{?fedora} >= 44
%cmake_build -t tests-tar-pkg
%else
make tests-tar-pkg
%endif
# tarball of tests
%if 0%{?amzn}
cp -p %{_builddir}/%{name}-%{version}/amazon-linux-build/condor_tests-*.tar.gz %{buildroot}/%{_libdir}/condor/condor_tests-%{version}.tar.gz
%else
%if 0%{?rhel} >= 9 || 0%{?fedora}
cp -p %{_builddir}/%{name}-%{version}/redhat-linux-build/condor_tests-*.tar.gz %{buildroot}/%{_libdir}/condor/condor_tests-%{version}.tar.gz
%else
%if 0%{?suse_version}
cp -p %{_builddir}/%{name}-%{version}/build/condor_tests-*.tar.gz %{buildroot}/%{_libdir}/condor/condor_tests-%{version}.tar.gz
%else
cp -p %{_builddir}/%{name}-%{version}/condor_tests-*.tar.gz %{buildroot}/%{_libdir}/condor/condor_tests-%{version}.tar.gz
%endif
%endif
%endif
%endif

# Drop in a symbolic link for backward compatibility
ln -s ../..%{_libdir}/condor/condor_ssh_to_job_sshd_config_template %{buildroot}/%_sysconfdir/condor/condor_ssh_to_job_sshd_config_template

populate /usr/share/doc/condor-%{version}/examples %{buildroot}/usr/share/doc/condor-%{version}/etc/examples/*

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

# Install the basic configuration, a Personal HTCondor config. Allows for
# yum install condor + service condor start and go.
mkdir -p -m0755 %{buildroot}/%{_sysconfdir}/condor/config.d
mkdir -p -m0700 %{buildroot}/%{_sysconfdir}/condor/passwords.d
mkdir -p -m0700 %{buildroot}/%{_sysconfdir}/condor/tokens.d

populate %_sysconfdir/condor/config.d %{buildroot}/usr/share/doc/condor-%{version}/examples/00-security
populate %_sysconfdir/condor/config.d %{buildroot}/usr/share/doc/condor-%{version}/examples/00-minicondor
populate %_sysconfdir/condor/config.d %{buildroot}/usr/share/doc/condor-%{version}/examples/00-access-point
populate %_sysconfdir/condor/config.d %{buildroot}/usr/share/doc/condor-%{version}/examples/00-execution-point
populate %_sysconfdir/condor/config.d %{buildroot}/usr/share/doc/condor-%{version}/examples/00-kbdd
populate %_sysconfdir/condor/config.d %{buildroot}/usr/share/doc/condor-%{version}/examples/50ec2.config

# Install a second config.d directory under /usr/share, used for the
# convenience of software built on top of Condor such as GlideinWMS.
mkdir -p -m0755 %{buildroot}/usr/share/condor/config.d

mkdir -p -m0755 %{buildroot}/%{_var}/log/condor
mkdir -p -m0755 %{buildroot}/%{_sharedstatedir}/condor/spool
mkdir -p -m0755 %{buildroot}/%{_sharedstatedir}/condor/execute
mkdir -p -m0755 %{buildroot}/%{_sharedstatedir}/condor/krb_credentials
mkdir -p -m2770 %{buildroot}/%{_sharedstatedir}/condor/oauth_credentials


# not packaging configure/install scripts
%if ! %uw_build
rm -f %{buildroot}%{_bindir}/make-ap-from-tarball
rm -f %{buildroot}%{_bindir}/make-personal-from-tarball
rm -f %{buildroot}%{_sbindir}/condor_configure
rm -f %{buildroot}%{_sbindir}/condor_install
rm -f %{buildroot}/%{_mandir}/man1/condor_configure.1
rm -f %{buildroot}/%{_mandir}/man1/condor_install.1
%endif

mkdir -p %{buildroot}/%{_var}/www/wsgi-scripts/condor_credmon_oauth
mv %{buildroot}/%{_libexecdir}/condor/condor_credmon_oauth.wsgi %{buildroot}/%{_var}/www/wsgi-scripts/condor_credmon_oauth/condor_credmon_oauth.wsgi

# Move oauth credmon config files out of examples and into config.d
mv %{buildroot}/usr/share/doc/condor-%{version}/examples/condor_credmon_oauth/config/condor/40-oauth-credmon.conf %{buildroot}/%{_sysconfdir}/condor/config.d/40-oauth-credmon.conf
mv %{buildroot}/usr/share/doc/condor-%{version}/examples/condor_credmon_oauth/config/condor/40-oauth-tokens.conf %{buildroot}/%{_sysconfdir}/condor/config.d/40-oauth-tokens.conf
mv %{buildroot}/usr/share/doc/condor-%{version}/examples/condor_credmon_oauth/README.credentials %{buildroot}/%{_var}/lib/condor/oauth_credentials/README.credentials

# Move vault credmon config file out of examples and into config.d
mv %{buildroot}/usr/share/doc/condor-%{version}/examples/condor_credmon_oauth/config/condor/40-vault-credmon.conf %{buildroot}/%{_sysconfdir}/condor/config.d/40-vault-credmon.conf

# install tmpfiles.d/condor.conf
mkdir -p %{buildroot}%{_tmpfilesdir}
install -m 0644 %{buildroot}/usr/share/doc/condor-%{version}/examples/condor-tmpfiles.conf %{buildroot}%{_tmpfilesdir}/%{name}.conf

install -Dp -m0755 %{buildroot}/usr/share/doc/condor-%{version}/examples/condor-annex-ec2 %{buildroot}%{_libexecdir}/condor/condor-annex-ec2

mkdir -p %{buildroot}%{_unitdir}
install -m 0644 %{buildroot}/usr/share/doc/condor-%{version}/examples/condor-annex-ec2.service %{buildroot}%{_unitdir}/condor-annex-ec2.service
install -m 0644 %{buildroot}/usr/share/doc/condor-%{version}/examples/condor.service %{buildroot}%{_unitdir}/condor.service
# Disabled until HTCondor security fixed.
# install -m 0644 %{buildroot}/usr/share/doc/condor-%{version}/examples/condor.socket %{buildroot}%{_unitdir}/condor.socket

mkdir -p %{buildroot}%{_sysusersdir}
install -m 0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/condor.conf

mkdir -p %{buildroot}%{_datadir}/condor/
%if %uw_build
cp %{SOURCE2} %{buildroot}%{_datadir}/condor/
%endif

#Fixups for packaged build, should have been done by cmake

mkdir -p %{buildroot}/usr/share/condor
mv %{buildroot}/usr/%{_lib}/condor/Chirp.jar %{buildroot}/usr/share/condor
mv %{buildroot}/usr/%{_lib}/condor/CondorJava*.class %{buildroot}/usr/share/condor
mv %{buildroot}/usr/%{_lib}/condor/libchirp_client.so %{buildroot}/usr/%{_lib}
mv %{buildroot}/usr/%{_lib}/condor/libcondor_utils_*.so %{buildroot}/usr/%{_lib}

rm -rf %{buildroot}/usr/share/doc/condor-%{version}/LICENSE
rm -rf %{buildroot}/usr/share/doc/condor-%{version}/NOTICE.txt
rm -rf %{buildroot}/usr/share/doc/condor-%{version}/README

# we must place the config examples in builddir so %doc can find them
mv %{buildroot}/usr/share/doc/condor-%{version}/examples %_builddir/%name-%condor_version

# classad3 shouldn't be distributed yet
rm -rf %{buildroot}/usr/lib*/python%{python3_version}/site-packages/classad3

%clean
rm -rf %{buildroot}


%check
# This currently takes hours and can kill your machine...
#cd condor_tests
#make check-seralized

#################
%files
%defattr(-,root,root,-)
%doc LICENSE NOTICE.txt examples
%dir %_sysconfdir/condor/
%config %_sysconfdir/condor/condor_config
%{_tmpfilesdir}/%{name}.conf
%{_unitdir}/condor.service
# Disabled until HTCondor security fixed.
# % {_unitdir}/condor.socket
%{_sysusersdir}/condor.conf
%dir %_datadir/condor/
%_datadir/condor/Chirp.jar
%_datadir/condor/CondorJavaInfo.class
%_datadir/condor/CondorJavaWrapper.class
%if %uw_build
%_datadir/condor/htcondor.pp
%endif
%dir %_sysconfdir/condor/passwords.d/
%dir %_sysconfdir/condor/tokens.d/
%dir %_sysconfdir/condor/config.d/
%config(noreplace) %{_sysconfdir}/condor/config.d/00-security
%dir /usr/share/condor/config.d/
%_libdir/condor/condor_ssh_to_job_sshd_config_template
%_sysconfdir/condor/condor_ssh_to_job_sshd_config_template
%_sysconfdir/bash_completion.d/condor
%_libdir/libchirp_client.so
%_libdir/libcondor_utils_%{version_}.so

%_libdir/condor/libgetpwnam.so
%dir %_libexecdir/condor/
%_libexecdir/condor/cleanup_locally_mounted_checkpoint
%_libexecdir/condor/linux_kernel_tuning
%_libexecdir/condor/accountant_log_fixer
%_libexecdir/condor/check-url
%_libexecdir/condor/condor_annex
%_libexecdir/condor/condor_chirp
%_libexecdir/condor/condor_ssh
%_libexecdir/condor/sshd.sh
%_libexecdir/condor/get_orted_cmd.sh
%_libexecdir/condor/orted_launcher.sh
%_libexecdir/condor/set_batchtok_cmd
%_libexecdir/condor/cred_producer_krb
%_libexecdir/condor/condor_job_router
%_libexecdir/condor/condor_pid_ns_init
%_libexecdir/condor/condor_diagnostic_send_ep_logs
%_libexecdir/condor/condor_urlfetch
%_libexecdir/condor/htcondor_docker_test
%_libexecdir/condor/htcondor_docker_test_arm
%ifarch aarch64 ppc64le x86_64
%_libexecdir/condor/exit_37.sif
%endif
%dir %_libexecdir/condor/singularity_test_sandbox/
%dir %_libexecdir/condor/singularity_test_sandbox/dev/
%dir %_libexecdir/condor/singularity_test_sandbox/proc/
%_libexecdir/condor/singularity_test_sandbox/exit_37
%_libexecdir/condor/singularity_test_sandbox/get_user_ns
%_libexecdir/condor/condor_limits_wrapper.sh
%_libexecdir/condor/condor_rooster
%_libexecdir/condor/condor_schedd.init
%_libexecdir/condor/condor_ssh_to_job_shell_setup
%_libexecdir/condor/condor_ssh_to_job_sshd_setup
%_libexecdir/condor/condor_power_state
%_libexecdir/condor/condor_kflops
%_libexecdir/condor/condor_mips
%_libexecdir/condor/data_plugin
%_libexecdir/condor/box_plugin.py
%_libexecdir/condor/gdrive_plugin.py
%_libexecdir/condor/common-cloud-attributes-google.py
%_libexecdir/condor/common-cloud-attributes-aws.py
%_libexecdir/condor/common-cloud-attributes-aws.sh
%_libexecdir/condor/onedrive_plugin.py
%_libexecdir/condor/curl_plugin
%_libexecdir/condor/condor_shared_port
%_libexecdir/condor/condor_defrag
%_libexecdir/condor/interactive.sub
%_libexecdir/condor/condor_gangliad
%_libexecdir/condor/ce-audit.so
%_libexecdir/condor/adstash/__init__.py
%_libexecdir/condor/adstash/adstash.py
%_libexecdir/condor/adstash/config.py
%_libexecdir/condor/adstash/convert.py
%_libexecdir/condor/adstash/utils.py
%_libexecdir/condor/adstash/ad_sources/__init__.py
%_libexecdir/condor/adstash/ad_sources/ad_file.py
%_libexecdir/condor/adstash/ad_sources/generic.py
%_libexecdir/condor/adstash/ad_sources/registry.py
%_libexecdir/condor/adstash/ad_sources/schedd_history.py
%_libexecdir/condor/adstash/ad_sources/startd_history.py
%_libexecdir/condor/adstash/ad_sources/schedd_job_epoch_history.py
%_libexecdir/condor/adstash/ad_sources/schedd_transfer_epoch_history.py
%_libexecdir/condor/adstash/interfaces/__init__.py
%_libexecdir/condor/adstash/interfaces/elasticsearch.py
%_libexecdir/condor/adstash/interfaces/opensearch.py
%_libexecdir/condor/adstash/interfaces/generic.py
%_libexecdir/condor/adstash/interfaces/json_file.py
%_libexecdir/condor/adstash/interfaces/null.py
%_libexecdir/condor/adstash/interfaces/registry.py
%_libexecdir/condor/annex
%_mandir/man1/condor_advertise.1.gz
%_mandir/man1/condor_check_userlogs.1.gz
%_mandir/man1/condor_chirp.1.gz
%_mandir/man1/condor_config_val.1.gz
%_mandir/man1/condor_dagman.1.gz
%_mandir/man1/condor_dag_checker.1.gz
%_mandir/man1/condor_fetchlog.1.gz
%_mandir/man1/condor_findhost.1.gz
%_mandir/man1/condor_gpu_discovery.1.gz
%_mandir/man1/condor_history.1.gz
%_mandir/man1/condor_hold.1.gz
%_mandir/man1/condor_job_router_info.1.gz
%_mandir/man1/condor_master.1.gz
%_mandir/man1/condor_off.1.gz
%_mandir/man1/condor_on.1.gz
%_mandir/man1/condor_pool_job_report.1.gz
%_mandir/man1/condor_preen.1.gz
%_mandir/man1/condor_prio.1.gz
%_mandir/man1/condor_q.1.gz
%_mandir/man1/condor_qsub.1.gz
%_mandir/man1/condor_qedit.1.gz
%_mandir/man1/condor_qusers.1.gz
%_mandir/man1/condor_reconfig.1.gz
%_mandir/man1/condor_release.1.gz
%_mandir/man1/condor_remote_cluster.1.gz
%_mandir/man1/condor_reschedule.1.gz
%_mandir/man1/condor_restart.1.gz
%_mandir/man1/condor_rm.1.gz
%_mandir/man1/condor_run.1.gz
%_mandir/man1/condor_set_shutdown.1.gz
%_mandir/man1/condor_ssh_start.1.gz
%_mandir/man1/condor_sos.1.gz
%_mandir/man1/condor_ssl_fingerprint.1.gz
%_mandir/man1/condor_status.1.gz
%_mandir/man1/condor_store_cred.1.gz
%_mandir/man1/condor_submit.1.gz
%_mandir/man1/condor_submit_dag.1.gz
%_mandir/man1/condor_test_token.1.gz
%_mandir/man1/condor_token_create.1.gz
%_mandir/man1/condor_token_fetch.1.gz
%_mandir/man1/condor_token_list.1.gz
%_mandir/man1/condor_token_request.1.gz
%_mandir/man1/condor_token_request_approve.1.gz
%_mandir/man1/condor_token_request_auto_approve.1.gz
%_mandir/man1/condor_token_request_list.1.gz
%_mandir/man1/condor_top.1.gz
%_mandir/man1/condor_transfer_data.1.gz
%_mandir/man1/condor_transform_ads.1.gz
%_mandir/man1/condor_update_machine_ad.1.gz
%_mandir/man1/condor_updates_stats.1.gz
%_mandir/man1/condor_upgrade_check.1.gz
%_mandir/man1/condor_urlfetch.1.gz
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
%_mandir/man1/condor_drain.1.gz
%_mandir/man1/condor_ping.1.gz
%_mandir/man1/condor_rmdir.1.gz
%_mandir/man1/condor_tail.1.gz
%_mandir/man1/condor_who.1.gz
%_mandir/man1/condor_now.1.gz
%_mandir/man1/classad_eval.1.gz
%_mandir/man1/classads.1.gz
%_mandir/man1/htcondor-jdl.1.gz
%_mandir/man1/condor_adstash.1.gz
%_mandir/man1/condor_evicted_files.1.gz
%_mandir/man1/condor_watch_q.1.gz
%_mandir/man1/get_htcondor.1.gz
%_mandir/man1/htcondor.1.gz
# bin/condor is a link for checkpoint, reschedule, vacate
%_bindir/condor_submit_dag
%_bindir/condor_who
%_bindir/condor_now
%_bindir/condor_prio
%_bindir/condor_transfer_data
%_bindir/condor_check_userlogs
%_bindir/condor_q
%_libexecdir/condor/condor_transferer
%_libexecdir/condor/condor_container_launcher.sh
%_bindir/condor_docker_enter
%_bindir/condor_qedit
%_bindir/condor_qusers
%_bindir/condor_userlog
%_bindir/condor_release
%_bindir/condor_userlog_job_counter
%_bindir/condor_config_val
%_bindir/condor_reschedule
%_bindir/condor_userprio
%_bindir/condor_check_config
%_bindir/condor_dagman
%_bindir/condor_dag_checker
%_bindir/condor_rm
%_bindir/condor_vacate
%_bindir/condor_run
%_bindir/condor_router_history
%_bindir/condor_router_q
%_bindir/condor_router_rm
%_bindir/condor_vacate_job
%_bindir/condor_findhost
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
%_bindir/condor_ssl_fingerprint
%_bindir/condor_suspend
%_bindir/condor_test_match
%_bindir/condor_token_create
%_bindir/condor_token_fetch
%_bindir/condor_token_request
%_bindir/condor_token_request_approve
%_bindir/condor_token_request_auto_approve
%_bindir/condor_token_request_list
%_bindir/condor_token_list
%_bindir/condor_scitoken_exchange
%_bindir/condor_drain
%_bindir/condor_ping
%_bindir/condor_tail
%_bindir/condor_qsub
%_bindir/condor_pool_job_report
%_bindir/condor_job_router_info
%_bindir/condor_transform_ads
%_bindir/condor_update_machine_ad
%_bindir/condor_nsenter
%_bindir/condor_evicted_files
%_bindir/condor_adstash
%_bindir/condor_remote_cluster
%_bindir/bosco_cluster
%_bindir/condor_ssh_start
%_bindir/condor_test_token
%_bindir/condor_manifest
%_bindir/condor_upgrade_check
%_bindir/condor_join_pool
# sbin/condor is a link for master_off, off, on, reconfig,
# reconfig_schedd, restart
%_sbindir/condor_advertise
%_sbindir/condor_aklog
%_sbindir/condor_credmon_krb
%_sbindir/condor_c-gahp
%_sbindir/condor_c-gahp_worker_thread
%_sbindir/condor_collector
%_sbindir/condor_docker_pat_producer
%_sbindir/condor_credd
%_sbindir/condor_fetchlog
%_sbindir/condor_ft-gahp
%_sbindir/condor_had
%_sbindir/condor_librarian
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
%_sbindir/condor_sos
%_sbindir/condor_startd
%_sbindir/condor_starter
%_sbindir/condor_store_cred
%_sbindir/condor_testwritelog
%_sbindir/condor_updates_stats
%_sbindir/ec2_gahp
%_sbindir/condor_gridmanager
%_sbindir/remote_gahp
%_sbindir/rvgahp_client
%_sbindir/rvgahp_proxy
%_sbindir/rvgahp_server
%_sbindir/AzureGAHPServer
%_sbindir/gce_gahp
%_sbindir/arc_gahp
%_libexecdir/condor/condor_gpu_discovery
%_libexecdir/condor/condor_gpu_utilization
%config(noreplace) %_sysconfdir/condor/ganglia.d/00_default_metrics
%defattr(-,condor,condor,-)
%dir %_var/lib/condor/
%dir %_var/lib/condor/execute/
%dir %_var/lib/condor/spool/
%dir %_var/log/condor/
%defattr(-,root,condor,-)
%dir %_var/lib/condor/oauth_credentials
%defattr(-,root,root,-)
%dir %_var/lib/condor/krb_credentials

###### blahp files #######
%config %_sysconfdir/blah.config
%config %_sysconfdir/blparser.conf
%dir %_sysconfdir/blahp/
%config %_sysconfdir/blahp/condor_local_submit_attributes.sh
%config %_sysconfdir/blahp/flux_local_submit_attributes.sh
%config %_sysconfdir/blahp/kubernetes_local_submit_attributes.sh
%config %_sysconfdir/blahp/lsf_local_submit_attributes.sh
%config %_sysconfdir/blahp/nqs_local_submit_attributes.sh
%config %_sysconfdir/blahp/pbs_local_submit_attributes.sh
%config %_sysconfdir/blahp/sge_local_submit_attributes.sh
%config %_sysconfdir/blahp/slurm_local_submit_attributes.sh
%_bindir/blahpd
%dir %_libexecdir/blahp
%_libexecdir/blahp/*

####### procd files #######
%_sbindir/condor_procd
%_sbindir/gidd_alloc
%_sbindir/procd_ctl
%_mandir/man1/procd_ctl.1.gz
%_mandir/man1/gidd_alloc.1.gz
%_mandir/man1/condor_procd.1.gz

####### classads files #######
%defattr(-,root,root,-)
%_libdir/libclassad.so.*

#################
%files devel
%{_includedir}/condor/chirp_client.h
%{_includedir}/condor/condor_event.h
%{_includedir}/condor/file_lock.h
%{_includedir}/condor/read_user_log.h
%{_libdir}/condor/libchirp_client.a
%{_libdir}/libclassad.a

####### classads-devel files #######
%defattr(-,root,root,-)
%_bindir/classad_functional_tester
%_bindir/classad_version
%_libdir/libclassad.so
%dir %_includedir/classad/
%_includedir/classad/attrrefs.h
%_includedir/classad/classad_distribution.h
%_includedir/classad/classadErrno.h
%_includedir/classad/classad.h
%_includedir/classad/classadCache.h
%_includedir/classad/classad_containers.h
%_includedir/classad/classad_flat_map.h
%_includedir/classad/collectionBase.h
%_includedir/classad/collection.h
%_includedir/classad/common.h
%_includedir/classad/debug.h
%_includedir/classad/exprList.h
%_includedir/classad/exprTree.h
%_includedir/classad/flat_set.h
%_includedir/classad/fnCall.h
%_includedir/classad/indexfile.h
%_includedir/classad/jsonSink.h
%_includedir/classad/jsonSource.h
%_includedir/classad/lexer.h
%_includedir/classad/lexerSource.h
%_includedir/classad/literals.h
%_includedir/classad/matchClassad.h
%_includedir/classad/natural_cmp.h
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

%if %uw_build
#################
%files tarball
%{_bindir}/make-ap-from-tarball
%{_bindir}/make-personal-from-tarball
%{_sbindir}/condor_configure
%{_sbindir}/condor_install
%{_mandir}/man1/condor_configure.1.gz
%{_mandir}/man1/condor_install.1.gz
%endif

#################
%files kbdd
%defattr(-,root,root,-)
%config(noreplace) %_sysconfdir/condor/config.d/00-kbdd
%_sbindir/condor_kbdd

#################
%if ! 0%{?amzn} && "%{os_release_id}" != "sles"
%files vm-gahp
%defattr(-,root,root,-)
%_sbindir/condor_vm-gahp
%_libexecdir/condor/libvirt_simple_script.awk

%endif
#################
%files test
%defattr(-,root,root,-)
%_libexecdir/condor/condor_sinful
%_libexecdir/condor/condor_testingd
%_libexecdir/condor/test_user_mapping
%_libexecdir/condor/test_offer_resources
%{_bindir}/common_transfer_savings.py
%if %uw_build
%_libdir/condor/condor_tests-%{version}.tar.gz
%_libexecdir/condor/ccb_proxy_bench
%_libexecdir/condor/test_dc_std_functiond
%_libexecdir/condor/test_stdf_timer_d
%_libexecdir/condor/test_std_pipe_handlerd
%_libexecdir/condor/test_awaitable_deadline_socketd
%_libexecdir/condor/test_awaitable_deadline_socket_client
%_libexecdir/condor/test_generator
%_libexecdir/condor/memory_exerciser_dinner
%_libexecdir/condor/test_starter_guidance.exe
%endif
# Experimental - not for wider deployment
%_bindir/condor_login
%_sbindir/condor_placementd

%files -n python3-condor
%defattr(-,root,root,-)
%_bindir/condor_top
%_bindir/condor_diagnostics
%_bindir/classad_eval
%_bindir/condor_watch_q
%_bindir/htcondor
/usr/%{_lib}/python%{python3_version}/site-packages/htcondor-*.egg-info/
/usr/%{_lib}/python%{python3_version}/site-packages/htcondor_cli/
/usr/%{_lib}/python%{python3_version}/site-packages/classad2/
/usr/%{_lib}/python%{python3_version}/site-packages/htcondor2/

%files credmon-local
%doc examples/condor_credmon_oauth
%_sbindir/condor_credmon_oauth
%_sbindir/scitokens_credential_producer
%_libexecdir/condor/credmon
%_var/lib/condor/oauth_credentials/README.credentials
%config(noreplace) %_sysconfdir/condor/config.d/40-oauth-credmon.conf
%ghost %_var/lib/condor/oauth_credentials/CREDMON_COMPLETE
%ghost %_var/lib/condor/oauth_credentials/pid

%files credmon-oauth
%_var/www/wsgi-scripts/condor_credmon_oauth
%config(noreplace) %_sysconfdir/condor/config.d/40-oauth-tokens.conf
%ghost %_var/lib/condor/oauth_credentials/wsgi_session_key

%files credmon-vault
%doc examples/condor_credmon_oauth
%_sbindir/condor_credmon_vault
%_bindir/condor_vault_storer
%_libexecdir/condor/credmon
%config(noreplace) %_sysconfdir/condor/config.d/40-vault-credmon.conf
%ghost %_var/lib/condor/oauth_credentials/CREDMON_COMPLETE
%ghost %_var/lib/condor/oauth_credentials/pid

%files credmon-multi
%_bindir/condor_vault_storer

%files -n minicondor
%config(noreplace) %_sysconfdir/condor/config.d/00-minicondor

%files ap
%config(noreplace) %_sysconfdir/condor/config.d/00-access-point

%files ep
%config(noreplace) %_sysconfdir/condor/config.d/00-execution-point

%post
/sbin/ldconfig
%if %uw_build
# Remove obsolete security configuration
rm -f /etc/condor/config.d/00-htcondor-9.0.config
%if 0%{?fedora}
test -x /usr/sbin/selinuxenabled && /usr/sbin/selinuxenabled
if [ $? = 0 ]; then
   restorecon -R -v /var/lock/condor
   setsebool -P condor_domain_can_network_connect 1
   setsebool -P daemons_enable_cluster_mode 1
   semanage port -a -t condor_port_t -p tcp 12345
   # the number of extraneous SELinux warnings on f17 is very high
fi
%endif
test -x /usr/sbin/selinuxenabled && /usr/sbin/selinuxenabled
if [ $? = 0 ]; then
   /usr/sbin/semodule -i /usr/share/condor/htcondor.pp
%if 0%{?rhel} < 9
   /usr/sbin/setsebool -P condor_domain_can_network_connect 1
%endif
   /usr/sbin/setsebool -P daemons_enable_cluster_mode 1
fi
%endif
if [ $1 -eq 1 ] ; then
    # Initial installation 
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%preun
if [ $1 -eq 0 ] ; then
    # Package removal, not upgrade
    /bin/systemctl --no-reload disable condor.service > /dev/null 2>&1 || :
    /bin/systemctl stop condor.service > /dev/null 2>&1 || :
fi

%postun
/sbin/ldconfig
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
# Note we don't try to restart - HTCondor will automatically notice the
# binary has changed and do graceful or peaceful restart, based on its
# configuration

%changelog
* Sun Aug 23 2026 Tim Theisen <ttheisen@fedoraproject.org> - 25.13.2-1
- Bring upstream and Fedora spec file in sync to speed updates - rhbz#2316408
- Also fixes build for f45/rawhide - rhbz#2503824

* Wed Jul 15 2026 Fedora Release Engineering <releng@fedoraproject.org> - 23.9.6-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_45_Mass_Rebuild

* Fri Jun 12 2026 Yaakov Selkowitz <yselkowi@redhat.com> - 23.9.6-17
- Rebuilt for openssl 4.0

* Thu Jun 04 2026 Python Maint <python-maint@redhat.com> - 23.9.6-16
- Rebuilt for Python 3.15

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 23.9.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 23.9.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Mon Jan 12 2026 Jonathan Wakely <jwakely@fedoraproject.org> - 23.9.6-13
- Rebuilt for Boost 1.90

* Thu Oct  2 2025 Daniel P. Berrangé <berrange@redhat.com> - 23.9.6-12
- Exclude build on i686

* Fri Sep 19 2025 Python Maint <python-maint@redhat.com> - 23.9.6-11
- Rebuilt for Python 3.14.0rc3 bytecode

* Fri Aug 15 2025 Python Maint <python-maint@redhat.com> - 23.9.6-10
- Rebuilt for Python 3.14.0rc2 bytecode

* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 23.9.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue Jun 03 2025 Python Maint <python-maint@redhat.com> - 23.9.6-8
- Rebuilt for Python 3.14

* Fri Mar 28 2025 Tim Theisen <ttheisen@fedoraproject.org> - 23.9.6-6
- Address CVE-2025-30093 - rhbz#2355671

* Mon Mar 10 2025 Zbigniew Jędrzejewski-Szmek  <zbyszek@in.waw.pl> - 23.9.6-6
- Add sysusers.d config file to allow rpm to create users/groups automatically

* Fri Mar 07 2025 Tim Theisen <ttheisen@fedoraproject.org> - 23.9.6-5
- Account for unified /usr/bin and /usr/sbin after Fedora 41

* Fri Mar 07 2025 Tim Theisen <ttheisen@fedoraproject.org> - 23.9.6-4
- Account for Unify /usr/bin and /usr/sbin - rhbz#2339993

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 23.9.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Oct 01 2024 Tim Theisen <ttheisen@fedoraproject.org> - 23.9.6-2
- Suppress provides/requires for libfmt - rhbz#2315859

* Mon Sep 16 2024 Tim Theisen <ttheisen@fedoraproject.org> - 23.9.6-1
- Update to latest upstream 23.9.6

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 23.1.0-8
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 23.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 23.1.0-6
- Rebuilt for Python 3.13

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 23.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 23.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Tim Theisen <ttheisen@fedoraproject.org> - 23.1.0-3
- Suppress provides/requires for libfmt - rhbz#2249305

* Thu Jan 18 2024 Jonathan Wakely <jwakely@redhat.com> - 23.1.0-2
- Rebuilt for Boost 1.83

* Fri Nov 10 2023 Tim Theisen <ttheisen@fedoraproject.org> - 23.1.0-1
- Update to latest upstream 23.1.0 - rhbz#2247369

* Mon Oct 02 2023 Tim Theisen <ttheisen@fedoraproject.org> - 23.0.0-2
- Drop condor-credmon-vault rhbz#2241709

* Sat Sep 30 2023 Tim Theisen <ttheisen@fedoraproject.org> - 23.0.0-1
- Update to latest upstream 23.0.0 - rhbz#1959462
- Fix build issues - rhbz#2114520, rhbz#2172630, rhbz#2172684
- Update to PCRE2 - rhbz#2128284

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
