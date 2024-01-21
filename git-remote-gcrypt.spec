Name:       git-remote-gcrypt
Version:    1.5
Release:    4%{?dist}
Summary:    GNU Privacy Guard-encrypted git remote

License:    GPLv3
URL:        https://git.spwhitton.name/%{name}
Source0:    https://git.spwhitton.name/%{name}/snapshot/%{name}-%{version}.tar.gz

BuildArch:  noarch

BuildRequires:  python3-docutils
Requires:   gnupg2 git-core

%description
This lets git store git repositories in encrypted form.
It supports storing repositories on rsync or sftp servers.
It can also store the encrypted git repository inside a remote git
repository. All the regular git commands like git push and git pull
can be used to operate on such an encrypted repository.

The aim is to provide confidential, authenticated git storage and
collaboration using typical untrusted file hosts or services.

%prep
%setup -q -n %{name}-%{version}

%build
:

%install
export DESTDIR="%{buildroot}"
export prefix="%{_prefix}"
./install.sh

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%license COPYING
%doc CHANGELOG CONTRIBUTING.rst README.rst

%changelog
* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

%autochangelog
