# Filter provides from plugins.
%global __provides_exclude_from ^%{_libdir}/%{name}/plugins/.*$


Name:		xed
Version:	3.8.2
Release:	2%{?dist}
Summary:	X-Apps [Text] Editor (Cross-DE, backward-compatible, GTK3, traditional UI)

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		https://github.com/linuxmint/%{name}
Source0:	%url/archive/%{version}/%{name}-%{version}.tar.gz

ExcludeArch:   %{ix86}

BuildRequires:	meson
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	gnome-common
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	libappstream-glib
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gspell-1)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gtksourceview-4)
BuildRequires:	pkgconfig(libpeas-gtk-1.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(iso-codes)
BuildRequires:	python3-gobject-base
BuildRequires:	pkgconfig(sm)
BuildRequires:	pkgconfig(xapp) >= 1.4.0
BuildRequires:	python%{python3_pkgversion}-devel

Requires:	iso-codes
Requires:	python%{python3_pkgversion}-gobject%{?_isa}
Requires:	xapps%{?_isa}
Suggests:	hunspell-en

%description
Xed is a small, but powerful text editor.  It has most standard text
editor functions and fully supports international text in Unicode.
Advanced features include syntax highlighting and automatic indentation
of source code, printing and editing of multiple documents in one window.

Xed is extensible through a plugin system, which currently includes
support for spell checking, comparing files, viewing CVS ChangeLogs, and
adjusting indentation levels.


%package devel
Summary:	Files needed to develop plugins for %{name}
Requires:	%{name}%{?_isa}	== %{version}-%{release}

%description devel
This package contains files needed to develop plugins for %{name}.


%package doc
Summary:	Documentation files for %{name}
BuildArch:	noarch

%description doc
This package contains the documentation files for %{name}.


%prep
%autosetup -p 1

# Use 'classic'-theme by default.
%{__sed} -i -e 's!xed!classic!g' data/org.x.editor.gschema.xml.in

# Make source-files noexec.
%{_bindir}/find . -type f -name '*.c' | %{_bindir}/xargs %{__chmod} -c 0644
%{_bindir}/find . -type f -name '*.h' | %{_bindir}/xargs %{__chmod} -c 0644

%build
%meson	\
	-Ddocs=true	\
	-Ddeprecated_warnings=false
%meson_build


%install
%meson_install
%{__sed} -i -e '/.*<project_group>.*/d'				\
	%{buildroot}%{_metainfodir}/org.x.editor.metainfo.xml

%find_lang %{name} --with-gnome 


%check
# Validate desktop-files.
%{_bindir}/desktop-file-validate				\
	%{buildroot}%{_datadir}/applications/org.x.editor.desktop

# Validate AppData-files.
%{_bindir}/appstream-util validate-relax --nonet		\
	%{buildroot}%{_metainfodir}/org.x.editor.metainfo.xml


%files -f %{name}.lang
%license AUTHORS COPYING debian/copyright
%doc ChangeLog README.md debian/changelog
%exclude %{_datadir}/%{name}/gir-1.0
%exclude %{_datadir}/%{name}/gir-1.0/*
%{_bindir}/%{name}
%{_metainfodir}/org.x.editor.metainfo.xml
%{_datadir}/applications/org.x.editor.desktop
%{_datadir}/dbus-1/services/org.x.editor.*service
%{_datadir}/glib-2.0/schemas/org.x.editor.*gschema.xml
%{_datadir}/gtksourceview-4/styles/xed.xml
%{_datadir}/%{name}/
%{_libdir}/%{name}/
%{_mandir}/man1/%{name}.1*


%files devel
%{_datadir}/%{name}/gir-1.0
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/%{name}.pc


%files doc
%license %{_datadir}/licenses/%{name}*
%doc %{_datadir}/doc/%{name}*
%doc %{_datadir}/gtk-doc/*


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jan 06 2025 Leigh Scott <leigh123linux@gmail.com> - 3.8.2-1
- Update to 3.8.2

* Fri Dec 20 2024 Leigh Scott <leigh123linux@gmail.com> - 3.8.1-1
- Update to 3.8.1

* Fri Dec 06 2024 Leigh Scott <leigh123linux@gmail.com> - 3.8.0-1
- Update to 3.8.0

* Mon Dec 02 2024 Leigh Scott <leigh123linux@gmail.com> - 3.6.9-1
- Update to 3.6.9

* Mon Nov 25 2024 Leigh Scott <leigh123linux@gmail.com> - 3.6.7-1
- Update to 3.6.7

* Mon Aug 26 2024 David King <amigadave@amigadave.com> - 3.6.6-2
- Rebuild against gspell

* Tue Aug 20 2024 Leigh Scott <leigh123linux@gmail.com> - 3.6.6-1
- Update to 3.6.6

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 3.6.5-2
- convert license to SPDX

* Sat Jul 20 2024 Leigh Scott <leigh123linux@gmail.com> - 3.6.5-1
- Update to 3.6.5

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jul 04 2024 Leigh Scott <leigh123linux@gmail.com> - 3.6.4-2
- Restore classic theme default

* Thu Jul 04 2024 Leigh Scott <leigh123linux@gmail.com> - 3.6.4-1
- Update to 3.6.4

* Tue Jun 18 2024 Leigh Scott <leigh123linux@gmail.com> - 3.6.3-1
- Update to 3.6.3

* Tue Jun 11 2024 Leigh Scott <leigh123linux@gmail.com> - 3.6.2-1
- Update to 3.6.2

* Wed Jun 05 2024 Leigh Scott <leigh123linux@gmail.com> - 3.6.1-1
- Update to 3.6.1

* Tue Jun 04 2024 Leigh Scott <leigh123linux@gmail.com> - 3.6.0-1
- Update to 3.6.0

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 04 2024 Leigh Scott <leigh123linux@gmail.com> - 3.4.5-1
- Update to 3.4.5 release

* Tue Dec 05 2023 Leigh Scott <leigh123linux@gmail.com> - 3.4.4-1
- Update to 3.4.4 release

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 27 2023 Leigh Scott <leigh123linux@gmail.com> - 3.4.2-1
- Update to 3.4.2 release

* Thu Jun 08 2023 Leigh Scott <leigh123linux@gmail.com> - 3.4.1-1
- Update to 3.4.1 release

* Fri Jun 02 2023 Leigh Scott <leigh123linux@gmail.com> - 3.4.0-1
- Update to 3.4.0 release

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec 16 2022 Leigh Scott <leigh123linux@gmail.com> - 3.2.8-1
- Update to 3.2.8 release

* Sun Jul 24 2022 Leigh Scott <leigh123linux@gmail.com> - 3.2.7-1
- Update to 3.2.7 release

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jul 17 2022 Leigh Scott <leigh123linux@gmail.com> - 3.2.5-1
- Update to 3.2.5 release

* Sun Jul 17 2022 Leigh Scott <leigh123linux@gmail.com> - 3.2.4-1
- Update to 3.2.4 release

* Sun Jun 19 2022 Leigh Scott <leigh123linux@gmail.com> - 3.2.3-1
- Update to 3.2.3 release

* Sun Feb 13 2022 Leigh Scott <leigh123linux@gmail.com> - 3.2.2-4
- Fix last commit

* Sun Feb 13 2022 Leigh Scott <leigh123linux@gmail.com> - 3.2.2-3
- Fix (rhbz#2053951)

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Jan 01 2022 Leigh Scott <leigh123linux@gmail.com> - 3.2.2-1
- Update to 3.2.2 release

* Mon Dec 06 2021 Leigh Scott <leigh123linux@gmail.com> - 3.2.1-1
- Update to 3.2.1 release

* Wed Nov 24 2021 Leigh Scott <leigh123linux@gmail.com> - 3.2.0-1
- Update to 3.2.0 release

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 25 2021 Leigh Scott <leigh123linux@gmail.com> - 3.0.2-1
- Update to 3.0.2 release

* Thu Jun 10 2021 Leigh Scott <leigh123linux@gmail.com> - 3.0.1-1
- Update to 3.0.1 release

* Tue Jun 01 2021 Leigh Scott <leigh123linux@gmail.com> - 3.0.0-1
- Update to 3.0.0 release

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan  2 2021 Leigh Scott <leigh123linux@gmail.com> - 2.8.4-1
- Update to 2.8.4 release

* Thu Dec 10 2020 Leigh Scott <leigh123linux@gmail.com> - 2.8.2-1
- Update to 2.8.2 release

* Tue Dec  8 2020 Leigh Scott <leigh123linux@gmail.com> - 2.8.1-1
- Update to 2.8.1 release

* Mon Nov 30 2020 Leigh Scott <leigh123linux@gmail.com> - 2.8.0-1
- Update to 2.8.0 release

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 14 2020 Leigh Scott <leigh123linux@gmail.com> - 2.6.2-1
- Update to 2.6.2 release

* Tue May 12 2020 Leigh Scott <leigh123linux@gmail.com> - 2.6.0-1
- Update to 2.6.0 release

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 11 2019 Leigh Scott <leigh123linux@googlemail.com> - 2.4.2-1
- Update to 2.4.2 release

* Tue Nov 26 2019 Leigh Scott <leigh123linux@googlemail.com> - 2.4.1-1
- Update to 2.4.1 release

* Fri Nov 22 2019 Leigh Scott <leigh123linux@googlemail.com> - 2.4.0-1
- Update to 2.4.0 release

* Wed Jul 31 2019 Leigh Scott <leigh123linux@googlemail.com> - 2.2.3-1
- Update to 2.2.3 release

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 14 2019 Leigh Scott <leigh123linux@googlemail.com> - 2.2.1-1
- Update to 2.2.1 release

* Sat Jun 29 2019 Leigh Scott <leigh123linux@googlemail.com> - 2.2.0-1
- Update to 2.2.0 release

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild
post.
* Sun Dec 16 2018 Leigh Scott <leigh123linux@googlemail.com> - 2.0.2-1
- Update to 2.0.2 release

* Wed Nov 28 2018 Leigh Scott <leigh123linux@googlemail.com> - 2.0.1-1
- Update to 2.0.1 release

* Mon Nov 19 2018 Leigh Scott <leigh123linux@googlemail.com> - 2.0.0-1
- Update to 2.0.0 release

* Wed Aug 15 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.8.3-1
- Update to 1.8.3 release

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.8.1-2
- Rebuilt for Python 3.7

* Sat Jun 02 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.8.1-1
- Update to 1.8.1 release

* Sun May 06 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.8.0-1
- Update to 1.8.0 release

* Sun Mar 11 2018 Kalev Lember <klember@redhat.com> - 1.6.4-0.2.20180309git3733860
- Rebuilt for gspell 1.8

* Fri Mar 09 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.6.4-0.1.20180309git3733860
- Update to git snapshot

* Thu Feb 22 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.6.3-4
- Update patch

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 29 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.6.3-2
- Update upstream pull requests

* Sat Nov 25 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.6.3-1
- Update to 1.6.3
- Add upstream pull requests

* Fri Nov 17 2017 Björn Esser <besser82@fedoraproject.org> - 1.6.2-1
- Update to 1.6.2 release (rhbz#1513985)

* Fri Nov 17 2017 Björn Esser <besser82@fedoraproject.org> - 1.6.0-2
- Adjustments for EPEL7

* Sat Nov 04 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.6.0-1
- Update to 1.6.0 release
- Fix conditional

* Fri Sep 01 2017 Björn Esser <besser82@fedoraproject.org> - 1.4.6-6
- Some more fixes for EPEL

* Fri Sep 01 2017 Björn Esser <besser82@fedoraproject.org> - 1.4.6-5
- Use Python34 on EPEL

* Fri Sep 01 2017 Björn Esser <besser82@fedoraproject.org> - 1.4.6-4
- Adjustments for EPEL

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 16 2017 Björn Esser <besser82@fedoraproject.org> - 1.4.6-1
- Update to 1.4.6 release (rhbz#1471446)

* Tue Jul 04 2017 Björn Esser <besser82@fedoraproject.org> - 1.4.5-1
- Update to 1.4.5 release (rhbz#1467641)

* Fri Jun 30 2017 Björn Esser <besser82@fedoraproject.org> - 1.4.4-2
- Fix filtered provides

* Wed Jun 28 2017 Björn Esser <besser82@fedoraproject.org> - 1.4.4-1
- Update to 1.4.4 release (rhbz#1463461)
- Filter provides from plugins

* Wed May 24 2017 Björn Esser <besser82@fedoraproject.org> - 1.4.2-1
- Update to 1.4.2 release (rhbz#1454988)

* Sun May 07 2017 Björn Esser <besser82@fedoraproject.org> - 1.4.1-1
- Update to 1.4.1 release (rhbz #1448673)

* Sat May 06 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.4.0-1
- Update to 1.4.0 release

* Sun Apr 02 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.2.2-3
- Redo patches with latest fixes

* Sat Apr 01 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.2.2-2
- Fix start up crash under wayland (rhbz #1438157)
- Fix 'format not a string literal' compile error

* Tue Feb 21 2017 Björn Esser <besser82@fedoraproject.org> - 1.2.2-1
- Initial import (rhbz#1424798)

* Sun Feb 19 2017 Björn Esser <besser82@fedoraproject.org> - 1.2.2-0.5
- Use 'classic'-theme by default
- Move devel-files to devel-pkg
- Remove exec-perms from source-files

* Sun Feb 19 2017 Björn Esser <besser82@fedoraproject.org> - 1.2.2-0.4
- Add patch to update to recent master

* Sun Feb 19 2017 Björn Esser <besser82@fedoraproject.org> - 1.2.2-0.3
- Fix dir-ownership for %%{_datadir}/help

* Sun Feb 19 2017 Björn Esser <besser82@fedoraproject.org> - 1.2.2-0.2
- Doc-pkg should be noarch'ed

* Sun Feb 19 2017 Björn Esser <besser82@fedoraproject.org> - 1.2.2-0.1
- Initial rpm-release (rhbz#1424798)
