%global _hardened_build 1
%bcond_without selinux

%global preversion rc1

Name:     icecream
Version:  1.4
Release:  %autorelease -p -e %{preversion}
Summary:  Distributed compiler
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:  GPL-2.0-or-later
URL:      https://github.com/icecc/icecream
Source0:  https://github.com/icecc/%{name}/archive/%{version}%{preversion}.tar.gz#/%{name}-%{version}%{preversion}.tar.gz
Source1:  fedora-sysconfig.icecream
Source2:  icecream.module.in
Source3:  icecream.fc
Source4:  icecream.te
Source5:  icecream.if
Source6:  iceccd.service
Source7:  icecc-scheduler.service
Source9:  iceccd-wrapper
Source10: icecc-scheduler-wrapper
Source11: icecream-tmpfiles.conf
Source12: icecream.xml
Source13: icecream-scheduler.xml
Patch1:   0001-Revert-chmod-chown-envs-dir-when-preparing-this.patch
Patch2:   0002-daemon-main-do-not-create-run-icecc-by-ourselves.patch
Patch3:   0003-Ignore-the-suse-directory.patch
Patch4:   0004-do-not-use-usr-bin-env.patch

BuildRequires: gcc-c++
BuildRequires: systemd
BuildRequires: libcap-ng-devel
BuildRequires: lzo-devel libzstd-devel libarchive-devel
BuildRequires: docbook2X
BuildRequires: environment(modules)
BuildRequires: firewalld-filesystem
BuildRequires: autoconf automake libtool

Requires:         firewalld-filesystem
Requires:         environment(modules)
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd
Requires(post):   findutils

%if %{with selinux}
# For SELinux protection:
BuildRequires: checkpolicy selinux-policy-devel hardlink
BuildRequires: make
# semanage is in policycoreutils (EL-5) or policycoreutils-python (Fedora). File dep will work in both.
Requires(post):   policycoreutils /usr/sbin/semanage
Requires(preun):  policycoreutils /usr/sbin/semanage
Requires(postun): policycoreutils
%define selinux_policyver %(sed -e 's,.*selinux-policy-\\([^/]*\\)/.*,\\1,' /usr/share/selinux/devel/policyhelp) 
%if "%{selinux_policyver}" != ""
Requires:         selinux-policy >= %{selinux_policyver}
%endif
%define selinux_variants mls strict targeted 
%endif


# description copied from Debian icecc package
%description
Icecream is a distributed compile system. It allows parallel compiling by
distributing the compile jobs to several nodes of a compile network running the
icecc daemon. The icecc scheduler routes the jobs and provides status and
statistics information to the icecc monitor. Each compile node can accept one
or more compile jobs depending on the number of processors and the settings of
the daemon. Link jobs and other jobs which cannot be distributed are executed
locally on the node where the compilation is started.

%package devel
Summary:  Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: libcap-ng-devel%{?_isa}
Requires: lzo-devel%{?_isa}
Requires: libzstd-devel%{?_isa}
Requires: libarchive-devel%{?_isa}

%description devel
This package contains development files for %{name}.

%prep
%autosetup -p1 -n %{name}-%{version}%{preversion}

mkdir SELinux
cp -p %{SOURCE3} %{SOURCE4} %{SOURCE5} SELinux
mkdir fedora
cp -p %{SOURCE6} %{SOURCE7} %{SOURCE9} %{SOURCE10} %{SOURCE11} fedora

# Create a sysusers.d config file
cat >icecream.sysusers.conf <<EOF
u icecc - 'Icecream distributed compiler' %{_localstatedir}/cache/icecream -
EOF

%build
./autogen.sh

%configure \
    --disable-static \
    --enable-shared \
    --enable-clang-rewrite-includes \
    --enable-clang-wrappers 

sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags}

%if %{with selinux}
pushd SELinux
for selinuxvariant in %{selinux_variants}; do
	make NAME=${selinuxvariant} -f %{_datadir}/selinux/devel/Makefile
	mv icecream.pp icecream.pp.${selinuxvariant}
	make NAME=${selinuxvariant} -f %{_datadir}/selinux/devel/Makefile clean
done
popd
%endif

%check
LD_LIBRARY_PATH=%{buildroot}/%{_libdir} make check

%install
make install DESTDIR=%{buildroot}
rm -f %{buildroot}/%{_libdir}/libicecc.la

# install config file and initscripts
install -d -m 755 %{buildroot}/%{_unitdir}
install -p -m 644 fedora/*.service              %{buildroot}/%{_unitdir}
install -p -m 755 fedora/*-wrapper              %{buildroot}/%{_libexecdir}/icecc
mkdir -p %{buildroot}%{_tmpfilesdir}
install -p -m 644 fedora/icecream-tmpfiles.conf %{buildroot}/%{_tmpfilesdir}/icecream.conf
install -d -m 755 %{buildroot}/%{_sysconfdir}/profile.d

install -m644 -p -D %{SOURCE12} %{buildroot}%{_prefix}/lib/firewalld/services/icecream.xml
install -m644 -p -D %{SOURCE13} %{buildroot}%{_prefix}/lib/firewalld/services/icecream-scheduler.xml

install -D -m 644 %{SOURCE1} %{buildroot}/%{_sysconfdir}/sysconfig/icecream

# create default working dir
mkdir -p %{buildroot}/%{_localstatedir}/cache/icecream

mkdir -p %{buildroot}/run/icecc/

# Make the environment-modules file
mkdir -p %{buildroot}%{_modulesdir}/icecream
sed  's#@LIBEXECDIR@#%{_libexecdir}#' < %{SOURCE2} > %{buildroot}%{_modulesdir}/icecream/icecc

%if %{with selinux}
for selinuxvariant in %{selinux_variants}; do
	install -d %{buildroot}/%{_datadir}/selinux/${selinuxvariant}
	install -p -m 644 -D SELinux/icecream.pp.${selinuxvariant} \
		 %{buildroot}/%{_datadir}/selinux/${selinuxvariant}/icecream.pp
done
# Hardlink identical policy module packages together
hardlink -cv %{buildroot}%{_datadir}/selinux
%endif


%define saveFileContext() \
if [ -s /etc/selinux/config ]; then \
	. %{_sysconfdir}/selinux/config; \
	FILE_CONTEXT=%{_sysconfdir}/selinux/%1/contexts/files/file_contexts; \
	if [ "${SELINUXTYPE}" == %1 -a -f ${FILE_CONTEXT} ]; then \
		cp -f ${FILE_CONTEXT} ${FILE_CONTEXT}.%{name}; \
	fi \
fi;

%define relabel() \
. %{_sysconfdir}/selinux/config; \
FILE_CONTEXT=%{_sysconfdir}/selinux/%1/contexts/files/file_contexts; \
selinuxenabled; \
if [ $? == 0  -a "${SELINUXTYPE}" == %1 -a -f ${FILE_CONTEXT}.%{name} ]; then \
	fixfiles -C ${FILE_CONTEXT}.%{name} restore; \
	rm -f ${FILE_CONTEXT}.%name; \
fi;

install -m0644 -D icecream.sysusers.conf %{buildroot}%{_sysusersdir}/icecream.conf

%pre
%if %{with selinux}
for selinuxvariant in %{selinux_variants}; do
	%saveFileContext ${selinuxvariant}
done
%endif
%post
/sbin/ldconfig
%if %{with selinux}
for selinuxvariant in %{selinux_variants}; do
	semodule -s ${selinuxvariant} -i \
		%{_datadir}/selinux/${selinuxvariant}/icecream.pp 2>/dev/null
done

for selinuxvariant in %{selinux_variants}; do
	semanage port -a -S ${selinuxvariant} -t iceccd_port_t -p tcp 10245
	semanage port -a -S ${selinuxvariant} -t icecc_scheduler_port_t -p tcp 8766
	semanage port -a -S ${selinuxvariant} -t icecc_scheduler_port_t -p udp 8765
	# tcp 8765 is taken by LIRC. icecream.te knows it.
	# semanage port -a -S ${selinuxvariant} -t icecc_scheduler_port_t -p tcp 8765
done 2>/dev/null

for selinuxvariant in %{selinux_variants}; do
	%relabel ${selinuxvariant}
done

restorecon -R %{_localstatedir}/cache/icecream /run/icecc 2>/dev/null
%endif

%firewalld_reload
%systemd_post iceccd.service icecc-scheduler.service

# Remove files owned by the user 'icecream' (used by older versions).
find %{_localstatedir}/cache/icecream/ -user icecream -delete 2>/dev/null
exit 0

%preun
%systemd_preun iceccd.service icecc-scheduler.service
%if %{with selinux}
if [ $1 -eq 0 ]; then # Final removal
	for selinuxvariant in %{selinux_variants}; do
		%saveFileContext ${selinuxvariant}
	done
	for selinuxvariant in %{selinux_variants}; do
		semanage port -d -S ${selinuxvariant} -t iceccd_port_t -p tcp 10245
		semanage port -d -S ${selinuxvariant} -t icecc_scheduler_port_t -p tcp 8766
		semanage port -d -S ${selinuxvariant} -t icecc_scheduler_port_t -p udp 8765
	done 2>/dev/null
fi
%endif
exit 0

%postun
/sbin/ldconfig
%systemd_postun_with_restart iceccd.service icecc-scheduler.service
%if %{with selinux}
if [ $1 -eq 0 ]; then # Final removal
	for selinuxvariant in %{selinux_variants}; do
		semodule -s ${selinuxvariant} -r icecream 2>/dev/null
		%relabel ${selinuxvariant}
	done
fi
%endif
exit 0

%files
%license COPYING
%doc README NEWS TODO
%{_bindir}/icecc
%{_bindir}/icecc-create-env
%{_bindir}/icecc-test-env
%{_bindir}/icerun
%{_libexecdir}/icecc/
%{_libdir}/libicecc.so.*
%{_sbindir}/iceccd
%{_sbindir}/icecc-scheduler
%{_modulesdir}/icecream/
%config(noreplace) %{_sysconfdir}/sysconfig/icecream
%{_unitdir}/icecc*.service
%attr(0775, root, icecc) %{_localstatedir}/cache/icecream
%attr(0775, root, icecc) /run/icecc
%{_mandir}/man*/*
%{_tmpfilesdir}/icecream.conf
%{?with_selinux:%{_datadir}/selinux/*/icecream.pp}
%{_prefix}/lib/firewalld/services/icecream.xml
%{_prefix}/lib/firewalld/services/icecream-scheduler.xml
%{_sysusersdir}/icecream.conf

%files devel
%dir %{_includedir}/icecc/
%{_includedir}/icecc/*.h
%{_libdir}/libicecc.so
%{_libdir}/pkgconfig/icecc.pc

%changelog
%autochangelog
