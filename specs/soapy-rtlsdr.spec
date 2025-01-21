Name:           soapy-rtlsdr
Version:        0.3.2
Release:        9%{?dist}
Summary:        SoapySDR module for RTL-SDR hardware

License:        MIT
URL:            https://github.com/pothosware/SoapyRTLSDR
Source0:        https://github.com/pothosware/SoapyRTLSDR/archive/refs/tags/soapy-rtl-sdr-%{version}.tar.gz

BuildRequires:  cmake gcc-c++ SoapySDR-devel rtl-sdr-devel

%description
SoapyRTLSDR is a plug-in module for SoapySDR adding support for
RTL-SDR hardware.

%prep
%autosetup -n SoapyRTLSDR-soapy-rtl-sdr-%{version}

%build
%cmake
%cmake_build


%install
%cmake_install


%ldconfig_scriptlets
%files
%license LICENSE.txt
%{_libdir}/SoapySDR/modules*/librtlsdrSupport.so

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Apr  9 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 0.3.2-7
- Rebuilt for new rtl-sdr

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Aug 16 2021 Matt Domsch <matt@domsch.com> - 0.3.2-1
- Upstream 0.3.2

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Aug  2 2020 Matt Domsch <matt@domsch.com> 0.3.1-1
- Upstream 0.3.1, changed tagging, tgz name and internal path name
- Fedora 33 cmake updates

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Apr 12 2020 Matt Domsch <matt@domsch.com> 0.3.0-1
- Upstream 0.3.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug  7 2018 Matt Domsch <matt@domsch.com> 0.2.5-1
- initial Fedora packaging
