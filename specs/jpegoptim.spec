
Name:		jpegoptim
Version:	1.5.5
Release:	6%{?dist}
Summary:	Utility to optimize JPEG files

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://www.kokkonen.net/tjko/projects.html

Source0:	https://github.com/tjko/jpegoptim/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:	coreutils
BuildRequires:	gcc
BuildRequires:	libjpeg-devel
BuildRequires:	make

%description
Jpegoptim is an utility to optimize JPEG files. Provides lossless optimization
(based on optimizing the Huffman tables) and "lossy" optimization based on
setting maximum quality factor.


%prep
%setup -q


%build
%configure
%make_build


%install
install -Dpm 0755 jpegoptim %{buildroot}/%{_bindir}/jpegoptim
install -Dpm 0644 jpegoptim.1 %{buildroot}/%{_mandir}/man1/jpegoptim.1


%files
%license COPYRIGHT LICENSE
%doc README
%{_bindir}/jpegoptim
%{_mandir}/man1/*.1*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.5.5-5
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Aug 11 2023 Denis Fateyev <denis@fateyev.com> - 1.5.5-1
- Update to version 1.5.5

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon May 22 2023 Denis Fateyev <denis@fateyev.com> - 1.5.4-1
- Update to version 1.5.4

* Sat Mar 25 2023 Denis Fateyev <denis@fateyev.com> - 1.5.3-1
- Update to version 1.5.3

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 05 2023 Denis Fateyev <denis@fateyev.com> - 1.5.1-1
- Update to version 1.5.1

* Fri Oct 07 2022 Denis Fateyev <denis@fateyev.com> - 1.5.0-1
- Update to version 1.5.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Apr 28 2018 Denis Fateyev <denis@fateyev.com> - 1.4.6-1
- Update to version 1.4.6

* Sat Apr 07 2018 Denis Fateyev <denis@fateyev.com> - 1.4.5-1
- Update to version 1.4.5

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Sep 03 2016 Denis Fateyev <denis@fateyev.com> - 1.4.4-1
- Update to version 1.4.4
- Remove unneeded error handling patch

* Sat Feb 20 2016 Denis Fateyev <denis@fateyev.com> - 1.4.3-4
- Added detailed error handling patch
- Modernized the package spec

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 19 2015 Denis Fateyev <denis@fateyev.com> - 1.4.3-1
- Update to version 1.4.3

* Tue Dec 23 2014 Denis Fateyev <denis@fateyev.com> - 1.4.2-1
- Update to version 1.4.2

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Denis Fateyev <denis@fateyev.com> - 1.4.1-1
- Update to version 1.4.1

* Sat May 03 2014 Denis Fateyev <denis@fateyev.com> - 1.3.1-1
- Update to version 1.3.1

* Tue Jan 07 2014 Denis Fateyev <denis@fateyev.com> - 1.3.0-1
- Initial Fedora RPM package
