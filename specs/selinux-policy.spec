# Conditionals for policy types (all built by default)
%bcond targeted 1
%bcond minimum  1
%bcond mls      1

# github repo with selinux-policy sources
%global giturl https://github.com/fedora-selinux/selinux-policy
%global commit 86239660160a15a019ae3ae91f0e51c820f9fcaa
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%define distro redhat
%define polyinstatiate n
%define monolithic n

%define POLICYVER 34
%define POLICYCOREUTILSVER 3.8
%define CHECKPOLICYVER 3.8
Summary: SELinux policy configuration
Name: selinux-policy
Version: 41.30
Release: 1%{?dist}
License: GPL-2.0-or-later
Source: %{giturl}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Source1: Makefile.devel
Source2: selinux-policy.conf

# Tool helps during policy development, to expand system m4 macros to raw allow rules
# Git repo: https://github.com/fedora-selinux/macro-expander.git
Source3: macro-expander

# Include SELinux policy for container from separate container-selinux repo
# Git repo: https://github.com/containers/container-selinux.git
Source4: container-selinux.tgz

# modules enabled in -minimum policy
Source16: modules-minimum.lst

Source36: selinux-check-proper-disable.service

# Script to convert /var/run file context entries to /run
Source37: varrun-convert.sh
# Configuration files to dnf-protect targeted and/or mls subpackages
Source38: selinux-policy-targeted.conf
Source39: selinux-policy-mls.conf
# Script to convert /usr/sbin file context entries to /usr/bin
Source40: binsbin-convert.sh

# Provide rpm macros for packages installing SELinux modules
Source5: rpm.macros

Url: %{giturl}
BuildArch: noarch
BuildRequires: python3 gawk checkpolicy >= %{CHECKPOLICYVER} m4 policycoreutils-devel >= %{POLICYCOREUTILSVER} bzip2
BuildRequires: make
BuildRequires: systemd-rpm-macros
BuildRequires: groff
Requires(pre): policycoreutils >= %{POLICYCOREUTILSVER}
Requires(post): /bin/awk /usr/bin/sha512sum
Requires(meta): (rpm-plugin-selinux if rpm-libs)
Requires: selinux-policy-any = %{version}-%{release}
Provides: selinux-policy-base = %{version}-%{release}
Suggests: selinux-policy-targeted

%description
SELinux core policy package.
Originally based off of reference policy,
the policy has been adjusted to provide support for Fedora.

%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%dir %{_datadir}/selinux
%dir %{_datadir}/selinux/packages
%dir %{_sysconfdir}/selinux
%ghost %config(noreplace) %{_sysconfdir}/selinux/config
%ghost %{_sysconfdir}/sysconfig/selinux
%{_usr}/lib/tmpfiles.d/selinux-policy.conf
%{_rpmconfigdir}/macros.d/macros.selinux-policy
%{_unitdir}/selinux-check-proper-disable.service
%{_libexecdir}/selinux/binsbin-convert.sh
%{_libexecdir}/selinux/varrun-convert.sh

%package sandbox
Summary: SELinux sandbox policy
Requires(pre): selinux-policy-base = %{version}-%{release}
Requires(pre): selinux-policy-targeted = %{version}-%{release}

%description sandbox
SELinux sandbox policy for use with the sandbox utility.

%files sandbox
%verify(not md5 size mtime) %{_datadir}/selinux/packages/sandbox.pp

%post sandbox
rm -f %{_sysconfdir}/selinux/*/modules/active/modules/sandbox.pp.disabled 2>/dev/null
rm -f %{_sharedstatedir}/selinux/*/active/modules/disabled/sandbox 2>/dev/null
%{_sbindir}/semodule -n -X 100 -i %{_datadir}/selinux/packages/sandbox.pp 2> /dev/null
if %{_sbindir}/selinuxenabled ; then
    %{_sbindir}/load_policy
fi;
exit 0

%preun sandbox
if [ $1 -eq 0 ] ; then
    %{_sbindir}/semodule -n -d sandbox 2>/dev/null
    if %{_sbindir}/selinuxenabled ; then
        %{_sbindir}/load_policy
    fi;
fi;
exit 0

%package devel
Summary: SELinux policy development files
Requires(pre): selinux-policy = %{version}-%{release}
Requires: selinux-policy = %{version}-%{release}
Requires: m4 checkpolicy >= %{CHECKPOLICYVER}
Requires: /usr/bin/make
Requires(post): policycoreutils-devel >= %{POLICYCOREUTILSVER}

%description devel
SELinux policy development package.
This package contains:
- interfaces, macros, and patterns for policy development
- a policy example
- the macro-expander utility
and some additional files.

%files devel
%{_bindir}/macro-expander
%dir %{_datadir}/selinux/devel
%dir %{_datadir}/selinux/devel/include
%{_datadir}/selinux/devel/include/*
%exclude %{_datadir}/selinux/devel/include/contrib/container.if
%dir %{_datadir}/selinux/devel/html
%{_datadir}/selinux/devel/html/*html
%{_datadir}/selinux/devel/html/*css
%{_datadir}/selinux/devel/Makefile
%{_datadir}/selinux/devel/example.*
%{_datadir}/selinux/devel/policy.*
%ghost %verify(not md5 size mode mtime) %{_sharedstatedir}/sepolgen/interface_info

%post devel
%{_sbindir}/selinuxenabled && %{_bindir}/sepolgen-ifgen 2>/dev/null
exit 0

%package doc
Summary: SELinux policy documentation
Requires(pre): selinux-policy = %{version}-%{release}
Requires: selinux-policy = %{version}-%{release}

%description doc
SELinux policy documentation package.
This package contains manual pages and documentation of the policy modules.

%files doc
%{_mandir}/man*/*
%exclude %{_mandir}/man8/container_selinux.8.gz
%doc %{_datadir}/doc/%{name}

%define common_params DISTRO=%{distro} UBAC=n DIRECT_INITRC=n MONOLITHIC=%{monolithic} MLS_CATS=1024 MCS_CATS=1024

%define makeCmds() \
%make_build %common_params UNK_PERMS=%3 NAME=%1 TYPE=%2 bare \
%make_build %common_params UNK_PERMS=%3 NAME=%1 TYPE=%2 conf \
install -p -m0644 ./dist/%1/booleans.conf ./policy/booleans.conf \
install -p -m0644 ./dist/%1/users ./policy/users \

%define makeModulesConf() \
install -p -m0644 ./dist/%1/modules.conf ./policy/modules.conf \

%define installCmds() \
%make_build %common_params UNK_PERMS=%3 NAME=%1 TYPE=%2 base.pp \
%make_build %common_params UNK_PERMS=%3 NAME=%1 TYPE=%2 validate modules \
make %common_params UNK_PERMS=%3 NAME=%1 TYPE=%2 DESTDIR=%{buildroot} install \
make %common_params UNK_PERMS=%3 NAME=%1 TYPE=%2 DESTDIR=%{buildroot} install-appconfig \
make %common_params UNK_PERMS=%3 NAME=%1 TYPE=%2 DESTDIR=%{buildroot} SEMODULE="%{_sbindir}/semodule -p %{buildroot} -X 100 " load \
%{__mkdir} -p %{buildroot}%{_sysconfdir}/selinux/%1/logins \
touch %{buildroot}%{_sysconfdir}/selinux/%1/contexts/files/file_contexts.subs \
install -p -m0644 ./config/file_contexts.subs_dist %{buildroot}%{_sysconfdir}/selinux/%1/contexts/files \
install -p -m0644 ./dist/%1/setrans.conf %{buildroot}%{_sysconfdir}/selinux/%1/setrans.conf \
install -p -m0644 ./dist/customizable_types %{buildroot}%{_sysconfdir}/selinux/%1/contexts/customizable_types \
touch %{buildroot}%{_sysconfdir}/selinux/%1/contexts/files/file_contexts.bin \
touch %{buildroot}%{_sysconfdir}/selinux/%1/contexts/files/file_contexts.local \
touch %{buildroot}%{_sysconfdir}/selinux/%1/contexts/files/file_contexts.local.bin \
install -p -m0644 ./dist/booleans.subs_dist %{buildroot}%{_sysconfdir}/selinux/%1 \
rm -f %{buildroot}%{_datadir}/selinux/%1/*pp*  \
%{_bindir}/sha512sum %{buildroot}%{_sysconfdir}/selinux/%1/policy/policy.%{POLICYVER} | cut -d' ' -f 1 > %{buildroot}%{_sysconfdir}/selinux/%1/.policy.sha512; \
rm -rf %{buildroot}%{_sysconfdir}/selinux/%1/contexts/netfilter_contexts  \
rm -rf %{buildroot}%{_sysconfdir}/selinux/%1/modules/active/policy.kern \
rm -f %{buildroot}%{_sharedstatedir}/selinux/%1/active/*.linked \
%nil

%define fileList() \
%defattr(-,root,root) \
%dir %{_sysconfdir}/selinux/%1 \
%config(noreplace) %{_sysconfdir}/selinux/%1/setrans.conf \
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/selinux/%1/seusers \
%dir %{_sysconfdir}/selinux/%1/logins \
%dir %{_sharedstatedir}/selinux/%1/active \
%verify(not md5 size mtime) %{_sharedstatedir}/selinux/%1/semanage.read.LOCK \
%verify(not md5 size mtime) %{_sharedstatedir}/selinux/%1/semanage.trans.LOCK \
%dir %attr(700,root,root) %dir %{_sharedstatedir}/selinux/%1/active/modules \
%verify(not md5 size mtime) %{_sharedstatedir}/selinux/%1/active/modules/100/base \
%dir %{_sysconfdir}/selinux/%1/policy/ \
%verify(not md5 size mtime) %{_sysconfdir}/selinux/%1/policy/policy.%{POLICYVER} \
%{_sysconfdir}/selinux/%1/.policy.sha512 \
%dir %{_sysconfdir}/selinux/%1/contexts \
%config %{_sysconfdir}/selinux/%1/contexts/customizable_types \
%config(noreplace) %{_sysconfdir}/selinux/%1/contexts/securetty_types \
%config(noreplace) %{_sysconfdir}/selinux/%1/contexts/dbus_contexts \
%config %{_sysconfdir}/selinux/%1/contexts/x_contexts \
%config %{_sysconfdir}/selinux/%1/contexts/default_contexts \
%config %{_sysconfdir}/selinux/%1/contexts/virtual_domain_context \
%config %{_sysconfdir}/selinux/%1/contexts/virtual_image_context \
%config %{_sysconfdir}/selinux/%1/contexts/lxc_contexts \
%config %{_sysconfdir}/selinux/%1/contexts/systemd_contexts \
%config %{_sysconfdir}/selinux/%1/contexts/sepgsql_contexts \
%config %{_sysconfdir}/selinux/%1/contexts/openssh_contexts \
%config %{_sysconfdir}/selinux/%1/contexts/snapperd_contexts \
%config(noreplace) %{_sysconfdir}/selinux/%1/contexts/default_type \
%config(noreplace) %{_sysconfdir}/selinux/%1/contexts/failsafe_context \
%config(noreplace) %{_sysconfdir}/selinux/%1/contexts/initrc_context \
%config(noreplace) %{_sysconfdir}/selinux/%1/contexts/removable_context \
%config(noreplace) %{_sysconfdir}/selinux/%1/contexts/userhelper_context \
%dir %{_sysconfdir}/selinux/%1/contexts/files \
%verify(not md5 size mtime) %{_sysconfdir}/selinux/%1/contexts/files/file_contexts \
%ghost %{_sysconfdir}/selinux/%1/contexts/files/file_contexts.bin \
%verify(not md5 size mtime) %{_sysconfdir}/selinux/%1/contexts/files/file_contexts.homedirs \
%ghost %{_sysconfdir}/selinux/%1/contexts/files/file_contexts.homedirs.bin \
%config(noreplace) %{_sysconfdir}/selinux/%1/contexts/files/file_contexts.local \
%ghost %{_sysconfdir}/selinux/%1/contexts/files/file_contexts.local.bin \
%config(noreplace) %{_sysconfdir}/selinux/%1/contexts/files/file_contexts.subs \
%{_sysconfdir}/selinux/%1/contexts/files/file_contexts.subs_dist \
%{_sysconfdir}/selinux/%1/booleans.subs_dist \
%config %{_sysconfdir}/selinux/%1/contexts/files/media \
%dir %{_sysconfdir}/selinux/%1/contexts/users \
%config(noreplace) %{_sysconfdir}/selinux/%1/contexts/users/root \
%config(noreplace) %{_sysconfdir}/selinux/%1/contexts/users/guest_u \
%config(noreplace) %{_sysconfdir}/selinux/%1/contexts/users/xguest_u \
%config(noreplace) %{_sysconfdir}/selinux/%1/contexts/users/user_u \
%config(noreplace) %{_sysconfdir}/selinux/%1/contexts/users/staff_u \
%dir %{_datadir}/selinux/%1 \
%{_datadir}/selinux/%1/base.lst \
%{_datadir}/selinux/%1/modules.lst \
%{_datadir}/selinux/%1/nonbasemodules.lst \
%dir %{_sharedstatedir}/selinux/%1 \
%verify(not md5 size mtime) %{_sharedstatedir}/selinux/%1/active/commit_num \
%verify(not md5 size mtime) %{_sharedstatedir}/selinux/%1/active/users_extra \
%verify(not md5 size mtime) %{_sharedstatedir}/selinux/%1/active/homedir_template \
%verify(not md5 size mtime) %{_sharedstatedir}/selinux/%1/active/seusers \
%verify(not md5 size mtime) %{_sharedstatedir}/selinux/%1/active/file_contexts \
%verify(not md5 size mtime) %{_sharedstatedir}/selinux/%1/active/policy.kern \
%ghost %{_sharedstatedir}/selinux/%1/active/policy.linked \
%ghost %{_sharedstatedir}/selinux/%1/active/seusers.linked \
%ghost %{_sharedstatedir}/selinux/%1/active/users_extra.linked \
%verify(not md5 size mtime) %{_sharedstatedir}/selinux/%1/active/file_contexts.homedirs \
%verify(not md5 size mtime) %{_sharedstatedir}/selinux/%1/active/modules_checksum \
%ghost %verify(not mode md5 size mtime) %{_sharedstatedir}/selinux/%1/active/modules/400/extra_binsbin \
%ghost %verify(not mode md5 size mtime) %{_sharedstatedir}/selinux/%1/active/modules/400/extra_binsbin/cil \
%ghost %verify(not mode md5 size mtime) %{_sharedstatedir}/selinux/%1/active/modules/400/extra_binsbin/lang_ext \
%ghost %verify(not mode md5 size mtime) %{_sharedstatedir}/selinux/%1/active/modules/400/extra_varrun \
%ghost %verify(not mode md5 size mtime) %{_sharedstatedir}/selinux/%1/active/modules/400/extra_varrun/cil \
%ghost %verify(not mode md5 size mtime) %{_sharedstatedir}/selinux/%1/active/modules/400/extra_varrun/lang_ext \
%nil

%define relabel() \
if [ -s %{_sysconfdir}/selinux/config ]; then \
    . %{_sysconfdir}/selinux/config &> /dev/null || true; \
fi; \
FILE_CONTEXT=%{_sysconfdir}/selinux/%1/contexts/files/file_contexts; \
if %{_sbindir}/selinuxenabled && [ "${SELINUXTYPE}" = %1 -a -f ${FILE_CONTEXT}.pre ]; then \
     %{_sbindir}/fixfiles -C ${FILE_CONTEXT}.pre restore &> /dev/null > /dev/null; \
     rm -f ${FILE_CONTEXT}.pre; \
fi; \
# rebuilding the rpm database still can sometimes result in an incorrect context \
%{_sbindir}/restorecon -R /usr/lib/sysimage/rpm \
# In some scenarios, /usr/bin/httpd is labelled incorrectly after sbin merge. \
# Relabel all files under /usr/bin, in case they got installed before policy \
# was updated and the labels were incorrect. \
%{_sbindir}/restorecon -R /usr/bin /usr/sbin \
if %{_sbindir}/restorecon -e /run/media -R /root /var/log /var/run /etc/passwd* /etc/group* /etc/*shadow* 2> /dev/null;then \
    continue; \
fi;

%define preInstall() \
if [ $1 -ne 1 ] && [ -s %{_sysconfdir}/selinux/config ]; then \
     for MOD_NAME in ganesha ipa_custodia kdbus; do \
        if [ -d %{_sharedstatedir}/selinux/%1/active/modules/100/$MOD_NAME ]; then \
           %{_sbindir}/semodule -n -d $MOD_NAME 2> /dev/null; \
        fi; \
     done; \
     . %{_sysconfdir}/selinux/config; \
     FILE_CONTEXT=%{_sysconfdir}/selinux/%1/contexts/files/file_contexts; \
     if [ "${SELINUXTYPE}" = %1 -a -f ${FILE_CONTEXT} ]; then \
        [ -f ${FILE_CONTEXT}.pre ] || cp -f ${FILE_CONTEXT} ${FILE_CONTEXT}.pre; \
     fi; \
     touch %{_sysconfdir}/selinux/%1/.rebuild; \
     if [ -e %{_sysconfdir}/selinux/%1/.policy.sha512 ]; then \
        POLICY_FILE=`ls %{_sysconfdir}/selinux/%1/policy/policy.* | sort | head -1` \
        sha512=`sha512sum $POLICY_FILE | cut -d ' ' -f 1`; \
	checksha512=`cat %{_sysconfdir}/selinux/%1/.policy.sha512`; \
	if [ "$sha512" == "$checksha512" ] ; then \
		rm %{_sysconfdir}/selinux/%1/.rebuild; \
	fi; \
   fi; \
fi;

%define postInstall() \
if [ -s %{_sysconfdir}/selinux/config ]; then \
    . %{_sysconfdir}/selinux/config &> /dev/null || true; \
fi; \
if [ -e %{_sysconfdir}/selinux/%2/.rebuild ]; then \
   rm %{_sysconfdir}/selinux/%2/.rebuild; \
fi; \
%{_sbindir}/semodule -B -n -s %2 2> /dev/null; \
[ "${SELINUXTYPE}" == "%2" ] && %{_sbindir}/selinuxenabled && load_policy; \
if [ %1 -eq 1 ]; then \
   %{_sbindir}/restorecon -R /root /var/log /run /etc/passwd* /etc/group* /etc/*shadow* 2> /dev/null; \
else \
%relabel %2 \
fi;

%define modulesList() \
awk '$1 !~ "/^#/" && $2 == "=" && $3 == "module" { printf "%%s ", $1 }' ./policy/modules.conf > %{buildroot}%{_datadir}/selinux/%1/modules.lst \
awk '$1 !~ "/^#/" && $2 == "=" && $3 == "base" { printf "%%s ", $1 }' ./policy/modules.conf > %{buildroot}%{_datadir}/selinux/%1/base.lst \

%define nonBaseModulesList() \
modules=`cat %{buildroot}%{_datadir}/selinux/%1/modules.lst` \
for i in $modules; do \
    if [ $i != "sandbox" ];then \
        echo "%verify(not md5 size mtime) %{_sharedstatedir}/selinux/%1/active/modules/100/$i" >> %{buildroot}%{_datadir}/selinux/%1/nonbasemodules.lst \
    fi; \
done;

# Make sure the config is consistent with what packages are installed in the system
# this covers cases when system is installed with selinux-policy-{mls,minimal}
# or selinux-policy-{targeted,mls,minimal} where switched but the machine has not
# been rebooted yet.
# The macro should be called at the beginning of "post" (to make sure load_policy does not fail)
# and in "posttrans" (to make sure that the store is consistent when all package transitions are done)
# Parameter determines the policy type to be set in case of miss-configuration (if backup value is not usable)
# Steps:
# * load values from config and its backup
# * check whether SELINUXTYPE from backup is usable and make sure that it's set in the config if so
# * use "targeted" if it's being installed and BACKUP_SELINUXTYPE cannot be used
# * check whether SELINUXTYPE in the config is usable and change it to newly installed policy if it isn't
%define checkConfigConsistency() \
if [ -f %{_sysconfdir}/selinux/.config_backup ]; then \
    . %{_sysconfdir}/selinux/.config_backup; \
else \
    BACKUP_SELINUXTYPE=targeted; \
fi; \
if [ -s %{_sysconfdir}/selinux/config ]; then \
    . %{_sysconfdir}/selinux/config; \
    if ls %{_sysconfdir}/selinux/$BACKUP_SELINUXTYPE/policy/policy.* &>/dev/null; then \
        if [ "$BACKUP_SELINUXTYPE" != "$SELINUXTYPE" ]; then \
            sed -i 's/^SELINUXTYPE=.*/SELINUXTYPE='"$BACKUP_SELINUXTYPE"'/g' %{_sysconfdir}/selinux/config; \
        fi; \
    elif [ "%1" = "targeted" ]; then \
        if [ "%1" != "$SELINUXTYPE" ]; then \
            sed -i 's/^SELINUXTYPE=.*/SELINUXTYPE=%1/g' %{_sysconfdir}/selinux/config; \
        fi; \
    elif ! ls  %{_sysconfdir}/selinux/$SELINUXTYPE/policy/policy.* &>/dev/null; then \
        if [ "%1" != "$SELINUXTYPE" ]; then \
            sed -i 's/^SELINUXTYPE=.*/SELINUXTYPE=%1/g' %{_sysconfdir}/selinux/config; \
        fi; \
    fi; \
fi;

# Create hidden backup of /etc/selinux/config and prepend BACKUP_ to names
# of variables inside so that they are easy to use later
# This should be done in "pretrans" because config content can change during RPM operations
# The macro has to be used in a script slot with "-p <lua>"
%define backupConfigLua() \
local sysconfdir = rpm.expand("%{_sysconfdir}") \
local config_file = sysconfdir .. "/selinux/config" \
local config_backup = sysconfdir .. "/selinux/.config_backup" \
os.remove(config_backup) \
if posix.stat(config_file) then \
    local f = assert(io.open(config_file, "r"), "Failed to read " .. config_file) \
    local content = f:read("*all") \
    f:close() \
    local backup = content:gsub("SELINUX", "BACKUP_SELINUX") \
    local bf = assert(io.open(config_backup, "w"), "Failed to open " .. config_backup) \
    bf:write(backup) \
    bf:close() \
end

# Remove the local_varrun SELinux module
%define removeVarrunModuleLua() \
if posix.access ("%{_sharedstatedir}/selinux/%1/active/modules/400/extra_varrun/cil", "r") then \
  os.execute ("%{_bindir}/rm -rf %{_sharedstatedir}/selinux/%1/active/modules/400/extra_varrun") \
end

# Remove the local_binsbin SELinux module
%define removeBinsbinModuleLua() \
if posix.access ("%{_sharedstatedir}/selinux/%1/active/modules/400/extra_binsbin/cil", "r") then \
  os.execute ("%{_bindir}/rm -rf %{_sharedstatedir}/selinux/%1/active/modules/400/extra_binsbin") \
end

%build

%prep
%autosetup -p 1 -n %{name}-%{commit}
tar -C policy/modules/contrib -xf %{SOURCE4}

%install
# Build targeted policy
%{__rm} -fR %{buildroot}
mkdir -p %{buildroot}%{_sysconfdir}/selinux
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
touch %{buildroot}%{_sysconfdir}/selinux/config
touch %{buildroot}%{_sysconfdir}/sysconfig/selinux
mkdir -p %{buildroot}%{_usr}/lib/tmpfiles.d/
install -p -m0644 %{SOURCE2} %{buildroot}%{_usr}/lib/tmpfiles.d/
mkdir -p %{buildroot}%{_bindir}
install -p -m 755 %{SOURCE3} %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_libexecdir}/selinux
install -p -m 755  %{SOURCE37} %{buildroot}%{_libexecdir}/selinux
install -p -m 755  %{SOURCE40} %{buildroot}%{_libexecdir}/selinux

# Always create policy module package directories
mkdir -p %{buildroot}%{_datadir}/selinux/{targeted,mls,minimum,modules}/
mkdir -p %{buildroot}%{_sharedstatedir}/selinux/{targeted,mls,minimum,modules}/

mkdir -p %{buildroot}%{_datadir}/selinux/packages

mkdir -p %{buildroot}%{_sysconfdir}/dnf/protected.d/

# Install devel
make clean
%if %{with targeted}
# Build targeted policy
%makeCmds targeted mcs allow
%makeModulesConf targeted
%installCmds targeted mcs allow
# install permissivedomains.cil
%{_sbindir}/semodule -p %{buildroot} -X 100 -s targeted -i \
    ./dist/permissivedomains.cil
# recreate sandbox.pp
rm -rf %{buildroot}%{_sharedstatedir}/selinux/targeted/active/modules/100/sandbox
%make_build %common_params UNK_PERMS=allow NAME=targeted TYPE=mcs sandbox.pp
mv sandbox.pp %{buildroot}%{_datadir}/selinux/packages/sandbox.pp
%modulesList targeted
%nonBaseModulesList targeted
install -p -m 644 %{SOURCE38} %{buildroot}%{_sysconfdir}/dnf/protected.d/
%endif

%if %{with minimum}
# Build minimum policy
%makeCmds minimum mcs allow
%makeModulesConf targeted
%installCmds minimum mcs allow
rm -rf %{buildroot}%{_sharedstatedir}/selinux/minimum/active/modules/100/sandbox
install -p -m 644 %{SOURCE16} %{buildroot}%{_datadir}/selinux/minimum/modules-enabled.lst
%modulesList minimum
%nonBaseModulesList minimum
%endif

%if %{with mls}
# Build mls policy
%makeCmds mls mls deny
%makeModulesConf mls
%installCmds mls mls deny
%modulesList mls
%nonBaseModulesList mls
install -p -m 644 %{SOURCE39} %{buildroot}%{_sysconfdir}/dnf/protected.d/
%endif

# remove leftovers when save-previous=true (semanage.conf) is used
rm -rf %{buildroot}%{_sharedstatedir}/selinux/{minimum,targeted,mls}/previous

make %common_params UNK_PERMS=allow NAME=targeted TYPE=mcs DESTDIR=%{buildroot} PKGNAME=%{name} install-docs
make %common_params UNK_PERMS=allow NAME=targeted TYPE=mcs DESTDIR=%{buildroot} PKGNAME=%{name} install-headers
mkdir %{buildroot}%{_datadir}/selinux/devel/
mv %{buildroot}%{_datadir}/selinux/targeted/include %{buildroot}%{_datadir}/selinux/devel/include
install -p -m 644 %{SOURCE1} %{buildroot}%{_datadir}/selinux/devel/Makefile
install -p -m 644 doc/example.* %{buildroot}%{_datadir}/selinux/devel/
install -p -m 644 doc/policy.* %{buildroot}%{_datadir}/selinux/devel/
%{_bindir}/sepolicy manpage -a -p %{buildroot}%{_mandir}/man8/ -w -r %{buildroot}
mkdir %{buildroot}%{_datadir}/selinux/devel/html
mv %{buildroot}%{_datadir}/man/man8/*.html %{buildroot}%{_datadir}/selinux/devel/html
mv %{buildroot}%{_datadir}/man/man8/style.css %{buildroot}%{_datadir}/selinux/devel/html

mkdir -p %{buildroot}%{_rpmconfigdir}/macros.d
install -p -m 644 %{SOURCE5} %{buildroot}%{_rpmconfigdir}/macros.d/macros.selinux-policy
sed -i 's/SELINUXPOLICYVERSION/%{version}/' %{buildroot}%{_rpmconfigdir}/macros.d/macros.selinux-policy
sed -i 's@SELINUXSTOREPATH@%{_sharedstatedir}/selinux@' %{buildroot}%{_rpmconfigdir}/macros.d/macros.selinux-policy

mkdir -p %{buildroot}%{_unitdir}
install -p -m 644 %{SOURCE36} %{buildroot}%{_unitdir}

%post
%systemd_post selinux-check-proper-disable.service
if [ ! -s %{_sysconfdir}/selinux/config ]; then
#
#     New install so we will default to targeted policy
#
echo "
# This file controls the state of SELinux on the system.
# SELINUX= can take one of these three values:
#     enforcing - SELinux security policy is enforced.
#     permissive - SELinux prints warnings instead of enforcing.
#     disabled - No SELinux policy is loaded.
# See also:
# https://docs.fedoraproject.org/en-US/quick-docs/getting-started-with-selinux/#getting-started-with-selinux-selinux-states-and-modes
#
# NOTE: In earlier Fedora kernel builds, SELINUX=disabled would also
# fully disable SELinux during boot. If you need a system with SELinux
# fully disabled instead of SELinux running with no policy loaded, you
# need to pass selinux=0 to the kernel command line. You can use grubby
# to persistently set the bootloader to boot with selinux=0:
#
#    grubby --update-kernel ALL --args selinux=0
#
# To revert back to SELinux enabled:
#
#    grubby --update-kernel ALL --remove-args selinux
#
SELINUX=enforcing
# SELINUXTYPE= can take one of these three values:
#     targeted - Targeted processes are protected,
#     minimum - Modification of targeted policy. Only selected processes are protected.
#     mls - Multi Level Security protection.
SELINUXTYPE=targeted

" > %{_sysconfdir}/selinux/config

     ln -sf ../selinux/config %{_sysconfdir}/sysconfig/selinux
     %{_sbindir}/restorecon %{_sysconfdir}/selinux/config 2> /dev/null || :
else
     . %{_sysconfdir}/selinux/config
fi
exit 0

%preun
%systemd_preun selinux-check-proper-disable.service

%postun
%systemd_postun selinux-check-proper-disable.service
if [ $1 = 0 ]; then
     %{_sbindir}/setenforce 0 2> /dev/null
     if [ ! -s %{_sysconfdir}/selinux/config ]; then
          echo "SELINUX=disabled" > %{_sysconfdir}/selinux/config
     else
          sed -i 's/^SELINUX=.*/SELINUX=disabled/g' %{_sysconfdir}/selinux/config
     fi
fi
exit 0

%if %{with targeted}
%package targeted
Summary: SELinux targeted policy
Provides: selinux-policy-any = %{version}-%{release}
Obsoletes: selinux-policy-targeted-sources < 2
Requires(pre): policycoreutils >= %{POLICYCOREUTILSVER}
Requires(pre): coreutils
Requires(pre): selinux-policy = %{version}-%{release}
Requires: selinux-policy = %{version}-%{release}
Conflicts:  audispd-plugins <= 1.7.7-1
Obsoletes: mod_fcgid-selinux <= %{version}-%{release}
Obsoletes: cachefilesd-selinux <= 0.10-1
Conflicts:  seedit
Conflicts:  389-ds-base < 1.2.7, 389-admin < 1.1.12
Conflicts: container-selinux < 2:1.12.1-22

%description targeted
SELinux targeted policy package.

%pretrans targeted -p <lua>
%backupConfigLua
%removeVarrunModuleLua targeted
%removeBinsbinModuleLua targeted

%pre targeted
%preInstall targeted

%post targeted
%checkConfigConsistency targeted
exit 0

%posttrans targeted
%checkConfigConsistency targeted
%{_libexecdir}/selinux/varrun-convert.sh targeted
%{_libexecdir}/selinux/binsbin-convert.sh targeted
%postInstall $1 targeted
%{_sbindir}/restorecon -Ri /usr/lib/sysimage/rpm /var/lib/rpm /etc/mdevctl.d
%{_sbindir}/restorecon -i /usr/sbin/fapolicyd* /usr/sbin/usbguard*

%postun targeted
if [ $1 = 0 ]; then
    if [ -s %{_sysconfdir}/selinux/config ]; then
        source %{_sysconfdir}/selinux/config &> /dev/null || true
    fi
    if [ "$SELINUXTYPE" = "targeted" ]; then
        %{_sbindir}/setenforce 0 2> /dev/null
        if [ ! -s %{_sysconfdir}/selinux/config ]; then
            echo "SELINUX=disabled" > %{_sysconfdir}/selinux/config
        else
            sed -i 's/^SELINUX=.*/SELINUX=disabled/g' %{_sysconfdir}/selinux/config
        fi
    fi
fi
exit 0


%triggerin -- pcre2
%{_sbindir}/selinuxenabled && %{_sbindir}/semodule -nB 2> /dev/null
exit 0

%triggerin -- fapolicyd-selinux
%{_libexecdir}/selinux/binsbin-convert.sh targeted
%{_sbindir}/restorecon /usr/sbin/fapolicyd*

%triggerin -- usbguard-selinux
%{_libexecdir}/selinux/binsbin-convert.sh targeted
%{_sbindir}/restorecon /usr/sbin/usbguard*

%triggerprein -p <lua> -- container-selinux
%removeVarrunModuleLua targeted

%triggerprein -p <lua> -- pcp-selinux
%removeVarrunModuleLua targeted

%triggerprein -p <lua> -- fapolicyd-selinux
%removeBinsbinModuleLua targeted

%triggerprein -p <lua> -- usbguard-selinux
%removeBinsbinModuleLua targeted

%triggerpostun -- pcp-selinux
%{_libexecdir}/selinux/varrun-convert.sh targeted
exit 0

%triggerpostun -- container-selinux
%{_libexecdir}/selinux/varrun-convert.sh targeted
exit 0

%triggerpostun -- fapolicyd-selinux
%{_libexecdir}/selinux/binsbin-convert.sh targeted
exit 0

%triggerpostun -- usbguard-selinux
%{_libexecdir}/selinux/binsbin-convert.sh targeted
exit 0

%files targeted -f %{buildroot}%{_datadir}/selinux/targeted/nonbasemodules.lst
%config(noreplace) %{_sysconfdir}/dnf/protected.d/selinux-policy-targeted.conf
%config(noreplace) %{_sysconfdir}/selinux/targeted/contexts/users/unconfined_u
%config(noreplace) %{_sysconfdir}/selinux/targeted/contexts/users/sysadm_u
%fileList targeted
%verify(not md5 size mtime) %{_sharedstatedir}/selinux/targeted/active/modules/100/permissivedomains
%endif

%if %{with minimum}
%package minimum
Summary: SELinux minimum policy
Provides: selinux-policy-any = %{version}-%{release}
Requires(post): policycoreutils-python-utils >= %{POLICYCOREUTILSVER}
Requires(pre): coreutils
Requires(pre): selinux-policy = %{version}-%{release}
Requires: selinux-policy = %{version}-%{release}
Conflicts:  seedit
Conflicts: container-selinux <= 1.9.0-9

%description minimum
SELinux minimum policy package.

%pretrans minimum -p <lua>
%backupConfigLua

%pre minimum
%preInstall minimum
if [ $1 -ne 1 ]; then
    %{_sbindir}/semodule -s minimum --list-modules=full | awk '{ if ($4 != "disabled") print $2; }' > %{_datadir}/selinux/minimum/instmodules.lst
fi

%post minimum
%checkConfigConsistency minimum
modules=`cat %{_datadir}/selinux/minimum/modules.lst`
basemodules=`cat %{_datadir}/selinux/minimum/base.lst`
enabledmodules=`cat %{_datadir}/selinux/minimum/modules-enabled.lst`
if [ ! -d %{_sharedstatedir}/selinux/minimum/active/modules/disabled ]; then
    mkdir %{_sharedstatedir}/selinux/minimum/active/modules/disabled
fi
if [ $1 -eq 1 ]; then
for p in $modules; do
    touch %{_sharedstatedir}/selinux/minimum/active/modules/disabled/$p
done
for p in $basemodules $enabledmodules; do
    rm -f %{_sharedstatedir}/selinux/minimum/active/modules/disabled/$p
done
%{_sbindir}/semanage import -S minimum -f - << __eof
login -m  -s unconfined_u -r s0-s0:c0.c1023 __default__
login -m  -s unconfined_u -r s0-s0:c0.c1023 root
__eof
%{_sbindir}/restorecon -R /root /var/log /var/run 2> /dev/null
%{_sbindir}/semodule -B -s minimum 2> /dev/null
else
instpackages=`cat %{_datadir}/selinux/minimum/instmodules.lst`
for p in $packages; do
    touch %{_sharedstatedir}/selinux/minimum/active/modules/disabled/$p
done
for p in $instpackages apache dbus inetd kerberos mta nis; do
    rm -f %{_sharedstatedir}/selinux/minimum/active/modules/disabled/$p
done
%{_sbindir}/semodule -B -s minimum 2> /dev/null
%relabel minimum
fi
exit 0

%posttrans minimum
%checkConfigConsistency minimum
%{_libexecdir}/selinux/varrun-convert.sh minimum
%{_libexecdir}/selinux/binsbin-convert.sh minimum
%{_sbindir}/restorecon -Ri /usr/lib/sysimage/rpm /var/lib/rpm

%postun minimum
if [ $1 = 0 ]; then
    if [ -s %{_sysconfdir}/selinux/config ]; then
        source %{_sysconfdir}/selinux/config &> /dev/null || true
    fi
    if [ "$SELINUXTYPE" = "minimum" ]; then
        %{_sbindir}/setenforce 0 2> /dev/null
        if [ ! -s %{_sysconfdir}/selinux/config ]; then
            echo "SELINUX=disabled" > %{_sysconfdir}/selinux/config
        else
            sed -i 's/^SELINUX=.*/SELINUX=disabled/g' %{_sysconfdir}/selinux/config
        fi
    fi
fi
exit 0

%files minimum -f %{buildroot}%{_datadir}/selinux/minimum/nonbasemodules.lst
%config(noreplace) %{_sysconfdir}/selinux/minimum/contexts/users/unconfined_u
%config(noreplace) %{_sysconfdir}/selinux/minimum/contexts/users/sysadm_u
%fileList minimum
%{_datadir}/selinux/minimum/modules-enabled.lst
%endif

%if %{with mls}
%package mls
Summary: SELinux MLS policy
Provides: selinux-policy-any = %{version}-%{release}
Obsoletes: selinux-policy-mls-sources < 2
Requires: policycoreutils-newrole >= %{POLICYCOREUTILSVER} setransd
Requires(pre): policycoreutils >= %{POLICYCOREUTILSVER}
Requires(pre): coreutils
Requires(pre): selinux-policy = %{version}-%{release}
Requires: selinux-policy = %{version}-%{release}
Conflicts:  seedit
Conflicts: container-selinux <= 1.9.0-9

%description mls
SELinux MLS (Multi Level Security) policy package.

%pretrans mls -p <lua>
%backupConfigLua

%pre mls
%preInstall mls

%post mls
%checkConfigConsistency mls
exit 0

%posttrans mls
%checkConfigConsistency mls
%{_libexecdir}/selinux/varrun-convert.sh mls
%{_libexecdir}/selinux/binsbin-convert.sh mls
%postInstall $1 mls
%{_sbindir}/restorecon -Ri /usr/lib/sysimage/rpm /var/lib/rpm

%postun mls
if [ $1 = 0 ]; then
    if [ -s %{_sysconfdir}/selinux/config ]; then
        source %{_sysconfdir}/selinux/config &> /dev/null || true
    fi
    if [ "$SELINUXTYPE" = "mls" ]; then
        %{_sbindir}/setenforce 0 2> /dev/null
        if [ ! -s %{_sysconfdir}/selinux/config ]; then
            echo "SELINUX=disabled" > %{_sysconfdir}/selinux/config
        else
            sed -i 's/^SELINUX=.*/SELINUX=disabled/g' %{_sysconfdir}/selinux/config
        fi
    fi
fi
exit 0

%files mls -f %{buildroot}%{_datadir}/selinux/mls/nonbasemodules.lst
%config(noreplace) %{_sysconfdir}/dnf/protected.d/selinux-policy-mls.conf
%config(noreplace) %{_sysconfdir}/selinux/mls/contexts/users/unconfined_u
%fileList mls
%endif

%changelog
%autochangelog
