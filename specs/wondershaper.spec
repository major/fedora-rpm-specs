Name:		wondershaper
Version:	1.2.1
Release:	24%{?dist}
Summary:	Simple Network Shaper
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://sourceforge.net/projects/wondershaper/
Source:		http://downloads.sourceforge.net/project/wondershaper/%{name}-%{version}.tar.gz
Requires:	iproute
Requires:	kernel-modules-extra
BuildArch:	noarch

%description
Many cable-modem and ADSL users experience horrifying latency
while uploading or downloading. They also notice that uploading
hampers downloading greatly. The Wondershaper neatly addresses
these issues, allowing users of a router with a Wondershaper to
continue using SSH over a loaded link happily.

%prep
%setup -q

%build
# Nothing to build.

%install
install -pDm 755 wshaper %{buildroot}/%{_sbindir}/%{name}

%files
%doc ChangeLog README
%license COPYING
%{_sbindir}/%{name}

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.2.1-23
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Aug 8 2015 Mosaab Alzoubi <moceap@hotmail.com> - 1.2.1-5
- Fix #1209243
- Use %%license

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Nov 20 2013 Mosaab Alzoubi <moceap@hotmail.com> - 1.2.1-2
- Fix package git commit.

* Tue Nov 19 2013 Mosaab Alzoubi <moceap@hotmail.com> - 1.2.1-1
- Update to 1.2.1 .
- Replace URL with main program page.
- General tweaks.
- Remove VERSION file from %%doc.

* Fri Oct 18 2013 Mosaab Alzoubi <moceap@hotmail.com> - 1.2-3
- Remove permissions line.

* Fri Oct 18 2013 Mosaab Alzoubi <moceap@hotmail.com> - 1.2-2
- To zero warnings by rpmlint.

* Thu Oct 10 2013 Mosaab Alzoubi <moceap@hotmail.com> - 1.2-1
- NG of wondershaper , update to version 1.2 

* Thu Oct 10 2013 Mosaab Alzoubi <moceap@hotmail.com> - 1.1a-6
- Fixes to be compatible with Fedora rules.

* Sun Sep 23 2012 Muhammad Shaban <Mr.Muhammad@linuxac.org> - 1.1a-5.1
- Initial build for Kenzi.

* Thu Aug 7 2008 Marek Mahut <mmahut@fedoraproject.org> - 1.1a-2
- Initial package release.
