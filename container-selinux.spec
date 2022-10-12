%global debug_package   %{nil}

# container-selinux
%global git0 https://github.com/containers/container-selinux

%global built_tag v2.190.0
%global built_tag_strip %(b=%{built_tag}; echo ${b:1})
%global gen_version %(b=%{built_tag_strip}; echo ${b/-/"~"})

# container-selinux stuff (prefix with ds_ for version/release etc.)
# Some bits borrowed from the openstack-selinux package
%global selinuxtype targeted
%global moduletype services
%global modulenames container

# Usage: _format var format
# Expand 'modulenames' into various formats as needed
# Format must contain '$x' somewhere to do anything useful
%global _format() export %1=""; for x in %{modulenames}; do %1+=%2; %1+=" "; done;

# Hooked up to autobuilder, please check with @lsm5 before updating
Name: container-selinux
Epoch: 2
Version: %{gen_version}
Release: %autorelease
License: GPLv2
URL: %{git0}
Summary: SELinux policies for container runtimes
Source0: %{git0}/archive/v%{built_tag_strip}.tar.gz
BuildArch: noarch
BuildRequires: make
BuildRequires: git-core
BuildRequires: pkgconfig(systemd)
BuildRequires: selinux-policy >= %_selinux_policy_version
BuildRequires: selinux-policy-devel >= %_selinux_policy_version
# RE: rhbz#1195804 - ensure min NVR for selinux-policy
Requires: selinux-policy >= %_selinux_policy_version
Requires(post): selinux-policy-base >= %_selinux_policy_version
Requires(post): selinux-policy-targeted >= %_selinux_policy_version
Requires(post): policycoreutils
Requires(post): libselinux-utils
Requires(post): sed
Obsoletes: %{name} <= 2:1.12.5-13
Obsoletes: docker-selinux <= 2:1.12.4-28
Provides: docker-selinux = %{?epoch:%{epoch}:}%{version}-%{release}
Conflicts: udica < 0.2.6-1
Conflicts: k3s-selinux <= 0.4-1

%description
SELinux policy modules for use with container runtimes.

%prep
%autosetup -Sgit %{name}-%{built_tag_strip}

%build
make

%install
# install policy modules
%_format MODULES $x.pp.bz2
install -d %{buildroot}%{_datadir}/selinux/packages
install -d -p %{buildroot}%{_datadir}/selinux/devel/include/services
install -p -m 644 container.if %{buildroot}%{_datadir}/selinux/devel/include/services
install -m 0644 $MODULES %{buildroot}%{_datadir}/selinux/packages
install -d %{buildroot}/%{_datadir}/containers/selinux
install -m 644 container_contexts %{buildroot}/%{_datadir}/containers/selinux/contexts
install -d %{buildroot}%{_datadir}/udica/templates
install -m 0644 udica-templates/*.cil %{buildroot}%{_datadir}/udica/templates

%check

%pre
%selinux_relabel_pre -s %{selinuxtype}

%post
# Install all modules in a single transaction
if [ $1 -eq 1 ]; then
   %{_sbindir}/setsebool -P -N virt_use_nfs=1 virt_sandbox_use_all_caps=1
fi
%_format MODULES %{_datadir}/selinux/packages/$x.pp.bz2
%{_sbindir}/semodule -n -s %{selinuxtype} -r container 2> /dev/null
%{_sbindir}/semodule -n -s %{selinuxtype} -d docker 2> /dev/null
%{_sbindir}/semodule -n -s %{selinuxtype} -d gear 2> /dev/null
%selinux_modules_install -s %{selinuxtype} $MODULES
. %{_sysconfdir}/selinux/config
sed -e "\|container_file_t|h; \${x;s|container_file_t||;{g;t};a\\" -e "container_file_t" -e "}" -i /etc/selinux/${SELINUXTYPE}/contexts/customizable_types 
matchpathcon -qV %{_sharedstatedir}/containers || restorecon -R %{_sharedstatedir}/containers &> /dev/null || :

%postun
if [ $1 -eq 0 ]; then
   %selinux_modules_uninstall -s %{selinuxtype} %{modulenames} docker
fi

%posttrans
%selinux_relabel_post -s %{selinuxtype}

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files
%doc README.md
%{_datadir}/selinux/*
%dir %{_datadir}/containers/selinux
%{_datadir}/containers/selinux/contexts
%dir %{_datadir}/udica/templates/
%{_datadir}/udica/templates/*
# Currently shipped in selinux-policy-doc
#%%{_datadir}/man/man8/container_selinux.8.gz

%triggerpostun -- container-selinux < 2:2.162.1-3
if %{_sbindir}/selinuxenabled ; then
    echo "Fixing Rootless SELinux labels in homedir"
    %{_sbindir}/restorecon -R /home/*/.local/share/containers/storage/overlay*  2> /dev/null
fi

%changelog
%autochangelog
