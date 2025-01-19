# Review: https://bugzilla.redhat.com/show_bug.cgi?id=442269

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
%global		gittardate		20240825
%global		gittartime		1714

%global		gitbaredate	20240817
%global		git_rev		95d5b02e901b0bf33c5ab037a88b8c054a3f818f
%global		git_short		%(echo %{git_rev} | cut -c-8)
%global		git_version	%{gitbaredate}git%{git_short}
%endif

 
%if 0%{?use_git} || 0%{?use_gitbare}
%global		git_ver_rpm	^%{git_version}
%global		git_builddir	-%{git_version}
%endif


%global		main_version	0.6.3

Name:			lxappearance
Version:		%{main_version}%{git_ver_rpm}
Release:		3%{?dist}
Summary:		Feature-rich GTK+ theme switcher for LXDE

# SPDX confirmed
License:		GPL-2.0-or-later
URL:			http://lxde.org/
%if 0%{?use_gitbare}
Source0:		%{name}-%{gittardate}T%{gittartime}.tar.gz
%endif
%if 0%{?use_git}
Source0:		%{name}-%{main_version}-%{?git_version}.tar.bz2
%endif
%if 0%{?use_release}
Source0:        http://downloads.sourceforge.net/sourceforge/lxde/%{name}-%{main_version}.tar.xz
%endif

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  pkgconfig(glib-2.0) >= 2.26.0
BuildRequires:  pkgconfig(gtk+-2.0) >= 2.12.0
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(libmenu-cache) >= 0.3.2
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  docbook-utils
BuildRequires:  docbook-style-xsl
BuildRequires:  /usr/bin/xsltproc

BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  /usr/bin/git

Requires:       lxsession >= 0.4.0

%description
LXAppearance is a new GTK+ theme switcher developed for LXDE, the Lightweight 
X11 Desktop Environment. It is able to change GTK+ themes, icon themes, and 
fonts used by applications. All changes done by the users can be seen 
immediately in the preview area. After clicking the "Apply" button, the 
settings will be written to gtkrc, and all running programs will be asked to 
reload their themes.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains header files for developing plug-ins 
for LXAppearance.


%prep
%if 0%{?use_release}
%setup -q -n %{name}-%{main_version}%{git_builddir}

git init
%endif

%if 0%{?use_gitbare}
%setup -q -c -T  -n %{name}-%{main_version}%{git_builddir} -a 0
git clone ./%{name}.git/
cd %{name}

#git checkout -b %{version}-fedora %{version}
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
cp -a data/ ..

cat > GITHASH <<EOF
EOF

cat GITHASH | while read line
do
	commit=$(echo "$line" | sed -e 's|[ \t].*||')
	git cherry-pick $commit
done

%endif

git config user.name "lxpanel Fedora maintainer"
git config user.email "lxpanel-maintainers@fedoraproject.org"

%if 0%{?use_release}
git add .
git commit -m "base" -q
%endif

sh autogen.sh


%build
%if 0%{?use_gitbare}
pushd %{name}
%endif

%configure \
	--disable-silent-rules \
	--enable-man \
%if 0
	--enable-gtk3 \
%endif
	%{nil}
%make_build


%install
%if 0%{?use_gitbare}
pushd %{name}
%endif

%make_install

%if 0%{?use_gitbare}
popd
%endif

# Own plugin directory
mkdir -p %{buildroot}%{_libdir}/%{name}/plugins/

%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files	-f %{name}.lang
%doc		AUTHORS
%license	COPYING

%{_bindir}/%{name}
%{_datadir}/applications/*%{name}.desktop
%dir	%{_datadir}/%{name}/
%{_datadir}/%{name}/ui/
%dir	%{_libdir}/%{name}/plugins/
%{_mandir}/man1/%{name}*.1.*

%files	devel
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3^20240817git95d5b02e-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Aug 30 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.6.3^20240817git95d5b02e-2
- Own plugin directory

* Sun Aug 25 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.6.3^20240817git95d5b02e-1
- Update to the latest git

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3^20230917git655fd083-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3^20230917git655fd083-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3^20230917git655fd083-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Dec 31 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.6.3^20230917git655fd083-1
- Update to the latest git

* Fri Sep 15 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.6.3^20230913git5423cc46-1
- Update to the latest git

* Mon Aug 14 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.6.3^20230801git8e634d03-1
- Update to the latest git

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-14.D20200807gitd132fdd8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-13.D20200807gitd132fdd8.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-13.D20200807gitd132fdd8.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-13.D20200807gitd132fdd8.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-13.D20200807gitd132fdd8.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Mar 21 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.6.3-13.D20200807gitd132fdd8
- Update to the latest git
- Fix segfault with GLib 2.68
- Fix segfault when removing icon theme

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Apr  8 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.6.3-3
- Fix non-initialized variable usage detected by clang
  (sourceforge bug 866)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 28 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.6.3-1
- 0.6.3

* Sun Feb 28 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.6.2-1
- 0.6.2

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.6.1-1
- 0.6.1

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 14 2013 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.2-5
- Fix desktop vendor conditionals
- Make build verbose

* Fri Apr 26 2013 Jon Ciesla <limburgher@gmail.com> - 0.5.2-4
- Drop desktop vendor tag.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jun 03 2012 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.2-1
- Update to 0.5.2 (#827780)

* Sun Mar 04 2012 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.1-1
- Update to 0.5.1 (includes manpage again)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.5.0-3
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Oct 13 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.0-1
- Update to 0.5.0

* Fri Sep 04 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.0-0.1.20100903gitf0945814
- Update to GIT preview of 0.5.0

* Wed Feb 17 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.0-2
- Add patch to fix DSO linking (#564754)

* Thu Jan 07 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.0-1
- Update to 0.4.0

* Fri Dec 11 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.0-1
- Update to 0.3.0

* Mon Nov 23 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.1-3
- Workaround for infinite loop that causes FTBFS (#538963)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 06 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.1-1
- Update to 0.2.1

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Apr 20 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.2-1
- Update to 0.2
- Remove install-patch, applied upstream

* Sat Apr 12 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.1-1
- Initial Fedora RPM
