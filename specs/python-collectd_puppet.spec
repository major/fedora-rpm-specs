# Created by pyp2rpm-3.3.2
%global pypi_name collectd-puppet
%global module_name collectd_puppet
%global forgeurl https://github.com/cernops/collectd-puppet

Name:           python-%{module_name}
Version:        2.0.0
Release:        %autorelease
Summary:        Collectd plugin to monitor puppet agents
%global tag %{version}
%forgemeta

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            %{forgeurl}
Source0:        %{forgesource}
BuildArch:      noarch

Requires:       collectd-python

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  systemd-rpm-macros


%description
Collectd plugin for puppet run status.

%package -n     python3-%{module_name}
Summary:        %{summary}

Requires:       python3dist(pyyaml)
%description -n python3-%{module_name}
Collectd plugin for puppet run status.

%prep
%forgesetup

%build
%py3_build

%install
%py3_install

%postun
%systemd_postun_with_restart collectd.service

%files -n python3-%{module_name}
%license LICENSE
%doc README.rst NEWS.rst
%{_datadir}/collectd/puppet_types.db
%{python3_sitelib}/%{module_name}
%{python3_sitelib}/%{module_name}-%{version}-py%{python3_version}.egg-info

%changelog
%autochangelog
