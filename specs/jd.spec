##########################################
# For using svn: do
# export SVNROOT="http://svn.sourceforge.jp/svnroot/jd4linux/jd"
# svn checkout $SVNROOT/trunk
# mv trunk jd-%%{main_ver}-%%{strtag}
# tar czf jd-%%{main_ver}-%%{strtag}.tgz jd-%%{main_ver}-%%{strtag}
##########################################

%undefine       _changelog_trimtime

##########################################
# Defined by upsteam
#
%define         main_ver      0.13.0
#%%define         strtag        20200118
%dnl %define         pre_ver       beta
##########################################
#
%global         reponame      JDim
%global         gitdate       20250111
%global         gitcommit     afa6968bb0196ada6f2e8bdacc0184815c13e5b2
%dnl %global         gitcommit     JDim-v%{main_ver}
%global         shortcommit   %(c=%{gitcommit}; echo ${c:0:7})

%global         tarballdate   20250111
%global         tarballtime   2245

##########################################
# Defined by vendor
#
%define         extra_rel     %{nil}
%define         use_gitcommit_as_rel  0
# Tag name changed from vendor to vendorname so as not to
# overwrite Vendor entry in Summary
%define         vendorname    fedora
%define         fontpackage   mona-fonts-VLGothic
##########################################

##########################################
%if 0%{?use_gitcommit_as_rel} >= 1
%global         gittag        %{gitdate}git%{shortcommit}
%global         gitver_rpm    ^%{gittag}
%global         gitver_build  -%{gittag}
%else
%global         gittag        %{nil}
%global         gitver_rpm    %{nil}
%global         gitver_build  %{nil}
%endif

%define         _with_migemo  1
%define         migemo_dict   %{_datadir}/cmigemo/utf-8/migemo-dict

%if ! 0%{?fedora}
%define         _with_migemo 0
%endif
##########################################

##########################################
%global		use_gcc_strict_sanitize	0

%global		flagrel	%{nil}
%if	0%{?use_cppcheck} >= 1
%global		flagrel	%{flagrel}.cppcheck
%endif
%if	0%{?use_gcc_strict_sanitize} >= 1
%global		flagrel	%{flagrel}.san
%endif

#%%undefine _annotated_build
%if 0%{?use_gitcommit_as_rel} >= 1
%global		clamp_mtime_to_source_date_epoch	0
%endif
##########################################


Name:           jd
Epoch:          1
Version:        %{main_ver}%{?strtag:.%{strtag}}%{?pre_ver:~%{pre_ver}}%{gitver_rpm}
Release:        1%{?dist}%{flagrel}
Summary:        A 2ch browser

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            https://github.com/JDimproved/JDim

%dnl Source0:        http://dl.sourceforge.jp/jd4linux/%{repoid}/%{name}-%{main_ver}-%{strtag}.tgz
Source0:        JDim-%{tarballdate}T%{tarballtime}.tar.gz
Source1:        create-JD-git-bare-tarball.sh

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(gtkmm-3.0)
BuildRequires:  libgcrypt-devel
BuildRequires:  libxcrypt-devel
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)

%if 0%{?_with_migemo} >= 1
BuildRequires:  cmigemo-devel
%endif

BuildRequires:  meson
BuildRequires:  gtest-devel
BuildRequires:  %{_bindir}/appstream-util
BuildRequires:  %{_bindir}/desktop-file-validate
BuildRequires:  git
BuildRequires:  make

%if 0%{?use_gcc_strict_sanitize}
BuildRequires:	libasan
BuildRequires:	libubsan
%endif

Requires:       %{fontpackage}


%description
JD is a 2ch browser based on gtkmm2.

%prep
%setup -q -c -T -n %{name}-%{main_ver}%{?strtag:.%{strtag}}%{gitver_build} -a 0

git clone ./%{reponame}.git
cd JDim

git config user.name "%{name} Fedora maintainer"
git config user.email "%{name}-owner@fedoraproject.org"

%if 0%{?use_gitcommit_as_rel} >= 1
git checkout -b %{main_ver}-fedora-local %{gitcommit}
%else
git checkout -b %{main_ver}-fedora-local %{gitcommit}
#git checkout -b %{main_ver}-fedora-local %{reponame}-v%{main_ver}
%endif

cp -a [A-Z]* ..

# reset to base, as git information is embedded in the source
git checkout -b %{main_ver}-fedora
#git reset %{reponame}-v%{main_ver}
%if 0%{?use_gitcommit_as_rel} >= 1
git reset %{gitcommit}
%else
git reset %{gitcommit}
#git reset %{reponame}-v%{main_ver}
%endif

%build
cd %{reponame}

# set TZ for __TIME__
export TZ='Asia/Tokyo'

%set_build_flags
# workaround for calling crypt_r / linking -lcrypt issue with asan
# https://bugzilla.redhat.com/show_bug.cgi?id=1827338
# https://github.com/google/sanitizers/issues/1365
export LDFLAGS="$LDFLAGS -Wl,--push-state,--no-as-needed -lcrypt -Wl,--pop-state"

%if 0%{?use_gcc_strict_sanitize}
export CC="${CC} -fsanitize=address -fsanitize=undefined"
export CXX="${CXX} -fsanitize=address -fsanitize=undefined"
export LDFLAGS="${LDFLAGS} -pthread"
%endif

%meson \
    -Dalsa=enabled \
    -Dbuild_tests=enabled \
    -Dcompat_cache_dir=enabled \
%if 0%{?_with_migemo} >= 1
    -Dmigemo=enabled \
    -Dmigemodict=%{migemo_dict} \
%endif
    -Dpackager="jd-%{version}-%{release}.%{_arch}.rpm by Fedora Project" \
    -Dtls=gnutls \
    %{nil}

%meson_build \
	--ninja-args "-k 0"

%install
cd %{reponame}

%meson_install

# Create symlink
ln -sf jdim %{buildroot}%{_bindir}/%{name}
ln -sf jdim.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/jdim.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/jdim.metainfo.xml

cd %{reponame}
%if 0%{?use_gcc_strict_sanitize} >= 1
export ASAN_OPTIONS=detect_leaks=0
%endif
%meson_test -v

%files
%defattr(-,root,root,-)
%license COPYING
%doc ChangeLog
%doc README.md
%{_bindir}/jdim
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/jdim.desktop
%{_metainfodir}/jdim.metainfo.xml
%{_datadir}/icons/hicolor/*/apps/jdim.*

%changelog
* Sat Jan 11 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1:0.13.0-1
- 0.13.0

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 1:0.12.0-3
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jul 07 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1:0.12.0-1
- 0.12.0

* Tue Jun 18 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1:0.12.0~beta-1
- 0.12.0-beta

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 13 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1:0.11.0-1
- 0.11.0

* Sun Dec 24 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1:0.11.0~beta-1
- 0.11.0 beta

* Sun Jul 23 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1:0.10.1-1
- 0.10.1

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jul  9 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1:0.10.0-1
- 0.10.0

* Mon Jun 19 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1:0.10.0~beta-1
- 0.10.0 beta

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.9.0-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 18 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1:0.9.0-2
- Add missing cstdint header inclusion (gcc13)

* Sun Jan  8 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1:0.9.0-1
- JDim 0.9.0

* Sun Dec 18 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1:0.9.0-0.1.beta.D20221218git3f6cf65
- 0.9.0 beta

* Wed Jul 27 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1:0.8.0-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 18 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1:0.8.0-1
- JDim 0.8.0

* Sun Feb 06 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1:0.7.0-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Jan 16 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1:0.7.0-1
- JDim 0.7.0

* Sun Jul 25 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1:0.6.0-1.1
- Rebuild for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jul 11 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1:0.6.0-1
- JDim 0.6.0

* Wed May  5 2021 Mamoru TASAKA <mtasaka@fedoraproject.org>
- 20210502git5991e9

* Sat Jan 30 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1:0.5.0-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 10 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1:0.5.0-1
- JDim 0.5.0

* Thu Dec 31 2020 Mamoru TASAKA <mtasaka@fedoraproject.org>
- 20201229git7ee2d99

* Sun Dec 20 2020 Mamoru TASAKA <mtasaka@fedoraproject.org>
- 20201219git8310a3b

* Wed Nov 25 2020 Mamoru TASAKA <mtasaka@fedoraproject.org>
- 20201121git11d9b64

* Thu Nov  5 2020 Mamoru TASAKA <mtasaka@fedoraproject.org>
- 20201031git3535ce7

* Tue Oct 27 2020 Mamoru TASAKA <mtasaka@fedoraproject.org>
- 20201025gita4796c6

* Tue Aug 11 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1:0.4.0-1
- JDim 0.4.0

* Wed Jul 22 2020 Tom Stellard <tstellar@redhat.com> - 1:0.3.0-1.1
- Use make macros
- https://fedoraproject.org/wiki/Changes/UseMakeBuildInstallMacro

* Mon Feb  3 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1:0.3.0-1
- Use JDim, introduce Epoch
- 0.3.0

* Tue Jan 15 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.8.9.180424-5
- Bump release to introduce proper upgradepath

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 2.8.9.180424-3.1
- Rebuilt for libcrypt.so.2 (#1666033)

* Mon Aug 27 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.8.9.180424-3
- Apply upstream patch to suppress GLib deprecation warning

* Mon Jul 16 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.8.9.180424-2
- F-29: mass rebuild

* Wed May  2 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.8.9.180424-1
- yama-natuki 2.8.9-180424

* Sat Feb 17 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.8.9.180217-1
- Use yama-natuki JD
- Switch to git

* Fri Feb 15 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.8.9-6
- Fix gcc8 patch
  http://mao.5ch.net/test/read.cgi/linux/1516535816/69

* Thu Feb 15 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.8.9-5
- Fix for gcc8 std::string access strict check

* Thu Feb 15 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.8.9-4
- Patch to build with xcrypt

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 2.8.9-3.2
- Rebuilt for switch to libxcrypt

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.8.9-3.1
- Remove obsolete scriptlets

* Thu Feb 16 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.8.9-3
- Patch for glibmm24 2.50

* Fri Feb  5 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.8.9-2
- F-24: mass rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.8.9-1.1
- Rebuilt for GCC 5 C++11 ABI change

* Fri Feb 27 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.8.9-1
- 2.8.9

* Thu Feb 12 2015 Mamoru TASAKA <mtasaka@fedoraproject.org>
- Update to the latest trunk (r4207)

* Sun Feb  1 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.8.9-0.3.rc150201
- 2.8.9 rc 150201

* Wed Jan 28 2015 Mamoru TASAKA <mtasaka@fedoraproject.org>
- Update to the latest trunk

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 12 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.8.8-2
- F-21: mass rebuild

* Mon Jun  2 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.8.8-1
- 2.8.8

* Fri May  2 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.8.8-0.4.rc140429
- 2.8.8 rc 140429

* Thu Apr 17 2014 Mamoru TASAKA <mtasaka@fedoraproject.org>
- Update to the latest trunk

* Wed Apr  9 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.8.8-0.2.beta140329
- 2.8.8 beta140329

* Thu Feb  6 2014 Mamoru TASAKA <mtasaka@fedoraproject.org>
- Update to the latest trunk

* Mon Jan  6 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.8.7-1
- 2.8.7

* Mon Dec 30 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.8.7-0.2.rc131230
- 2.8.7 rc 131230

* Fri Aug 16 2013 Mamoru TASAKA <mtasaka@fedoraproject.org>
- Update to the latest trunk

* Sun May 19 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.8.6-1
- 2.8.6

* Mon Apr 15 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.8.6-0.7.rc130414
- 2.8.6 rc 130414

* Wed Apr 10 2013 Mamoru TASAKA <mtasaka@fedoraproject.org>
- Update to the latest trunk

* Mon Mar  4 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.8.6-0.5.beta130304
- 2.8.6 beta 130304

* Wed Feb 27 2013 Mamoru TASAKA <mtasaka@fedoraproject.org>
- Update to the latest trunk

* Sat Feb  9 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.8.6-0.4.svn4081_trunk
- F-19: kill vendorization of desktop file (fpc#247)

* Thu Feb 07 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.8.6-0.3.svn4081_trunk
- F-19: rebuild for new gnutls

* Sun Feb 03 2013 Mamoru TASAKA <mtasaka@fedoraproject.org>
- Update to latest trunk

* Sun Dec 12 2012 Mamoru TASAKA <mtasaka@fedoraproject.org>
- Update to latest trunk

* Mon Aug 27 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.8.5-1
- 2.8.5

* Sun Aug 12 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.8.5-0.5.rc120811
- 2.8.5 rc 120811

* Mon Aug  6 2012 Mamoru Tasaka <mtasaka@fedoraproject.org>
- rev 4020

* Tue Mar  6 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> 
- rev 4017

* Mon Feb  6 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.8.5-0.3.beta120206
- 2.8.5 beta 120206

* Tue Jan 31 2012 Mamoru Tasaka <mtasaka@fedoraproject.org>
- rev 3993

* Sun Jan  8 2012 Mamoru Tasaka <mtasaka@fedoraproject.org>
- rev 3982

* Sat Oct 22 2011 Mamoru Tasaka <mtasaka@fedoraproject.org>
- rev 3975

* Mon Aug  8 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.8.2-1
- 2.8.2

* Wed Aug  3 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.8.2-0.3.rc110803
- 2.8.2 rc 110803

* Mon Jul 25 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.8.2-0.2.beta110724
- 2.8.2 beta 110724

* Sat Mar 12 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.8.1-1
- 2.8.1

* Fri Feb 18 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.8.1-0.3.beta110214
- Patch (from rev 3850) to fix segv with long URL

* Tue Feb 15 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.8.1-0.2.beta110214
- 2.8.1 beta 110214

* Thu Feb  3 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.8.0-1
- 2.8.0

* Sat Jan 29 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.8.0-0.6.rc110129
- 2.8.0 rc 111029

* Mon Jan 24 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.8.0-0.5.beta110118
- Patch for gcc 460

* Thu Jan 20 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.8.0-0.4.beta110118
- Patch to fix segfault with icon settings (rev 3818)

* Tue Jan 18 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.8.0-0.3.beta110118
- 2.8.0 beta 110118

* Wed Dec 29 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.7.5-1
- 2.7.5

* Tue Dec 14 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.7.5-0.3.beta101213
- 2.7.5 beta 101213

* Thu Nov  4 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.7.5-0.2.beta101104
- 2.7.5 beta 101104

* Mon Aug 23 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.7.0-1
- 2.7.0

* Thu Aug 19 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.7.0-0.6.rc100818
- 2.7.0 rc 100810

* Sat Aug  7 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.7.0-0.4.beta100808
- 2.7.0 beta 100807

* Sun Jun 28 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.7.0-0.2.beta100627
- 2.7.0 beta 100627

* Mon Apr 26 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.6.5-1
- 2.6.5

* Mon Apr 19 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.6.5-0.3.rc100419
- 2.6.5 rc 100419

* Sun Apr 11 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.6.5-0.2.beta100411
- 2.6.5 beta 100411

* Mon Feb  8 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.6.0-1
- 2.6.0

* Tue Feb  2 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- Change env->pkg default item to Fedora specific

* Sun Jan 31 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.6.0-0.3.rc100130
- 2.6.0 rc 100130

* Sat Jan 23 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.6.0-0.2.beta100123
- 2.6.0 beta 100123

* Fri Jan  1 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- A Happy New Year

* Mon Dec 28 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.5.5-1
- 2.5.5

* Sat Dec 26 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.5.5-0.4.beta091225
- 2.5.5 rc 091225

* Sun Dec 20 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.5.5-0.3.beta091220
- 2.5.5 beta 091220

* Sun Dec  6 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.5.0-1
- 2.5.0

* Mon Nov 30 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.5.0-0.5.rc091129
- 2.5.0 rc 091129

* Tue Nov 24 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.5.0-0.4.beta091123
- 2.5.0 beta 091123

* Wed Nov  4 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.5.0-0.2.beta091103
- 2.5.0 beta 091103

* Sun Sep 27 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.4.2-1
- 2.4.2

* Mon Sep 21 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.4.2-0.5.rc090921
- 2.4.2 rc 090921

* Mon Sep 14 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.4.2-0.4.beta090914
- 2.4.2 beta 090914

* Thu Aug  6 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.4.2-0.3.beta090806
- 2.4.2 beta 090806

* Sun Jul 12 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.4.1-1
- 2.4.1

* Sun Jul  5 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.4.1-0.3.rc090705
- 2.4.1 rc 090705

* Mon Jun 29 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.4.1-0.2.beta090628
- 2.4.1 beta 090628

* Fri May 22 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.4.0-1
- 2.4.0

* Sat May 16 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.4.0-0.5.rc090516
- 2.4.0 rc 090516

* Sun May 10 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.4.0-0.4.beta090510
- 2.4.0 beta 090510

* Wed Apr 29 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.4.0-0.2.beta090429
- 2.4.0 beta 090429

* Thu Mar  5 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.3.0-1
- 2.3.0

* Mon Mar  2 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.3.0-0.2.rc090302
- 2.3.0 rc 090302

* Tue Feb 24 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- F-11: Mass rebuild

* Tue Feb 24 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- GTK icon updating script update

* Fri Feb 13 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.2.0-1
- 2.2.0

* Sun Feb  8 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.2.0-0.4.rc090208
- 2.2.0 rc 090208

* Thu Jan 29 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.2.0-0.3.beta090128
- '2.2.0' beta 090128
- Although tarball says version is 2.1.1, the upsteam developer said that
  he/she will retag version number to 2.2.0
- kill oniguruma support on all branches

* Tue Jan 20 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- Try to kill oniguruma support on F-11 (seemingly behaving badly
  with cmigemo)

* Tue Dec 30 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.1.0-2
- Workaround for the issue on res 868 in JD 6 thread (segv when
  bookmarking when bookmark is empty)

* Mon Dec 29 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.1.0-1
- 2.1.0

* Sun Dec 28 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- rev 2608 (patched against previous rc)

* Tue Dec 23 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.1.0-0.5.rc081223
- 2.1.0 rc 081223

* Sat Dec 20 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- rev 2579
- Use oniguruma on F-9+ for regex

* Tue Dec 16 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.1.0-0.2.beta081216
- 2.1.0 beta 081216

* Mon Nov 24 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.0.3-1
- 2.0.3

* Tue Nov 18 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.0.3-0.3.rc081117
- 2.0.3 rc 081117

* Mon Nov 10 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.0.3-0.2.beta081110
- 2.0.3 beta 081110

* Sat Sep 20 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.0.2-1
- 2.0.2

* Tue Sep 16 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.0.1-2
- Patch to cope with occasional cookie change

* Sun Sep 14 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.0.1-1
- 2.0.1

* Wed Sep 10 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.0.1-0.3.rc080909
- 2.0.1 rc 080909

* Tue Sep  9 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- rev 2322
- Set xdg-open as default browser now by configure option

* Mon Sep  8 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- rev 2319
- revert default browser setting

* Tue Sep  2 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.0.1-0.2.beta080901
- 2.0.1 beta 080901
- Change default config in Fedora
  fonts: use Mona-VLGothic
  browser: use xdg-open

* Tue Aug  5 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- Switch the default fonts to VLGothic-based Mona

* Mon Jul 28 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.0.0-2
- Change Japanese fonts Requires (F-10+)

* Wed Jul 23 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.0.0-1
- 2.0.0

* Mon Jul 14 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.0.0-0.8.rc080714
- 2.0.0 rc 080714

* Thu Jul  3 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.0.0-0.7.beta20080702
- 2.0.0 beta 20080702

* Tue Jun 24 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- F-10: rebuild against new gnutls
- F-10: kill subversion tagging until dependency is solved.

* Mon Jun  2 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.0.0-0.6.beta20080601
- 2.0.0 beta 20080601

* Mon Jun  2 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.0.0-0.5.svn2081_trunk
- Workarround for bug 449225

* Sun May 25 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.0.0-0.5.svn2066_trunk
- Enable alsa

* Fri Apr 18 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.0.0-0.4.beta080418
- 2.0.0 beta 080418

* Tue Apr 15 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.9.9-1
- 1.9.9

* Wed Apr  9 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.9.9-0.3.rc080408
- 1.9.9 rc 080408

* Sun Mar 23 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 
- Workaround for bug 438600

* Mon Feb 25 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.9.9-0.3.beta080225
- 1.9.9 beta 080225

* Sat Feb  9 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- Remove patch for gcc43 (applied by upstream)
- Remove workarround for libsigc++ side bug

* Fri Feb  8 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.0.0-0.2.svn1774
- Patch to make jd happy with gcc43
- Workarround for libsigc++ side bug (bug 431017)

* Fri Dec 28 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.9.8-1
- 1.9.8

* Sun Dec 23 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.9.8-0.5.rc071223
- 1.9.8 rc 071223

* Tue Dec 18 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.9.8-0.4,beta071218
- 1.9.8 beta 071218

* Mon Dec 10 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.9.8-0.3.beta071210
- 1.9.8 beta 071210

* Sun Dec  9 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- Switch from openssl to gnutls

* Thu Nov 22 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.9.7-1
- 1.9.7

* Thu Nov 15 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.9.7-0.4.rc071105
- 1.9.7 rc 071115

* Fri Nov  9 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.9.7-0.3.beta071109
- 1.9.7 beta 071109

* Fri Nov  2 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyoa.c.jp> - 1.9.7-0.2.beta071101
- 1.9.7 beta 071101

* Fri Oct  5 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.9.6-1
- 1.9.6

* Sun Sep 30 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.9.6-0.6.rc070930
- 1.9.6 rc 070930

* Tue Sep 18 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.9.6-0.5.beta070918
- 1.9.6 beta 070918

* Sun Aug  5 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.9.6-0.2.beta070804
- 1.9.6 beta 070804 release 2

* Sat Aug  4 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.9.6-0.1.beta070804
- 1.9.6 beta 070804

* Sat Jun 30 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.9.5-1
- 1.9.5

* Mon Jun 25 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.9.5-0.6.rc070625
- 1.9.5 rc 070625

* Sat Jun 16 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.9.5-0.5.beta070616
- 1.9.5 beta 070616

* Mon Jun 11 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.9.5-0.4.beta070611
- 1.9.5 beta 070611

* Mon May 28 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.9.5-0.3.beta070528
- 1.9.5 beta 070528

* Tue May 22 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.9.5-0.2.beta070516
- Support C/Migemo search

* Tue May 15 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.9.5-0.1.beta070516
- 1.9.5 beta 070516

* Tue Apr  3 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.8.8-1
- 1.8.8

* Fri Mar 30 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.8.8-0.3.rc070330
- 1.8.8 rc 070330

* Fri Mar 23 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.8.8-0.3.beta070324
- 1.8.8 beta 070324

* Sat Mar 17 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.8.8-0.2.beta070317
- 1.8.8 beta 070317

* Sun Feb 18 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.8.8-0.1.beta070218
- 1.8.8 beta 070218

* Fri Feb  2 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.8.5-1
- 1.8.5

* Sun Jan 21 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.8.5-0.3.rc071121
- 1.8.5 rc 071121

* Sun Jan 14 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.8.5-0.3.beta071114
- 1.8.5 beta 070114

* Sun Jan  7 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.8.5-0.2.beta061227
- Add fix for zero-inserted dat problem

* Tue Dec 26 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.8.5-0.1.beta061227
- 1.8.5 beta 061227

* Sun Dec 17 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.8.1-1
- 1.8.1

* Tue Dec 12 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.8.1-0.2.rc061213
- 1.8.1 rc 061213

* Sat Dec  2 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.8.1-0.2.beta061202
- 1.8.1 beta 061202

* Tue Nov 14 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.8.0-1
- 1.8.0

* Wed Nov  8 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.8.0-0.5.rc061108
- 1.8.0 rc 061108

* Fri Nov  3 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.8.0-0.5.beta061103
- 1.8.0 beta 061103

* Sat Oct 28 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.8.0-0.4.cvs061028
- Detect libSM and libICE for x86_64.
- cvs 061028 (23:59 JST)

* Wed Oct 25 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.8.0-0.3.beta061023
- Remove some category from desktop files due to
  desktop-file-utils change.

* Tue Oct 24 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.8.0-0.2.beta061023
- 1.8.0 beta 061023

* Sun Oct 22 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.8.0-0.1.cvs061022
- cvs 061022 (23:59 JST)

* Mon Oct  9 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.8.0-0.1.beta061009
- 1.8.0 beta 061009

* Sat Oct  7 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.7.0-2
- Add libSM-devel to BuildRequires.

* Wed Sep 27 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.7.0-1
- 1.7.0

* Mon Sep 25 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.7.0-0.1.rc060921
- Import to Fedora Extras.

* Sun Mar  9 2006 Houritsuchu <houritsuchu@hotmail.com>
- Version up.
- add icon

* Sat Feb 25 2006 Houritsuchu <houritsuchu@hotmail.com>
- first
