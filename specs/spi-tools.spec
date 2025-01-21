Name:		spi-tools
Version:	1.0.2
Release:	6%{?dist}
Summary:	Simple command line tools to help using Linux spidev devices

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:	GPL-2.0-only
URL:		https://github.com/cpb-/spi-tools/
Source0:	https://github.com/cpb-/spi-tools/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:		0001-Don-t-override-the-compiler-flags-with-nonsense-ones.patch

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	help2man

%description
This package contains spi-config and spi-pipe, simple command line tools to
help using Linux spidev devices.


%prep
%autosetup -p1


%build
autoreconf -fi
%configure
%make_build


%install
%make_install


%files
%license LICENSE
%doc README.md
%{_bindir}/spi-config
%{_bindir}/spi-pipe
%{_mandir}/man1/spi-config.1*
%{_mandir}/man1/spi-pipe.1*


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0.2-5
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Feb 06 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 1.0.2-1
- Update to 1.0.2

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Dec 05 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 1.0.1-1
- Update to 1.0.1

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jul 20 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 1.0.0-1
- Update to 1.0.0

* Sat May 15 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 0.8.7-1
- Update to 0.8.7

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Oct 10 16:02:10 BST 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.8.5-1
- Update to 0.8.5

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Lubomir Rintel <lkundrak@v3.sk> - 0.8.4-1
- Update to 0.8.4

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 18 2019 Lubomir Rintel <lkundrak@v3.sk> - 0.8.3-1
- Update to 0.8.3
- Drop Group tag
- Fix Source

* Sat Mar 24 2018 Lubomir Rintel <lkundrak@v3.sk> - 0.8.1-1
- Initial packaging
