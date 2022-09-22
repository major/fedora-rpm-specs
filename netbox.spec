Name:           netbox
Version:        2.11.10
Release:        %autorelease
Summary:        IP address management (IPAM) and data center infrastructure management (DCIM)

License:        ASL 2.0 and MIT and OFL
URL:            https://github.com/netbox-community/netbox/
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        netbox.service
Source2:        netbox-rq.service
Source3:        https://github.com/netbox-community/netbox-docker/raw/release/docker/configuration.docker.py
Source4:        https://github.com/netbox-community/netbox-docker/raw/release/docker/ldap_config.docker.py
Source5:        ldap_config.example.py
# Non-upstreamable
Patch0001:      0001-Use-var-lib-netbox-for-the-static-and-media-files.patch
Patch0002:      0002-Default-docs-root-to-the-same-folder-as-the-netbox.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  systemd-rpm-macros
Requires:       /usr/bin/gunicorn
Requires(pre):  shadow-utils
# base_requirements.txt
Requires:       python3dist(django) >= 3.1
Requires:       python3dist(django-cacheops)
Requires:       python3dist(django-cors-headers)
Requires:       python3dist(django-debug-toolbar)
Requires:       python3dist(django-filter)
Requires:       python3dist(django-mptt)
Requires:       python3dist(django-pglocks)
Requires:       python3dist(django-prometheus)
Requires:       python3dist(django-rq)
Requires:       python3dist(django-tables2)
Requires:       python3dist(django-taggit)
Requires:       python3dist(django-timezone-field)
Requires:       python3dist(djangorestframework)
Requires:       python3dist(drf-yasg[validation])
Requires:       python3dist(gunicorn)
Requires:       python3dist(jinja2)
Requires:       python3dist(markdown)
Requires:       python3dist(netaddr)
Requires:       python3dist(pillow)
# originally: psycopg2
Requires:       python3dist(psycopg2)
# originally: pycryptodome
Requires:       python3dist(pycryptodomex)
Requires:       python3dist(pyyaml)
Requires:       python3dist(redis)
Requires:       python3dist(svgwrite)
Requires:       python3dist(tablib)
Recommends:     python3dist(django-storages)
Suggests:       python3dist(django-auth-ldap)
# netbox/project-static/bootstrap-*-dist/
# License(s): MIT
Provides:       bundled(js-bootstrap) = 3.4.1
# netbox/project-static/clipboard.js/
# License(s): MIT
Provides:       bundled(js-clipboard) = 2.0.6
# netbox/project-static/flatpickr-*/
# License(s): MIT
Provides:       bundled(js-flatpickr) = 4.6.3
# netbox/project-static/materialdesignicons-*/
# License(s): ASL 2.0 and MIT
Provides:       bundled(materialdesign-webfont) = 5.8.55
# netbox/project-static/jquery/
# License(s): MIT
Provides:       bundled(js-jquery) = 3.5.1
# netbox/project-static/jquery-ui-*/
# License(s): MIT
Provides:       bundled(js-jquery-ui) = 1.12.1
# netbox/project-static/select2-*/
# License(s): MIT
Provides:       bundled(js-select2) = 4.0.13
# netbox/project-static/select2-bootstrap-*/
# License(s): MIT
Provides:       bundled(js-select2-bootstrap-theme) = 0.1.0~beta10

%description
NetBox is an IP address management (IPAM)
and data center infrastructure management (DCIM) tool.
Initially conceived by the network engineering team at DigitalOcean,
NetBox was developed specifically to address the needs of network
and infrastructure engineers. It is intended to function
as a domain-specific source of truth for network operations.

%prep
%autosetup -p1
find -type f -name '*.py' \
  -exec sed -i -e 's/from Crypto\./from Cryptodome./' '{}' + \
  -exec pathfix.py -pni '%python3 %{py3_shbang_opts}' '{}' + \
  %{nil}
cat << EOF >> contrib/gunicorn.py

# Configure Gunicorn to cope with prometheus client
# (https://github.com/prometheus/client_python#multiprocess-mode-gunicorn)
from prometheus_client import multiprocess

def child_exit(server, worker):
    multiprocess.mark_process_dead(worker.pid)
EOF

%install
install -Dpm0644 -t %{buildroot}%{_unitdir} %{S:1}
install -Dpm0644 -t %{buildroot}%{_unitdir} %{S:2}
mkdir -p %{buildroot}%{_sysconfdir}/netbox/{config,reports,scripts}
mkdir -p %{buildroot}%{_sysconfdir}/netbox/config/ldap
install -Dpm0640 netbox/netbox/configuration.example.py %{buildroot}%{_sysconfdir}/netbox/config/configuration.py
install -Dpm0640 %{S:5} %{buildroot}%{_sysconfdir}/netbox/config/ldap/ldap_config.py
install -Dpm0644 contrib/gunicorn.py %{buildroot}%{_sysconfdir}/netbox/gunicorn_config.py

mkdir -p %{buildroot}{%{_datadir},%{_sysconfdir}/netbox}
cp -a netbox %{buildroot}%{_datadir}
install -Dpm0644 %{S:3} %{buildroot}%{_datadir}/netbox/netbox/configuration.py
install -Dpm0644 %{S:4} %{buildroot}%{_datadir}/netbox/netbox/ldap_config.py
rm -v %{buildroot}%{_datadir}/netbox/netbox/configuration.*.py
mkdir -p %{buildroot}%{_sharedstatedir}/netbox/static
rm -v %{buildroot}%{_datadir}/netbox/media/*/.gitignore
cp -a %{buildroot}%{_datadir}/netbox/media %{buildroot}%{_sharedstatedir}/netbox/
rm -r %{buildroot}%{_datadir}/netbox/media

# "Help" buttons
mkdir -p %{buildroot}%{_datadir}/netbox/docs
cp -a docs/models %{buildroot}%{_datadir}/netbox/docs
mkdir -p %{buildroot}%{_datadir}/netbox/docs/media
cp -a docs/media/models %{buildroot}%{_datadir}/netbox/docs/media

%py_byte_compile %python3 %{buildroot}%{_datadir}/netbox

%pre
getent group netbox >/dev/null || groupadd -r netbox
getent passwd netbox >/dev/null || \
    useradd -r -g netbox -d %{_datadir}/netbox -s /bin/bash \
    -c "NetBox user" netbox
exit 0

%post
%systemd_post netbox.service netbox-rq.service

%preun
%systemd_preun netbox.service netbox-rq.service

%postun
%systemd_postun_with_restart netbox.service netbox-rq.service

%files
%license LICENSE.txt NOTICE
%doc README.md CHANGELOG.md
%{_datadir}/netbox/
%{_unitdir}/netbox.service
%{_unitdir}/netbox-rq.service
%defattr(-,netbox,netbox)
%dir %{_sysconfdir}/netbox/
%dir %{_sysconfdir}/netbox/{config,reports,scripts}/
%config(noreplace) %{_sysconfdir}/netbox/config/configuration.py
%dir %{_sysconfdir}/netbox/config/ldap/
%config(noreplace) %{_sysconfdir}/netbox/config/ldap/ldap_config.py
%config(noreplace) %{_sysconfdir}/netbox/gunicorn_config.py
%{_sharedstatedir}/netbox/

%changelog
%autochangelog
