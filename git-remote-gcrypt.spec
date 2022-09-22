Name:       git-remote-gcrypt
Version:    1.4
Release:    3%{?dist}
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
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Dusty Mabe <dusty@dustymabe.com> - 1.4-1
- Update to 1.4 release

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Sep 29 2019 Dusty Mabe <dusty@dustymabe.com> - 1.2-1
- First package for Fedora
