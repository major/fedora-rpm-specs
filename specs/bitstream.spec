Name:           bitstream
Version:        1.5
Release:        15%{?dist}
Summary:        Simpler access to binary structures such as specified by MPEG, DVB, IETF

License:        MIT
URL:            https://code.videolan.org/videolan/bitstream
Source0:        http://download.videolan.org/pub/videolan/bitstream/%{version}/bitstream-%{version}.tar.bz2
BuildArch:      noarch

BuildRequires:  make

%description
biTStream is a set of C headers allowing a simpler access to binary structures
such as specified by MPEG, DVB, IETF, etc.

%package devel
Summary: Simpler access to binary structures such as specified by MPEG, DVB, IETF

%description devel
biTStream is a set of C headers allowing a simpler access to binary structures
such as specified by MPEG, DVB, IETF, etc.


%prep
%autosetup -p1


%build
#Nothing to build


%install
%make_install PREFIX=%{_prefix}



%files devel
%doc AUTHORS NEWS README TODO
%license COPYING
%{_includedir}/bitstream
%{_datadir}/pkgconfig/bitstream.pc


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 08 2018 Nicolas Chauvet <kwizart@gmail.com> - 1.5-1
- Update to 1.5

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 04 2018 Nicolas Chauvet <kwizart@gmail.com> - 1.4-1
- Update to 1.4

* Tue Feb 06 2018 Nicolas Chauvet <kwizart@gmail.com> - 1.3-1
- Update to 1.3

* Thu Sep 14 2017 Nicolas Chauvet <kwizart@gmail.com> - 1.2-1
- Update to 1.2

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Sep 26 2016 Nicolas Chauvet <kwizart@gmail.com> - 1.1-2
- Only create a -devel package
- Remove Group from rpm
- Update license to MIT

* Thu Sep 15 2016 Nicolas Chauvet <kwizart@gmail.com> - 1.1-1
- Update to 1.1

* Mon Jan 16 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.0-1
- Initial spec file

