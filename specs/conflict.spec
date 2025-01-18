Name:           conflict
Version:        20240429
Release:        2%{?dist}
Summary:        Check for conflicting binary names on path

License:        MIT
URL:            https://invisible-island.net/conflict/conflict.html
Source0:        https://invisible-island.net/archives/conflict/conflict-%{version}.tgz
Source1:        https://invisible-island.net/archives/conflict/conflict-%{version}.tgz.asc
Source2:        https://invisible-island.net/public/dickey@invisible-island.net-rsa3072.asc

BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  groff
BuildRequires:  make

%description
CONFLICT examines the user-specifiable list of programs, looking for instances
in the user's path which conflict (i.e., the name appears in more than one
point in the path).


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n %{name}-%{version}


%build
%configure --disable-stripping
%make_build


%install
%make_install

%check
bash run_test.sh

%files
%license COPYING
%doc README
%doc CHANGES
%{_bindir}/conflict
%{_mandir}/man1/conflict.1*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 20240429-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

%autochangelog
