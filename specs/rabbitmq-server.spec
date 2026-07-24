# Check here - https://www.rabbitmq.com/docs/which-erlang
%global erlang_minver 27
# We want to install into /usr/lib, even on 64-bit platforms
%global _rabbit_libdir %{_exec_prefix}/lib/rabbitmq
# Technically, we're noarch; but Elixir we're using is not.
%global debug_package %{nil}


Name: rabbitmq-server
Version: 4.3.3
Release: %autorelease
Summary: The RabbitMQ server
License: MPL-2.0
Source0: https://github.com/rabbitmq/rabbitmq-server/releases/download/v%{version}/%{name}_%{version}.orig.tar.xz
Source1: https://github.com/rabbitmq/rabbitmq-server/releases/download/v%{version}/%{name}_%{version}.orig.tar.xz.asc
Source2: https://github.com/rabbitmq/signing-keys/releases/download/2.0/rabbitmq-release-signing-key.asc
# curl -O https://raw.githubusercontent.com/lemenkov/rabbitmq-server/cdfc661/packaging/RPMS/Fedora/rabbitmq-server.logrotate
Source3: rabbitmq-server.logrotate
# curl -O https://raw.githubusercontent.com/rabbitmq/rabbitmq-server-release/rabbitmq_v3_6_16/packaging/RPMS/Fedora/rabbitmq-server.tmpfiles
Source5: rabbitmq-server.tmpfiles
Source6: rabbitmq-server-cuttlefish
Patch: rabbitmq-server-0001-Use-default-EPMD-socket.patch
Patch: rabbitmq-server-0002-Use-proto_dist-from-command-line.patch
Patch: rabbitmq-server-0003-force-python3.patch
Patch: rabbitmq-server-0004-Greatly-simplified-wrapper-script-which-works-proper.patch
Patch: rabbitmq-server-0005-rabbit_plugins-demote-duplicate-plugin-warnings-from.patch

URL: https://www.rabbitmq.com/
BuildRequires: elixir
BuildRequires: erlang >= %{erlang_minver}
# for %%gpgverify
BuildRequires: gnupg2
BuildRequires: hostname
BuildRequires: libxslt
BuildRequires: make
BuildRequires: python3
BuildRequires: rsync
BuildRequires: systemd
BuildRequires: xmlto
BuildRequires: zip
Requires: erlang-eldap%{?_isa} >= %{erlang_minver}
Requires: erlang-erts%{?_isa} >= %{erlang_minver}
Requires: erlang-kernel%{?_isa} >= %{erlang_minver}
Requires: erlang-mnesia%{?_isa} >= %{erlang_minver}
Requires: erlang-os_mon%{?_isa} >= %{erlang_minver}
Requires: erlang-public_key%{?_isa} >= %{erlang_minver}
Requires: erlang-sasl%{?_isa} >= %{erlang_minver}
Requires: erlang-ssl%{?_isa} >= %{erlang_minver}
Requires: erlang-stdlib%{?_isa} >= %{erlang_minver}
Requires: erlang-syntax_tools%{?_isa} >= %{erlang_minver}
Requires: erlang-tools%{?_isa} >= %{erlang_minver}
Requires: erlang-xmerl%{?_isa} >= %{erlang_minver}
Requires: logrotate
Requires: util-linux
# Users and groups
Requires(pre): systemd
Requires(post): systemd
Requires(preun): systemd

%description
RabbitMQ is an implementation of AMQP, the emerging standard for high
performance enterprise messaging. The RabbitMQ server is a robust and
scalable implementation of an AMQP broker.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

# Create a sysusers.d config file
cat >rabbitmq-server.sysusers.conf <<EOF
u rabbitmq - 'RabbitMQ messaging server' %{_localstatedir}/lib/rabbitmq -
EOF


%build
make PROJECT_VERSION=%{version} ESCRIPT_ZIP="zip -9 -X" V=1 # Doesn't support %%{?_smp_mflags}


%install
make install \
	PROJECT_VERSION=%{version} \
	ESCRIPT_ZIP="zip -9 -X" \
	DESTDIR=%{buildroot} \
	PREFIX=%{_prefix} \
	RMQ_ROOTDIR=%{_rabbit_libdir}

make install-man \
	PROJECT_VERSION=%{version} \
	ESCRIPT_ZIP="zip -9 -X" \
	DESTDIR=%{buildroot} \
	PREFIX=%{_prefix} \
	RMQ_ROOTDIR=%{_rabbit_libdir}

mkdir -p %{buildroot}%{_localstatedir}/lib/rabbitmq/mnesia
mkdir -p %{buildroot}%{_localstatedir}/log/rabbitmq

#Copy all necessary lib files etc.
install -p -D -m 0644 ./deps/rabbit/docs/rabbitmq-server.service.example %{buildroot}%{_unitdir}/%{name}.service
install -p -D -m 0755 ./scripts/rabbitmq-script-wrapper %{buildroot}%{_sbindir}/rabbitmqctl
install -p -D -m 0755 ./scripts/rabbitmq-script-wrapper %{buildroot}%{_sbindir}/rabbitmq-server
install -p -D -m 0755 ./scripts/rabbitmq-script-wrapper %{buildroot}%{_sbindir}/rabbitmq-plugins
install -p -D -m 0755 ./scripts/rabbitmq-script-wrapper %{buildroot}%{_sbindir}/rabbitmq-diagnostics

# Make necessary symlinks
mkdir -p %{buildroot}%{_rabbit_libdir}/bin
for app in $(basename -a %{buildroot}%{_rabbit_libdir}/lib/rabbitmq_server-%{version}/sbin/*); do
       ln -s ../lib/rabbitmq_server-%{version}/sbin/${app} %{buildroot}%{_rabbit_libdir}/bin/${app}
done

ln -s ./lib/rabbitmq_server-%{version}/plugins %{buildroot}%{_rabbit_libdir}/plugins

install -p -D -m 0755 %{S:3} %{buildroot}%{_rabbit_libdir}/bin/cuttlefish

install -p -D -m 0755 scripts/rabbitmq-server.ocf %{buildroot}%{_exec_prefix}/lib/ocf/resource.d/rabbitmq/rabbitmq-server

install -p -D -m 0644 %{S:3} %{buildroot}%{_sysconfdir}/logrotate.d/rabbitmq-server

install -p -D -m 0644 ./deps/rabbit/docs/rabbitmq.conf.example %{buildroot}%{_sysconfdir}/rabbitmq/rabbitmq.conf

install -d %{buildroot}%{_localstatedir}/run/rabbitmq
install -p -D -m 0644 %{SOURCE5} %{buildroot}%{_prefix}/lib/tmpfiles.d/%{name}.conf
install -m0644 -D rabbitmq-server.sysusers.conf %{buildroot}%{_sysusersdir}/rabbitmq-server.conf


%check
#make check


%post
%systemd_post %{name}.service


%preun
# We do not remove /var/log and /var/lib directories
# Leave rabbitmq user and group
%systemd_preun %{name}.service

# Clean out plugin activation state, both on uninstall and upgrade
rm -rf %{_localstatedir}/lib/rabbitmq/plugins
rm -f %{_rabbit_libdir}/lib/rabbitmq_server-%{version}/ebin/rabbit.{rel,script,boot}


%postun
%systemd_postun_with_restart %{name}.service


%files
%dir %attr(0755, rabbitmq, rabbitmq) %{_sysconfdir}/rabbitmq
%config(noreplace) %attr(0644, rabbitmq, rabbitmq) %{_sysconfdir}/rabbitmq/rabbitmq.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/rabbitmq-server
%{_sbindir}/rabbitmqctl
%{_sbindir}/rabbitmq-server
%{_sbindir}/rabbitmq-plugins
%{_sbindir}/rabbitmq-diagnostics
%{_rabbit_libdir}/
%{_unitdir}/%{name}.service
# FIXME this should add dependency on "/usr/lib/ocf/resource.d/" owner
%dir /usr/lib/ocf/resource.d/rabbitmq/
/usr/lib/ocf/resource.d/rabbitmq/rabbitmq-server
%{_tmpfilesdir}/%{name}.conf
%dir %attr(0750, rabbitmq, rabbitmq) %{_localstatedir}/lib/rabbitmq
%dir %attr(0750, rabbitmq, rabbitmq) %{_localstatedir}/log/rabbitmq
%dir %attr(0755, rabbitmq, rabbitmq) %{_localstatedir}/run/rabbitmq
%license LICENSE LICENSE-*
%{_mandir}/man5/rabbitmq-env.conf.5*
%{_mandir}/man8/rabbitmq-diagnostics.8*
%{_mandir}/man8/rabbitmq-plugins.8*
%{_mandir}/man8/rabbitmq-server.8*
%{_mandir}/man8/rabbitmq-service.8*
%{_mandir}/man8/rabbitmq-streams.8*
%{_mandir}/man8/rabbitmq-queues.8*
%{_mandir}/man8/rabbitmq-upgrade.8*
%{_mandir}/man8/rabbitmqctl.8*
%{_sysusersdir}/rabbitmq-server.conf


%changelog
%autochangelog
