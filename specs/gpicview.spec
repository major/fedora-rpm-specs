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
%global		gittardate		20250212
%global		gittartime		2356

%global		gitbaredate	20241011
%global		git_rev		4dbf512562ff00df2c3476f52f1e568d7c873090
%global		git_short		%(echo %{git_rev} | cut -c-8)
%global		git_version	%{gitbaredate}git%{git_short}
%endif

%if 0%{?use_git} || 0%{?use_gitbare}
%global		git_ver_rpm	^%{git_version}
%global		git_builddir	-%{git_version}
%endif


%global		main_version	0.2.6

Name:			gpicview
Version:		%{main_version}%{git_ver_rpm}
Release:		1%{?dist}
Summary:		Simple and fast Image Viewer for X

# SPDX confirmed
License:		GPL-2.0-or-later
URL:			https://github.com/lxde/%{name}/
%if 0%{?use_gitbare}
Source0:		%{name}-%{gittardate}T%{gittartime}.tar.gz
%endif
%if 0%{?use_release}
Source0:		https://github.com/lxde/%{name}/archive/%{main_version}/%{name}-%{version}.tar.gz
%endif
Source101:		create-gpicview-git-bare-tarball.sh

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	gettext
BuildRequires:	intltool
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	libjpeg-devel
BuildRequires:	desktop-file-utils

BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	git

Requires:		/usr/bin/xdg-mime

%description
Gpicview is an simple and image viewer with a simple and intuitive interface.
It's extremely lightweight and fast with low memory usage. This makes it 
very suitable as default image viewer of desktop system. Although it is 
developed as the primary image viewer of LXDE, the Lightweight X11 Desktop 
Environment, it only requires GTK+ and can be used in any desktop environment.

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

# Restore timestamps
set +x
echo "Restore timestamps"
git ls-tree -r --name-only HEAD | while read f
do
	unixtime=$(git log -n 1 --pretty='%ct' -- $f)
	touch -d "@${unixtime}" $f
done
set -x

cp -a [A-Z]* ..
%endif

git config user.name "gpicview Fedora maintainer"
git config user.email "gpicview-maintainers@fedoraproject.org"

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
	--disable-silent-rules \
	%{nil}
%make_build

%install
%if 0%{?use_gitbare}
cd %{name}
%endif

%make_install
desktop-file-install \
	--delete-original \
	--dir=${RPM_BUILD_ROOT}%{_datadir}/applications \
	--remove-category=Application \
	--remove-category=Utility \
	--remove-category=Photography \
	$RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

%if 0%{?use_gitbare}
cd ..
%endif

%find_lang %{name}

%files -f %{name}.lang
%license	COPYING
%doc	AUTHORS

%{_bindir}/gpicview
%{_datadir}/applications/*gpicview.desktop
%dir	%{_datadir}/gpicview/
%{_datadir}/gpicview/pixmaps/
%{_datadir}/gpicview/ui/
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_mandir}/man1/%{name}.1*

%changelog
* Wed Feb 12 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.6^20241011git4dbf5125-1
- Update to the latest git

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6^20240818.1git1efbde2a-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Oct 08 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.6^20240818.1git1efbde2a-1
- Update to the latest git

* Sun Aug 25 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.6^20240818gitcfce58f1-1
- Update to the latest git

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 17 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.6-1
- 0.2.6

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5^20231013git95eef260-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5^20231013git95eef260-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Dec 31 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.5^20231013git95eef260-1
- Update to the latest git

* Fri Sep 15 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.5^20230913git3438fc58-1
- Update to the latest git

* Sat Aug 19 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.5^20230818git583563d2-1
- Update to the latest git

* Mon Aug 14 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.5^20230802git1c0c9211-1
- Update to the latest git

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Aug 27 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.5-16
- Use gtk3 on F-37+

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.5-5
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Feb 28 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.5-1
- 0.2.5

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jul 15 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.4-1
- 0.2.4

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr 11 2013 Jon Ciesla <limburgher@gmail.com> - 0.2.1-11
- Drop desktop vendor tag.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 0.2.1-9
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 0.2.1-8
- rebuild against new libjpeg

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.2.1-5
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb 17 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.1-3
- Add patch to fix DSO linking (#564627)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 29 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.1-1
- Update to 0.2.1

* Sun May 31 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.0-1
- Update to 0.2.0

* Sun May 17 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.99-1
- Update to 0.1.99 (0.2.0 Beta)
- Require xdg-utils
- Fix URL of Source0
- Run update-desktop-database in %%post and %%postun

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Dec 20 2008 Marc Wiriadisastra <marc@mwiriadi.id.au> - 0.1.11-1
- New upstream release

* Tue Dec 2 2008 Marc Wiriadisastra <marc@mwiriadi.id.au> - 0.1.10-2
- Rebuild of gpicview after updates from Patrice. Thanks and credit
 go to Patrice.

* Sun Sep 14 2008 Marc Wiriadisastra <marc@mwiriadi.id.au> - 0.1.10-1
- New upstream release

* Sat Feb 23 2008 Marc Wiriadisastra <marc@mwiriadi.id.au> - 0.1.9-1
- New upstream release

* Sat Feb 2 2008 Marc Wiriadisastra <marc@mwiriadi.id.au> - 0.1.8-1
- New upstream release

* Fri Jan 11 2008 parag <paragn@fedoraproject.org> - 0.1.7-3
- Spec cleanup

* Thu Jan 10 2008 Marc Wiriadisastra <marc@mwiriadi.id.au> - 0.1.7-2
- Removed zero size files
- added lang in spec file

* Thu Jan 10 2008 Marc Wiriadisastra <marc@mwiriadi.id.au> - 0.1.7-1
- Initial release
