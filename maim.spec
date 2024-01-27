Name:			maim
Version:		5.7.4
Release:		7%{?dist}
Summary:		Command-line screen capture tool

License:		GPLv3
URL:			https://github.com/naelstrof/maim
Source0:		https://github.com/naelstrof/maim/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	gcc-c++
BuildRequires:	cmake
BuildRequires:	libX11-devel
BuildRequires:	libXrender-devel
BuildRequires:	libXfixes-devel
BuildRequires:	libXrandr-devel
BuildRequires:	libXcomposite-devel
BuildRequires:	libpng-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libwebp-devel
BuildRequires:	mesa-libGL-devel
BuildRequires:	glm-devel
BuildRequires:	libslopy-devel >= 7.5
BuildRequires:	libicu-devel

%description
maim (make image) is a screenshot utility that provides options for capturing
predetermined or user selected regions of your desktop.

%prep
%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%doc README.md
%{_bindir}/maim
%{_mandir}/man1/maim.1.*

%license COPYING license.txt

%changelog
* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 František Zatloukal <fzatlouk@redhat.com> - 5.7.4-4
- Rebuilt for ICU 73.2

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 31 2022 Pete Walter <pwalter@fedoraproject.org> - 5.7.4-2
- Rebuild for ICU 72

* Mon Nov 28 2022 Alois Mahdal <netvor@vornet.cz> - 5.7.4-1
- Update to upstream release 5.7.4 (RHBZ#1823039)

* Mon Aug 01 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 5.6.3-9
- Rebuilt for ICU 71.1

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 5.6.3-6
- Rebuild for slop-7.6

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu May 20 2021 Pete Walter <pwalter@fedoraproject.org> - 5.6.3-4
- Rebuild for ICU 69

* Wed May 19 2021 Pete Walter <pwalter@fedoraproject.org> - 5.6.3-3
- Rebuild for ICU 69

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Nov 29 2020 Aymen Qader <qader.aymen@gmail.com> - 5.6.3-1
- Update to upstream release 5.6.3.

* Sat Aug 01 2020 Aymen Qader <qader.aymen@gmail.com> - 5.5.3-5
- Use new CMake macros; add libicu-devel build dependency.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.3-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 19 2019 Aymen Qader <qader.aymen@gmail.com> 5.5.3-1
- Initial version of the package
