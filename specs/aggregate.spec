Name:           aggregate
Version:        1.6
Release:        32%{?dist}
Summary:        IPv4 CIDR prefix aggregator

License:        ISC
URL:            http://ftp.isc.org/isc/aggregate/
Source0:        http://ftp.isc.org/isc/aggregate/aggregate-%{version}.tar.gz
Patch0:         aggregate-fedora.patch
Patch1:         aggregate-configure-c99.patch

BuildRequires:         gcc
BuildRequires:         perl-generators
BuildRequires: make

%description
aggregate takes a list of prefixes in conventional format on stdin, 
and performs two optimizations to attempt to reduce the length of 
the prefix list.


%package ios
Summary: Cisco/IOS IPv4 prefix lists aggregator
Requires: aggregate
BuildArch: noarch

%description ios
aggregate-ios takes Cisco IOS configuration on stdin, and optimizes 
any prefix filters found using aggregate.

%prep
%autosetup
chmod -x LICENSE


%build
%configure
%make_build


%install
%make_install


%files
%doc HISTORY
%license LICENSE
%{_bindir}/aggregate
%{_mandir}/man1/aggregate.1.*

%files ios
%{_bindir}/aggregate-ios
%{_mandir}/man1/aggregate-ios.1.*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jul  7 2023 Yanko Kaneti <yaneti@declera.com> - 1.6-27
- SPDX migration - ISC is ISC. Modernize a bit

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 06 2022 Peter Fordham <peter.fordham@gmail.com> - 1.6-25
- Port configure script to C99.

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jul 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-20
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Yanko Kaneti <yaneti@declera.com> 1.6-15
- BR: gcc - https://fedoraproject.org/wiki/Changes/Remove_GCC_from_BuildRoot

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.6-4
- Perl 5.18 rebuild

* Mon May 20 2013 Yanko Kaneti <yaneti@declera.com> 1.6-3
- Make the -ios subpackage noarch

* Fri Dec  9 2011 Yanko Kaneti <yaneti@declera.com> 1.6-2
- Some changes suggested by review comment #1

* Fri May 20 2011 Yanko Kaneti <yaneti@declera.com> 1.6-1
- First attempt at packaging.
