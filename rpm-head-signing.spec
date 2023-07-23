Name:          rpm-head-signing
Version:       1.7.1
Release:       2%{?dist}
Summary:       A python module for signing RPM header and file digests
License:       BSD
URL:           https://github.com/fedora-iot/rpm-head-signing
Source0:       %url/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: rpm-devel

%description
A small Python module (with C helper) to extract a RPM header and file
digests and reinsert the signature and signed file digests. This is
used for when you want to retrieve the parts to sign if you have a
remote signing server without having to transmit the entire RPM over
to the server.

%prep
%autosetup -p1

%build
%py3_build

%install
%py3_install

%files
%license LICENSE
%doc README.md
%{_bindir}/verify-rpm-ima-signatures
%{python3_sitearch}/rpm_head_signing/
%{python3_sitearch}/rpm_head_signing-*/

%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 20 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 1.7.1-1
- Initial package
