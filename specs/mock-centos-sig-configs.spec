Name:           mock-centos-sig-configs
Version:        0.6.1
Release:        %autorelease
Summary:        Mock configs for CentOS SIGs

License:        MIT
URL:            https://pagure.io/centos-sig-hyperscale/mock-centos-sig-configs
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  make
Requires:       mock-core-configs
Enhances:       mock-core-configs

BuildArch:      noarch

%description
This package contains mock configs for various CentOS SIGs.

%prep
%setup -q

%build

%install
%make_install

%files
%license LICENSE
%doc README.md
%defattr(0644, root, mock)
%config(noreplace) %{_sysconfdir}/mock/*.cfg
%config(noreplace) %{_sysconfdir}/mock/templates/*.tpl

%changelog
%autochangelog
