%global rel 20200705.2a7d4a2

Name:           agedu
Version:        0
Release:        32.%{rel}%{?dist}
Summary:        An utility for tracking down wasted disk space
License:        MIT
URL:            http://www.chiark.greenend.org.uk/~sgtatham/agedu/
# Upstream tarball is regenerated nightly, so md5sums will differ.
Source0:        http://www.chiark.greenend.org.uk/~sgtatham/agedu/agedu-%{rel}.tar.gz

BuildRequires:  gcc
BuildRequires: make

%description
Agedu is a program that helps you to track down wasted disk space by creating
a graphical representation of last access times and occupied disk space of
files and directories.

%prep
%setup -q -n %{name}-%{rel}

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%doc LICENCE TODO
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0-32.20200705.2a7d4a2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-31.20200705.2a7d4a2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-30.20200705.2a7d4a2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-29.20200705.2a7d4a2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-28.20200705.2a7d4a2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-27.20200705.2a7d4a2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-26.20200705.2a7d4a2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-25.20200705.2a7d4a2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-24.20200705.2a7d4a2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-23.20200705.2a7d4a2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 05 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 0-22.0200705.2a7d4a2
- Update to 20200705.2a7d4a2.

* Fri Jul 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-21.20171202.8a8299e
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-20.20171202.8a8299e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-19.20171202.8a8299e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-18.20171202.8a8299e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-17.20171202.8a8299e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-16.20171202.8a8299e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 28 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 0-15.20171202.8a8299e
- Update to 20171202.8a8299e.
- Added gcc buildrequires.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-14.r9153
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-13.r9153
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-12.r9153
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-11.r9153
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-10.r9153
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-9.r9153
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-8.r9153
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-7.r9153
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-6.r9153
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-5.r9153
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-4.r9153
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-3.r9153
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Apr 28 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0-2.r9153
- Update to upstream r9153.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-2.r8928
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 07 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0-1.r8928
- Update to upstream r8928.

* Sun Dec 27 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0-1.r8768
- Update to upstream r8768.

* Tue Sep 22 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0-1.r8642
- Update to upstream r8642.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-2.r8442
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu May 21 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0-1.r8442
- First release. 
