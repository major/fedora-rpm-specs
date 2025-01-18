Name:			diffuse
Version:		0.9.0
Release:		5%{?dist}
Summary:		Graphical tool for merging and comparing text files
License:		GPL-2.0-or-later
URL:			https://mightycreak.github.io/diffuse/
Source0:		https://codeload.github.com/MightyCreak/diffuse/tar.gz/v%{version}
BuildArch:		noarch
BuildRequires:		autoconf
BuildRequires:		desktop-file-utils
BuildRequires:		gettext
BuildRequires:		glib2-devel
BuildRequires:		gtk-update-icon-cache
BuildRequires:		meson
BuildRequires:		python3-cairo
BuildRequires:		python3-devel
BuildRequires:		python3-gobject
Requires:		gnome-icon-theme
Requires:		gnome-icon-theme-legacy
Requires:		hicolor-icon-theme
Requires:		python3-cairo
Requires:		python3-gobject
Provides:		difftool
Provides:		mergetool

%description
Diffuse is a graphical tool for merging and comparing text files. Diffuse is
able to compare an arbitrary number of files side-by-side and gives users the
ability to manually adjust line-matching and directly edit files. Diffuse can
also retrieve revisions of files from Bazaar, CVS, Darcs, Git, Mercurial,
Monotone, RCS, Subversion, and SVK repositories for comparison and merging.
This is the Python 3 fork of Diffuse.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/io.github.mightycreak.Diffuse.desktop
%meson_test

%files -f %{name}.lang
%license COPYING
%doc AUTHORS CHANGELOG.md README.md
%config(noreplace) %{_sysconfdir}/diffuserc
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/io.github.mightycreak.Diffuse.desktop
%{_datadir}/gnome/help/%{name}/
%{_datadir}/icons/hicolor/*/apps/io.github.mightycreak*
%{_datadir}/appdata/io.github.mightycreak.Diffuse.appdata.xml
%{_datadir}/omf/%{name}/
%{_mandir}/man*/*
%{_mandir}/*/man*/*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 niohiani <notinsideofhereiamnotinside@gmail.com> 0.9.0-2
- Release 0.9.0 with some packaging modifications by Leigh Scott reincorporated

* Sat Jan 20 2024 niohiani <notinsideofhereiamnotinside@gmail.com> 0.9.0-1
- Release 0.9.0

* Sun Apr 16 2023 niohiani <notinsideofhereiamnotinside@gmail.com> 0.8.2-1
- Release 0.8.2

* Fri Apr 07 2023 niohiani <notinsideofhereiamnotinside@gmail.com> 0.8.1-1
- Release 0.8.1

* Thu Nov 10 2022 niohiani <notinsideofhereiamnotinside@gmail.com> 0.7.7-1
- New release - 0.7.7

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu May 12 2022 niohiani <notinsideofhereiamnotinside@gmail.com> 0.7.5-2
- Appended additional required packages to .spec file as a quick fix for Diffuse failing to launch under GNOME with Fedora 36.

* Mon Apr 18 2022 niohiani <notinsideofhereiamnotinside@gmail.com> 0.7.5-1
- initial build of release 0.7.5.

* Tue Apr 12 2022 niohiani <notinsideofhereiamnotinside@gmail.com> 0.7.4-1
- initial build of release 0.7.4.

* Tue Nov 23 2021 niohiani <notinsideofhereiamnotinside@gmail.com> 0.7.3-1
- release 0.7.3.

* Thu Nov 18 2021 niohiani <notinsideofhereiamnotinside@gmail.com> 0.7.2-1
- 0.7.2 new official release due to small translation fix.

* Thu Nov 18 2021 niohiani <notinsideofhereiamnotinside@gmail.com> 0.7.1-1
- 0.7.1 official release.

* Wed Nov 17 2021 niohiani <notinsideofhereiamnotinside@gmail.com> 0.7.1-1
- Based on 0.7.1 commits.

* Tue Nov 16 2021 niohiani <notinsideofhereiamnotinside@gmail.com> 0.7.0-1
- Based on 0.7.0 commits.

* Tue Nov 16 2021 niohiani <notinsideofhereiamnotinside@gmail.com> 0.6.1-2
- Based on newer commits prior to the in-progress 0.7.0 work.

* Fri Jul 23 2021 niohiani <notinsideofhereiamnotinside@gmail.com> 0.6.1-1
- Initial build of version pulled directly from git.

* Wed May 26 2021 niohiani <notinsideofhereiamnotinside@gmail.com> 0.6.0-1
- Packaging of this application is now up to par for inclusion in the default repos. Upon successfully importing the package, the COPR repository for test builds will become defunct.

* Mon Dec  7 2020 niohiani <notinsideofhereiamnotinside@gmail.com> 0.6.0
- Updated to 0.6.0. Mainly under the hood changes in this release, so nothing really visible to the users in this version. That said, I figured it was a long time since the last release (4 months ago) and, as promised, I want Diffuse development to be a bit more active and iterative. Replace old install.py with the more standard Meson. Remove u string prefixes since Python 3 is in UTF-8 by default. Replaced some interpolation operators (%) for the f string prefix. Use the window scale factor for the icons generation

* Tue Nov  3 2020 niohiani <notinsideofhereiamnotinside@gmail.com> 0.5.9
- Fedora Packaging of Python 3 Fork and Initial upload to COPR of said fork