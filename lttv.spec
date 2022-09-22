Summary: Linux Trace Toolkit Viewer
Name:    lttv
Version: 1.5
Release: 22%{?dist}
License: GPLv2
URL:     http://lttng.org/lttv
Source:  http://www.lttng.org/files/packages/lttv-%{version}.tar.bz2
Source1: lttv.desktop
Source2: lttv-icon.svg
Source3: lttv.1
Source4: lttv.real.1
Source5: lttv-gui.1
Patch0:  lttv.git-b9ce0bad-fsf-address-change.patch
Patch1:  lttv.git-adc007f3-licence-change.patch

BuildRequires:  gcc
BuildRequires: glib2-devel
BuildRequires: gtk2-devel
BuildRequires: popt-devel
BuildRequires: libbabeltrace-devel
BuildRequires: desktop-file-utils
BuildRequires: make

%global __provides_exclude_from ^%{_libdir}/lttv/plugins/.*\\.so$

%description
LTTV is a modular stand-alone viewer for Linux kernel and user-space traces. 
It can perform analysis on traces of a Linux kernel or user-space applications 
instrumented with LTTng and UST.

%package devel
Summary:        Include Files and Libraries mandatory for LTTV modules development
License:        GPLv2
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains all necessary include files and libraries needed
to develop extra LTTV modules.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
iconv -f iso8859-1 -t utf-8 AUTHORS > AUTHORS.conv && mv -f AUTHORS.conv AUTHORS

%build
%configure --disable-dependency-tracking --disable-static --disable-silent-rules
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
rm -vf %{buildroot}/%{_libdir}/*.la
rm -vf %{buildroot}/%{_libdir}/lttv/plugins/*.la
cp -p %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/lttv
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}
mkdir -p %{buildroot}%{_mandir}/man1/
cp -p %{SOURCE3} %{buildroot}%{_mandir}/man1/
cp -p %{SOURCE4} %{buildroot}%{_mandir}/man1/
cp -p %{SOURCE5} %{buildroot}%{_mandir}/man1/

%files
%doc AUTHORS ChangeLog COPYING README 
%{_bindir}/lttv.real
%{_bindir}/lttv
%{_bindir}/lttv-gui
%{_libdir}/lttv
%{_datadir}/pixmaps/lttv
%{_datadir}/applications/lttv.desktop
%{_mandir}/man1/%{name}*

%files devel
%{_includedir}/lttv
%{_includedir}/lttvwindow

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar 05 2014 <suchakra@fedoraproject.org> - 1.5-5
- Rebuilt for soname change

* Fri Nov 8 2013 Suchakra Sharma <suchakra@fedoraproject.org> - 1.5-4
- Add BR for desktop-file-utils

* Thu Nov 7 2013 Suchakra Sharma <suchakra@fedoraproject.org> - 1.5-3
- Filter provides of plugins
- Minor changes in spec based on review comments 

* Sat Nov 2 2013 Suchakra Sharma <suchakra@fedoraproject.org> - 1.5-2
- Patches for licence change and incorrect FSF address
- Change AUTHORS file format to UTF-8

* Thu Oct 24 2013 Suchakra Sharma <suchakra@fedoraproject.org> - 1.5-1
- New spec based on Yannick's previous spec in Bug 717750

* Thu Sep 1 2011 Yannick Brosseau <yannick.brosseau@gmail.com> - 0.12.38-2
- Add man pages and desktop file
- Update to follow guidelines

* Tue Jun 28 2011 Yannick Brosseau <yannick.brosseau@gmail.com> 0.12.38-1

* Fri Nov 12 2010 - tonyj@novell.com
- Add ltt-private.h

* Thu Nov 11 2010 - tonyj@novell.com
- Package liblttvtraceread_loader for JNI (eclipse). 
- Pull lttv-fix-marker_field.patch from upstream git

* Sun Oct  3 2010 - tonyj@novell.com
- Initial checkin v0.12.35
