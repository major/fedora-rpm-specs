Name:           sl
Version:        5.02
Release:        23%{?dist}
Summary:        Joke command for when you type 'sl' instead of 'ls'
License:        SL
URL:            https://github.com/mtoyoda/sl
Source0:        https://github.com/mtoyoda/sl/archive/%{version}/sl-%{version}.tar.gz
BuildRequires: make
BuildRequires:  ncurses-devel, gcc

# Copyright file is taken from the Debian project
# http://packages.debian.org/changelogs/pool/main/s/sl/sl_3.03-14/sl.copyright
# and has been confirmed with the original author.

%description
The sl (Steam Locomotive) command is a joke which displays a train on your
terminal when you accidentally type 'sl' instead of 'ls'.


%prep
%setup -q

%build
make %{?_smp_mflags} CFLAGS="%{optflags}"


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
install -m0755 sl %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{_mandir}/man1
install -p -m644 sl.1 %{buildroot}%{_mandir}/man1/
mkdir -p %{buildroot}%{_mandir}/ja/man1
install -p -m644 sl.1.ja %{buildroot}%{_mandir}/ja/man1/


%files
%doc README.ja.md README.md LICENSE
%{_mandir}/ja/man1/*
%{_mandir}/man1/*
%{_bindir}/sl


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.02-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.02-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.02-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.02-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.02-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.02-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.02-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.02-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.02-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.02-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Feb 07 2020 Vojtech Trefny <vtrefny@redhat.com> - 5.02-13
- Remove libtermcap-devel from BuildRequires

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.02-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.02-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.02-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.02-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Matěj Cepl <mcepl@redhat.com> - 5.02-8
- Add gcc as BuildRequires.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.02-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.02-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.02-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.02-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.02-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Dec 05 2014 Matej Cepl <mcepl@redhat.com> - 5.02-1
- Update to the new upstream (and new build system; #1170931)

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.03-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.03-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.03-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.03-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 27 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.03-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.03-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.03-11
- Rebuilt for glibc bug#747377

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.03-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.03-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.03-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Nov 18 2008 Tom "spot" Callaway <tcallawa@redhat.com> 3.03-7
- fix license tag (Freely redistributable without restriction is only
  for firmware)

* Sun Oct 26 2008 Marc Bradshaw <packages@marcbradshaw.co.uk> 3.03-6
- Moved man file to japanese language directory

* Sat Oct 25 2008 Marc Bradshaw <packages@marcbradshaw.co.uk> 3.03-5
- Cleanup of spec file

* Wed Oct 15 2008 Marc Bradshaw <packages@marcbradshaw.co.uk> 3.03-4
- Cleanup of spec file

* Wed Oct 15 2008 Marc Bradshaw <packages@marcbradshaw.co.uk> 3.03-3
- Update Licence
- Update COPYRIGHT to include statement from author confirming licence
- Full statement may be found at the following URL
- http://marcbradshaw.co.uk/packages/review/sl/sl-license-mail.txt

* Thu Aug 09 2007 Marc Bradshaw <packages@marcbradshaw.co.uk> 3.03-2
- Clean of spec file

* Thu Jul 12 2007 Marc Bradshaw <packages@marcbradshaw.co.uk> 3.03-1
- Initial package release
