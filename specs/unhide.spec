%global srcname Unhide
Name:           unhide
Version:        20220611
Release:        4%{?dist}
Summary:        Tool to find hidden processes and TCP/UDP ports from rootkits
License:        GPL-3.0-only
URL:            http://www.unhide-forensics.info/
Source0:        http://github.com/YJesus/%{srcname}/archive/v%{version}/%{srcname}-v%{version}.tar.gz

BuildRequires: gcc

%description
Unhide is a forensic tool to find hidden processes and TCP/UDP ports by 
rootkits/LKMs or by another hiding technique.

%prep
%autosetup -n %{srcname}-%{version}
chmod -x sanity*.sh

%build
%{__cc} %{optflags} -lpthread unhide-linux*.c unhide-output.c -o unhide %{?__global_ldflags}
%{__cc} %{optflags} unhide-tcp.c unhide-tcp-fast.c unhide-output.c -o unhide-tcp %{?__global_ldflags}
%{__cc} %{optflags} unhide_rb.c -o unhide_rb %{?__global_ldflags}

%install
mkdir -p %{buildroot}%{_sbindir}/
mkdir -p %{buildroot}%{_mandir}/man8/
mkdir -p %{buildroot}%{_mandir}/es/man8/
mkdir -p %{buildroot}%{_mandir}/fr/man8/
install -pm0755 unhide %{buildroot}%{_sbindir}/
install -pm0755 unhide-tcp %{buildroot}%{_sbindir}/
install -pm0755 unhide_rb %{buildroot}%{_sbindir}/
install -pm0644 man/unhide.8 %{buildroot}%{_mandir}/man8/
install -pm0644 man/unhide-tcp.8 %{buildroot}%{_mandir}/man8/
install -pm0644 man/es/unhide.8 %{buildroot}%{_mandir}/es/man8
install -pm0644 man/es/unhide-tcp.8 %{buildroot}%{_mandir}/es/man8/
install -pm0644 man/fr/unhide.8 %{buildroot}%{_mandir}/fr/man8/
install -pm0644 man/fr/unhide-tcp.8 %{buildroot}%{_mandir}/fr/man8/

%files
%doc changelog README.txt NEWS sanity.sh sanity-tcp.sh
%license COPYING LICENSE
%{_mandir}/man8/unhide*.8*
%{_mandir}/es/man8/unhide*.8*
%{_mandir}/fr/man8/unhide*.8*
%{_sbindir}/unhide
%{_sbindir}/unhide-tcp
%{_sbindir}/unhide_rb

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 20220611-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20220611-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20220611-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Robby Callicotte <rcallicotte@fedoraproject.org> - 20220611-1
- Rebased to new version

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20130526-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20130526-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20130526-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20130526-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20130526-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20130526-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20130526-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20130526-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20130526-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20130526-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 20130526-10
- Add gcc as BR (minimal buildroot change)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20130526-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20130526-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20130526-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20130526-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20130526-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130526-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130526-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130526-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 09 2014 Christopher Meng <rpm@cicku.me> - 20130526-1
- Update to 20130526
- Add multilingual manpages.
- SPEC cleanup, build with RELRO.

* Fri Jul 26 2013 Parag <paragn AT fedoraproject DOT org> - 1.0-10.20121229
- Update to new version

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-9.20100201
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-8.20100201
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-7.20100201
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-6.20100201
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon May 03 2010 Rakesh Pandit <rakesh@fedoraproject.org> 1.0-5.20100201
- Updated to 20100201

* Fri Dec 04 2009 Rakesh Pandit <rakesh@fedoraproject.org> 1.0-5.20090810
- Updated to 20090810

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-4.20080519
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-3.20080519
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 08 2009 Rakesh Pandit <rakesh@fedoraproject.org> 1.0-2
- clarified from upstream about license - fixed.

* Sat Dec 06 2008 Rakesh Pandit <rakesh@fedoraproject.org> 1.0-1
- Fixed %%Version and %%Release fields.

* Fri Nov 07 2008 Rakesh Pandit <rakesh@fedoraproject.org> 20080519-2
- Clear %%install, consistency of macro use

* Tue Nov 04 2008 Rakesh Pandit <rakesh@fedoraproject.org> 20080519-1
- Initial package
