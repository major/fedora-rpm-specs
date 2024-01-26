%global git_tag f16f247d30f868e84f31e24792b4464488f1c009
%global short_tag %(c=%{git_tag}; echo ${c:0:7})

Summary:        Uncompress the Apple compressed disk image files
Name:           dmg2img
Version:        1.6.7
Release:        19.20170502.git.f16f247%{?dist}
# dmg2img is GPL without specific version
# vfdecrypt is MIT licensed
License:        GPL+ and MIT
#Source0:        http://vu1tur.eu.org/tools/%{name}-%{version}.tar.gz
Source0:        https://github.com/Lekensteyn/%{name}/archive/%{git_tag}/%{name}-%{version}.git.tar.gz
URL:            http://vu1tur.eu.org/tools/
BuildRequires:  gcc
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)
BuildRequires: make


%description
This package contains dmg2img utility that is able to uncompress compressed dmg
files into plain disk or filesystem images.


%prep
%autosetup -p1 -n %{name}-%{git_tag}


%build
make CC="%{__cc}" CFLAGS="%{optflags}" %{_smp_mflags}


%install
install -D -p -m 0755 dmg2img %{buildroot}%{_bindir}/dmg2img
install -D -p -m 0755 vfdecrypt %{buildroot}%{_bindir}/vfdecrypt
install -D -p -m 0644 vfdecrypt.1 %{buildroot}%{_mandir}/man1/vfdecrypt.1


%files
%license COPYING
%doc README
%{_bindir}/dmg2img
%{_bindir}/vfdecrypt
%{_mandir}/man1/vfdecrypt.1*


%changelog
* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.7-19.20170502.git.f16f247
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.7-18.20170502.git.f16f247
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.7-17.20170502.git.f16f247
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.7-16.20170502.git.f16f247
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.7-15.20170502.git.f16f247
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.7-14.20170502.git.f16f247
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.6.7-13.20170502.git.f16f247
- Rebuilt with OpenSSL 3.0.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.7-12.20170502.git.f16f247
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.7-11.20170502.git.f16f247
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct 26 2020 Peter Lemenkov <lemenkov@gmail.com> - 1.6.7-10.20170502.git.f16f247
- Fix building with OpenSSL 1.1

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 30 2017 Peter Lemenkov <lemenkov@gmail.com> - 1.6.7-1
- Ver. 1.6.7

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Nov 16 2014 Peter Lemenkov <lemenkov@gmail.com> - 1.6.5-1
- Ver. 1.6.5

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jan 09 2012 Lubomir Rintel <lkundrak@v3.sk> - 1.6.2-2
- Add a missing BR (Richard Shaw, #749752)
- Cosmetic fixes (Scott Tsai, #749752)

* Fri Oct 29 2011 Lubomir Rintel <lkundrak@v3.sk> - 1.6.2-1
- Initial packaging
