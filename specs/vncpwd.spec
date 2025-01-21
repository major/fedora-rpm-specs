%global         gituser         jeroennijhof
%global         gitname         vncpwd
%global         commit          58d585cbbc861bd6dbd9f6709ce8cb7f2afb75ba
%global         commitdate      20180223
%global         shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           vncpwd
Version:        0.1
Release:        8%{?dist}
Summary:        VNC Password Decrypter

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            https://github.com/jeroennijhof/vncpwd

# Source0:        https://github.com/%{gituser}/%{gitname}/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
Source0:        https://github.com/%{gituser}/%{gitname}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires:  gcc

%description
The vncpwd decrypts the VNC password.

%prep
%autosetup -n %{name}-%{version}


%build
%make_build CFLAGS="%{optflags}"



%install
make install DESTDIR="%{buildroot}"



%files
%doc README
%license LICENSE
%{_bindir}/%{name}

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.1-7
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 23 2022 Michal Ambroz <rebus at, seznam.cz> 0.1-1
- bump to release 0.1

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-11.20170607git596854c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-10.20170607git596854c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-9.20170607git596854c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-8.20170607git596854c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-7.20170607git596854c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-6.20170607git596854c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-5.20170607git596854c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-4.20170607git596854c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Dec 10 2017 Michal Ambroz <rebus at, seznam.cz> 0.0-3.20170607git596854c
- bump to latest commit
- upstream notified about wrong FSF address
- https://github.com/jeroennijhof/vncpwd/issues/3

* Thu Apr 13 2017 Michal Ambroz <rebus at, seznam.cz> 0.0-2.gitdafebe0
- removed unused macro, adding README as license file

* Sat Mar 18 2017 Michal Ambroz <rebus at, seznam.cz> 0.0-1.gitdafebe0
- initial build for Fedora
