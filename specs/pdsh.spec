Name: pdsh
Version: 2.34
Release: 14%{?dist}
Summary: Parallel remote shell program
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
Url: https://github.com/chaos/pdsh/
Source0: https://github.com/chaos/pdsh/releases/download/pdsh-2.33/pdsh-%{version}.tar.gz
Requires: pdsh-rcmd
BuildRequires: make
BuildRequires: autoconf, automake, libtool
BuildRequires: perl-generators

# Enabling and disabling pdsh options
#  defaults:
#  enabled:  readline, rsh, ssh, dshgroup, netgroup, debug, nodeupdown, genders
#            torque
#  disabled: rms, mrsh, qshell, mqshell, xcpu, nodeattr, machines, slurm
#
#  To build the various module subpackages, pass --with <pkg> on
#   the rpmbuild command line (if your rpm is a recent enough version)
#  
#  Similarly, to disable various pdsh options pass --without <pkg> on
#   the rpmbuild command line.
#
#  This specfile used to support passing the --with and --without through
#   the environment variables PDSH_WITH_OPTIONS and PDSH_WITHOUT_OPTIONS.
#   e.g. PDSH_WITH_OPTIONS="qshell genders" rpmbuild ....
#   Unfortunately, new rpm doesn't tolerate such nonsense, so it doesn't work anymore.

# Read: If neither macro exists, then add the default definition.
# These are default ENABLED.
%{!?_with_readline: %{!?_without_readline: %global _with_readline --with-readline}}
%{!?_with_rsh: %{!?_without_rsh: %global _with_rsh --with-rsh}}
%{!?_with_ssh: %{!?_without_ssh: %global _with_ssh --with-ssh}}
%{!?_with_dshgroups: %{!?_without_dshgroups: %global _with_dshgroups --with-dshgroups}}
%{!?_with_netgroup: %{!?_without_netgroup: %global _with_netgroup --with-netgroup}}
%{!?_with_debug: %{!?_without_debug: %global _with_debug --with-debug}}
%{!?_with_nodeupdown: %{!?_without_nodeupdown: %global _with_nodeupdown --with-nodeupdown}}
%{!?_with_genders: %{!?_without_genders: %global _with_genders --with-genders}}
%{!?_with_torque: %{!?_without_torque: %global _with_torque --with-torque}}
# These are default DISABLED.
%{!?_with_rms: %{!?_without_rms: %global _without_rms --without-rms}}
%{!?_with_mrsh: %{!?_without_mrsh: %global _without_mrsh --without-mrsh}}
%{!?_with_qshell: %{!?_without_qshell: %global _without_qshell --without-qshell}}
%{!?_with_mqshell: %{!?_without_mqshell: %global _without_mqshell --without-mqshell}}
%{!?_with_xcpu: %{!?_without_xcpu: %global _without_xcpu --without-xcpu}}
%{!?_with_nodeattr: %{!?_without_nodeattr: %global _without_nodeattr --without-nodeattr}}
%{!?_with_machines: %{!?_without_machines: %global _without_machines --without-machines}}
%{!?_with_slurm: %{!?_without_slurm: %global _without_slurm --without-slurm}}

#
# If "--with debug" is set compile with --enable-debug
#   and try not to strip binaries.
#
# (See /usr/share/doc/rpm-*/conditionalbuilds)
#
%if %{?_with_debug:1}%{!?_with_debug:0}
  %global _enable_debug --enable-debug
%endif

# Macro controlled BuildRequires
%{?_with_qshell:BuildRequires: qsnetlibs}
%{?_with_mqshell:BuildRequires: qsnetlibs}
BuildRequires: readline-devel
%{?_with_nodeupdown:BuildRequires: libnodeupdown-devel}
%{?_with_genders:BuildRequires: libgenders-devel > 1.0}
%{?_with_torque:BuildRequires: torque-devel}

%description
Pdsh is a multithreaded remote shell client which executes commands
on multiple remote hosts in parallel.  Pdsh can use several different
remote shell services, including standard "rsh", Kerberos IV, and ssh.

%package qshd
Summary: Remote shell daemon for pdsh/qshell/Elan3
Requires(post):  xinetd

%description qshd
Remote shell service for running Quadrics Elan3 jobs under pdsh.
Sets up Elan capabilities and environment variables needed by Quadrics
MPICH executables.

%package mqshd
Summary: Remote shell daemon for pdsh/mqshell/Elan3
Requires(post):  xinetd

%description mqshd
Remote shell service for running Quadrics Elan3 jobs under pdsh with
mrsh authentication.  Sets up Elan capabilities and environment variables 
needed by Quadrics MPICH executables.

%package   rcmd-rsh
Summary:   Provides bsd rcmd capability to pdsh
Provides:  pdsh-rcmd
Requires:  %{name}%{?_isa} = %{version}-%{release}

%description rcmd-rsh
Pdsh module for bsd rcmd functionality. Note: This module
requires that the pdsh binary be installed setuid root.

%package   rcmd-ssh
Summary:   Provides ssh rcmd capability to pdsh
Provides:  pdsh-rcmd
Requires:  openssh-clients
Requires:  %{name}%{?_isa} = %{version}-%{release}

%description rcmd-ssh
Pdsh module for ssh rcmd functionality.

%package   rcmd-qshell
Summary:   Provides qshell rcmd capability to pdsh
Provides:  pdsh-rcmd
Conflicts: pdsh-rcmd-mqshell
Requires:  %{name}%{?_isa} = %{version}-%{release}

%description rcmd-qshell
Pdsh module for running QsNet MPI jobs. Note: This module
requires that the pdsh binary be installed setuid root.

%package   rcmd-mrsh
Summary:   Provides mrsh rcmd capability to pdsh
Provides:  pdsh-rcmd
Requires:  %{name}%{?_isa} = %{version}-%{release}

%description rcmd-mrsh
Pdsh module for mrsh rcmd functionality.

%package   rcmd-mqshell
Summary:   Provides mqshell rcmd capability to pdsh
Provides:  pdsh-rcmd
Conflicts: pdsh-rcmd-qshell
Requires:  %{name}%{?_isa} = %{version}-%{release}

%description rcmd-mqshell
Pdsh module for mqshell rcmd functionality.

%package   rcmd-xcpu
Summary:   Provides xcpu rcmd capability to pdsh
Provides:  pdsh-xcpu
Requires:  %{name}%{?_isa} = %{version}-%{release}

%description rcmd-xcpu
Pdsh module for xcpu rcmd functionality.

%package   mod-genders
Summary:   Provides libgenders support for pdsh
Requires:  genders >= 1.1
Conflicts: pdsh-mod-nodeattr
Conflicts: pdsh-mod-machines
Requires:  %{name}%{?_isa} = %{version}-%{release}

%description mod-genders
Pdsh module for libgenders functionality.

%package   mod-nodeattr
Summary:   Provides genders support for pdsh using the nodeattr program
Requires:  genders 
Conflicts: pdsh-mod-genders
Conflicts: pdsh-mod-machines
Requires:  %{name}%{?_isa} = %{version}-%{release}

%description mod-nodeattr
Pdsh module for genders functionality using the nodeattr program.

%package   mod-nodeupdown
Summary:   Provides libnodeupdown support for pdsh
Requires:  whatsup
Requires:  %{name}%{?_isa} = %{version}-%{release}

%description mod-nodeupdown
Pdsh module providing -v functionality using libnodeupdown.

%package   mod-rms
Summary:   Provides RMS support for pdsh
Requires:  qsrmslibs
Requires:  %{name}%{?_isa} = %{version}-%{release}

%description mod-rms
Pdsh module providing support for gathering the list of target nodes
from an allocated RMS resource.

%package   mod-machines
Summary:   Pdsh module for gathering list of target nodes from a machines file
Conflicts: pdsh-mod-genders
Conflicts: pdsh-mod-nodeattr
Requires:  %{name}%{?_isa} = %{version}-%{release}

%description mod-machines
Pdsh module for gathering list of all target nodes from a machines file.

%package   mod-dshgroup
Summary:   Provides dsh-style group file support for pdsh
Requires:  %{name}%{?_isa} = %{version}-%{release}

%description mod-dshgroup
Pdsh module providing dsh (Dancer's shell) style "group" file support.
Provides -g groupname and -X groupname options to pdsh.

%package   mod-netgroup
Summary:   Provides netgroup support for pdsh
Requires:  %{name}%{?_isa} = %{version}-%{release}

%description mod-netgroup
Pdsh module providing support for targeting hosts based on netgroup.
Provides -g groupname and -X groupname options to pdsh.

%package   mod-slurm
Summary:   Provides support for running pdsh under SLURM allocations
Requires:  slurm
Requires:  %{name}%{?_isa} = %{version}-%{release}

%description mod-slurm
Pdsh module providing support for gathering the list of target nodes
from an allocated SLURM job.

%package   mod-torque
Summary:   Provides support for running pdsh under Torque jobid
Requires:  torque
Requires:  %{name}%{?_isa} = %{version}-%{release}

%description mod-torque
Pdsh module providing support for running pdsh on Torque nodes.

%prep
%setup -q
chmod +x configure

%build
%configure \
    %{?_enable_debug}       \
    %{?_with_rsh}           \
    %{?_without_rsh}        \
    %{?_with_ssh}           \
    %{?_without_ssh}        \
    %{?_with_qshell}        \
    %{?_without_qshell}     \
    %{?_with_readline}      \
    %{?_without_readline}   \
    %{?_with_machines}      \
    %{?_without_machines}   \
    %{?_with_genders}       \
    %{?_without_genders}    \
    %{?_with_rms}           \
    %{?_without_rms}        \
    %{?_with_nodeupdown}    \
    %{?_without_nodeupdown} \
    %{?_with_nodeattr}      \
    %{?_without_nodeattr}   \
    %{?_with_mrsh}          \
    %{?_without_mrsh}       \
    %{?_with_mqshell}       \
    %{?_without_mqshell}    \
    %{?_with_xcpu}          \
    %{?_without_xcpu}       \
    %{?_with_slurm}         \
    %{?_without_slurm}      \
    %{?_with_dshgroups}     \
    %{?_without_dshgroups}  \
    %{?_with_netgroup}      \
    %{?_without_netgroup}   \
    %{?_with_torque}        \
    %{?_without_torque}

# FIXME: build fails when trying to build with _smp_mflags if qsnet is enabled
# make %{_smp_mflags} CFLAGS="$RPM_OPT_FLAGS"
make CFLAGS="$RPM_OPT_FLAGS"

%install
mkdir -p $RPM_BUILD_ROOT
DESTDIR="$RPM_BUILD_ROOT" make install
if [ -x $RPM_BUILD_ROOT/%{_sbindir}/in.qshd ]; then
   install -D -m644 etc/qshell.xinetd $RPM_BUILD_ROOT/%{_sysconfdir}/xinetd.d/qshell
fi
if [ -x $RPM_BUILD_ROOT/%{_sbindir}/in.mqshd ]; then
   install -D -m644 etc/mqshell.xinetd $RPM_BUILD_ROOT/%{_sysconfdir}/xinetd.d/mqshell
fi
# according to developer: .so's are modules not really libraries .a's and
# .la's don't need to be packaged.
rm $RPM_BUILD_ROOT/%{_libdir}/pdsh/*a

%files
%doc README NEWS DISCLAIMER.* README.KRB4 README.modules
%license COPYING
%{_bindir}/pdsh
%{_bindir}/pdcp
%{_bindir}/dshbak
%{_bindir}/rpdcp
%dir %{_libdir}/pdsh
%{_libdir}/pdsh/execcmd.so
%{_mandir}/man1/*

%if %{?_with_rsh:1}%{!?_with_rsh:0}
%files rcmd-rsh
%{_libdir}/pdsh/xrcmd.*
%endif

%if %{?_with_ssh:1}%{!?_with_ssh:0}
%files rcmd-ssh
%{_libdir}/pdsh/sshcmd.*
%endif

%if %{?_with_qshell:1}%{!?_with_qshell:0}
%files rcmd-qshell
%{_libdir}/pdsh/qcmd.*
%endif

%if %{?_with_mrsh:1}%{!?_with_mrsh:0}
%files rcmd-mrsh
%{_libdir}/pdsh/mcmd.*
%endif

%if %{?_with_mqshell:1}%{!?_with_mqshell:0}
%files rcmd-mqshell
%{_libdir}/pdsh/mqcmd.*
%endif

%if %{?_with_xcpu:1}%{!?_with_xcpu:0}
%files rcmd-xcpu
%{_libdir}/pdsh/xcpucmd.*
%endif

%if %{?_with_genders:1}%{!?_with_genders:0}
%files mod-genders
%{_libdir}/pdsh/genders.*
%endif

%if %{?_with_nodeattr:1}%{!?_with_nodeattr:0}
%files mod-nodeattr
%{_libdir}/pdsh/nodeattr.*
%endif

%if %{?_with_nodeupdown:1}%{!?_with_nodeupdown:0}
%files mod-nodeupdown
%{_libdir}/pdsh/nodeupdown.*
%endif

%if %{?_with_rms:1}%{!?_with_rms:0}
%files mod-rms
%{_libdir}/pdsh/rms.*
%endif

%if %{?_with_machines:1}%{!?_with_machines:0}
%files mod-machines
%{_libdir}/pdsh/machines.*
%endif

%if %{?_with_dshgroups:1}%{!?_with_dshgroups:0}
%files mod-dshgroup
%{_libdir}/pdsh/dshgroup.*
%endif

%if %{?_with_netgroup:1}%{!?_with_netgroup:0}
%files mod-netgroup
%{_libdir}/pdsh/netgroup.*
%endif

%if %{?_with_slurm:1}%{!?_with_slurm:0}
%files mod-slurm
%{_libdir}/pdsh/slurm.*
%endif

%if %{?_with_torque:1}%{!?_with_torque:0}
%files mod-torque
%{_libdir}/pdsh/torque.*
%endif

%if %{?_with_qshell:1}%{!?_with_qshell:0}
%files qshd
%{_sbindir}/in.qshd
%{_sysconfdir}/xinetd.d/qshell

%post qshd
if ! grep "^qshell" /etc/services >/dev/null; then
  echo "qshell            523/tcp                  # pdsh/qshell/elan3" >>/etc/services
fi
%{_initrddir}/xinetd reload

%endif

%if %{?_with_mqshell:1}%{!?_with_mqshell:0}
%files mqshd
%{_sbindir}/in.mqshd
%{_sysconfdir}/xinetd.d/mqshell

%post mqshd
if ! grep "^mqshell" /etc/services >/dev/null; then
  echo "mqshell         21234/tcp                  # pdsh/mqshell/elan3" >>/etc/services
fi
%{_initrddir}/xinetd reload

%endif

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.34-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 2.34-13
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.34-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.34-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.34-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.34-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.34-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.34-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.34-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.34-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.34-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.34-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.34-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 18 2020 Tom Callaway <spot@fedoraproject.org> - 2.34-1
- update to 2.34

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.33-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 18 2019 Tom Callaway <spot@fedoraproject.org> - 2.33-1
- update to 2.33

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.31-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.31-14
- Rebuild for readline 8.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.31-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.31-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.31-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.31-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.31-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.31-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 2.31-7
- Rebuild for readline 7.x

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.31-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 19 2016 Tom Callaway <spot@fedoraproject.org> - 2.31-5
- spec file cleanups

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.31-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.31-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Nov 25 2013 Tom Callaway <spot@fedoraproject.org> - 2.31-1
- update to 2.31

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.26-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 2.26-6
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.26-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jul 23 2012 Tom Callaway <spot@fedoraproject.org> - 2.26-4
- enable mod-genders by default (bz810019)
- enable mod-torque by default

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun May  1 2011 Tom Callaway <spot@fedoraproject.org> - 2.26-1
- update to 2.26

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Sep  9 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 2.22-1
- update to 2.22

* Fri Sep  3 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 2.21-1
- update to 2.21

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Jun 07 2009 Ruben Kerkhof <ruben@rubenkerkhof.com> 2.18-2
- Enable nodeupdown module

* Mon Apr 13 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 2.18-1
- update to 2.18

* Tue Mar 31 2009 Michael Schwendt <mschwendt@fedoraproject.org> - 2.17-3
- fix unowned directories (#473578)
  and let all module subpackages require the main package

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jan 14 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 2.17-1
- update to 2.17
- fix netgroup

* Thu Aug 28 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.16-1
- attempt to make this package suck... less.
- fix license tag
- update to 2.16
- fix compile against glibc 2.8 (ARG_MAX not defined)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.11-6
- Autorebuild for GCC 4.3

* Thu Oct 05 2006 Christian Iseli <Christian.Iseli@licr.org> 2.11-5
 - rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Mon Sep 18 2006 Ben Woodard <woodard@redhat.com> 2.11-4
- bump version for fc6

* Thu Aug 24 2006 Ben Woodard <woodard@redhat.com> 2.11-3
- Remove whatsup requirement for dshgrp and netgroup
- Enable dshgroup and netgroup by default

* Mon Jul 31 2006 Ben Woodard <woodard@redhat.com> 2.11-2
- Hardcode readline-devel dependency.

* Mon Jul 31 2006 Ben Woodard <woodard@redhat.com> 2.11-1
- Track upstream version
- Added dependency on openssh-clients for rcmd-ssh

* Thu Mar 30 2006 Ben Woodard <woodard@redhat.com> 2.10-4
- upstream pointed out that they had added two new subpackages
  that I'd failed to include.

* Thu Mar 30 2006 Ben Woodard <woodard@redhat.com> 2.10-3
- added dist tag so that I can build on multiple versions

* Thu Mar 30 2006 Ben Woodard <woodard@redhat.com> 2.10-2
- new version 2.10-1 used by upstream
- remove release from source line to track upstream
- deleted patch which is no longer needed
- removed -n from setup line. No longer needed.
- hack to fix perms so no longer needed

* Mon Mar 13 2006 Ben Woodard <woodard@redhat.com> 2.8.1-7
- An optimization in pdsh depended on the .la files being there. Removed
  optimization.

* Mon Mar 6 2006 Ben Woodard <woodard@redhat.com> 2.8.1-6
- Add COPYING file to file list
- removed .la packages from sub packages.

* Fri Feb 24 2006 Ben Woodard <woodard@redhat.com> 2.8.1-5
- changed source location to point to main site not mirror.
- inserted version macro in source line

* Thu Feb 23 2006 Ben Woodard <woodard@redhat.com> 2.8.1-4
- changed perms of pdsh and pcp after install so that find-debuginfo.sh finds
  the files and they get stripped.
- removed change of attributes of pdsh and pcp in files section
- removed .a files from packages.

* Wed Feb 22 2006 Ben Woodard <woodard@redhat.com>
- add parameters to make
- replace etc with _sysconfdir in most places
- remove post section with unexplained removing of cached man pages.
- removed dots at end of all summaries.

* Thu Feb 16 2006 Ben Woodard <woodard@redhat.com> 2.8.1-3
- removed dot at end of summary
- removed unused/broken smp build
- changed to using initrddir macro
- changed depricated Prereq to Requires

* Thu Feb 9 2006 Ben Woodard <woodard@redhat.com> 2.8.1-2
- add in rpmlint fixes
- change buildroot

* Wed Feb 8 2006 Mark Grondona <mgrondona@llnl.gov> 2.8.1-1
- pdsh 2.8.1 critical bugfix release

* Wed Feb 1 2006 Ben Woodard <woodard@redhat.com> 2.8-2
- Modified spec file to fix some problems uncovered by rpmlint
