%global policy_version 43.1.1

%global with_selinux 1
%global selinuxtype targeted

Name:    keylime
Version: 7.14.1
Release: %autorelease
Summary: Open source TPM software for Bootstrapping and Maintaining Trust

URL:            https://github.com/keylime/keylime
Source0:        https://github.com/keylime/keylime/archive/refs/tags/v%{version}.tar.gz
# The selinux policy for keylime is distributed via this repo: https://github.com/RedHat-SP-Security/keylime-selinux
Source1:        https://github.com/RedHat-SP-Security/%{name}-selinux/archive/v%{policy_version}/keylime-selinux-%{policy_version}.tar.gz
Source2:        %{name}.sysusers
Source3:        %{name}.tmpfiles

Patch: 0001-Fix-timestamp-conversion-to-use-UTC-timezone.patch
Patch: 0002-Fix-efivar-availability-check-in-test_create_mb_poli.patch

# Main program: Apache-2.0
# Icons: MIT
License: Apache-2.0 AND MIT

BuildArch: noarch

BuildRequires: git-core
BuildRequires: openssl
BuildRequires: openssl-devel
BuildRequires: python3-devel
BuildRequires: python3-dbus
BuildRequires: python3-jinja2
BuildRequires: python3-cryptography
BuildRequires: python3-docutils
BuildRequires: python3-gpg
BuildRequires: python3-pip
BuildRequires: python3-pyasn1
BuildRequires: python3-pyasn1-modules
BuildRequires: python3-requests
BuildRequires: python3-tornado
BuildRequires: python3-sqlalchemy
BuildRequires: python3-lark-parser
BuildRequires: python3-psutil
BuildRequires: python3-pyyaml
BuildRequires: python3-jsonschema
BuildRequires: python3-setuptools
BuildRequires: systemd-rpm-macros
BuildRequires: rpm-sign
BuildRequires: createrepo_c
BuildRequires: tpm2-tools

Requires: python3-%{name} = %{version}-%{release}
Requires: %{name}-base = %{version}-%{release}
Requires: %{name}-verifier = %{version}-%{release}
Requires: %{name}-registrar = %{version}-%{release}
Requires: %{name}-tenant = %{version}-%{release}
Requires: %{name}-tools = %{version}-%{release}

# webapp was removed upstream in release 6.4.2.
Obsoletes: %{name}-webapp < 6.4.2

# python agent was removed upstream in release 7.0.0.
Obsoletes: python3-%{name}-agent < 7.0.0

# Agent.
Requires: keylime-agent
Suggests: %{name}-agent-rust

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

Requires(pre): python3-jinja2
Requires: procps-ng
Requires: tpm2-tss
Requires: openssl

%if 0%{?with_selinux}
# This ensures that the *-selinux package and all it’s dependencies are not pulled
# into containers and other systems that do not use SELinux
Recommends:       (%{name}-selinux = %{version}-%{release} if selinux-policy-%{selinuxtype})
%endif

# This generates lines like 'Requires: (efivar-libs if filesystem(aarch64))'.
# We need to transform x86_64 into x86-64, hence the gsub.
%{lua:
  for i in string.gmatch(rpm.expand("%efi"):gsub("_","-"), "%S+") do
    print('Requires: (efivar-libs if filesystem('..i..'))\n')
  end
}

%description base
The base package contains the Keylime default configuration

%package -n python3-%{name}
Summary: The Python Keylime module
License: MIT

# Conflicts with the monolithic versions of the package, before the split.
Conflicts: keylime < 6.3.0-3

Requires: %{name}-base = %{version}-%{release}
%{?python_provide:%python_provide python3-%{name}}

Requires: python3-tornado
Requires: python3-sqlalchemy
Requires: python3-alembic
Requires: python3-cryptography
Requires: python3-pyyaml
Requires: python3-packaging
Requires: python3-requests
Requires: python3-gpg
Requires: python3-lark
Requires: python3-pyasn1
Requires: python3-pyasn1-modules
Requires: python3-psutil
Requires: python3-jsonschema
Requires: python3-typing-extensions
Requires: tpm2-tools

%description -n python3-%{name}
The python3-keylime module implements the functionality used
by Keylime components.

%package verifier
Summary: The Python Keylime Verifier component
License: MIT

# Conflicts with the monolithic versions of the package, before the split.
Conflicts: keylime < 6.3.0-3

Requires: %{name}-base = %{version}-%{release}
Requires: python3-%{name} = %{version}-%{release}

%description verifier
The Keylime Verifier continuously verifies the integrity state
of the machine that the agent is running on.

%package registrar
Summary: The Keylime Registrar component
License: MIT

# Conflicts with the monolithic versions of the package, before the split.
Conflicts: keylime < 6.3.0-3

Requires: %{name}-base = %{version}-%{release}
Requires: python3-%{name} = %{version}-%{release}

%description registrar
The Keylime Registrar is a database of all agents registered
with Keylime and hosts the public keys of the TPM vendors.

%if 0%{?with_selinux}
# SELinux subpackage
%package selinux
Summary:             keylime SELinux policy
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

Requires: %{name}-base = %{version}-%{release}
Requires: python3-%{name} = %{version}-%{release}


%description tenant
The Keylime Tenant can be used to provision a Keylime Agent.

%package tools
Summary: Keylime tools
License: MIT

# Conflicts with the monolithic versions of the package, before the split.
Conflicts: keylime < 6.3.0-3

Requires: %{name}-base = %{version}-%{release}
Requires: python3-%{name} = %{version}-%{release}

%description tools
The keylime tools package includes miscelaneous tools.


%prep
%autosetup -S git -n %{name}-%{version} -a1

%generate_buildrequires
%pyproject_buildrequires

%build
%if 0%{?with_selinux}
# SELinux policy (originally from selinux-policy-contrib)
# this policy module will override the production module

make -f %{_datadir}/selinux/devel/Makefile %{name}.pp
bzip2 -9 %{name}.pp
%endif

%pyproject_wheel

mkdir -p manpages
rst2man --syntax-highlight=none docs/man/keylime_tenant.1.rst manpages/keylime_tenant.1
rst2man --syntax-highlight=none docs/man/keylime-policy.1.rst manpages/keylime-policy.1
rst2man --syntax-highlight=none docs/man/keylime_registrar.8.rst manpages/keylime_registrar.8
rst2man --syntax-highlight=none docs/man/keylime_verifier.8.rst manpages/keylime_verifier.8

%install
%pyproject_install
mkdir -p %{buildroot}/%{_sharedstatedir}/%{name}
mkdir -p --mode=0700 %{buildroot}/%{_rundir}/%{name}

mkdir -p --mode=0700 %{buildroot}/%{_sysconfdir}/%{name}/
for comp in "verifier" "tenant" "registrar" "ca" "logging"; do
    mkdir -p --mode=0700  %{buildroot}/%{_sysconfdir}/%{name}/${comp}.conf.d
    install -Dpm 400 config/${comp}.conf %{buildroot}/%{_sysconfdir}/%{name}
done

# Ship some scripts.
mkdir -p %{buildroot}/%{_datadir}/%{name}/scripts
for s in create_runtime_policy.sh \
         create_mb_refstate \
         ek-openssl-verify \
         keylime_oneshot_attestation; do
    install -Dpm 755 scripts/${s} \
        %{buildroot}/%{_datadir}/%{name}/scripts/${s}
done

# Ship configuration templates.
cp -r ./templates %{buildroot}%{_datadir}/%{name}/templates/

mkdir -p --mode=0755 %{buildroot}/%{_bindir}
install -Dpm 755 ./keylime/cmd/convert_config.py %{buildroot}/%{_bindir}/keylime_upgrade_config

%if 0%{?with_selinux}
install -D -m 0644 %{name}.pp.bz2 %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}/%{name}.pp.bz2
install -D -p -m 0644 keylime-selinux-%{policy_version}/%{name}.if %{buildroot}%{_datadir}/selinux/devel/include/distributed/%{name}.if
%endif

install -Dpm 644 ./services/%{name}_verifier.service \
    %{buildroot}%{_unitdir}/%{name}_verifier.service

install -Dpm 644 ./services/%{name}_registrar.service \
    %{buildroot}%{_unitdir}/%{name}_registrar.service

# TPM cert store is deployed to both /usr/share/keylime/tpm_cert_store
# and then /var/lib/keylime/tpm_cert_store.
for cert_store_dir in %{_datadir} %{_sharedstatedir}; do
    mkdir -p %{buildroot}/"${cert_store_dir}"/%{name}
    cp -r ./tpm_cert_store %{buildroot}/"${cert_store_dir}"/%{name}/
done

# Install the sysusers + tmpfiles.d configuration.
install -p -D -m 0644 %{SOURCE2} %{buildroot}/%{_sysusersdir}/%{name}.conf
install -p -D -m 0644 %{SOURCE3} %{buildroot}/%{_tmpfilesdir}/%{name}.conf

# Install manpages
install -d %{buildroot}%{_mandir}/man1
install -d %{buildroot}%{_mandir}/man8
install -m 644 manpages/keylime_tenant.1 %{buildroot}%{_mandir}/man1/
install -m 644 manpages/keylime-policy.1 %{buildroot}%{_mandir}/man1/
install -m 644 manpages/keylime_registrar.8 %{buildroot}%{_mandir}/man8/
install -m 644 manpages/keylime_verifier.8 %{buildroot}%{_mandir}/man8/

%pyproject_save_files -l %{name}

%check
# Create the default configuration files to be used by the tests.
# Also set the associated environment variables so that the tests
# will actually use them.
CONF_TEMP_DIR="$(mktemp -d)"

%{python3} -m keylime.cmd.convert_config --out "${CONF_TEMP_DIR}" --templates templates/
export KEYLIME_VERIFIER_CONFIG="${CONF_TEMP_DIR}/verifier.conf"
export KEYLIME_TENANT_CONFIG="${CONF_TEMP_DIR}/tenant.conf"
export KEYLIME_REGISTRAR_CONFIG="${CONF_TEMP_DIR}/registrar.conf"
export KEYLIME_CA_CONFIG="${CONF_TEMP_DIR}/ca.conf"
export KEYLIME_LOGGING_CONFIG="${CONF_TEMP_DIR}/logging.conf"

# Run the tests.
%{python3} -m unittest

# Cleanup.
[ "${CONF_TEMP_DIR}" ] && rm -rf "${CONF_TEMP_DIR}"
for e in KEYLIME_VERIFIER_CONFIG \
         KEYLIME_TENANT_CONFIG \
         KEYLIME_REGISTRAR_CONFIG \
         KEYLIME_CA_CONFIG \
         KEYLIME_LOGGING_CONFIG; do
    unset "${e}"
done
exit 0

%pre base
%sysusers_create_compat %{SOURCE2}
exit 0

%post base
for c in ca logging; do
    [ -e /etc/keylime/"${c}.conf" ] || continue
    /usr/bin/keylime_upgrade_config --component "${c}" \
                                    --input /etc/keylime/"${c}.conf" \
                                    >/dev/null
done
exit 0

%posttrans base
if [ -d %{_sysconfdir}/%{name} ]; then
    chmod 500 %{_sysconfdir}/%{name}
    chown -R %{name}:%{name} %{_sysconfdir}/%{name}

    for comp in "verifier" "tenant" "registrar" "ca" "logging"; do
        [ -d %{_sysconfdir}/%{name}/${comp}.conf.d ] && \
            chmod 500 %{_sysconfdir}/%{name}/${comp}.conf.d
    done
fi

[ -d %{_sharedstatedir}/%{name} ] && \
    chown -R %{name} %{_sharedstatedir}/%{name}/

[ -d %{_sharedstatedir}/%{name}/tpm_cert_store ] && \
    chmod 400 %{_sharedstatedir}/%{name}/tpm_cert_store/*.pem && \
    chmod 500 %{_sharedstatedir}/%{name}/tpm_cert_store/

[ -d %{_localstatedir}/log/%{name} ] && \
    chown -R %{name} %{_localstatedir}/log/%{name}/
exit 0

%post verifier
[ -e /etc/keylime/verifier.conf ] && \
    /usr/bin/keylime_upgrade_config --component verifier \
                                    --input /etc/keylime/verifier.conf \
                                    >/dev/null
%systemd_post %{name}_verifier.service
exit 0

%post registrar
[ -e /etc/keylime/registrar.conf ] && \
    /usr/bin/keylime_upgrade_config --component registrar \
                                    --input /etc/keylime/registrar.conf /
                                    >/dev/null
%systemd_post %{name}_registrar.service
exit 0

%post tenant
[ -e /etc/keylime/tenant.conf ] && \
    /usr/bin/keylime_upgrade_config --component tenant \
                                    --input /etc/keylime/tenant.conf \
                                    >/dev/null
exit 0

%preun verifier
%systemd_preun %{name}_verifier.service

%preun registrar
%systemd_preun %{name}_registrar.service

%postun verifier
%systemd_postun_with_restart %{name}_verifier.service

%postun registrar
%systemd_postun_with_restart %{name}_registrar.service

%if 0%{?with_selinux}
# SELinux contexts are saved so that only affected files can be
# relabeled after the policy module installation
%pre selinux
%selinux_relabel_pre -s %{selinuxtype}

%post selinux
%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{selinuxtype}/%{name}.pp.bz2
%selinux_relabel_post -s %{selinuxtype}

if [ "$1" -le "1" ]; then # First install
    # The services need to be restarted for the custom label to be
    # applied in case they where already present in the system,
    # restart fails silently in case they where not.
    for svc in registrar verifier; do
        [ -f "%{_unitdir}/%{name}_${svc}".service ] && \
            %systemd_postun_with_restart "%{name}_${svc}".service
    done
fi
exit 0

%postun selinux
if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} %{name}
    %selinux_relabel_post -s %{selinuxtype}
fi
%endif

%files verifier
%license LICENSE
%attr(500,%{name},%{name}) %dir %{_sysconfdir}/%{name}/verifier.conf.d
%config(noreplace) %verify(not md5 size mode mtime) %attr(400,%{name},%{name}) %{_sysconfdir}/%{name}/verifier.conf
%{_bindir}/%{name}_verifier
%{_bindir}/%{name}_ca
%{_unitdir}/keylime_verifier.service
%{_mandir}/man8/keylime_verifier.8*

%files registrar
%license LICENSE
%attr(500,%{name},%{name}) %dir %{_sysconfdir}/%{name}/registrar.conf.d
%config(noreplace) %verify(not md5 size mode mtime) %attr(400,%{name},%{name}) %{_sysconfdir}/%{name}/registrar.conf
%{_bindir}/%{name}_registrar
%{_unitdir}/keylime_registrar.service
%{_mandir}/man8/keylime_registrar.8*

%if 0%{?with_selinux}
%files selinux
%{_datadir}/selinux/packages/%{selinuxtype}/%{name}.pp.*
%{_datadir}/selinux/devel/include/distributed/%{name}.if
%ghost %verify(not md5 size mode mtime) %{_sharedstatedir}/selinux/%{selinuxtype}/active/modules/200/%{name}
%endif

%files tenant
%license LICENSE
%attr(500,%{name},%{name}) %dir %{_sysconfdir}/%{name}/tenant.conf.d
%config(noreplace) %verify(not md5 size mode mtime) %attr(400,%{name},%{name}) %{_sysconfdir}/%{name}/tenant.conf
%{_bindir}/%{name}_tenant
%{_mandir}/man1/keylime_tenant.1*

%files -n python3-%{name} -f %{pyproject_files}
%license LICENSE
%{_datadir}/%{name}/scripts/create_mb_refstate
%{_bindir}/keylime_attest
%{_bindir}/keylime_convert_runtime_policy
%{_bindir}/keylime_create_policy
%{_bindir}/keylime_sign_runtime_policy
%{_bindir}/keylime-policy
%{_mandir}/man1/keylime-policy.1*


%files tools
%license LICENSE
%{_bindir}/%{name}_userdata_encrypt

%files base
%license LICENSE
%doc README.md
%attr(500,%{name},%{name}) %dir %{_sysconfdir}/%{name}
%attr(500,%{name},%{name}) %dir %{_sysconfdir}/%{name}/{ca,logging}.conf.d
%config(noreplace) %verify(not md5 size mode mtime) %attr(400,%{name},%{name}) %{_sysconfdir}/%{name}/ca.conf
%config(noreplace) %verify(not md5 size mode mtime) %attr(400,%{name},%{name}) %{_sysconfdir}/%{name}/logging.conf
%attr(700,%{name},%{name}) %dir %{_rundir}/%{name}
%attr(700,%{name},%{name}) %dir %{_sharedstatedir}/%{name}
%attr(755,root,root) %dir %{_datadir}/%{name}/tpm_cert_store
%attr(644,root,root) %{_datadir}/%{name}/tpm_cert_store/*.pem
%attr(500,%{name},%{name}) %dir %{_sharedstatedir}/%{name}/tpm_cert_store
%attr(400,%{name},%{name}) %{_sharedstatedir}/%{name}/tpm_cert_store/*.pem
%{_tmpfilesdir}/%{name}.conf
%{_sysusersdir}/%{name}.conf
%{_datadir}/%{name}/scripts/create_runtime_policy.sh
%{_datadir}/%{name}/scripts/ek-openssl-verify
%{_datadir}/%{name}/scripts/keylime_oneshot_attestation
%{_datadir}/%{name}/templates
%{_bindir}/keylime_upgrade_config

%files
%license LICENSE

%changelog
%autochangelog
