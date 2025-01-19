%global		use_release	0
%global		use_gitbare	1

%if 0%{?use_gitbare} < 1
# force
%global		use_release	1
%endif

%global		main_version	1.3.2
%undefine		prever
%global		prerpmver		%(echo "%{?prever}" | sed -e 's|-||g')

# Upstream git:
# git://pcmanfm.git.sourceforge.net/gitroot/pcmanfm/pcmanfm

%global		git_version	%{nil}
%global		git_ver_rpm	%{nil}
%global		git_builddir	%{nil}

%if 0%{?use_gitbare} >= 1
%global		tarballdate	20241225
%global		tarballtime	1736

%global		githeaddate	20241216
%global		git_rev		a8ae14c5de336f56efbc5a98b7d5c50a833f20b3
%global		git_short		%(echo %{git_rev} | cut -c-8)
%global		git_version	%{githeaddate}git%{git_short}
%endif


%global		libfm_minver	1.2.0

%undefine		_changelog_trimtime

%if 0%{?use_gitbare}
%global		git_ver_rpm	^%{git_version}
%global		git_builddir	-%{git_version}
%endif

%global		use_gcc_strict_sanitize	0

%global		flagrel	%{nil}
%if	0%{?use_gcc_strict_sanitize} >= 1
%global		flagrel	%{flagrel}.san
%endif

#%%undefine _annotated_build

Name:		pcmanfm
Version:	%{main_version}%{git_ver_rpm}
Release:	2%{?dist}%{flagrel}
Summary:	Extremly fast and lightweight file manager

# SPDX confirmed
License:	GPL-2.0-or-later
URL:		http://pcmanfm.sourceforge.net/
%if 0%{?use_gitbare} >= 1
Source0:	%{name}-%{tarballdate}T%{tarballtime}.tar.gz
%endif
%if 0%{?use_release} >= 1
Source0:	http://downloads.sourceforge.net/pcmanfm/%{name}-%{main_version}%{?prever}.tar.xz
%endif
## Missing in the tarball, taken from git tree
#Source1:	pcmanfm.conf
# From git head e2f4578bd5e89c7a1 data/*.desktop.in
Source1:	pcmanfm.desktop.in
Source2:	pcmanfm-desktop-pref.desktop.in
Source100:	create-pcmanfm-git-bare-tarball.sh

# support new desktop insertion
# https://sourceforge.net/p/pcmanfm/bugs/1064/
Patch101:	pcmanfm-0101-split-out-per-monitor-initialization-part-from-fm_de.patch
Patch102:	pcmanfm-0102-use-GList-for-FmDesktop-entries-instead-of-static-ar.patch
Patch103:	pcmanfm-0103-Fix-the-bug-that-desktop-configuration-is-not-proper.patch
Patch104:	pcmanfm-0104-Finish-implementation-of-inserting-new-monitor.patch

# connect_model: connect to signal before setting folder for model
Patch202:	pcmanfm-0202-connect_model-connect-to-signal-before-setting-folde.patch

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	libfm-gtk-devel >= %{libfm_minver}
BuildRequires:	menu-cache-devel

BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	intltool

%if 0%{?use_gitbare}
BuildRequires:	automake
BuildRequires:	intltool
%endif
%if 0%{?use_gcc_strict_sanitize}
BuildRequires:	libasan
BuildRequires:	libubsan
%endif

BuildRequires:	git

# Patch0
#BuildRequires:	automake

# Request for now
Requires:		libfm-gtk-utils

# Write explicitly
Requires:	libfm >= %{libfm_minver}

%description
PCMan File Manager is an extremly fast and lightweight file manager 
which features tabbed browsing and user-friendly interface.

%package		devel
Summary:		Development files for %{name}
Requires:		%{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%if 0%{?use_release}
%setup -q -n %{name}-%{main_version}%{?prever}%{git_builddir}
#install -cpm 644 %{SOURCE1} %{SOURCE2} data/

git init
%endif

%if 0%{?use_gitbare}
%setup -q -c -T -n %{name}-%{main_version}%{?prever}%{git_builddir}%{?prever} -a 0
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

install -cpm 0644  [A-Z]* ..
%endif

git config user.name "pcmanfm Fedora maintainer"
git config user.email "pcmanfm-owner@fedoraproject.org"

%if 0%{?use_release}
git add .
git commit -q -m "init tree"
%endif

cat %PATCH101 | git am
cat %PATCH102 | git am
cat %PATCH103 | git am
cat %PATCH104 | git am
cat %PATCH202 | git am

%if 0%{?use_gitbare}
sh autogen.sh

# Patch0
autoreconf -fi
%endif

# permission fix
%if 0%{?use_gitbare} < 1
chmod 0644 [A-Z]*
%endif
# ??
chmod u+x configure
chmod u+x */

%build
%if 0%{?use_gcc_strict_sanitize}
export CC="${CC} -fsanitize=address -fsanitize=undefined"
export CXX="${CXX} -fsanitize=address -fsanitize=undefined"
export LDFLAGS="${LDFLAGS} -pthread"
%endif

%if 0%{?use_gitbare}
cd %{name}
%endif

# src/desktop.c
export LDFLAGS="-lm"
%configure \
	--disable-silent-rules \
	--with-gtk=3

make -C po -j1 GMSGFMT="msgfmt --statistics"
make  %{?_smp_mflags} -k

%install
%if 0%{?use_gitbare}
cd %{name}
%endif

make install \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALL="install -p"

desktop-file-install \
	--delete-original \
	--dir $RPM_BUILD_ROOT%{_datadir}/applications \
	--remove-category 'Application' \
	$RPM_BUILD_ROOT%{_datadir}/applications/%{name}*.desktop

%if 0%{?use_gitbare}
cd ..
%endif

%find_lang %{name}

%{_prefix}/lib/rpm/check-rpaths

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc	AUTHORS
%license	COPYING
%doc	README

%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%{_libdir}/%{name}/
%dir	%{_datadir}/%{name}/
%{_datadir}/%{name}/ui/
%{_datadir}/applications/*%{name}*.desktop
%config(noreplace) %{_sysconfdir}/xdg/%{name}/

%files devel
%{_includedir}/pcmanfm-modules.h

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2^20241216gita8ae14c5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Dec 25 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.2^20241216gita8ae14c5-1
- Update to the latest git

* Fri Dec 06 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.2^20241203git836c77c8-1
- Update to the latest git

* Sat Nov 23 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.2^20241103git1312f603-1
- Update to the latest git

* Sun Aug 25 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.2^20240821gitaa4860d6-1
- Update to the latest git

* Tue Aug 13 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.2^20240812git12abd7e1-1
- Update to the latest git

* Fri Jul 26 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.2^20230917gite6b422b2-6
- Apply upstream PR for gcc14 -Werror=incompatible-pointer-types

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2^20230917gite6b422b2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2^20230917gite6b422b2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2^20230917gite6b422b2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.2^20230917gite6b422b2-2
- Change -Wincompatible-pointer-types from error to warning

* Thu Sep 21 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.2^20230917gite6b422b2-1
- Update to the latest git

* Mon Aug 14 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.2^20230807git752d11b7-1
- Update to the latest git

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-1.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-1.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Feb  7 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.2-1
- 1.3.2 release

* Wed Feb  3 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.1-6.D20210203git31394e55
- Rebase to the latest git

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-5.D20200322gitbe8c60d5.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-5.D20200322gitbe8c60d5.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May  5 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.1-5.D20200322gitbe8c60d5
- connect_model: connect to signal before setting folder for model (bug 1645030)

* Wed Apr  8 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.1-4.D20200322gitbe8c60d5
- Update to the latest git (the previous GIOChannel patch merged)

* Sun Mar 22 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.1-3.D20190224gitc52cc4b2
- main: set the GIOChannel encoding to binary
  (may fix 1797193)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2.D20181227git0619a81f.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2.D20181227git0619a81f.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2.D20181227git0619a81f.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 10 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.1-2.D20181227git0619a81f
- Update to the latest git
  - fix isdigit() undefined behavior to fix Alt+Home issue [SF#1085] (may fix #1649027)

* Wed Dec 19 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.1-1
- 1.3.1 release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Apr 29 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.0-1
- 1.3.0 release

* Wed Feb 14 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.5-5.D20171226gitc23e94fb
- Fix patch5

* Mon Feb 12 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.5-4.D20171226gitc23e94fb
- Primary patches for supporting desktop insertion [SF#1064]

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Dec 30 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.5-3
- Upstream patch to fix an issue with losing icons on desktop [SF#1030]

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-2.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.5-2
- Upstream patch to use runtime home directory for socket path
  instead of tmpdir

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Dec 11 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.5-1
- 1.2.5

* Sun Aug 28 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.4-3
- Fix crash when changing desktop size or turning off desktop
  mode (sfbug:1024)

* Sun Feb 28 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.4-2
- 1.2.4

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-2.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 21 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.3-2
- Make about dialog work

* Fri Oct 17 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.3-1
- 1.2.3

* Sun Aug 24 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.2-1
- 1.2.2

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jul  4 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.1-1
- 1.2.1

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Feb 21 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.0-1
- 1.2.0

* Mon Feb 10 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.0-0.1.rc1
- 1.2.0 rc1

* Mon Nov 11 2013 Christoph Wickert <wickert@kolabsys.com> - 1.1.2-3.D20130830gitfc8adaab77
- Rebuild for new menu-cache 0.5.x

* Sun Sep  1 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.1.2-2.D20130830gitfc8adaab77
- Use git head to fix desktop background issue after
  pcmanfm exit
- Also remove old mimetype (ref: bug 988831)

* Thu Aug 15 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.1.2-1
- 1.1.2

* Sun Aug 11 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.1.1-2
- Regenerate desktop file from .in file using intltool

* Thu Aug  8 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.1.1-1
- 1.1.1

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-4.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 26 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 1.1.0-4
- Really drop desktop vendor tag

* Wed May 01 2013 Jon Ciesla <limburgher@gmail.com> - 1.1.0-3
- Drop desktop vendor tag.

* Mon Apr  1 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.1.0-2
- Add workaround for tab too small with GTK3
  (bug 922729, pcmanfm-Bugs-3602000)
- Add workaround for pcmanfm --help showing garbage message
  (pcmanfm-Bugs-3607427)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Nov  4 2012 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.1.0-1
- 1.1.0

* Wed Sep 27 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.0.1-1
- 1.0.1

* Wed Aug 15 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.0-1
- 1.0 release

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.10-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan  5 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.9.10-2
- F-17: rebuild against gcc47

* Fri Oct 28 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.9.10-1
- 0.9.10

* Sun Aug 28 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.9.9-8
- 0.9.9 release

* Sun Aug  7 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.9.9-7
- Update to the latest git

* Mon May 30 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.9.9-6
- Update to the latest git on "tab-rework" branch

* Sun Apr 24 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.9.9-5
- Update to the latest git

* Fri Apr 22 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.9.9-4
- Just kill hal dependency on F-16+

* Sat Apr 09 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.9.9-3
- Update to the latest git

* Sun Feb 20 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.9.9-2
- Update to the latest git

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.9-1.git0f075cf5ba.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Dec  5 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- Update to the latest git

* Wed Oct 13 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.9.8-1
- Update to 0.9.8

* Sat May 29 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.9.7-1
- Update to 0.9.7

* Sun May  9 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.9.5-2
- Translation update from git

* Thu Apr 29 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.9.5-1
- Update to 0.9.5

* Sun Apr 18 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.9.4-1
- Update to 0.9.4
- Require hal-storage-addon
- Fix Source0 URL

* Mon Mar 22 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.9.3-1
- Update to 0.9.3
- Install %%name.png for compatibility on <= F-13

* Sun Feb 14 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.5.2-2
- Fix F-13 DSO linkage issue

* Fri Oct 30 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.2-1
- Update tp 0.5.2 (fixes sourceforge bug 2883172)

* Sat Jul 25 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.5.1-2
- F-12: Mass rebuild

* Thu Jun  4 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.5.1-1
- Update to 0.5.1
- Remove icon name fallback hack
- Still enable 2 patches

* Mon Apr  6 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.5-7
- Fix the issue when application cannot be lauched from desktop menu
  (sourceforge bug 2313286)

* Tue Feb 24 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.5-6
- F-11: Mass rebuild

* Fri Aug  8 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.5-5
- More fallback

* Wed Jul 30 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.5-4
- More fallback for gnome-icon-theme 2.23.X (F-10)

* Tue Jul 29 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.5-2
- F-10+: Use more generic icon name due to gnome-icon-theme 2.23.X change
  First try (need more fix)

* Thu Jul 17 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.5-1
- 0.5

* Wed Jul 16 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.4.6.2-1
- 0.4.6.2

* Tue Jul 15 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.4.6.1-1
- 0.4.6
- 0.4.6.1
- -Werror-implicit-function-declaration is added upstream

* Sat Jun 28 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.4.5-1
- 0.4.5 (remote server access function temporally removed)
- BR: intltool

* Sun May 25 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.4.4.2-1
- 0.4.4.2

* Mon May 19 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.4.4.0-1
- 0.4.4.0

* Sun May 11 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.4.1.1-1
- 0.4.1
- 0.4.1.1

* Mon May  5 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.4.0-1
- 0.4.0

* Sun Apr 13 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.3.9.98-2
- First trial to suppress compilation warning (containing fix for
  crash on an occasion)

* Wed Apr  9 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.3.9.98-1
- 0.3.9.98

* Thu Mar 20 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.3.9.10-1
- 0.3.9.10

* Sat Mar 15 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.3.9.5-1
- 0.3.9.5

* Wed Mar  5 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.3.9-1
- 0.3.9

* Fri Feb 29 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.3.6.1-1
- 0.3.6.1

* Sat Feb 23 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.3.6-1
- 0.3.6

* Wed Feb 20 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.3.5.99-1
- 0.3.6 RC
- 2 patches dropped (applied by upstream)

* Tue Feb 19 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.3.5.23-3
- Fix crash on mounting removable devices

* Mon Feb 18 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.3.5.23-2
- Apply patch to fix crash on 64bits arch as suggested by Hans
  (bug 433182)
- Disable to mount removable devices for now

* Sun Feb 17 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.3.5.23-1
- Initial draft
- Disable inotify support, too buggy (also default is no currently)


