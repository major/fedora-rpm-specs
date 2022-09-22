Summary:	Image viewing utility
Name:		gliv
Version:	1.9.7
Release:	29%{?dist}
License:	GPLv2+
URL:		http://guichaz.free.fr/gliv/
VCS:		git://repo.or.cz/gliv.git
Source0:	http://guichaz.free.fr/gliv/files/%{name}-%{version}.tar.bz2
Source1:	gliv.desktop
Source2:	gliv.applications
Patch1:		gliv-0001-Something-is-always-bigger-than-nothing-NULL.patch
BuildRequires:  gcc
BuildRequires:	gtk2-devel >= 2.6.0
BuildRequires:	gtkglext-devel >= 0.7.0
BuildRequires:	desktop-file-utils
BuildRequires: make


%description
GLiv is an OpenGL image viewer. GLiv is very fast and smooth at rotating,
panning and zooming if you have an OpenGL accelerated graphics board.


%prep
%setup -q
%patch1 -p1 -b .fix_comparison_with_null


%build
%configure
make %{?_smp_mflags}


%install
make DESTDIR=%{buildroot} install
%find_lang %{name}

install -D -p -m 0644 %{SOURCE2}  %{buildroot}%{_datadir}/application-registry/gliv.applications

install -D -p -m 0644 gliv.png %{buildroot}%{_datadir}/pixmaps/gliv.png

install -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install \
	--dir %{buildroot}%{_datadir}/applications \
	%{SOURCE1}

%files -f %{name}.lang
%doc COPYING NEWS README THANKS
%{_mandir}/man1/gliv.1*
%{_mandir}/*/man1/gliv.1*
%{_bindir}/gliv
%{_datadir}/applications/*gliv.desktop
%{_datadir}/application-registry/gliv.applications
%{_datadir}/pixmaps/gliv.png


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.7-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.7-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.7-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.7-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.7-25
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.7-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.7-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.7-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.7-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.7-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.7-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.7-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.7-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Aug 11 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.9.7-12
- Don't run autoreconf (F21FTBFS RHBZ#1106645).

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 21 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.9.7-9
- Reconfigure to allow building on AArch64 (rhbz #925427)

* Sun Jul 21 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.9.7-8
- Fixed rhbz #865114 ( https://bugzilla.redhat.com/865114 )
- Cleaned up spec-file

* Thu Apr 11 2013 Jon Ciesla <limburgher@gmail.com> - 1.9.7-7
- Drop desktop vendor tag.

* Sat Jan 26 2013 Ville Skyttä <ville.skytta@iki.fi> - 1.9.7-6
- Desktop entry improvements (#904637).

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.9.7-3
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 15 2011 Peter Lemenkov <lemenkov@gmail.com> - 1.9.7-1
- Ver 1.9.7
- The only patch was dropped (merged upstream)

* Mon Aug 30 2010 Peter Lemenkov <lemenkov@gmail.com> - 1.9.6-6
- Fixed segfault (see rhbz #628224).
- Cleaned up spec-file a little

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Feb  9 2008 Peter Lemenkov <lemenkov@gmail.com> - 1.9.6-3
- Updated version tag.
- Rebuild for GCC 4.3

* Wed Nov 22 2006 Peter Lemenkov <lemenkov@gmail.com> - 1.9.6-2
- Spec cleanup

* Wed Nov 22 2006 Peter Lemenkov <lemenkov@gmail.com> - 1.9.6-1
- Upgrade to ver. 1.9.6
- Missing BR added

* Tue Nov 21 2006 Peter Lemenkov <lemenkov@gmail.com> - 1.9.5-2
- Little cleanups in spec file

* Sun May 28 2006 Adrien BUSTANY <madcat@mymadcat.com> - 1.9.5-1
- Updated to release 1.9.5

* Fri May 27 2005 Dag Wieers <dag@wieers.com> - 1.9.3-1 - 3051+/dag
- Updated to release 1.9.3.

* Tue Mar 22 2005 Dag Wieers <dag@wieers.com> - 1.9.2-1
- Updated to release 1.9.2.

* Wed Jan 05 2005 Dag Wieers <dag@wieers.com> - 1.9.1-1
- Updated to release 1.9.1.

* Thu Aug 05 2004 Dag Wieers <dag@wieers.com> - 1.8.4-1
- Updated to release 1.8.4.

* Thu Jun 24 2004 Dag Wieers <dag@wieers.com> - 1.8.3-1
- Updated to release 1.8.3.

* Sat Feb 07 2004 Dag Wieers <dag@wieers.com> - 1.8.1-0
- Updated to release 1.8.1.

* Sat Jan 24 2004 Dag Wieers <dag@wieers.com> - 1.8-0
- Initial package. (using DAR)
