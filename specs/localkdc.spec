%bcond selinux 1
%global selinux_variants targeted
%global selinuxtype targeted
%global selinux_package_dir %{_datadir}/selinux/packages

# The localkdc sources themselves are MIT licensed.  The LICENSE.dependencies
# contains the full license breakdown of the bundled Rust dependencies.
#
# %%{cargo_license_summary} output, for comparison on future rebuilds:
# Apache-2.0 OR BSL-1.0
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# BSD-2-Clause
# BSD-2-Clause OR Apache-2.0 OR MIT
# LGPL-2.1-or-later
# MIT
# MIT OR Apache-2.0
# Unlicense OR MIT

%define localkdc_license %{shrink:
    MIT AND
    (Apache-2.0 OR BSL-1.0) AND
    (Apache-2.0 OR MIT) AND
    (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
    BSD-2-Clause AND
    (BSD-2-Clause OR Apache-2.0 OR MIT) AND
    LGPL-2.1-or-later AND
    (MIT OR Apache-2.0) AND
    (Unlicense OR MIT)
}

Name:           localkdc
Version:        0.2.1
Release:        %autorelease
Summary:        A local KDC based on MIT Kerberos

License:        %{localkdc_license}
URL:            https://gitlab.com/kirmes/localkdc
Source:         https://gitlab.com/kirmes/localkdc/-/archive/%{version}/%{name}-%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  bats
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  go-md2man
BuildRequires:  krb5-devel
BuildRequires:  make
BuildRequires:  pam-devel
BuildRequires:  systemd-rpm-macros

Requires:       bash
Requires:       gawk
Requires:       hostname
Requires:       krb5-server
Requires:       krb5-workstation
Requires:       certmonger
Requires:       pam
%if %{with selinux}
Requires:       (%{name}-selinux = %{version}-%{release} if selinux-policy-%{selinuxtype})
%endif


%description
localkdc is a local authentication hub that leverages Kerberos for managing
authentication and authorization on individual machines, whether standalone or
domain-enrolled. It reuses expertise accumulated through decades of work on
Samba and FreeIPA.

The KDC communicates over a Unix domain socket rather than network ports,
allowing systemd to activate it on demand. User principals are discovered
dynamically from the operating system via systemd's userdb, eliminating separate
database maintenance. Credential verification is delegated to PAM, so any local
system user can authenticate via Kerberos using their existing system
password. There is no directory service or manual enrollment required.


%if %{with selinux}
%package selinux
Summary:        SELinux support for %{name}
BuildArch:      noarch
# This subpackage does not include anything derived from the
# statically-linked Rust dependencies.
License:        MIT

BuildRequires:  selinux-policy-devel

Requires:       selinux-policy-%{selinuxtype}
Requires(post): selinux-policy-%{selinuxtype}

%description selinux
SELinux support for %{name}
#endif with selinux
%endif


%prep
%autosetup -p1
%cargo_prep
pushd src >/dev/null
%cargo_prep
popd >/dev/null

%generate_buildrequires
pushd src >/dev/null
%cargo_generate_buildrequires -a -t
popd >/dev/null


%build
%cmake \
    -DCMAKE_INSTALL_RUNSTATEDIR=%{_rundir} \
    -DCMAKE_INSTALL_LOCALSTATEDIR=%{_localstatedir}
%cmake_build

LDEPS="$(pwd)/LICENSE.dependencies"
pushd src >/dev/null
%{cargo_license_summary}
%{cargo_license} > "${LDEPS}"
popd >/dev/null

pushd selinux >/dev/null
for SELINUXVARIANT in %{selinux_variants}; do
    %make_build -f /usr/share/selinux/devel/Makefile %{name}.pp
    mv -v %{name}.pp %{name}-${SELINUXVARIANT}.pp
done
popd >/dev/null


%install
%cmake_install

install -d -m 0755 %{buildroot}%{_sysconfdir}/localkdc
install -d -m 0755 %{buildroot}%{_localstatedir}/kerberos/localkdc

%if %{with selinux}
# Install the SELinux module(s).
rm -fv selinux-files.txt

for SELINUXVARIANT in %{selinux_variants}; do
    install -d -m 755 %{buildroot}%{selinux_package_dir}/${SELINUXVARIANT}
    bzip2 selinux/%{name}-${SELINUXVARIANT}.pp
    MODULE_PATH=%{selinux_package_dir}/${SELINUXVARIANT}/%{name}.pp.bz2
    install -p -m 644 selinux/%{name}-${SELINUXVARIANT}.pp.bz2 \
      %{buildroot}${MODULE_PATH}

    echo ${MODULE_PATH} >> selinux-files.txt
done
#endif with selinux
%endif


%check
# tests/integration/ requires root and live system daemons (systemd-userdbd,
# krb5kdc, ...) and is not run here.
bats tests/unit/


%post
%systemd_post localkdc.service localkdc.socket localkdc-pam-auth.socket

%preun
%systemd_preun localkdc.service localkdc.socket localkdc-pam-auth.socket

%postun
%systemd_postun localkdc.service localkdc.socket localkdc-pam-auth.socket

%if %{with selinux}
%pre selinux
for SELINUXVARIANT in %{selinux_variants}; do
    %selinux_relabel_pre -s ${SELINUXVARIANT}
done

%post selinux
for SELINUXVARIANT in %{selinux_variants}; do
    MODULE_PATH=%{selinux_package_dir}/${SELINUXVARIANT}/%{name}.pp.bz2
    %selinux_modules_install -s ${SELINUXVARIANT} ${MODULE_PATH}
done

%postun selinux
if [ $1 -eq 0 ]; then
    for SELINUXVARIANT in %{selinux_variants}; do
        %selinux_modules_uninstall -s ${SELINUXVARIANT} %{name}
    done
fi

%posttrans selinux
for SELINUXVARIANT in %{selinux_variants}; do
    %selinux_relabel_post -s ${SELINUXVARIANT}
done
#endif with selinux
%endif


%files
%license LICENSE LICENSE.dependencies
%doc README.md
%dir %{_sysconfdir}/localkdc
%config(noreplace) %{_sysconfdir}/pam.d/localkdc-otp
%{_bindir}/lkdcctl
%dir %{_libexecdir}/localkdc
%{_libexecdir}/localkdc/localkdc-pam-auth
%dir %{_libdir}/krb5/plugins/audit
%{_libdir}/krb5/plugins/audit/audit_json.so
%dir %{_libdir}/krb5/plugins/kadm5_hook
%{_libdir}/krb5/plugins/kadm5_hook/kadm5_chpass.so
%{_libdir}/krb5/plugins/kdb/kdb_userdb.so
%dir %{_datadir}/localkdc
%{_datadir}/localkdc/templates
%{_unitdir}/localkdc.service
%{_unitdir}/localkdc.socket
%{_unitdir}/localkdc-pam-auth@.service
%{_unitdir}/localkdc-pam-auth.socket
%dir %{_localstatedir}/kerberos/localkdc
%{_mandir}/man7/localkdc.7*
%{_mandir}/man8/lkdcctl.8*

%if %{with selinux}
%files selinux -f selinux-files.txt
%license LICENSE
%endif


%changelog
%autochangelog
