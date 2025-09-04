# Created by pyp2rpm-3.3.2
%global pypi_name collectd-puppet
%global module_name collectd_puppet
%global forgeurl https://github.com/cernops/collectd-puppet

Name:           python-%{module_name}
Version:        2.1.1
Release:        %autorelease
Summary:        Collectd plugin to monitor puppet agents
%global tag %{version}
%forgemeta

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            %{forgeurl}
Source0:        %{forgesource}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  systemd-rpm-macros

Requires:       collectd-python

%description
Collectd plugin for puppet run status.


%package -n     python3-%{module_name}
Summary:        %{summary}


%description -n python3-%{module_name}
Collectd plugin for puppet run status.


%prep
%forgesetup


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l collectd_puppet


%postun
%systemd_postun_with_restart collectd.service


%files -n python3-%{module_name} -f %{pyproject_files}
%doc README.rst NEWS.rst
%{_datadir}/collectd/puppet_types.db


%changelog
%autochangelog
