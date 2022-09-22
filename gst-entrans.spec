%global gstversion 1.0
%global gst_minver 1.0.0

Name:           gst-entrans
Version:        1.4.1
Release:        4%{?dist}
Summary:        Plug-ins and tools for transcoding and recording with GStreamer

License:        LGPLv2+
URL:            http://gentrans.sourceforge.net/
Source0:        http://downloads.sourceforge.net/gentrans/%{name}-%{version}.tar.gz

# Patch python shebang to /usr/bin/python2
Patch0:         gst-entrans-python_shebang.patch
Patch1:         gst-entrans-enplayer_python_shebang.patch

BuildRequires:  make
BuildRequires:  gstreamer1-devel >= %{gst_minver}
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  alsa-lib-devel
# For autoreconf
BuildRequires:  gettext-devel libtool
Requires:       gstreamer1 >= %{gst_minver}
Requires:       gstreamer1-plugins-entrans%{?_isa} = %{version}-%{release}
Requires:       python3-gstreamer1

%description
GEntrans is a software package providing a collection of plug-ins and tools 
for the GStreamer multimedia framework specifically geared towards transcoding 
and recording purposes.

GStreamer allows for easy multimedia processing and creation of multimedia 
applications, as e.g. demonstrated by a number of players and some other 
applications already built on it. The purpose here is to concentrate on using 
the framework for transcoding purposes.


%package -n gstreamer1-plugins-entrans
Summary:        GStreamer plug-ins from GEntrans
Obsoletes:      gstreamer-plugins-entrans < 0.10.4-4

%description -n gstreamer1-plugins-entrans
GEntrans is a software package providing a collection of plug-ins and tools 
for the GStreamer multimedia framework specifically geared towards transcoding 
and recording purposes.

This package provides several GStreamer plugins from GEntrans.


%package -n gstreamer1-plugins-entrans-docs
Summary:        Documentation for GStreamer plug-ins from GEntrans
BuildArch:      noarch
BuildRequires:  gtk-doc
Obsoletes:      gstreamer-plugins-entrans-docs < 0.10.4-4

%description -n gstreamer1-plugins-entrans-docs
GEntrans is a software package providing a collection of plug-ins and tools 
for the GStreamer multimedia framework specifically geared towards transcoding 
and recording purposes.

This package provides documentation for several GStreamer plugins from GEntrans.


%prep
%setup -q
%patch0 -p1 -b .python_shebang
%patch1 -p1 -b .python_shebang


%build
# Add aarch64 support to build
autoreconf -f -i
%configure --enable-debug --disable-static --enable-gtk-doc
make %{?_smp_mflags}


%check
make check


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

# These files shouldn't be in the RPM
rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{gstversion}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{gstversion}/*.a

# Symlink the old executable name for compatibility
ln -s entrans-1.0 $RPM_BUILD_ROOT%{_bindir}/entrans
ln -s enplayer-1.0 $RPM_BUILD_ROOT%{_bindir}/enplayer



%files
%doc AUTHORS COPYING
%doc docs/manual/html/
%{_bindir}/entrans
%{_bindir}/entrans-1.0
%{_bindir}/enplayer
%{_bindir}/enplayer-1.0
%doc %{_mandir}/man1/entrans-*
%doc %{_mandir}/man1/enplayer-*


%files -n gstreamer1-plugins-entrans
%doc COPYING
%{_libdir}/gstreamer-%{gstversion}/libgstentransalsa.so
%{_libdir}/gstreamer-%{gstversion}/libgstentransavidemux.so
%{_libdir}/gstreamer-%{gstversion}/libgstentransentrans.so
%{_libdir}/gstreamer-%{gstversion}/libgstentransmencoder.so
%{_libdir}/gstreamer-%{gstversion}/libgstentranstranscode.so
%{_libdir}/gstreamer-%{gstversion}/libgstentransvirtualdub.so
%{_libdir}/gstreamer-%{gstversion}/libgstentransyuv4mpeg.so

%files -n gstreamer1-plugins-entrans-docs
%doc COPYING
%doc %{_datadir}/gtk-doc/html/%{name}-plugins-%{gstversion}/


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Aug 20 2021 Theodore Lee <theo148@gmail.com> - 1.4.1-2
- Correct location of BuildRequires make tag

* Fri Aug 20 2021 Theodore Lee <theo148@gmail.com> - 1.4.1-1
- Update to upstream 1.4.1 bugfix release

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 18 2019 Theodore Lee <theo148@gmail.com> - 1.4.0-1
- Update to upstream 1.4.0 release (Python 3 port), resolving BZ 1737989
- Drop python2 BuildRequires

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 1.2.2-2
- Rebuild with fixed binutils

* Sat Jul 28 2018 Theodore Lee <theo148@gmail.com> - 1.2.2-1
- Update to upstream 1.2.2 release, fixes gtk-doc build, resolving BZ 1555852
- Add python2 BuildRequires for gtk-doc build
- Add check section to run testsuite

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 26 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.2.1-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Theodore Lee <theo148@gmail.com> - 1.2.1-1
- Update to upstream 1.2.1 release, should fully resolve BZ 1467136
- Add python shebang patch for enplayer

* Mon Jul 03 2017 Gwyn Ciesla <limburgher@gmail.com> - 1.2.0-1
- 1.2.0, resolves BZ 1467136.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Nov 10 2016 Theodore Lee <theo148@gmail.com> - 1.0.3-1
- Update to upstream 1.0.3 release

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Sep 06 2015 Theodore Lee <theo148@gmail.com> - 1.0.2-5
- Correct dependency on gstreamer-python to python-gstreamer1
- Add patch for python shebang

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 03 2014 Theodore Lee <theo148@gmail.com> - 1.0.2-1
- Update to 1.0.2 release
- Update man file path

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Apr 03 2013 Theodore Lee <theo148@gmail.com> - 1.0.0-1
- Update to 1.0.0 release (GStreamer 1.0 port)
- Switch over build dependencies to GStreamer 1.0
- Rename gstreamer-plugins-entrans[-docs] to gstreamer1-plugins-entrans[-docs]
- Run autoreconf in build for initial aarch64 build support

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 06 2012 Theodore Lee <theo148@gmail.com> - 0.10.4-1
- Update to 0.10.4 release
- Drop liboil-devel buildrequires

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 17 2011 Theodore Lee <theo148@gmail.com> - 0.10.3-4
- Drop requires on gtk-doc

* Sun Jun 19 2011 Theodore Lee <theo148@gmail.com> - 0.10.3-3
- Add license files to subpackages
- Move gtk-doc BuildRequires to plugin docs subpackage

* Fri Jun 10 2011 Theodore Lee <theo148@gmail.com> - 0.10.3-2
- Specify minimum GStreamer versions
- Be more specific in the files section
- Include documentation
- Split GStreamer plugins into separate packages

* Tue Nov 23 2010 Theodore Lee <theo148@gmail.com> - 0.10.3-1
- Latest upstream release

* Thu Sep 30 2010 Theodore Lee <theo148@gmail.com> - 0.10.2-1
- Tweaked install to remove static libraries

* Wed Sep 29 2010 Theodore Lee <theo148@gmail.com> - 0.10.2-0.1.aa
- Initial specfile
