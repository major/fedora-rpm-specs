%global have_pygobject3_devel 1
%global have_xtest_devel  1

%global sub_version             1.1
%global libxklavier_version     4.0
%global libxml2_version         2.0

%global libinput_paddir %{_libdir}/%{name}-%sub_version
%global moduledir       %{_libdir}/%{name}-%sub_version/modules
%global kbduidir        %{_libdir}/%{name}-%sub_version/modules/kbdui
%global xkeysenddir     %{_libdir}/%{name}-%sub_version/modules/xkeysend


Name:       input-pad
Version:    1.0.99.20210817
Release:    10%{?dist}
Summary:    On-screen Input Pad to Send Characters with Mouse
License:    LGPL-2.0-or-later
URL:        https://github.com/fujiwarat/input-pad/wiki
Source0:    https://github.com/fujiwarat/input-pad/releases/download/%{version}/%{name}-%{version}.tar.gz
# Patch0:     %%{name}-HEAD.patch


BuildRequires:  gettext-devel
BuildRequires:  gtk3-devel
BuildRequires:  libtool
BuildRequires:  libxkbfile-devel
BuildRequires:  libxklavier-devel       >= %libxklavier_version
BuildRequires:  libxml2-devel           >= %libxml2_version
BuildRequires:  intltool
BuildRequires:  pkgconfig
%if %have_xtest_devel
BuildRequires:  libXtst-devel
%endif
%if %have_pygobject3_devel
BuildRequires:  gobject-introspection-devel
%endif
BuildRequires: make
%if %have_pygobject3_devel
Requires:       gobject-introspection
Requires:       python3-gobject
%endif
Provides:       %{name}-xtest = %{version}-%{release}
Obsoletes:      %{name}-xtest < %{version}-%{release}

%description
The input pad is a tool to send a character on button to text applications.

%package devel
Summary:    Development tools for input-pad
Requires:   %{name} = %{version}-%{release}

%description devel
The input-pad-devel package contains the header files.


%prep
%setup -q
# %%patch0 -p1

%build
autoreconf -v
%configure \
%if %have_xtest_devel
    --enable-xtest              \
%endif
    --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL='install -p'

if [ ! -d $RPM_BUILD_ROOT%kbduidir ] ; then
    mkdir -p $RPM_BUILD_ROOT%kbduidir
fi
if [ ! -d $RPM_BUILD_ROOT%xkeysenddir ] ; then
    mkdir -p $RPM_BUILD_ROOT%xkeysenddir
fi

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a
%if %have_xtest_devel
rm -f $RPM_BUILD_ROOT%xkeysenddir/*.la
rm -f $RPM_BUILD_ROOT%xkeysenddir/*.a
%endif

%find_lang %{name}

%ldconfig_scriptlets

%files -f %{name}.lang
%doc AUTHORS COPYING README
%{_bindir}/input-pad
%dir %libinput_paddir
%dir %moduledir
%dir %xkeysenddir
%xkeysenddir/libinput-pad-xtest-gdk.so
%dir %kbduidir
%{_libdir}/libinput-pad-*.so.*
%if %have_pygobject3_devel
%{_libdir}/girepository-1.0/InputPad-%{sub_version}.typelib
%endif
%{_datadir}/%name
%{_datadir}/pixmaps/input-pad.png
%{_mandir}/man1/input-pad.1.gz

%files devel
%{_includedir}/%{name}-%sub_version
%{_libdir}/libinput-pad-*.so
%{_libdir}/pkgconfig/*.pc
%if %have_pygobject3_devel
%{_datadir}/gir-1.0/InputPad-%{sub_version}.gir
%endif

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.99.20210817-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.99.20210817-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.99.20210817-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.99.20210817-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.99.20210817-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.99.20210817-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 16 2022 Takao Fujiwara <tfujiwar@redhat.com> - 1.0.99.20210817-4
- Migrate license tag to SPDX

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.99.20210817-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.99.20210817-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 17 2021 Takao Fujiwara <tfujiwar@redhat.com> - 1.0.99.20210817-1
- Bump to 1.0.99.20210817-1

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.99.20140916-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.99.20140916-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.99.20140916-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.99.20140916-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 03 2020 Takao Fujiwara <tfujiwar@redhat.com> - 1.0.99.20140916-14
- Replace python2-gobject with python3-gobject

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.99.20140916-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 04 2019 Kalev Lember <klember@redhat.com> - 1.0.99.20140916-12
- Update requires for pygobject3 -> python2-gobject rename

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.99.20140916-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.99.20140916-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.99.20140916-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.99.20140916-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.99.20140916-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Apr 06 2017 Takao Fujiwara <tfujiwar@redhat.com> - 1.0.99.20140916-6
- Disabled eek
- Merged xtest

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.99.20140916-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.99.20140916-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Sep 02 2015 Takao Fujiwara <tfujiwar@redhat.com> - 1.0.99.20140916-3
- Changed URL

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.99.20140916-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Sep 16 2014 Takao Fujiwara <tfujiwar@redhat.com> - 1.0.99.20140916-1
- Bumped to 1.0.99.20140916

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 1.0.3-3
- Rebuilt for gobject-introspection 1.41.4

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Dec 06 2013 Takao Fujiwara <tfujiwar@redhat.com> - 1.0.3-1
- Bumped to 1.0.3

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr 04 2013 Takao Fujiwara <tfujiwar@redhat.com> - 1.0.2-4
- Added autoreconf to use autoconf 2.69 or later. BZ#925590

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 25 2012 Takao Fujiwara <tfujiwar@redhat.com> - 1.0.2-1
- Bumped to 1.0.2

* Wed Apr 04 2012 Takao Fujiwara <tfujiwar@redhat.com> - 1.0.1-4
- Added input-pad-HEAD.patch from upstream

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.0.1-2
- Rebuild for new libpng

* Thu May 19 2011 Takao Fujiwara <tfujiwar@redhat.com> - 1.0.1-1
- Bumped to 1.0.1

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov 30 2010 Takao Fujiwara <tfujiwar@redhat.com> - 1.0.0-1
- Bumped to 1.0.0

* Tue Sep 07 2010 Takao Fujiwara <tfujiwar@redhat.com> - 0.1.2-1
- Bumped to 0.1.2

* Sun Aug 01 2010 Thomas Spura <tomspur@fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Thu Jul 08 2010 Takao Fujiwara <tfujiwar@redhat.com> - 0.1.1-1
- Bumped to 0.1.1
- Added acronym table. Enabled eek-gtk.

* Tue Jun 29 2010 Takao Fujiwara <takao.fujiwara1@gmail.com> - 0.1.0.20100630-1
- Bumped to 0.1.0.20100630

* Tue Jun 22 2010 Takao Fujiwara <takao.fujiwara1@gmail.com> - 0.1.0.20100622-1
- Bumped to 0.1.0.20100622

* Mon Jun 14 2010 Takao Fujiwara <takao.fujiwara1@gmail.com> - 0.1.0.20100614-1
- Initial Implementation. Bug 599316
