Name:       clpeak
Version:    1.1.4
Release:    2%{?dist}
Summary:    Find peak OpenCL capacities like bandwidth & compute
License:    Apache-2.0
URL:        https://github.com/krrishnarraj/%{name}
Source0:    %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: mesa-libGL-devel
BuildRequires: ocl-icd-devel
BuildRequires: opencl-headers


%description
A tool which profiles OpenCL devices to find their peak capacities like
bandwidth & compute.

%prep
%autosetup


%build
%cmake
%cmake_build


%install
%cmake_install
rm -v %{buildroot}/%{_datadir}/clpeak/LICENSE


%check
%ctest


%files
%license LICENSE
%doc README.md
%{_bindir}/clpeak


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Dec 24 2024 Filipe Rosset <rosset.filipe@gmail.com> - 1.1.4-1
- Updated to 1.1.4 fixes rhbz#2333953

* Fri Nov 29 2024 Dominik Mierzejewski <dominik@greysector.net> - 1.1.3-1
- updated to 1.1.3 (resolves rhbz#2328987)
- license changed to Apache-2.0
- run tests

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 04 2022 Dominik Mierzejewski <dominik@greysector.net> - 1.1.2-1
- update to 1.1.2
- specfile cleanups

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 04 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 1.1.0-1
- Update to 1.1.0
- Package cleanups

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-23.20170711git8edab23
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-22.20170711git8edab23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-21.20170711git8edab23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-20.20170711git8edab23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-19.20170711git8edab23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-18.20170711git8edab23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-17.20170711git8edab23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-16.20170711git8edab23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-15.20170711git8edab23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 11 2017 Filipe Rosset <rosset.filipe@gmail.com> - 0.1-14.20170711git8edab23
- Update to the latest upstream, fixes rhbz#1423267
- Include upstream fix for https://github.com/krrishnarraj/clpeak/issues/36

* Sat Jun 17 2017 Filipe Rosset <rosset.filipe@gmail.com> - 0.1-13.20170617git7904f26
- Update to the latest upstream, fixes rhbz#1423267

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-12.20160207git1f90347
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Feb 07 2016 Fabian Deutsch <fabiand@fedoraproject.org> - 0.1-11.20160207git1f90347
- Update to the latest upstream

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-10.20150215git9a39c0c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-9.20150215git9a39c0c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.1-8.20150215git9a39c0c
- Rebuilt for GCC 5 C++11 ABI change

* Tue Feb 17 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.1-7.20150215git9a39c0c
- Re-enable ARMv7 now headers issue is fixed

* Sun Feb 15 2015 Fabian Deutsch <fabiand@fedoraproject.org> - 0.1-6.20150215git9a39c0c
- Update to latest upstream

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-5.20140603git97519a8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-4.20140603git97519a8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jun 03 2014 Fabian Deutsch <fabiand@fedoraproject.org> - 0.1-3.20140503git97519a8
- Async update to sync with upstream

* Fri Apr 25 2014 Fabian Deutsch <fabiand@fedoraproject.org> - 0.1-2.20140425gitc0b94f2
- Improve installation
- Drop gcc-c++ BR

* Fri Apr 25 2014 Fabian Deutsch <fabiand@fedoraproject.org> - 0.1-1.20140425gitc0b94f2
- Initial package
