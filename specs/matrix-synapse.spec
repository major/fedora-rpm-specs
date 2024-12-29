%bcond_without check

Name:       matrix-synapse
Version:    1.121.1
Release:    %autorelease
Summary:    A Matrix reference homeserver written in Python using Twisted
License:    AGPL-3.0-or-later
URL:        https://github.com/element-hq/synapse

%global upstream_tag v%{lua:return(rpm.expand("%{version}"):gsub("~",""))}
%global archive_tag %{lua:return(rpm.expand("%{version}"):gsub("~",""))}

Source0:    %{url}/archive/%{upstream_tag}/synapse-%{version}.tar.gz
Source1:    synapse.sysconfig
Source2:    synapse.service
Source3:    matrix-synapse.sysusers
Patch1:     0001-pyo3-Disable-abi3-feature.patch
Patch2:     0002-Build-RustExtension-with-debug-symbols.patch
ExclusiveArch:  %{rust_arches}

Recommends:     %{name}+postgres
Recommends:     %{name}+systemd
Recommends:     %{name}+user-search

BuildRequires:  python3-devel
BuildRequires:  rust-packaging >= 21
BuildRequires:  /usr/bin/openssl
BuildRequires:  systemd-rpm-macros

%description
Matrix is an ambitious new ecosystem for open federated Instant Messaging and
VoIP. Synapse is a reference "homeserver" implementation of Matrix from the
core development team at matrix.org, written in Python/Twisted. It is intended
to showcase the concept of Matrix and let folks see the spec in the context of
a coded base and let you run your own homeserver and generally help bootstrap
the ecosystem.

%pyproject_extras_subpkg -n %{name} matrix-synapse-ldap3 postgres saml2 oidc systemd url_preview sentry jwt cache_memory user-search


%prep
%autosetup -p1 -n synapse-%{archive_tag}

# We don't support the built-in client so remove all the bundled JS.
rm -rf synapse/static

%cargo_prep


%generate_buildrequires
cd rust
%cargo_generate_buildrequires
cd ..

# Missing: opentracing,redis
%pyproject_buildrequires -x test,matrix-synapse-ldap3,postgres,saml2,oidc,systemd,url-preview,sentry,jwt,cache-memory,user-search


%build
%pyproject_wheel


%install
%pyproject_install
%py3_shebang_fix %{buildroot}%{python3_sitearch}/synapse/_scripts
%pyproject_save_files synapse

install -p -D -T -m 0644 contrib/systemd/log_config.yaml %{buildroot}%{_sysconfdir}/synapse/log_config.yaml
install -p -D -T -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/sysconfig/synapse
install -p -D -T -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}/synapse.service
install -p -d -m 755 %{buildroot}%{_sharedstatedir}/synapse
install -p -D -m 0644 %{SOURCE3} %{buildroot}%{_sysusersdir}/%{name}.conf


%if %{with check}
%check
set -o pipefail
PYTHONPATH=%{buildroot}%{python3_sitearch}:%{buildroot}%{python3_sitelib}:$PWD trial-3 %_smp_mflags tests | tee trial.stdout

# Guard against new types of tests being skipped.
WHITELIST="Requires hiredis
Requires jaeger_client
Requires Postgres
Test only applies when postgres is used as the database
not supported
not supported yet
Synapse does not correctly handle this case
\`BaseFederationServlet\` does not support cancellation yet.
Once we remove ops from the Sliding Sync response, this test should pass
Test is not possible because when everyone leaves the room, the server is \`no_longer_in_room\` and we don't have any \`current_state_events\` to query"
REASONS=$(cat trial.stdout | sed -n '/^\[SKIPPED\]$/{n;p;}')
SKIPPED=$(comm -23 <(echo "$REASONS" | sort | uniq) <(echo "$WHITELIST" | sort | uniq))
if [ ! -z "$SKIPPED" ]; then
  echo -e "Failing, because tests were skipped:\n$SKIPPED"
  exit 1
fi

%endif


%pre
%sysusers_create_compat %{SOURCE3}


%post
%systemd_post synapse.service


%preun
%systemd_preun synapse.service


%postun
%systemd_postun_with_restart synapse.service


%files -f %{pyproject_files}
%license LICENSE
%doc *.rst
%config(noreplace) %{_sysconfdir}/sysconfig/synapse
%{_bindir}/export_signing_key
%{_bindir}/generate_config
%{_bindir}/generate_log_config
%{_bindir}/generate_signing_key
%{_bindir}/hash_password
%{_bindir}/register_new_matrix_user
%{_bindir}/synapse_homeserver
%{_bindir}/synapse_port_db
%{_bindir}/synapse_review_recent_signups
%{_bindir}/synapse_worker
%{_bindir}/synctl
%{_bindir}/update_synapse_database
%{_unitdir}/synapse.service
%attr(755,synapse,synapse) %dir %{_sharedstatedir}/synapse
%attr(755,synapse,synapse) %dir %{_sysconfdir}/synapse
%attr(644,synapse,synapse) %config(noreplace) %{_sysconfdir}/synapse/log_config.yaml
%{_sysusersdir}/%{name}.conf


%changelog
%autochangelog
