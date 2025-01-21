%define __cmake_in_source_build 1

Name:           sdcv
Version:        0.5.4
Release:        7%{?dist}
Summary:        Console version of StarDict program
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://sdcv.sourceforge.net/
Source0:        http://github.com/Dushistov/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz


BuildRequires: make
BuildRequires:  cmake gcc-c++
BuildRequires:  zlib-devel  glib2-devel gettext-devel
BuildRequires:  readline-devel

%description
SDCV is simple, cross-platform text-base utility for work with
dictionaries in StarDict's format.

%description -l ru
SDCV - простая, консольная утилита работы 
со словарям в формате StarDict

%prep
%setup -q

%build
%cmake .
make %{?_smp_mflags}
make lang %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
%find_lang %{name}

%files -f %{name}.lang
%doc NEWS LICENSE AUTHORS README.org
%{_bindir}/%{name}
%{_mandir}/man1/sdcv.1.gz
%{_mandir}/uk/man1/sdcv.1.gz

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.5.4-6
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Aug 21 2022 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 0.5.4-1
- Update to 0.5.4 (#2120029)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 22 2020 Jeff Law <law@redhat.com> - 0.5.2-4
- Use cmake_in_source_build to fix FTBFS due to recent cmake macro changes

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Mar 31 2020 Artem Egorenkov <aegorenk@redhat.com> - 0.5.2-1
- version updated to 0.5.2

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.1-9
- Rebuild for readline 8.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Björn Esser <besser82@fedoraproject.org> - 0.5.1-7
- Append curdir to CMake invokation. (#1668512)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug  7 2017 Pavel Zhukov <pzhukov@redhat.com> - 0.5.1-3
- Proper use of cmake macros

* Mon Aug  7 2017 Pavel Zhukov <pzhukov@redhat.com> - 0.5.1-1
- New release 0.5.1

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.4.2-18
- Rebuild for readline 7.x

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.4.2-15
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 17 2013 Pavel Zhukov <landgraf@fedoraproject.org> - 0.4.2-11
- Support for the ARM 64 bit CPU architecture (aarch64) 

* Fri Mar 15 2013 Pavel Zhukov <landgraf@fedoraproject.org> - 0.4.2-10
- Fix build with gcc-4.8

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed May 11 2011 Pavel Zhukov <landgraf@fedoraproject.org> - 0.4.2-6
- Increment release number to become AutoQA happy

* Sat May 07 2011 Pavel Zhukov <landgraf@fedoraproject.org> - 0.4.2-5
- Enable readline support 
- Thank to Vadim V. Raskhozhev <iamdexpl@gmail.com>

* Thu Jan 12 2011 Pavel Zhukov <landgraf@fedoraproject.org> - 0.4.2-4
- fixed License tag

* Wed Jan 12 2011 Pavel Zhukov <landgraf@fedoraproject.org> - 0.4.2-3
- rename patchs for better legibity
- fixed doc section 

* Fri Dec 31 2010 Pavel Zhukov <landgraf@fedoraproject.org> - 0.4.2-2
- some minor bugfixes and gettext patch

* Thu Dec 30 2010 Pavel Zhukov <landgraf@fedoraproject.org> - 0.4.2-1
- Initial package
- version 0.4.2

