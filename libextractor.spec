%global plugindir	%{_libdir}/%{name}
%global gtkver		3

Name:		libextractor
Version:	1.10
Release:	8%{?dist}
Summary:	Simple library for keyword extraction

License:	GPLv3+
URL:		https://www.gnu.org/software/libextractor
Source0:	https://ftp.gnu.org/gnu/libextractor/%{name}-%{version}.tar.gz
Source1:	https://ftp.gnu.org/gnu/libextractor/%{name}-%{version}.tar.gz.sig
Source2:        https://ftp.gnu.org/gnu/gnu-keyring.gpg
Source10:	README.fedora

BuildRequires:  gcc
## exiv2 config check uses g++
BuildRequires:  gcc-c++
BuildRequires:	gettext zzuf
BuildRequires:	libtool-ltdl-devel
BuildRequires:	bzip2-devel zlib-devel
BuildRequires:  gnupg2
BuildRequires: make

%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%package plugins
Summary:	Plugins for libextractor
Obsoletes:	%{name}-plugins-pdf < %{version}
Obsoletes:	%{name}-plugins-thumbnailqt < %{version}
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-plugins-base
Requires:	%{name}-plugins-exiv2
Requires:	%{name}-plugins-ogg
Requires:	%{name}-plugins-ole2
Requires:	%{name}-plugins-thumbnailgtk
Requires:	%{name}-plugins-rpm
Requires:	%{name}-plugins-tiff
Requires:	%{name}-plugins-gif
Requires:	%{name}-plugins-mime
Requires:	%{name}-plugins-flac
BuildArch:	noarch


%global pluginpkg(B:R:P:u)	\
%package plugins-%1	\
Summary:	The '%1' libextractor plugin\
Provides:	plugin(%{name}) = %1 %%{-P*}		\
%%{-u:Requires(post):	/usr/sbin/update-alternatives}	\
%%{-u:Requires(preun):	/usr/sbin/update-alternatives}	\
%%{-B:BuildRequires:	%%{-B*}}			\
Requires:	%{name}%{?_isa} = %{version}-%{release} %%{-R*}	\
	\
%description plugins-%1	\
libextractor is a simple library for keyword extraction.  libextractor\
does not support all formats but supports a simple plugging mechanism\
such that you can quickly add extractors for additional formats, even\
without recompiling libextractor.\
\
This package ships the '%1' plugin.\
\
%files plugins-%1			\
%plugindir/libextractor_%1.so*		\
%nil

%package plugins-base
Summary:	Base plugins for libextractor
Requires:	%{name}%{?_isa} = %{version}-%{release}

%pluginpkg flac -B flac-devel
%pluginpkg exiv2 -B exiv2-devel
%pluginpkg ogg -B libvorbis-devel
%pluginpkg ole2 -B libgsf-devel,glib2-devel
%pluginpkg rpm  -B rpm-devel
%pluginpkg tiff -B libtiff-devel
%pluginpkg gif  -B giflib-devel
%pluginpkg mime -B file-devel
%pluginpkg thumbnailgtk -B gtk%{gtkver}-devel,gtk2-devel,file-devel

## does not work with libjpeg-turbo
#pluginpkg jpeg -B libjpeg-devel

## is not detected...
## TODO: check whether supported in future versions
#pluginpkg gstreamer  -B gstreamer-devel,libgsf-gnome-devel,libgsf-devel,gtk


%description
libextractor is a simple library for keyword extraction.  libextractor
does not support all formats but supports a simple plugging mechanism
such that you can quickly add extractors for additional formats, even
without recompiling libextractor.  libextractor typically ships with a
dozen helper-libraries that can be used to obtain keywords from common
file-types.

libextractor is a part of the GNU project (http://www.gnu.org/).


%description plugins
libextractor is a simple library for keyword extraction.  libextractor
does not support all formats but supports a simple plugging mechanism
such that you can quickly add extractors for additional formats, even
without recompiling libextractor.

This is a metapackage which requires all supported plugins for
libextractor.

%description plugins-base
libextractor is a simple library for keyword extraction.  libextractor
does not support all formats but supports a simple plugging mechanism
such that you can quickly add extractors for additional formats, even
without recompiling libextractor.

This package contains all plugins for libextractor which do not
introduce additional dependencies.


%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'

%setup -q

install -pm644 %{SOURCE10} .
rm -f README.debian

sed -i 's!\(-L\(/usr\|\$with_qt\)/lib\|-I/usr/include\) !!g' configure


%build
export ac_cv_lib_mpeg2_mpeg2_init=no
export lt_cv_sys_dlsearch_path='/%{_lib}:%{_prefix}/%{_lib}:%plugindir'
%configure --disable-static	\
	--disable-rpath		\
	--disable-xpdf		\
	CPPFLAGS='-DLIBDIR=\"%{_libdir}\"'	\
	LDFLAGS='-Wl,--as-needed'

cat config.log

# build with --as-needed and disable rpath
sed -i \
	-e 's! -shared ! -Wl,--as-needed\0!g'					\
	-e '\!sys_lib_dlsearch_path_spec=\"/lib /usr/lib !s!\"/lib /usr/lib !\"/%{_lib} /usr/{%_lib} !g'	\
	-e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
	-e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
	libtool

# not SMP safe
make # %{?_smp_mflags}



%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

rm -f $RPM_BUILD_ROOT%plugindir/libextractor_thumbnail.so

echo '%defattr(-,root,root,-)' > filelists.base

for i in $RPM_BUILD_ROOT%plugindir/*.so; do
	readelf -a "$i" | \
	sed '/(NEEDED)/s!.*\[\(.*\)\].*!\1!p;d' | {
		target=base
		fname=${i##$RPM_BUILD_ROOT}
		while read lib; do
			lib=${lib%%.so*}
			case $lib in
				(libgcc_s|ld-linux*)			;;
				(libz|libdl)				;;
				(libextractor|libextractor_common)	;;
				(libc|libm|libpthread)	;;
				(libstdc++) ;;
				(*)
					target=other
					echo "$fname -> $lib"
					;;
			esac
		done

		case $target in
			(base)	echo "$fname" >> filelists.base;;
		esac
	}
done

rm -f $RPM_BUILD_ROOT%{_infodir}/dir

mv $RPM_BUILD_ROOT%{_bindir}/{,libextractor-}extract
mv $RPM_BUILD_ROOT%{_mandir}/man1/{,libextractor-}extract.1

%find_lang libextractor


%check
export LD_LIBRARY_PATH=$RPM_BUILD_ROOT%{_libdir}
export LIBEXTRACTOR_PREFIX=$RPM_BUILD_ROOT%{_libdir}/libextractor

### RPM test in rawhide fails with
# Got additional meta data of type 58 and format 1 with value `Thu Oct  2 09:44:33 2003' from plugin `rpm'
# Did not get expected meta data of type 58 and format 1 with value `Thu Oct  2 11:44:33 2003' from plugin `rpm'
# FAIL: test_rpm
#
### ignore it for now
if make check; then
   echo "Test succeeded unexpectedly! Revisit me!" >&2
   false
fi



%files -f libextractor.lang
%license COPYING
%doc AUTHORS ChangeLog NEWS README* TODO
%{_bindir}/*
%{_libdir}/libextractor.so.2*
%{_libdir}/libextractor_common.so.1*
%{_infodir}/*info*
%{_mandir}/man1/*
%dir %plugindir

%files plugins
%files plugins-base -f filelists.base

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/libextractor/*.so
%{_mandir}/man3/*
%{_libdir}/pkgconfig/*


%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Sep 14 2022 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.10-7
- Rebuilt for flac 1.4.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 02 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.10-1
- 1.10

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep 05 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.9-5
- Patch for CVE-2019-15531

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 10 22:13:20 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.9-3
- Rebuild for RPM 4.15

* Mon Jun 10 15:42:02 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.9-2
- Rebuild for RPM 4.15

* Mon Feb 11 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.9-1
- 1.9

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Rex Dieter <rdieter@fedoraproject.org> - 1.7-2
- pull in candidate fix for exiv2-0.27 (#1671085)
- fix rpath harder
- BR: gcc-c++

* Wed Jul 18 2018 Gwyn Ciesla <limburgher@gmail.com> - 1.7-1
- 1.7.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 11 2018 Sandro Mani <manisandro@gmail.com> - 1.6-4
- Rebuild (giflib)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 11 2017 Gwyn Ciesla <limburgher@gmail.com> - 1.6-2
- Patch for CVE-2017-17440.

* Fri Oct 20 2017 Gwyn Ciesla <limburgher@gmail.com> - 1.6-1
- 1.6

* Fri Aug 11 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.4-7
- Rebuilt after RPM update (№ 3)

* Thu Aug 10 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.4-6
- Rebuilt for RPM soname bump

* Thu Aug 10 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.4-5
- Rebuilt for RPM soname bump

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 12 2017 Gwyn Ciesla <limburgher@gmail.com> - 1.4-2
- Fix info path, BZ 1419284.

* Mon Jun 12 2017 Gwyn Ciesla <limburgher@gmail.com> - 1.4-1
- Update to 1.4, BZ 1460472.

* Tue May 02 2017 Rex Dieter <rdieter@fedoraproject.org> - 1.3-10
- rebuild for exiv2-0.26 (#1448439)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jul 29 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.3-7
- Rebuilt for rpm 4.12.90

* Wed Jun 24 2015 Rex Dieter <rdieter@fedoraproject.org> - 1.3-6
- rebuild (exiv2)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.3-4
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jan 06 2014 Jon Ciesla <limburgher@gmail.com> - 1.3-1
- Update to 1.3, BZ 1046656.

* Tue Dec 03 2013 Rex Dieter <rdieter@fedoraproject.org> - 1.2-2
- rebuild (exiv2)

* Thu Oct 24 2013 Jon Ciesla <limburgher@gmail.com> - 1.2-1
- Update to 1.2, BZ 1021197.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 05 2013 Jon Ciesla <limburgher@gmail.com> - 1.1-1
- Update to 1.1, BZ 981378.

* Tue Mar 19 2013 Jon Ciesla <limburgher@gmail.com> - 1.0.1-1903
- Additional macro cleanup.

* Thu Feb 28 2013 Jon Ciesla <limburgher@gmail.com> - 1.0.1-1902
- Fix macros.
- Fix FTBFS.

* Wed Feb 13 2013 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 1.0.1-1901
- workaround buildproblems in rawhide

* Sun Oct 21 2012 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 1.0.1-1900
- updated to 1.0.1
- changed license to GPLv3+
- obsoleted -pdf plugin (removed upstream due to licensing issues)
- obsoleted qt thumbnail plugin (removed upstream)
- registered new plugins

* Sun Oct 21 2012 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.6.3-1900
- rebuilt

* Sun Jul 22 2012 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.6.3-1805
- fixed arm build issue by using wildcard in ld-linux detection

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-1804
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul  2 2012 Marek Kasik <mkasik@redhat.com> - 0.6.3-1803
- Rebuild (poppler-0.20.1)

* Wed May 16 2012 Marek Kasik <mkasik@redhat.com> - 0.6.3-1802
- Rebuild (poppler-0.20.0)

* Wed May 02 2012 Rex Dieter <rdieter@fedoraproject.org> - 0.6.3-1801
- rebuild (exiv2)

* Tue Apr  3 2012 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.6.3-1800
- rebuilt for librpm api change

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-1701
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Dec 17 2011 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.6.3-1700
- updated to 0.6.3

* Mon Nov 28 2011 Ville Skyttä <ville.skytta@iki.fi> - 0.6.2-1606
- Run tests during build.

* Fri Oct 28 2011 Rex Dieter <rdieter@fedoraproject.org> - 0.6.2-1605
- rebuild(poppler)

* Fri Oct 14 2011 Rex Dieter <rdieter@fedoraproject.org> - 0.6.2-1604
- rebuild (exiv2)

* Fri Sep 30 2011 Marek Kasik <mkasik@redhat.com> - 0.6.2-1603
- Rebuild (poppler-0.18.0)

* Mon Sep 19 2011 Marek Kasik <mkasik@redhat.com> - 0.6.2-1602
- Rebuild (poppler-0.17.3)

* Fri Jul 15 2011 Marek Kasik <mkasik@redhat.com> - 0.6.2-1601
- Rebuild (poppler-0.17.0)

* Sun Mar 13 2011 Marek Kasik <mkasik@redhat.com> - 0.6.2-1508
- Rebuild (poppler-0.16.3)

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-1507
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 23 2011 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.6.2-1506
- rebuilt (librpm)

* Sat Jan 01 2011 Rex Dieter <rdieter@fedoraproject.org> - 0.6.2-1505
- rebuild (exiv2,poppler)

* Wed Dec 15 2010 Rex Dieter <rdieter@fedoraproject.org> - 0.6.2-1504
- rebuild (poppler)

* Sat Nov 06 2010 Rex Dieter <rdieter@fedoraproject.org> - 0.6.2-1503
- rebuilt (poppler)

* Sat Oct  9 2010 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.6.2-1502
- removed some old %%trigger scripts (solves #626959)
- removed pkgconfig path dependencies which are already implied by autodeps (#533957)

* Wed Oct  6 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 0.6.2-1501
- rebuild for poppler

* Mon Aug 30 2010 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.6.2-1500
- updated to 0.6.2

* Thu Aug 19 2010 Rex Dieter <rdieter@fedoraproject.org> - 0.6.1-1403
- rebuild (poppler)

* Mon May 31 2010 Rex Dieter <rdieter@fedoraproject.org> - 0.6.1-1402
- rebuild (exiv2)

* Wed May  5 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.6.1-1401
- Rebuild against new poppler

* Sat Mar 20 2010 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.6.1-1400
- updated to 0.6.1
- added some %%{?_isa} annotations
- require -rpm plugin again

* Sat Jan 16 2010 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.6.0-1301
- updated to 0.6.0
- removed -pluginpath patch; upstream changed plugin loading mechanism
  which fixed the problem solved by the patch
- removed 'update-alternatives' registration of thumbnail* plugins; it
  conflicts with new loading mechanism

* Mon Jan 04 2010 Rex Dieter <rdieter@fedoraproject.org> - 0.5.23-1304
- rebuild (exiv2)

* Sun Nov 22 2009 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.5.23-1303
- fixed plugin loading by disabling various autodetections (#452504)

* Sun Sep 13 2009 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de>
- conditionalized build of 'flac' plugin and noarch subpackages to
  ease packaging under RHEL5

* Sat Sep 12 2009 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.5.23-0
- updated to 0.5.23
- reenabled rpm plugin
- build exiv2 plugin with system library

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Mar  7 2009 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.5.22-1
- updated to 0.5.22
- disabled rpm plugin for now as it does not build with rpm-4.6
- disabled builtin xpdf plugin

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.20b-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Nov 26 2008 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.5.21-1
- updated to 0.5.21
- added -rpm plugin

* Wed Jul 16 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.5.20b-2
- fix license tag

* Sat Jun 21 2008 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.5.20b-1
- updated to 0.5.20b (SECURITY); fixes CVE-2008-1693 (xpdf embedded
  font vulnerability)
- build with -Wl,-as-needed
- fixed rpath issues

* Wed Feb 13 2008 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.5.19a-1
- updated to 0.5.19a
- added flac-plugin subpackage

* Sat Aug 25 2007 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.5.18a-1
- updated to 0.5.18a
- renamed 'extract' program to 'libextractor-extract'
- installed info file

* Sat Feb  3 2007 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.5.17a-1
- updated to 0.5.17a
- fixed URL
- removed -debug patch and the fixups in %%prep which were fixed
  upstream too

* Tue Jan  2 2007 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.5.17-2
- disabled debug messages
- fixed pkgconfig installation dir

* Tue Jan  2 2007 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.5.17-1
- updated to 0.5.17
- fixed 'datadir' brokeness
- added pkgconfig files

* Thu Dec 28 2006 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.5.16-4
- %%ghost'ified the files created by 'update-alternatives'
- initial fedora release (review #214087)
- removed glib-devel BR (should be glib2-devel which is implicated by gtk2-devel)

* Wed Dec 27 2006 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.5.16-3
- added a README.fedora
- removed the previously added 'Requires: plugin(%%name)'
- added the pdf plugin to the requirements of the -plugins subpackage

* Thu Dec 14 2006 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.5.16-2
- added a requirement for plugins to the main package
- do not ship README.debian anymore
- improved URL:

* Fri Nov 24 2006 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.5.16-1
- updated to 0.5.16; handling of libgsf linking of main library needs
  some rethinking: adding such a heavy dependency just to workaround a
  problem in one plugin is not acceptably

* Thu Nov  2 2006 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.5.15-2
- updated to 0.5.15

* Sun Oct  8 2006 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.5.14-1
- initial built
