# Review: https://bugzilla.redhat.com/show_bug.cgi?id=529465

%global minor_version 0.2
%global thunar_version 1.8.0

Name:           thunar-vcs-plugin
Version:        0.2.0
Release:        35%{?dist}
Summary:        Version Contol System plugin for the Thunar filemanager

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://goodies.xfce.org/projects/thunar-plugins/%{name}
Source0:        http://archive.xfce.org/src/thunar-plugins/%{name}/%{minor_version}/%{name}-%{version}.tar.bz2

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  Thunar-devel >= %{thunar_version}
BuildRequires:  subversion-devel >= 1.5
BuildRequires:  apr-devel >= 0.9.7
BuildRequires:  e2fsprogs-devel
BuildRequires:  uuid-devel
BuildRequires:  libuuid-devel
BuildRequires:  gettext, intltool

Requires:       Thunar >= %{thunar_version}
Requires:       subversion
Requires:       git
# Obsolete thunar-svn-plugin for smooth upgrades
Provides:       thunar-svn-plugin = %{version}-%{release}
Obsoletes:      thunar-svn-plugin < 0.0.4-1

%description
The Thunar VCS Plugin adds Subversion and GIT actions to the context menu of 
Thunar. This gives a VCS integration to Thunar. The current features are:
* Most of the SVN actions: add, blame, checkout, cleanup, commit, copy, 
  delete, export, import, lock, log, move, properties, relocate, resolved, 
  revert, status, switch, unlock and update
* Subversion info in file properties dialog
* Basic GIT actions: add, blame, branch, clean, clone, log, move, reset, stash 
  and status

This project was formerly known as Thunar SVN Plugin.

%prep
%setup -q

%build
%configure --disable-static --enable-subversion --enable-git
# remove rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build

%install

%make_install

# remove libtool archive
rm $RPM_BUILD_ROOT%{_libdir}/thunarx-*/%{name}.la

%find_lang %{name}


%ldconfig_scriptlets

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/thunarx-*/%{name}.so
%{_libexecdir}/tvp-svn-helper
%{_libexecdir}/tvp-git-helper
%{_datadir}/icons/hicolor/*/apps/subversion.png
%{_datadir}/icons/hicolor/*/apps/git.png


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Dec 22 2024 Mukundan Ragavan <nonamedotc@gmail.com> - 0.2.0-34
- rebuild for xfce 4.20

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.2.0-33
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Aug 11 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.2.0-20
- Update to 0.2.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 02 2018 Mukundan Ragavan <nonamedotc@gmail.com> - 0.1.5-6
- Specfile cleanup

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jul 06 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.1.5-1
- Update to 0.1.5

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Mar 01 2015 Kevin Fenzi <kevin@scrye.com> 0.1.4-9
- Rebuild for Xfce 4.12

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Apr 05 2012 Kevin Fenzi <kevin@scrye.com> - 0.1.4-3
- Rebuild for Xfce 4.10

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Mar 20 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.4-1
- Update to 0.1.4 (for Thunar >= 1.2.0)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Nov 25 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.2-3
- Rebuild vor subversion 1.6

* Wed Nov 10 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.2-2
- Require git
- Rework description

* Tue Nov 10 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.2-1
- Update to 0.1.2

* Sat Oct 24 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.1-1
- Update to 0.1.1
- Include git icons

* Wed Sep 30 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.0-1
- Initial Fedora package
