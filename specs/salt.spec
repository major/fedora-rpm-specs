## For Python 3 only 

# Release Candidate
%global __rc_ver %{nil}

%global fish_dir %{_datadir}/fish/vendor_functions.d
%global zsh_dir %{_datadir}/zsh/site-functions

# py3_shbang_flags is '-s' and causing issues with pip install.
%global py3_shebang_flags %(echo %py3_shebang_flags | sed s/s//)

Name:    salt
Version: 3007.5
Release: %autorelease
Summary: A parallel remote execution system
Group:   System Environment/Daemons
License: Apache-2.0
URL:     https://saltproject.io/
Source0: %{pypi_source}
Source1: %{name}-proxy@.service
Source2: %{name}-master
Source3: %{name}-syndic
Source4: %{name}-minion
Source5: %{name}-api
Source6: %{name}-master.service
Source7: %{name}-syndic.service
Source8: %{name}-minion.service
Source9: %{name}-api.service
Source10: README.fedora
Source11: %{name}-common.logrotate
Source12: %{name}.bash
Source13: %{name}.fish
Source14: %{name}_common.fish
Source15: %{name}-call.fish
Source16: %{name}-cp.fish
Source17: %{name}-key.fish
Source18: %{name}-master.fish
Source19: %{name}-minion.fish
Source20: %{name}-run.fish
Source21: %{name}-syndic.fish
Source22: %{name}.sysusers

# Fix local contextvars and requirements
Patch0: contextvars.patch
# Fix urlib changes in python >= 3.12.6
# https://github.com/saltstack/salt/issues/66898
Patch2: urllib.patch
BuildArch: noarch

%ifarch %{ix86} x86_64
Requires: dmidecode
%endif

Requires: pciutils
Requires: which
Requires: dnf-utils
Requires: logrotate
Requires: python3-tornado

BuildRequires: systemd-rpm-macros
BuildRequires: python3-devel

%description
Salt is a distributed remote execution system used to execute commands and
query data. It was developed in order to bring the best solutions found in
the world of remote execution together and make them better, faster and more
malleable. Salt accomplishes this via its ability to handle larger loads of
information, and not just dozens, but hundreds or even thousands of individual
servers, handle them quickly and through a simple and manageable interface.


%package    master
Summary:    Management component for salt, a parallel remote execution system
Group:      System Environment/Daemons
Requires:   %{name} = %{version}-%{release}
Requires:   python3-systemd

%description master
The Salt master is the central server to which all minions connect.
Supports Python 3.


%package    minion
Summary:    Client component for Salt, a parallel remote execution system
Group:      System Environment/Daemons
Requires:   %{name} = %{version}-%{release}

%description minion
The Salt minion is the agent component of Salt. It listens for instructions
from the master, runs jobs, and returns results back to the master.
Supports Python 3.


%package    syndic
Summary:    Master-of-master component for Salt, a parallel remote execution system
Group:      System Environment/Daemons
Requires:   %{name}-master = %{version}-%{release}

%description syndic
The Salt syndic is a master daemon which can receive instruction from a
higher-level master, allowing for tiered organization of your Salt
infrastructure.
Supports Python 3.


%package    api
Summary:    REST API for Salt, a parallel remote execution system
Group:      Applications/System
Requires:   %{name}-master = %{version}-%{release}
Requires:   python3-cherrypy >= 3.2.2

%description api
salt-api provides a REST interface to the Salt master.
Supports Python 3.


%package    cloud
Summary:    Cloud provisioner for Salt, a parallel remote execution system
Group:      Applications/System
Requires:   %{name}-master = %{version}-%{release}
Requires:   python3-libcloud

%description cloud
The salt-cloud tool provisions new cloud VMs, installs salt-minion on them, and
adds them to the master's collection of controllable minions.
Supports Python 3.


%package    ssh
Summary:    Agentless SSH-based version of Salt, a parallel remote execution system
Group:      Applications/System
Requires:   %{name} = %{version}-%{release}

%description ssh
The salt-ssh tool can run remote execution functions and states without the use
of an agent (salt-minion) service.
Supports Python 3.


%prep
%autosetup -p1
%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files salt

# Add some directories
install -d -m 0755 %{buildroot}%{_var}/log/%{name}
touch %{buildroot}%{_var}/log/%{name}/minion
touch %{buildroot}%{_var}/log/%{name}/master
install -d -m 0755 %{buildroot}%{_var}/cache/%{name}
install -d -m 0755 %{buildroot}%{_sysconfdir}/%{name}
install -d -m 0755 %{buildroot}%{_sysconfdir}/%{name}/master.d
install -d -m 0755 %{buildroot}%{_sysconfdir}/%{name}/minion.d
install -d -m 0755 %{buildroot}%{_sysconfdir}/%{name}/pki
install -d -m 0755 %{buildroot}%{_sysconfdir}/%{name}/pki/master
install -d -m 0755 %{buildroot}%{_sysconfdir}/%{name}/pki/minion
install -d -m 0700 %{buildroot}%{_sysconfdir}/%{name}/cloud.conf.d
install -d -m 0700 %{buildroot}%{_sysconfdir}/%{name}/cloud.deploy.d
install -d -m 0700 %{buildroot}%{_sysconfdir}/%{name}/cloud.maps.d
install -d -m 0700 %{buildroot}%{_sysconfdir}/%{name}/cloud.profiles.d
install -d -m 0700 %{buildroot}%{_sysconfdir}/%{name}/cloud.providers.d
install -d -m 0755 %{buildroot}%{_sysconfdir}/%{name}/proxy.d

# Add the config files
install -p -m 0640 conf/minion %{buildroot}%{_sysconfdir}/%{name}/minion
install -p -m 0640 conf/master %{buildroot}%{_sysconfdir}/%{name}/master
# Use salt user on nre master installations
sed -i 's/#user: root/user: salt/g' %{buildroot}%{_sysconfdir}/%{name}/master
install -p -m 0600 conf/cloud  %{buildroot}%{_sysconfdir}/%{name}/cloud
install -p -m 0640 conf/roster %{buildroot}%{_sysconfdir}/%{name}/roster
install -p -m 0640 conf/proxy  %{buildroot}%{_sysconfdir}/%{name}/proxy

# Add the unit files
mkdir -p %{buildroot}%{_unitdir}
install -p -m 0644 %{SOURCE6} %{buildroot}%{_unitdir}/
install -p -m 0644 %{SOURCE7} %{buildroot}%{_unitdir}/
install -p -m 0644 %{SOURCE8} %{buildroot}%{_unitdir}/
install -p -m 0644 %{SOURCE9} %{buildroot}%{_unitdir}/
install -p -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/

# Logrotate
install -p %{SOURCE10} .
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d/
install -p -m 0644 %{SOURCE11} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}

# Bash completion
mkdir -p %{buildroot}%{_sysconfdir}/bash_completion.d/
install -p -m 0644 %{SOURCE12} %{buildroot}%{_sysconfdir}/bash_completion.d/%{name}.bash

# Fish completion (TBD remove -v)
mkdir -p %{buildroot}%{fish_dir}
install -p -m 0644  %{SOURCE13} %{buildroot}%{fish_dir}/%{name}.fish
install -p -m 0644  %{SOURCE14} %{buildroot}%{fish_dir}/%{name}_common.fish
install -p -m 0644  %{SOURCE15} %{buildroot}%{fish_dir}/%{name}-call.fish
install -p -m 0644  %{SOURCE16} %{buildroot}%{fish_dir}/%{name}-cp.fish
install -p -m 0644  %{SOURCE17} %{buildroot}%{fish_dir}/%{name}-key.fish
install -p -m 0644  %{SOURCE18} %{buildroot}%{fish_dir}/%{name}-master.fish
install -p -m 0644  %{SOURCE19} %{buildroot}%{fish_dir}/%{name}-minion.fish
install -p -m 0644  %{SOURCE20} %{buildroot}%{fish_dir}/%{name}-run.fish
install -p -m 0644  %{SOURCE21} %{buildroot}%{fish_dir}/%{name}-syndic.fish

# ZSH completion
mkdir -p %{buildroot}%{zsh_dir}
install -p -m 0644 pkg/common/%{name}.zsh %{buildroot}%{zsh_dir}/_%{name}

# Salt user and group
install -p -D -m 0644 %{SOURCE22} %{buildroot}%{_sysusersdir}/salt.conf
mkdir -p %{buildroot}%{_sysconfdir}/%{name}/gpgkeys

%check
%pyproject_check_import -t


%files -f %{pyproject_files}
%license LICENSE
%doc README.fedora
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%config(noreplace) %{_sysconfdir}/bash_completion.d/%{name}.bash
%dir %{_var}/cache/%{name}/
%{_var}/log/%{name}
%{_bindir}/spm
%doc %{_mandir}/man1/spm.1*
%dir %{zsh_dir}
%dir %{_sysconfdir}/%{name}/
%dir %{_sysconfdir}/%{name}/pki/
%{fish_dir}/%{name}*.fish
%{zsh_dir}/_%{name}
%{_bindir}/salt-pip

%files master
%doc %{_mandir}/man7/%{name}.7*
%doc %{_mandir}/man1/%{name}.1*
%doc %{_mandir}/man1/%{name}-cp.1*
%doc %{_mandir}/man1/%{name}-key.1*
%doc %{_mandir}/man1/%{name}-master.1*
%doc %{_mandir}/man1/%{name}-run.1*
%{_bindir}/%{name}
%{_bindir}/%{name}-cp
%{_bindir}/%{name}-key
%{_bindir}/%{name}-master
%{_bindir}/%{name}-run
%{_unitdir}/%{name}-master.service
%{_sysusersdir}/salt.conf
%config(noreplace) %attr(0750, salt, salt) %{_sysconfdir}/%{name}/master
%config(noreplace) %attr(0750, salt, salt) %{_sysconfdir}/%{name}/master.d
%config(noreplace) %attr(0750, salt, salt) %{_sysconfdir}/%{name}/pki/master
%config(noreplace) %attr(0750, salt, salt) %{_sysconfdir}/%{name}/gpgkeys

%files minion
%doc %{_mandir}/man1/%{name}-call.1*
%doc %{_mandir}/man1/%{name}-minion.1*
%doc %{_mandir}/man1/%{name}-proxy.1*
%{_bindir}/%{name}-minion
%{_bindir}/%{name}-call
%{_bindir}/%{name}-proxy
%{_unitdir}/%{name}-minion.service
%{_unitdir}/%{name}-proxy@.service
%config(noreplace) %{_sysconfdir}/%{name}/minion
%config(noreplace) %{_sysconfdir}/%{name}/proxy
%config(noreplace) %{_sysconfdir}/%{name}/minion.d
%config(noreplace) %{_sysconfdir}/%{name}/pki/minion

%files syndic
%doc %{_mandir}/man1/%{name}-syndic.1*
%{_bindir}/%{name}-syndic
%{_unitdir}/%{name}-syndic.service

%files api
%doc %{_mandir}/man1/%{name}-api.1*
%{_bindir}/%{name}-api
%{_unitdir}/%{name}-api.service

%files cloud
%doc %{_mandir}/man1/%{name}-cloud.1*
%{_bindir}/%{name}-cloud
%{_sysconfdir}/%{name}/cloud.conf.d
%{_sysconfdir}/%{name}/cloud.deploy.d
%{_sysconfdir}/%{name}/cloud.maps.d
%{_sysconfdir}/%{name}/cloud.profiles.d
%{_sysconfdir}/%{name}/cloud.providers.d
%config(noreplace) %{_sysconfdir}/%{name}/cloud

%files ssh
%doc %{_mandir}/man1/%{name}-ssh.1*
%{_bindir}/%{name}-ssh
%config(noreplace) %{_sysconfdir}/%{name}/roster


# assumes systemd for RHEL 7 & 8
%preun master
%systemd_preun %{name}-syndic.service

%preun minion
%systemd_preun %{name}-minion.service

%preun api
%systemd_preun %{name}-api.service


%post master
chown salt:salt %{_sysconfdir}/%{name}/gpgkeys -R
%systemd_post %{name}-master.service

%post syndic
%systemd_post %{name}-syndic.service

%post minion
%systemd_post %{name}-minion.service

%post api
%systemd_post %{name}-api.service

%postun master
%systemd_postun_with_restart %{name}-master.service

%postun syndic
%systemd_postun_with_restart %{name}-syndic.service

%postun minion
%systemd_postun_with_restart %{name}-minion.service

%postun api
%systemd_postun_with_restart %{name}-api.service


%changelog
%autochangelog
