Name:           fswebcam
Version:        20200725
Release:        12%{?dist}
Summary:        Tiny and flexible webcam program

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://www.sanslogic.co.uk/fswebcam/
Source0:        %{url}files/%{name}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  gd-devel
BuildRequires:  make

%description
A tiny and flexible webcam program for capturing images from a V4L1/V4L2
device, and overlaying a caption or image.

%prep
%autosetup

%build
%configure
%make_build

%install
%make_install

%files
%doc CHANGELOG README LICENSE example.conf
%{_mandir}/man*/%{name}*.*
%{_bindir}/%{name}

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 20200725-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 20200725-11
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20200725-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20200725-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20200725-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20200725-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20200725-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20200725-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20200725-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20200725-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20200725-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 19 2021 Fabian Affolter <mail@fabian-affolter.ch> - 20200725-1
- Update URL (#1917620)
- Update to latest upstream release 20200725

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20140113-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20140113-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20140113-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20140113-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20140113-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20140113-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20140113-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20140113-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20140113-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20140113-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20140113-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20140113-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20140113-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jan 14 2014 Fabian Affolter <mail@fabian-affolter.ch> - 20140113-1
- Update to new upstream version 20140113

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20110717-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 26 2013 Fabian Affolter <mail@fabian-affolter.ch> - 20110717-6
- Spec file updated

* Tue Jun 11 2013 Remi Collet <rcollet@redhat.com> - 20110717-5
- Rebuild for new GD 2.1.0

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20110717-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20110717-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20110717-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jul 18 2011 Fabian Affolter <mail@fabian-affolter.ch> - 20110717-1
- Update to new upstream version 20110717

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20101118-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Nov 18 2010 Fabian Affolter <mail@fabian-affolter.ch> - 20101118-1
- Remove patches, they are upstream
- Update to new upstream version 20101118

* Tue Aug 31 2010 Fabian Affolter <mail@fabian-affolter.ch> - 20100622-2
- Added patch acc. upstream commit 05ea39c7e4ad3386c326171287bf7f9dd46d680e
  to fix #603849

* Tue Jun 22 2010 Fabian Affolter <mail@fabian-affolter.ch> - 20100622-1
- Update to new upstream version 20100622

* Thu Apr 08 2010 Fabian Affolter <mail@fabian-affolter.ch> - 20100405-1
- Update to new upstream version 20100405

* Thu Dec 24 2009 Fabian Affolter <mail@fabian-affolter.ch> - 20091224-1
- Update to new upstream version 20091224

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20070108-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20070108-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Dec 27 2008 Fabian Affolter <mail@fabian-affolter.ch> - 20070108-3
- General update for a new Review request

* Mon Oct 01 2007 Philip Heron <phil@sanslogic.co.uk> - 20070108-2
- Update license to GPL2 and removed gd > 2 requirement.

* Tue Jan 09 2007 Philip Heron <phil@sanslogic.co.uk> - 20070108-1
- Update for latest release.

* Sun Dec 10 2006 Philip Heron <phil@firestorm.cx> - 20061210-1
- Add example configuration.

* Fri Apr 28 2006 Philip Heron <phil@firestorm.cx> - 20060424-1
- Update package description, and group.

* Wed Feb 22 2006 Philip Heron <phil@firestorm.cx>
- Update spec to use configure script and cleaned up.
