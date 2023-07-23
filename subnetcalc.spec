Name:           subnetcalc
Version:        2.4.22
Release:        2%{?dist}
Summary:        IPv4/IPv6 Subnet Calculator
License:        GPLv3+
URL:            https://www.nntb.no/~dreibh/subnetcalc/
Source0:        https://www.nntb.no/~dreibh/subnetcalc/download/%{name}-%{version}.tar.xz


BuildRequires:  gcc gcc-c++
BuildRequires:  GeoIP-devel
BuildRequires:  cmake

%description
SubNetCalc is an IPv4/IPv6 subnet address calculator. For given IPv4 or IPv6 
address and netmask or prefix length, it calculates network address, broadcast
address, maximum number of hosts and host address range. Also, it prints the 
addresses in binary format for better understandability. Furthermore, it 
prints useful information on specific address types (e.g. type, scope, 
interface ID, etc.).

%prep
%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc AUTHORS ChangeLog README.md
%license COPYING
%{_bindir}/subnetcalc
%{_mandir}/man1/subnetcalc.1*

%changelog
* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jul  2 2023 Yanko Kaneti <yaneti@declera.com> - 2.4.22-1
- Update to 2.4.22

* Tue Jan 24 2023 Yanko Kaneti <yaneti@declera.com> - 2.4.21-1
- Update to 2.4.21. New project URL

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Sep 13 2022 Yanko Kaneti <yaneti@declera.com> - 2.4.20-1
- Update to 2.4.20

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov  9 2021 Yanko Kaneti <yaneti@declera.com> - 2.4.19-1
- Update to 2.4.19

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Feb  2 2021 Yanko Kaneti <yaneti@declera.com> - 2.4.17-1
- Update to 2.4.17

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug  4 2020 Yanko Kaneti <yaneti@declera.com> - 2.4.16-4
- Up to date cmake setup

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.16-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 18 2020 Yanko Kaneti <yaneti@declera.com> - 2.4.16-1
- Update to 2.4.16

* Sat Feb 8 2020 Yanko Kaneti <yaneti@declera.com> - 2.4.15-1
- Update to 2.4.15

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 16 2019 Yanko Kaneti <yaneti@declera.com> - 2.4.14-1
- Update to 2.4.14

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 21 2019 Yanko Kaneti <yaneti@declera.com> - 2.4.11-1
- Update to 2.4.11

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec  3 2018 Yanko Kaneti <yaneti@declera.com> - 2.4.10-1
- Update to 2.4.10. Switch to cmake

* Mon Jul 16 2018 Yanko Kaneti <yaneti@declera.com> - 2.4.3-7
- also BR: gcc-c++ - https://fedoraproject.org/wiki/Changes/Remove_GCC_from_BuildRoot

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Feb 29 2016 Yanko Kaneti <yaneti@declera.com> - 2.4.3-1
- Update to 2.4.3

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jul 10 2015 Christopher Meng <rpm@cicku.me> - 2.4.2-1
- Update to 2.4.2

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.3.1-3
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 29 2014 Christopher Meng <rpm@cicku.me> - 2.3.1-1
- Update to 2.3.1

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Mar 15 2014 Christopher Meng <rpm@cicku.me> - 2.2.1-1
- Update to 2.2.1

* Tue Nov 12 2013 Christopher Meng <rpm@cicku.me> - 2.2.0-1
- Initial Package.
