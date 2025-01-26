%global betaver beta3
%global tclver 0.2
%global mainver 2.1
%{!?tcl_version: %global tcl_version %(echo 'puts $tcl_version' | tclsh8.6)}
%{!?tcl_sitearch: %global tcl_sitearch %{_libdir}/tcl%{tcl_version}}
%global tkphonearch %{_arch}

Name:		iaxclient
Version:	%{mainver}
Release:	0.52.%{betaver}%{?dist}
Summary:	Library for creating telephony solutions that interoperate with Asterisk
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:	LicenseRef-Callaway-LGPLv2+
URL:		http://iaxclient.wiki.sourceforge.net/
Source0:	http://downloads.sourceforge.net/iaxclient/%{name}-%{version}%{betaver}.tar.gz
Source1:	tkiaxphone.desktop
Source2:	wxiax.desktop
Source3:	phone.png
Source4:	run-tkiaxphone.sh
Patch0:		iaxclient-2.1beta3-wxGTK28.patch
Patch1:		iaxclient-2.1beta3-tkphone-cleanups.patch
Patch2:		iaxclient-2.1beta3-tcl-includedir.patch
Patch3:		iaxclient-2.1beta3-tcl-libdir.patch
Patch4:		iaxclient-2.1beta3-tcl-nodoc.patch
Patch5:		iaxclient-2.1beta3-theora-detection.patch
Patch6:		iaxclient-2.1beta3-implicit-DSO-libm.patch
Patch7:		iaxclient-2.1beta3-arm-barriers.patch
Patch8:		iaxclient-portable.patch
# Link against the locally build iax
Patch9:		iaxclient-link-local-iax.patch
# Use system ilbc
Patch10:	iaxclient-system-ilbc.patch
# Add missing -fPIC to configure.ac test
Patch11:	iaxclient-2.1beta3-fpic.patch
Patch12:        wxwidgets-3.0.patch
Patch13:        gtk3.patch
Patch14:	iaxclient-gcc14.patch

# Fix some makefile issues
Patch20:	iax-0.2.3_makefile.patch
# Fix format-security issue
Patch21:	iax-0.2.3_format-security.patch
# Add missing #include <sys/socket.h>
Patch22:	iax-0.2.3_socket.patch
Patch23:	iaxclient-c99.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gsm-devel
BuildRequires:  gtk3-devel
BuildRequires:  ilbc-devel
BuildRequires:  libogg-devel
BuildRequires:  liboggz-devel
BuildRequires:  libtheora-devel
BuildRequires:  libtool
BuildRequires:  libvidcap-devel
BuildRequires:  make
BuildRequires:  portaudio-devel
BuildRequires:  SDL-devel
BuildRequires:  spandsp-devel
BuildRequires:  speex-devel
BuildRequires:  speexdsp-devel
BuildRequires:  tk-devel < 1:9
BuildRequires:  wxGTK-devel

%description
Iaxclient is an open source, multiplatform library for creating telephony 
solutions that interoperate with Asterisk, the Open Source PBX.

Although asterisk supports other VOIP protocols (including SIP, and with 
patches, H.323), IAX's simple, lightweight nature gives it several advantages, 
particularly in that it can operate easily through NAT and packet firewalls, 
and it is easily extensible and simple to understand.
Iaxclient pulls together the wide array of open source technologies required 
for telephony applications.

%package libiax
Summary:	IAX library
Obsoletes:	iax < 0.2.3

%description libiax
The %{name}-libs package contains the IAX library version 0.2.3, an improved
version of the abandoned upstream IAX library.

%package libiax-devel
Summary:	IAX library development files
Requires:	%{name}-libiax%{?_isa} = %{version}-%{release}
Obsoletes:	iax-devel < 0.2.3

%description libiax-devel
The %{name}-libiax-devel package contains libraries and header files for
developing applications that use %{name}-libiax.


%package devel
Summary:	Development files for %{name}
Requires:	pkgconfig
Requires:	%{name} = %{mainver}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n tcl-iaxclient
Summary:	Tcl interface to iax2 client lib
Version:	%{tclver}
# Automatically converted from old format: BSD - review is highly recommended.
License:	LicenseRef-Callaway-BSD
Requires:	tcl(abi) = 8.6
Requires:	%{name} = %{mainver}-%{release}

%description -n tcl-iaxclient
Tcl extensions to iaxclient libraries.

%package -n tkiaxphone
Summary:	Tk IAX Phone Client
Version:	%{mainver}
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:	LicenseRef-Callaway-LGPLv2+
Requires:	tcl(abi) = 8.6
Requires:	%{name} = %{mainver}-%{release}

%description -n tkiaxphone
Tk IAX Phone Client.

%package -n wxiax
Summary:	wx IAX Phone Client
Version:	%{mainver}
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:	LicenseRef-Callaway-LGPLv2+
Requires:	%{name} = %{mainver}-%{release}

%description -n wxiax
wx IAX Phone Client.

%prep
%setup -q -n %{name}-%{mainver}%{betaver}
%patch -P0 -p1 -b .wxGTK28
%patch -P1 -p1 -b .tkphone
%patch -P2 -p1 -b .includedir
%patch -P3 -p1 -b .libdir
%patch -P4 -p1 -b .nodoc
%patch -P5 -p1 -b .theoradetect
%patch -P6 -p1 -b .DSO
%patch -P7 -p1 -b .arm
%patch -P8 -p1 -b .portable
%patch -P9 -p1 -b .linkiax
%patch -P10 -p1 -b .ilbc
%patch -P11 -p1 -b .fpic
%patch -P12 -p1 -b .wx3
%patch -P13 -p1 -b .gtk3
%patch -P14 -p1 -b .gcc14

# Delete bundled libraries (except libiax2) just to be sure
rm -rf lib/{gsm, portmixer, sox, spandsp}

autoreconf -vif

chmod -x contrib/tcl/README.txt

(
cd lib/libiax2
%patch -P20 -p1 -b .iaxmakefile
%patch -P21 -p1 -b .iaxfmtsecurity
%patch -P22 -p1 -b .iaxsocket

sed -i 's|${exec_prefix}/lib|${exec_prefix}/%{_lib}|g' iax-config.in
sed -i 's|/usr/lib|%{_libdir}|g' iax-config.in

autoreconf -vif
)

%patch -P23 -p1 -b .c99

%build
(
cd lib/libiax2
%configure --disable-static
make %{?_smp_mflags} UCFLAGS="%{optflags}"
)

%configure --disable-static --with-wish=%{_bindir}/wish8.6
# sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
# sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags} LIBTOOL="%{_bindir}/libtool"

(
cd contrib/tcl/
%configure
make %{?_smp_mflags} LIBTOOL="%{_bindir}/libtool"
)

%install
%make_install -C lib/libiax2

%make_install LIBTOOL="%{_bindir}/libtool"

find %{buildroot} -name '*.a' -exec rm -f {} ';'
find %{buildroot} -name '*.la' -exec rm -f {} ';'

install -d %{buildroot}%{tcl_sitearch}
mv %{buildroot}%{_libdir}/iaxclient %{buildroot}%{tcl_sitearch}/

%make_install LIBTOOL="%{_bindir}/libtool" -C contrib/tcl
mv %{buildroot}%{_libdir}/tcliaxclient0.2 %{buildroot}%{tcl_sitearch}/tcliaxclient0.2
chmod +x %{buildroot}%{tcl_sitearch}/iaxclient/tkphone/phone.ui.tcl
chmod +x %{buildroot}%{tcl_sitearch}/iaxclient/tkphone/pref.ui.tcl
install -p %{SOURCE4} %{buildroot}%{_bindir}

install -Dd %{buildroot}%{_datadir}/pixmaps/
install -p %{SOURCE3} %{buildroot}%{_datadir}/pixmaps/tkiaxphone.png
install -p %{SOURCE3} %{buildroot}%{_datadir}/pixmaps/wxiax.png

install -Dd %{buildroot}%{_datadir}/applications/

desktop-file-install --vendor ""			\
	--dir $RPM_BUILD_ROOT%{_datadir}/applications	\
	%{SOURCE1}

desktop-file-install --vendor ""			\
	--dir $RPM_BUILD_ROOT%{_datadir}/applications	\
	%{SOURCE2}	

cd %{buildroot}%{tcl_sitearch}/iaxclient/tkphone/
ln -s iaxcli iaxcli-Linux-%{tkphonearch}


%files
%doc AUTHORS ChangeLog README
%license COPYING.LIB
%{_bindir}/iaxcomm
%{_bindir}/iaxphone
%{_datadir}/iaxcomm/
%{_libdir}/libiaxclient.so.*

%files libiax
%doc lib/libiax2/ChangeLog lib/libiax2/COPYING lib/libiax2/COPYING.LIB
%{_libdir}/libiax.so.*

%files libiax-devel
%{_bindir}/iax-config
%{_includedir}/iax/
%{_libdir}/libiax.so

%files devel
%{_bindir}/stresstest
%{_bindir}/testcall
%{_bindir}/vtestcall
%{_includedir}/iaxclient.h
%{_libdir}/libiaxclient.so
%{_libdir}/pkgconfig/iaxclient.pc

%files -n tcl-iaxclient
%doc contrib/tcl/README.txt
%{tcl_sitearch}/tcliaxclient0.2/

%files -n tkiaxphone
%{_bindir}/run-tkiaxphone.sh
%{_bindir}/tkiaxphone
%{tcl_sitearch}/iaxclient/
%{_datadir}/applications/tkiaxphone.desktop
%{_datadir}/pixmaps/tkiaxphone.png

%files -n wxiax
%{_bindir}/wxiax
%{_datadir}/applications/wxiax.desktop
%{_datadir}/pixmaps/wxiax.png

%changelog
* Sun Jan 19 2025 Sandro Mani <manisandro@gmail.com> - 2.1-0.52.beta3
- BR: tk-devel < 1:9

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-0.51.beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 2.1-0.50.beta3
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-0.49.beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-0.48.beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-0.47.beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-0.46.beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Feb 24 2023 Florian Weimer <fweimer@redhat.com> - 2.1-0.45.beta3
- Port to C99

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-0.44.beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug 04 2022 Scott Talbert <swt@techie.net> - 2.1-0.43.beta3
- Rebuild with wxWidgets 3.2

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-0.42.beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 30 2022 Sandro Mani <manisandro@gmail.com> - 2.1-0.41.beta3
- Rebuild (ilbc)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-0.40.beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-0.39.beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-0.38.beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-0.37.beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-0.36.beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 25 2019 Scott Talbert <swt@techie.net> - 2.1-0.35.beta3
- Rebuild with wxWidgets GTK3 build

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-0.34.beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-0.33.beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 23 2018 Scott Talbert <swt@techie.net> - 2.1-0.32.beta3
- Rebuild with wxWidgets 3.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-0.31.beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 18 2018 Sandro Mani <manisandro@gmail.com> - 2.1-0.30.beta3
- Add missing BR: gcc-c++, make

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-0.29.beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-0.28.beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-0.27.beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-0.26.beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-0.25.beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 19 2016 Tom Callaway <spot@fedoraproject.org> - 2.1-0.24.beta3
- spec file cleanups

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-0.23.beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 04 2015 Sandro Mani <manisandro@gmail.com> - 2.1-0.22.beta3
- Rebuild (GCC5)

* Thu Jan 08 2015 Sandro Mani <manisandro@gmail.com> - 2.1-0.21.beta3
- Ship bundled libiax2 in -libiax
- Use system spandsp
- Use system ilbc

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-0.20.beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul  3 2014 Peter Robinson <pbrobinson@fedoraproject.org> 2.1-0.19.beta3
- Add patch to fix build on aarch64

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-0.18.beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 2.1-0.17.beta3
- Updated requires to require tcl-8.6

* Wed May 21 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 2.1-0.16.beta3
- Rebuilt for https://fedoraproject.org/wiki/Changes/f21tcl86

* Tue Dec 03 2013 Tom Callaway <spot@fedoraproject.org> - 2.1-0.15.beta3
- Fix format-security issue (bz 1037126)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-0.14.beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 15 2013 Tom Callaway <spot@fedoraproject.org> - 2.1-0.13.beta3
- add memory barriers for arm (bz 927443)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-0.12.beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-0.11.beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-0.10.beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 2.1-0.9.beta3
- Rebuild for new libpng

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-0.8.beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 14 2010 Dan Horák <dan@danny.cz> - 2.1-0.7.beta3
- rebuilt against wxGTK-2.8.11-2

* Wed Jun 02 2010 Rakesh Pandit <rakesh@fedoraproject.org> - 2.1-0.6.beta3
- Bump for new liboggz lib

* Wed Feb 10 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 2.1-0.5.beta3
- fix implicit DSO linking issue with libm

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-0.4.beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Mar 12 2009 Tom "spot" Callaway <tcallawa@redhat.com> 2.1-0.3.beta3
- fix lib/libiax2/iax-config.in to not use wrong /usr/lib

* Mon Nov  3 2008 Tom "spot" Callaway <tcallawa@redhat.com> 2.1-0.2.beta3
- fix theora detection

* Tue Jun 10 2008 Tom "spot" Callaway <tcallawa@redhat.com> 2.1-0.1.beta3
- Initial package for Fedora

