Name:           linphone
Version:        3.6.1
Release:        49%{?dist}
Summary:        Phone anywhere in the whole world by using the Internet

License:        GPLv2+
URL:            http://www.linphone.org/

Source0:        http://download.savannah.gnu.org/releases/linphone/3.7.x/sources/%{name}-%{version}.tar.gz
Patch0:         linphone-3.6.1-rootca.patch
Patch1:         linphone-3.6.1-arm.patch
Patch2:		linphone-3.6.1-theora-fix.patch
Patch3:		linphone-3.6.1-upnp-fix.patch

Obsoletes: ortp <= 1:0.24.2-2

# for video support
BuildRequires:  gcc-c++
BuildRequires:  glew-devel
BuildRequires:  libtheora-devel
BuildRequires:  libv4l-devel
BuildRequires:  libvpx-devel
# xxd used in mediastreamer2/src/Makefile.in
BuildRequires:  vim-common

BuildRequires:  libosip2-devel >= 3.6.0
BuildRequires:  libeXosip2-devel >= 3.6.0
BuildRequires:  libpcap-devel
BuildRequires:  libsoup-devel
BuildRequires:  libudev-devel
# on i386, armv7hl error: libupnp uses large file support, so users must do that, too
# Disabled for f34
#BuildRequires:  libupnp-devel
BuildRequires:  openssl-devel
BuildRequires:  pulseaudio-libs-devel

BuildRequires:  sqlite-devel
BuildRequires:  readline-devel
BuildRequires:  ncurses-devel

BuildRequires:  libnotify-devel
BuildRequires:  gtk2-devel >= 2.16
BuildRequires:  alsa-lib-devel

BuildRequires:  opus-devel
BuildRequires:  speex-devel >= 1.2
BuildRequires:  speexdsp-devel >= 1.2
BuildRequires:  spandsp-devel
BuildRequires:  gsm-devel

BuildRequires:  desktop-file-utils

BuildRequires:  perl(XML::Parser)

BuildRequires:  libglade2-devel

BuildRequires:  intltool
BuildRequires:  doxygen

BuildRequires:  libtool

BuildRequires:  ortp-devel >= 1:0.22.0
BuildRequires: make
Requires:       ortp%{?_isa} >= 1:0.22.0

%description
Linphone is mostly sip compliant. It works successfully with these
implementations:
    * eStara softphone (commercial software for windows)
    * Pingtel phones (with DNS enabled and VLAN QOS support disabled).
    * Hotsip, a free of charge phone for Windows.
    * Vocal, an open source SIP stack from Vovida that includes a SIP proxy
        that works with linphone since version 0.7.1.
    * Siproxd is a free sip proxy being developed by Thomas Ries because he
        would like to have linphone working behind his firewall. Siproxd is
        simple to setup and works perfectly with linphone.
    * Partysip aims at being a generic and fully functionnal SIP proxy. Visit
        the web page for more details on its functionalities.

Linphone may work also with other sip phones, but this has not been tested yet.

%package devel
Summary:        Development libraries for linphone
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       linphone-mediastreamer-devel%{?_isa} = %{version}-%{release}
Requires:       glib2-devel%{?_isa}

%description    devel
Libraries and headers required to develop software with linphone.

%package mediastreamer
Summary:        A media streaming library for telephony applications

%description mediastreamer
Mediastreamer2 is a GPL licensed library to make audio and video
real-time streaming and processing. Written in pure C, it is based
upon the oRTP library.

%package mediastreamer-devel
Summary:        Development libraries for mediastreamer2
Requires:       linphone-mediastreamer%{?_isa} = %{version}-%{release}
Requires:       ortp-devel%{?_isa}

%description mediastreamer-devel
Libraries and headers required to develop software with mediastreamer2.

%prep
%setup0 -q
%patch0 -p1 -b .rootca
%ifarch %{arm}
%patch1 -p1 -b .arm
%endif
%patch2 -p1 -b .theora-fix
%if 0%{?fedora} > 28
%patch3 -p2 -b .upnp-fix
%endif

autoreconf -i -f

# remove bundled oRTP
#rm -rf oRTP

# Fix encoding
for f in share/cs/*.1; do
  /usr/bin/iconv -f iso-8859-2 -t utf-8 -o $f.new $f
  sed -i -e 's/Encoding: ISO-8859-2/Encoding: UTF-8/' $f.new
  mv $f.new $f
done
for f in ChangeLog AUTHORS; do
  /usr/bin/iconv -f iso-8859-1 -t utf-8 -o $f.new $f
  mv $f.new $f
done


%build
%configure --disable-static \
           --enable-glx \
           --disable-ffmpeg \
           --disable-rpath \
           --enable-console_ui=yes \
           --enable-gtk_ui=yes \
           --enable-ipv6 \
           --enable-truespeech \
           --enable-alsa \
           --disable-strict \
           --enable-nonstandard-gsm \
           --enable-rsvp \
           --enable-ssl \
%ifarch i686 armv7hl
           --disable-upnp \
%endif
           --enable-zrtp \
           --enable-external-ortp

make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

# from oRTP install only %{_libdir}/libortp.so.9*
rm -rf $RPM_BUILD_ROOT%{_includedir}/ortp $RPM_BUILD_ROOT%{_datadir}/doc/ortp-0.22.0 $RPM_BUILD_ROOT%{_libdir}/pkgconfig/ortp.pc $RPM_BUILD_ROOT%{_libdir}/libortp.so

%find_lang %{name}
%find_lang mediastreamer

desktop-file-install \
  --delete-original \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  --remove-category Application \
  --add-category Telephony \
  --add-category GTK \
  $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

# move docs to %%doc
mkdir -p doc/linphone doc/mediastreamer
mv $RPM_BUILD_ROOT%{_datadir}/doc/linphone*/html doc/linphone
mv $RPM_BUILD_ROOT%{_datadir}/doc/mediastreamer*/html doc/mediastreamer

%ldconfig_scriptlets

%ldconfig_scriptlets mediastreamer

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_bindir}/linphone
%{_bindir}/linphonec
%{_bindir}/linphonecsh
%{_bindir}/lpc2xml_test
%{_bindir}/xml2lpc_test
%{_libdir}/liblinphone.so.5*
%{_libdir}/liblpc2xml.so.0*
%{_libdir}/libxml2lpc.so.0*
#{_libdir}/libortp.so.9*
%{_mandir}/man1/*
%lang(cs) %{_mandir}/cs/man1/*
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/gnome/help/linphone
%{_datadir}/pixmaps/linphone
%{_datadir}/sounds/linphone
%{_datadir}/linphone

%files devel
%doc doc/linphone/html
%{_includedir}/linphone
%{_libdir}/liblinphone.so
%{_libdir}/liblpc2xml.so
%{_libdir}/libxml2lpc.so
%{_libdir}/pkgconfig/linphone.pc

%files mediastreamer -f mediastreamer.lang
%doc mediastreamer2/AUTHORS mediastreamer2/ChangeLog mediastreamer2/COPYING
%doc mediastreamer2/NEWS mediastreamer2/README
%{_bindir}/mediastream
%{_libdir}/libmediastreamer_base.so.3*
%{_libdir}/libmediastreamer_voip.so.3*
%{_datadir}/images

%files mediastreamer-devel
%doc doc/mediastreamer/html
%{_includedir}/mediastreamer2
%{_libdir}/libmediastreamer_base.so
%{_libdir}/libmediastreamer_voip.so
%{_libdir}/pkgconfig/mediastreamer.pc

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Feb 10 2022 Orion Poplawski <orion@nwra.com> - 3.6.1-48
- Rebuild for glew 2.2

* Thu Jan 27 2022 Tom Callaway <spot@fedoraproject.org> - 3.6.1-47
- rebuild for libvpx

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 3.6.1-45
- Rebuilt with OpenSSL 3.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Feb 09 2021 Nicolas Chauvet <kwizart@gmail.com> - 3.6.1-43
- Rebuilt for upnp (disable)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-41
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 16 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.6.1-39
- libupnp rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan  7 2020 Tom Callaway <spot@fedoraproject.org> - 3.6.1-37
- rebuild for libsrtp2

* Thu Dec 26 2019 Stuart Gathman <stuart@gathman.org> - 3.6.1-36
- Reenable external-ortp, zrtp (may try bundling again later)

* Mon Oct  7 2019 Alexey Kurov <nucleo@fedoraproject.org> - 3.6.1-35
- Obsoletes: ortp <= 1:0.24.2-2

* Mon Sep 30 2019 Alexey Kurov <nucleo@fedoraproject.org> - 3.6.1-34
- build bundled oRTP
- disabled zrtp support

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 10 2019 Alexey Kurov <nucleo@fedoraproject.org> - 3.6.1-32
- disabled upnp on i686 and armv7hl

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.6.1-31
- Rebuild for readline 8.0

* Tue Feb 05 2019 Björn Esser <besser82@fedoraproject.org> - 3.6.1-30
- rebuilt (libvpx)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 23 2018 Nicolas Chauvet <kwizart@gmail.com> - 3.6.1-28
- Rebuilt for glew 2.1.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun May 27 2018 Alexey Kurov <nucleo@fedoraproject.org> - 3.6.1-26
- apply upnp patch for F29+

* Sun May 27 2018 Alexey Kurov <nucleo@fedoraproject.org> - 3.6.1-25
- fix upnp FTBFS (rhbz #1582911)

* Fri Apr 13 2018 Nicolas Chauvet <kwizart@gmail.com> - 3.6.1-24
- Rebuilt for libupnp 1.8x

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Feb  2 2018 Tom Callaway <spot@fedoraproject.org> - 3.6.1-22
- again.

* Fri Jan 26 2018 Tom Callaway <spot@fedoraproject.org> - 3.6.1-21
- rebuild for new libvpx

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 3.6.1-17
- Rebuild for readline 7.x

* Tue Jan 10 2017 Orion Poplawski <orion@cora.nwra.com> - 3.6.1-16
- Rebuild for glew 2.0.0

* Fri Jul 22 2016 Tom Callaway <spot@fedoraproject.org> - 3.6.1-15
- rebuild for libvpx 1.6.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Adam Jackson <ajax@redhat.com> 3.6.1-13
- --disable-strict to work around libsoup deprecation warnings

* Thu Jan 14 2016 Adam Jackson <ajax@redhat.com> - 3.6.1-12
- Rebuild for glew 1.13

* Tue Dec  1 2015 Tom Callaway <spot@fedoraproject.org> - 3.6.1-11
- rebuild for libvpx 1.5.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 3.6.1-9
- Rebuilt for GCC 5 C++11 ABI change

* Mon Apr  6 2015 Tom Callaway <spot@fedoraproject.org> - 3.6.1-8
- rebuild for libvpx 1.4.0

* Thu Jan 29 2015 Peter Robinson <pbrobinson@fedoraproject.org> 3.6.1-7
- Add speexdsp-devel as a dep to fix FTBFS

* Fri Nov 14 2014 Tom Callaway <spot@fedoraproject.org> - 3.6.1-6
- rebuild for new libsrtp

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Nov 18 2013 Dave Airlie <airlied@redhat.com> - 3.6.1-3
- rebuilt for GLEW 1.10

* Sat Jul 27 2013 Alexey Kurov <nucleo@fedoraproject.org> - 3.6.1-2
- use /etc/ssl/certs/ca-bundle.crt root_ca
- fix armv7hl compilation

* Sun Jul  7 2013 Alexey Kurov <nucleo@fedoraproject.org> - 3.6.1-1
- linphone-3.6.1

* Fri Apr 26 2013 Jon Ciesla <limburgher@gmail.com> - 3.5.2-8
- Drop desktop vendor tag.

* Sat Mar 23 2013 Alexey Kurov <nucleo@fedoraproject.org> - 3.5.2-7
- autoreconf in %%prep (#926078)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec 31 2012 Alexey Kurov <nucleo@fedoraproject.org> - 3.5.2-5
- add -mediastreamer and -mediastreamer-devel subpackages

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Mar  5 2012 Alexey Kurov <nucleo@fedoraproject.org> - 3.5.2-3
- drop regression patch

* Mon Feb 27 2012 Alexey Kurov <nucleo@fedoraproject.org> - 3.5.2-2
- install docs in -devel
- update glib-2.31 patch
- revert commit causing regression in 3.5.2

* Wed Feb 22 2012 Alexey Kurov <nucleo@fedoraproject.org> - 3.5.2-1
- linphone-3.5.2

* Sun Feb 19 2012 Alexey Kurov <nucleo@fedoraproject.org> - 3.5.1-1
- linphone-3.5.1
- BR: libsoup-devel
- Requires: ortp >= 1:0.18.0

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 27 2011 Alexey Kurov <nucleo@fedoraproject.org> - 3.5.0-2
- enable spandsp

* Mon Dec 26 2011 Alexey Kurov <nucleo@fedoraproject.org> - 3.5.0-1
- linphone-3.5.0
- add BR: libnotify-devel
- disable spandsp (#691039)

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 3.4.3-2
- Rebuild for new libpng

* Fri Sep  2 2011 Alexey Kurov <nucleo@fedoraproject.org> - 3.4.3-1
- linphone-3.4.3
- BR: openssl-devel libsamplerate-devel gettext
- BR: pulseaudio-libs-devel jack-audio-connection-kit-devel
- drop 3.2.1 patches

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Mar 17 2010 Jesse Keating <jkeating@redhat.com> - 3.2.1-2
- Apply patches from bug 555510 to update linphone
- Drop the doc/mediastreamer dir from devel package

* Mon Mar 01 2010 Adam Jackson <ajax@redhat.com> 2.1.1-5
- Rebuild for libortp.so.7

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Mar 13 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.1.1-3
- Re-base patches to fix rebuild breakdowns.
- Fix various autotool source file bugs.
- Use pre-built autotool-generated files.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 14 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 2.1.1-1
- Update to 2.1.1

* Fri Feb  1 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 2.1.0-1
- Update to 2.1.0

* Wed Aug 29 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.7.1-4
- Update license tag.

* Wed Aug 29 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.7.1-3
- Update license tag.

* Mon May 14 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.7.1-2
- Add patch for compiling against external GSM library.

* Tue Apr 17 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.7.1-1
- Update to 1.7.1
- Drop linphone-1.0.1-desktop.patch, linphone-1.4.1-libs.patch and
  linphone-1.5.1-osipcompat.patch

* Fri Mar 16 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.0-4
- Fix up encodings in Czech manpages

* Fri Mar 16 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.0-3
- Move autoheader after aclocal, fixes 232592

* Mon Jan 29 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.0-2
- Fix buildrequires

* Mon Jan 29 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.0-1
- Update to 1.6.0

* Wed Nov 22 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.5.1-2
- Mark translated man pages with lang macro

* Tue Nov 21 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.5.1-1
- Update to 1.5.1

* Thu Oct 26 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.5.0-2
- Don't forget to add new files and remove old ones!

* Thu Oct 26 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.5.0-1
- Update to 1.5.0
- Fix spelling error in description.
- Remove invalid categories on desktop file.

* Wed Aug 30 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2.0-7
- Bump release so that I can "make tag"

* Wed Aug 30 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2.0-6
- Add BR for perl(XML::Parser) so that intltool will work.

* Wed Aug 30 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2.0-5
- Bump release and rebuild.

* Mon Feb 13 2006 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 1.2.0-2
- Rebuild for Fedora Extras 5

* Wed Feb  8 2006 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 1.2.0-1
- Added version for speex-devel BR (#179879)

* Tue Jan 24 2006 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 1.2.0-2
- Fixed selecting entry from address book (#177189)

* Tue Jan  3 2006 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 1.2.0-1
- Upstream update

* Mon Dec  5 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 1.1.0-2
- Added version on ortp-devel

* Mon Dec  5 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 1.1.0-1
- Upstream update

* Wed Nov 30 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 1.0.1-5
- Remove ortp documentation for -devel

* Wed Nov 30 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 1.0.1-4
- Split out ortp

* Fri May 27 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 1.0.1-3
- Fix multiple menu entry and missing icon (#158975)
- Clean up spec file

* Fri May  6 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 1.0.1-2
- Add disttag to Release

* Fri Apr  8 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 1.0.1-2
- Remove -Werror from configure for now
- Fix .desktop file to have Terminal=false instead of 0

* Thu Mar 24 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 1.0.1-1
- Upstream update
- Separated ortp
- Added %%doc

* Wed Mar 23 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.12.2-7
- pkgconfig and -devel fixes

* Wed Mar 23 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.12.2-6
- Fix build on x86_64

* Sat Mar 19 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.12.2-5
- %%

* Sat Mar 19 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.12.2-4
- Used %%find_lang
- Tightened up %%files
- Streamlined spec file

* Thu Mar 17 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.12.2-3
- Broke %%description at 80 columns

* Wed Mar 16 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.12.2-2
- Removed explicit Requires

* Tue Mar 15 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.12.2-1
- Bump release to 1
- Cleaned up the -docs and -speex patches

* Fri Jan 21 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0:0.12.2-0.iva.1
- Fixed a silly spec error

* Fri Jan 21 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0:0.12.2-0.iva.0
- Initial RPM release.
