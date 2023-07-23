Name:    pjproject
Summary: Libraries for building embedded/non-embedded VoIP applications
Version: 2.10
Release: 8%{?dist}
License: GPLv2+
URL:     http://www.pjsip.org

Source0: https://github.com/pjsip/pjproject/archive/%{version}/%{name}-%{version}.tar.gz

# Tell the build system not to use most of the third_party directory
Patch1: pjproject_no_third_party.patch
# Keep the .pc file clean
# see https://bugzilla.redhat.com/show_bug.cgi?id=728302#c66
Patch2: pjproject_fixup_pc_file.patch
# Add a config_site.h file to increase performance and set reasonable server
# configuration for running as a server and not just a client
Patch3: pjproject_config_site.patch
# Fix ARMv7 endianness
Patch4: pjproject-armv7.patch
# Add aarch64 detection
Patch5: pjproject-aarch64.patch
# Add ppc64 detection
Patch6: pjproject-ppc64.patch
# Add s390 detection
Patch7: pjproject-s390.patch
# Don't use SSE2 if it is not available
Patch8: pjproject-sse2-2.9.patch

BuildRequires: make
BuildRequires: autoconf
BuildRequires: alsa-lib-devel
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: gsm-devel
BuildRequires: libsrtp-devel
BuildRequires: libuuid-devel
BuildRequires: openssl-devel
BuildRequires: pkgconfig
BuildRequires: portaudio-devel
BuildRequires: speex-devel
BuildRequires: speexdsp-devel
BuildRequires: libyuv-devel

# See third_party/webrtc/README.chromium
# (version shipped in Fedora (webrtc-audio-processing) is incompatible)
Provides: bundled(webrtc) = 90

# See third_party/srtp/VERSION
# (libsrtp-2.3.0 shipped in Fedora seems incompatible,
# results in Error initializing SRTP library: cipher failure [status=259807])
Provides: bundled(srtp) = 2.1.0


%description
This package provides the Open Source, comprehensive, high performance,
small footprint multimedia communication libraries written in C
language for building embedded/non-embedded VoIP applications.
It contains:
- PJSIP - Open Source SIP Stack
- PJMEDIA - Open Source Media Stack
- PJNATH - Open Source NAT Traversal Helper Library
- PJLIB-UTIL - Auxiliary Library
- PJLIB - Ultra Portable Base Framework Library
- PJSUA2 - Object Oriented abstractions layer for PJSUA


%package devel
Summary: Development files to use pjproject
Requires: %{name} = %{version}-%{release}


%description devel
Header information for:
- PJSIP - Open Source SIP Stack
- PJMEDIA - Open Source Media Stack
- PJNATH - Open Source NAT Traversal Helper Library
- PJLIB-UTIL - Auxiliary Library
- PJLIB - Ultra Portable Base Framework Library


%package -n pjsua
Summary: command line SIP user agent
Requires: %{name} = %{version}-%{release}


%description -n pjsua
pjsua is an open source command line SIP user agent (softphone)
that is used as the reference implementation for PJSIP, PJNATH, and PJMEDIA.
Despite its simple command line appearance, it does pack many features!



%prep
%autosetup -p1 -n %{name}-%{version}
# Update old FSF addresses
grep -ril '59 Temple Place' * | xargs sed -i 's/59 Temple Place,\s\+Suite 330,/51 Franklin Street, Fifth Floor,/im'
grep -ril '59 Temple Place' * | xargs sed -i 's/59 Temple Place - Suite 330,/51 Franklin Street, Fifth Floor,/im'
grep -ril 'Boston, MA\s\+02111-1307' * | xargs sed -i 's/Boston,\s\+MA\s\+02111-1307/Boston, MA  02110-1335/im'

# make sure we don't bundle these third-party libraries
# (They're excluded through ./configure, but this is an
# additional safety net)
# Kept bundled libraries: see Provides: bundled(...) above
rm -rf third_party/BaseClasses
rm -rf third_party/bdsound
rm -rf third_party/bin
rm -rf third_party/g7221
rm -rf third_party/gsm
rm -rf third_party/ilbc
rm -rf third_party/milenage
rm -rf third_party/mp3
rm -rf third_party/resample
rm -rf third_party/speex
# rm -rf third_party/srtp
# rm -rf third_party/webrtc
rm -rf third_party/threademulation
rm -rf third_party/yuv
rm -rf third_party/build/baseclasses
rm -rf third_party/build/g7221
rm -rf third_party/build/gsm
rm -rf third_party/build/ilbc
rm -rf third_party/build/milenage
rm -rf third_party/build/resample
rm -rf third_party/build/samplerate
rm -rf third_party/build/speex
# rm -rf third_party/build/srtp
# rm -rf third_party/build/webrtc
rm -rf third_party/build/yuv


%build
# Regenerate aconfigure for Patch8
autoconf aconfigure.ac > aconfigure

# We're building without audio or video support, as Asterisk isn't using
# that functionality, and it made it easier to ensure that we don't
# bundle any unnecessary libraries.  Please contact me if your project
# needs this support, and I'll re-enable it
export CFLAGS="-DPJ_HAS_IPV6=1 -DNDEBUG ${ARCHFLAGS} %{optflags}"

%configure --enable-shared        \
           --with-external-gsm    \
           --with-external-pa     \
           --with-external-speex  \
           --with-external-yuv    \
           --disable-opencore-amr \
           --disable-resample     \
           --disable-sound        \
           --disable-video        \
           --disable-v4l2         \
           --disable-ilbc-codec   \
           --disable-g7221-codec  

#make %{?_smp_mflags} dep
#make %{?_smp_mflags}
make -j1 dep
make -j1


%install
%make_install

install -p -D -m 0755 pjsip-apps/bin/pjsua-* %{buildroot}%{_bindir}/pjsua

# Remove the static libraries, as they aren't wanted
find %{buildroot} -type f -name "*.a" -delete



%files
%doc README.txt README-RTEMS INSTALL.txt
%license COPYING
%{_libdir}/lib*.so.*

%files devel
%{_libdir}/lib*.so
%{_includedir}/pj++/
%{_includedir}/pj/
%{_includedir}/pjlib-util/
%{_includedir}/pjmedia-audiodev/
%{_includedir}/pjmedia-codec/
%{_includedir}/pjmedia-videodev/
%{_includedir}/pjmedia/
%{_includedir}/pjnath/
%{_includedir}/pjsip-simple/
%{_includedir}/pjsip-ua/
%{_includedir}/pjsip/
%{_includedir}/pjsua-lib/
%{_includedir}/pjsua2/
%{_includedir}/*.h
%{_includedir}/*.hpp
%{_libdir}/pkgconfig/libpjproject.pc

%files -n pjsua
%{_bindir}/pjsua


%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 2.10-4
- Rebuilt with OpenSSL 3.0.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Nov 29 2020 Sandro Mani <manisandro@gmail.com> - 2.10-1
- Update to 2.10

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan  7 2020 Tom Callaway <spot@fedoraproject.org> - 2.9-3
- rebuild for libsrtp2

* Thu Oct 10 2019 Jared K. Smith <jsmith@fedoraproject.org> - 2.9-2
- Try again to fix SSE2-related build issues on non-X86_64 systems

* Wed Oct 09 2019 Jared K. Smith <jsmith@fedoraproject.org> - 2.9-1
- Update to upstream 2.9 release

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 18 2018 Miro Hrončok <mhroncok@redhat.com> - 2.7.2-3
- Remove Python 2 subpackage (#1627359)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 22 2018 Jared Smith <jsmith@fedoraproject.org> - 2.7.2-1
- Update to upstream 2.7.2 release for security updates

* Mon Feb 19 2018 Jared Smith <jsmith@fedoraproject.org> - 2.6-11
- Add missing BuildRequires on gcc and gcc-c++

* Thu Feb 15 2018 Jared Smith <jsmith@fedoraproject.org> - 2.6-10
- Use ldconfig_scriptlets macro

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Feb 07 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.6-8
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sun Dec 17 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.6-7
- Python 2 binary package renamed to python2-pjsua
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Sun Sep 03 2017 Jared Smith <jsmith@fedoraproject.org> - 2.6-6
- Don't run make in parallel, to try to identify build problem on PPC builds

* Sun Sep  3 2017 Tom Hughes <tom@compton.nu> - 2.6-5
- Fix armv7 patch to remove replaced error directive

* Fri Sep 01 2017 Sandro Mani <manisandro@gmail.com> - 2.6-4
- Add patch to only build with sse2 if it is enabled
- Add patch to add s390 build definitions to config.h

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 13 2017 Jared Smith <jsmith@fedoraproject.org> - 2.6-1
- Update to upstream 2.6 release

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 03 2016 Benjamin Lefoul <lef@fedoraproject.org> - 2.4.5-7
- Commenting out latest patch for BZ 1381133

* Tue Sep 20 2016 Benjamin Lefoul <lef@fedoraproject.org> - 2.4.5-6
- Add support for multiple listeners. More info with Ring project at SFL.

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.5-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Feb 24 2016 Jared Smith <jsmith@fedoraproject.org> - 2.4.5-4
- Include config_site.h file to improve performance

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jared Smith <jsmith@fedoraproject.org> - 2.4.5-2
- Add -DNDEBUG to CFLAGS at request of Asterisk developers

* Mon Aug 31 2015 Jared Smith <jsmith@fedoraproject.org> - 2.4.5-1
- Update to upstream 2.4.5 release
- Create sub-packages for pjsua and python bindings

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May  5 2015 Peter Robinson <pbrobinson@fedoraproject.org> 2.4-1
- Upstream 2.4 release

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.3-8
- Rebuilt for GCC 5 C++11 ABI change

* Thu Jan 29 2015 Peter Robinson <pbrobinson@fedoraproject.org> 2.3-7
- Fix endian support for aarch64
- Add speexdsp-devel dep as speex_echo.h has moved there

* Fri Nov 14 2014 Tom Callaway <spot@fedoraproject.org> - 2.3-6
- rebuild against new libsrtp

* Sun Oct 26 2014 Jared Smith <jsmith@fedoraproject.org> - 2.3-5
- Fix endianness support on ARM platform

* Wed Oct 15 2014 Jared Smith <jsmith@fedoraproject.org> - 2.3-3
- Add IPv6 support

* Wed Sep 10 2014 Jared Smith <jsmiht@fedoraproject.org> - 2.3-2
- Disable video support, and specifically tell it not to use libyuv,
  as the version of libyuv in Fedora is too old
- Disable ilbc codec support, as it is not needed

* Wed Sep 10 2014 Jared Smith <jsmiht@fedoraproject.org> - 2.3-1
- Update to upstream 2.3 release

* Fri Jun 20 2014 Jared Smith <jsmiht@fedoraproject.org> - 2.2.1-1
- Update to upstream 2.2.1 release

* Sun Mar 09 2014 Jared Smith <jsmiht@fedoraproject.org> - 2.2-4
- Instead of deleting the empty file pj/config_site.h, make it non-empty

* Fri Feb 28 2014 Jared Smith <jsmiht@fedoraproject.org> - 2.2-3
- Fix the location of the .so files
- Add a massive patch to fix the incorrect FSF address

* Fri Feb 28 2014 Jared Smith <jsmiht@fedoraproject.org> - 2.2-2
- Rebase a patch to simple eliminate the third_party directory
- Add a patch to fix up the .pc file

* Fri Feb 28 2014 Jared Smith <jsmiht@fedoraproject.org> - 2.2-1
- Update to upstream 2.2 release

* Fri Jan 17 2014 Dale Macartney <dbmacartney@fedoraproject.org> - 2.1-0.6.git217740d
- Shorten sumary, and moved libs to -devel package

* Mon Nov 25 2013 Anthony Messina <amessina@messinet.com> - 2.1-0.5.git217740d
- Enable G.722.1 and ILBC

* Mon Nov 25 2013 Anthony Messina <amessina@messinet.com> - 2.1-0.4.git217740d
- Build without opencore-amr

* Mon Nov 18 2013 Anthony Messina <amessina@messinet.com> - 2.1-0.3.git217740d
- Updates for SIP transaction handling

* Sat Nov 16 2013 Anthony Messina <amessina@messinet.com> - 2.1-0.2.gitde17f0e
- Rebuild for updates to OpenSSL

* Mon Oct 07 2013 Anthony Messina <amessina@messinet.com> - 2.1-0.1.gitde17f0e
- Package for Fedora & Asterisk: https://wiki.asterisk.org/wiki/display/AST/Installing+pjproject

* Mon Apr 22 2013 Anthony Messina <amessina@messinet.com> - 2.1-1
- Update to 2.1 release

* Sat Feb 16 2013 Mario Santagiuliana <fedora@marionline.it> - 2.0.1-1
- New version 2.0.1

* Mon Apr 16 2012 Mario Santagiuliana <fedora@marionline.it> - 1.12-2
- fix warning mixed-use-of-spaces-and-tabs from rpmlint
- use macro name and version

* Wed Apr 11 2012 Tom Callaway <spot@fedoraproject.org> - 1.12-1
- use system copy of libsrtp

* Thu Jan 12 2012 Mario Santagiuliana <fedora@marionline.it> 1.12-0
- Update to version 1.12

* Sun Jan 08 2012 Mario Santagiuliana <fedora@marionline.it> 1.10-7
- Follow the comment of Rex Dieter:
  https://bugzilla.redhat.com/show_bug.cgi?id=728302#c17

* Sat Jan 07 2012 Mario Santagiuliana <fedora@marionline.it> 1.10-6
- Follow the comment of Rex Dieter:
  https://bugzilla.redhat.com/show_bug.cgi?id=728302#c14
  https://bugzilla.redhat.com/show_bug.cgi?id=728302#c15

* Thu Dec 29 2011 Mario Santagiuliana <fedora@marionline.it> 1.10-5
- Follow the comment of Rex Dieter:
  https://bugzilla.redhat.com/show_bug.cgi?id=728302#c11

* Mon Aug 15 2011 Mario Santagiulaina <fedora@marionline.it> 1.10-4
- Forgot to write changelog for 1.10-3.
- Version 1.10.3 add patch to resolve libdir issue.

* Mon Aug 15 2011 Mario Santagiulaina <fedora@marionline.it> 1.10-2
- Follow the comment of Thomas Spura:
  https://bugzilla.redhat.com/show_bug.cgi?id=728302#c1

* Thu Aug 04 2011 Mario Santagiulaina <fedora@marionline.it> 1.10-1
- Initial RPM release
