Name:               python-calligrabot
Version:            1.0.0
Release:            3%{?dist}
Summary:            A robosignatory driver for the CentOS Stream signing service

License:            MIT
URL:                https://pagure.io/calligrabot/
Source0:            https://pagure.io/calligrabot/archive/%{version}/calligrabot-%{version}.tar.gz

BuildArch:          noarch

BuildRequires:      python3-devel
BuildRequires:      python3-setuptools

# For running tests
BuildRequires:      koji
BuildRequires:      python3-fedora-messaging
BuildRequires:      python3-pytest
BuildRequires:      python3-robosignatory >= 0.7.0
BuildRequires:      python3-rpm-head-signing

%description
A robosignatory driver for the CentOS Stream signing service.

%package -n python3-calligrabot
Summary: %summary
Requires: koji

%description -n python3-calligrabot
A robosignatory driver for the CentOS Stream signing service.


%prep
%setup -q -n calligrabot-%{version}
# Remove bundled egg-info in case it exists
rm -rf calligrabot.egg-info


%build
%py3_build


%install
%py3_install


%check
%pytest


%files -n python3-calligrabot
%doc README.md
%license LICENSE
%{python3_sitelib}/calligrabot/
%{python3_sitelib}/calligrabot-%{version}*
%{_bindir}/calligrabot


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Sep 10 2021 Merlin Mathesius <mmathesi@redhat.com> - 1.0.0-1
- Initial packaging for Fedora.
