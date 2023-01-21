Name:           ht
Version:        2.1.0
Release:        15%{?dist}
Summary:        File editor/viewer/analyzer for executables

License:        GPL-2.0-only
URL:            https://hte.sourceforge.net/
Source0:        https://downloads.sourceforge.net/hte/ht-%{version}.tar.bz2

Patch1:         ht-2.0.22-format-security.patch
Patch2:         ht-2.1.0-signed-char.patch
Patch3:         ht-2.1.0-uint-abs.patch
Patch4:         ht-2.1.0-gcc10.patch

BuildRequires:  libX11-devel
BuildRequires:  ncurses-devel
BuildRequires:  lzo-devel
BuildRequires:  recode
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make

%description
HT is a file editor/viewer/analyzer for executables. The goal is to combine
the low-level functionality of a debugger and the usability of IDEs. We plan
to implement all (hex-)editing features and support of the most important
file formats.

%prep
%autosetup -p1

recode latin1..utf8 TODO
find . -name \*.cc -o -name \*.h | xargs chmod 0644

%build
%configure --enable-maintainermode
%make_build

%install
%make_install

# rename ht binary to hte, to avoid conflict with tex4ht
mv %{buildroot}%{_bindir}/ht %{buildroot}%{_bindir}/hte

%files
%doc ChangeLog AUTHORS NEWS README TODO KNOWNBUGS
%license COPYING
%{_bindir}/hte

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-10
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 14 2019 Jeff Law <law@redhat.com> - 2.1.0-7
- Fix narrowing conversion problem caught by gcc-10

* Sun Dec 01 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 2.1.0-6
- Revived package. Fixed FTBFS.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 11 2019 Nicolas Chauvet <kwizart@gmail.com> - 2.1.0-1
- Update to 2.1.0 - rhbz#1203552

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.22-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.22-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.22-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.22-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.22-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.22-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.22-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jul 15 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.0.22-4
- Add ht-2.0.22-autotools.patch (Fix F23FTBFS, RHBZ#1239565).
- Modernize spec.
- Add %%license.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 09 2014 Rex Dieter <rdieter@fedoraproject.org> 2.0.22-1
- ht-2.0.22
- fix FTBFS with -Werror=format-security (#1037124)

* Mon Jun 09 2014 Rex Dieter <rdieter@fedoraproject.org> 2.0.18-7
- rename ht binary to hte, avoids conflict with tex4ht (#959696)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.18-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Feb 19 2011 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 2.0.18-1
- version upgrade

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Apr  5 2009 Dan Horák <dan[AT]danny.cz>
- 2.0.16-1
- version update
- added patch for building with gcc 4.4
- remove executable permissions on source files

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Nov 11 2008 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 2.0.15-1
- version upgrade

* Tue Nov 11 2008 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 2.0.14-2
- recode TODO to utf8
- fix permissions on endianess.cc
- honor optflags via non standard maintainer mode

* Wed Sep 03 2008 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 2.0.14-1
- version upgrade
- BR lzo-devel
- use opt flags

* Mon Jan 07 2008 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 2.0.10-1
- version upgrade
- fix source location
- fix license

* Mon Jun 25 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 2.0.8-1
- initial version
