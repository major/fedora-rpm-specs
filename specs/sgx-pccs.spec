
# Change after running pccs-nodejs-bundler
%global node_modules_date 20260318

%global with_sysusers_scripts 0
%if 0%{?rhel} == 9
%global with_sysusers_scripts 1
%endif


Name: sgx-pccs
Version: 1.25
Release: %autorelease
# The PCCS service was previously bundled in linux-sgx RPMs,
# whose versioning follows the SGX versions.
#
# With the split of PCCS into its own package, it has a
# distinct version, which follows the DCAP versions which
# are sadly numerically older than SGX versions.
#
# Thus we're forced to take an epoch to preserve the upgrade
# path
Epoch: 1
URL: https://github.com/intel/confidential-computing.tee.dcap.pccs
Summary: SGX Provisioning Certificate Caching Service

# Check pccs-<version>-nodejs-licenses.txt after re-running
# the deps bundler for any changes that are needed here
License: %{shrink:
  %dnl node_modules
  0BSD AND

  %dnl node_modules
  Apache-2.0 AND

  %dnl node_modules
  BlueOak-1.0.0 AND

  %dnl node_modules
  BSD-2-Clause AND

  %dnl sgx-pccs, node_modules
  BSD-3-Clause AND

  %dnl node_modules
  ISC AND

  %dnl node_modules
  MIT AND

  %dnl node_modules
  Unlicense AND

  %dnl node_modules
  WTFPL
}

# While Intel SGX is an x86_64 only feature, in theory
# it is possible to run pccs/pccsadmin on any platform
# as they're merely playing a supporting role not directly
# required local SGX hardware, so let the RPM build
# everywhere nodejs is capable of.
ExclusiveArch: %{nodejs_arches}
ExcludeArch: %{ix86}

Source0: https://github.com/intel/confidential-computing.tee.dcap.pccs/archive/refs/tags/DCAP_%{version}.tar.gz#/pccs-%{version}.tar.gz
Source1: pccs.sysusers.conf
Source2: pccs.service
# RPM build doesn't run this, but we want it in the src.rpm
# as record of what was used to create Source4
Source3: pccs-nodejs-bundler
# Pre-created using Source3
Source4: pccs-%{version}-%{node_modules_date}-node-modules.tar.xz

# Maintained in https://github.com/berrange/confidential-computing.tee.dcap.pccs/tree/dist-git-<version>
#
Patch: 0001-service-sanitize-paths-to-all-resources.patch
Patch: 0002-pccsadmin-remove-leftover-debugging-print-args-state.patch
Patch: 0003-pccsadmin-make-keyring-module-optional.patch
Patch: 0004-pccsadmin-ignore-errors-trying-to-clear-the-keyring.patch
Patch: 0005-service-update-sqlite3-to-6.0.0-series-override-seri.patch


%if 0%{?fedora} >= 44 || 0%{?rhel} >= 11
Requires: nodejs24
%else
Requires: nodejs
%endif

# XXX nodejs-packaging needs fixing to auto-add 'Requires: nodejs(abi) == XX'
# then this can be reduced to only 'BuildRequires: nodejs, /usr/bin/node'
# See also https://src.fedoraproject.org/rpms/linux-sgx/pull-request/6
# Match this version with later 'Requires: nodejsXX' against sgx-pccs
%if 0%{?fedora} >= 44 || 0%{?rhel} >= 11
BuildRequires: nodejs24-devel, /usr/bin/node, /usr/bin/npm
%else
# npm in RHEL 9, nodejs-npm in RHEL 10 and F<44
BuildRequires: nodejs-devel, /usr/bin/node, /usr/bin/npm
%endif
BuildRequires: nodejs-packaging
BuildRequires: python3-rpm-macros
BuildRequires: systemd-rpm-macros
BuildRequires: util-linux-core
BuildRequires: git-core
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: sqlite-devel
BuildRequires: chrpath

%if %{with_sysusers_scripts}
%{sysusers_requires_compat}
%endif

%description
SGX Provisioning Certificate Caching Service

%package admin
Summary: SGX Provisioning Certificate Caching Service Admin Tool
%if 0%{?fedora}
Requires: python3-keyring
%endif
Requires: python3-requests
Requires: python3-urllib3
Requires: python3-packaging
# pccs admin tool can be used against a remote pccs
# so don't force a hard dep
Recommends: sgx-pccs = %{epoch}:%{version}-%{release}
BuildArch: noarch

%description admin
SGX Provisioning Certificate Caching Service Admin Tool

%prep
%autosetup -S git_am -n confidential-computing.tee.dcap.pccs-DCAP_%{version}

tar Jxvf %{SOURCE4}

%build

(
  cd service

  # Force NPM sqlite3 to link against the distro library
  # instead of either downloading pre-built, or static
  # linking its own copy
  sed -i -e 's|"sqlite%":"internal"|"sqlite%":"/usr"|' node_modules/sqlite3/binding.gyp
  # Fix multi-lib path
  sed -i -e "s|/lib|/%{_lib}|" node_modules/sqlite3/binding.gyp
  # Force debug symbols
  sed -i -e 's|"install":.*|"install": "node-gyp rebuild --debug",|' node_modules/sqlite3/package.json

  # The {SOURCE3} bundler script  uses '--ignore-scripts'
  # when creating the bundle on the packager's local dev
  # machine. We must re-run install now to finish job in
  # RPM build context
  for pkg in node_modules/*
  do
    (
      cd $pkg
      # Get verbose output from node-gyp for sqlite3 build
      export V=1
      npm run install --if-present
    )
  done

  # Keep brp-mangle-shebangs happy
  find node_modules -type f -exec chmod -x {} \;

  chrpath --delete node_modules/sqlite3/build/Debug/node_sqlite3.node
)

%install

%__install -d %{buildroot}%{_bindir}
%__install -d %{buildroot}%{_datadir}/pccsadmin
%__install -d %{buildroot}%{_sharedstatedir}/pccs
%__install -d %{buildroot}%{_localstatedir}/log/pccs
%__install -d %{buildroot}%{_sysconfdir}/pccs
%__install -d %{buildroot}%{_sysconfdir}/pccs/ssl
%__install -d %{buildroot}%{_sysusersdir}
%__install -d %{buildroot}%{_unitdir}
%__install -d %{buildroot}%{nodejs_sitearch}/pccs

(
    cd service
    mv config/default.json \
        %{buildroot}%{_sysconfdir}/pccs/default.json

    # Pull together all license files relevant to the code that is shipped
    # Err on the side of pulling in much too much, rather than miss something
    for f in $(find node_modules -type f \
                   -iname 'licence*' -o \
                   -iname 'license*' -o \
                   -iname 'copying*')
    do
      d=$(dirname $f | sed -e 's,node_modules/,,')
      mkdir -p ../node_modules/$d
      mv $f ../node_modules/$d
    done

    # Install all the local package code and deps as
    # pccs offers no 'makefile' to do this for us
    cp -a pccs_server.js %{buildroot}%{nodejs_sitearch}/pccs/pccs_server.js
    cp -a package.json %{buildroot}%{nodejs_sitearch}/pccs/package.json
    for d in constants \
             controllers \
             dao \
             middleware \
             migrations \
             node_modules \
             pckCertSelection \
             pcs_client \
             routes \
             services \
             utils \
             x509
    do
        cp -a $d %{buildroot}%{nodejs_sitearch}/pccs/$d
    done

    # So find-debuginfo processes it
    chmod +x %{buildroot}%{nodejs_sitearch}/pccs/node_modules/sqlite3/build/Debug/node_sqlite3.node

)

# Many modules are duplicated across the deps chain. Other simple
# files end up having common content across modules. Rather than
# try to flatten the node_modules deps, hardlinking kills the
# duplication.
hardlink -t %{buildroot}%{nodejs_sitearch}/pccs/node_modules


# Can't install pccs_server.js directly in _bindir because
# it assumes its js modules are in the same directory
# so create a trivial wrapper
cat >>%{buildroot}%{_bindir}/pccs <<EOF
#!/usr/bin/sh

exec node %{nodejs_sitearch}/pccs/pccs_server.js
EOF
chmod +x %{buildroot}%{_bindir}/pccs


%__install -m 0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/pccs.conf
%__install -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}/pccs.service


%__install -m 0755 PccsAdminTool/pccsadmin.py %{buildroot}%{_datadir}/pccsadmin/pccsadmin.py
cp -a PccsAdminTool/lib %{buildroot}%{_datadir}/pccsadmin/lib

# Can't install pccsadmin.py directly in _bindir because
# it assumes its py modules are in the same directory
# so create a trivial wrapper
cat > %{buildroot}%{_bindir}/pccsadmin <<EOF
#!/usr/bin/sh

exec python3 %{_datadir}/pccsadmin/pccsadmin.py "\$@"
EOF
chmod +x %{buildroot}%{_bindir}/pccsadmin

%py3_shebang_fix %{buildroot}/%{_datadir}/pccsadmin/pccsadmin.py

for file in $(find %{buildroot}%{nodejs_sitearch}/pccs -type f -exec grep -l '^#!.*/usr/bin/env node' {} \;)
do
  sed -i -e 's,^#!.*/usr/bin/env node,#!%{__nodejs},' $file
  chmod +x $file
done


%if %{with_sysusers_scripts}
%pre -n sgx-pccs
%sysusers_create_compat %{SOURCE1}
%endif

%post -n sgx-pccs
%systemd_post pccs.service

%preun -n sgx-pccs
%systemd_preun pccs.service

%postun -n sgx-pccs
%systemd_postun_with_restart pccs.service

%files
%license License.txt node_modules/
%{_bindir}/pccs
%dir %{_sysconfdir}/pccs
%attr(0750,root,pccs) %dir %{_sysconfdir}/pccs/ssl
%config(noreplace) %{_sysconfdir}/pccs/default.json
%{_unitdir}/pccs.service
%{nodejs_sitearch}/pccs
%{_sysusersdir}/pccs.conf
%attr(0700,pccs,pccs) %dir %{_sharedstatedir}/pccs
%attr(0700,pccs,pccs) %dir %{_localstatedir}/log/pccs

%files admin
%license License.txt
%{_bindir}/pccsadmin
%{_datadir}/pccsadmin

%changelog
%autochangelog
