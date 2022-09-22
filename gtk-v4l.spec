Name:		gtk-v4l
Version:	0.4
Release:	24%{?dist}
Summary:	Video4Linux Device Preferences
License:	LGPLv2+
URL:		http://fedorahosted.org/gtk-v4l
Source0:	https://fedorahosted.org/releases/g/t/%{name}/%{name}-%{version}.tar.gz
Patch0:         0001-gtk-v4l-device-remove-source-on-finalize.patch
Patch1:         0002-gtk-v4l-Werror-format-security.patch
BuildRequires:  gcc
BuildRequires:	scrollkeeper
BuildRequires:	libv4l-devel >= 0.6
BuildRequires:	gtk3-devel >= 3.0
BuildRequires:	libgudev1-devel >= 151
BuildRequires: make


%description
gtk-v4l is a Video4Linux Web camera control app

%package devel
Summary:        Development files for gtk-v4l
Requires:       %{name} = %{version}-%{release}

%description devel
Contains library and header files for gtk-v4l


%prep
%setup -q
%patch0 -p1
%patch1 -p1


%build
%configure --disable-static
make CFLAGS="$RPM_OPT_FLAGS"  %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%ldconfig_scriptlets


%files
%doc COPYING AUTHORS ChangeLog README
%{_bindir}/gtk-v4l
%{_datadir}/applications/gtk-v4l.desktop
%{_libdir}/libgtkv4l.so.0.0.0
%{_libdir}/libgtkv4l.so.0

%files devel
%doc COPYING
%{_includedir}/gtk-v4l-widget.h
%{_includedir}/gtk-v4l-device-list.h
%{_libdir}/libgtkv4l.so


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jun 10 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 0.4-8
- Fix FTBFS with -Werror=format-security (#1037113, #1106738)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jul 31 2012 Huzaifa Sidhpurwala <huzaifas@redhat.com> - 0.4.4
- Change of license, from GPLv2+ to LGPLv2+

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May  9 2012 Hans de Goede <hdegoede@redhat.com> - 0.4-2
- Remove glib source on a device unplug, this avoids errors when the fd
  gets reused later

* Fri Jan 20 2012 Huzaifa Sidhpurwala <huzaifas@redhat.com> - 0.4-1
- New upstream release

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.3-5
- Rebuild for new libpng

* Sat Mar 12 2011 Hans de Goede <hdegoede@redhat.com> - 0.3-4
- Don't try to reset inactive controls (avoids error dialogs)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jun 03 2010 Huzaifa Sidhpurwala <huzaifas@redhat.com> 0.3-2
- New upstream, version bump

* Thu Feb 25 2010 Huzaifa Sidhpurwala <huzaifas@redhat.com> 0.1-2
- Correct spelling mistakes, remove Requires

* Wed Feb 24 2010 Huzaifa Sidhpurwala <huzaifas@redhat.com> 0.1-1
- Initial build
