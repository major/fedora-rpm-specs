Name:           freeciv
Version:        3.1.4
Release:        1%{?dist}
Summary:        A multi-player strategy game

License:        GPL-2.0-or-later
URL:            http://sourceforge.net/projects/freeciv/
Source0:        http://download.sourceforge.net/%{name}/%{name}-%{version}.tar.xz

# If a local build fails unable to find Qt5, remove qt-devel.
BuildRequires:  gcc gcc-c++
BuildRequires:	gtk4-devel
BuildRequires:	readline-devel
BuildRequires:	zlib-devel
BuildRequires:	SDL2_mixer-devel
BuildRequires:	ncurses-devel
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	libcurl-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  sqlite-devel
BuildRequires:  make

%description
Freeciv is a turn-based, multi-player, X based strategy game. Freeciv
is generally comparable to, and has compatible rules with, the
Civilization II(R) game by Microprose(R). In Freeciv, each player is
the leader of a civilization, and is competing with the other players
in order to become the leader of the greatest civilization.

%package common
Summary:  %{summary}

%description common
Freeciv common files

%package gtk
Summary:  %{summary}
Requires:  %{name}-common = %{version}-%{release}
Provides: freeciv = %{version}-%{release}
Obsoletes: freeciv < 0:3.0.3-2

%description gtk
Freeciv gtk client

%package qt
Summary:  %{summary}
Requires:  %{name}-common = %{version}-%{release}

%description qt
Freeciv qt client

%prep
%setup -q -n %{name}-%{version}

%build
export MOCCMD="$(%{_qt6_qmake} -query QT_HOST_LIBEXECS)/moc"
%configure --enable-client=gtk4,qt --disable-static --enable-ruledit \
	--with-qtver=qt6 --enable-fcmp=gtk4,qt
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
%find_lang %{name}-core
%find_lang %{name}-nations
%find_lang %{name}-ruledit

desktop-file-install --delete-original \
	--dir $RPM_BUILD_ROOT%{_datadir}/applications  	\
	$RPM_BUILD_ROOT%{_datadir}/applications/org.%{name}.server.desktop

desktop-file-install --delete-original	\
	--dir $RPM_BUILD_ROOT%{_datadir}/applications	\
	$RPM_BUILD_ROOT%{_datadir}/applications/org.%{name}.gtk4.desktop

desktop-file-install --delete-original	\
	--dir $RPM_BUILD_ROOT%{_datadir}/applications	\
	$RPM_BUILD_ROOT%{_datadir}/applications/org.%{name}.qt.desktop

%if 0%{?rhel}
# On RHEL 7, the doc macro puts docs in a versioned subdir
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/freeciv/
%endif

# Remove civmanual
#rm $RPM_BUILD_ROOT%{_bindir}/civmanual
find $RPM_BUILD_ROOT -name '*.la' -delete
find $RPM_BUILD_ROOT -name '*.a' -delete

%files common -f %{name}-core.lang -f %{name}-nations.lang -f %{name}-ruledit.lang
%doc %{_docdir}/freeciv/*

%license COPYING
%{_bindir}/freeciv-server
%{_bindir}/freeciv-manual
%{_bindir}/freeciv-ruledit
%{_bindir}/freeciv-ruleup
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/pixmaps/%{name}-*.png
%{_datadir}/metainfo/*
%{_mandir}/man6/freeciv*6*
%{_sysconfdir}/freeciv/database.lua

%files gtk
%{_bindir}/freeciv-mp-gtk4
%{_bindir}/freeciv-gtk4

%files qt
%{_bindir}/freeciv-mp-qt
%{_bindir}/freeciv-qt

%changelog
* Fri Jan 03 2025 Gwyn Ciesla <gwync@protonmail.com> - 3.1.4-1
- 3.1.4

* Sun Dec 08 2024 Pete Walter <pwalter@fedoraproject.org> - 3.1.3-2
- Rebuild for ICU 76

* Thu Oct 10 2024 Gwyn Ciesla <gwync@protonmail.com> - 3.1.3-1
- 3.1.3

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jul 05 2024 Gwyn Ciesla <gwync@protonmail.com> - 3.1.2-1
- 3.1.2

* Fri Apr 26 2024 Gwyn Ciesla <gwync@protonmail.com> - 3.1.1-1
- 3.1.1

* Mon Mar 04 2024 Gwyn Ciesla <gwync@protonmail.com> - 3.1.0-1
- 3.1.0

* Fri Feb 09 2024 Gwyn Ciesla <gwync@protonmail.com> - 3.0.10-1
- 3.0.10

* Wed Jan 31 2024 Pete Walter <pwalter@fedoraproject.org> - 3.0.9-4
- Rebuild for ICU 74

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Nov 13 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.0.9-1
- 3.0.9

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 František Zatloukal <fzatlouk@redhat.com> - 3.0.8-2
- Rebuilt for ICU 73.2

* Fri Jun 30 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.0.8-1
- 3.0.8

* Tue Apr 11 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.0.7-1
- 3.0.7

* Sat Mar 04 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.0.6-2
- migrated to SPDX license

* Fri Feb 03 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.0.6-1
- 3.0.6

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 31 2022 Pete Walter <pwalter@fedoraproject.org> - 3.0.5-2
- Rebuild for ICU 72

* Fri Dec 16 2022 Gwyn Ciesla <gwync@protonmail.com> - 3.0.5-1
- 3.0.5

* Mon Oct 10 2022 Gwyn Ciesla <gwync@protonmail.com> - 3.0.4-1
- 3.0.4

* Mon Oct 03 2022 Gwyn Ciesla <gwync@protonmail.com> - 3.0.3-2
- Enable qt client.

* Fri Aug 05 2022 Gwyn Ciesla <gwync@protonmail.com> - 3.0.3-1
- 3.0.3

* Mon Aug 01 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 3.0.2-3
- Rebuilt for ICU 71.1

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Gwyn Ciesla <gwync@protonmail.com> - 3.0.2-1
- 3.0.2

* Thu Apr 14 2022 Gwyn Ciesla <gwync@protonmail.com> - 3.0.1-1
- 3.0.1

* Tue Feb 22 2022 Gwyn Ciesla <gwync@protonmail.com> - 3.0.0-1
- 3.0.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec 10 2021 Gwyn Ciesla <gwync@protonmail.com> - 2.6.6-1
- 2.6.6

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 28 2021 Gwyn Ciesla <gwync@protonmail.com> - 2.6.5-1
- 2.6.5

* Tue Apr 06 2021 Gwyn Ciesla <gwync@protonmail.com> - 2.6.4-2
- Move client to gtk 3.22.

* Thu Apr 01 2021 Gwyn Ciesla <gwync@protonmail.com> - 2.6.4-1
- 2.6.4

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 31 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.6.3-1
- 2.6.3

* Mon Nov 30 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.6.2.1-1
- 2.6.2.1

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Apr 14 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.6.2-2
- Drop ggz bits, deprecated.

* Mon Feb 17 2020 Pete Walter <pwalter@fedoraproject.org> - 2.6.2-1
- 2.6.2

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 18 2019 Gwyn Ciesla <gwync@protonmail.com> - 2.6.1-1
- 2.6.1

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.6.0-4
- Rebuild for readline 8.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 23 2018 Gwyn Ciesla <limburgher@gmail.com> - 2.6.0-2
- 2.6.0 final.

* Tue Jul 17 2018 Gwyn Ciesla <limburgher@gmail.com> - 2.6.0-1.rc2
- 2.6.0 RC2.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-1.rc1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Gwyn Ciesla <limburgher@gmail.com> - 2.6.0-1.rc1
- 2.6.0 RC1.

* Mon Apr 09 2018 Gwyn Ciesla <limburgher@gmail.com> - 2.6.0-1.beta3
- 2.6.0 beta3.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-1.beta2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 22 2018 Gwyn Ciesla <limburgher@gmail.com> - 2.6.0-0.beta2
- 2.6.0 beta2.

* Mon Sep 18 2017 Gwyn Ciesla <limburgher@gmail.com> - 2.6.0-0.beta1
- 2.6.0 beta1.

* Sat Aug 19 2017 Gwyn Ciesla <limburgher@gmail.com> - 2.5.9-1
- 2.5.9.

* Sun Aug 13 2017 Gwyn Ciesla <limburgher@gmail.com> - 2.5.8-1
- 2.5.8.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Gwyn Ciesla <limburgher@gmail.com> - 2.5.7-1
- 2.5.7.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 2.5.6-2
- Rebuild for readline 7.x

* Mon Nov 21 2016 Jon Ciesla <limburgher@gmail.com> - 2.5.6-1
- 2.5.6.

* Mon Aug 01 2016 Jon Ciesla <limburgher@gmail.com> - 2.5.5-1
- 2.5.5.

* Sun May 15 2016 Jon Ciesla <limburgher@gmail.com> - 2.5.4-1
- 2.5.4.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 20 2016 Jon Ciesla <limburgher@gmail.com> - 2.5.2-1
- 2.5.2.

* Thu Aug 20 2015 Jon Ciesla <limburgher@gmail.com> - 2.5.1-1
- Latest upstream.
- Disable esound.
- Fix doc packaging.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 16 2015 Jon Ciesla <limburgher@gmail.com> - 2.5.0-5
- 2.5.0 Final.

* Fri Mar 13 2015 Jon Ciesla <limburgher@gmail.com> - 2.5.0-4.RC2
- 2.5.0 RC2.

* Wed Mar 04 2015 Jon Ciesla <limburgher@gmail.com> - 2.5.0-3.RC1
- 2.5.0 RC1.

* Thu Dec 18 2014 Jon Ciesla <limburgher@gmail.com> - 2.5.0-2.beta2
- 2.5.0 beta2.

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-1.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 30 2014 Jon Ciesla <limburgher@gmail.com> - 2.5.0-0.beta1
- 2.5.0 beta1.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Feb 10 2014 Jon Ciesla <limburgher@gmail.com> - 2.4.2-1
- 2.4.2.

* Mon Dec 09 2013 Jon Ciesla <limburgher@gmail.com> - 2.4.1-1
- 2.4.1.

* Mon Sep 16 2013 Jon Ciesla <limburgher@gmail.com> - 2.4.0-1
- 2.4.0.
- Add libcurl BR.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 08 2013 Jon Ciesla <limburgher@gmail.com> - 2.3.4-1
- 2.3.4.

* Mon Feb 11 2013 Jon Ciesla <limburgher@gmail.com> - 2.3.3-2
- Drop desktop vendor tag.

* Wed Aug 29 2012 Jon Ciesla <limburgher@gmail.com> - 2.3.3-1
- 2.3.3, BZ 777333, fixes security flaw.

* Wed Aug 29 2012 Jon Ciesla <limburgher@gmail.com> - 2.3.2-3
- Fix SDL_mixer/hardened build interaction, BZ 852635.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 13 2012 Jon Ciesla <limburgher@gmail.com> - 2.3.2-1
- Update to 2.3.2.
- Add hardened build.

* Thu Jan 05 2012 Jon Ciesla <limburgher@gmail.com> - 2.3.1-1
- Update to 2.3.1.

* Fri Sep 09 2011 Jon Ciesla <limb@jcomserv.net> 2.3.0-1
- Update to 2.3.0.

* Wed Mar 09 2011 Jon Ciesla <limb@jcomserv.net> 2.2.5-1
- Update to 2.2.5.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 30 2010 Thomas Janssen <thomasj@fedoraproject.org> 2.2.4-1
- update to 2.2.4
- fixes #664193

* Mon Aug 30 2010 Thomas Janssen <thomasj@fedoraproject.org> 2.2.2-2
- fix stealth fighter crash #628649

* Mon Aug 02 2010 Thomas Janssen <thomasj@fedoraproject.org> 2.2.2-1
- security fix https://www.redhat.com/security/data/cve/CVE-2010-2445.html
- fixes #612296

* Sun Jun 06 2010 Thomas Janssen <thomasj@fedoraproject.org> 2.2.0-2
- security fix http://gna.org/bugs/?15624
- #600742 #600743 #600744

* Tue Mar 02 2010 Thomas Janssen <thomasj@fedoraproject.org> 2.2.0-1
- New upstream source 2.2.0

* Fri Jan 29 2010 Brian Pepple <bpepple@fedoraproject.org> - 2.1.11-1
- Update to 2.1.11.

* Fri Dec 11 2009 Brian Pepple <bpepple@fedoraproject.org> - 2.1.10-1
- Update to 2.1.10.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Apr  5 2009 Brian Pepple <bpepple@fedoraproject.org> - 2.1.9-1
- Update to 2.1.9.

* Mon Mar 09 2009 Adam Tkac <atkac redhat com> - 2.1.8-3
- drop bind-devel BuildReq, it is not needed

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec  4 2008 Brian Pepple <bpepple@fedoraproject.org> - 2.1.8-1
- Update to 2.1.8.

* Wed Nov 26 2008 Brian Pepple <bpepple@fedoraproject.org> - 2.1.7-1
- Update to 2.1.7.

* Sat Nov 22 2008 Brian Pepple <bpepple@fedoraproject.org> - 2.1.6-2
- Simplify summary.

* Sat Aug 23 2008 Brian Pepple <bpepple@fedoraproject.org> - 2.1.6-1
- Update to 2.1.6.

* Thu Jun 19 2008 Brian Pepple <bpepple@fedoraproject.org> - 2.1.5-1
- Update to 2.1.5.

* Tue Apr 29 2008 Brian Pepple <bpepple@fedoraproject.org> - 2.1.4-1
- Update to 2.1.4.

* Sat Feb  9 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 2.1.3-4
- Fix up typo.

* Fri Feb  8 2008 Rex Dieter <rdieter@fedoraproject.org> 2.1.3-3
- fixup ggz integration (#431726)

* Mon Feb  4 2008 Brian Pepple <bpepple@fedoraproject.org> - 2.1.3-2
- Add ggz gaming support.

* Sat Jan 26 2008 Brian Pepple <bpepple@fedoraproject.org> - 2.1.3-1
- Update to 2.1.3.

* Tue Dec 25 2007 Brian Pepple <bpepple@fedoraproject.org> - 2.1.2-1
- Update to 2.1.2.

* Thu Nov 29 2007 Brian Pepple <bpepple@fedoraproject.org> - 2.1.1-1
- Update to 2.1.1.
- Drop buffer overflow patch. fixed upstream.
- Drop open file patch. fixed upstream.

* Sat Nov 24 2007 Brian Pepple <bpepple@fedoraproject.org> - 2.1.0-2
- Add patch to fix buffer overflow. (#397531)

* Sun Oct 28 2007 Brian Pepple <bpepple@fedoraproject.org> - 2.1.0-1
- Update to 2.1.0.
- Update urls.
- Update aifill & open patches.
- Remove old freeciv pixmap.
- Remove desktop patch.

* Sun Sep 16 2007 Brian Pepple <bpepple@fedoraproject.org> - 2.0.9-4
- Add patch to fix open function build bug.

* Tue Aug 21 2007 Brian Pepple <bpepple@fedoraproject.org> - 2.0.9-3
- Rebuild.

* Thu Aug  2 2007 Brian Pepple <bpepple@fedoraproject.org> - 2.0.9-2
- Update license tag.

* Tue Feb 13 2007 Brian Pepple <bpepple@fedoraproject.org> - 2.0.9-1
- Update to 2.0.9.
- Drop button patch, fixed upstream.
- Drop security patch, fixed upstream.
- Drop X-Fedora category from desktop files.

* Thu Sep  7 2006 Brian Pepple <bpepple@fedoraproject.org> - 2.0.8-7
- Rebuild for FC6.

* Wed Aug  2 2006 Brian Pepple <bpepple@fedoraproject.org> - 2.0.8-6
- Update security patch.
- Add patch to fix turn done buttons style.

* Tue Aug  1 2006 Brian Pepple <bpepple@fedoraproject.org> - 2.0.8-5
- Add patch to fix CVE-2006-3913 vulnerability. (#200545)
- Replace desktop file category 'Strategy' with 'StrategyGame'. (#198086)

* Mon Mar  6 2006 Brian Pepple <bdpepple@ameritech.net> - 2.0.8-2
- Update to 2.0.8.

* Thu Feb 16 2006 Brian Pepple <bdpepple@ameritech.net> - 2.0.7-6
- Remove unnecessary BR (alsa-lib-devel & SDL-devel).

* Mon Feb 13 2006 Brian Pepple <bdpepple@ameritech.net> - 2.0.7-5
- rebuilt for new gcc4.1 snapshot and glibc changes

* Sun Dec  4 2005 Brian Pepple <bdpepple@ameritech.net> - 2.0.7-4
- Rebuild for new bind.

* Sun Nov  6 2005 Brian Pepple <bdpepple@ameritech.net> - 2.0.7-3
- Update to 2.0.7.
- Modify desktop patch for upstream fixes.
- Drop the %%config from .desktop files.

* Mon Sep 26 2005 Brian Pepple <bdpepple@ameritech.net> - 2.0.6-3
- Update to 2.0.6.

* Fri Sep  2 2005 Brian Pepple <bdpepple@ameritech.net> - 2.0.5-3
- Update to 2.0.5.
- Enable debug info.

* Tue Aug 16 2005 Brian Pepple <bdpepple@ameritech.net> - 2.0.4-4
- Rebuild for cairo dep.

* Thu Jul 28 2005 Brian Pepple <bdpepple@ameritech.net> - 2.0.4-2
- Update to 2.0.4.
- Use new stdsounds.

* Fri Jul 15 2005 Brian Pepple <bdpepple@ameritech.net> - 2.0.3-2
- Bump release.

* Thu Jul 14 2005 Brian Pepple <bdpepple@ameritech.net> - 2.0.3-1
- Update to 2.0.3.

* Tue Jun 14 2005 Brian Pepple <bdpepple@ameritech.net> - 2.0.2-1
- Update to 2.0.2.
- Add dist tag.

* Tue Apr 26 2005 Brian Pepple <bdpepple@ameritech.net> - 2.0.1-1.fc4
- Update to 2.0.1.

* Mon Apr 18 2005 Brian Pepple <bdpepple@ameritech.net> - 2.0.0-3.fc4
- Re-add patch to set aifill to 5 on new servers to get some opponents.

* Mon Apr 18 2005 Brian Pepple <bdpepple@ameritech.net> - 2.0.0-2.fc4
- remove redundant --dir* options in %%configure & %%makeinstall.

* Mon Apr 18 2005 Brian Pepple <bdpepple@ameritech.net> - 2.0.0-1.fc4
- Update to 2.0.0.
- Drop 1.14 patches.
- Add new BR's for 2.0.0.

* Sat Mar 26 2005 Brian Pepple <bdpepple@ameritech.net> - 1.14.2-7
- Fixed typos.

* Sat Mar 26 2005 Brian Pepple <bdpepple@ameritech.net> - 1.14.2-6
- Added more macros.
- Replaced BuildPrereq with BuildRequires.
- Drop version of gtk2-devel, since FC3 & later meet minimum needed.

* Wed Mar 23 2005 Brian Pepple <bdpepple@ameritech.net> - 1.14.2-5
- Changed X-Red-Hat-Extra to X-Fedora.
- Added URL.
- Changed BuildRoot to preferred value.
- Removed period from summary.

* Wed Jan 12 2005 Tim Waugh <twaugh@redhat.com> 1.14.2-4
- Rebuilt for new readline.

* Tue Oct 26 2004 Daniel Reed <djr@redhat.com> 1.14.2-3
- [136921] Try a little harder to run as nobody

* Mon Oct 25 2004 Daniel Reed <djr@redhat.com> 1.14.2-2
- [136921] Provide the user with the opportunity to run FreeCiv as root if unable to su to nobody, and throw up an error message if everything fails

* Mon Sep 13 2004 Karsten Hopp <karsten@redhat.de> 1.14.2-1 
- update to latest stable version

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Feb 23 2004 Karsten Hopp <karsten@redhat.de> 1.14.1-3
- rebuild with new chown syntax

* Mon Feb 23 2004 Tim Waugh <twaugh@redhat.com>
- Use ':' instead of '.' as separator for chown.

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Dec 03 2003 Karsten Hopp <karsten@redhat.de> 1.14.1-1
- update to bugfix release 1.14.1

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu May 08 2003 Karsten Hopp <karsten@redhat.de> 1.14.0-1
- update

* Thu Feb 20 2003 Karsten Hopp <karsten@redhat.de> 1.13.0-6
- remove last patch (obsolete)

* Wed Feb 19 2003 Karsten Hopp <karsten@redhat.de>
- fix message translation (#84599)

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Thu Nov 07 2002 Karsten Hopp <karsten@redhat.de>
- spelling fix (#75021)
- set aifill to 5 on new servers to get some opponents (#72586)

* Thu Aug 01 2002 Karsten Hopp <karsten@redhat.de>
- desktop fixes (#69391)

* Wed Jul 24 2002 Karsten Hopp <karsten@redhat.de>
- 0.1.13
- s/Games/Game in desktop-file-install
- fix URL
- add standard sounds 

* Wed Jul 17 2002 Karsten Hopp <karsten@redhat.de> 1.12.0-6
- fix path to datafiles if FREECIV_PATH is not set (#67922)
- fix desktop files (#67920)
- use desktop-file-install

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu Jan 24 2002 Bernhard Rosenkraenzer <bero@redhat.com> 1.12.0-2
- Rebuild in current environment

* Thu Aug 23 2001 Bernhard Rosenkraenzer <bero@redhat.com> 1.12.0-1
- 1.12.0 (non-beta)

* Tue Jul 31 2001 Bernhard Rosenkraenzer <bero@redhat.com> 1.11.4-9
- Rebuild - the fix for #49442 didn't seem to get in last time.

* Mon Jul 30 2001 Bernhard Rosenkraenzer <bero@redhat.com> 1.11.4-8
- Fix up demographics (#50119)

* Wed Jun 27 2001 Than Ngo <than@redhat.com>
- support new gettext
- add patch to build against new libtool

* Tue Mar 20 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- use gtk-config instead of glib-config

* Sun Feb 25 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Fix up civclient-wrapper so it doesn't fail silently when started as
  potentially harmful user (Bug #28928)

* Tue Aug  1 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Fix warning in civclient-wrapper (Bug 14860)

* Fri Jul 21 2000 Trond Eivind Glomsrød <teg@redhat.com>
- 1.11.4
- move to /usr/bin and /usr/share/freeciv (no more /usr/games)

* Wed Jul 12 2000 Trond Eivind Glomsrød <teg@redhat.com>
- remove icon, glint is obsoleted
- don't use find to build file lists, it claimed to own
  lots of directories
- use %%{_tmppath}

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Mon Jul 10 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 1.11.0 (Bug #13610)
- Add .desktop files (Bug #13610)
- Add BuildPrereq: lines
- fix build

* Thu Jun  8 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- move to dist
- update
- clean up the spec file
- fix build with gcc 2.96
- make the gtk client default; it's better than the Xaw one by now.

* Thu Feb 24 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 1.10.0

* Fri Feb  4 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 1.9.2
- use the configure macro

* Sun Nov  7 1999 Bernhard Rosenkraenzer <bero@redhat.com>
- redo RPM for 1.9.0 (many changes to build/install procedure)
