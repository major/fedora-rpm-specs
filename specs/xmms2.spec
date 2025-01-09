Name:			xmms2
Summary: 		A modular audio framework and plugin architecture
Version:		0.9.4
Release:		2%{?dist}
License:		LGPL-2.1-or-later AND GPL-2.0-or-later AND BSD-3-Clause
# We can't use the upstream source tarball as-is, because it includes an mp4 decoder.
# Also, the ogg sample included is not under a FOSS license.
# https://github.com/xmms2/xmms2-devel/releases/download/%%{version}/xmms2-%%{version}.tar.xz
# Cleaning it is simple, just rm -rf src/plugins/mp4 mind.in.a.box-lament_snipplet.ogg
Source0:		%{name}-%{version}-clean.tar.xz
Source1:		xmms2-client-launcher.sh
# CC-BY
# taken from http://ccmixter.org/files/unreal_dm/38156
Source2:		unreal_dm-free.music.and.free.beer.ogg
# Apply c++ client fix from gentoo
Patch2:			xmms2-0.9.3-gentoo-cpp-client.patch
# Apply fix to faad plugin from gentoo
Patch3:			xmms2-0.9.3-gentoo-faad.patch
# Apply fix for curl buffer overrun
Patch4:			xmms2-0.9.3-curl-buffer-overrun-fix.patch
# Swap mind.in.a.box for free.music.and.free.beer
Patch11:		xmms2-0.9.3-no-mind-in-a-box.patch
URL:			http://wiki.xmms2.xmms.se/
BuildRequires:		git
BuildRequires:		python3-devel
BuildRequires:		python3-cython
BuildRequires:		python-unversioned-command
BuildRequires:		sqlite-devel
BuildRequires:		flac-devel
BuildRequires:		libofa-devel
BuildRequires:		libcdio-paranoia-devel
BuildRequires:		libdiscid-devel
BuildRequires:		libsmbclient-devel
BuildRequires:		libmpcdec-devel
BuildRequires:		gnome-vfs2-devel
BuildRequires:		pkgconfig(jack)
BuildRequires:		fftw-devel
BuildRequires:		libsamplerate-devel
BuildRequires:		libxml2-devel
BuildRequires:		alsa-lib-devel
BuildRequires:		libao-devel
BuildRequires:		libshout-devel
BuildRequires:		ruby-devel
BuildRequires:		ruby
BuildRequires:		ruby(rubygems)
BuildRequires:		perl-devel
BuildRequires:		perl-generators
BuildRequires:		boost-devel
BuildRequires:		pulseaudio-libs-devel
BuildRequires:		libmodplug-devel
BuildRequires:		ecore-devel
BuildRequires:		mpg123-devel
BuildRequires:		libmad-devel
BuildRequires:		doxygen
BuildRequires:		perl-Pod-Parser
BuildRequires:		pkgconfig(avahi-client)
BuildRequires:		pkgconfig(avahi-glib)
BuildRequires:		pkgconfig(avahi-compat-libdns_sd)
BuildRequires:		libvisual-devel
BuildRequires:		wavpack-devel
BuildRequires:		SDL-devel
BuildRequires:		glib2-devel
BuildRequires:		readline-devel
BuildRequires:		ncurses-devel
BuildRequires:		mac-devel
BuildRequires:		fluidsynth-devel
BuildRequires:		opusfile-devel
BuildRequires:		libmms-devel
BuildRequires:		libcurl-devel
BuildRequires:		flex
BuildRequires:		bison
# For /usr/share/perl5/ExtUtils/xsubpp
BuildRequires:		perl-ExtUtils-ParseXS
BuildRequires:		gcc
BuildRequires:		gcc-c++
BuildRequires:		waf
BuildRequires:		openssl-devel-engine, openssl-devel

Obsoletes:		xmms2-mad < 0.8-26
Provides:		xmms2-mad = %{version}-%{release}

Obsoletes:		xmms2-mac < 0.8-24
Provides:		xmms2-mac = %{version}-%{release}

Obsoletes:		xmms2-mms < 0.8-39
Provides:		xmms2-mms = %{version}-%{release}

Obsoletes:		xmms2-nyxmms2 < 0.8-89
Provides:		xmms2-nyxmms2 = %{version}-%{release}

%description
XMMS2 is an audio framework, but it is not a general multimedia player - it 
will not play videos. It has a modular framework and plugin architecture for 
audio processing, visualisation and output, but this framework has not been 
designed to support video. Also the client-server design of XMMS2 (and the 
daemon being independent of any graphics output) practically prevents direct 
video output being implemented. It has support for a wide range of audio 
formats, which is expandable via plugins. It includes a basic CLI interface 
to the XMMS2 framework, but most users will want to install a graphical XMMS2 
client (such as gxmms2 or esperanza).

%package devel
Summary:	Development libraries and headers for XMMS2
Requires:	glib2-devel, boost-devel
Requires:	pkgconfig
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Development libraries and headers for XMMS2. You probably need this to develop
or build new plugins for XMMS2.

%package docs
Summary:	Development documentation for XMMS2
Requires:	%{name} = %{version}-%{release}

%description docs
API documentation for the XMMS2 modular audio framework architecture.

%package perl
Summary:	Perl support for XMMS2
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
Requires:	%{name} = %{version}-%{release}

%description perl
Perl bindings for XMMS2.

%package python3
Summary:	Python3 support for XMMS2
Requires:	%{name} = %{version}-%{release}

%description python3
Python3 bindings for XMMS2.

%package ruby
Summary:	Ruby support for XMMS2
Requires:	%{name} = %{version}-%{release}
Requires:	ruby(release)

%description ruby
Ruby bindings for XMMS2.

%prep
%setup -q -n %{name}-%{version}
%patch -P2 -p1 -b .cpp-client
%patch -P3 -p1 -b .faad
%patch -P4 -p1 -b .overrun
%patch -P11 -p1 -b .nomind
cp %{SOURCE2} .

# This header doesn't need to be executable
chmod -x src/include/xmmsclient/xmmsclient++/dict.h

%build
export CFLAGS="%{optflags} -DHAVE_G_FILE_QUERY_FILE_TYPE"
export CPPFLAGS="%{optflags}"
export LIBDIR="%{_libdir}"
export XSUBPP="%{_bindir}/xsubpp"

./waf configure --prefix=%{_prefix} --libdir=%{_libdir} --with-ruby-libdir=%{ruby_vendorlibdir} --with-ruby-archdir=%{ruby_vendorarchdir} \
--with-perl-archdir=%{perl_archlib} --with-pkgconfigdir=%{_libdir}/pkgconfig -j1
./waf build -v %{?_smp_mflags}

# make the docs
doxygen

%install
export LIBDIR="%{_libdir}"
./waf install --destdir=%{buildroot} --prefix=%{_prefix} --libdir=%{_libdir} --with-ruby-libdir=%{ruby_vendorlibdir} --with-ruby-archdir=%{ruby_vendorarchdir} \
  --with-perl-archdir=%{perl_archlib} --with-pkgconfigdir=%{_libdir}/pkgconfig

# exec flags for debuginfo
chmod +x %{buildroot}%{_libdir}/%{name}/* %{buildroot}%{_libdir}/libxmmsclient*.so* \
	%{buildroot}%{perl_archlib}/auto/Audio/XMMSClient/XMMSClient.so %{buildroot}%{ruby_vendorarchdir}/xmmsclient_*.so

# Convert to utf-8
for i in %{buildroot}%{_mandir}/man1/*.gz; do
	gunzip $i;
done
for i in %{buildroot}%{_mandir}/man1/*.1 xmms2-%{version}.ChangeLog; do
	iconv -o $i.iso88591 -f iso88591 -t utf8 $i
	mv $i.iso88591 $i
done

install -m0755 %{SOURCE1} %{buildroot}%{_bindir}

%ldconfig_scriptlets

%files
%license COPYING COPYING.GPL COPYING.LGPL
%doc AUTHORS xmms2-%{version}.ChangeLog README.mdown
%{_bindir}/%{name}*
%{_bindir}/_xmms2-migrate-collections-v0
%{_bindir}/s4
%{_bindir}/sqlite2s4
%{_libdir}/libxmmsclient*.so.*
%{_libdir}/%{name}
%{_mandir}/man1/%{name}*
%{_datadir}/pixmaps/%{name}*
%{_datadir}/%{name}

%files devel
%{_includedir}/%{name}/
%{_libdir}/libxmmsclient*.so
%{_libdir}/pkgconfig/%{name}-*.pc

%files docs
%doc doc/xmms2/html

%files perl
%{perl_archlib}/Audio/
%{perl_archlib}/auto/Audio/

%files python3
%{python3_sitearch}/xmmsclient/

%files ruby
%{ruby_vendorlibdir}/xmmsclient.rb
%{ruby_vendorlibdir}/xmmsclient/
%{ruby_vendorarchdir}/xmmsclient_ecore.so
%{ruby_vendorarchdir}/xmmsclient_ext.so
%{ruby_vendorarchdir}/xmmsclient_glib.so

%changelog
* Wed Jan 08 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.4-2
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.4

* Tue Oct 22 2024 Tom Callaway <spot@fedoraproject.org> - 0.9.4-1
- update to 0.9.4

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 12 2024 Jitka Plesnikova <jplesnik@redhat.com> - 0.9.3-6
- Perl 5.40 rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 0.9.3-5
- Rebuilt for Python 3.13

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 03 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.3-3
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.3

* Sun Nov 19 2023 Leigh Scott <leigh123linux@gmail.com> - 0.9.3-2
- provides/obsoletes xmms2-mms (from rpmfusion)

* Tue Sep 12 2023 Tom Callaway <spot@fedoraproject.org> - 0.9.3-1
- update to 0.9.3
- add BR: mac-devel
- provides/obsoletes xmms2-mac (from rpmfusion)
- provides/obsoletes xmms2-nyxmms2 (upstream dropped that naming)

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-88
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 0.8-87
- Perl 5.38 rebuild

* Fri Mar 17 2023 Yaakov Selkowitz <yselkowi@redhat.com> - 0.8-86
- Rebuilt for libmpcdec 1.3.0

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-85
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 04 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.8-84
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.2

* Thu Sep 15 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.8-83
- Rebuild for new flac

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-82
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.8-81
- Perl 5.36 rebuild

* Wed Jan 26 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.8-80
- F-36: rebuild against ruby31

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-79
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 0.8-78
- Rebuilt with OpenSSL 3.0.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-77
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.8-76
- Perl 5.34 rebuild

* Wed Feb 03 2021 Kalev Lember <klember@redhat.com> - 0.8-75
- Drop unused gamin-devel build dep

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-74
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 06 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.8-73
- F-34: rebuild against ruby 3.0

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-72
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-71
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.8-70
- Perl 5.32 rebuild

* Tue Mar 31 2020 Adrian Reber <adrian@lisas.de> - 0.8-69
- Rebuilt for libcdio-2.1.0

* Fri Feb 28 2020 Tom Callaway <spot@fedoraproject.org> - 0.8-68
- abandon all hope ye who enter here

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-67
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 18 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.8-66
- Remove python2 related files explicitly for F-32 for now

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-65
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 04 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.8-64
- Perl 5.30 re-rebuild updated packages

* Mon Jun 03 2019 Xavier Bachelot <xavier@bachelot.org> - 0.8-63
- Obsoletes xmms2-mad for proper upgrade path.

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.8-62
- Perl 5.30 rebuild

* Tue May 28 2019 Petr Pisar <ppisar@redhat.com> - 0.8-61
- Build-require python2 because waf uses it (bug #1711261)
* Mon Apr 15 2019 Xavier Bachelot <xavier@bachelot.org> - 0.8-60
- Add BuildRequires: libmad-devel for mad plugin.

* Sun Mar 17 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8-59
- Subpackage python2-xmms2 has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Feb 18 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.8-58
- Yet more python2 explicit usage
- Remove redundant BuildRequires

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8-58
- Rebuild for readline 8.0

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-57
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 23 2018 Tom Callaway <spot@fedoraproject.org> - 0.8-56
- add BuildRequires: gcc, gcc-c++
- fix build to use python2 explicitly

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-55
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.8-54
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-53
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Adrian Reber <adrian@lisas.de> - 0.8-52
- Rebuilt for libcdio-2.0.0

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 0.8-51
- Rebuilt for switch to libxcrypt

* Fri Jan 05 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.8-50
- F-28: rebuild for ruby25

* Mon Nov 20 2017 Tom Callaway <spot@fedoraproject.org> - 0.8-49
- remove non-free ogg sample

* Fri Sep  1 2017 Tom Callaway <spot@fedoraproject.org> - 0.8-48
- rebuild against fixed efl

* Sun Aug 20 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.8-47
- Add Provides for the old name without %%_isa

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.8-46
- Python 2 binary package renamed to python2-xmms2
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.8-43
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 0.8-41
- Rebuilt for Boost 1.63

* Fri Jan 13 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.8-40
- F-26: rebuild for ruby24

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.8-39
- Rebuild for readline 7.x

* Fri Nov 18 2016 Tom Callaway <spot@fedoraproject.org> - 0.8-38
- add mpg123-devel to BuildRequires for mp3 support

* Mon Nov 14 2016 Adrian Reber <adrian@lisas.de> - 0.8-37
- Rebuilt for libcdio-0.94

* Tue Oct 18 2016 Tom Callaway <spot@fedoraproject.org> - 0.8-36
- fix build against openssl 1.1

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-35
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.8-34
- Perl 5.24 rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 16 2016 Jonathan Wakely <jwakely@redhat.com> - 0.8-32
- Rebuilt for Boost 1.60

* Thu Jan 14 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.8-31
- F-24: rebuild against ruby23

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 0.8-30
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-29
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 0.8-28
- rebuild for Boost 1.58

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.8-26
- Perl 5.22 rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.8-25
- Rebuilt for GCC 5 C++11 ABI change

* Mon Jan 26 2015 Petr Machata <pmachata@redhat.com> - 0.8-24
- Rebuild for boost 1.57.0

* Fri Jan 16 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.8-23
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_2.2
- Remove deprecated Config:: usage, do some trick on waf

* Tue Nov 11 2014 Adrian Reber <adrian@lisas.de> - 0.8-22
- Rebuilt for libcdio-0.93

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.8-21
- Perl 5.20 rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 0.8-18
- Rebuild for boost 1.55.0

* Wed May  7 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.8-17
- Patch for libmodplug pkgconfig header dir output change
  (c.f. Debian bug 652139, 724487)
- Patch for vorbisenc pkgconfig libs dir output change

* Tue May  6 2014 Tom Callaway <spot@fedoraproject.org> - 0.8-16
- rebuild for new ruby

* Mon Dec 16 2013 Adrian Reber <adrian@lisas.de> - 0.8-15
- Rebuilt for libcdio-0.92

* Thu Sep 26 2013 Rex Dieter <rdieter@fedoraproject.org> 0.8-14
- add explicit avahi build deps

* Sun Aug 11 2013 Tom Callaway <spot@fedoraproject.org> - 0.8-13
- add missing BuildRequires
- add disgusting hack to this awful package to get it building again. whoever invented waf 
  should be forced to endure severe punishment.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 0.8-11
- Rebuild for boost 1.54.0

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.8-10
- Perl 5.18 rebuild

* Tue Apr 02 2013 Vít Ondruch <vondruch@redhat.com> - 0.8-9
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.8-8
- Rebuild for Boost-1.53.0

* Mon Jan 07 2013 Adrian Reber <adrian@lisas.de> - 0.8-7
- Rebuilt for libcdio-0.90

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 08 2012 Petr Pisar <ppisar@redhat.com> - 0.8-5
- Perl 5.16 rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-4
- Rebuilt for c++ ABI breakage

* Wed Feb 08 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.8-3
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec  5 2011 Tom Callaway <spot@fedoraproject.org> - 0.8-1
- update to 0.8

* Sun Nov 20 2011 Adrian Reber <adrian@lisas.de> - 0.7-11
- Rebuild for libcdio-0.83

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.7-10
- Perl mass rebuild

* Thu Jun 09 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.7-9
- Perl 5.14 mass rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Nov 17 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 0.7-7
- bump for libecore

* Thu Sep 02 2010 Rakesh Pandit <rakesh@fedoraproject.org> - 0.7-6
- Bump for libao

* Sat Jul 31 2010 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 0.7-5
- Add -j1 to the "./waf configure" line.

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.7-4.1
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Tue Jun 29 2010 Mike McGrath <mmcgrath@redhat.com> - 0.7-3.1
- Rebuild to fix broken libcore-ver-svn dep

* Wed Jun 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.7-3
- Mass rebuild with perl-5.12.0

* Tue Jun  1 2010 Ville Skyttä <ville.skytta@iki.fi> - 0.7-2
- Rebuild.

* Fri Jan 22 2010 Adrian Reber <adrian@lisas.de> - 0.6-7
- Rebuild for libcdio-0.82

* Tue Jan 19 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 0.6-6
- rebuild for new boost

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 0.6-5
- rebuild against perl 5.10.1

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 0.6-4
- rebuilt with new openssl

* Tue Aug 11 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 0.6-3
- BuildRequires: glib2-devel, readline-devel, ncurses-devel

* Tue Aug 11 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 0.6-2
- BuildRequires: SDL-devel

* Tue Aug 11 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 0.6-1
- update to 0.6

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 18 2009 Tomas Mraz <tmraz@redhat.com> - 0.5-5
- rebuild with new openssl

* Tue Jan 13 2009 Adrian Reber <adrian@lisas.de> - 0.5-4
- Rebuild for libcdio-0.81

* Wed Dec 17 2008 Benjamin Kosnik  <bkoz@redhat.com> - 0.5-3
- Rebuild for boost-1.37.0.

* Wed Dec 10 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.5-2
- new docs subpackage
- many cleanups from package review

* Thu Dec 4 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.5-1
- Initial package for Fedora
