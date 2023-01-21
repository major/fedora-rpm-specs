Name:           fts-rest-client
Version:        3.12.0
Release:        2%{?dist}
Summary:        File Transfer Service (FTS) -- Python3 Client and CLI

License:        ASL 2.0
URL:            https://fts.web.cern.ch/
# git clone --depth=1 --branch v3.12.0-client https://gitlab.cern.ch/fts/fts-rest-flask.git fts-rest-client-3.12.0
# tar -C fts-rest-client-3.12.0/ -czf fts-rest-client-3.12.0.tar.gz src/cli src/fts3 LICENSE setup.py setup.cfg --transform "s|^|fts-rest-client-3.12.0/|" --show-transformed-names
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       python3
Requires:       python%{python3_pkgversion}-m2crypto
Requires:       python%{python3_pkgversion}-requests

# Replace previous FTS Python2 Client package
Provides:       python-fts = %{version}-%{release}
Provides:       fts-rest-cli = %{version}-%{release}
Obsoletes:      python-fts < 3.12.0
Obsoletes:      fts-rest-cli < 3.12.0

BuildArch:      noarch

%description
File Transfer Service (FTS) -- Python3 Client and CLI

%prep
%setup -q

%build
%py3_build

%install
mkdir -p %{buildroot}%{_sysconfdir}/fts3
cp src/cli/fts3client.cfg %{buildroot}%{_sysconfdir}/fts3
%py3_install

%files
%license LICENSE
%{python3_sitelib}/fts3/
%{python3_sitelib}/fts*-*.egg-info/
%{_bindir}/fts-rest-*
%dir %{_sysconfdir}/fts3/
%config(noreplace) %{_sysconfdir}/fts3/fts3client.cfg

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 27 2022 Mihai Patrascoiu <mihai.patrascoiu@cern.ch> - 3.12.0-1
- First EPEL release (v3.12.0 upstream release)
