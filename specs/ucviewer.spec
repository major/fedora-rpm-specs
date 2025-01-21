%global svndate	20101019
%global svnrev	4

Name:		ucviewer
# The only place I could find a version was in the documentation.
Version:	0.1
Release:	0.34.%{svndate}svn%{svnrev}%{?dist}
Summary:	A tool for browsing Unicode tables
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://sourceforge.net/projects/ucviewer/
# Upstream does not release versioned tarballs
# Also, they bundle a copy of lua. :P
# svn export https://ucviewer.svn.sourceforge.net/svnroot/ucviewer ucviewer-20101019
# rm -rf ucviewer-20101019/src/lua-5.1.4
# tar cfj ucviewer-20101019.tar.bz2 ucviewer-20101019
Source0:	%{name}-%{svndate}.tar.bz2
# Desktop file not provided by upstream
Source1:	%{name}.desktop
# Use system lua
Patch0:		%{name}-20101019-system-lua.patch
# Don't prompt on buildtype (and use sane system paths)
Patch1:		%{name}-20101019-no-prompting.patch
# lua_open() changed to luaL_newstate()
Patch2:         %{name}-20101019-lua_open-to-luaL_newstate.patch
BuildRequires: make
BuildRequires:	lua-devel, qt-devel
BuildRequires:	desktop-file-utils
BuildRequires:  gcc-c++

%description
Unicode Viewer is a tool for browsing Unicode tables to obtain detailed
information about every glyph. It provides a GUI with multiple functions
for navigating through the data and a Lua scripting interface to create
new functions. It also displays each glyph's DUCET-information and
allows sorting according to an order specified in an allkeys.txt-File.

%prep
%setup -q -n %{name}-%{svndate}
%patch -P0 -p1 -b .system
%patch -P1 -p1 -b .no-prompting
%patch -P2 -p1 -b .lua_open

%build
%{qmake_qt4}
make %{?_smp_mflags}

%install
make INSTALL_ROOT=%{buildroot} install
mkdir %{buildroot}%{_datadir}/pixmaps
pushd %{buildroot}%{_datadir}/pixmaps
ln -s ../UnicodeViewer/icon/uc-book.png .
popd
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE1}

%files
%doc ReadMe.txt
%license License.txt
%{_bindir}/UnicodeViewer
%{_datadir}/applications/ucviewer.desktop
%{_datadir}/pixmaps/uc-book.png
%{_datadir}/UnicodeViewer/

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.34.20101019svn4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.1-0.33.20101019svn4
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.32.20101019svn4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.31.20101019svn4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.30.20101019svn4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.29.20101019svn4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.28.20101019svn4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.27.20101019svn4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.26.20101019svn4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.25.20101019svn4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.24.20101019svn4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.23.20101019svn4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.22.20101019svn4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.21.20101019svn4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.20.20101019svn4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Parag Nemade <pnemade AT redhat DOT com> - 0.1-0.19.20101019svn4
- Add BuildRequires: gcc-c++ as per packaging guidelines
- Added %%license
- Removed Group tag

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.18.20101019svn4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.17.20101019svn4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.16.20101019svn4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.15.20101019svn4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.14.20101019svn4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Feb 02 2016 Rex Dieter <rdieter@fedoraproject.org> - 0.1-0.13.20101019svn4
- use %%qmake_qt4 macro to ensure proper build flags

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.12.20101019svn4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.1-0.11.20101019svn4
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.10.20101019svn4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.9.20101019svn4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Sep 18 2013 Parag <paragn AT fedoraproject DOT org> - 0.1-0.8.20101019svn4
- Fix rh#992831 - ucviewer: FTBFS in rawhide
- Added patch which replaced lua_open by luaL_newstate function

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.7.20101019svn4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.6.20101019svn4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.5.20101019svn4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.4.20101019svn4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.3.20101019svn4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Oct 19 2010 Tom "spot" Callaway <tcallawa@redhat.com> 0.1-0.2.20101019svn4
- fix license tag
- fix desktop file

* Tue Oct 19 2010 Tom "spot" Callaway <tcallawa@redhat.com> 0.1-0.1.20101019svn4
- initial package for Fedora
