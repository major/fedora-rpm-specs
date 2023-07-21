Name:           fts-rest-client
Version:        3.12.2
Release:        4%{?dist}
Summary:        File Transfer Service (FTS) -- Python3 Client and CLI

License:        ASL 2.0
URL:            https://fts.web.cern.ch/
# git clone --depth=1 --branch v3.12.2 https://gitlab.cern.ch/fts/fts-rest-flask.git fts-rest-client-3.12.2
# tar -C fts-rest-client-3.12.2/ -czf fts-rest-client-3.12.2.tar.gz src/cli src/fts3 LICENSE setup.py setup.cfg --transform "s|^|fts-rest-client-3.12.2/|" --show-transformed-names
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
%py3_install

%files
%license LICENSE
%{python3_sitelib}/fts3/
%{python3_sitelib}/fts*-*.egg-info/
%{_bindir}/fts-rest-*

%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jul 06 2023 Mihai Patrascoiu <mihai.patrascoiu@cern.ch> - 3.12.2-3
- Remove "/etc/fts3/fts3client.cfg" from the installation files (FTS-1842)

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 3.12.2-2
- Rebuilt for Python 3.12

* Thu Mar 02 2023 Mihai Patrascoiu <mihai.patrascoiu@cern.ch> - 3.12.2-1
- New upstream release 3.12.2
- Remove patch for bugzilla#2164054 as it has been addressed upstream

* Tue Jan 31 2023 Mihai Patrascoiu <mihai.patrascoiu@cern.ch> - 3.12.1-1
- New upstream release 3.12.1
- Apply patch for bugzilla#2164054

* Tue Jan 31 2023 Miro Hrončok <mhroncok@redhat.com> - 3.12.0-3
- Rebuilt to change Python shebangs to /usr/bin/python3.6 on EPEL 8

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 27 2022 Mihai Patrascoiu <mihai.patrascoiu@cern.ch> - 3.12.0-1
- First EPEL release (v3.12.0 upstream release)
