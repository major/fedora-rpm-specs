%global srcname keylime
%global policy_version 1.0.0

# Package is actually noarch, but it has an optional dependency that is
# arch-specific.
%global debug_package %{nil}
%global with_selinux 1
%global selinuxtype targeted

Name:    keylime
Version: 6.4.3
Release: %autorelease
Summary: Open source TPM software for Bootstrapping and Maintaining Trust

URL:            https://github.com/keylime/keylime
Source0:        https://github.com/keylime/keylime/archive/refs/tags/v%{version}.tar.gz
Source1:        %{srcname}.sysusers
# The selinux policy for keylime is distributed via this repo: https://github.com/RedHat-SP-Security/keylime-selinux
Source2:        https://github.com/RedHat-SP-Security/%{name}-selinux/archive/v%{policy_version}/keylime-selinux-%{policy_version}.tar.gz

Patch: 0001-Proper-exception-handling-in-tornado_requests.patch

# Main program: BSD
# Icons: MIT
License: ASL 2.0 and MIT

BuildRequires: git-core
BuildRequires: swig
BuildRequires: openssl-devel
BuildRequires: python3-devel
BuildRequires: python3-dbus
BuildRequires: python3-setuptools
BuildRequires: systemd-rpm-macros

Requires: python3-%{srcname} = %{version}-%{release}
Requires: %{srcname}-base = %{version}-%{release}
Requires: %{srcname}-verifier = %{version}-%{release}
Requires: %{srcname}-registrar = %{version}-%{release}
Requires: %{srcname}-tenant = %{version}-%{release}
Requires: %{srcname}-tools = %{version}-%{release}

# webapp was removed upstream in release 6.4.2.
Obsoletes: %{srcname}-webapp < 6.4.2

# Agent.
Requires: keylime-agent
Suggests: python3-%{srcname}-agent

# Conflicts with the monolithic versions of the package, before the split.
Conflicts: keylime < 6.3.0-3

%{?python_enable_dependency_generator}
%description
Keylime is a TPM based highly scalable remote boot attestation
and runtime integrity measurement solution.

%package base
Summary: The base package contains the default configuration
License: MIT

# Conflicts with the monolithic versions of the package, before the split.
Conflicts: keylime < 6.3.0-3

Requires(pre): shadow-utils
Requires: procps-ng
Requires: tpm2-tss

%if 0%{?with_selinux}
# This ensures that the *-selinux package and all it’s dependencies are not pulled
# into containers and other systems that do not use SELinux
Recommends:       (%{srcname}-selinux if selinux-policy-%{selinuxtype})
%endif

%ifarch %efi
Requires: efivar-libs
%endif


%description base
The base package contains the Keylime default configuration

%package -n python3-%{srcname}
Summary: The Python Keylime module
License: MIT

# Conflicts with the monolithic versions of the package, before the split.
Conflicts: keylime < 6.3.0-3

Requires: %{srcname}-base = %{version}-%{release}
%{?python_provide:%python_provide python3-%{srcname}}

Requires: python3-tornado
Requires: python3-sqlalchemy
Requires: python3-alembic
Requires: python3-cryptography
Requires: python3-pyyaml
Requires: python3-packaging
Requires: python3-requests
Requires: python3-gpg
Requires: python3-lark-parser
Requires: python3-pyasn1
Requires: python3-pyasn1-modules
Requires: tpm2-tools

%description -n python3-%{srcname}
The python3-keylime module implements the functionality used
by Keylime components.

%package verifier
Summary: The Python Keylime Verifier component
License: MIT

# Conflicts with the monolithic versions of the package, before the split.
Conflicts: keylime < 6.3.0-3

Requires: %{srcname}-base = %{version}-%{release}
Requires: python3-%{srcname} = %{version}-%{release}

%description verifier
The Keylime Verifier continuously verifies the integrity state
of the machine that the agent is running on.

%package registrar
Summary: The Keylime Registrar component
License: MIT

# Conflicts with the monolithic versions of the package, before the split.
Conflicts: keylime < 6.3.0-3

Requires: %{srcname}-base = %{version}-%{release}
Requires: python3-%{srcname} = %{version}-%{release}

%description registrar
The Keylime Registrar is a database of all agents registered
with Keylime and hosts the public keys of the TPM vendors.

%package -n python3-%{srcname}-agent
Summary: The Python Keylime Agent
License: MIT

# Conflicts with the monolithic versions of the package, before the split.
Conflicts: keylime < 6.3.0-3

Requires: %{srcname}-base = %{version}-%{release}
Requires: python3-%{srcname} = %{version}-%{release}
Requires: python3-psutil
Requires: python3-zmq

# Virtual Provides to support swapping between Python and Rust implementation.
Provides:  keylime-agent
Conflicts: keylime-agent

%description -n python3-%{srcname}-agent
The Keylime Agent is deployed to the remote machine that is to be
measured or provisioned with secrets stored within an encrypted
payload released once trust is established.

%if 0%{?with_selinux}
# SELinux subpackage
%package selinux
Summary:             keylime SELinux policy
BuildArch:           noarch
Requires:            selinux-policy-%{selinuxtype}
Requires(post):      selinux-policy-%{selinuxtype}
BuildRequires:       selinux-policy-devel
%{?selinux_requires}

%description selinux
Custom SELinux policy module
%endif

%package tenant
Summary: The Python Keylime Tenant
License: MIT

# Conflicts with the monolithic versions of the package, before the split.
Conflicts: keylime < 6.3.0-3

Requires: %{srcname}-base = %{version}-%{release}
Requires: python3-%{srcname} = %{version}-%{release}


%description tenant
The Keylime Tenant can be used to provision a Keylime Agent.

%package tools
Summary: Keylime tools
License: MIT

# Conflicts with the monolithic versions of the package, before the split.
Conflicts: keylime < 6.3.0-3

Requires: %{srcname}-base = %{version}-%{release}
Requires: python3-%{srcname} = %{version}-%{release}

%description tools
The keylime tools package includes miscelaneous tools.


%prep
%autosetup -S git -n %{srcname}-%{version} -a2

%if 0%{?with_selinux}
# SELinux policy (originally from selinux-policy-contrib)
# this policy module will override the production module

make -f %{_datadir}/selinux/devel/Makefile %{srcname}.pp
bzip2 -9 %{srcname}.pp
%endif

%build
%py3_build

%install
%py3_install
mkdir -p %{buildroot}/%{_sharedstatedir}/%{srcname}
mkdir -p --mode=0700 %{buildroot}/%{_rundir}/%{srcname}
mkdir -p --mode=0700 %{buildroot}/%{_localstatedir}/log/%{srcname}

# Setting up the agent to use keylime user/group.
sed -e 's/^run_as.*/run_as = %{srcname}:%{srcname}/g' -i %{srcname}.conf

# rhbz#2114485 - using sha256 for tpm_hash_alg.
sed -e 's/^tpm_hash_alg[[:space:]]*=.*/tpm_hash_alg = sha256/g' -i %{srcname}.conf

%if 0%{?with_selinux}
install -D -m 0644 %{srcname}.pp.bz2 %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}/%{srcname}.pp.bz2
install -D -p -m 0644 keylime-selinux-%{policy_version}/%{srcname}.if %{buildroot}%{_datadir}/selinux/devel/include/distributed/%{srcname}.if
%endif

install -Dpm 600 %{srcname}.conf \
    %{buildroot}%{_sysconfdir}/%{srcname}.conf

install -Dpm 644 ./services/%{srcname}_agent.service \
    %{buildroot}%{_unitdir}/%{srcname}_agent.service

install -Dpm 644 ./services/%{srcname}_agent_secure.mount \
    %{buildroot}%{_unitdir}/%{srcname}_agent_secure.mount

install -Dpm 644 ./services/%{srcname}_verifier.service \
    %{buildroot}%{_unitdir}/%{srcname}_verifier.service

install -Dpm 644 ./services/%{srcname}_registrar.service \
    %{buildroot}%{_unitdir}/%{srcname}_registrar.service

cp -r ./tpm_cert_store %{buildroot}%{_sharedstatedir}/keylime/

install -p -d %{buildroot}/%{_tmpfilesdir}
cat > %{buildroot}/%{_tmpfilesdir}/%{srcname}.conf << EOF
d %{_rundir}/%{srcname} 0700 %{srcname} %{srcname} -
EOF

install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/%{srcname}.conf

%pre base
%sysusers_create_compat %{SOURCE1}
exit 0

%posttrans base
[ -f %{_sysconfdir}/%{srcname}.conf ] && \
    chmod 600 %{_sysconfdir}/%{srcname}.conf && \
    chown %{srcname} %{_sysconfdir}/%{srcname}.conf
[ -d %{_sharedstatedir}/%{srcname} ] && \
    chown -R %{srcname} %{_sharedstatedir}/%{srcname}/
[ -d %{_localstatedir}/log/%{srcname} ] && \
    chown -R %{srcname} %{_localstatedir}/log/%{srcname}/
exit 0

%post verifier
%systemd_post %{srcname}_verifier.service

%post registrar
%systemd_post %{srcname}_registrar.service

%post -n python3-%{srcname}-agent
%systemd_post %{srcname}_agent.service

%if 0%{?with_selinux}
# SELinux contexts are saved so that only affected files can be
# relabeled after the policy module installation
%pre selinux
%selinux_relabel_pre -s %{selinuxtype}

%post selinux
%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{selinuxtype}/%{srcname}.pp.bz2
%selinux_relabel_post -s %{selinuxtype}

if [ "$1" -le "1" ]; then # First install
    # The services need to be restarted for the custom label to be
    # applied in case they where already present in the system,
    # restart fails silently in case they where not.
    for svc in agent registrar verifier; do
        [ -f "%{_unitdir}/%{srcname}_${svc}".service ] && \
            %systemd_postun_with_restart "%{srcname}_${svc}".service
    done
fi
exit 0

%postun selinux
if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} %{srcname}
    %selinux_relabel_post -s %{selinuxtype}
fi
%endif

%preun verifier
%systemd_preun %{srcname}_verifier.service

%preun registrar
%systemd_preun %{srcname}_registrar.service

%preun -n python3-%{srcname}-agent
%systemd_preun %{srcname}_agent.service

%postun verifier
%systemd_postun_with_restart %{srcname}_verifier.service

%postun registrar
%systemd_postun_with_restart %{srcname}_registrar.service

%postun -n python3-%{srcname}-agent
%systemd_postun_with_restart %{srcname}_agent.service

%files verifier
%license LICENSE
%{_bindir}/%{srcname}_verifier
%{_bindir}/%{srcname}_ca
%{_bindir}/%{srcname}_migrations_apply
%{_unitdir}/keylime_verifier.service

%files registrar
%license LICENSE
%{_bindir}/%{srcname}_registrar
%{_unitdir}/keylime_registrar.service

%files -n python3-%{srcname}-agent
%license LICENSE
%{_bindir}/%{srcname}_agent
%{_unitdir}/%{srcname}_agent.service
%{_unitdir}/%{srcname}_agent_secure.mount
%{_bindir}/%{srcname}_ima_emulator

%if 0%{?with_selinux}
%files selinux
%{_datadir}/selinux/packages/%{selinuxtype}/%{srcname}.pp.*
%{_datadir}/selinux/devel/include/distributed/%{srcname}.if
%ghost %verify(not md5 size mode mtime) %{_sharedstatedir}/selinux/%{selinuxtype}/active/modules/200/%{srcname}
%endif

%files tenant
%license LICENSE
%{_bindir}/%{srcname}_tenant

%files -n python3-%{srcname}
%license LICENSE
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}

%files tools
%license LICENSE
%{_bindir}/%{srcname}_userdata_encrypt

%files base
%license LICENSE
%doc README.md
%config(noreplace) %attr(600,%{srcname},%{srcname}) %{_sysconfdir}/%{srcname}.conf
%attr(700,%{srcname},%{srcname}) %dir %{_rundir}/%{srcname}
%attr(700,%{srcname},%{srcname}) %dir %{_localstatedir}/log/%{srcname}
%attr(700,%{srcname},%{srcname}) %{_sharedstatedir}/%{srcname}
%{_tmpfilesdir}/%{srcname}.conf
%{_sysusersdir}/%{srcname}.conf

%files
%license LICENSE

%changelog
%autochangelog
