%global commit 28d2f659985241be222c145719ee5d75aa02b9ee
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20130131
%define debug_package %{nil}

Name:           notify-sharp
Version:        0.4.1
Release:        0.21.%{commitdate}git%{shortcommit}%{?dist}
Summary:        A C# implementation for Desktop Notifications
License:        MIT
URL:            https://github.com/hyperair/notify-sharp
# git clone https://github.com/hyperair/notify-sharp.git
# tar --exclude-vcs -cZf notify-sharp-git28d2f65.tar.xz notify-sharp
Source0:        notify-sharp-git%{shortcommit}.tar.xz
# Use dbus-sharp 2.0
Patch1:		notify-sharp-0.4.1-dbus2.patch
BuildRequires: make
BuildRequires:  mono-devel, gtk-sharp2-devel, gnome-sharp-devel, dbus-sharp-glib-devel
BuildRequires:  autoconf, automake, libtool
BuildRequires:  monodoc-devel
# Mono only available on these:
ExclusiveArch: %{mono_arches}

%description
notify-sharp is a C# client implementation for Desktop Notifications,
i.e. notification-daemon. It is inspired by the libnotify API.

Desktop Notifications provide a standard way of doing passive pop-up
notifications on the Linux desktop. These are designed to notify the
user of something without interrupting their work with a dialog box
that they must close. Passive popups can automatically disappear after
a short period of time.

%package devel
Summary:        Development files for notify-sharp
Requires:       %{name} = %{version}-%{release} 
Requires:       pkgconfig

%description devel
Development files for notify-sharp

%package doc
Summary:        Documentation files for notify-sharp
Requires:       %{name} = %{version}-%{release} 
Requires:       monodoc

%description doc
Documentation files for notify-sharp

%prep
%setup -qn %{name}
%patch -P1 -p1 -b .dbus2

sed -i "s#gmcs#mcs#g" configure.ac

%build
autoreconf -vif
%configure --libdir=%{_prefix}/lib --disable-docs
make

%install
make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_libdir}/pkgconfig/
test "%{_libdir}" = "%{_prefix}/lib" || mv $RPM_BUILD_ROOT%{_prefix}/lib/pkgconfig/*.pc $RPM_BUILD_ROOT%{_libdir}/pkgconfig/


%files
%doc COPYING NEWS README AUTHORS
%{_prefix}/lib/mono/gac/notify-sharp/
%{_prefix}/lib/mono/notify-sharp/

%files devel
%{_libdir}/pkgconfig/notify-sharp.pc

%files doc

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-0.21.20130131git28d2f65
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-0.20.20130131git28d2f65
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-0.19.20130131git28d2f65
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-0.18.20130131git28d2f65
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-0.17.20130131git28d2f65
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-0.16.20130131git28d2f65
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-0.15.20130131git28d2f65
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-0.14.20130131git28d2f65
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-0.13.20130131git28d2f65
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-0.12.20130131git28d2f65
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-0.11.20130131git28d2f65
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 03 2020 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 0.4.1-0.10.20130131git28d2f65
- built without docs because mdoc.exe is not built with Mono 6 and mcs anymore

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-0.9.20130131git28d2f65
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 31 2019 Tom Callaway <spot@fedoraproject.org> - 0.4.1-0.8.20130131git28d2f65
- rebuild for proper provides

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-0.7.20130131git28d2f65
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-0.6.20130131git28d2f65
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-0.5.20130131git28d2f65
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-0.4.20130131git28d2f65
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-0.3.20130131git28d2f65
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-0.2.20130131git28d2f65
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 27 2017 Tom Callaway <spot@fedoraproject.org> - 0.4.1-0.1.20130131git28d2f65
- update to latest git
- build against dbus-sharp-2.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-0.28.20100411svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 13 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-0.27.20100411svn
- mono rebuild for aarch64 support

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-0.26.20100411svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-0.25.20100411svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 18 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.4.0-0.24.20100411svn
- Rebuild (mono4)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-0.23.20100411svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-0.22.20100411svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-0.21.20100411svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-0.20.20100411svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-0.19.20100411svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 06 2012 Christian Krause <chkr@fedoraproject.org> - 0.4.0-0.18.20100411svn
- Change paths for mono assemblies according to updated packaging
  guidelines (http://fedoraproject.org/wiki/Packaging:Mono)
- Use dbus-sharp instead of deprecated ndesk-dbus

* Wed May 09 2012 Karsten Hopp <karsten@redhat.com> 0.4.0-0.17.20100411svn
- fix PPC filelist

* Wed May 02 2012 Dennis Gilmore <dennis@ausil.us> - 0.4.0-0.16.20100411svn
- make the location for docs match whats in the mono package
- use the mono_arches macro for ExclusiveArch

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-0.15.20100411svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-0.14.20100411svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 07 2011 Dan Horák <dan[at]danny.cz> - 0.4.0-0.13.20100411svn
- updated the supported arch list

* Thu Oct 28 2010 Christian Krause <chkr@fedoraproject.org> - 0.4.0-0.12.20100411svn
- Rebuilt against Mono 2.8

* Sun Apr 11 2010 Christian Krause <chkr@fedoraproject.org> - 0.4.0-0.11.20100411svn
- Update to latest snapshot
- Fix minor directory ownership issue (BZ 512564)

* Mon Oct 26 2009 Dennis Gilmore <dennis@ausil.us> - 0.4.0-0.10.20080912svn
- Switch to ExcludeArch sparc64 has no mono

* Thu Aug 20 2009 Toshio Kuratomi <toshio@fedoraproject.org> - 0.4.0-0.9.20080912svn.1
- Rebuild to pick up ppc64 builds

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-0.8.20080912svn.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jun 17 2009 Karsten Hopp <karsten@redhat.com> 0.4.0-0.7.20080912svn.1
- mono is available on s390x

* Fri May 29 2009 Xavier Lamien <laxathom@fedoraproject.org> - 0.4.0-0.7.20080912svn
- Build arch ppc64.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-0.6.20080912svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Oct 9 2008 Sindre Pedersen Bjørdal <sindrepb@fedoraproject.org - 0.4.0-0.5.20080912svn
- Fix doc package dependencies. 

* Wed Sep 24 2008 Sindre Pedersen Bjørdal <sindrepb@fedoraproject.org - 0.4.0-0.4.20080912svn
- Replace with simple sed line in spec
- Build documentation, add monodoc dependencies.

* Wed Sep 24 2008 Sindre Pedersen Bjørdal <sindrepb@fedoraproject.org - 0.4.0-0.3.20080912svn
- Add patch to fix libdir on all arches.

* Mon Sep 22 2008 Sindre Pedersen Bjørdal <sindrepb@fedoraproject.org - 0.4.0-0.2.20080912svn
- Update changelog
- Fix whitespace issues

* Fri Sep 12 2008 Sindre Pedersen Bjørdal <sindrepb@fedoraproject.org - 0.4.0-0.1.20080912svn
- Redid svn checkout and tarball creation process
- Added autoreconfig shebang + autotools deps

* Sat May 31 2008 Nigel Jones <dev@nigelj.com> - 0.4.0-0.1.20080531svn
- Initial RPM based on David Nielsen's work on fedorapeople.org
