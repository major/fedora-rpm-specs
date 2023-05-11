%global extdir      %{_datadir}/gnome-shell/extensions/dash-to-dock@micxgx.gmail.com
%global gschemadir  %{_datadir}/glib-2.0/schemas

%global giturl https://github.com/micheleg/dash-to-dock
#%%global commit 004f257c3dea5f1851dadd753be87afc555b3dfb
#%%global commit_short %%(c=%%{commit}; echo ${c:0:7})
#%%global commit_date 20220428

Name:           gnome-shell-extension-dash-to-dock
Version:        80
Release:        1%{?dist}
#Release:        5.%%{commit_date}git%%{commit_short}%%{?dist}
Summary:        Dock for the Gnome Shell by micxgx@gmail.com

License:        GPLv2+
URL:            https://micheleg.github.io/dash-to-dock
%if 0%{?commit:1}
Source0:        %{giturl}/archive/%{commit}.tar.gz
%else
Source0:        %{giturl}/archive/extensions.gnome.org-v%{version}.tar.gz#/%{name}-%{version}.tar.gz
%endif

BuildArch:      noarch

BuildRequires:  gettext
BuildRequires:  make
BuildRequires:  sassc
BuildRequires:  %{_bindir}/glib-compile-schemas

Requires:       gnome-shell-extension-common
# libdbusmenu won't be part of RHEL 9, thus disable the dependency.
%if 0%{?fedora}
Requires:       libdbusmenu-gtk3
%endif

%description
This extension enhances the dash moving it out of the overview and
transforming it in a dock for an easier launching of applications
and a faster switching between windows and desktops without having
to leave the desktop view.


%prep
%if 0%{?commit:1}
%autosetup -n dash-to-dock-%{commit} -p 1
%else
%autosetup -n dash-to-dock-extensions.gnome.org-v%{version} -p 1
%endif


%build
%make_build


%install
%make_install

# Cleanup crap.
%{__rm} -fr %{buildroot}%{extdir}/{COPYING*,README*,locale,schemas}

# Create manifest for i18n.
%find_lang %{name} --all-name


# Fedora handles this using triggers.
%if 0%{?rhel} && 0%{?rhel} <= 7
%postun
if [ $1 -eq 0 ] ; then
  %{_bindir}/glib-compile-schemas %{gschemadir} &> /dev/null || :
fi


%posttrans
%{_bindir}/glib-compile-schemas %{gschemadir} &> /dev/null || :
%endif


%files -f %{name}.lang
%license COPYING
%doc README.md
%{extdir}
%{gschemadir}/*gschema.xml


%changelog
* Tue May 09 2023 Frantisek Zatloukal <fzatlouk@redhat.com> - 80-1
- dash-to-dock 80

* Fri Mar 10 2023 Pablo Greco <pgreco@centosproject.org> - 79-1
- dash-to-dock 79

* Tue Feb 28 2023 Pablo Greco <pgreco@centosproject.org> - 78-1
- dash-to-dock 78

* Sat Feb 25 2023 Pablo Greco <pgreco@centosproject.org> - 76-1
- dash-to-dock 76 (support for gnome 44)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 74-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Sep 29 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 74-1
- dash-to-dock 74

* Tue Aug 30 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 73-1
- dash-to-dock 73

* Fri Aug 12 2022 Pablo Greco <pgreco@centosproject.org> - 72-4
- Fix app dot always visible

* Thu Aug 04 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 72-3
- backport bunch of upstream patches:
- Don't autohide while a menu is open
- Update show apps icon for GNOME 42 changes
- 42 cleanups
- Enable preliminary 43 support

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 72-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 18 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 72-1
- dash-to-dock 72

* Mon May 02 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 71-5.20220428git004f257
- Updated support for GNOME 42
- Updated git snapshot with various fixes

* Mon Feb 21 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 71-4.20220124git53114b4
- Preliminary support for GNOME 42

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 71-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Nov 15 2021 Frantisek Zatloukal <fzatlouk@redhat.com> - 71-2
- Backport some fixes from master branch:
- https://launchpad.net/bugs/1947149
- https://github.com/micheleg/dash-to-dock/issues/1553
- https://github.com/micheleg/dash-to-dock/pull/1576/

* Sat Oct 30 2021 Maxwell G <gotmax@e.email> - 71-1
- Update to latest released upstream version, 71
- Remove patches that are now present in upstream

* Sat Oct 16 2021 Frantisek Zatloukal <fzatlouk@redhat.com> - 69-12.20211003git9605dd6
- Apply PR#1530 on F34 too

* Fri Oct 15 2021 Frantisek Zatloukal <fzatlouk@redhat.com> - 69-11.20211003git9605dd6
- Pull in more bugfixes from upstream: PR#1530 and PR#1530
- Drop hacked up GNOME 41 that is replaced by the PR#1531

* Fri Oct 8 2021 Maxwell G <gotmax@e.email> - 69-10.20211003git9605dd6
- Switch back to micheleg/dash-to-dock now that @ewlsh's PR was merged.
- Update %%commit_short variable to determine value based on %%commit.

* Thu Sep 23 2021 Frantisek Zatloukal <fzatlouk@redhat.com> - 69-9.2021706gite4beec8
- Add a small fixup for GNOME 41

* Thu Jul 22 2021 Björn Esser <besser82@fedoraproject.org> - 69-8.2021706gite4beec8
- Add missing BuildRequires

* Thu Jul 22 2021 Artem Vorotnikov <artem@vorotnikov.me> - 69-8.2021706gite4beec8
- Upgrade the PR for GNOME 40 to the latest commit

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 69-7.2021503gita2d40e2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu May 06 2021 Mike DePaulo <mikedep333@gmail.com> - 69-6.2021503gita2d40e2
- Upgrade the PR for GNOME 40 to the latest commit,
  "Fix separator in vertical mode."

* Fri Apr 30 2021 Mike DePaulo <mikedep333@gmail.com> - 69-5.20210430git5c438b8
- Upgrade to the PR for GNOME 40 (Fedora 34) support by ewlsh,
  which was last updated 2021-04-29 (rhbz: #1925747)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 69-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 01 2020 Tomas Popela <tpopela@redhat.com> - 69-3
- Disable the libdbusmenu-gtk3 dependency on ELN/RHEL 9 as it won't contain
  libdbusmenu

* Thu Nov 19 2020 Mike DePaulo <mikedep333@gmail.com> - 69-2
- Merge PR from topherisswell (Christopher Morrow) to depend on libdbusmenu-gtk3
- Either this or the previous change (or both) should resolve enabling the
  extension on recent / all installations of F33 (rhbz: #1884795)

* Thu Nov 19 2020 Nikolaos Perrakis <nikperrakis@gmail.com> - 69-1.20201004git71abe80
- Upgrade to version 69, fixing GNOME 3.38 compatibility issues

* Mon Sep 14 2020 Mike DePaulo <mikedep333@gmail.com> - 68-3.20200911gite2cc441
- Upgrade to PR/branch for GNOME 3.38 compatibility, latest as of 2020-09-11

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 68-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 20 2020 Mike DePaulo <mikedep333@gmail.com> - 68-1
- Update from nightlies (called v67, of v68) to v68 release (2020-04-19)

* Thu Apr 16 2020 Mike DePaulo <mikedep333@gmail.com> - 67-8.20200408git3ca96a2
- Rebase to master branch as of 2020-04-15
  ("Use new convenience function to open settings")
- Use latest proposed patches (37 total) for GNOME 3.36 compatibility
  as of 2020-04-16
  ("DnD shoud work properly also in horizontal mode")

* Thu Apr 09 2020 Mike DePaulo <mikedep333@gmail.com> - 67-7.20200408git77bc707
- Rebase to master branch as of 2020-04-08
- Use latest proposed patches (36 total) for GNOME 3.36 compatibility
  as of 2020-04-08
  https://github.com/micheleg/dash-to-dock/pull/1097#event-3216150535

* Mon Apr 06 2020 Mike DePaulo <mikedep333@gmail.com> - 67-6.20200323git70f1db8
- Rebase to master branch as of 2020-03-23
- Use latest proposed patches (36 total) for GNOME 3.36 compatibility
  (rhbz: #1794889)

* Tue Mar 03 2020 Mike DePaulo <mikedep333@gmail.com> - 67-5.20200224git5658b5c
- Add 7 new addtl proposed patches for GNOME 3.36 compatibility (rhbz: #1794889)

* Thu Feb 27 2020 Mike DePaulo <mikedep333@gmail.com> - 67-4.20200224git5658b5c
- Add new addtl proposed patch for GNOME 3.36 compatibility (rhbz: #1794889)

* Tue Feb 25 2020 Mike DePaulo <mikedep333@gmail.com> - 67-3
- Upgrade to latest master branch
- Add proposed PR/patches for GNOME 3.36 compatibility

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 67-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Oct 27 2019 Mike DePaulo <mikedep333@gmail.com> - 67-1
- Upgrade to 67 for GNOME 3.34 (f31) compatibility (rhbz#1753665)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 66-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 21 2019 Björn Esser <besser82@fedoraproject.org> - 66-1
- Upgrade to 66 for GNOME 3.32 (f30) compatibility (rhbz#1700690)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 64-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 15 2018 Mike DePaulo <mikedep333@gmail.com> - 64-1
- Upgrade to 64 for GNOME 3.30 (f29) compatibility as well as formal
  GNOME 3.28 (f28 & EPEL 7.6) compatibility. (resolves #1634447)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 61-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 61-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 03 2017 Björn Esser <besser82@fedoraproject.org> - 61-1
- Initial import (rhbz#1520149)

* Fri Dec 01 2017 Björn Esser <besser82@fedoraproject.org> - 61-0.1
- Initial rpm release (rhbz#1520149)
