# Review: https://bugzilla.redhat.com/show_bug.cgi?id=445140

%global		use_release	0
%global		use_gitbare	1

%if 0%{?use_gitbare} < 1
# force
%global		use_release	1
%endif

%global		git_version	%{nil}
%global		git_ver_rpm	%{nil}
%global		git_builddir	%{nil}

%if 0%{?use_gitbare}
%global		gittardate		20241002
%global		gittartime		2221

%global		gitbaredate	20240905
%global		git_rev		6aaa2949c8caf63cda04ee4068fe389751aa1e7b
%global		git_short		%(echo %{git_rev} | cut -c-8)
%global		git_version	%{gitbaredate}git%{git_short}
%endif

%if 0%{?use_git} || 0%{?use_gitbare}
%global		git_ver_rpm	^%{git_version}
%global		git_builddir	-%{git_version}
%endif


%global		main_version	0.1.11

Name:			lxtask
Version:		%{main_version}%{git_ver_rpm}
Release:		2%{?dist}
Summary:		Lightweight and desktop independent task manager

# SPDX confirmed
License:		GPL-2.0-or-later
URL:			http://lxde.sourceforge.net/
%if 0%{?use_gitbare}
Source0:		%{name}-%{gittardate}T%{gittartime}.tar.gz
%endif
%if 0%{?use_release}
Source0:		https://github.com/lxde/%{name}/archive/%{main_version}/%{name}-%{version}.tar.gz
%endif
Source100:		create-lxtask-git-bare-tarball.sh

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	git
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	intltool
BuildRequires:	automake
BuildRequires:	libtool


%description
LXTask is a lightweight task manager derived from xfce4 task manager with all
xfce4 dependencies removed, some bugs fixed, and some improvement of UI. 
Although being part of LXDE, the Lightweight X11 Desktop Environment, it's 
totally desktop independent and only requires pure gtk+.


%prep
%if 0%{?use_release}
%setup -q -n %{name}-%{main_version}%{git_builddir}

git init
%endif

%if 0%{?use_gitbare}
%setup -q -c -T -n %{name}-%{main_version}%{git_builddir} -a 0
git clone ./%{name}.git/
cd %{name}

git checkout -b %{main_version}-fedora %{git_rev}
cp -a [A-Z]* ..
%endif

git config user.name "lxpanel Fedora maintainer"
git config user.email "lxpanel-owner@fedoraproject.org"

%if 0%{?use_release}
git add .
git commit -m "base" -q
%endif


%build
%if 0%{?use_gitbare}
cd %{name}
%endif

bash autogen.sh
%configure \
	--enable-gtk3 \
	%{nil}
%make_build


%install
%if 0%{?use_gitbare}
cd %{name}
%endif

%make_install

desktop-file-install \
	--delete-original \
	--dir=%{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/%{name}.desktop

%if 0%{?use_gitbare}
cd ..
%endif

%find_lang %{name}

%files -f %{name}.lang
%doc	AUTHORS
%doc	ChangeLog
%doc	README
%doc	TODO
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/*%{name}.desktop
%{_mandir}/man1/lxtask.1*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.11^20240905git6aaa2949-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Oct 02 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.1.11^20240905git6aaa2949-1
- Update to the latest git

* Fri Aug 30 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.1.11^20240828git67c04303-1
- Update to the latest git

* Sun Aug 25 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.1.11^20240823git0113fe4e-1
- Update to the latest git

* Thu Aug 15 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.1.11-1
- 0.1.11

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10^20230802git5c0d3456-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10^20230802git5c0d3456-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10^20230802git5c0d3456-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Aug 14 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.1.10^20230802git5c0d3456-1
- Update to the latest git
- Switch to GTK3

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-1.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-1.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-1.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct 28 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.1.10-1
- 0.1.10

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-2.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 24 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.1.9-2
- Apply upstream track proposal patch for gcc10 -fno-common

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar  2 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.1.9-1
- 0.1.9 formal release

* Fri Mar  1 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.1.8-10.D20190224gitdb6017ff
- Update to the latest git

* Mon Feb 11 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.1.8-9
- Upstream patch for correcting "free memory" usage display

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan  5 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.1.8-5
- Make renice process work (SF#889)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 28 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.1.8-1
- 0.1.8

* Sun Feb 28 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.1.7-1
- 0.1.7

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.1.6-1
- 0.1.6

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 14 2013 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.4-6
- Fix desktop vendor conditionals

* Fri Apr 26 2013 Jon Ciesla <limburgher@gmail.com> - 0.1.4-5
- Drop desktop vendor tag.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Mar 03 2012 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.4-2
- Support full cmdline (LXDE #3469683)
- Close dialog with Escape button or CTRL+W (LXDE #3490254)
- Don't resize columns automatically
- Fix integer overflow
- Update translations from Pootle

* Sat Mar 03 2012 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.4-1
- Update to 0.1.4
- Fix crash (#732182)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.1.3-3
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Apr 15 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.3-1
- Update to 0.1.3

* Tue Apr 06 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.2-1
- Update to 0.1.2

* Thu Jul 30 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 06 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.1-1
- Update to 0.1.1

* Mon Feb 23 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.1-2
- Fix categories in desktop file

* Sun May 04 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.1-1
- Initial Fedora RPM
