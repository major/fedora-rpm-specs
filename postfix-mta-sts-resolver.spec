%global pypi_name postfix_mta_sts_resolver

Name:           postfix-mta-sts-resolver
Version:        1.4.0
Release:        %autorelease
Summary:        Daemon providing MTA-STS map to Postfix

License:        MIT
URL:            https://github.com/Snawoot/%{name}

# pypi version is stripped down without manpages, doc and examples
Source0:        https://github.com/Snawoot/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        mta-sts-daemon.yml
Source2:        postfix-mta-sts-resolver.service
Source3:        https://github.com/Snawoot/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz.asc
Source4:        https://github.com/Snawoot.gpg

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  rubygem-asciidoctor
BuildRequires:  make
BuildRequires:  systemd-rpm-macros
BuildRequires:  pyproject-rpm-macros
BuildRequires:  sed
BuildRequires:  gnupg2

Requires(pre):  shadow-utils
BuildRequires:  tox
BuildRequires:  python3dist(tox-current-env)

%description
postfix-mta-sts-resolver provides a lookup daemon and command line
query utility for MTA-STS policies (RFC 8461).  The daemon provides TLS
client policy to Postfix via socketmap.



%prep
%{gpgverify} --keyring='%{SOURCE4}' --signature='%{SOURCE3}' --data='%{SOURCE0}'
%autosetup -n %{name}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel
make doc


%install
%pyproject_install
%pyproject_save_files postfix_mta_sts_resolver

install -p -D -m 0640 %{SOURCE1} %{buildroot}%{_sysconfdir}/mta-sts-daemon.yml
install -p -D -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}.service

mkdir -p %{buildroot}%{_sharedstatedir}/mta-sts

mkdir -p %{buildroot}%{_mandir}/man1
install -p -D -m 0644 man/*.1 %{buildroot}%{_mandir}/man1/
mkdir -p %{buildroot}%{_mandir}/man5
install -p -D -m 0644 man/*.5 %{buildroot}%{_mandir}/man5/


%check
# Upstream's test suite doesn't play nicely with Fedora's offline build system
%pyproject_check_import -e 'postfix_mta_sts_resolver.postgres_cache' -e 'postfix_mta_sts_resolver.redis_cache' -e 'postfix_mta_sts_resolver.sqlite_cache'


%pyproject_extras_subpkg -n %{name} sqlite dev redis postgres uvloop


%files  -f %{pyproject_files} 
%license LICENSE
%doc README.md config_examples
%{_mandir}/man*/*
%{_bindir}/mta-sts-query
%{_bindir}/mta-sts-daemon
%config(noreplace) %attr(0640,root,mta-sts) %{_sysconfdir}/mta-sts-daemon.yml
%{_unitdir}/%{name}.service
%dir %attr(0755,mta-sts,mta-sts) %{_sharedstatedir}/mta-sts


%pre
getent group mta-sts >/dev/null || groupadd -r mta-sts
getent passwd mta-sts >/dev/null || \
    useradd -r -g mta-sts -d %{_sharedstatedir}/mta-sts -s /sbin/nologin \
    -c "Postfix MTA-STS Map Daemon" mta-sts


%post
%systemd_post %{name}.service


%preun
%systemd_preun %{name}.service


%postun
%systemd_postun_with_restart %{name}.service


%changelog
%autochangelog
