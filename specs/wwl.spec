Summary: Calculates distance and azimuth between two Maidenhead locators
Name: wwl
Version: 1.3
Release: 11%{?dist}
License: wwl
URL: http://www.db.net/downloads/
Source: http://www.db.net/downloads/wwl+db-%{version}.tgz
BuildRequires: gcc
BuildRequires: make

%description
This program combines two handy ham radio Maindensquare programs into one.
When used as locator, it will take the Maindenhead square on the
command line and write it back out as lat / long.
When used as wwl, it will calculate distance and azimuth
between the two Maidenhead squares given.
If only four characters of the Maidenhead square is given, this
program will auto fill in the missing two chars with 'AA'.

%prep
%autosetup -n wwl+db-%{version}

%build
%make_build CFLAGS="%{optflags}"

%install
mkdir -p "%{buildroot}%{_bindir}" "%{buildroot}%{_mandir}/man1"
%make_install PREFIX="%{buildroot}%{_prefix}" MAN1PREFIX="%{buildroot}%{_mandir}/man1/" LN="ln -r"
chmod 0644 %{buildroot}%{_mandir}/man1/wwl.1*

%files
%{_bindir}/*
%{_mandir}/*/*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct  1 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 1.3-2
- Fixed according to the review

* Thu Aug 20 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 1.3-1
- Initial release
