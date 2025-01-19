%define     version     0.177.5
%define     repoid      32988

Summary:    2ch client for KDE
Name:       kita
Version:    %{version}
Release:    42%{?dist}
Source:     http://downloads.sourceforge.jp/kita/%{repoid}/kita-%{version}.tar.gz
#Patch0:     kita-0.177.3-nonweak-symbol.patch
Patch10:    kita-0.177.5-g++44.patch
Patch11:    kita-0.177.5-ui-include-fix.patch
Patch12:    kita-0.177.5-acinclude-m4-syntax-fix.patch

# Overall		GPL-2.0-or-later
# kita/src/libkita/qcp932codec.cpp	MIT
# SPDX confirmed
License:    GPL-2.0-or-later AND MIT
URL:        http://sourceforge.jp/projects/kita/


BuildRequires:       gcc-c++
BuildRequires:       libart_lgpl-devel
BuildRequires:       kdelibs3-devel
BuildRequires:       libjpeg-devel

BuildRequires:       automake
BuildRequires:       libtool
BuildRequires:       desktop-file-utils
BuildRequires:       gettext
BuildRequires:       make

Requires:            mona-fonts-VLGothic

%description
Kita is a 2ch client for KDE.

%prep
%setup -q

#%%patch0 -p2 -b .link
%patch -P10 -p1 -b .g++
%patch -P11 -p1 -b .include
%patch -P12 -p1 -b .syntax

# Support automake 1.11
%{__sed} -i.automake \
	-e 's|automake\*1\.10*|automake*1.1*|' \
	admin/cvs.sh

# Support autoconf 2.71
%{__sed} -i.autoconf \
	-e 's@autoconf\*2\.6\*@autoconf*2.6* | autoconf*2.7*@' \
	-e 's@autoheader\*2\.6\*@autoheader*2.6* | autoheader*2.7*@' \
	admin/cvs.sh

%{__sed} -i.soname \
   -e 's|kita_la_|libkitamain_la_|' \
   -e 's| kita\.la| libkitamain.la|' \
   -e 's|-avoid-version||' \
   kita/src/Makefile.{in,am}
	

sed -i -e 's|grep klineedit|grep -i klineedit|' \
	acinclude.m4 \
	admin/acinclude.m4.in \
	configure \
	%{nil}

%{__sed} -i.dsktop -e 's|Terminal=0|Terminal=false|' \
   kita/src/kita.desktop

make dist -f Makefile.cvs

%build
export LDFLAGS="-Wl,--rpath,%{_libdir}/%{name}"
if [ %{_lib} != lib ] ; then
   SUF=64
else
   SUF=
fi

unset QTDIR || :
. %{_sysconfdir}/profile.d/qt.sh

%configure \
    --disable-rpath \
    --enable-libsuffix=$SUF \
    --libdir=%{_libdir}/%{name} \
    --enable-xdg-menu

# -j2 failed
# make only succeeds with autoconf-2.63, not autoconf-2.64
# Don't know why... and I don't know where to investigate...
# For now using system-wide libtool
%{__make} -j1 \
	LIBTOOL=%{_bindir}/libtool

%install
%{__rm} -rf %{buildroot}

export LDFLAGS="-Wl,--rpath,%{_libdir}/%{name}"
%{__make} \
   kdelnkdir=%{_datadir}/applications \
   DESTDIR=%{buildroot} \
   install

desktop-file-install \
      --delete-original \
%if 0%{?fedora} < 19
      --vendor fedora \
%endif
      --dir %{buildroot}%{_datadir}/applications \
      --add-category KDE \
      --add-category Qt \
      --remove-category Application \
      %{buildroot}/%{_datadir}/applications/%{name}.desktop

# remove unneeded files
find %{buildroot}%{_libdir} -name \*.so -or -name \*.la | xargs %{__rm} -f

unlink %{buildroot}%{_datadir}/doc/HTML/en/kita/common
ln -sf ../common %{buildroot}%{_datadir}/doc/HTML/en/kita/common

# convert encoding
for f in README README.2ch TODO ; do
   iconv -f EUCJP -t UTF8 ${f} > ${f}.tmp && \
      ( touch -r ${f} ${f}.tmp ; %{__mv} -f ${f}.tmp ${f} )
   %{__rm} -f ${f}.tmp
done

# install mo file
%find_lang %{name}

%ldconfig_scriptlets

%files -f %{name}.lang
%defattr(-, root, root,-)
%doc AUTHORS
%license COPYING
%doc ChangeLog
%doc README
%doc README.2ch
%doc TODO
%{_bindir}/*
%{_libdir}/%{name}/
%{_datadir}/apps/%{name}/

%{_datadir}/applications/*%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/*.png

%{_datadir}/doc/HTML/en/kita/

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.177.5-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.177.5-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Feb 18 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.177.5-40
- SPDX migration

* Sat Feb 17 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.177.5-39
- Fix acinclude.m4 syntax error detected by autoconf 2.72

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.177.5-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.177.5-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.177.5-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.177.5-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.177.5-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.177.5-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.177.5-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Mar 25 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.177.5-31
- Detect autoconf 2.71

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.177.5-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.177.5-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.177.5-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.177.5-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.177.5-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 17 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.177.5-25
- Some build fix

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.177.5-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.177.5-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.177.5-22
- Remove obsolete scriptlets

* Tue Aug  8 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.177.5-21
- Add BR: libjpeg-devel explicitly

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.177.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.177.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.177.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.177.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.177.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.177.5-15
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.177.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.177.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.177.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Feb  9 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.177.5-11
- F-19: kill vendorization of desktop file (fpc#247)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.177.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan  5 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.177.5-9
- F-17: rebuild against gcc47

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.177.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Nov 20 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.177.5-7
- F-13: Use system-wide libtool for now (FTBFS 539049)

* Sat Jul 25 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.177.5-6
- F-12: Mass rebuild

* Thu Jun 11 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.177.5-5
- Support automake 1.11 and above (build error detected by
  mass rebuild by Matt Domsch)

* Tue Feb 24 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.177.5-4
- GTK icon cache updating script update

* Sat Feb 21 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.177.5-3
- Fix g++44 build

* Thu Oct  9 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.177.5-2
- Fix sparc64 build

* Tue Sep 23 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.177.5-1
- 0.177.5
- cookie-change.patch accepted by upstream

* Wed Sep 17 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.177.4-1
- 0.177.4

* Tue Sep 16 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.177.3-14
- Workaround to 2ch cookie style change

* Mon Jul 28 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.177.3-13
- Change Japanese fonts Requires (F-10+)

* Sat Feb  9 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- Rebuild against gcc43 (F-9)

* Sat Dec  8 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.177.3-12
- kdelibs3-devel switch (F-9)

* Wed Aug 22 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.177.3-11.dist.1
- Mass rebuild (buildID or binutils issue)

* Sun Aug 12 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.177.3-11
- Fix up BR

* Fri Aug  3 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.177.3-10.dist.2
- License update

* Wed Sep 27 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.177.3-10
- Make common directory link again by symlink
- First remove undefined non-weak symbol related to Qt and KDE
  (still need fixes for Kita internal undefined symbol).

* Tue Sep 19 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.177.3-9
- Again move HTML directory to the original.

* Tue Aug 29 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.177.3-8
- Unset QTDIR, not QTLIB

* Tue Aug 29 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.177.3-7
- Again specify Qt lib directory.

* Tue Aug 29 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.177.3-6
- Check the minimal BuildRequires again.

* Tue Aug 29 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.177.3-5
- Maybe better handling of architecture.

* Tue Aug 29 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.177.3-4
- Remove some requirement on %%post and %%postun.

* Mon Aug 28 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.177.3-3
- Remove gamin-devel.
- Minor fix for desktop file.

* Mon Aug 28 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.177.3-2
- Soname versioning.
- Rename kita.so as this soname is invalid.

* Mon Aug 28 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.177.3-1
- Package for Fedora Extras.
- Add missing BuildRequires.
- Use desktop-file-utils
- Fix scriptlets.
- Change encodings.

* Sun Nov 21 2004 Hideki Ikemoto<ikemo@users.sourceforge.jp>
- remove kitapart/kita*ui.rc

* Sat Oct 07 2004 Hideki Ikemoto<ikemo@users.sourceforge.jp>
- set %%{_prefix} if SuSE

* Sat May 15 2004 Hideki Ikemoto<ikemo@users.sourceforge.jp>
- add 'Serial' field (comment)

* Sat Dec 13 2003 Hideki Ikemoto<ikemo@users.sourceforge.jp>
- don't use %%configure

* Mon Oct 13 2003 Hideki Ikemoto<ikemo@users.sourceforge.jp>
- add files

* Wed Mar 03 2003 Hideki Ikemoto<ikemo@users.sourceforge.jp>
- initial release.
