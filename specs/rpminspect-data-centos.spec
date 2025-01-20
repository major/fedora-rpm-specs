Name:           rpminspect-data-centos
Version:        1.4
Release:        6%{?dist}
Epoch:          1
Summary:        Build deviation compliance tool data files for CentOS
Group:          Development/Tools
License:        CC-BY-SA-4.0
URL:            https://gitlab.com/redhat/centos-stream/ci-cd/rpminspect-data-centos
Source0:        https://dcantrell.fedorapeople.org/rpminspect-data-centos/%{name}-%{version}.tar.xz
Source1:        https://dcantrell.fedorapeople.org/rpminspect-data-centos/%{name}-%{version}.tar.xz.asc
Source2:        gpgkey-62977BB9C841B965.gpg

BuildArch:      noarch

BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  gnupg2

Requires:       rpminspect >= 1.11

# Used by inspections enabled in the configuration file
Requires:       fedora-license-data
Requires:       xhtml1-dtds
Requires:       html401-dtds
Requires:       dash
Requires:       ksh
Requires:       zsh
Requires:       tcsh
Requires:       rc
Requires:       bash
Requires:       libabigail
Requires:       /usr/bin/annocheck

%description
CentOS and CentOS Stream specific configuration file for rpminspect
and data files used by the inspections provided by librpminspect.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup


%build
%meson
%meson_build


%install
%meson_install


%files
%license CC-BY-SA-4.0.txt
%doc AUTHORS README
%{_datadir}/rpminspect
%{_bindir}/rpminspect-centos


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Sep 22 2023 David Cantrell <dcantrell@redhat.com> - 1.4-2
- Convert License tag to SPDX expression

* Thu Sep 21 2023 David Cantrell <dcantrell@redhat.com> - 1.4-1
- Upgrade to rpminspect-data-centos-1.4

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Mar 14 2023 David Cantrell <dcantrell@redhat.com> - 1.2-1
- Upgrade to rpminspect-data-centos-1.2

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Nov 12 2021 David Cantrell <dcantrell@redhat.com> - 1.1-1
- Upgrade to rpminspect-data-centos-1.1

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 24 2021 David Cantrell <dcantrell@redhat.com> - 1.0-1
- Upgrade to rpminspect-data-centos-1.0
