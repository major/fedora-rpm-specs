Name:		datefudge
Version:	1.24
Release:	5%{?dist}
Summary:	Fake the system date

License:	GPLv2+
URL:		http://packages.qa.debian.org/d/datefudge.html
Source0:	http://cdn.debian.net/debian/pool/main/d/datefudge/%{name}_%{version}.tar.xz

BuildRequires:  gcc
BuildRequires: make
%description
This program (and preload library) fakes the system date so that 
programs think the wall clock is ... different. The faking is not 
complete; time-stamp on files are not affected in any way. This 
package is useful if you want to test the date handling of your 
programs without changing the system clock. 

%prep
%autosetup -p1
sed "s/VERSION := \$\(.*\)/VERSION := %{version}/g" -i Makefile
sed 's/-o root -g root/-p/g' -i Makefile

%build
LDFLAGS="%{__global_ldflags}" CFLAGS="%{optflags}" make libdir=%{_libexecdir} %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} libdir=%{_libexecdir}
chmod +x %{buildroot}/%{_libexecdir}/%{name}/datefudge.so #for stripping

%files
%{_libexecdir}/%{name}

%doc README COPYING
%{_mandir}/man1/datefudge.1*
%{_bindir}/datefudge

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct 12 2020 Nikos Mavrogiannopoulos <nmav@redhat.com> - 1.24-1
- New upstream release

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 11 2020 Nikos Mavrogiannopoulos <nmav@redhat.com> - 1.23-1
- New upstream release

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Aug 11 2017 Nikos Mavrogiannopoulos <nmav@redhat.com> - 1.22-1
- New upstream release

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Sep  2 2016 Nikos Mavrogiannopoulos <nmav@redhat.com> - 1.21-1
- New upstream release

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Dec  3 2014 Nikos Mavrogiannopoulos <nmav@redhat.com> - 1.20-1
- New upstream release

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Nov 18 2013 Nikos Mavrogiannopoulos <nmav@redhat.com> - 1.18-2
- Removed support for EL5
- Apply build LDFLAGS and CFLAGS.

* Wed Nov 13 2013 Nikos Mavrogiannopoulos <nmav@redhat.com> - 1.18-1
- Initial version of the package
