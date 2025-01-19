%global		use_release	0
%global		use_git		0
%global		use_gitbare	1

%if 0%{?use_git} < 1
%if 0%{?use_gitbare} < 1
# force
%global		use_release	1
%endif
%endif

%global		git_version	%{nil}
%global		git_ver_rpm	%{nil}
%global		git_builddir	%{nil}

%if 0%{?use_gitbare}
%global		gittardate		20231201
%global		gittartime		1031

%global		gitbaredate	20231121
%global		git_rev		f663dca570562d5dfb7ab31a9035e51f29591eef
%global		git_short		%(echo %{git_rev} | cut -c-8)
%global		git_version	%{gitbaredate}git%{git_short}
%endif

%if 0%{?use_git} || 0%{?use_gitbare}
%global		git_ver_rpm	^%{git_version}
%global		git_builddir	-%{git_version}
%endif


%global		main_version	0.2.3

Name:			lxappearance-obconf
Version:		%{main_version}%{git_ver_rpm}
Release:		5%{?dist}
Summary:		Plugin to configure Openbox inside LXAppearance

# SPDX confirmed
License:		GPL-2.0-or-later
URL:			http://lxde.org/
%if 0%{?use_gitbare}
Source0:		%{name}-%{gittardate}T%{gittartime}.tar.gz
%endif
%if 0%{?use_release}
Source0:		http://downloads.sourceforge.net/sourceforge/lxde/%{name}-%{version}.tar.xz
%endif
Source1:		create-%{name}-git-bare-tarball.sh

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	pkgconfig(obrender-3.5) >= 3.5
BuildRequires:	pkgconfig(obt-3.5) >= 3.5
BuildRequires:	openbox-devel >= 3.5.2
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(gthread-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(lxappearance)
BuildRequires:	libSM-devel
BuildRequires:	gettext
BuildRequires:	intltool
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	libtool
BuildRequires:	/usr/bin/git
Requires:		lxappearance >= 0.5.0
Requires:		openbox >= 3.5.2

%description
This plugin adds an additional tab called "Window Border" to LXAppearance.
It is only visible when the plugin is installed and Openbox is in use.

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

git config user.name "%{name} Fedora maintainer"
git config user.email "%{name}-maintainers@fedoraproject.org"

%if 0%{?use_release}
git add .
git commit -m "base" -q
%endif

sh autogen.sh

%build
%if 0%{?use_gitbare}
cd %{name}
%endif

%configure \
	--disable-static \
	--disable-silent-rules \
	%{nil}
%make_build

%install
%if 0%{?use_gitbare}
cd %{name}
%endif

%make_install
%if 0%{?use_gitbare}
cd ..
%endif

find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
%find_lang %{name}

%files -f %{name}.lang
# FIXME add NEWS and TODO if not empty
%license	COPYING
%doc	AUTHORS
%doc	CHANGELOG
%doc	README

%{_libdir}/lxappearance/plugins/obconf.so
%{_datadir}/lxappearance/obconf/


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3^20231121gitf663dca5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3^20231121gitf663dca5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3^20231121gitf663dca5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3^20231121gitf663dca5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Dec  1 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.3^20231121gitf663dca5-1
- Update to the latest git

* Tue Nov 21 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.3^20230918git63c5dc1b-2
- Fix compilation with libxml2 2.12.0

* Tue Sep 19 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.3^20230918git63c5dc1b-1
- Update to the latest git
- SPDX migration

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Leigh Scott <leigh123linux@gmail.com> - 0.2.3-17
- Rebuild fo new imlib2

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan  5 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.3-15
- preview_menu: set parent for menu.title.bg when parentrelative
  (sfbug: 960)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Feb 28 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.3-1
- 0.2.3

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jul 12 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.2-1
- 0.2.2

* Thu Jul 02 2015 Miroslav Lichvar <mlichvar@redhat.com> - 0.2.0-8
- Rebuild for new openbox

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Aug 15 2013 Miroslav Lichvar <mlichvar@redhat.com> - 0.2.0-4
- Fix building with openbox-3.5.2 (#992155)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Aug 04 2012 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.0-1
- Update to 0.2.0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Mar 04 2012 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.2-0.3.20120304git5fad8207
- Update to latest git to fix broken preview with Openbox 3.5

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-0.2.20110828git02aeaab2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Aug 28 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.2-0.1.20110828git02aeaab2
- Update to latest GIT snapshot to the package build with openbox >= 3.5.0

* Sun Aug 28 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.1-1
- Update to 0.1.1 (Note that upstream's 0.0.1 tarball is actually 0.1.1 in VCS)

* Wed Jul 14 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.0-0.1.20110714git3a0fd02d
- Update to latest GIT snapshot

* Fri Jan 28 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.0-0.1.20110128git710ba0e6
- Update to latest GIT snapshot

* Fri Sep 03 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.0-0.1.20100903git1769cdca
- Update to latest GIT snapshot

* Fri Aug 13 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.0-0.1.20100813git1bf017ee
- initial package
