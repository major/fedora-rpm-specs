Name:           appx-util
Version:        0.4
Release:        9%{?dist}
Summary:        Utility to create Microsoft .appx packages

# See LICENSING.md for details
License:        MPLv2.0 and BSD
URL:            https://github.com/OSInside/appx-util
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# Backports from upstream
## From: https://github.com/OSInside/appx-util/commit/504dad8ca52a44eb6f3a656368f6708b63f73c10
Patch0001:      0001-Add-support-for-OpenSSL-3.0.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel
# For tests
BuildRequires:  /usr/bin/python3

%description
appx is a tool which creates and optionally signs
Microsoft Windows APPX packages.


%prep
%autosetup -p1


%build
%cmake
%cmake_build


%install
%cmake_install


%check
%ctest


%files
%license LICENSE* LICENSING.md
%doc README.md CONTRIBUTING.md
%{_bindir}/appx


%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 30 2021 Neal Gompa <ngompa@fedoraproject.org> - 0.4-5
- Backport fix for OpenSSL 3.0 compatibility (RH#2018887)

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 0.4-4
- Rebuilt with OpenSSL 3.0.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed May 26 2021 Neal Gompa <ngompa13@gmail.com> - 0.4-2
- Update license tag

* Wed May 26 2021 Neal Gompa <ngompa13@gmail.com> - 0.4-1
- Update to 0.4

* Tue May 25 2021 Neal Gompa <ngompa13@gmail.com> - 0.3-1
- Update to 0.3

* Mon May 24 2021 Neal Gompa <ngompa13@gmail.com> - 0.2-1
- Initial package
