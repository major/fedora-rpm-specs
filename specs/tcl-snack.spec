# We used to define this dynamically, but the Fedora buildsystem chokes on
# using this for the versioned Requires on tcl(abi), so we hardcode it.
# This sucks, but there is no other clean way around it, because tcl
# (and tclsh) aren't in the default buildroot.
%{!?tcl_version: %global tcl_version 8.6}
%{!?tcl_sitearch: %global tcl_sitearch %{_libdir}/tcl%{tcl_version}}
%global realname snack

Name:		tcl-%{realname}
Version:	2.2.10
Release:	62%{?dist}
Summary:	Sound toolkit
# generic/snackDecls.h, generic/snackStubInit.c and generic/snackStubLib.c 
# are under the TCL "license.terms", a copy of which can be found in the tcl package.
# SnackMpg.c just says "BSD" so we pick the most common one. :P
License:	GPL-2.0-or-later AND TCL AND BSD-3-Clause
URL:		http://www.speech.kth.se/snack/
# The upstream source has two files which implement MP3 decoding.
# ./generic/jkFormatMP3.c and ./generic/jkFormatMP3.h
# Those files are non-free so we cannot ship that code, thus, the modified tarball.
# We implement MP3 support the same way that Debian does (libsnackmpg)
# Also, mac/snack.mcp.sit.hqx is a mysterious old compressed file with no clear license.
# It is removed.
# Upstream source can be found here: http://www.speech.kth.se/snack/dist/snack2.2.10.tar.gz
Source0:	%{realname}%{version}-nomp3.tar.gz
# License confirmation email for generic/ffa.c
Source1:	LICENSE-ffa.c.txt
# Copied from debian sources
Source2:	SnackMpg.c
Patch0:		snack2.2.10-mpg123.patch
Patch1:		snack2.2.10-extracflags.patch
Patch3:		snack2.2.10-newALSA.patch
Patch4:		tcl-snack-2.2.10-CVE-2012-6303-fix.patch
Patch5:		snack2.2.10-format-security.patch
# Credit to Sergei Golovan, patches taken from Debian
Patch6:		tcl-snack-2.2.10-python3.patch
Patch7:		snack2.2.10-seektell-fix.patch
Patch8:		tcl-snack-configure-c99.patch
Patch9:		tcl-snack-sigproc2-c99.patch
# Do not use obsolete distutils
Patch10:	snack2.2.10-python3-setuptools.patch
Patch11:	snack2.2.10-const-fix.patch
BuildRequires:	make
BuildRequires:	gcc-c++
BuildRequires:	tcl-devel, tk-devel, libogg-devel, libvorbis-devel
BuildRequires:	libXft-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	python3-devel, python3-setuptools
BuildRequires:	mpg123-devel
Requires:	tcl(abi) = %{tcl_version}
Provides:	%{realname} = %{version}-%{release}

%description
The Snack Sound Toolkit is designed to be used with a scripting language such 
as Tcl/Tk or Python. Using Snack you can create powerful multi-platform audio 
applications with just a few lines of code. Snack has commands for basic sound 
handling, such as playback, recording, file and socket I/O. Snack also provides 
primitives for sound visualization, e.g. waveforms and spectrograms. It was 
developed mainly to handle digital recordings of speech, but is just as useful 
for general audio. Snack has also successfully been applied to other 
one-dimensional signals. The combination of Snack and a scripting language 
makes it possible to create sound tools and applications with a minimum of 
effort. This is due to the rapid development nature of scripting languages. As 
a bonus you get an application that is cross-platform from start. It is also 
easy to integrate Snack based applications with existing sound analysis 
software.

%package devel
Summary:	Development files for Snack Sound Toolkit
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains development files for the Snack Sound Toolkit.

%package -n python3-%{realname}
%{?python_provide:%python_provide python3-%{realname}}
%{?python_provide:%python_provide python3-tcl-snack}
Summary:	Python bindings for Snack Sound Toolkit
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description -n python3-%{realname}
This package contains python3 bindings for the Snack Sound Toolkit. Tcl, Tk, and
Tkinter are also required to use Snack.

%prep
%setup -q -n %{realname}%{version}
%patch -P0 -p1 -b .mpg123
%patch -P1 -p1 -b .extracflags
%patch -P3 -p1 -b .newALSA
%patch -P4 -p1 -b .CVE20126303
%patch -P5 -p1 -b .format-security
%patch -P6 -p1 -b .py3
%patch -P7 -p1 -b .seektell
%patch -P8 -p1 -b .configure-c99
%patch -P9 -p1 -b .sigproc2-c99
%patch -P10 -p1 -b .setuptools
%patch -P11 -p1 -b .const-fix
cp %{SOURCE1} .
cp %{SOURCE2} generic/
chmod -x generic/*.c generic/*.h unix/*.c COPYING README demos/python/*
iconv -f iso-8859-1 -t utf-8 -o README{.utf8,}
mv README{.utf8,}
sed -i -e 's|\r||g' demos/python/*.txt

%build
cd unix/
%configure --disable-static --with-tcl=%{_libdir} --with-tk=%{_libdir} --with-ogg-include=%{_includedir} --with-ogg-lib=%{_libdir} --enable-alsa
make %{?_smp_mflags} EXTRACFLAGS="%{optflags}" stublib all libsnackogg.so libsnackmpg.so
cd ../python
%{__python3} setup.py build

%install
pushd unix/
make install DESTDIR=%{buildroot}
find %{buildroot} -name '*.la' -exec rm -f {} ';'
popd

pushd python
%{__python3} setup.py install --skip-build --root %{buildroot}
install -d %{buildroot}%{tcl_sitearch}
mv %{buildroot}%{_libdir}/%{realname}2.2 %{buildroot}%{tcl_sitearch}/%{realname}2.2
chmod -x %{buildroot}%{tcl_sitearch}/%{realname}2.2/snack.tcl
popd

# Devel bits
mkdir -p %{buildroot}%{_includedir}
install -p generic/*.h %{buildroot}%{_includedir}
install -p unix/snackConfig.sh %{buildroot}%{_libdir}

%filter_from_requires /libsnackstub2.2.so/d

%ldconfig_scriptlets

%files
%doc README
%license COPYING LICENSE-ffa.c.txt
%{tcl_sitearch}/%{realname}2.2/
# %%{_libdir}/libsnackstub*.so

%files devel
%{_includedir}/*.h
%{_libdir}/libsnackstub2.2.a
%{_libdir}/snackConfig.sh

%files -n python3-%{realname}
%doc doc/python-man.html demos/python/
%{python3_sitelib}/tkSnack*
%{python3_sitelib}/__pycache__/tkSnack*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.10-62
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.10-61
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.2.10-60
- Rebuilt for Python 3.13

* Sat Feb 10 2024 Tom Callaway <spot@fedoraproject.org> - 2.2.10-59
- fix FTBFS

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.10-58
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.10-57
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.2.10-56
- Rebuilt for Python 3.12

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.10-55
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec 30 2022 Tom Callaway <spot@fedoraproject.org> 2.2.10-54
- use setuptools instead of obsolete distutils (#2154978)

* Fri Nov 18 2022 Florian Weimer <fweimer@redhat.com> - 2.2.10-53
- Fixes for building in strict C99 mode (#2143895)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.10-52
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.2.10-51
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.10-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.10-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.2.10-48
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.10-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.10-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.2.10-45
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.10-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2.10-43
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2.10-42
- Rebuilt for Python 3.8

* Tue Jul 30 2019 Tom Callaway <spot@fedoraproject.org> - 2.2.10-41
- enable mp3 support the same way debian does
- fix issue where code tries to use old seektell
- disable sharedstubs, it does not work

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.10-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.10-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct  4 2018 Tom Callaway <spot@fedoraproject.org> - 2.2.10-38
- move to python3

* Mon Jul 23 2018 Tom Callaway <spot@fedoraproject.org> - 2.2.10-37
- fix FTBFS

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.10-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.2.10-35
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.10-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.2.10-33
- Python 2 binary package renamed to python2-tcl-snack
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.10-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.10-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.10-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.10-29
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.10-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Tom Callaway <spot@fedoraproject.org> - 2.2.10-27
- modernize spec file

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.10-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.10-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.10-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 2.2.10-23
- Changed requires to require tcl-8.6

* Wed May 21 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 2.2.10-22
- Rebuilt for https://fedoraproject.org/wiki/Changes/f21tcl86

* Mon Dec  9 2013 Tom Callaway <spot@fedoraproject.org> - 2.2.10-21
- fix format-security issues

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.10-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Feb 12 2013 Tom Callaway <spot@fedoraproject.org> - 2.2.10-18
- remove unlicensed compressed mac file from source tarball
- update license tag to include TCL

* Wed Jan  2 2013 Tom Callaway <spot@fedoraproject.org> - 2.2.10-17
- apply fix from Michael Karcher to fix CVE-2012-6303 (bz 885893)

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.10-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.10-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.10-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 2.2.10-13
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 22 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 2.2.10-11
- turn alsa back on, /dev/dsp is dead

* Mon Mar 16 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 2.2.10-10
- enable -devel package

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Dec 24 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.2.10-8
- fix missing BR: libXft-devel

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 2.2.10-7
- Rebuild for Python 2.6

* Wed Oct 22 2008 Tom "spot" Callaway <tcallawa@redhat.com> 2.2.10-6
- disable alsa (bz 463259)

* Mon Sep 22 2008 Tom "spot" Callaway <tcallawa@redhat.com> 2.2.10-5
- fix to work with new alsa (from Jeremiah at Myah OS)

* Thu Sep 18 2008 Tom "spot" Callaway <tcallawa@redhat.com> 2.2.10-4
- *sigh* hardcoding the tcl version is the only way to get it through the buildsystem

* Wed Sep 17 2008 Tom "spot" Callaway <tcallawa@redhat.com> 2.2.10-3
- don't hardcode tcl abi version

* Mon Aug  4 2008 Tom "spot" Callaway <tcallawa@redhat.com> 2.2.10-2
- add BR: python

* Wed Jun 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> 2.2.10-1
- Initial package for Fedora

