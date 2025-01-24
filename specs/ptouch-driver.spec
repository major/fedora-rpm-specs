%global upstream_name printer-driver-ptouch

Name:           ptouch-driver
Version:        1.7.1
Release:        1%{?dist}
Summary:        CUPS driver for Brother P-touch label printers

License:        GPL-2.0-or-later
URL:            https://github.com/philpem/printer-driver-ptouch
Source0:        https://github.com/philpem/printer-driver-ptouch/releases/download/v%{version}/%{upstream_name}-%{version}.tar.gz


# gcc is no longer in buildroot by default (needed for rastertoptch filter)
BuildRequires:  gcc
# uses autosetup
BuildRequires:  git-core
# uses make
BuildRequires:  make
BuildRequires:  cups-devel
BuildRequires:  automake
# ensure we have postscript tags for drivers
BuildRequires:  python3-cups
BuildRequires:  perl(XML::LibXML)
BuildRequires:  libpng-devel
Requires:       cups

%description
This is a CUPS raster filter for Brother P-touch label printers.  It is
meant to be used by the PostScript Description files of the drivers from
the foomatic package.

%package        foomatic
Summary:        Foomatic database data for Brother P-touch label printers
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       foomatic-db >= 4.0-25.20101123.fc15

%description    foomatic
This package contains foomatic database XML entries to generate PPDs
for driving the family of Brother P-touch label printers.

%prep
%autosetup -S git -n %{upstream_name}-%{version}

%build
%set_build_flags

./autogen.sh

# On 64bits, we need to install into lib, not lib64
# (see _cups_serverbin macro from cups-devel)
# and this package for some reason uses libdir
%configure --libdir=%{_prefix}/lib

%make_build

%install
%make_install

%files
%license COPYING
%{_cups_serverbin}/filter/rastertoptch
%doc AUTHORS ChangeLog NEWS README

%files foomatic
%{_datarootdir}/foomatic/db/source/driver/ptouch-*.xml
%{_datarootdir}/foomatic/db/source/printer/Brother-*.xml
%{_datarootdir}/foomatic/db/source/opt/Brother-PT-*.xml
%{_datarootdir}/foomatic/db/source/opt/Brother-PTQL-*.xml
%{_datarootdir}/foomatic/db/source/opt/Brother-QL-*.xml

%changelog
* Wed Jan 22 2025 Zdenek Dohnal <zdohnal@redhat.com> - 1.7.1-1
- 1.7.1 (fedora#2338600)

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Nov 20 2023 Zdenek Dohnal <zdohnal@redhat.com> - 1.7-1
- 2250264 - ptouch-driver-1.7 is available
- SPDX migration
- spec cleanup

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 05 2020 Zdenek Dohnal <zdohnal@redhat.com> - 1.5.1-3
- make is no longer in buildroot by default

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Zdenek Dohnal <zdohnal@redhat.com> - 1.5.1-1
- 1.5.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 14 2019 Jeff Law <law@redhat.com> - 1.3-25
- Fix inline vs static inline issue for gcc-10

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Zdenek Dohnal <zdohnal@redhat.com> - 1.3-21
- gcc is no longer in buildroot by default

* Fri Feb 09 2018 Zdenek Dohnal <zdohnal@redhat.com> - 1.3-20
- remove old stuff

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jan 04 2012 Jiri Popelka <jpopelka@redhat.com> - 1.3-8
- Use _cups_serverbin macro from cups-devel for where to put driver executables.
- Change URL
- modernize spec

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Feb 03 2011 Jiri Popelka <jpopelka@redhat.com> - 1.3-6
- Add PT-2300 model and fix it's BytesPerLine (#560610)

* Wed Jan 19 2011 Jiri Popelka <jpopelka@redhat.com> - 1.3-5
- Use Requires insted of Conflicts

* Wed Jan 19 2011 Jiri Popelka <jpopelka@redhat.com> - 1.3-4
- foomatic sub-package conflicts with foomatic-db < 4.0-25.20101123

* Wed Jan 19 2011 Jiri Popelka <jpopelka@redhat.com> - 1.3-3
- New foomatic sub-package with foomatic database XML entries (#560610)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri May 08 2009 Lubomir Rintel <lkundrak@v3.sk> 1.3-1
- New upstream release

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 13 2008 Lubomir Kundrak <lkundrak@redhat.com> 1.2-9
- Fix build with gcc-4.3

* Wed Aug 22 2007 Lubomir Kundrak <lkundrak@redhat.com> 1.2-8
- Bump revision for BuildID in -debuginfo rebuild

* Fri Aug 3 2007 Lubomir Kundrak <lkundrak@redhat.com> 1.2-7
- Modify the License tag in accordance with the new guidelines

* Fri Aug 3 2007 Lubomir Kundrak <lkundrak@redhat.com> 1.2-6
- No. No automake. For the kids!

* Fri Jul 27 2007 Lubomir Kundrak <lkundrak@redhat.com> 1.2-5
- ...and call it

* Fri Jul 27 2007 Lubomir Kundrak <lkundrak@redhat.com> 1.2-4
- ...the specific version of automake

* Fri Jul 27 2007 Lubomir Kundrak <lkundrak@redhat.com> 1.2-3
- We need automake for patch0 to have effect

* Fri Jul 27 2007 Lubomir Kundrak <lkundrak@redhat.com> 1.2-2
- Install to the right place on 64bit platforms

* Fri Jul 20 2007 Lubomir Kundrak <lkundrak@redhat.com> 1.2-1
- Initial package
