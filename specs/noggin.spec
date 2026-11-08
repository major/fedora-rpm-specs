Name:           noggin
Version:        1.9.0
Release:        %autorelease
Summary:        Self-service user portal for FreeIPA for communities

License:        MIT
URL:            https://noggin-aaa.readthedocs.io/
Source0:        https://github.com/fedora-infra/noggin/archive/v%{version}/%{name}-%{version}.tar.gz

Source10:       noggin-README.Fedora

# Backports from upstream
## From:

# Proposed upstream
## From:

# Downstream Fedora changes

BuildArch:      noarch
BuildRequires:  pyproject-rpm-macros >= 0-14
BuildRequires:  systemd-rpm-macros
Requires:       nginx-filesystem
Requires:       (python3dist(gunicorn) with /usr/bin/gunicorn-3)


%description
Noggin is a self-service portal for FreeIPA.

The primary purpose of the portal is to allow users to sign up
and manage their account information and group membership.

%package theme-fas
Summary:        Fedora Account System theme for Noggin
Requires:       %{name} = %{version}-%{release}

%description theme-fas
Provides a theme for Noggin used for the Fedora Account System.

%package theme-centos
Summary:        CentOS Accounts theme for Noggin
Requires:       %{name} = %{version}-%{release}

%description theme-centos
Provides a theme for Noggin used for CentOS Accounts.

%package theme-openSUSE
Summary:        openSUSE Accounts theme for Noggin
Requires:       %{name} = %{version}-%{release}

%description theme-openSUSE
Provides a theme for Noggin used for openSUSE Accounts.


%prep
%autosetup -n %{name}-%{version} -p1

# Allow markupsafe 3 and newer
sed -i "/^markupsafe/s/\^/>=/" pyproject.toml

# Allow Flask-Mail 0.10 and newer
sed -i "/^Flask-Mail/s/\^/>=/" pyproject.toml

# Install README.Fedora file
install -pm 0644 %{SOURCE10} README.Fedora


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files noggin

mkdir -p %{buildroot}%{_bindir}
install -pm 0755 deployment/scripts/sar.py %{buildroot}%{_bindir}/noggin-sar
# Fix shebangs for noggin-sar
%py3_shebang_fix %{buildroot}%{_bindir}/noggin-sar

mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_sysconfdir}/%{name}
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
mkdir -p %{buildroot}%{_localstatedir}/log/noggin
install -pm 0644 deployment/noggin.service %{buildroot}%{_unitdir}/%{name}.service
install -pm 0644 deployment/noggin.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/%{name}
touch %{buildroot}%{_sysconfdir}/%{name}/%{name}.cfg
touch %{buildroot}%{_localstatedir}/log/noggin/access.log
touch %{buildroot}%{_localstatedir}/log/noggin/error.log
mkdir -p %{buildroot}%{_sysconfdir}/nginx/conf.d
install -pm 0644 deployment/nginx.conf %{buildroot}%{_sysconfdir}/nginx/conf.d/noggin.conf
mkdir -p %{buildroot}%{_localstatedir}/log/nginx
touch %{buildroot}%{_localstatedir}/log/nginx/noggin.access.log
touch %{buildroot}%{_localstatedir}/log/nginx/noggin.error.log


%check
%pyproject_check_import


%files -f %{pyproject_files}
%license LICENSE
%doc README.md deployment/noggin.cfg.example README.Fedora
%{_bindir}/noggin-sar
%{_unitdir}/%{name}.service
%ghost %{_sysconfdir}/%{name}/%{name}.cfg
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%config(noreplace) %{_sysconfdir}/nginx/conf.d/noggin.conf
%dir %{_localstatedir}/log/noggin
%ghost %{_localstatedir}/log/noggin/*.log
%ghost %{_localstatedir}/log/nginx/*.log
%exclude %{python3_sitelib}/%{name}/themes/fas
%exclude %{python3_sitelib}/%{name}/themes/centos
%exclude %{python3_sitelib}/%{name}/themes/openSUSE


%files theme-fas
%{python3_sitelib}/%{name}/themes/fas


%files theme-centos
%{python3_sitelib}/%{name}/themes/centos


%files theme-openSUSE
%{python3_sitelib}/%{name}/themes/openSUSE


%changelog
%autochangelog
