Name:		psftools
Version:	1.0.10
Release:	10%{?dist}
Summary:	Conversion tools for .PSF fonts

License:	GPLv2+
URL:		https://www.seasip.info/Unix/PSF/
Source0:	https://www.seasip.info/Unix/PSF/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires:	gcc

%description
The PSFTOOLS are designed to manipulate fixed-width bitmap fonts, such as DOS
or Linux console fonts. Both the PSF1 (8 pixels wide) and PSF2 (any width)
formats are supported; the default output format is PSF2.


%prep
%setup -q


%build
%configure --disable-shared
make %{?_smp_mflags}


%install
%make_install


%files
%{_bindir}/*
%{_mandir}/man1/*
%exclude %{_includedir}/*.h
%exclude %{_libdir}/*
%doc doc/*.txt
%doc NEWS AUTHORS
%license COPYING


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 17 2018 Lubomir Rintel <lkundrak@v3.sk> - 1.0.10-2
- Dropped Group tag (Robert-André Mauchin, rh#1628148)

* Thu Aug 16 2018 Lubomir Rintel <lkundrak@v3.sk> - 1.0.10-1
- Initial packaging
