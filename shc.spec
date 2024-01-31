%global owner neurobin

Name: shc
Summary: Shell script compiler
URL: https://neurobin.org/projects/softwares/unix/shc/
Version: 4.0.3
Release: 11%{?dist}
Source0: https://github.com/%{owner}/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
License: GPLv3
BuildRequires: make
BuildRequires: gcc

%description
SHC is a generic shell script compiler. It takes
a script, which is specified on the command line
and produces C source code. The generated source
code is then compiled and linked to produce a s-
tripped binary. 

%prep
%autosetup -n %{name}-%{version}

%build
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc AUTHORS ChangeLog README README.md
%{_bindir}/%{name}
%{_mandir}/*/%{name}*

%changelog
* Mon Jan 29 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 9 2019 Mosaab Alzoubi <moceap@hotmail.com> - 4.0.3-1
- Update to 4.0.3

* Mon Apr 10 2017 Mosaab Alzoubi <moceap@hotmail.com> - 3.9.3-1
- Initial
