%define         repoid           6183
%define		_default_patch_fuzz	2

Name:           manedit
Version:        1.2.1
Release:        35%{?dist}
Summary:        UNIX Manual Page Editor

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
#URL:            http://wolfpack.twu.net/ManEdit/
URL:            http://freshmeat.net/projects/manedit/
#Source0:        http://wolfpack.twu.net/users/wolfpack/%{name}-%{version}.tar.bz2
Source0:        http://freshmeat.net/redir/manedit/%{repoid}/url_bz2/manedit-%{version}.tar.bz2
Source1:        manedit.desktop
Source2:        manview.desktop
Patch0:         manedit-0.7.1-makefile.patch
Patch1:         manedit-1.2.1-more-manpages.patch
Patch4:		manedit-1.1.1-fix-compilation.patch
Patch5:		manedit-1.1.1-fix-segv-on-manview.patch
Patch6:		manedit-1.1.1-tmpdir.patch
Patch7:		manedit-1.1.1-fix-segv-on-refresh-with-selected.patch

# This is gtk+ package
BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires:  gtk+-devel
BuildRequires:  zlib-devel
BuildRequires:  bzip2-devel
BuildRequires:  desktop-file-utils
Requires:       man-db
Requires:	xorg-x11-fonts-ISO8859-15-100dpi

%description
ManEdit is a UNIX manual page editor and viewer, 
it is designed specifically for the editing of the 
UNIX manual page format using an integrated XML interface.

NOTE: This is a gtk+ package and some characters,
especially UTF-8 characters will be garbled.

%prep
%setup -q

# Base Makefile on FreeBSD style
%{__cp} -p ./manedit/Makefile.FreeBSD ./manedit/Makefile
%patch -P0 -p1 -b .fedora
%patch -P4 -p1 -b .compile
%patch -P1 -p1 -b .manpages
%patch -P5 -p1 -b .segv_manview
%patch -P6 -p1 -b .tmpdir
%patch -P7 -p1 -b .segv_refresh

%build
# I cannot understand this configure!!
#%%configure

pushd manedit
%{__make} %{?_smp_mflags} -k \
   CC="gcc -Werror-implicit-function-declaration" \
   OPTFLAGS="$RPM_OPT_FLAGS -DHAVE_GZIP -DHAVE_BZIP2" \
   LDFLAGS="-lz -lbz2"
%{__make} manedit.1.out ; %{__mv} -f manedit.1.out manedit.1
popd

%install
%{__rm} -rf $RPM_BUILD_ROOT

pushd manedit
%{__mkdir_p} $RPM_BUILD_ROOT%{_prefix}
%{__make} install PREFIX=$RPM_BUILD_ROOT%{_prefix}

# remove manwrap
%{__rm} -f $RPM_BUILD_ROOT%{_bindir}/manwrap

desktop-file-install \
%if 0%{?fedora} && 0%{?fedora} < 19
   --vendor fedora \
%endif
   --dir $RPM_BUILD_ROOT%{_datadir}/applications \
   %{SOURCE1} \
   %{SOURCE2}

# install icons
# size 20 don't seems to be owned by hicolor-icon-theme
for size in 32x32 48x48; do
   %{__install} -D -c -p -m 644 images/icon_manedit_${size}.xpm \
      $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${size}/apps/manedit.xpm
done

for size in 16x16 48x48 ; do
   %{__install} -D -c -p -m 644 images/icon_manedit_viewer_${size}.xpm \
      $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${size}/apps/manedit_viewer.xpm
done
%{__rm} -rf $RPM_BUILD_ROOT%{_datadir}/pixmaps/

popd

%files
%doc AUTHORS LICENSE README

%{_bindir}/man*

%{_datadir}/icons/hicolor/*/apps/*.xpm
%{_datadir}/applications/*.desktop

%{_datadir}/%{name}/
%{_mandir}/man1/%{name}.1*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 1.2.1-34
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.1-18
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.2.1-12
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 1.2.1-8
- Remove --vendor from desktop-file-install https://fedorahosted.org/fesco/ticket/1077

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-7.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-6.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-5.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-4.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jul 13 2010 Mike McGrath <mmcgrath@redhat.com> - 1.2.1-3.1
- Rebuilt against man-db to fix broken dep

* Sat Jul 25 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.2.1-3
- F-12: Mass rebuild

* Tue Feb 24 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.2.1-2
- GTK icon cache updating script update

* Thu Oct 16 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.2.1-1
- 1.2.1

* Fri Aug 29 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.1.1-3
- Use gcc instead of %%__cc
  (On F-10+ %%__cc is expanded as "gcc -std=c99" and using glib headers
   fails with this)

* Thu Jul  3 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.1.1-2
- Modify tmpdir.patch: to fix segv on the exit of manview
- Fix segv on refresh on manview when one item is selected

* Mon Jun 30 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.1.1-1
- 1.1.1
- Seems that URL are moved temporarily
- Fix segv on clicking "Index" on manview
- Fix potentially insecure tmpdir creation

* Fri Apr  4 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.8.1-3
- Fix implicit function declaration

* Sat Feb  9 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- Rebuild against gcc43 (F-9)

* Mon Dec 17 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.8.1-2
- Revert change from 0.7.1 to fix segv when pushed new button
  (bug 356171)

* Wed Aug 22 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.8.1-1.dist.3
- Mass rebuild (buildID or binutils issue)

* Fri Aug  3 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.8.1-1.dist.2
- License update

* Sun Feb 11 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.8.1-1
- 0.8.1

* Sat Nov 11 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.7.1-5
- Remove some warnings.

* Thu Nov  2 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.7.1-4
- Add a comment about gtk+ issue on %%description.

* Tue Oct 31 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.7.1-3
- Install manview desktop, related icons.
- Change Requires.
- Remove manwrap

* Sun Oct 29 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.7.1-2
- Improve Makefile and mandir treatments, patches from Patrice Dumas.
- Make man page.
- Correct install directory.

* Sat Oct 28 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.7.1-1
- Re-submit to Fedora Extras.

* Thu Apr 14 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.5.11-5
- Fix build for GCC4.

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Wed Feb  9 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0:0.5.11-3
- Add patch for multilib and substitute hardcoded 'lib' in %%prep.
- Add patch to disable stripping.

* Wed Nov 17 2004 Michael Schwendt <mschwendt[AT]users.sf.net> - 0:0.5.11-2
- BR bzip2-devel + patch to enable bzip2, bump release

* Sat Oct 3 2004 Nils O. Selåsdal <NOS@Utel.no> - 0:0.5.11-0.fdr.1
- Update to 0.5.11

* Thu Oct 2 2003 Nils O. Selåsdal <NOS@Utel.no> - 0:0.5.10-0.fdr.2
- Put .desktop in its own file
- Save .spec file as utf-8
- use mainstream tar.bz2 instead of tgz

* Wed Aug 27 2003 Nils O. Selåsdal <NOS@Utel.no> - 0:0.5.10-0.fdr.1
- Initial RPM for Fedora
