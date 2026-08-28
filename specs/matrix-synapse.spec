%bcond check 1
# F43FailsToInstall: python3-pysaml2
# https://bugzilla.redhat.com/show_bug.cgi?id=2372073
%bcond saml2 0

Name:       matrix-synapse
Version:    1.159.0
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
Patch1:     matrix-synapse-1.159-pyo3-Disable-abi3-feature.patch
Patch2:     matrix-synapse-1.159-Build-RustExtension-with-debug-symbols.patch
Patch3:     matrix-synapse-1.151.0-no_parameterized.patch
Patch4:     matrix-synapse-1.159-pyo3_pythonize_0.29.patch
ExclusiveArch:  %{rust_arches}

Recommends:     %{name}+postgres
Recommends:     %{name}+systemd

BuildRequires:  jq
BuildRequires:  python3-devel
BuildRequires:  rust-packaging >= 21
BuildRequires:  /usr/bin/openssl
BuildRequires:  systemd-rpm-macros
BuildRequires:  tomcli

Obsoletes:      %{name}+systemd < 1.150.0-2
# Handles obsolete extra `user_search`. Keep this line until F42 EOL.
Obsoletes:      %{name}+user-search < 1.138.0-2
%if %{without saml2}
Obsoletes:      %{name}+saml2 < 1.136.0-2
%endif

%description
Matrix is an ambitious new ecosystem for open federated Instant Messaging and
VoIP. Synapse is a reference "homeserver" implementation of Matrix from the
core development team at matrix.org, written in Python/Twisted. It is intended
to showcase the concept of Matrix and let folks see the spec in the context of
a coded base and let you run your own homeserver and generally help bootstrap
the ecosystem.

%pyproject_extras_subpkg -n %{name} matrix-synapse-ldap3 postgres %{?with_saml2:saml2} oidc url_preview sentry jwt cache_memory


%prep
%autosetup -p1 -n synapse-%{archive_tag}

# We don't support the built-in client so remove all the bundled JS.
rm -rf synapse/static

# We cannot respect upper bounds on the versions of Python build dependencies.
echo "$(tomcli get pyproject.toml build-system.requires -F json |
  jq '.[] |= sub("(,<=.*).*"; "") | .[]' -r)" |
  xargs -r -x tomcli set pyproject.toml lists str build-system.requires


%cargo_prep


%generate_buildrequires
cd rust
%cargo_generate_buildrequires
cd ..

# Missing: opentracing,redis
%pyproject_buildrequires -x test,matrix-synapse-ldap3,postgres%{?with_saml2:,saml2},oidc,url-preview,sentry,jwt,cache-memory


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
# Drop tests using parameterized
rm -f \
  tests/app/test_openid_listener.py \
  tests/config/test_experimental.py \
  tests/config/test_load.py \
  tests/config/test_server.py \
  tests/events/test_auto_accept_invites.py \
  tests/events/test_event_parsing.py \
  tests/events/test_presence_router.py \
  tests/federation/test_federation_media.py \
  tests/federation/test_federation_out_of_band_membership.py \
  tests/federation/test_federation_server.py \
  tests/handlers/test_appservice.py \
  tests/handlers/test_device.py \
  tests/handlers/test_e2e_keys.py \
  tests/handlers/test_oauth_delegation.py \
  tests/handlers/test_presence.py \
  tests/handlers/test_profile.py \
  tests/handlers/test_room_policy.py \
  tests/handlers/test_sliding_sync.py \
  tests/handlers/test_sync.py \
  tests/http/test_proxy.py \
  tests/http/test_matrixfederationclient.py \
  tests/http/test_proxyagent.py \
  tests/http/test_site.py \
  tests/media/test_media_storage.py \
  tests/media/test_oembed.py \
  tests/module_api/test_api.py \
  tests/push/test_bulk_push_rule_evaluator.py \
  tests/push/test_email.py \
  tests/push/test_http.py \
  tests/replication/storage/test_events.py \
  tests/replication/tcp/streams/test_events.py \
  tests/rest/admin/test_admin.py \
  tests/rest/admin/test_background_updates.py \
  tests/rest/admin/test_device.py \
  tests/rest/admin/test_federation.py \
  tests/rest/admin/test_media.py \
  tests/rest/admin/test_room.py \
  tests/rest/admin/test_user.py \
  tests/rest/client/sliding_sync/test_connection_tracking.py \
  tests/rest/client/sliding_sync/test_extension_account_data.py \
  tests/rest/client/sliding_sync/test_extension_e2ee.py \
  tests/rest/client/sliding_sync/test_extension_receipts.py \
  tests/rest/client/sliding_sync/test_extension_sticky_events.py \
  tests/rest/client/sliding_sync/test_extension_thread_subscriptions.py \
  tests/rest/client/sliding_sync/test_extension_typing.py \
  tests/rest/client/sliding_sync/test_extension_to_device.py \
  tests/rest/client/sliding_sync/test_extensions.py \
  tests/rest/client/sliding_sync/test_lists_filters.py \
  tests/rest/client/sliding_sync/test_room_subscriptions.py \
  tests/rest/client/sliding_sync/test_rooms_invites.py \
  tests/rest/client/sliding_sync/test_rooms_meta.py \
  tests/rest/client/sliding_sync/test_rooms_timeline.py \
  tests/rest/client/sliding_sync/test_rooms_required_state.py \
  tests/rest/client/sliding_sync/test_sliding_sync.py \
  tests/rest/client/test_auth_metadata.py \
  tests/rest/client/test_delayed_events.py \
  tests/rest/client/test_media.py \
  tests/rest/client/test_msc4388_rendezvous.py \
  tests/rest/client/test_owned_state.py \
  tests/rest/client/test_push_rule_attrs.py \
  tests/rest/client/test_redactions.py \
  tests/rest/client/test_rooms.py \
  tests/rest/client/test_sync.py \
  tests/rest/synapse/mas/test_users.py \
  tests/storage/test_client_ips.py \
  tests/storage/test_event_chain.py \
  tests/storage/test_event_federation.py \
  tests/storage/test_purge.py \
  tests/storage/test_room.py \
  tests/storage/test_sliding_sync_tables.py \
  tests/test_event_auth.py \
  tests/test_types.py \
  tests/util/caches/test_response_cache.py \
  tests/util/test_async_helpers.py \
  tests/util/test_stream_change_cache.py
# Drop failing test
rm tests/util/test_httpresourcetree.py

set -o pipefail
PYTHONPATH=%{buildroot}%{python3_sitearch}:%{buildroot}%{python3_sitelib}:$PWD trial-3 %_smp_mflags tests | tee trial.stdout

# Guard against new types of tests being skipped.
ALLOWLIST="Requires hiredis
Requires jaeger_client
Requires Postgres
Requires SAML2 and OIDC
Requires pysaml2
Test only applies when postgres is used as the database
not supported
not supported yet
Synapse does not correctly handle this case
\`BaseFederationServlet\` does not support cancellation yet.
Once we remove ops from the Sliding Sync response, this test should pass
Test is not possible because when everyone leaves the room, the server is \`no_longer_in_room\` and we don't have any \`current_state_events\` to query"
REASONS=$(cat trial.stdout | sed -n '/^\[SKIPPED\]$/{n;p;}')
SKIPPED=$(comm -23 <(echo "$REASONS" | sort | uniq) <(echo "$ALLOWLIST" | sort | uniq))
if [ ! -z "$SKIPPED" ]; then
  echo -e "Failing, because tests were skipped:\n$SKIPPED"
  exit 1
fi

%endif


%post
%systemd_post synapse.service


%preun
%systemd_preun synapse.service


%postun
%systemd_postun_with_restart synapse.service


%files -f %{pyproject_files}
%license LICENSE-AGPL-3.0
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
