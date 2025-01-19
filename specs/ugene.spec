%global   use_release_branch  0

%if 0%{?use_release_branch} < 1
# master
%global	gitdate		20240830
%global	gitcommit		cff1c2a52a64c901d70e089e83d90eac38361ca5
# New git commit with non-free part removed using "git filter-branch"
%global	gitcommit_free		ccd03e86863580e7e6eea3a1d30aebd4d401233b
%else
# currently 41.0 branch
%global	gitdate		20211117
%global	gitcommit		2d776cc668bc5019452e25ecc330c88093e75c48
# New git commit with non-free part using "git filter-branch"
%global	gitcommit_free		f995e33068c5959c1bab249cd04ed3776e9b2d96
%endif


%global	shortcommit	%(c=%{gitcommit}; echo ${c:0:7})
%global	git_version	%{gitdate}git%{shortcommit}

%global	tarballdate	20240902
%global	tarballtime	1513

%global	use_release	1
%global	use_gitbare	0

%if	0%{?use_gitbare} < 1
# force
%global	use_release	1
%endif

%if	0%{?use_release} >= 1
%global	GIT	true
%else
%global	GIT	git
%endif

%global	mainver		51.0
%undefine	prever

%if		0%{?use_release} >= 1
%global	fedoraver		%{mainver}%{?prever:~%{prerpmver}}
%endif
%if		0%{?use_gitbare} >= 1
%global	fedoraver		%{mainver}%{?git_version:^%{git_version}}
%endif


Name:		ugene
Summary:	Integrated bioinformatics toolkit

Version:	%{fedoraver}
Release:	2%{?dist}

#The entire source code is GPLv2+ except:
#file src/libs_3rdparty/qtbindings_core/src/qtscriptconcurrent.h which is GPLv2
#files in src/plugins_3rdparty/script_debuger/src/qtscriptdebug/ which are GPLv2
# Automatically converted from old format: GPLv2+ and GPLv2 - review is highly recommended.
License:	GPL-2.0-or-later AND GPL-2.0-only
URL:		http://ugene.net
%if	0%{?use_release} >= 1
#Source0:	https://github.com/ugeneunipro/ugene/archive/%{mainver}.tar.gz/#/%{name}-%{mainver}.tar.gz
# Removing non-free part
Source0:	%{name}-free-%{mainver}.tar.gz
# Source0 is created by # env VERSION=%%{mainver} source ./%{SOURCE1}
%endif
%if	0%{?use_gitbare} >= 1
Source0:	%{name}-free-%{tarballdate}T%{tarballtime}.tar.gz
%endif
Source1:	create-ugene-free-tarball.sh
Source2:	create-%{name}-git-bare-tarball.sh
# This is not installed
Source10:	ugene.wrapper
Patch1:	ugene-49.1-narrowing-for-unsigned-char.patch
Patch2:	ugene-51.0-c23-function-proto.patch
# Currently distro-specific
Patch102:	ugene-44.x-libs_3rdparty-breakpad-sys_mmap_use_system_mmap.patch
Patch103:	ugene-40.1-libs_3rdparty-breakpad-unwind-nonsupported-arch.patch
Patch104:	ugene-47.x-plugins_3rdparty-hmm2-nosse-arch.patch
Patch105:	ugene-40.1-libs_3rdparty-breakpad-arch-port.patch
Patch106:	ugene-47.x-git-plgins-smith_waterman-nonsse2-arch.patch
Patch107:	ugene-40.1-qbswap-bigendian-workaround.patch
Patch108:	ugene-47.x-has-sse-i686.patch
Patch109:	ugene-50.x-aarch64-neon-impl-not-yet.patch

BuildRequires:	make
BuildRequires:	gcc-c++
BuildRequires:	desktop-file-utils

%if		0%{?use_gitbare} >= 1
BuildRequires:	%{_bindir}/git
%endif

BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5NetworkAuth)
BuildRequires:	cmake(Qt5PrintSupport)
BuildRequires:	cmake(Qt5Script)
BuildRequires:	cmake(Qt5ScriptTools)
BuildRequires:	cmake(Qt5Sql)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5WebSockets)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Xml)

BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(xtst)
BuildRequires:	pkgconfig(zlib)

Provides:		bundled(samtools) = 0.1.18

%description
Unipro UGENE is a cross-platform visual environment for DNA and protein
sequence analysis. UGENE integrates the most important bioinformatics
computational algorithms and provides an easy-to-use GUI for performing
complex analysis of the genomic data. One of the main features of UGENE
is a designer for custom bioinformatics workflows.

%prep
%if		0%{?use_release} >= 1
%setup -q
# Umm...
sed -i.desktop ugene.pri -e '\@desktop@s|etc/share/|etc/shared/|'
%endif

%if		0%{?use_gitbare} >= 1
%setup -q -c -n %{name}-%{mainver}%{?git_version:-%{git_version}} -T -a 0
git clone ./%{name}.git/
cd %{name}
cp -a [A-Z]* ..

git checkout -b %{mainver}-fedora %{gitcommit_free}
git config user.name "%{name} Fedora maintainer"
git config user.email "%{name}-maintainers@fedoraproject.org"
%endif
%patch -P1 -p1 -b .narrow
	%GIT commit -m "Fix narrowing on arch where default char is unsigned" -a
%patch -P2 -p1 -b .c23
	%GIT comit -m "Fix for C23 strict function prototype" -a
%patch -P102 -p1 -b .sys_mmap -Z
	%GIT commit -m "libs_3rdparty/breakpad: use C function instead of directly using syscall assemble code" -a
%patch -P103 -p1 -b .unwind -Z
	%GIT commit -m "libs_3rdparty/breakpad: workaround for arch not supporting unwind" -a
%patch -P104 -p1 -b .sse -Z
	%GIT commit -m "plugins_3rdparty/hmm2: support architecture not supporting SSE2" -a
%patch -P105 -p1 -b .port -Z
	%GIT commit -m "libs_3rdparty/breakpad: workaround for arch not ported by the upstream" -a
%patch -P106 -p1 -b .sse_2 -Z
	%GIT	commit -m "plugins/smith_waterman: support architecture not supporting SSE2" -a
%patch -P107 -p1 -b .char_bigen -Z
	%GIT	commit -m "src/corelibs/U2Core et al.: Workaround for Qt qbswap issue on Q_BIG_ENDIAN" -a
%patch -P108 -p1 -b .sse_i686 -Z
	%GIT commit -m "ugene_globals.pri: tell sse2 available also on i686" -a
%if 1
%patch -P109 -p1 -b .neon -Z
	%GIT commit -m "neon impl not yet available" -a
%endif

sed -i.nonfree CMakeLists.txt -e '\@add_subdirectory.*plugins_3rdparty/psipred@d'
sed -i.nonfree ugene.pro -e '\@plugins_3rdparty/psipred@d'
	%GIT commit -m "remove nonfree code" -a

%build
%if		0%{?use_gitbare} >= 1
cd %{name}
%endif
%{qmake_qt5} -r \
	PREFIX=%{_libdir}/%{name} \
	UGENE_EXCLUDE_LIST_ENABLED=1 \
	UGENE_USE_SYSTEM_SQLITE=1 \
	UGENE_USE_BUNDLED_ZLIB=0 \
	UGENE_WITHOUT_NON_FREE=1 \
	%{nil}

%make_build -k

%install
LIBAPPDIR=%{_libdir}/%{name}

%if		0%{?use_gitbare} >= 1
cd %{name}
%endif
make install \
	INSTALL_ROOT=%{buildroot} \
	INSTALL="install -p" \
	%{nil}

# Some needed files are not installed.....
mkdir -p %{buildroot}$LIBAPPDIR
cp -a src/_release/* %{buildroot}$LIBAPPDIR
rm -f %{buildroot}$LIBAPPDIR/*.a

# 1. manually move files...
pushd %{buildroot}
rm -f ./$LIBAPPDIR/LICENSE*

# 1-0 bindir
mkdir -p ./%{_bindir}
install -cpm 0755 %{SOURCE10} ./%{_bindir}/%{name}

# 1-1 data files
mkdir -p ./%{_datadir}/%{name}/
mv ./$LIBAPPDIR/data ./%{_datadir}/%{name}
ln -sf ../../../%{_datadir}/%{name} ./$LIBAPPDIR/data

# 1-11 hicolor
mkdir -p ./%{_datadir}/icons/hicolor/32x32/mimetypes/
mv ./$LIBAPPDIR/application-x-ugene-ext.png ./%{_datadir}/icons/hicolor/32x32/mimetypes/

# 1-12 mime
mkdir -p ./%{_datadir}/mime/packages
mv ./$LIBAPPDIR/application-x-ugene.xml ./%{_datadir}/mime/packages

# 1-13 man file
mkdir -p ./%{_mandir}/man1
mv ./$LIBAPPDIR/%{name}.1* ./%{_mandir}/man1

# 1-14 desktop files
mkdir -p ./%{_datadir}/applications/
mv ./$LIBAPPDIR/%{name}.desktop ./%{_datadir}/applications/

# 1-15 icons
mkdir -p ./%{_datadir}/pixmaps
mv ./$LIBAPPDIR/%{name}.{png,xpm} ./%{_datadir}/pixmaps
popd

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%license	LICENSE.txt
%license	LICENSE.3rd_party.txt

%{_bindir}/%{name}

%dir	%{_libdir}/%{name}/
%{_libdir}/%{name}/lib*.so

%dir	%{_libdir}/%{name}/plugins/
%{_libdir}/%{name}/plugins/*.license
%{_libdir}/%{name}/plugins/*.plugin
%{_libdir}/%{name}/plugins/lib*.so

%{_libdir}/%{name}/%{name}
%{_libdir}/%{name}/%{name}cl
%{_libdir}/%{name}/%{name}m
%{_libdir}/%{name}/%{name}ui
%{_libdir}/%{name}/plugins_checker

%dir	%{_datadir}/%{name}/
%{_datadir}/%{name}/data/
%{_libdir}/%{name}/data

%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/ugene.*
%{_datadir}/icons/hicolor/32x32/mimetypes/application-x-ugene-ext.png

%{_datadir}/mime/packages/*.xml
%{_mandir}/man1/%{name}.1*

%changelog
* Fri Jan 17 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 51.0-2
- Support C23 strict function prototype

* Thu Sep 26 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 51.0-1
- 51.0

* Wed Aug  7 2024 Miroslav Suchý <msuchy@redhat.com> - 50.0-3
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 50.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Apr 14 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 50.0-1
- 50.0

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 49.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 49.1-2
- Fix -Wnarrowing on non x86(-64) arch detected by gcc14

* Tue Nov 28 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 49.1-1
- 49.1

* Thu Nov  9 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 49.0-1
- 49.0

* Tue Sep  5 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 48.1-1
- 48.1

* Thu Aug 10 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 48.0-1
- 48.0

* Sat Jul 22 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 47.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue May 23 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 47.0-1
- 47.0

* Fri Feb 24 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 46.0-1
- 46.0

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 45.1-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 18 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 45.1-2
- Header file inclusion fix for gcc13

* Sun Jan  1 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 45.1-1
- A Happy New Year 45.1 release

* Tue Dec 20 2022 Florian Weimer <fweimer@redhat.com> - 45.0-2
- Apply upstream patch to fix C99 compatibility issue

* Sun Nov 20 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 45.0-1
- 45.0

* Sun Aug 21 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 44.0-1
- 44.0

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 43.0-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun  6 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 43.0-1
- 43.0

* Wed Mar  9 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 42.0-1
- 42.0

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 41.0-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Dec  4 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 41.0-1
- 41.0

* Wed Nov 17 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 40.1-2
- Surely remove nonfree code from tarball

* Tue Nov  9 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 40.1-1
- 40.1

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 34.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 34.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 23 07:55:33 CET 2020 Jan Grulich <jgrulich@redhat.com> - 34.0-5
- rebuild (qt5)

* Sun Oct 18 2020 Jeff Law <law@redhat.com> - 34.0-4
- Fix missing #includes for gcc-11

* Fri Sep 11 2020 Jan Grulich <jgrulich@redhat.com> - 34.0-3
- rebuild (qt5)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 34.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr 15 2020 Rex Dieter <rdieter@fedoraproject.org> - 34.0-1
- ugene-34.0
- update Source0 URL
- no longer uses qt5 private api (yay)
- use %%check

* Mon Apr 06 2020 Rex Dieter <rdieter@fedoraproject.org> - 33.0-13
- rebuild (qt5)

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 33.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 09 2019 Jan Grulich <jgrulich@redhat.com> - 33.0-11
- rebuild (qt5)

* Sat Oct 05 2019 Yuliya Algaer <yalgaer@redhat.com> - 33.0-10
- New release

* Wed Sep 25 2019 Jan Grulich <jgrulich@redhat.com> - 1.31.1-7
- rebuild (qt5)
- workaround FTBFS using -fpermissive (#1736931)

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.31.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 17 2019 Jan Grulich <jgrulich@redhat.com> - 1.31.1-5
- rebuild (qt5)

* Sun Mar 03 2019 Rex Dieter <rdieter@fedoraproject.org> - 1.31.1-4
- rebuild (qt5)

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.31.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 13 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.31.1-2
- rebuild (qt5)

* Thu Oct 25 2018 Yuliya Algaer <yalgaer@fedoraproject.com> - 1.31.1-1
- New upstream release

* Fri Aug 24 2018 Yuliya Algaer <yalgaer@fedoraproject.org> - 1.31.0-6
- New upstream release

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.30.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 21 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.30.0-24
- rebuild (qt5)

* Mon Jun 11 2018 Yuliya Algaer <yalgaer@fedoraproject.org> - 1.30.0-23
- New upstream release

* Sun May 27 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.29.0-7
- rebuild (qt5)

* Wed Feb 14 2018 Jan Grulich <jgrulich@redhat.com> - 1.29.0-6
- rebuild (qt5)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.29.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.29.0-4
- Remove obsolete scriptlets

* Tue Jan 02 2018 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.29.0-3
- Fix FTBFS with Qt 5.10

* Mon Jan 01 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.29.0-2
- rebuild (qt5)

* Sun Dec 31 2017 Yuliya Algaer <yalgaer@fedoraproject.org> - 1.29.0-1
- New upstream release.

* Wed Dec 20 2017 Jan Grulich <jgrulich@redhat.com> - 1.28.1-3
- rebuild (qt5)

* Mon Nov 27 2017 Rex Dieter <rdieter@fedoraproject.org> - 1.28.1-2
- rebuild (qt5)

* Tue Nov 21 2017 Yuliya Algaer <yalgaer@fedoraproject.org> - 1.28.1-1
- New upstream release.

* Tue Oct 10 2017 Rex Dieter <rdieter@fedoraproject.org> - 1.27.0-8
- rebuild (qt5)

* Mon Aug 28 2017 Yuliya Algaer <yalgaer@fedoraproject.org> - 1.27.0-7
- New upstream release

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild
