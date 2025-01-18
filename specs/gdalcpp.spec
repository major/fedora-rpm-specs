%global commit 7e23085e7da80c8805fff54cc18e2705ac332074
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global debug_package %{nil}

Name:           gdalcpp
Version:        1.3.0
Release:        9.20210925git%{shortcommit}%{?dist}
Summary:        C++11 wrapper classes for GDAL/OGR

License:        BSL-1.0
URL:            https://github.com/joto/gdalcpp
Source0:        https://github.com/joto/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz

%description
These are some small wrapper classes for GDAL offering:

* classes with RAII instead of the arcane cleanup functions in stock GDAL
* works with GDAL 1 and 2
* allows you to write less boilerplate code

The classes are not very complete, they just have the code I needed for
various programs.


%package        devel
Summary:        Development files for %{name}
Provides:       %{name}-static = %{version}-%{release}

%description    devel
These are some small wrapper classes for GDAL offering:

* classes with RAII instead of the arcane cleanup functions in stock GDAL
* works with GDAL 1 and 2
* allows you to write less boilerplate code

The classes are not very complete, they just have the code I needed for
various programs.


%prep
%setup -q -n %{name}-%{commit}


%build


%install
mkdir -p %{buildroot}%{_includedir}
cp -p *.hpp  %{buildroot}%{_includedir}


%files devel
%doc README.md
%license LICENSE.txt
%{_includedir}/*.hpp


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-9.20210925git7e23085
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-8.20210925git7e23085
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-7.20210925git7e23085
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-6.20210925git7e23085
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5.20210925git7e23085
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4.20210925git7e23085
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3.20210925git7e23085
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2.20210925git7e23085
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec 17 2021 Tom Hughes <tom@compton.nu> - 1.3.0-1.20210925git7e23085
- Update to 1.3.0 upstream release

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-7.20180829git4df5ca1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-6.20180829git4df5ca1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5.20180829git4df5ca1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4.20180829git4df5ca1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3.20180829git4df5ca1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2.20180829git4df5ca1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec  8 2018 Tom Hughes <tom@compton.nu> - 1.2.0-1.20180829git4df5ca1
- Update to 1.2.0 upstream release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-8.20160601git225b97c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-7.20160601git225b97c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-6.20160601git225b97c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-5.20160601git225b97c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4.20160601git225b97c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jun  1 2016 Tom Hughes <tom@compton.nu> - 1.1.1-3.20160601git225b97c
- Update to upstream snapshot

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec  4 2015 Tom Hughes <tom@compton.nu> - 1.1.1-1
- Update to 1.1.1 upstream release

* Tue Dec  1 2015 Tom Hughes <tom@compton.nu> - 1.1.0-1
- Restore dist tag

* Mon Nov 23 2015 Tom Hughes <tom@compton.nu> - 1.1.0-1
- Update to 1.1.0 upstream release

* Tue Aug 25 2015 Tom Hughes <tom@compton.nu> - 0-0.1.20150825git75c0ac4
- Initial build
