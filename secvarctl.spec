Name:		secvarctl
Version:	0.3
Release:	4%{?dist}
Summary:	A command line tool for managing Secure Boot Variables on POWER

License:	ASL 2.0
URL:		https://github.com/open-power/secvarctl
Source0:	https://github.com/open-power/secvarctl/archive/v%{version}.tar.gz


BuildRequires:	gcc
BuildRequires:	cmake
BuildRequires:	mbedtls-devel


%description
secvarctl is a collection of sub-commands for reading, writing
and updating secure variables on POWER's Secure Boot.
The sub-commands are:
	-read , prints info on secure variables
	-write , updates secure variable with new signed authenticated file
	-validate , validates format of given file
	-verify , determines if new variable updates are correctly signed/formatted
	-generate , create relevant files for secure variable management

%prep
%setup -q


%build
%cmake -DCMAKE_BUILD_TYPE="Release"
%cmake_build


%install
%cmake_install


%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Morten Stevens <mstevens@fedoraproject.org> - 0.3-3
- Rebuilt for mbedTLS 2.28.0

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 14 2021 Nick Child <nnac123@linux.vnet.ibm.com> - 0.3-1
- Update to v0.3

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Apr 29 2021 Nick Child <nnac123@linux.vnet.ibm.com> - 0.2-1
- Update to v0.2
- Allow compiling with Openssl

* Thu Nov  5 2020 Nick Child <nnac123@linux.vnet.ibm.com> - 0.1-1
- Initial package
- 
