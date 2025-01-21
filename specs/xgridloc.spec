Name:		xgridloc
Version:	1.8.4
Release:	11%{?dist}
Summary:	A GTK+ application for the calculation of Maidenhead QRA Locators

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:	GPL-3.0-only
URL:		https://www.qsl.net/5b4az/

Source0:        https://www.qsl.net/5b4az/pkg/locator/%{name}/%{name}-%{version}.tar.bz2

# desktop file
Source1:	%{name}.desktop
Patch0: xgridloc-configure-c99.patch


BuildRequires:	make
BuildRequires:	gcc-c++
BuildRequires:	desktop-file-utils
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	glib2-devel
BuildRequires:	gtk3-devel

%description
xgridloc is a GTK+ graphical version of gridloc and performs the same basic
functions for ham radio operators, but additionally it can use xplanet to
display the home and DX locations and the great circle path between them.

%prep
%autosetup -p1


%build
./autogen.sh
%configure
%make_build


%install
%make_install

mkdir -p %{buildroot}%{_datadir}/pixmaps/
ln -rs %{buildroot}%{_datadir}/%{name}/%{name}.svg %{buildroot}%{_datadir}/pixmaps/%{name}.svg

# no upstream .desktop so we'll use a temporary one
desktop-file-install  \
	--dir=%{buildroot}%{_datadir}/applications %{SOURCE1}


%files
%doc AUTHORS NEWS README doc/%{name}.html
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.svg
%{_mandir}/man1/%{name}.1*


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul  29 2024 Miroslav Suchý <msuchy@redhat.com> - 1.8.4-10
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 11 2023 Florian Weimer <fweimer@redhat.com> - 1.8.4-5
- Port configure script to C99 (#2160018)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 19 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 1.8.4-1
- New version
  Resolves: rhbz#1983096

* Sun Jul 11 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 1.8.3-2
- Installed .glade file and icon system wide

* Thu Jul  8 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 1.8.3-1
- New version
- Simplified the SPEC file

* Wed Jul  7 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 1.8.2-32
- Fixed no_home patch
  Resolves: rhbz#1965709
- SPEC file cleanup

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 29 2019 Richard Shaw <hobbes1069@gmail.com> - 1.8.2-1
- Update to 1.8.2.

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.9-13
- Rebuild for new libpng

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Apr 30 2010 Randall J. Berry 'Dp67' <dp67@fedoraproject.org> - 0.9-11
- recommit

* Fri Apr 30 2010 Randall J. Berry 'Dp67' <dp67@fedoraproject.org> - 0.9-10
- fix .desktop add Network;

* Thu Apr 22 2010 Jon Ciesla <limb@jcomserv.net> - 0.9-9
- Fix for libm DSO Linking FTBFS, BZ 565163.

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 9 2009 Randall J. Berry 'Dp67' <dp67@fedoraproject.org> - 0.9-6
- Upstream source added COPYING file
- Fix .desktop file removed ext from icon
- Mock build f11/devel i386
- Test build on Koji all arches

* Fri Feb 6 2009 Randall J. Berry 'Dp67' <dp67@fedoraproject.org> - 0.9-5
- bump src to f11
- minor spec edits

* Sun Jan 18 2009 Randall J. Berry 'Dp67' <dp67@fedoraproject.org> - 0.9-4
- Check rpmlint fix lint errors
- 3 packages and 1 specfiles checked; 0 errors, 0 warnings.
- Submit for review
- Mock build f9/10/devel i386
- Test build on Koji all arches

* Sun Jan 18 2009 Randall J. Berry 'Dp67' <dp67@fedoraproject.org> - 0.9-3
- Add default config file
- Mock build f9/10/devel i386

* Sun Jan 18 2009 Randall J. Berry 'Dp67' <dp67@fedoraproject.org> - 0.9-2
- Mock build f9/10/devel i386

* Wed Jan 14 2009 Randall J. Berry 'Dp67' <dp67@fedoraproject.org> - 0.9-1
- Upstream upgrade to 0.9
- rpmbuild F9 i386

* Sat Mar 01 2008 Robert 'Bob' Jensen <bob@bobjensen.com> - 0.7-1
- Initial spec
