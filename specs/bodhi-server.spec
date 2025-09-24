%global pypi_name bodhi-server
%global src_name bodhi_server
%global pypi_version 25.5.1

Name:           %{pypi_name}
Version:        %{pypi_version}
Release:        %autorelease
Summary:        Bodhi server

License:        GPL-2.0-or-later
URL:            https://github.com/fedora-infra/bodhi
Source:         %{pypi_source bodhi_server}
# Upstream commits 7fab645 and cbd503a
Patch:          %{name}-bump-zstandard-dep.patch

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  pyproject-rpm-macros
BuildRequires:  systemd-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-pytest-mock
BuildRequires:  python3-sphinx
BuildRequires:  python3-responses
BuildRequires:  python3-webtest
BuildRequires:  python3-librepo
BuildRequires:  python3-createrepo_c
BuildRequires:  createrepo_c
BuildRequires:  skopeo
BuildRequires:  dnf
BuildRequires:  python3dist(libdnf5)

Requires: bodhi-client >= 8.3.0
Requires: python3-bodhi-messages >= 8.1.1
Requires: fedora-messaging
Requires: git
Requires: httpd
Requires: intltool
Requires: python3-librepo
Requires: python3-mod_wsgi

%{?sysusers_requires_compat}

Provides:  bundled(chrissimpkins-hack-fonts)
Provides:  bundled(fedora-bootstrap) = 5.3.3-0
Provides:  bundled(fontawesome-fonts-web) = 4.6.3
Provides:  bundled(js-chart) = 3.8.0
Provides:  bundled(js-jquery) = 3.6.0
Provides:  bundled(js-messenger) = 1.4.1
Provides:  bundled(js-moment) = 2.8.3
Provides:  bundled(js-selectize) = 0.15.2
Provides:  bundled(js-typeahead.js) = 1.1.1
Provides:  bundled(open-sans-fonts)

%py_provides python3-bodhi-server

%description
Bodhi is a modular framework that facilitates the process of publishing
updates for a software distribution.


%package -n bodhi-composer
Summary: Bodhi composer backend

Requires: %{py3_dist jinja2}
Requires: bodhi-server == %{version}-%{release}
Requires: pungi >= 4.1.20
Requires: python3-createrepo_c >= 1.0.0
Requires: skopeo
Requires: python3dist(libdnf5)

%description -n bodhi-composer
The Bodhi composer is the component that publishes Bodhi artifacts to
repositories.


%prep
%autosetup -p1 -n %{src_name}-%{pypi_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires

# https://docs.fedoraproject.org/en-US/packaging-guidelines/UsersAndGroups/#_dynamic_allocation
cat > %{name}.conf << EOF
#Type Name   ID  GECOS           Home directory         Shell
u     bodhi  -   "Bodhi Server"  %{_datadir}/%{name}    /sbin/nologin
EOF


%build
%pyproject_wheel
make %{?_smp_mflags} -C docs man

%install
%pyproject_install

%{__mkdir_p} %{buildroot}/var/lib/bodhi
%{__mkdir_p} %{buildroot}/var/cache/bodhi
%{__mkdir_p} %{buildroot}%{_sysconfdir}/httpd/conf.d
%{__mkdir_p} %{buildroot}%{_sysconfdir}/bodhi
%{__mkdir_p} %{buildroot}%{_datadir}/bodhi
%{__mkdir_p} -m 0755 %{buildroot}/%{_localstatedir}/log/bodhi

install -m 644 apache/bodhi.conf %{buildroot}%{_sysconfdir}/httpd/conf.d/bodhi.conf
sed -i -s 's/BODHI_VERSION/%{version}/g' %{buildroot}%{_sysconfdir}/httpd/conf.d/bodhi.conf
sed -i -s 's/python3.7/python%{python3_version}/g' %{buildroot}%{_sysconfdir}/httpd/conf.d/bodhi.conf
install -m 640 production.ini %{buildroot}%{_sysconfdir}/bodhi/production.ini
install -m 640 alembic.ini %{buildroot}%{_sysconfdir}/bodhi/alembic.ini
install apache/bodhi.wsgi %{buildroot}%{_datadir}/bodhi/bodhi.wsgi
install -d %{buildroot}%{_mandir}/man1
install -pm0644 docs/_build/*.1 %{buildroot}%{_mandir}/man1/

install -p -D -m 0644 %{name}.conf %{buildroot}%{_sysusersdir}/%{name}.conf

%check
# For some reason the pytest fixture responsible to set the testing
# config file url doesn't work in Koji
export BODHI_CONFIG=$(pwd)/tests/testing.ini

# sanity_checks tests rely on dnf command, but system's dnf cache is not accessible
# within koji
%{pytest} -v -k 'not sanity_check and not TestSanityCheckRepodata'

%pre -n %{pypi_name}
%sysusers_create_compat %{name}.conf


%files -n %{pypi_name}
%doc README.rst bodhi/server/migrations/README.rst bodhi/server/static/vendor/fedora-bootstrap/README.rst
%{_bindir}/bodhi-approve-testing
%{_bindir}/bodhi-check-policies
%{_bindir}/bodhi-clean-old-composes
%{_bindir}/bodhi-expire-overrides
%{_bindir}/bodhi-push
%{_bindir}/bodhi-sar
%{_bindir}/bodhi-shell
%{_bindir}/bodhi-untag-branched
%{_bindir}/initialize_bodhi_db
%config(noreplace) %{_sysconfdir}/bodhi/alembic.ini
%config(noreplace) %{_sysconfdir}/httpd/conf.d/bodhi.conf
%dir %{_sysconfdir}/bodhi/
%{python3_sitelib}/bodhi
%{python3_sitelib}/bodhi_server-%{pypi_version}.dist-info
%{_mandir}/man1/bodhi-*.1*
%{_mandir}/man1/initialize_bodhi_db.1*
%{_sysusersdir}/%{name}.conf
%attr(-,bodhi,root) %{_datadir}/bodhi
%attr(-,bodhi,bodhi) %config(noreplace) %{_sysconfdir}/bodhi/*
%attr(0775,bodhi,bodhi) %{_localstatedir}/cache/bodhi
# These excluded files are in the bodhi-composer package so don't include them here.
%exclude %{python3_sitelib}/bodhi/server/tasks/composer.py
%exclude %{python3_sitelib}/bodhi/server/tasks/__pycache__/composer.*
%exclude %{python3_sitelib}/bodhi/server/metadata.py
%exclude %{python3_sitelib}/bodhi/server/__pycache__/metadata.*

%files -n bodhi-composer
%license COPYING
%doc README.rst
%pycached %{python3_sitelib}/bodhi/server/tasks/composer.py
%pycached %{python3_sitelib}/bodhi/server/metadata.py

%changelog
%autochangelog
