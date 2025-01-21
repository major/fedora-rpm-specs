%global forgeurl https://github.com/CyberShadow/znc-clientbuffer
%global commit 9766a4ad5d27e815bbbc8b6842e13b7b4b5826f6
%forgemeta

%global modname clientbuffer
%global znc_version %((znc -v 2>/dev/null || echo 'a 0') | head -1 | awk '{print $2}')

Name:           znc-%{modname}
Version:        0
Release:        0.29%{?dist}
Summary:        ZNC module for client specific buffers

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            %forgeurl
Source0:        %forgesource

BuildRequires:  gcc-c++
BuildRequires:  python-devel
BuildRequires:  cmake
BuildRequires:  zlib-devel
BuildRequires:  znc-devel
Requires:       znc%{?_isa} = %znc_version

%description
The client buffer module maintains client specific buffers for identified
clients.

%prep
%autosetup -n %{name}-%{commit}

%build
CXXFLAGS="%{optflags}" LDFLAGS="%{__global_ldflags}" znc-buildmod %{modname}.cpp

%install
install -Dpm0755 %{modname}.so %{buildroot}%{_libdir}/znc/%{modname}.so

%files
%{_libdir}/znc/%{modname}.so

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Aug 25 2024 Neil Hanlon <nhanlon@ciq.com - 0-0.28
- rebuild for znc 1.9.1 in f42
- znc-buildmod needs cmake/python

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 0-0.27
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 19 2021 Pablo Greco <pablo@fliagreco.com.ar> - 0-0.18
- Rebuilt for bad version in f33

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 22 2020 Jason L Tibbitts III <tibbs@math.uh.edu> - 0-0.15
- Rebuild for new znc.

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 29 2019 Jason L Tibbitts III <tibbs@math.uh.edu> - 0-0.13.git9766a4a
- Rebuild for new znc.

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12.git9766a4a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 29 2019 Jason L Tibbitts III <tibbs@math.uh.edu> - 0-0.11.20190129git9766a4a
- Convert to forge macros.

* Wed Jan 23 2019 Pete Walter <pwalter@fedoraproject.org> - 0-0.10gitfe0f368
- Rebuild for ICU 63

* Tue Jul 31 2018 Jason L Tibbitts III <tibbs@math.uh.edu> - 0-0.9gitfe0f368
- Require specific version of znc, to avoid unexpected breakage when znc
  updates.  (Broken deps are better than a broken server.)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8gitfe0f368
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Pete Walter <pwalter@fedoraproject.org> - 0-0.7gitfe0f368
- Rebuild for ICU 62

* Fri Jun 01 2018 Jason L Tibbitts III <tibbs@math.uh.edu> - 0-0.6gitfe0f368
- Rebuild for new znc.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5gitfe0f368
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4gitfe0f368
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3gitfe0f368
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2gitfe0f368
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Aug 17 2016 Igor Gnatenko <ignatenko@redhat.com> - 0-0.1gitfe0f368
- Initial package
