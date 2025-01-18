%global commit fef89a4174a7bf8cd99fa9154864ce9e8e3bf989
%global short_commit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20160908

Name:           crossguid
Version:        0
Release:        0.25.%{commit_date}git%{short_commit}%{?dist}
Summary:        Lightweight cross platform C++ GUID/UUID library

License:        MIT
URL:            https://github.com/graeme-hill/%{name}/
Source0:        %{url}/archive/%{short_commit}/%{name}-%{short_commit}.tar.gz
# Custom Makefile to properly handle build and installation
Source1:        Makefile.%{name}

BuildRequires:  gcc-c++
BuildRequires:  libuuid-devel
BuildRequires:  make

%description
CrossGuid is a minimal, cross platform, C++ GUID library. It uses the best
native GUID/UUID generator on the given platform and has a generic class for
parsing, stringifying, and comparing IDs.


%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.


%prep
%autosetup -n %{name}-%{commit}

cp -p %{SOURCE1} Makefile


%build
%make_build CXXFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS"


%install
%make_install LIBDIR=%{_libdir} INCLUDEDIR=%{_includedir}


%check
make test CXXFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS"
./test


%files
%doc README.md
%license LICENSE
%{_libdir}/*.so.*


%files devel
%{_includedir}/*
%{_libdir}/*.so


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.25.20160908gitfef89a4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.24.20160908gitfef89a4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.23.20160908gitfef89a4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.22.20160908gitfef89a4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.21.20160908gitfef89a4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20.20160908gitfef89a4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.19.20160908gitfef89a4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.18.20160908gitfef89a4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Oct 02 2021 Leigh Scott <leigh123linux@gmail.com> - 0-0.17.20160908gitfef89a4
- Fix linking

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.16.20160908gitfef89a4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.15.20160908gitfef89a4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.20160908gitfef89a4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.20160908gitfef89a4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12.20160908gitfef89a4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 12 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0-0.11.20160908gitfef89a4
- Fix linking

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.20160908gitfef89a4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.20160908gitfef89a4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.20160908gitfef89a4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.20160908gitfef89a4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.20160908gitfef89a4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr 26 2017 Mohamed El Morabity <melmorabity@fedorapeople.org> - 0-0.5.20160908gitfef89a4
- Update to latest snapshot

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.20150803git8f399e8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.20150803git8f399e8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0-0.2.20150803git8f399e8
- Fix typo in description

* Thu Sep 24 2015 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0-0.1.20150803git8f399e8
- Initial RPM release
