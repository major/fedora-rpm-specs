Name:           xkb-switch
Version:        1.8.5
Release:        5%{?dist}
Summary:        Switch your X keyboard layouts from the command line 

License:        GPLv3+
URL:            https://github.com/ierton/xkb-switch
Source0:        https://github.com/ierton/xkb-switch/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libX11-devel
BuildRequires:  libxkbfile-devel

%description
xkb-switch is a C++ program that allows to query and change the XKB layout
state.


%prep
%setup -q -n %{name}-%{version}


%build
%cmake -DBUILD_XKBSWITCH_LIB:BOOL=OFF
%cmake_build


%install
%cmake_install

install -p -D -m644 man/%{name}.1 %{buildroot}/%{_mandir}/man1/%{name}.1


%files
%license COPYING
%doc README.md
%{_mandir}/man1/*
%{_bindir}/xkb-switch



%changelog
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Mar 07 2021 Till Hofmann <thofmann@fedoraproject.org> - 1.8.5-1
- Update to 1.8.5

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 17 2019 Till Hofmann <thofmann@fedoraproject.org> - 1.6.0-1
- Update to 1.6.0

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-7.20160925gitda4ef22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-6.20160925gitda4ef22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-5.20160925gitda4ef22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-4.20160925gitda4ef22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3.20160925gitda4ef22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2.20160925gitda4ef22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 14 2017 Till Hofmann <till.hofmann@posteo.de> - 1.5.0-1.20160925gitda4ef22
- Update to 1.5.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2.20160925gitd7c1856
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Sep 25 2016 Till Hofmann <till.hofmann@posteo.de> - 1.4.0-1.20160925gitd7c1856
- Update to commit 1.4.0 (commit d7c1856)
- Remove upstreamed patch

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2.20150719git532d923
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Aug 01 2015 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 1.3.1-1.20150719git532d923
- Add man page
- Change version to the actual upstream version (found with xkb-switch -v)

* Sun Jul 19 2015 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 0-0.5.20150719git532d923
- Add libX11-devel build dependency

* Sat Jul 18 2015 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 0-0.4.20150719git532d923
- Update to commit 532d923 (fixed README permissions)

* Thu Jul 16 2015 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 0-0.3.20150715git8ab2a49
- Fix permissions of README.md

* Tue Jul 14 2015 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 0-0.2.20150715git8ab2a49
- Update to commit 8ab2a49 with fixed license

* Tue Jul 14 2015 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 0-0.1.20150714git97bf2c8
- Initial package
