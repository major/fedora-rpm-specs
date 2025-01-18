Name:		SDL2_ttf
Version:	2.22.0
Release:	4%{?dist}
Summary:	TrueType font rendering library for SDL2
License:	Zlib
URL:		https://github.com/libsdl-org/SDL_ttf
Source0:	https://github.com/libsdl-org/SDL_ttf/releases/download/release-%{version}/SDL2_ttf-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:	SDL2-devel
BuildRequires:  libGL-devel
BuildRequires:	freetype-devel
BuildRequires:  harfbuzz-devel
BuildRequires:	zlib-devel

%description
This library allows you to use TrueType fonts to render text in SDL2
applications.

%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	SDL2-devel%{?_isa}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup
rm -rf external
# Fix end-of-line encoding
sed -i 's/\r//' README.txt CHANGES.txt LICENSE.txt

%build
%cmake -DSDL2TTF_HARFBUZZ=true
%cmake_build

%install
%cmake_install
find %{buildroot} -type f -name '*.la' -delete -print

%ldconfig_scriptlets

%files
%license LICENSE.txt
%doc README.txt CHANGES.txt
%{_libdir}/lib*.so.*

%files devel
%{_libdir}/lib*.so
%{_includedir}/SDL2/*
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/SDL2_ttf/

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.22.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.22.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Tom Callaway <spot@fedoraproject.org> - 2.22.0-1
- update to 2.22.0
- fix license tag to be SPDX

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.20.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.20.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Feb  8 2023 Tom Callaway <spot@fedoraproject.org> - 2.20.2-1
- update to 2.20.2

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.20.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 03 2022 Pete Walter <pwalter@fedoraproject.org> - 2.20.1-1
- Update to 2.20.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.20.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul  8 2022 Tom Callaway <spot@fedoraproject.org> - 2.20.0-1
- update to 2.20.0

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 12 2022 Tom Callaway <spot@fedoraproject.org> - 2.0.18-1
- update to 2.0.18

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.15-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.15-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.15-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov  6 2019 Tom Callaway <spot@fedoraproject.org> - 2.0.15-3
- rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Tom Callaway <spot@fedoraproject.org> - 2.0.15-1
- update to 2.0.15

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 12 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.0.14-2
- add libGL-devel to BRs

* Tue Feb  2 2016 Tom Callaway <spot@fedoraproject.org> - 2.0.14-1
- update to 2.0.14

* Sun Jan 10 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.0.13-1
- Update to 2.0.13 (RHBZ #1296754)

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 2 2014 Tom Callaway <spot@fedoraproject.org> - 2.0.12-2
- delete external directory to drop bundles
- do not own /usr/include/SDL2
- fix unused-direct-shlib-dependency

* Mon Nov 25 2013 Tom Callaway <spot@fedoraproject.org> - 2.0.12-1
- initial package
