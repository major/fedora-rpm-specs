%bcond check 1

%global gomodulesmode GO111MODULE=on
%global gotestflags %{gocompilerflags} -short

Name:           caddy
Version:        2.11.4
Release:        %autorelease
ExclusiveArch:  %{golang_arches_future}
Summary:        Web server with automatic HTTPS
License:        Apache-2.0 AND BSD-2-Clause AND BSD-2-Clause-Views AND BSD-3-Clause AND CC0-1.0 AND ISC AND MIT AND MPL-2.0 AND OFL-1.1
URL:            https://caddyserver.com
Source0:        https://github.com/caddyserver/caddy/archive/v%{version}/caddy-%{version}.tar.gz
Source1:        caddy-%{version}-vendor.tar.bz2
Source2:        go-vendor-tools.toml

# based on reference files upstream
# https://github.com/caddyserver/dist
Source10:       Caddyfile
Source20:       caddy.service
Source21:       caddy-api.service
Source30:       poweredby-white.png
Source31:       poweredby-black.png

# downstream only patch to disable commands that can alter the binary
Patch1:         0001-Disable-commands-that-can-alter-the-binary.patch

BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
BuildRequires:  askalono-cli

BuildRequires:  systemd-rpm-macros
%{?systemd_ordering}

Requires:       system-logos-httpd
Provides:       webserver


%description
Fast and extensible multi-platform HTTP/1-2-3 web server with automatic HTTPS.


%prep
%autosetup -p 1 -a 1


%build
export GO_LDFLAGS="-X github.com/caddyserver/caddy/v2.CustomVersion=v%{version}"
%gobuild -o bin/caddy ./cmd/caddy


%install
# licenses
%go_vendor_license_install -c %{S:2}

# command
install -D -p -m 0755 -t %{buildroot}%{_bindir} bin/caddy

# man page
./bin/caddy manpage --directory %{buildroot}%{_mandir}/man8

# config
install -D -p -m 0644 -t %{buildroot}%{_sysconfdir}/caddy %{S:10}
install -d -m 0755 %{buildroot}%{_sysconfdir}/caddy/Caddyfile.d

# systemd units
install -D -p -m 0644 -t %{buildroot}%{_unitdir} %{S:20} %{S:21}

# sysusers
install -d -m 0755 %{buildroot}%{_sysusersdir}
cat > %{buildroot}%{_sysusersdir}/caddy.conf << EOF
u caddy - "Caddy web server" /var/lib/caddy
EOF

# data directory
install -d -m 0750 %{buildroot}%{_sharedstatedir}/caddy

# welcome page
%if %{defined fedora}
install -D -p -m 0644 %{S:30} %{buildroot}%{_datadir}/caddy/poweredby.png
ln -s ../fedora-testpage/index.html %{buildroot}%{_datadir}/caddy/index.html
%else
install -D -p -m 0644 %{S:31} %{buildroot}%{_datadir}/caddy/poweredby.png
ln -s ../testpage/index.html %{buildroot}%{_datadir}/caddy/index.html
%endif
install -d -m 0755 %{buildroot}%{_datadir}/caddy/icons
ln -s ../../pixmaps/poweredby.png %{buildroot}%{_datadir}/caddy/icons/poweredby.png
%if %{defined rhel} && 0%{?rhel} >= 9
ln -s ../pixmaps/system-noindex-logo.png %{buildroot}%{_datadir}/caddy/system_noindex_logo.png
%endif

# shell completions
install -d -m 0755 %{buildroot}%{bash_completions_dir}
./bin/caddy completion bash > %{buildroot}%{bash_completions_dir}/caddy
install -d -m 0755 %{buildroot}%{zsh_completions_dir}
./bin/caddy completion zsh > %{buildroot}%{zsh_completions_dir}/_caddy
install -d -m 0755 %{buildroot}%{fish_completions_dir}
./bin/caddy completion fish > %{buildroot}%{fish_completions_dir}/caddy.fish


%check
# ensure that the version was embedded correctly
[[ "$(./bin/caddy version)" == "v%{version}" ]] || exit 1

# license validation
%go_vendor_license_check -c %{S:2}

# upstream tests
%if %{with check}
%gocheck2
%endif


%post
%systemd_post caddy.service caddy-api.service

if [ -x /usr/sbin/getsebool ]; then
    # connect to ACME endpoint to request certificates
    setsebool -P httpd_can_network_connect on
fi
if [ -x /usr/sbin/semanage -a -x /usr/sbin/restorecon ]; then
    # file contexts
    semanage fcontext --add --type httpd_exec_t        '%{_bindir}/caddy'               2> /dev/null || :
    semanage fcontext --add --type httpd_sys_content_t '%{_datadir}/caddy(/.*)?'        2> /dev/null || :
    semanage fcontext --add --type httpd_config_t      '%{_sysconfdir}/caddy(/.*)?'     2> /dev/null || :
    semanage fcontext --add --type httpd_var_lib_t     '%{_sharedstatedir}/caddy(/.*)?' 2> /dev/null || :
    restorecon -r %{_bindir}/caddy %{_datadir}/caddy %{_sysconfdir}/caddy %{_sharedstatedir}/caddy || :
fi
if [ -x /usr/sbin/semanage ]; then
    # QUIC
    semanage port --add --type http_port_t --proto udp 80   2> /dev/null || :
    semanage port --add --type http_port_t --proto udp 443  2> /dev/null || :
    # admin endpoint
    semanage port --add --type http_port_t --proto tcp 2019 2> /dev/null || :
fi


%preun
%systemd_preun caddy.service caddy-api.service


%postun
%systemd_postun_with_restart caddy.service caddy-api.service

if [ $1 -eq 0 ]; then
    if [ -x /usr/sbin/getsebool ]; then
        # connect to ACME endpoint to request certificates
        setsebool -P httpd_can_network_connect off
    fi
    if [ -x /usr/sbin/semanage ]; then
        # file contexts
        semanage fcontext --delete --type httpd_exec_t        '%{_bindir}/caddy'               2> /dev/null || :
        semanage fcontext --delete --type httpd_sys_content_t '%{_datadir}/caddy(/.*)?'        2> /dev/null || :
        semanage fcontext --delete --type httpd_config_t      '%{_sysconfdir}/caddy(/.*)?'     2> /dev/null || :
        semanage fcontext --delete --type httpd_var_lib_t     '%{_sharedstatedir}/caddy(/.*)?' 2> /dev/null || :
        # QUIC
        semanage port     --delete --type http_port_t --proto udp 80   2> /dev/null || :
        semanage port     --delete --type http_port_t --proto udp 443  2> /dev/null || :
        # admin endpoint
        semanage port     --delete --type http_port_t --proto tcp 2019 2> /dev/null || :
    fi
fi


%files -f %{go_vendor_license_filelist}
%{_bindir}/caddy
%{_mandir}/man8/caddy*.8*
%{_datadir}/caddy
%{_unitdir}/caddy.service
%{_unitdir}/caddy-api.service
%{_sysusersdir}/caddy.conf
%dir %{_sysconfdir}/caddy
%config(noreplace) %{_sysconfdir}/caddy/Caddyfile
%dir %{_sysconfdir}/caddy/Caddyfile.d
%attr(0750,caddy,caddy) %dir %{_sharedstatedir}/caddy
%{bash_completions_dir}/caddy
%{zsh_completions_dir}/_caddy
%{fish_completions_dir}/caddy.fish


%changelog
%autochangelog
