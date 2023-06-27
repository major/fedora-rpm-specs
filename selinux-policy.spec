# github repo with selinux-policy sources
%global giturl https://github.com/fedora-selinux/selinux-policy
%global commit babc97bc83af7be306fcfaac65485faa09edfe89
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%define distro redhat
%define polyinstatiate n
%define monolithic n
%if %{?BUILD_DOC:0}%{!?BUILD_DOC:1}
%define BUILD_DOC 1
%endif
%if %{?BUILD_TARGETED:0}%{!?BUILD_TARGETED:1}
%define BUILD_TARGETED 1
%endif
%if %{?BUILD_MINIMUM:0}%{!?BUILD_MINIMUM:1}
%define BUILD_MINIMUM 1
%endif
%if %{?BUILD_MLS:0}%{!?BUILD_MLS:1}
%define BUILD_MLS 1
%endif
%define POLICYVER 33
%define POLICYCOREUTILSVER 3.4-1
%define CHECKPOLICYVER 3.2
Summary: SELinux policy configuration
Name: selinux-policy
Version: 38.18
Release: 1%{?dist}
License: GPL-2.0-or-later
Source: %{giturl}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Source1: modules-targeted-base.conf
Source31: modules-targeted-contrib.conf
Source2: booleans-targeted.conf
Source3: Makefile.devel
Source4: setrans-targeted.conf
Source5: modules-mls-base.conf
Source32: modules-mls-contrib.conf
Source6: booleans-mls.conf
Source8: setrans-mls.conf
Source14: securetty_types-targeted
Source15: securetty_types-mls
#Source16: modules-minimum.conf
Source17: booleans-minimum.conf
Source18: setrans-minimum.conf
Source19: securetty_types-minimum
Source20: customizable_types
Source22: users-mls
Source23: users-targeted
Source25: users-minimum
Source26: file_contexts.subs_dist
Source27: selinux-policy.conf
Source28: permissivedomains.cil
Source30: booleans.subs_dist

# Tool helps during policy development, to expand system m4 macros to raw allow rules
# Git repo: https://github.com/fedora-selinux/macro-expander.git
Source33: macro-expander

# Include SELinux policy for container from separate container-selinux repo
# Git repo: https://github.com/containers/container-selinux.git
Source35: container-selinux.tgz

Source36: selinux-check-proper-disable.service

# Provide rpm macros for packages installing SELinux modules
Source102: rpm.macros

Url: %{giturl}
BuildArch: noarch
BuildRequires: python3 gawk checkpolicy >= %{CHECKPOLICYVER} m4 policycoreutils-devel >= %{POLICYCOREUTILSVER} bzip2
BuildRequires: make
BuildRequires: systemd-rpm-macros
Requires(pre): policycoreutils >= %{POLICYCOREUTILSVER}
Requires(post): /bin/awk /usr/bin/sha512sum
Requires(meta): rpm-plugin-selinux
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
%{_sbindir}/semodule -n -X 100 -i %{_datadir}/selinux/packages/sandbox.pp
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
%{_mandir}/ru/*/*
%exclude %{_mandir}/man8/container_selinux.8.gz
%doc %{_datadir}/doc/%{name}

%define common_params DISTRO=%{distro} UBAC=n DIRECT_INITRC=n MONOLITHIC=%{monolithic} MLS_CATS=1024 MCS_CATS=1024

%define makeCmds() \
%make_build %common_params UNK_PERMS=%3 NAME=%1 TYPE=%2 bare \
%make_build %common_params UNK_PERMS=%3 NAME=%1 TYPE=%2 conf \
cp -f selinux_config/booleans-%1.conf ./policy/booleans.conf \
cp -f selinux_config/users-%1 ./policy/users \
#cp -f selinux_config/modules-%1-base.conf  ./policy/modules.conf \

%define makeModulesConf() \
cp -f selinux_config/modules-%1-%2.conf  ./policy/modules-base.conf \
cp -f selinux_config/modules-%1-%2.conf  ./policy/modules.conf \
if [ %3 == "contrib" ];then \
	cp selinux_config/modules-%1-%3.conf ./policy/modules-contrib.conf; \
	cat selinux_config/modules-%1-%3.conf >> ./policy/modules.conf; \
fi; \

%define installCmds() \
%make_build %common_params UNK_PERMS=%3 NAME=%1 TYPE=%2 base.pp \
%make_build %common_params UNK_PERMS=%3 NAME=%1 TYPE=%2 validate modules \
make %common_params UNK_PERMS=%3 NAME=%1 TYPE=%2 DESTDIR=%{buildroot} install \
make %common_params UNK_PERMS=%3 NAME=%1 TYPE=%2 DESTDIR=%{buildroot} install-appconfig \
make %common_params UNK_PERMS=%3 NAME=%1 TYPE=%2 DESTDIR=%{buildroot} SEMODULE="%{_sbindir}/semodule -p %{buildroot} -X 100 " load \
%{__mkdir} -p %{buildroot}%{_sysconfdir}/selinux/%1/logins \
touch %{buildroot}%{_sysconfdir}/selinux/%1/contexts/files/file_contexts.subs \
install -m0644 selinux_config/securetty_types-%1 %{buildroot}%{_sysconfdir}/selinux/%1/contexts/securetty_types \
install -m0644 selinux_config/file_contexts.subs_dist %{buildroot}%{_sysconfdir}/selinux/%1/contexts/files \
install -m0644 selinux_config/setrans-%1.conf %{buildroot}%{_sysconfdir}/selinux/%1/setrans.conf \
install -m0644 selinux_config/customizable_types %{buildroot}%{_sysconfdir}/selinux/%1/contexts/customizable_types \
touch %{buildroot}%{_sysconfdir}/selinux/%1/contexts/files/file_contexts.bin \
touch %{buildroot}%{_sysconfdir}/selinux/%1/contexts/files/file_contexts.local \
touch %{buildroot}%{_sysconfdir}/selinux/%1/contexts/files/file_contexts.local.bin \
cp %{SOURCE30} %{buildroot}%{_sysconfdir}/selinux/%1 \
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
%{_datadir}/selinux/%1/modules-base.lst \
%{_datadir}/selinux/%1/modules-contrib.lst \
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
if %{_sbindir}/restorecon -e /run/media -R /root /var/log /var/run /etc/passwd* /etc/group* /etc/*shadow* 2> /dev/null;then \
    continue; \
fi;

%define preInstall() \
if [ $1 -ne 1 ] && [ -s %{_sysconfdir}/selinux/config ]; then \
     for MOD_NAME in ganesha ipa_custodia kdbus; do \
        if [ -d %{_sharedstatedir}/selinux/%1/active/modules/100/$MOD_NAME ]; then \
           %{_sbindir}/semodule -n -d $MOD_NAME; \
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
%{_sbindir}/semodule -B -n -s %2; \
[ "${SELINUXTYPE}" == "%2" ] && %{_sbindir}/selinuxenabled && load_policy; \
if [ %1 -eq 1 ]; then \
   %{_sbindir}/restorecon -R /root /var/log /run /etc/passwd* /etc/group* /etc/*shadow* 2> /dev/null; \
else \
%relabel %2 \
fi;

%define modulesList() \
awk '$1 !~ "/^#/" && $2 == "=" && $3 == "module" { printf "%%s ", $1 }' ./policy/modules-base.conf > %{buildroot}%{_datadir}/selinux/%1/modules-base.lst \
awk '$1 !~ "/^#/" && $2 == "=" && $3 == "base" { printf "%%s ", $1 }' ./policy/modules-base.conf > %{buildroot}%{_datadir}/selinux/%1/base.lst \
if [ -e ./policy/modules-contrib.conf ];then \
	awk '$1 !~ "/^#/" && $2 == "=" && $3 == "module" { printf "%%s ", $1 }' ./policy/modules-contrib.conf > %{buildroot}%{_datadir}/selinux/%1/modules-contrib.lst; \
fi;

%define nonBaseModulesList() \
contrib_modules=`cat %{buildroot}%{_datadir}/selinux/%1/modules-contrib.lst` \
base_modules=`cat %{buildroot}%{_datadir}/selinux/%1/modules-base.lst` \
for i in $contrib_modules $base_modules; do \
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

%build

%prep
%autosetup -p 1 -n %{name}-%{commit}
tar -C policy/modules/contrib -xf %{SOURCE35}

mkdir selinux_config
for i in %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} %{SOURCE8} %{SOURCE14} %{SOURCE15} %{SOURCE17} %{SOURCE18} %{SOURCE19} %{SOURCE20} %{SOURCE22} %{SOURCE23} %{SOURCE25} %{SOURCE26} %{SOURCE31} %{SOURCE32};do
 cp $i selinux_config
done

%install
# Build targeted policy
%{__rm} -fR %{buildroot}
mkdir -p %{buildroot}%{_sysconfdir}/selinux
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
touch %{buildroot}%{_sysconfdir}/selinux/config
touch %{buildroot}%{_sysconfdir}/sysconfig/selinux
mkdir -p %{buildroot}%{_usr}/lib/tmpfiles.d/
cp %{SOURCE27} %{buildroot}%{_usr}/lib/tmpfiles.d/
mkdir -p %{buildroot}%{_bindir}
install -m 755  %{SOURCE33} %{buildroot}%{_bindir}/

# Always create policy module package directories
mkdir -p %{buildroot}%{_datadir}/selinux/{targeted,mls,minimum,modules}/
mkdir -p %{buildroot}%{_sharedstatedir}/selinux/{targeted,mls,minimum,modules}/

mkdir -p %{buildroot}%{_datadir}/selinux/packages

# Install devel
make clean
%if %{BUILD_TARGETED}
# Build targeted policy
%makeCmds targeted mcs allow
%makeModulesConf targeted base contrib
%installCmds targeted mcs allow
# install permissivedomains.cil
%{_sbindir}/semodule -p %{buildroot} -X 100 -s targeted -i %{SOURCE28}
# recreate sandbox.pp
rm -rf %{buildroot}%{_sharedstatedir}/selinux/targeted/active/modules/100/sandbox
%make_build %common_params UNK_PERMS=allow NAME=targeted TYPE=mcs sandbox.pp
mv sandbox.pp %{buildroot}%{_datadir}/selinux/packages/sandbox.pp
%modulesList targeted
%nonBaseModulesList targeted
%endif

%if %{BUILD_MINIMUM}
# Build minimum policy
%makeCmds minimum mcs allow
%makeModulesConf targeted base contrib
%installCmds minimum mcs allow
rm -rf %{buildroot}%{_sharedstatedir}/selinux/minimum/active/modules/100/sandbox
%modulesList minimum
%nonBaseModulesList minimum
%endif

%if %{BUILD_MLS}
# Build mls policy
%makeCmds mls mls deny
%makeModulesConf mls base contrib
%installCmds mls mls deny
%modulesList mls
%nonBaseModulesList mls
%endif

# remove leftovers when save-previous=true (semanage.conf) is used
rm -rf %{buildroot}%{_sharedstatedir}/selinux/{minimum,targeted,mls}/previous

mkdir -p %{buildroot}%{_mandir}
cp -R  man/* %{buildroot}%{_mandir}
make %common_params UNK_PERMS=allow NAME=targeted TYPE=mcs DESTDIR=%{buildroot} PKGNAME=%{name} install-docs
make %common_params UNK_PERMS=allow NAME=targeted TYPE=mcs DESTDIR=%{buildroot} PKGNAME=%{name} install-headers
mkdir %{buildroot}%{_datadir}/selinux/devel/
mv %{buildroot}%{_datadir}/selinux/targeted/include %{buildroot}%{_datadir}/selinux/devel/include
install -m 644 selinux_config/Makefile.devel %{buildroot}%{_datadir}/selinux/devel/Makefile
install -m 644 doc/example.* %{buildroot}%{_datadir}/selinux/devel/
install -m 644 doc/policy.* %{buildroot}%{_datadir}/selinux/devel/
%{_bindir}/sepolicy manpage -a -p %{buildroot}%{_datadir}/man/man8/ -w -r %{buildroot}
mkdir %{buildroot}%{_datadir}/selinux/devel/html
mv %{buildroot}%{_datadir}/man/man8/*.html %{buildroot}%{_datadir}/selinux/devel/html
mv %{buildroot}%{_datadir}/man/man8/style.css %{buildroot}%{_datadir}/selinux/devel/html

mkdir -p %{buildroot}%{_rpmconfigdir}/macros.d
install -m 644 %{SOURCE102} %{buildroot}%{_rpmconfigdir}/macros.d/macros.selinux-policy
sed -i 's/SELINUXPOLICYVERSION/%{version}-%{release}/' %{buildroot}%{_rpmconfigdir}/macros.d/macros.selinux-policy
sed -i 's@SELINUXSTOREPATH@%{_sharedstatedir}/selinux@' %{buildroot}%{_rpmconfigdir}/macros.d/macros.selinux-policy

mkdir -p %{buildroot}%{_unitdir}
install -m 644 %{SOURCE36} %{buildroot}%{_unitdir}

rm -rf selinux_config

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

%if %{BUILD_TARGETED}
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

%pre targeted
%preInstall targeted

%post targeted
%checkConfigConsistency targeted
%postInstall $1 targeted
exit 0

%posttrans targeted
%checkConfigConsistency targeted
%{_sbindir}/restorecon -Ri /usr/lib/sysimage/rpm /var/lib/rpm

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
%{_sbindir}/selinuxenabled && %{_sbindir}/semodule -nB
exit 0

%triggerpostun -- selinux-policy-targeted < 3.12.1-74
rm -f %{_sysconfdir}/selinux/*/modules/active/modules/sandbox.pp.disabled 2>/dev/null
exit 0

%triggerpostun targeted -- selinux-policy-targeted < 3.13.1-138
CR=$'\n'
INPUT=""
for i in `find %{_sysconfdir}/selinux/targeted/modules/active/modules/ -name \*disabled`; do
    module=`basename $i | sed 's/.pp.disabled//'`
    if [ -d %{_sharedstatedir}/selinux/targeted/active/modules/100/$module ]; then
        touch %{_sharedstatedir}/selinux/targeted/active/modules/disabled/$p
    fi
done
for i in `find %{_sysconfdir}/selinux/targeted/modules/active/modules/ -name \*.pp`; do
    INPUT="${INPUT}${CR}module -N -a $i"
done
for i in $(find %{_sysconfdir}/selinux/targeted/modules/active -name \*.local); do
    cp $i %{_sharedstatedir}/selinux/targeted/active
done
echo "$INPUT" | %{_sbindir}/semanage import -S targeted -N
if %{_sbindir}/selinuxenabled ; then
        %{_sbindir}/load_policy
fi
exit 0

%files targeted -f %{buildroot}%{_datadir}/selinux/targeted/nonbasemodules.lst
%config(noreplace) %{_sysconfdir}/selinux/targeted/contexts/users/unconfined_u
%config(noreplace) %{_sysconfdir}/selinux/targeted/contexts/users/sysadm_u
%fileList targeted
%verify(not md5 size mtime) %{_sharedstatedir}/selinux/targeted/active/modules/100/permissivedomains
%endif

%if %{BUILD_MINIMUM}
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
contribpackages=`cat %{_datadir}/selinux/minimum/modules-contrib.lst`
basepackages=`cat %{_datadir}/selinux/minimum/modules-base.lst`
if [ ! -d %{_sharedstatedir}/selinux/minimum/active/modules/disabled ]; then
    mkdir %{_sharedstatedir}/selinux/minimum/active/modules/disabled
fi
if [ $1 -eq 1 ]; then
for p in $contribpackages; do
    touch %{_sharedstatedir}/selinux/minimum/active/modules/disabled/$p
done
for p in $basepackages apache dbus inetd kerberos mta nis; do
    rm -f %{_sharedstatedir}/selinux/minimum/active/modules/disabled/$p
done
%{_sbindir}/semanage import -S minimum -f - << __eof
login -m  -s unconfined_u -r s0-s0:c0.c1023 __default__
login -m  -s unconfined_u -r s0-s0:c0.c1023 root
__eof
%{_sbindir}/restorecon -R /root /var/log /var/run 2> /dev/null
%{_sbindir}/semodule -B -s minimum
else
instpackages=`cat %{_datadir}/selinux/minimum/instmodules.lst`
for p in $contribpackages; do
    touch %{_sharedstatedir}/selinux/minimum/active/modules/disabled/$p
done
for p in $instpackages apache dbus inetd kerberos mta nis; do
    rm -f %{_sharedstatedir}/selinux/minimum/active/modules/disabled/$p
done
%{_sbindir}/semodule -B -s minimum
%relabel minimum
fi
exit 0

%posttrans minimum
%checkConfigConsistency minimum
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

%triggerpostun minimum -- selinux-policy-minimum < 3.13.1-138
if [ `ls -A %{_sharedstatedir}/selinux/minimum/active/modules/disabled/` ]; then
    rm -f %{_sharedstatedir}/selinux/minimum/active/modules/disabled/*
fi
CR=$'\n'
INPUT=""
for i in `find %{_sysconfdir}/selinux/minimum/modules/active/modules/ -name \*disabled`; do
    module=`basename $i | sed 's/.pp.disabled//'`
    if [ -d %{_sharedstatedir}/selinux/minimum/active/modules/100/$module ]; then
        touch %{_sharedstatedir}/selinux/minimum/active/modules/disabled/$p
    fi
done
for i in `find %{_sysconfdir}/selinux/minimum/modules/active/modules/ -name \*.pp`; do
    INPUT="${INPUT}${CR}module -N -a $i"
done
echo "$INPUT" | %{_sbindir}/semanage import -S minimum -N
if %{_sbindir}/selinuxenabled ; then
    %{_sbindir}/load_policy
fi
exit 0

%files minimum -f %{buildroot}%{_datadir}/selinux/minimum/nonbasemodules.lst
%config(noreplace) %{_sysconfdir}/selinux/minimum/contexts/users/unconfined_u
%config(noreplace) %{_sysconfdir}/selinux/minimum/contexts/users/sysadm_u
%fileList minimum
%endif

%if %{BUILD_MLS}
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
%postInstall $1 mls
exit 0

%posttrans mls
%checkConfigConsistency mls
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

%triggerpostun mls -- selinux-policy-mls < 3.13.1-138
CR=$'\n'
INPUT=""
for i in `find %{_sysconfdir}/selinux/mls/modules/active/modules/ -name \*disabled`; do
    module=`basename $i | sed 's/.pp.disabled//'`
    if [ -d %{_sharedstatedir}/selinux/mls/active/modules/100/$module ]; then
        touch %{_sharedstatedir}/selinux/mls/active/modules/disabled/$p
    fi
done
for i in `find %{_sysconfdir}/selinux/mls/modules/active/modules/ -name \*.pp`; do
    INPUT="${INPUT}${CR}module -N -a $i"
done
echo "$INPUT" | %{_sbindir}/semanage import -S mls -N
if %{_sbindir}/selinuxenabled ; then
        %{_sbindir}/load_policy
fi
exit 0


%files mls -f %{buildroot}%{_datadir}/selinux/mls/nonbasemodules.lst
%config(noreplace) %{_sysconfdir}/selinux/mls/contexts/users/unconfined_u
%fileList mls
%endif

%changelog
* Sun Jun 25 2023 Zdenek Pytela <zpytela@redhat.com> - 38.18-1
- Add support for kafs-dns requested by keyutils
- Allow insights-client execmem
- Add support for chronyd-restricted
- Add init_explicit_domain() interface
- Allow fsadm_t to get attributes of cgroup filesystems
- Add list_dir_perms to kerberos_read_keytab
- Label /var/run/tmpfiles.d/static-nodes.conf with kmod_var_run_t
- Allow sendmail manage its runtime files
- Allow keyutils_dns_resolver_exec_t be an entrypoint
- Allow collectd_t read network state symlinks
- Revert "Allow collectd_t read proc_net link files"
- Allow nfsd_t to list exports_t dirs
- Allow cupsd dbus chat with xdm
- Allow haproxy read hardware state information
- Add the kafs module

* Thu Jun 15 2023 Zdenek Pytela <zpytela@redhat.com> - 38.17-1
- Label /dev/userfaultfd with userfaultfd_t
- Allow blueman send general signals to unprivileged user domains
- Allow dkim-milter domain transition to sendmail
- Label /usr/sbin/cifs.idmap with cifs_helper_exec_t
- Allow cifs-helper read sssd kerberos configuration files
- Allow rpm_t sys_admin capability
- Allow dovecot_deliver_t create/map dovecot_spool_t dir/file
- Allow collectd_t read proc_net link files
- Allow insights-client getsession process permission
- Allow insights-client work with pipe and socket tmp files
- Allow insights-client map generic log files
- Update cyrus_stream_connect() to use sockets in /run
- Allow keyutils-dns-resolver read/view kernel key ring
- Label /var/log/kdump.log with kdump_log_t

* Fri Jun 09 2023 Zdenek Pytela <zpytela@redhat.com> - 38.16-1
- Add support for the systemd-pstore service
- Allow kdumpctl_t to execmem
- Update sendmail policy module for opensmtpd
- Allow nagios-mail-plugin exec postfix master
- Allow subscription-manager execute ip
- Allow ssh client connect with a user dbus instance
- Add support for ksshaskpass
- Allow rhsmcertd file transition in /run also for socket files
- Allow keyutils_dns_resolver_t execute keyutils_dns_resolver_exec_t
- Allow plymouthd read/write X server miscellaneous devices
- Allow systemd-sleep read udev pid files
- Allow exim read network sysctls
- Allow sendmail request load module
- Allow named map its conf files
- Allow squid map its cache files
- Allow NetworkManager_dispatcher_dhclient_t to execute shells without a domain transition

* Tue May 30 2023 Zdenek Pytela <zpytela@redhat.com> - 38.15-1
- Update policy for systemd-sleep
- Remove permissive domain for rshim_t
- Remove permissive domain for mptcpd_t
- Allow systemd-bootchartd the sys_ptrace userns capability
- Allow sysadm_t read nsfs files
- Allow sysadm_t run kernel bpf programs
- Update ssh_role_template for ssh-agent
- Update ssh_role_template to allow read/write unallocated ttys
- Add the booth module to modules.conf
- Allow firewalld rw ica_tmpfs_t files

* Fri May 26 2023 Zdenek Pytela <zpytela@redhat.com> - 38.14-1
- Remove permissive domain for cifs_helper_t
- Update the cifs-helper policy
- Replace cifsutils_helper_domtrans() with keyutils_request_domtrans_to()
- Update pkcsslotd policy for sandboxing
- Allow abrt_t read kernel persistent storage files
- Dontaudit targetd search httpd config dirs
- Allow init_t nnp domain transition to policykit_t
- Allow rpcd_lsad setcap and use generic ptys
- Allow samba-dcerpcd connect to systemd_machined over a unix socket
- Allow wireguard to rw network sysctls
- Add policy for boothd
- Allow kernel to manage its own BPF objects
- Label /usr/lib/systemd/system/proftpd.* & vsftpd.* with ftpd_unit_file_t

* Mon May 22 2023 Zdenek Pytela <zpytela@redhat.com> - 38.13-1
- Add initial policy for cifs-helper
- Label key.dns_resolver with keyutils_dns_resolver_exec_t
- Allow unconfined_service_t to create .gnupg labeled as gpg_secret_t
- Allow some systemd services write to cgroup files
- Allow NetworkManager_dispatcher_dhclient_t to read the DHCP configuration files
- Allow systemd resolved to bind to arbitrary nodes
- Allow plymouthd_t bpf capability to run bpf programs
- Allow cupsd to create samba_var_t files
- Allow rhsmcert request the kernel to load a module
- Allow virsh name_connect virt_port_t
- Allow certmonger manage cluster library files
- Allow plymouthd read init process state
- Add chromium_sandbox_t setcap capability
- Allow snmpd read raw disk data
- Allow samba-rpcd work with passwords
- Allow unconfined service inherit signal state from init
- Allow cloud-init manage gpg admin home content
- Allow cluster_t dbus chat with various services
- Allow nfsidmapd work with systemd-userdbd and sssd
- Allow unconfined_domain_type use IORING_OP_URING_CMD on all device nodes
- Allow plymouthd map dri and framebuffer devices
- Allow rpmdb_migrate execute rpmdb
- Allow logrotate dbus chat with systemd-hostnamed
- Allow icecast connect to kernel using a unix stream socket
- Allow lldpad connect to systemd-userdbd over a unix socket
- Allow journalctl open user domain ptys and ttys
- Allow keepalived to manage its tmp files
- Allow ftpd read network sysctls
- Label /run/bgpd with zebra_var_run_t
- Allow gssproxy read network sysctls
- Add the cifsutils module

* Tue Apr 25 2023 Zdenek Pytela <zpytela@redhat.com> - 38.12-1
- Allow telnetd read network sysctls
- Allow munin system plugin read generic SSL certificates
- Allow munin system plugin create and use netlink generic socket
- Allow login_userdomain create user namespaces
- Allow request-key to send syslog messages
- Allow request-key to read/view any key
- Add fs_delete_pstore_files() interface
- Allow insights-client work with teamdctl
- Allow insights-client read unconfined service semaphores
- Allow insights-client get quotas of all filesystems
- Add fs_read_pstore_files() interface
- Allow generic kernel helper to read inherited kernel pipes

* Fri Apr 14 2023 Zdenek Pytela <zpytela@redhat.com> - 38.11-1
- Allow dovecot-deliver write to the main process runtime fifo files
- Allow dmidecode write to cloud-init tmp files
- Allow chronyd send a message to cloud-init over a datagram socket
- Allow cloud-init domain transition to insights-client domain
- Allow mongodb read filesystem sysctls
- Allow mongodb read network sysctls
- Allow accounts-daemon read generic systemd unit lnk files
- Allow blueman watch generic device dirs
- Allow nm-dispatcher tlp plugin create tlp dirs
- Allow systemd-coredump mounton /usr
- Allow rabbitmq to read network sysctls

* Tue Apr 04 2023 Zdenek Pytela <zpytela@redhat.com> - 38.10-1
- Allow certmonger dbus chat with the cron system domain
- Allow geoclue read network sysctls
- Allow geoclue watch the /etc directory
- Allow logwatch_mail_t read network sysctls
- Allow insights-client read all sysctls
- Allow passt manage qemu pid sock files

* Fri Mar 24 2023 Zdenek Pytela <zpytela@redhat.com> - 38.9-1
- Allow sssd read accountsd fifo files
- Add support for the passt_t domain
- Allow virtd_t and svirt_t work with passt
- Add new interfaces in the virt module
- Add passt interfaces defined conditionally
- Allow tshark the setsched capability
- Allow poweroff create connections to system dbus
- Allow wg load kernel modules, search debugfs dir
- Boolean: allow qemu-ga manage ssh home directory
- Label smtpd with sendmail_exec_t
- Label msmtp and msmtpd with sendmail_exec_t
- Allow dovecot to map files in /var/spool/dovecot

* Fri Mar 03 2023 Zdenek Pytela <zpytela@redhat.com> - 38.8-1
- Confine gnome-initial-setup
- Allow qemu-guest-agent create and use vsock socket
- Allow login_pgm setcap permission
- Allow chronyc read network sysctls
- Enhancement of the /usr/sbin/request-key helper policy
- Fix opencryptoki file names in /dev/shm
- Allow system_cronjob_t transition to rpm_script_t
- Revert "Allow system_cronjob_t domtrans to rpm_script_t"
- Add tunable to allow squid bind snmp port
- Allow staff_t getattr init pid chr & blk files and read krb5
- Allow firewalld to rw z90crypt device
- Allow httpd work with tokens in /dev/shm
- Allow svirt to map svirt_image_t char files
- Allow sysadm_t run initrc_t script and sysadm_r role access
- Allow insights-client manage fsadm pid files

* Wed Feb 08 2023 Zdenek Pytela <zpytela@redhat.com> - 38.7-1
- Allowing snapper to create snapshots of /home/ subvolume/partition
- Add boolean qemu-ga to run unconfined script
- Label systemd-journald feature LogNamespace
- Add none file context for polyinstantiated tmp dirs
- Allow certmonger read the contents of the sysfs filesystem
- Add journalctl the sys_resource capability
- Allow nm-dispatcher plugins read generic files in /proc
- Add initial policy for the /usr/sbin/request-key helper
- Additional support for rpmdb_migrate
- Add the keyutils module

* Mon Jan 30 2023 Zdenek Pytela <zpytela@redhat.com> - 38.6-1
- Boolean: allow qemu-ga read ssh home directory
- Allow kernel_t to read/write all sockets
- Allow kernel_t to UNIX-stream connect to all domains
- Allow systemd-resolved send a datagram to journald
- Allow kernel_t to manage and have "execute" access to all files
- Fix the files_manage_all_files() interface
- Allow rshim bpf cap2 and read sssd public files
- Allow insights-client work with su and lpstat
- Allow insights-client tcp connect to all ports
- Allow nm-cloud-setup dispatcher plugin restart nm services
- Allow unconfined user filetransition for sudo log files
- Allow modemmanager create hardware state information files
- Allow ModemManager all permissions for netlink route socket
- Allow wg to send msg to kernel, write to syslog and dbus connections
- Allow hostname_t to read network sysctls.
- Dontaudit ftpd the execmem permission
- Allow svirt request the kernel to load a module
- Allow icecast rename its log files
- Allow upsd to send signal to itself
- Allow wireguard to create udp sockets and read net_conf
- Use '%autosetup' instead of '%setup'
- Pass -p 1 to '%autosetup'

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 38.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jan 13 2023 Zdenek Pytela <zpytela@redhat.com> - 38.5-1
- Allow insights client work with gluster and pcp
- Add insights additional capabilities
- Add interfaces in domain, files, and unconfined modules
- Label fwupdoffline and fwupd-detect-cet with fwupd_exec_t
- Allow sudodomain use sudo.log as a logfile
- Allow pdns server map its library files and bind to unreserved ports
- Allow sysadm_t read/write ipmi devices
- Allow prosody manage its runtime socket files
- Allow kernel threads manage kernel keys
- Allow systemd-userdbd the sys_resource capability
- Allow systemd-journal list cgroup directories
- Allow apcupsd dbus chat with systemd-logind
- Allow nut_domain manage also files and sock_files in /var/run
- Allow winbind-rpcd make a TCP connection to the ldap port
- Label /usr/lib/rpm/rpmdb_migrate with rpmdb_exec_t
- Allow tlp read generic SSL certificates
- Allow systemd-resolved watch tmpfs directories
- Revert "Allow systemd-resolved watch tmpfs directories"

* Mon Dec 19 2022 Zdenek Pytela <zpytela@redhat.com> - 38.4-1
- Allow NetworkManager and wpa_supplicant the bpf capability
- Allow systemd-rfkill the bpf capability
- Allow winbind-rpcd manage samba_share_t files and dirs
- Label /var/lib/httpd/md(/.*)? with httpd_sys_rw_content_t
- Allow gpsd the sys_ptrace userns capability
- Introduce gpsd_tmp_t for sockfiles managed by gpsd_t
- Allow load_policy_t write to unallocated ttys
- Allow ndc read hardware state information
- Allow system mail service read inherited certmonger runtime files
- Add lpr_roles  to system_r roles
- Revert "Allow insights-client run lpr and allow the proper role"
- Allow stalld to read /sys/kernel/security/lockdown file
- Allow keepalived to set resource limits
- Add policy for mptcpd
- Add policy for rshim
- Allow admin users to create user namespaces
- Allow journalctl relabel with var_log_t and syslogd_var_run_t files
- Do not run restorecon /etc/NetworkManager/dispatcher.d in targeted
- Trim changelog so that it starts at F35 time
- Add mptcpd and rshim modules

* Wed Dec 14 2022 Zdenek Pytela <zpytela@redhat.com> - 38.3-1
- Allow insights-client dbus chat with various services
- Allow insights-client tcp connect to various ports
- Allow insights-client run lpr and allow the proper role
- Allow insights-client work with pcp and manage user config files
- Allow redis get user names
- Allow kernel threads to use fds from all domains
- Allow systemd-modules-load load kernel modules
- Allow login_userdomain watch systemd-passwd pid dirs
- Allow insights-client dbus chat with abrt
- Grant kernel_t certain permissions in the system class
- Allow systemd-resolved watch tmpfs directories
- Allow systemd-timedated watch init runtime dir
- Make `bootc` be `install_exec_t`
- Allow systemd-coredump create user_namespace
- Allow syslog the setpcap capability
- donaudit virtlogd and dnsmasq execmem

* Tue Dec 06 2022 Zdenek Pytela <zpytela@redhat.com> - 38.2-1
- Don't make kernel_t an unconfined domain
- Don't allow kernel_t to execute bin_t/usr_t binaries without a transition
- Allow kernel_t to execute systemctl to do a poweroff/reboot
- Grant basic permissions to the domain created by systemd_systemctl_domain()
- Allow kernel_t to request module loading
- Allow kernel_t to do compute_create
- Allow kernel_t to manage perf events
- Grant almost all capabilities to kernel_t
- Allow kernel_t to fully manage all devices
- Revert "In domain_transition_pattern there is no permission allowing caller domain to execu_no_trans on entrypoint, this patch fixing this issue"
- Allow pulseaudio to write to session_dbusd tmp socket files
- Allow systemd and unconfined_domain_type create user_namespace
- Add the user_namespace security class
- Reuse tmpfs_t also for the ramfs filesystem
- Label udf tools with fsadm_exec_t
- Allow networkmanager_dispatcher_plugin work with nscd
- Watch_sb all file type directories.
- Allow spamc read hardware state information files
- Allow sysadm read ipmi devices
- Allow insights client communicate with cupsd, mysqld, openvswitch, redis
- Allow insights client read raw memory devices
- Allow the spamd_update_t domain get generic filesystem attributes
- Dontaudit systemd-gpt-generator the sys_admin capability
- Allow ipsec_t only read tpm devices
- Allow cups-pdf connect to the system log service
- Allow postfix/smtpd read kerberos key table
- Allow syslogd read network sysctls
- Allow cdcc mmap dcc-client-map files
- Add watch and watch_sb dosfs interface

* Mon Nov 21 2022 Zdenek Pytela <zpytela@redhat.com> - 38.1-1
- Revert "Allow sysadm_t read raw memory devices"
- Allow systemd-socket-proxyd get attributes of cgroup filesystems
- Allow rpc.gssd read network sysctls
- Allow winbind-rpcd get attributes of device and pty filesystems
- Allow insights-client domain transition on semanage execution
- Allow insights-client create gluster log dir with a transition
- Allow insights-client manage generic locks
- Allow insights-client unix_read all domain semaphores
- Add domain_unix_read_all_semaphores() interface
- Allow winbind-rpcd use the terminal multiplexor
- Allow mrtg send mails
- Allow systemd-hostnamed dbus chat with init scripts
- Allow sssd dbus chat with system cronjobs
- Add interface to watch all filesystems
- Add watch_sb interfaces
- Add watch interfaces
- Allow dhcpd bpf capability to run bpf programs
- Allow netutils and traceroute bpf capability to run bpf programs
- Allow pkcs_slotd_t bpf capability to run bpf programs
- Allow xdm bpf capability to run bpf programs
- Allow pcscd bpf capability to run bpf programs
- Allow lldpad bpf capability to run bpf programs
- Allow keepalived bpf capability to run bpf programs
- Allow ipsec bpf capability to run bpf programs
- Allow fprintd bpf capability to run bpf programs
- Allow systemd-socket-proxyd get filesystems attributes
- Allow dirsrv_snmp_t to manage dirsrv_config_t & dirsrv_var_run_t files

* Mon Oct 31 2022 Zdenek Pytela <zpytela@redhat.com> - 37.14-1
- Allow rotatelogs read httpd_log_t symlinks
- Add winbind-rpcd to samba_enable_home_dirs boolean
- Allow system cronjobs dbus chat with setroubleshoot
- Allow setroubleshootd read device sysctls
- Allow virt_domain read device sysctls
- Allow rhcd compute selinux access vector
- Allow insights-client manage samba var dirs
- Label ports 10161-10162 tcp/udp with snmp
- Allow aide to connect to systemd_machined with a unix socket.
- Allow samba-dcerpcd use NSCD services over a unix stream socket
- Allow vlock search the contents of the /dev/pts directory
- Allow insights-client send null signal to rpm and system cronjob
- Label port 15354/tcp and 15354/udp with opendnssec
- Allow ftpd map ftpd_var_run files
- Allow targetclid to manage tmp files
- Allow insights-client connect to postgresql with a unix socket
- Allow insights-client domtrans on unix_chkpwd execution
- Add file context entries for insights-client and rhc
- Allow pulseaudio create gnome content (~/.config)
- Allow login_userdomain dbus chat with rhsmcertd
- Allow sbd the sys_ptrace capability
- Allow ptp4l_t name_bind ptp_event_port_t

* Mon Oct 03 2022 Zdenek Pytela <zpytela@redhat.com> - 37.13-1
- Remove the ipa module
- Allow sss daemons read/write unnamed pipes of cloud-init
- Allow postfix_mailqueue create and use unix dgram sockets
- Allow xdm watch user home directories
- Allow nm-dispatcher ddclient plugin load a kernel module
- Stop ignoring standalone interface files
- Drop cockpit module
- Allow init map its private tmp files
- Allow xenstored change its hard resource limits
- Allow system_mail-t read network sysctls
- Add bgpd sys_chroot capability

* Thu Sep 22 2022 Zdenek Pytela <zpytela@redhat.com> - 37.12-1
- nut-upsd: kernel_read_system_state, fs_getattr_cgroup
- Add numad the ipc_owner capability
- Allow gst-plugin-scanner read virtual memory sysctls
- Allow init read/write inherited user fifo files
- Update dnssec-trigger policy: setsched, module_request
- added policy for systemd-socket-proxyd
- Add the new 'cmd' permission to the 'io_uring' class
- Allow winbind-rpcd read and write its key ring
- Label /run/NetworkManager/no-stub-resolv.conf net_conf_t
- blueman-mechanism can read ~/.local/lib/python*/site-packages directory
- pidof executed by abrt can readlink /proc/*/exe
- Fix typo in comment
- Do not run restorecon /etc/NetworkManager/dispatcher.d in mls and minimum

* Wed Sep 14 2022 Zdenek Pytela <zpytela@redhat.com> - 37.11-1
- Allow tor get filesystem attributes
- Allow utempter append to login_userdomain stream
- Allow login_userdomain accept a stream connection to XDM
- Allow login_userdomain write to boltd named pipes
- Allow staff_u and user_u users write to bolt pipe
- Allow login_userdomain watch various directories
- Update rhcd policy for executing additional commands 5
- Update rhcd policy for executing additional commands 4
- Allow rhcd create rpm hawkey logs with correct label
- Allow systemd-gpt-auto-generator to check for empty dirs
- Update rhcd policy for executing additional commands 3
- Allow journalctl read rhcd fifo files
- Update insights-client policy for additional commands execution 5
- Allow init remount all file_type filesystems
- Confine insights-client systemd unit
- Update insights-client policy for additional commands execution 4
- Allow pcp pmcd search tracefs and acct_data dirs
- Allow httpd read network sysctls
- Dontaudit domain map permission on directories
- Revert "Allow X userdomains to mmap user_fonts_cache_t dirs"
- Revert "Allow xdm_t domain to mmap /var/lib/gdm/.cache/fontconfig BZ(1725509)"
- Update insights-client policy for additional commands execution 3
- Allow systemd permissions needed for sandboxed services
- Add rhcd module
- Make dependency on rpm-plugin-selinux unordered

* Fri Sep 02 2022 Zdenek Pytela <zpytela@redhat.com> - 37.10-1
- Allow ipsec_t read/write tpm devices
- Allow rhcd execute all executables
- Update rhcd policy for executing additional commands 2
- Update insights-client policy for additional commands execution 2
- Allow sysadm_t read raw memory devices
- Allow chronyd send and receive chronyd/ntp client packets
- Allow ssh client read kerberos homedir config files
- Label /var/log/rhc-worker-playbook with rhcd_var_log_t
- Update insights-client policy (auditctl, gpg, journal)
- Allow system_cronjob_t domtrans to rpm_script_t
- Allow smbd_t process noatsecure permission for winbind_rpcd_t
- Update tor_bind_all_unreserved_ports interface
- Allow chronyd bind UDP sockets to ptp_event ports.
- Allow unconfined and sysadm users transition for /root/.gnupg
- Add gpg_filetrans_admin_home_content() interface
- Update rhcd policy for executing additional commands
- Update insights-client policy for additional commands execution
- Add userdom_view_all_users_keys() interface
- Allow gpg read and write generic pty type
- Allow chronyc read and write generic pty type
- Allow system_dbusd ioctl kernel with a unix stream sockets
- Allow samba-bgqd to read a printer list
- Allow stalld get and set scheduling policy of all domains.
- Allow unconfined_t transition to targetclid_home_t

* Thu Aug 11 2022 Zdenek Pytela <zpytela@redhat.com> - 37.9-1
- Allow nm-dispatcher custom plugin dbus chat with nm
- Allow nm-dispatcher sendmail plugin get status of systemd services
- Allow xdm read the kernel key ring
- Allow login_userdomain check status of mount units
- Allow postfix/smtp and postfix/virtual read kerberos key table
- Allow services execute systemd-notify
- Do not allow login_userdomain use sd_notify()
- Allow launch-xenstored read filesystem sysctls
- Allow systemd-modules-load write to /dev/kmsg and send a message to syslogd
- Allow openvswitch fsetid capability
- Allow openvswitch use its private tmpfs files and dirs
- Allow openvswitch search tracefs dirs
- Allow pmdalinux read files on an nfsd filesystem
- Allow winbind-rpcd write to winbind pid files
- Allow networkmanager to signal unconfined process
- Allow systemd_hostnamed label /run/systemd/* as hostnamed_etc_t
- Allow samba-bgqd get a printer list
- fix(init.fc): Fix section description
- Allow fedora-third-party read the passwords file
- Remove permissive domain for rhcd_t
- Allow pmie read network state information and network sysctls
- Revert "Dontaudit domain the fowner capability"
- Allow sysadm_t to run bpftool on the userdomain attribute
- Add the userdom_prog_run_bpf_userdomain() interface
- Allow insights-client rpm named file transitions
- Add /var/tmp/insights-archive to insights_client_filetrans_named_content

* Mon Aug 01 2022 Zdenek Pytela <zpytela@redhat.com> - 37.8-1
- Allow sa-update to get init status and start systemd files
- Use insights_client_filetrans_named_content
- Make default file context match with named transitions
- Allow nm-dispatcher tlp plugin send system log messages
- Allow nm-dispatcher tlp plugin create and use unix_dgram_socket
- Add permissions to manage lnk_files into gnome_manage_home_config
- Allow rhsmcertd to read insights config files
- Label /etc/insights-client/machine-id
- fix(devices.fc): Replace single quote in comment to solve parsing issues
- Make NetworkManager_dispatcher_custom_t an unconfined domain

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 37.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 14 2022 Zdenek Pytela <zpytela@redhat.com> - 37.7-1
- Update winbind_rpcd_t
- Allow some domains use sd_notify()
- Revert "Allow rabbitmq to use systemd notify"
- fix(sedoctool.py): Fix syntax warning: "is not" with a literal
- Allow nm-dispatcher console plugin manage etc files
- Allow networkmanager_dispatcher_plugin list NetworkManager_etc_t dirs
- Allow nm-dispatcher console plugin setfscreate
- Support using systemd-update-helper in rpm scriptlets
- Allow nm-dispatcher winbind plugin read samba config files
- Allow domain use userfaultfd over all domains
- Allow cups-lpd read network sysctls

* Wed Jun 29 2022 Zdenek Pytela <zpytela@redhat.com> - 37.6-1
- Allow stalld set scheduling policy of kernel threads
- Allow targetclid read /var/target files
- Allow targetclid read generic SSL certificates (fixed)
- Allow firewalld read the contents of the sysfs filesystem
- Fix file context pattern for /var/target
- Use insights_client_etc_t in insights_search_config()
- Allow nm-dispatcher ddclient plugin handle systemd services
- Allow nm-dispatcher winbind plugin run smbcontrol
- Allow nm-dispatcher custom plugin create and use unix dgram socket
- Update samba-dcerpcd policy for kerberos usage 2
- Allow keepalived read the contents of the sysfs filesystem
- Allow amandad read network sysctls
- Allow cups-lpd read network sysctls
- Allow kpropd read network sysctls
- Update insights_client_filetrans_named_content()
- Allow rabbitmq to use systemd notify
- Label /var/target with targetd_var_t
- Allow targetclid read generic SSL certificates
- Update rhcd policy
- Allow rhcd search insights configuration directories
- Add the kernel_read_proc_files() interface
- Require policycoreutils >= 3.4-1
- Add a script for enclosing interfaces in ifndef statements
- Disable rpm verification on interface_info

* Wed Jun 22 2022 Zdenek Pytela <zpytela@redhat.com> - 37.5-1
- Allow transition to insights_client named content
- Add the insights_client_filetrans_named_content() interface
- Update policy for insights-client to run additional commands 3
- Allow dhclient manage pid files used by chronyd
- Allow stalld get scheduling policy of kernel threads
- Allow samba-dcerpcd work with sssd
- Allow dlm_controld send a null signal to a cluster daemon
- Allow ksmctl create hardware state information files
- Allow winbind_rpcd_t connect to self over a unix_stream_socket
- Update samba-dcerpcd policy for kerberos usage
- Allow insights-client execute its private memfd: objects
- Update policy for insights-client to run additional commands 2
- Use insights_client_tmp_t instead of insights_client_var_tmp_t
- Change space indentation to tab in insights-client
- Use socket permissions sets in insights-client
- Update policy for insights-client to run additional commands
- Change rpm_setattr_db_files() to use a pattern
- Allow init_t to rw insights_client unnamed pipe
- Add rpm setattr db files macro
- Fix insights client
- Update kernel_read_unix_sysctls() for sysctl_net_unix_t handling
- Allow rabbitmq to access its private memfd: objects
- Update policy for samba-dcerpcd
- Allow stalld setsched and sys_nice

* Tue Jun 07 2022 Zdenek Pytela <zpytela@redhat.com> - 37.4-1
- Allow auditd_t noatsecure for a transition to audisp_remote_t
- Allow ctdbd nlmsg_read on netlink_tcpdiag_socket
- Allow pcp_domain execute its private memfd: objects
- Add support for samba-dcerpcd
- Add policy for wireguard
- Confine targetcli
- Allow systemd work with install_t unix stream sockets
- Allow iscsid the sys_ptrace userns capability
- Allow xdm connect to unconfined_service_t over a unix stream socket

* Fri May 27 2022 Zdenek Pytela <zpytela@redhat.com> - 37.3-1
- Allow nm-dispatcher custom plugin execute systemctl
- Allow nm-dispatcher custom plugin dbus chat with nm
- Allow nm-dispatcher custom plugin create and use udp socket
- Allow nm-dispatcher custom plugin create and use netlink_route_socket
- Use create_netlink_socket_perms in netlink_route_socket class permissions
- Add support for nm-dispatcher sendmail scripts
- Allow sslh net_admin capability
- Allow insights-client manage gpg admin home content
- Add the gpg_manage_admin_home_content() interface
- Allow rhsmcertd create generic log files
- Update logging_create_generic_logs() to use create_files_pattern()
- Label /var/cache/insights with insights_client_cache_t
- Allow insights-client search gconf homedir
- Allow insights-client create and use unix_dgram_socket
- Allow blueman execute its private memfd: files
- Move the chown call into make-srpm.sh

* Fri May 06 2022 Zdenek Pytela <zpytela@redhat.com> - 37.2-1
- Use the networkmanager_dispatcher_plugin attribute in allow rules
- Make a custom nm-dispatcher plugin transition
- Label port 4784/tcp and 4784/udp with bfd_multi
- Allow systemd watch and watch_reads user ptys
- Allow sblim-gatherd the kill capability
- Label more vdsm utils with virtd_exec_t
- Add ksm service to ksmtuned
- Add rhcd policy
- Dontaudit guest attempts to dbus chat with systemd domains
- Dontaudit guest attempts to dbus chat with system bus types
- Use a named transition in systemd_hwdb_manage_config()
- Add default fc specifications for patterns in /opt
- Add the files_create_etc_files() interface
- Allow nm-dispatcher console plugin create and write files in /etc
- Allow nm-dispatcher console plugin transition to the setfiles domain
- Allow more nm-dispatcher plugins append to init stream sockets
- Allow nm-dispatcher tlp plugin dbus chat with nm
- Reorder networkmanager_dispatcher_plugin_template() calls
- Allow svirt connectto virtlogd
- Allow blueman map its private memfd: files
- Allow sysadm user execute init scripts with a transition
- Allow sblim-sfcbd connect to sblim-reposd stream
- Allow keepalived_unconfined_script_t dbus chat with init
- Run restorecon with "-i" not to report errors

* Mon May 02 2022 Zdenek Pytela <zpytela@redhat.com> - 37.1-1
- Fix users for SELinux userspace 3.4
- Label /var/run/machine-id as machineid_t
- Add stalld to modules.conf
- Use files_tmpfs_file() for rhsmcertd_tmpfs_t
- Allow blueman read/write its private memfd: objects
- Allow insights-client read rhnsd config files
- Allow insights-client create_socket_perms for tcp/udp sockets

* Tue Apr 26 2022 Zdenek Pytela <zpytela@redhat.com> - 36.8-1
- Allow nm-dispatcher chronyc plugin append to init stream sockets
- Allow tmpreaper the sys_ptrace userns capability
- Label /usr/libexec/vdsm/supervdsmd and vdsmd with virtd_exec_t
- Allow nm-dispatcher tlp plugin read/write the wireless device
- Allow nm-dispatcher tlp plugin append to init socket
- Allow nm-dispatcher tlp plugin be client of a system bus
- Allow nm-dispatcher list its configuration directory
- Ecryptfs-private support
- Allow colord map /var/lib directories
- Allow ntlm_auth read the network state information
- Allow insights-client search rhnsd configuration directory

* Thu Apr 21 2022 Zdenek Pytela <zpytela@redhat.com> - 36.7-3
- Add support for nm-dispatcher tlp-rdw scripts
- Update github actions to satisfy git 2.36 stricter rules
- New policy for stalld
- Allow colord read generic files in /var/lib
- Allow xdm mounton user temporary socket files
- Allow systemd-gpt-auto-generator create and use netlink_kobject_uevent_socket
- Allow sssd domtrans to pkcs_slotd_t
- Allow keepalived setsched and sys_nice
- Allow xdm map generic files in /var/lib
- Allow xdm read generic symbolic links in /var/lib
- Allow pppd create a file in the locks directory
- Add file map permission to lpd_manage_spool() interface
- Allow system dbus daemon watch generic directories in /var/lib
- Allow pcscd the sys_ptrace userns capability
- Add the corecmd_watch_bin_dirs() interface

* Thu Apr 21 2022 Zdenek Pytela <zpytela@redhat.com> - 36.7-2
- Relabel explicitly some dirs in %posttrans scriptlets

* Thu Apr 21 2022 Zdenek Pytela <zpytela@redhat.com> - 36.7-1
- Add stalld module to modules-targeted-contrib.conf

* Mon Apr 04 2022 Zdenek Pytela <zpytela@redhat.com> - 36.6-1
- Add support for systemd-network-generator
- Add the io_uring class
- Allow nm-dispatcher dhclient plugin append to init stream sockets
- Relax the naming pattern for systemd private shared libraries
- Allow nm-dispatcher iscsid plugin append to init socket
- Add the init_append_stream_sockets() interface
- Allow nm-dispatcher dnssec-trigger script to execute pidof
- Add support for nm-dispatcher dnssec-trigger scripts
- Allow chronyd talk with unconfined user over unix domain dgram socket
- Allow fenced read kerberos key tables
- Add support for nm-dispatcher ddclient scripts
- Add systemd_getattr_generic_unit_files() interface
- Allow fprintd read and write hardware state information
- Allow exim watch generic certificate directories
- Remove duplicate fc entries for corosync and corosync-notifyd
- Label corosync-cfgtool with cluster_exec_t
- Allow qemu-kvm create and use netlink rdma sockets
- Allow logrotate a domain transition to cluster administrative domain

* Fri Mar 18 2022 Zdenek Pytela <zpytela@redhat.com> - 36.5-1
- Add support for nm-dispatcher console helper scripts
- Allow nm-dispatcher plugins read its directory and sysfs
- Do not let system_cronjob_t create redhat-access-insights.log with var_log_t
- devices: Add a comment about cardmgr_dev_t
- Add basic policy for BinderFS
- Label /var/run/ecblp0 pipe with cupsd_var_run_t
- Allow rpmdb create directory in /usr/lib/sysimage
- Allow rngd drop privileges via setuid/setgid/setcap
- Allow init watch and watch_reads user ttys
- Allow systemd-logind dbus chat with sosreport
- Allow chronyd send a message to sosreport over datagram socket
- Remove unnecessary /etc file transitions for insights-client
- Label all content in /var/lib/insights with insights_client_var_lib_t
- Update insights-client policy

* Wed Feb 23 2022 Zdenek Pytela <zpytela@redhat.com> - 36.4-2
- Add insights_client module to modules-targeted-contrib.conf

* Wed Feb 23 2022 Zdenek Pytela <zpytela@redhat.com> - 36.4-1
- Update NetworkManager-dispatcher cloud and chronyc policy
- Update insights-client: fc pattern, motd, writing to etc
- Allow systemd-sysctl read the security state information
- Allow init create and mounton to support PrivateDevices
- Allow sosreport dbus chat abrt systemd timedatex

* Tue Feb 22 2022 Zdenek Pytela <zpytela@redhat.com> - 36.3-2
- Update specfile to buildrequire policycoreutils-devel >= 3.3-4
- Add modules_checksum to %files

* Thu Feb 17 2022 Zdenek Pytela <zpytela@redhat.com> - 36.3-1
- Update NetworkManager-dispatcher policy to use scripts
- Allow init mounton kernel messages device
- Revert "Make dbus-broker service working on s390x arch"
- Remove permissive domain for insights_client_t
- Allow userdomain read symlinks in /var/lib
- Allow iptables list cgroup directories
- Dontaudit mdadm list dirsrv tmpfs dirs
- Dontaudit dirsrv search filesystem sysctl directories
- Allow chage domtrans to sssd
- Allow postfix_domain read dovecot certificates
- Allow systemd-networkd create and use netlink netfilter socket
- Allow nm-dispatcher read nm-dispatcher-script symlinks
- filesystem.te: add genfscon rule for ntfs3 filesystem
- Allow rhsmcertd get attributes of cgroup filesystems
- Allow sandbox_web_client_t watch various dirs
- Exclude container.if from policy devel files
- Run restorecon on /usr/lib/sysimage/rpm instead of /var/lib/rpm

* Fri Feb 11 2022 Zdenek Pytela <zpytela@redhat.com> - 36.2-1
- Allow sysadm_passwd_t to relabel passwd and group files
- Allow confined sysadmin to use tool vipw
- Allow login_userdomain map /var/lib/directories
- Allow login_userdomain watch library and fonts dirs
- Allow login_userdomain watch system configuration dirs
- Allow login_userdomain read systemd runtime files
- Allow ctdb create cluster logs
- Allow alsa bind mixer controls to led triggers
- New policy for insight-client
- Add mctp_socket security class and access vectors
- Fix koji repo URL pattern
- Update chronyd_pid_filetrans() to allow create dirs
- Update NetworkManager-dispatcher policy
- Allow unconfined to run virtd bpf
- Allow nm-privhelper setsched permission and send system logs
- Add the map permission to common_anon_inode_perm permission set
- Rename userfaultfd_anon_inode_perms to common_inode_perms
- Allow confined users to use kinit,klist and etc.
- Allow rhsmcertd create rpm hawkey logs with correct label

* Thu Feb 03 2022 Zdenek Pytela <zpytela@redhat.com> - 36.1-1
- Label exFAT utilities at /usr/sbin
- policy/modules/contrib: Support /usr/lib/sysimage/rpm as the rpmdb path
- Enable genfs_seclabel_symlinks policy capability
- Sync policy/policy_capabilities with refpolicy
- refpolicy: drop unused socket security classes
- Label new utility of NetworkManager nm-priv-helper
- Label NetworkManager-dispatcher service with separate context
- Allow sanlock get attributes of filesystems with extended attributes
- Associate stratisd_data_t with device filesystem
- Allow init read stratis data symlinks

* Tue Feb 01 2022 Zdenek Pytela <zpytela@redhat.com> - 35.13-1
- Allow systemd services watch dbusd pid directory and its parents
- Allow ModemManager connect to the unconfined user domain
- Label /dev/wwan.+ with modem_manager_t
- Allow alsactl set group Process ID of a process
- Allow domtrans to sssd_t and role access to sssd
- Creating interface sssd_run_sssd()
- Label utilities for exFAT filesystems with fsadm_exec_t
- Label /dev/nvme-fabrics with fixed_disk_device_t
- Allow init delete generic tmp named pipes
- Allow timedatex dbus chat with xdm

* Wed Jan 26 2022 Zdenek Pytela <zpytela@redhat.com> - 35.12-1
- Fix badly indented used interfaces
- Allow domain transition to sssd_t
- Dontaudit sfcbd sys_ptrace cap_userns
- Label /var/lib/plocate with locate_var_lib_t
- Allow hostapd talk with unconfined user over unix domain dgram socket
- Allow NetworkManager talk with unconfined user over unix domain dgram socket
- Allow system_mail_t read inherited apache system content rw files
- Add apache_read_inherited_sys_content_rw_files() interface
- Allow rhsm-service execute its private memfd: objects
- Allow dirsrv read configfs files and directories
- Label /run/stratisd with stratisd_var_run_t
- Allow tumblerd write to session_dbusd tmp socket files

* Wed Jan 19 2022 Zdenek Pytela <zpytela@redhat.com> - 35.11-1
- Revert "Label /etc/cockpit/ws-certs.d with cert_t"
- Allow login_userdomain write to session_dbusd tmp socket files
- Label /var/run/user/%{USERID}/dbus with session_dbusd_tmp_t

* Mon Jan 17 2022 Zdenek Pytela <zpytela@redhat.com> - 35.10-1
- Allow login_userdomain watch systemd-machined PID directories
- Allow login_userdomain watch systemd-logind PID directories
- Allow login_userdomain watch accountsd lib directories
- Allow login_userdomain watch localization directories
- Allow login_userdomain watch various files and dirs
- Allow login_userdomain watch generic directories in /tmp
- Allow rhsm-service read/write its private memfd: objects
- Allow radiusd connect to the radacct port
- Allow systemd-io-bridge ioctl rpm_script_t
- Allow systemd-coredump userns capabilities and root mounton
- Allow systemd-coredump read and write usermodehelper state
- Allow login_userdomain create session_dbusd tmp socket files
- Allow gkeyringd_domain write to session_dbusd tmp socket files
- Allow systemd-logind delete session_dbusd tmp socket files
- Allow gdm-x-session write to session dbus tmp sock files
- Label /etc/cockpit/ws-certs.d with cert_t
- Allow kpropd get attributes of cgroup filesystems
- Allow administrative users the bpf capability
- Allow sysadm_t start and stop transient services
- Connect triggerin to pcre2 instead of pcre

* Wed Jan 12 2022 Zdenek Pytela <zpytela@redhat.com> - 35.9-1
- Allow sshd read filesystem sysctl files
- Revert "Allow sshd read sysctl files"
- Allow tlp read its systemd unit
- Allow gssproxy access to various system files.
- Allow gssproxy read, write, and map ica tmpfs files
- Allow gssproxy read and write z90crypt device
- Allow sssd_kcm read and write z90crypt device
- Allow smbcontrol read the network state information
- Allow virt_domain map vhost devices
- Allow fcoemon request the kernel to load a module
- Allow sshd read sysctl files
- Ensure that `/run/systemd/*` are properly labeled
- Allow admin userdomains use socketpair()
- Change /run/user/[0-9]+ to /run/user/%{USERID} for proper labeling
- Allow lldpd connect to snmpd with a unix domain stream socket
- Dontaudit pkcsslotd sys_admin capability

* Thu Dec 23 2021 Zdenek Pytela <zpytela@redhat.com> - 35.8-1
- Allow haproxy get attributes of filesystems with extended attributes
- Allow haproxy get attributes of cgroup filesystems
- Allow sysadm execute sysadmctl in sysadm_t domain using sudo
- Allow userdomains use pam_ssh_agent_auth for passwordless sudo
- Allow sudodomains execute passwd in the passwd domain
- Allow braille printing in selinux
- Allow sandbox_xserver_t map sandbox_file_t
- Label /dev/ngXnY and /dev/nvme-subsysX with fixed_disk_device_t
- Add hwtracing_device_t type for hardware-level tracing and debugging
- Label port 9528/tcp with openqa_liveview
- Label /var/lib/shorewall6-lite with shorewall_var_lib_t
- Document Security Flask model in the policy

* Fri Dec 10 2021 Zdenek Pytela <zpytela@redhat.com> - 35.7-1
- Allow systemd read unlabeled symbolic links
- Label abrt-action-generate-backtrace with abrt_handle_event_exec_t
- Allow dnsmasq watch /etc/dnsmasq.d directories
- Allow rhsmcertd get attributes of tmpfs_t filesystems
- Allow lldpd use an snmp subagent over a tcp socket
- Allow xdm watch generic directories in /var/lib
- Allow login_userdomain open/read/map system journal
- Allow sysadm_t connect to cluster domains over a unix stream socket
- Allow sysadm_t read/write pkcs shared memory segments
- Allow sysadm_t connect to sanlock over a unix stream socket
- Allow sysadm_t dbus chat with sssd
- Allow sysadm_t set attributes on character device nodes
- Allow sysadm_t read and write watchdog devices
- Allow smbcontrol use additional socket types
- Allow cloud-init dbus chat with systemd-logind
- Allow svnserve send mail from the system
- Update userdom_exec_user_tmp_files() with an entrypoint rule
- Allow sudodomain send a null signal to sshd processes

* Fri Nov 19 2021 Zdenek Pytela <zpytela@redhat.com> - 35.6-1
- Allow PID 1 and dbus-broker IPC with a systemd user session
- Allow rpmdb read generic SSL certificates
- Allow rpmdb read admin home config files
- Report warning on duplicate definition of interface
- Allow redis get attributes of filesystems with extended attributes
- Allow sysadm_t dbus chat with realmd_t
- Make cupsd_lpd_t a daemon
- Allow tlp dbus-chat with NetworkManager
- filesystem: add fs_use_trans for ramfs
- Allow systemd-logind destroy unconfined user's IPC objects

* Thu Nov 04 2021 Zdenek Pytela <zpytela@redhat.com> - 35.5-1
- Support sanlock VG automated recovery on storage access loss 2/2
- Support sanlock VG automated recovery on storage access loss 1/2
- Revert "Support sanlock VG automated recovery on storage access loss"
- Allow tlp get service units status
- Allow fedora-third-party manage 3rd party repos
- Allow xdm_t nnp_transition to login_userdomain
- Add the auth_read_passwd_file() interface
- Allow redis-sentinel execute a notification script
- Allow fetchmail search cgroup directories
- Allow lvm_t to read/write devicekit disk semaphores
- Allow devicekit_disk_t to use /dev/mapper/control
- Allow devicekit_disk_t to get IPC info from the kernel
- Allow devicekit_disk_t to read systemd-logind pid files
- Allow devicekit_disk_t to mount filesystems on mnt_t directories
- Allow devicekit_disk_t to manage mount_var_run_t files
- Allow rasdaemon sys_admin capability to verify the CAP_SYS_ADMIN of the soft_offline_page function implemented in the kernel
- Use $releasever in koji repo to reduce rawhide hardcoding
- authlogin: add fcontext for tcb
- Add erofs as a SELinux capable file system
- Allow systemd execute user bin files
- Support sanlock VG automated recovery on storage access loss
- Support new PING_CHECK health checker in keepalived

* Wed Oct 20 2021 Zdenek Pytela <zpytela@redhat.com> - 35.4-1
- Allow fedora-third-party map generic cache files
- Add gnome_map_generic_cache_files() interface
- Add files_manage_var_lib_dirs() interface
- Allow fedora-third party manage gpg keys
- Allow fedora-third-party run "flatpak remote-add --from flathub"

* Tue Oct 19 2021 Zdenek Pytela <zpytela@redhat.com> - 35.3-1
- Allow fedora-third-party run flatpak post-install actions
- Allow fedora-third-party set_setsched and sys_nice

* Mon Oct 18 2021 Zdenek Pytela <zpytela@redhat.com> - 35.2-1
- Allow fedora-third-party execute "flatpak remote-add"
- Add files_manage_var_lib_files() interface
- Add write permisson to userfaultfd_anon_inode_perms
- Allow proper function sosreport via iotop
- Allow proper function sosreport in sysadmin role
- Allow fedora-third-party to connect to the system log service
- Allow fedora-third-party dbus chat with policykit
- Allow chrony-wait service start with DynamicUser=yes
- Allow management of lnk_files if similar access to regular files
- Allow unconfined_t transition to mozilla_plugin_t with NoNewPrivileges
- Allow systemd-resolved watch /run/systemd
- Allow fedora-third-party create and use unix_dgram_socket
- Removing pkcs_tmpfs_filetrans interface and edit pkcs policy files
- Allow login_userdomain named filetrans to pkcs_slotd_tmpfs_t domain

* Thu Oct 07 2021 Zdenek Pytela <zpytela@redhat.com> - 35.1-1
- Add fedoratp module
- Allow xdm_t domain transition to fedoratp_t
- Allow ModemManager create and use netlink route socket
- Add default file context for /run/gssproxy.default.sock
- Allow xdm_t watch fonts directories
- Allow xdm_t watch generic directories in /lib
- Allow xdm_t watch generic pid directories
