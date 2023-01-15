# Upstream tarballs use an additional release number
%global ups_rel 1

%if "%{ups_rel}" == "1"
%global name_version %{name}-%{version}
%else
%global name_version %{name}-%{version}-%{ups_rel}
%endif

# follow arch-inclusions for ucx
%ifarch aarch64 ppc64le x86_64
%bcond_without ucx
%else
%bcond_with ucx
%endif

Name:           slurm
Version:        22.05.6
Release:        3%{?dist}
Summary:        Simple Linux Utility for Resource Management
License:        GPLv2 and BSD
URL:            https://slurm.schedmd.com/
Source0:        https://download.schedmd.com/slurm/%{name_version}.tar.bz2
Source1:        slurm.conf
Source2:        slurmdbd.conf
Source3:        slurm-sview.desktop
Source4:        slurm-128x128.png
Source5:        slurm-setuser.in

# Release-style versioning of libslurmfull/libslurm_pmi
Patch0:         slurm_release_version.patch

# Build-related patches
Patch10:        slurm_check_version.patch
Patch11:        slurm_html_doc_path.patch
Patch12:        slurm_perlapi_rpaths.patch

# Other patches
# https://bugs.schedmd.com/show_bug.cgi?id=14868
Patch20:        slurm_runtime_linking.patch
Patch21:        slurm_to_python3.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  dbus-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  man2html
BuildRequires:  perl-devel
BuildRequires:  perl-ExtUtils-MakeMaker
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl-podlators
%if (0%{?epel} != 7)
BuildRequires:  pkgconf
%else
BuildRequires:  pkgconfig
%endif
BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(lua)
BuildRequires:  python3
BuildRequires:  systemd

BuildRequires:  freeipmi-devel
BuildRequires:  gtk2-devel
BuildRequires:  hdf5-devel
BuildRequires:  hwloc-devel
BuildRequires:  libcurl-devel
BuildRequires:  libssh2-devel
BuildRequires:  lz4-devel
BuildRequires:  mariadb-devel
BuildRequires:  munge-devel
# numctl-devel not available in el9 for arch s390x (#2099483);
# task/affinity plugin won't be available in el9 for arch s390x
%if (0%{?epel} != 9) || ("%{_arch}" != "s390x")
BuildRequires:  numactl-devel
%endif
BuildRequires:  pam-devel
BuildRequires:  pmix-devel
BuildRequires:  rdma-core-devel
BuildRequires:  readline-devel
BuildRequires:  rrdtool-devel
BuildRequires:  zlib-devel

%if 0%{?fedora} && %{with ucx}
BuildRequires:  ucx-devel
%endif

# create slurm-slurmrestd package for Fedora >= 34 and EPEL7/8/9
%if (0%{?fedora} >= 34) || (0%{?epel} >= 7)
BuildRequires:  http-parser-devel
BuildRequires:  json-c-devel
BuildRequires:  libjwt-devel
BuildRequires:  libyaml-devel
%endif

# exclude upstream-deprecated 32-bit architectures
ExcludeArch:    armv7hl
ExcludeArch:    i686

Requires:       /bin/mailx
Requires:       munge
Requires:       pmix
%if 0%{?fedora} && %{with ucx}
Requires:       ucx
%endif
%{?systemd_requires}

%description
Slurm is an open source, fault-tolerant, and highly scalable
cluster management and job scheduling system for Linux clusters.
Components include machine status, partition management,
job management, scheduling and accounting modules.

# -------------
# Base Packages
# -------------

%package devel
Summary: Development package for Slurm
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description devel
Development package for Slurm.  This package includes the header files
and libraries for the Slurm API.

%package doc
Summary: Slurm documentation
%description doc
Documentation package for Slurm.  Includes documentation and
html-based configuration tools for Slurm.

%package gui
Summary: Slurm gui and visual tools
Requires: %{name}%{?_isa} = %{version}-%{release}
%description gui
This package contains the Slurm visual tool sview and
its respective man pages.

%package libs
Summary: Slurm shared libraries
%description libs
Slurm shared libraries.

%package rrdtool
Summary: Slurm rrdtool external sensor plugin
Requires: %{name}%{?_isa} = %{version}-%{release}
%description rrdtool
Slurm external sensor plugin for rrdtool. This package is separated from
the base plugins package due to gui dependencies which are unneeded if not
using this plugin.

%package slurmctld
Summary: Slurm controller daemon
Requires: %{name}%{?_isa} = %{version}-%{release}
%description slurmctld
Slurm controller daemon. Used to manage the job queue, schedule jobs,
and dispatch RPC messages to the slurmd processon the compute nodes
to launch jobs.

%package slurmd
Summary: Slurm compute node daemon
Requires: %{name}%{?_isa} = %{version}-%{release}
%description slurmd
Slurm compute node daemon. Used to launch jobs on compute nodes

%package slurmdbd
Summary: Slurm database daemon
Requires: %{name}%{?_isa} = %{version}-%{release}
%description slurmdbd
Slurm database daemon. Used to accept and process database RPCs and upload
database changes to slurmctld daemons on each cluster.

%if (0%{?fedora} >= 34) || (0%{?epel} >= 7)
%package slurmrestd
Summary: Slurm REST API deamon
Requires: %{name}%{?_isa} = %{version}-%{release}
%description slurmrestd
Slurm REST API daemon.  The slurmrestd daemon is designed to allow clients
to communicate with Slurm via a REST API.
%endif

# -----------------
# Contribs Packages
# -----------------

%package contribs
Summary: Perl tools to print Slurm job state information
Requires: %{name}-perlapi%{?_isa} = %{version}-%{release}
%description contribs
Slurm contribution package which includes the programs seff,
sjobexitmod, sjstat and smail.  See their respective man pages
for more information.

%package nss_slurm
Summary: NSS plugin for slurm
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description nss_slurm
nss_slurm is an optional NSS plugin that can permit passwd and group resolution
for a job on the compute node to be serviced through the local slurmstepd
process, rather than through some alternate network-based service such as LDAP,
SSSD, or NSLCD.

%package openlava
Summary: Openlava/LSF wrappers for transition from OpenLava/LSF to Slurm
Requires: %{name}-perlapi%{?_isa} = %{version}-%{release}
%description openlava
OpenLava wrapper scripts used for helping migrate from OpenLava/LSF to Slurm.

%package pam_slurm
Summary: PAM module for restricting access to compute nodes via Slurm
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description pam_slurm
This module restricts access to compute nodes in a cluster where Slurm
is in use.  Access is granted to root, any user with a Slurm-launched job
currently running on the node, or any user who has allocated resources
on the node according to Slurm.

%package perlapi
Summary: Perl API to Slurm
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description perlapi
Perl API package for Slurm.  This package includes the perl API to provide a
helpful interface to Slurm through Perl.

%package torque
Summary: Torque/PBS wrappers for transition from Torque/PBS to Slurm
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-perlapi%{?_isa} = %{version}-%{release}
%description torque
Torque wrapper scripts used for helping migrate from Torque/PBS to Slurm.

%prep
%autosetup -p1 -n %{name_version}
cp %SOURCE1 etc/slurm.conf
cp %SOURCE1 etc/slurm.conf.example
cp %SOURCE2 etc/slurmdbd.conf
cp %SOURCE2 etc/slurmdbd.conf.example
mkdir -p share/applications
mkdir -p share/icons/hicolor/128x128/apps
cp %SOURCE3 share/applications/%{name}-sview.desktop
cp %SOURCE4 share/icons/hicolor/128x128/apps/%{name}.png
mkdir -p extras
cp %SOURCE5 extras/%{name}-setuser.in

%build
aclocal -I auxdir
autoconf
automake --no-force
# use -fcommon for gcc 10 to avoid multiple definition errors
export CFLAGS="%{build_cflags} -fcommon"
# use -z lazy to allow dlopen with unresolved symbols
export LDFLAGS="%{build_ldflags} -Wl,-z,lazy"
%configure \
  --prefix=%{_prefix} \
  --sysconfdir=%{_sysconfdir}/%{name} \
  --with-pam_dir=%{_libdir}/security \
%if 0%{?fedora} && %{with ucx}
  --with-ucx=%{_prefix} \
%endif
  --enable-pam \
  --enable-really-no-cray \
  --enable-shared \
  --enable-x11 \
  --disable-static \
  --disable-debug \
  --disable-salloc-background \
  --disable-partial_attach \
  --with-oneapi=no \
  --with-shared-libslurm \
  --without-rpath
# patch libtool to remove rpaths
sed -i 's|^hardcode_into_libs=.*|hardcode_into_libs=no|g' libtool
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

# configure extras/slurm-setuser script
sed -r '
s|^dir_conf=.*|dir_conf="%{_sysconfdir}/%{name}"|g;
s|^dir_log=.*|dir_log="%{_var}/log/%{name}"|g;
s|^dir_run=.*|dir_run="%{_rundir}/%{name}"|g;
s|^dir_spool=.*|dir_spool="%{_var}/spool/%{name}"|g;
s|^dir_tmpfiles_d=.*|dir_tmpfiles_d="%{_tmpfilesdir}"|g;' \
    extras/%{name}-setuser.in > extras/%{name}-setuser

# build base packages
%make_build

# build contribs packages
# INSTALLDIRS=vendor so perlapi goes to vendor_perl directory
%make_build PERL_MM_PARAMS="INSTALLDIRS=vendor" contrib

%check
# The test binaries need LD_LIBRARY_PATH to find the compiled slurm library
# in the build tree.
%make_build LD_LIBRARY_PATH="%{buildroot}%{_libdir};%{_libdir}" check

%install
%make_install
%make_build DESTDIR=%{buildroot} install-contrib

install -d -m 0755 %{buildroot}%{_sysconfdir}/%{name}
install -d -m 0755 %{buildroot}%{_unitdir}
install -m 0644 -p etc/cgroup.conf.example \
    %{buildroot}%{_sysconfdir}/%{name}
install -m 0644 -p etc/cgroup.conf.example \
    %{buildroot}%{_sysconfdir}/%{name}/cgroup.conf
install -m 0644 -p etc/slurm.conf %{buildroot}%{_sysconfdir}/%{name}
install -m 0644 -p etc/slurm.conf.example %{buildroot}%{_sysconfdir}/%{name}
install -m 0600 -p etc/slurmdbd.conf %{buildroot}%{_sysconfdir}/%{name}
install -m 0600 -p etc/slurmdbd.conf.example %{buildroot}%{_sysconfdir}/%{name}
install -m 0644 -p etc/slurmctld.service %{buildroot}%{_unitdir}
install -m 0644 -p etc/slurmd.service %{buildroot}%{_unitdir}
install -m 0644 -p etc/slurmdbd.service %{buildroot}%{_unitdir}
install -m 0644 -p etc/slurmrestd.service %{buildroot}%{_unitdir}

# tmpfiles.d file for creating /run/slurm dir after reboot
install -d -m 0755 %{buildroot}%{_tmpfilesdir}
cat  >%{buildroot}%{_tmpfilesdir}/%{name}.conf <<EOF
D %{_rundir}/%{name} 0755 root root -
EOF

# logrotate.d file for /var/log/slurm logging
install -d -m 0755 %{buildroot}%{_var}/log/%{name}
install -d -m 0755 %{buildroot}%{_sysconfdir}/logrotate.d
cat >%{buildroot}%{_sysconfdir}/logrotate.d/%{name} <<EOF
%{_var}/log/%{name}/*.log {
    missingok
    notifempty
    copytruncate
    rotate 5
}
EOF

# /var/run/slurm, /var/spool/slurm dirs, (ghost) pid files
install -d -m 0755 %{buildroot}%{_rundir}/%{name}
install -d -m 0755 %{buildroot}%{_var}/spool/%{name}/ctld
install -d -m 0755 %{buildroot}%{_var}/spool/%{name}/d
touch %{buildroot}%{_rundir}/%{name}/slurmctld.pid
touch %{buildroot}%{_rundir}/%{name}/slurmd.pid
touch %{buildroot}%{_rundir}/%{name}/slurmdbd.pid

# install desktop file for sview GTK+ program
desktop-file-install \
    --dir=%{buildroot}%{_datadir}/applications \
    share/applications/%{name}-sview.desktop

# install desktop icon for sview GTK+ program
install -d -m 0755 %{buildroot}%{_datadir}/icons/hicolor/128x128/apps
install -m 0644 share/icons/hicolor/128x128/apps/%{name}.png \
    %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{name}.png

# install the extras/slurm-setuser script
install -m 0755 extras/%{name}-setuser \
    %{buildroot}%{_bindir}/%{name}-setuser

install -m 0755 contribs/sjstat %{buildroot}%{_bindir}/sjstat

# fix perms on these files so debug info is extracted without error
chmod 0755 %{buildroot}%{perl_vendorarch}/auto/Slurm/Slurm.so
chmod 0755 %{buildroot}%{perl_vendorarch}/auto/Slurmdb/Slurmdb.so

# build man pages for contribs perl scripts
for prog in sjobexitmod sjstat mpiexec pbsnodes qalter qdel qhold qrerun qrls \
    qstat qsub bjobs bkill bsub lsid
do
    rm -f %{buildroot}%{_mandir}/man1/${prog}.1
    pod2man %{buildroot}%{_bindir}/${prog} > %{buildroot}%{_mandir}/man1/${prog}.1
done

# contribs docs
install -d -m 0755 %{buildroot}%{_docdir}/%{name}/contribs/lua
install -m 0644 contribs/README %{buildroot}%{_docdir}/%{name}/contribs
install -m 0644 contribs/lua/*.lua %{buildroot}%{_docdir}/%{name}/contribs/lua

# remove libtool archives
find %{buildroot} -name \*.a -o -name \*.la | xargs rm -f
# remove libslurmfull, libslurm_pmi symlinks (non-development, internal libraries)
rm -rf %{buildroot}%{_libdir}/libslurmfull.so
rm -rf %{buildroot}%{_libdir}/libslurm_pmi.so
# remove auth_none plugin
rm -f %{buildroot}%{_libdir}/%{name}/auth_none.so
# remove example plugins
rm -f %{buildroot}%{_libdir}/%{name}/job_submit_defaults.so
rm -f %{buildroot}%{_libdir}/%{name}/job_submit_logging.so
rm -f %{buildroot}%{_libdir}/%{name}/job_submit_partition.so
# remove cray files
rm -f %{buildroot}%{_libdir}/%{name}/*datawarp*.so
rm -f %{buildroot}%{_libdir}/%{name}/*cray*.so
rm -f %{buildroot}%{_mandir}/man5/cray*
rm -f %{buildroot}%{_sbindir}/capmc*
rm -f %{buildroot}%{_sbindir}/slurmsmwd*
# remove perl cruft
rm -f %{buildroot}%{perl_vendorarch}/auto/Slurm*/.packlist
rm -f %{buildroot}%{perl_vendorarch}/auto/Slurm*/Slurm*.bs
rm -f %{buildroot}%{perl_archlib}/perllocal.pod
%if 0%{?fedora} && (0%{?fedora} < 34)
# remove unused slurmrestd service file
rm -f %{buildroot}%{_unitdir}/slurmrestd.service
%endif

%ldconfig_scriptlets devel
%ldconfig_scriptlets libs

# -----
# Slurm
# -----

%files
%doc CONTRIBUTING.md DISCLAIMER META NEWS README.rst RELEASE_NOTES
%license COPYING LICENSE.OpenSSL
%dir %{_libdir}/%{name}
%dir %{_rundir}/%{name}
%dir %{_sysconfdir}/%{name}
%dir %{_var}/log/%{name}
%dir %{_var}/spool/%{name}
%dir %{_var}/spool/%{name}/ctld
%dir %{_var}/spool/%{name}/d
%config(noreplace) %{_sysconfdir}/%{name}/cgroup.conf
%config(noreplace) %{_sysconfdir}/%{name}/slurm.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%{_bindir}/sacct
%{_bindir}/sacctmgr
%{_bindir}/salloc
%{_bindir}/sattach
%{_bindir}/sbatch
%{_bindir}/sbcast
%{_bindir}/scancel
%{_bindir}/scontrol
%{_bindir}/scrontab
%{_bindir}/sdiag
%{_bindir}/sh5util
%{_bindir}/sinfo
%{_bindir}/sprio
%{_bindir}/squeue
%{_bindir}/sreport
%{_bindir}/srun
%{_bindir}/sshare
%{_bindir}/sstat
%{_bindir}/strigger
%{_bindir}/%{name}-setuser
%{_libdir}/%{name}/accounting_storage_*.so
%{_libdir}/%{name}/acct_gather_*.so
%if (0%{?fedora} >= 34) || (0%{?epel} >= 7)
%{_libdir}/%{name}/auth_jwt.so
%endif
%{_libdir}/%{name}/auth_munge.so
%{_libdir}/%{name}/burst_buffer_lua.so
%{_libdir}/%{name}/cgroup_v1.so
%{_libdir}/%{name}/cgroup_v2.so
%{_libdir}/%{name}/cli_filter_*.so
%{_libdir}/%{name}/core_spec_none.so
%{_libdir}/%{name}/cred_*.so
%{_libdir}/%{name}/ext_sensors_none.so
%{_libdir}/%{name}/gres_*.so
%{_libdir}/%{name}/gpu_generic.so
%{_libdir}/%{name}/hash_k12.so
%{_libdir}/%{name}/job_container_*.so
%{_libdir}/%{name}/job_submit_*.so
%{_libdir}/%{name}/jobacct_gather_*.so
%{_libdir}/%{name}/jobcomp_*.so
%{_libdir}/%{name}/launch_slurm.so
%{_libdir}/%{name}/mcs_*.so
%{_libdir}/%{name}/mpi_*.so
%{_libdir}/%{name}/node_features_*.so
%{_libdir}/%{name}/power_none.so
%{_libdir}/%{name}/preempt_*.so
%{_libdir}/%{name}/prep_script.so
%{_libdir}/%{name}/priority_*.so
%{_libdir}/%{name}/proctrack_*.so
%{_libdir}/%{name}/route_*.so
%{_libdir}/%{name}/sched_*.so
%{_libdir}/%{name}/select_*.so
%{_libdir}/%{name}/serializer_*.so
%{_libdir}/%{name}/site_factor_none.so
%{_libdir}/%{name}/slurmctld_nonstop.so
%{_libdir}/%{name}/switch_*.so
%{_libdir}/%{name}/task_*.so
%{_libdir}/%{name}/topology_*.so
%{_mandir}/man1/sacct.1*
%{_mandir}/man1/sacctmgr.1*
%{_mandir}/man1/salloc.1*
%{_mandir}/man1/sattach.1*
%{_mandir}/man1/sbatch.1*
%{_mandir}/man1/sbcast.1*
%{_mandir}/man1/scancel.1*
%{_mandir}/man1/scontrol.1*
%{_mandir}/man1/scrontab.1*
%{_mandir}/man1/sdiag.1*
%{_mandir}/man1/sh5util.1*
%{_mandir}/man1/sinfo.1*
%{_mandir}/man1/slurm.1*
%{_mandir}/man1/sprio.1*
%{_mandir}/man1/squeue.1*
%{_mandir}/man1/sreport.1*
%{_mandir}/man1/srun.1*
%{_mandir}/man1/sshare.1*
%{_mandir}/man1/sstat.1*
%{_mandir}/man1/strigger.1*
%{_mandir}/man5/acct_gather.conf.5*
%{_mandir}/man5/burst_buffer.conf.5*
%{_mandir}/man5/cgroup.conf.5*
%{_mandir}/man5/ext_sensors.conf.5*
%{_mandir}/man5/gres.conf.5*
%{_mandir}/man5/helpers.conf.5*
%{_mandir}/man5/job_container.conf.5*
%{_mandir}/man5/knl.conf.5*
%{_mandir}/man5/mpi.conf.5*
%{_mandir}/man5/nonstop.conf.5*
%{_mandir}/man5/oci.conf.5*
%{_mandir}/man5/slurm.conf.5*
%{_mandir}/man5/topology.conf.5*
%{_mandir}/man8/slurmrestd.8*
%{_mandir}/man8/spank.8*
%{_sysconfdir}/%{name}/cgroup*.conf.example
%{_sysconfdir}/%{name}/slurm.conf.example
%{_tmpfilesdir}/slurm.conf

# -----------
# Slurm-devel
# -----------

%files devel
%dir %{_includedir}/%{name}
%dir %{_libdir}/%{name}/src
%dir %{_libdir}/%{name}/src/sattach
%dir %{_libdir}/%{name}/src/srun
%{_includedir}/%{name}/pmi*.h
%{_includedir}/%{name}/slurm.h
%{_includedir}/%{name}/slurm_errno.h
%{_includedir}/%{name}/slurm_version.h
%{_includedir}/%{name}/slurmdb.h
%{_includedir}/%{name}/smd_ns.h
%{_includedir}/%{name}/spank.h
%{_libdir}/libpmi.so
%{_libdir}/libpmi2.so
%{_libdir}/libslurm.so
%{_libdir}/%{name}/src/sattach/sattach.wrapper.c
%{_libdir}/%{name}/src/srun/srun.wrapper.c

# ---------
# Slurm-doc
# ---------

%files doc
%{_docdir}

# ---------
# Slurm-gui
# ---------

%files gui
%{_bindir}/sview
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_mandir}/man1/sview.1*

%if (0%{?epel} == 7)
%post gui
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun gui
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans gui
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
%endif

# ----------
# Slurm-libs
# ----------

%files libs
%{_libdir}/libpmi.so.0*
%{_libdir}/libpmi2.so.0*
%{_libdir}/libslurm.so.*
%{_libdir}/libslurmfull-*.so
%{_libdir}/libslurm_pmi-*.so

# -------------
# Slurm-rrdtool
# -------------

%files rrdtool
%{_libdir}/%{name}/ext_sensors_rrd.so

# ---------------
# Slurm-slurmctld
# ---------------

%files slurmctld
%{_mandir}/man8/slurmctld.8*
%{_sbindir}/slurmctld
%{_unitdir}/slurmctld.service
%ghost %{_rundir}/%{name}/slurmctld.pid

# ------------
# Slurm-slurmd
# ------------

%files slurmd
%{_mandir}/man8/slurmd.8*
%{_mandir}/man8/slurmstepd.8*
%{_sbindir}/slurmd
%{_sbindir}/slurmstepd
%{_unitdir}/slurmd.service
%ghost %{_rundir}/%{name}/slurmd.pid

# --------------
# Slurm-slurmdbd
# --------------

%files slurmdbd
%config(noreplace) %{_sysconfdir}/%{name}/slurmdbd.conf
%{_libdir}/%{name}/accounting_storage_mysql.so
%{_mandir}/man5/slurmdbd.conf.5*
%{_mandir}/man8/slurmdbd.8*
%{_sbindir}/slurmdbd
%{_sysconfdir}/%{name}/slurmdbd.conf.example
%{_unitdir}/slurmdbd.service
%ghost %{_rundir}/%{name}/slurmdbd.pid

# ----------------
# Slurm-slurmrestd
# ----------------

%if (0%{?fedora} >= 34) || (0%{?epel} >= 7)
%files slurmrestd
%{_libdir}/%{name}/openapi*.so
%{_libdir}/%{name}/rest*.so
%{_sbindir}/slurmrestd
%{_unitdir}/slurmrestd.service
%endif

# --------------
# Slurm-contribs
# --------------

%files contribs
%dir %{_docdir}/%{name}
%dir %{_docdir}/%{name}/contribs
%dir %{_docdir}/%{name}/contribs/lua
%{_docdir}/%{name}/contribs/README
%{_docdir}/%{name}/contribs/lua/*.lua
%{_bindir}/seff
%{_bindir}/sgather
%{_bindir}/sjobexitmod
%{_bindir}/sjstat
%{_bindir}/smail
%{_mandir}/man1/sgather.1*
%{_mandir}/man1/sjobexitmod.1*
%{_mandir}/man1/sjstat.1*

# ---------------
# Slurm-nss_slurm
# ---------------

%files nss_slurm
%{_libdir}/libnss_slurm.so.2

# --------------
# Slurm-openlava
# --------------

%files openlava
%{_bindir}/bjobs
%{_bindir}/bkill
%{_bindir}/bsub
%{_bindir}/lsid
%{_mandir}/man1/bjobs.1*
%{_mandir}/man1/bkill.1*
%{_mandir}/man1/bsub.1*
%{_mandir}/man1/lsid.1*

# ---------------
# Slurm-pam_slurm
# ---------------

%files pam_slurm
%{_libdir}/security/pam_slurm.so
%{_libdir}/security/pam_slurm_adopt.so

# -------------
# Slurm-perlapi
# -------------

%files perlapi
%dir %{perl_vendorarch}/Slurm
%dir %{perl_vendorarch}/auto/Slurm
%dir %{perl_vendorarch}/auto/Slurmdb
%{_mandir}/man3/Slurm*.3pm*
%{perl_vendorarch}/Slurm.pm
%{perl_vendorarch}/Slurm/*.pm
%{perl_vendorarch}/Slurmdb.pm
%{perl_vendorarch}/auto/Slurm/Slurm.so
%{perl_vendorarch}/auto/Slurmdb/Slurmdb.so
%{perl_vendorarch}/auto/Slurmdb/autosplit.ix

# ------------
# Slurm-torque
# ------------

%files torque
%{_bindir}/generate_pbs_nodefile
%{_bindir}/mpiexec
%{_bindir}/pbsnodes
%{_bindir}/qalter
%{_bindir}/qdel
%{_bindir}/qhold
%{_bindir}/qrerun
%{_bindir}/qrls
%{_bindir}/qstat
%{_bindir}/qsub
%{_libdir}/%{name}/job_submit_pbs.so
%{_libdir}/%{name}/spank_pbs.so
%{_mandir}/man1/pbsnodes.1*
%{_mandir}/man1/qalter.1*
%{_mandir}/man1/qdel.1*
%{_mandir}/man1/qhold.1*
%{_mandir}/man1/qrerun.1*
%{_mandir}/man1/qrls.1*
%{_mandir}/man1/qstat.1*
%{_mandir}/man1/qsub.1*
%{_mandir}/man1/mpiexec.1*

%post slurmctld
%systemd_post slurmctld.service

%preun slurmctld
%systemd_preun slurmctld.service

%postun slurmctld
%systemd_postun_with_restart slurmctld.service

%post slurmd
%systemd_post slurmd.service

%preun slurmd
%systemd_preun slurmd.service

%postun slurmd
%systemd_postun_with_restart slurmd.service

%post slurmdbd
%systemd_post slurmdbd.service

%preun slurmdbd
%systemd_preun slurmdbd.service

%postun slurmdbd
%systemd_postun_with_restart slurmdbd.service

%changelog
%autochangelog
