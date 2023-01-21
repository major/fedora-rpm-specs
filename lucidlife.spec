Name:           lucidlife
Version:        0.9.2
Release:        32%{?dist}
Summary:        A Conway's Life simulator

License:        GPLv2+
URL:            http://linux.softpedia.com/get/GAMES-ENTERTAINMENT/Simulation/LucidLife-26633.shtml
Source0:        http://mirror.thecodergeek.com/src/lucidlife-0.9.2.tar.gz
Patch1: 	%{name}-fix-FSF-address.patch
Patch2: 	%{name}-printf-format-security.patch

BuildRequires:  gcc
BuildRequires:  gtk2-devel >= 2.6.0
BuildRequires:	gnome-vfs2-devel
BuildRequires:	desktop-file-utils
BuildRequires:	perl(XML::Parser)
BuildRequires:	gettext	
BuildRequires: make

%description
LucidLife is a Conway's Life simulator. The rules are rather simple. The game
is started with a large grid of cell locations, and an arbitrary set of
living cells. On each turn, each cell thrives or dies based on the number of 
cells which surround it. A dead (empty) cell with three live cells around it
becomes a living cell (a birth); a living cell with two or three neighbors
survives; otherwise the cell dies (due to overcrowding) or remains dead
(due to loneliness). It is based on the the GtkLife project, but with a
more modern user interface and other enhancements.


%prep
%setup -q
%patch1 -p0 -b .fix-FSF-address
%patch2 -p0 -b .printf-format-security


%build
autoconf
%configure LDFLAGS='-lX11'
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
%find_lang %{name}
desktop-file-install \
	--dir %{buildroot}%{_datadir}/applications	\
	--delete-original	\
	--remove-category=Application	\
	--add-category=LogicGame	\
	%{buildroot}%{_datadir}/applications/lucidlife.desktop
 

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%doc doc/*.png doc/*.html doc/*.gif doc/*.css
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/*%{name}.desktop


%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 24 2014 Peter Gordon <peter@thecodergeek.com> - 0.9.2-14
- Apply fix for print format security:
  + printf-format-security.patch
- Drop versioned DOCDIR patch, in accordance with UnversionedDocdirs feature:
  - make-docs-use-proper-docdir.patch
- Fixes bugs #1037183 (lucidlife FTBFS if "-Werror=format-security" flag is
  used) and #992152 (lucidlife: FTBFS in rawhide)
- Rerun autoconf in %%build to update for ARM64 arch support.
- Fixes bug #926097 (lucidlife: Does not support aarch64 in f19 and rawhide)


* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Apr 26 2013 Jon Ciesla <limburgher@gmail.com> - 0.9.2-12
- Drop desktop vendor tag.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jan 04 2012 Peter Gordon <peter@thecodergeek.com> - 0.9.2-9
- Rebuild for GCC 4.7

* Sun Nov 06 2011 Peter Gordon <peter@thecodergeek.com> - 0.9.2-8
- Rebuild for new libpng.

* Tue May 31 2011 Peter Gordon <peter@thecodergeek.com> 0.9.2-7
- Update spec file in accordance with newer packaging guidelines:
  - Remove BuildRoot references.
  - Remove %%defattr lines in %%files listing.
- Update Source0 and webpage URLs, since the icculus.org site appears to be
  down.
- Fix FTBFS. Resolves bug #564896 (FTBFS lucidlife-0.9.2-5.fc12: ImplicitDSOLinking)
- Fix spelling error in %%description.
- Add patch to correct the FSF address in the GPL license file.
  + fix-FSF-address.patch

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.9.2-3
- Autorebuild for GCC 4.3

* Tue Aug 21 2007 Peter Gordon <peter@thecodergeek.com> - 0.9.2-2
- Update License tag (GPLv2+).
- Rebuild with new BuildID-enabled binutils.

* Sun Apr 29 2007 Peter Gordon <peter@thecodergeek.com> - 0.9.2-1
- Update to new upstream bugfix release (0.9.2)
- Drop .desktop encoding fix (merged upstream):
  - add-.desktop-encoding.patch
- Use %%name in the %%files listing instead of hardcoding it, for consistency
  with my other packages; and use the $(VERSION) macro in the autotools build
  scripts to ease version bumps/updates.

* Fri Apr 20 2007 Peter Gordon <peter@thecodergeek.com> - 0.9.1-3
- Ammend make-docs-use-proper-dir patch to ensure that the "Help" menu
  functionality works properly. (Thanks to Leonard A. Hickey for the patch;
  resolves bug #237329.)
  
* Sun Mar 11 2007 Peter Gordon <peter@thecodergeek.com> - 0.9.1-2
- Add LogicGame to the categories of the installed .desktop file for improved
  organization with games-menus.
- Rework patch calls for more readability.

* Sat Oct 28 2006 Peter Gordon <peter@thecodergeek.com> - 0.9.1-1
- Update to new upstream release (0.9.1)
- Drop X-Fedora and Application categories in installed .desktop file
- Add patch (sent upstream) to add Encoding=UTF-8 in installed .desktop file:
  + add-.desktop-encoding.patch
- Add %%name prefix to old make-docs-use-proper-dir patch filename
  to keep it all in the same logical namespace.

* Sun Aug 27 2006 Peter Gordon <peter@thecodergeek.com> - 0.9-11
- Mass FC6 rebuild

* Sat Jul 22 2006 Peter Gordon <peter@thecodergeek.com> - 0.9-10
- Add gettext as a build requirement to fix reduced mock build NLS issues.
  Thanks again, Matt.

* Tue Jul 18 2006 Peter Gordon <peter@thecodergeek.com> - 0.9-9
- Add perl(XML::Parser) as a build requirement to fix reduced mock build
  (#199355) Thanks for your build report, Matt Domsch.
- Fix up zero-padding for single-digit dates in the %%changelog for
  consistency.

* Sat Apr 08 2006 Peter Gordon <peter@thecodergeek.com> - 0.9-8
- Use desktop-file-install's "--delete-original" option instead of doing
  it manually.

* Tue Mar 28 2006 Peter Gordon <peter@thecodergeek.com> - 0.9-7
- Add patch to put the documentation and %%doc stuff in the same directory.

* Sun Mar 19 2006 Peter Gordon <peter@thecodergeek.com> - 0.9-6
- Bump release due to CVS tagging not liking me. 

* Sun Mar 19 2006 Peter Gordon <peter@thecodergeek.com> - 0.9-5
- Rebuild for new dist tag in FE Devel.

* Wed Mar 15 2006 Peter Gordon <peter@thecodergeek.com> - 0.9-4
- Rebuild for spec file fixes and email address change.

* Sun Feb 26 2006 Peter Gordon <peter@thecodergeek.com> - 0.9-3
- Add %%{?dist} tag to the release to fix CVS tagging issue.

* Sun Feb 19 2006 Peter Gordon <peter@thecodergeek.com> - 0.9-2
- Dropped Requires: on gtk2 and gnome-vfs2, as the -devel sonames will pull
  these in.
- Fixed handling of .desktop file to conform to Fedora Extras guidelines. 
- Changed %%files section to use %%{_datadir}/%%{name} instead of hardcoding
  "lucidlife" to help prevent file ownership problems
- Thanks to Brian Pepple in BZ #177881 for these suggestions.

* Sun Jan 15 2006 Peter Gordon <peter@thecodergeek.com> - 0.9-1
- Initial packaging.
