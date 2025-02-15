%define          mainver   2.15.5
#%%define          betatag   dev-20160114
%define          dwfdate   20241229

%define          baserelease 10


%define          rel        %{?betatag:0.}%{baserelease}%{?betatag:.%(echo %betatag | sed -e 's|-||g')}

%if 0%{?fedora} >= 42
%global          use_systemd_sysusers  1
%else
# Drop this when F41 gets EOF
%global          use_systemd_sysusers  0
%endif

Summary:         Calculate tide all over the world
Name:            xtide
Version:         %{mainver}
Release:         %{rel}%{?dist}

URL:             http://www.flaterco.com/xtide/
Source0:         https://flaterco.com/files/xtide/%{name}-%{version}%{?betatag:-%betatag}.tar.xz

Source14:        xtide-get_harmonics-data.sh
Source20:        %{name}.desktop
Source30:        xtide-README.fedora

# Source41 is created by Harminics-dwf-create-regal-OK.sh in
# Source40
#
# (Updated: 2007-Nov-23) 
# Upstream now splitted free and non-free harmonics data
#                     
#Source40:        Harminics-USpart-recreate-sh.tar.bz2
#Source41:        harmonics-dwf-%%{dwfdate}-dump-US.tar.bz2
Source42:        https://flaterco.com/files/xtide/harmonics-dwf-%{dwfdate}-free.tar.xz

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:         GPL-3.0-or-later

BuildRequires:   make
BuildRequires:   gcc-c++
BuildRequires:   libXaw-devel
BuildRequires:   libXext-devel
BuildRequires:   libpng-devel
BuildRequires:   zlib-devel
BuildRequires:   desktop-file-utils
BuildRequires:   libdstr-devel
BuildRequires:   libtcd-devel
BuildRequires:   gpsd-devel >= 3
BuildRequires:   systemd
BuildRequires:   systemd-devel
# By SOURCE1
BuildRequires:   automake
BuildRequires:   autoconf
BuildRequires:   libtool
# By SOURCE3
BuildRequires:   byacc
BuildRequires:   flex
# Explicit for %%PATCH1
BuildRequires:   %{_bindir}/pkg-config

Requires:        wvs-data
Requires:        xorg-x11-fonts-misc
Requires:        xtide-common = %{version}-%{release}
Requires:        libxtide%{?_isa} = %{version}-%{release}

%if ! %{use_systemd_sysusers}
Requires(pre):      shadow-utils
%endif
Requires(preun):    systemd
Requires(postun):   systemd
Requires(post):     systemd

%package -n      libxtide
Summary:         XTide library
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:         GPL-3.0-or-later

%package -n      libxtide-devel
Summary:         Development files for libxtide
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:         GPL-3.0-or-later
Requires:        libxtide%{?_isa} = %{version}-%{release}


%package         common
Summary:         Xtide common files
# Automatically converted from old format: Public Domain - needs further work
License:         LicenseRef-Callaway-Public-Domain
Requires:        bzip2
Requires:        wget
BuildArch:       noarch

%description
XTide is a package that provides tide and current
predictions in a wide variety of formats.  Graphs, text listings, and
calendars can be generated, or a tide clock can be provided on your
desktop.

XTide can work with X-windows, plain text terminals, or the web. This
is accomplished with three separate programs: the interactive
interface (xtide), the non-interactive or command line interface
(tide), and the web interface.

The algorithm that XTide uses to predict tides is the one used by the
National Ocean Service in the U.S.  It is significantly more accurate
than the simple tide clocks that can be bought in novelty stores.
However, it takes more to predict tides accurately than just a spiffy
algorithm -- you also need some special data for each and every
location for which you want to predict tides.  XTide reads this data
from harmonics files.  See http://www.flaterco.com/xtide/files.html
for details on where to get these 

NOTE:
Please also see README.fedora in xtide-common package for Fedora 
specific issue.

%description -n libxtide
The libxtide package provides library files used for XTide.

%description -n libxtide-devel
The libxtide-devel package contains libraries and header files for
developing applications that use libxtide.


%description common
This package contains common files needed by xtide, xttpd and
tideEditor.
Please read README.fedora for Fedora specific issue.

%prep
%if 0%{?betatag:1}
%setup -q -n %{name}-%{version}-DEVELOPMENT -a 42
%else
%setup -q -n %{name}-%{version}%{?betatag:-%{betatag}} -a 42
%endif

# Systemd stuff
sed -i scripts/systemd/xttpd.socket \
	-e 's|ListenStream=80|ListenStream=8080|'

cat > scripts/systemd/xttpd.service.conf <<EOF
HFILE_PATH=%{_datadir}/%{name}-harmonics
XTTPD_FEEDBACK=xtide-maintainer@fedoraproject.org
EOF

sed -i scripts/systemd/xttpd.service.in \
	-e 's|^EnvironmentFile=.*$|EnvironmentFile=-%{_sysconfdir}/sysconfig/xttpd.service.conf|'

autoreconf -i

# Dstr -> Dstr.h
grep -rl 'include.*<Dstr>' . | while read f ; do
	sed -i.name -e 's|\(include.*\)<Dstr>|\1<Dstr.h>|' $f
done

# Embed version
sed -i.ver \
	-e "\@^PACKAGE_VERSION=@s|'.*'$|'%{version}-%{release}'|" \
	-e "\@^PACKAGE_STRING=@s|'\(XTide \).*'$|'\1%{version}-%{release}'|" \
	-e "\@^[ \t]*VERSION=@s|'.*'$|'%{version}-%{release}'|" \
	configure

# Kill rpath, ah!
sed -i.rpath configure \
	-e 's|hardcode_libdir_flag_spec=|kill_hardcode_libdir_flag_spec=|' \
	-e 's|hardcode_libdir_flag_spec_CXX=|kill_hardcode_libdir_flag_spec_CXX=|' \
	%{nil}
sed -i.rpath ltmain.sh \
	-e 's|\$finalize_rpath|\$finalize_no_rpath|' \
	%{nil}

%if %{use_systemd_sysusers}
# Create a sysusers.d config file
cat >xtide.sysusers.conf <<EOF
u xttpd - 'XTide web server' %{_sysconfdir}/%{name} -
EOF
%endif

%build
%configure \
   --enable-systemd \
%if 0
   --enable-moon-age \
%endif
   --with-xttpd-user=xttpd \
   --with-xttpd-group=xttpd


%{__make} %{?_smp_mflags} -k

echo "%{_datadir}/xtide-harmonics/" > %{name}.conf
echo "%{_datadir}/wvs-data/" >> %{name}.conf

%install
# 1. install xtide
%{__make} \
   DESTDIR=$RPM_BUILD_ROOT \
   INSTALL="%{__install} -p" \
   install

%{__mkdir_p} $RPM_BUILD_ROOT%{_sbindir}

# xttpd treatment
# xttpd is wrapped
%{__sed} -e 's|20081228|%{dwfdate}|' %{SOURCE14} \
   > xtide-get_harmonics-data.sh
%{__install} -c -p -m 755 xtide-get_harmonics-data.sh \
   $RPM_BUILD_ROOT%{_sbindir}

# ensure xttpd binary installation directory (original
# wrapper script is hardcorded)
%{__sed} -i -e 's|/usr/libexec|%{_libexecdir}|' \
   $RPM_BUILD_ROOT%{_sbindir}/xttpd

# Install systemd unit file
%{__mkdir_p} ${RPM_BUILD_ROOT}%{_unitdir}
%{__install} -c -p -m 644 \
	scripts/systemd/xttpd.socket \
	scripts/systemd/xttpd.service \
	${RPM_BUILD_ROOT}%{_unitdir}
%{__ln_s} -f \
	%{_sysconfdir}/sysconfig/xttpd.socket \
	${RPM_BUILD_ROOT}%{_unitdir}/xttpd.socket
%{__mkdir_p} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig
%{__install} -c -p -m 644 \
	scripts/systemd/xttpd.service.conf \
	$RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/
%{__install} -c -p -m 644 \
	scripts/systemd/xttpd.socket \
	$RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/xttpd.socket

# 1A Install harmonics file
%{__mkdir_p} ${RPM_BUILD_ROOT}%{_datadir}/%{name}
%{__mkdir_p} ${RPM_BUILD_ROOT}%{_datadir}/%{name}-harmonics

# 1B Add configuration file
%{__mkdir_p} ${RPM_BUILD_ROOT}%{_sysconfdir}
%{__install} -c -p -m 644 %{name}.conf ${RPM_BUILD_ROOT}%{_sysconfdir}/

# 1C Add desktop entry (xtide)
%{__mkdir_p} $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install \
   --dir $RPM_BUILD_ROOT%{_datadir}/applications \
   %{SOURCE20}

# 1D Install icon
for f in iconsrc/icon_*_orig.png ; do
   %{__install} -c -p -m 644 $f $RPM_BUILD_ROOT%{_datadir}/%{name}/
done
%{__mkdir_p} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps/
%{__mkdir_p} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/
%{__ln_s} -f ../../../../%{name}/icon_16x16_orig.png \
   $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{__ln_s} -f ../../../../%{name}/icon_48x48_orig.png \
   $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

# 1E install xttpd conf file
%{__mkdir_p} $RPM_BUILD_ROOT%{_initddir}
%{__mkdir_p} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig
%{__mkdir_p} $RPM_BUILD_ROOT%{_sysconfdir}/xtide

# 1F and others
%{__install} -c -p -m 644 %{SOURCE30} README.fedora

# 1G tcd data
%{__install} -c -p -m 644 harmonics-dwf-%{dwfdate}/*tcd \
   $RPM_BUILD_ROOT%{_datadir}/xtide-harmonics/

# 2 Documentation
for f in AUTHORS ChangeLog NEWS README ; do
   iconv -f ISO-8859-1 -t UTF-8 $f > $f.tmp && \
      ( touch -r $f $f.tmp ; mv -f $f.tmp $f ) || rm -f $f.tmp
done

rm -rf harmonics-dwf
mkdir harmonics-dwf
cp -a harmonics-dwf-%{dwfdate}/[A-Z]* \
	harmonics-dwf/

# 3 cleanup
rm -rf $RPM_BUILD_ROOT%{_libdir}/libxtide.{a,la}

%if %{use_systemd_sysusers}
install -m0644 -D xtide.sysusers.conf %{buildroot}%{_sysusersdir}/xtide.conf
%endif

%post
%systemd_post xttpd.socket xttpd.service
exit 0

%postun
%systemd_postun xttpd.socket xttpd.service
exit 0


%pre
%if ! %{use_systemd_sysusers}
getent group xttpd &>/dev/null || \
   %{_sbindir}/groupadd -r xttpd
getent passwd xttpd &> /dev/null || \
   %{_sbindir}/useradd \
   -c "XTide web server" \
   -g xttpd \
   -d %{_sysconfdir}/%{name} \
   -r \
   -s /sbin/nologin \
   xttpd 2>/dev/null
%endif
exit 0

%preun
%systemd_preun xttpd.socket xttpd.service
exit 0

%ldconfig_scriptlets -n libxtide

%files common
%doc README.fedora
%doc harmonics-dwf/
%config(noreplace) %{_sysconfdir}/%{name}.conf

%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}-harmonics
%dir %{_sysconfdir}/%{name}

%{_sbindir}/xtide-get*.sh

# Now include tcd data
%{_datadir}/%{name}-harmonics/*.tcd

%files -n libxtide
%{_libdir}/libxtide.so.1{,.*}

%files -n libxtide-devel
%{_libdir}/libxtide.so
%{_includedir}/libxtide/

%files
%defattr(-,root,root,-)

%doc AUTHORS README README-QUICK
%license COPYING
# xtide
%{_mandir}/man1/*tide.1*

%{_datadir}/applications/*%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/%{name}/icon_*_orig.png

%{_bindir}/*tide

# xttpd
%config(noreplace) %{_sysconfdir}/sysconfig/xttpd.service.conf
%config(noreplace) %{_sysconfdir}/sysconfig/xttpd.socket
%{_unitdir}/xttpd.service
%{_unitdir}/xttpd.socket

%{_sbindir}/xttpd
%{_datadir}/man/man8/xttpd.8*
%if %{use_systemd_sysusers}
%{_sysusersdir}/xtide.conf
%endif

%changelog
* Thu Feb 13 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.15.5-10
- Only apply Systemd Sysusers.d usage for F-42+

* Tue Feb 11 2025 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.15.5-10
- Add sysusers.d config file to allow rpm to create users/groups automatically

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Dec 30 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.15.5-8
- Update harmonics data to 20241229

* Thu Jul  25 2024 Miroslav Suchý <msuchy@redhat.com> - 2.15.5-7
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan  6 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.15.5-4
- harmonics data update (20240104)

* Sat Jul 22 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.15.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jan 24 2023 Adam Williamson <awilliam@redhat.com> - 2.15.5-2
- rebuild for new libgps

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.5-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.5-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu May 12 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.15.5-1
- 2.15.5

* Thu May  5 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.15.4-2
- Modify configure.ac to detect gpsd API version >=7 (version 3.18)

* Tue Feb 15 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.15.4-1
- 2.15.4

* Sun Feb  6 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.15.3-4
- Patch for libXaw 1.0.14 XawListChange API change

* Sun Feb  6 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.15.3-3
- harmonics data update (20220109)

* Sun Jul 25 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.15.3-2.2
- Rebuild for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Peter Hutterer <peter.hutterer@redhat.com> - 2.15.3-2.1
- Require xorg-x11-fonts-misc instead of -base. -base hasn't existed for
  over a decade.

* Sat Jan 30 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.15.3-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Aug  9 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.15.3-1
- 2.15.3

* Fri Aug 07 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.15.2-2.1
- F-33: mass rebuild

* Tue Jan 28 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.15.2-2
- harmonics data update (20191229)

* Tue Feb 26 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.15.2-1
- 2.15.2

* Tue Feb 05 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.15.1-7.1
- F-30: mass rebuild

* Wed Jan  2 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.15.1-7
- harmonics data update (20181227)

* Mon Jul 15 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.15.1-6
- F-29: mass rebuild

* Thu Feb 15 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.15.1-5
- harmonics data update (20180101)

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.15.1-4.1
- Remove obsolete scriptlets

* Fri Sep 22 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.15.1-4
- F-28: rebuild for gpsd

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.15.1-3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Wed Feb 15 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.15.1-3
- F-26: mass rebuild

* Mon Jan  2 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.15.1-2
- harmonics data update

* Sun Feb 28 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.15.1-1
- 2.15.1

* Sat Feb  6 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.15-2
- F-24: mass rebuild

* Tue Jan 26 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.15-1
- 2.15

* Sat Jan 16 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.15-0.2.dev20160114
- 2.15 dev20160114

* Sun Jan 10 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.15-0.1.dev20160105
- 2.15 dev20160105

* Tue Jan  5 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.14.3-8
- Use new configure.ac, Makefile.am provided by the upstream

* Sun Jan  3 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.14.3-7
- Use systemd patches provided by the upstream
- Make xttpd.socket (provided by the upstream) be symlink from
  %%_sysconfdir

* Thu Dec 31 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.14.3-6
- Switch to use systemd unit on F-24+

* Wed Dec 30 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.14.3-5
- Make xttpd server create pidfile by itself
- Modify rcscript to reflect server change
- Remove if-condition when calling xttpd-wrapper.sh
  with regard to XTTPD_FEEDBACK option

* Tue Dec 29 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.14.3-4
- Harmonics data 20151227

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.14-3.1
- Rebuilt for GCC 5 C++11 ABI change

* Sun Mar  8 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.14-3
- F-23: rebuild against new gpsd

* Sun Dec 28 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.14-2
- Harmonics data 20141224

* Tue Nov  4 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.14-1
- 2.14

* Fri Oct 17 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.14-0.4.dev20141014
- 2.14 dev20141014
- New subpackage: libxtide
- Make -common noarch

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.14-0.3.dev20140622.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 30 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.14-0.3.dev20140622
- 2.14 dev20140622

* Thu Jun 12 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.14-0.2.dev20140504
- F-21: mass rebuild

* Mon May 26 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.14-0.1.dev20140504
- 2.14 dev20140504

* Mon Dec 30 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.13.2-4
- Update harmonics data to 20131228

* Sun Dec  1 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.13.2-3
- F-21: rebuild against new gpsd

* Tue Aug  6 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.13.2-2
- F-20: mass rebuild

* Wed Jul 24 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.13.2-1
- 2.13.2

* Fri Jul 12 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.13.1-1
- 2.13.1

* Sat Feb  9 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.13-4
- F-19: kill vendorization of desktop file (fpc#247)

* Mon Dec 31 2012 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.13-3
- Update harmonics data to 20121224

* Mon Aug  6 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.13-2
- F-18: Mass rebuild

* Mon Jun 11 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.13-1
- 2.13

* Wed Mar 14 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.13-0.2.RC3
- 2.13 rc3

* Mon Mar  5 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.13-0.1.RC2
- 2.13 rc2

* Mon Mar  5 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.12.1-4
- Update harmonics data to 20120302
- Modify rc script for new systemd

* Thu Jan  5 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.12.1-3
- F-17: rebuild against gcc47

* Sat Dec 31 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.12.1-2
- Update harmonics data to 20111230

* Wed Nov 30 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.12.1-1
- Update to 2.12.1

* Sun Nov  6 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.12-1
- Update to 2.12

* Tue Aug 30 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.12-0.6.RC1
- Update to 2.12 RC1
- Kill gpsd support on <= F-16, xtide now uses gpsd 3.0

* Sun Aug 28 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.12-0.5.dev20110827
- Update to 2.12 dev 20110827

* Wed Aug 24 2011 Mamoru Tasaka <mtasaka@fedoraproject.org>
- F-17: rebuild against new gpsd

* Tue Aug  2 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.12-0.4.dev20110731
- Update to 2.12 dev 20110731

* Tue Apr 12 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.12-0.3.dev20101029
- Update dwf data to 20110410

* Sat Jan  1 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.12-0.2.dev20101029
- A Happy New Year
- Update dwf data to 20101230

* Mon Nov  1 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>- 2.12-0.1.dev20101029
- Update to 2.12 dev 20101029, enabling experimental SVG support

* Thu Aug 19 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.11-2
- Rebuild for new libtcd

* Fri Aug 13 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.11-1
- 2.11

* Sun Jul  4 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.11-0.8.RC1
- 2.11 RC1

* Fri Jul  2 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.11-0.7.dev20100625
- Update to 2.11 dev 20100625

* Tue Jun  1 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.11-0.6.dev20100406
- Update dwf data to 20100529

* Thu May 27 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.11-0.5.dev20100406
- Update dwf data to 20100522

* Fri May  7 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.11-0.4.dev20100406
- F-14+: enable gpsd support

* Thu Apr  8 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.11-0.3.dev20100406
- Update to 2.11 dev20100406

* Sat Jan  2 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.11-0.2.dev20091227
- Update to 2.11 dev20091227
- Update to dwf data 20091227

* Mon Sep 14 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.11-0.1.dev20090913
- Update to 2.11 development branch

* Sat Jul 25 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.10-5
- Use %%_initddir instead of %%_initrddir

* Wed Feb 25 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.10-4
- GTK icon cache updating script update

* Thu Jan  8 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.10-3
- Update harmonics data to 20081228
- Update xtide-get_harmonics-data.sh following harmonics tarball 
  format change

* Thu Feb  7 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.10-2
- Use system-wide libdstr (review request 431692 passed)

* Wed Feb  6 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.10-1
- 2.10

* Sat Jan 19 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.10-0.1.RC1
- Try 2.10 RC1

* Sun Dec 30 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.9.5-2
- Update harmonics data to 20071228

* Wed Dec 12 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.9.5-1
- 2.9.5

* Fri Nov 23 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.9.4-3
- Update harmonics data to 20071122.

* Wed Sep  5 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.9.4-1
- 2.9.4
  (Relicensed: GPLv2+ -> GPLv3+)
- Update user creation script

* Wed Aug 22 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.9.3-3.dist.2
- Mass rebuild (buildID or binutils issue)

* Fri Aug  3 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.9.3-3.dist.1
- License update

* Mon Jun 11 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.9.3-3
- Require needed fonts (bug reported from upstream)

* Thu May 31 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.9.3-2
- Ship US part tcd data, which are under public domain.

* Wed Apr 18 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.9.3-1
- 2.9.3

* Mon Apr  3 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.9.2-1
- 2.9.2

* Thu Mar 15 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.9.1-1
- 2.9.1

* Wed Feb 28 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.9-1
- 2.9

* Sun Feb 18 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.9-0.3.RC3
- 2.9 RC3

* Wed Feb 14 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.9-0.3.RC2
- 2.9 RC2

* Fri Feb  2 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.9-0.3.RC1
- 2.9 RC1

* Mon Jan 22 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.9-0.2.date20070120
- 2.9 dev 20070120

* Wed Jan 17 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.9-0.2.date20070115
- 2.9 dev 20070115

* Tue Jan  9 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.9-0.2.date20070108
- 2.9 dev 20070108

* Fri Jan  6 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.9-0.2.date20070103
- 2.9 dev 20070103

* Fri Dec 22 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.9-0.2.date20061222
- 2.9 dev 20061222

* Fri Dec 22 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.9-0.2.date20061221
- 2.9 dev 20061221

* Tue Dec 12 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.9-0.2.date20061210
- 2.9 dev 20061210

* Mon Dec  4 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.9-0.2.date20061203
- 2.9 dev 20061203
- Update desktop files
- Use scripts in source tarball
- Drop harmonics data description

* Wed Nov 29 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- Add more BuildRequires only for FC-5.

* Sun Nov 26 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.9-0.2.date20061122
- Ensure the hardcorded directories in some scripts can be 
  appropriately changed.
- Fix some typo in README.fedora

* Thu Nov 23 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.9-0.1.date20061122
- 2.9 dev 20061122 release

* Mon Nov 20 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.9-0.1.dev1
- Version down temporarily
- re-split libtcd, tcd-utils (see bug 211626)
- again include xttpd

* Sun Oct 29 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.9-0.14.dev20061027
- xtide-2.9dev20061029, tcd-utils-1.3.11(2005-08-11),
  update patches.
- Remove -DCOMPAT114 as required by newer tcd-utils
- Bump somajor of tcd-utils for API change.

* Fri Oct 27 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.9-0.13.dev20061015
- Fix some change in xtide-2.9dev-change-uidgid.patch

* Fri Oct 27 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.9-0.12.dev20061015
- More restrictive uid/gid mode for xttpd
- Another fix for xttpd.init

* Thu Oct 26 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.9-0.11.dev20061015
- Other fixes for xttpd.init, xttpd.conf
- Create "xttpd" user and use xttpd user for daemon.

* Wed Oct 25 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.9-0.10.dev20061015
- xtide doesn't need wrapperd, however, xttpd does.
- Fix xttpd init script

* Wed Oct 25 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.9-0.9.dev20061015
- Adjustment for WVS data directory change.

* Wed Oct 25 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.9-0.8.dev20061015
- Split WVS data.
- desktop-file-utils 0.11 change: X-Fedora, Application is no longer
  accepted (will be fixed in rawhide).

* Wed Oct 25 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.9-0.7.dev20061015
- Drop harmonics data for now.
- Define WVS_DIR, then rewrite tideEditor-wrapper.sh and wrap xtide
- Add fedora-specific document
- Include WVS data

* Sun Oct 22 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.9-0.6.dev20061015
- Install 48x48 icon as well.

* Sun Oct 22 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.9-0.5.dev20061015
- Use icon in xtide source
- Fix Group entry
- Re-source profile shell script for easier rebuilding

* Sun Oct 22 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.9-0.4.dev20061015
- Introduce common files package.
- CFLAGS treatment change.
- Treak configuration files and their locations.

* Sat Oct 21 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.9-0.3.dev20061015
- Various changes about compilation optflags.
- Change libtcd soname numbering
- Sprit xttpd, include scripts
- tideEditor wrapper script included and desktop files added.
- use "/sbin/ldconfig -n"
- Lots of help from Michael Schwendt and Patrice Dumas, thanks!!

* Sat Oct 21 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.9-0.2.dev20061015
- Re-unify libtcd and xtide, and include tcd-utils, 
  build all at once.

* Fri Oct 20 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.9-0.1.dev20061015
- Resubmit to Fedora Extras (bug #211626)
- Split libtcd to another package, require tcd-utils to
  rebuild tcd data.

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 2.8-4
- rebuild on all arches

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Fri Dec 17 2004 David M. Kaplan <dmk@erizo.ucdavis.edu> 0:2.8-2
- Made a small hack that should make it compile on x86_64 systems.

* Wed Dec 15 2004 David M. Kaplan <dmk@erizo.ucdavis.edu> 0:2.8-1
- Updated to version 2.8
- Cleaned up spec file because much of the tricks to get it to work
  are no longer necessary.

* Mon Dec  8 2003 David M. Kaplan <dmk@erizo.ucdavis.edu> 0:2.6.4-0.fdr.4
- Removed 644 permissions.

* Tue Dec  2 2003 David M. Kaplan <dmk@erizo.ucdavis.edu> 0:2.6.4-0.fdr.3
- Fixed problem with debuginfo rpm and lex.xml.c.
- Changed attributes to 644/755 to agree with Fedora specification.

* Mon Nov 17 2003 David M. Kaplan <dmk@erizo.ucdavis.edu> 0:2.6.4-0.fdr.1
- Updated to 2.6.4 version of xtide

* Mon Oct 20 2003 David M. Kaplan <dmk@erizo.ucdavis.edu> 0:2.6.3-0.fdr.2
- Made changes to spec and patch as per Michael Schwendt's suggestions

* Fri Oct 17 2003 David M. Kaplan <dmk@erizo.ucdavis.edu> 0:2.6.3-0.fdr.1
- Modified spec file to meet requirements for fedora

* Tue Oct 14 2003 David M. Kaplan <dmk@erizo.ucdavis.edu> 2.6.3-0.fdr.0
- Modify for Fedora submission

* Tue Oct 14 2003 David M. Kaplan <dmkaplan@ucdavis.edu> 2.6.3-0
- Update to XTide 2.6.3

* Fri Sep 05 2003 David M. Kaplan <dmkaplan@ucdavis.edu>
- Updated to XTide 2.6.2

* Thu Feb 17 2003 David M. Kaplan <dmkaplan@ucdavis.edu>
- Updated to XTide 2.6 FINAL (2003-02-12)

* Thu Feb 17 2003 David M. Kaplan <dmkaplan@ucdavis.edu>
- Updated to XTide 2.6 DEVELOPMENT (2003-02-12)

* Thu Jan 23 2003 David M. Kaplan <dmkaplan@ucdavis.edu>
- Updated to XTide 2.6 DEVELOPMENT (2003-01-17)

* Sat Dec 28 2002 David M. Kaplan <dmkaplan@ucdavis.edu>
- First RPM build.

