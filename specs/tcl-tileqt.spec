%{!?tcl_version: %global tcl_version %(echo 'puts $tcl_version' | tclsh)}
%{!?tcl_sitearch: %global tcl_sitearch %{_libdir}/tcl%{tcl_version}}
%global realname tileqt
%global betaver b1

Name:		tcl-%{realname}
Version:	0.4
Release:	0.38.%{betaver}%{?dist}
Summary:	QT widget support for Tile Toolkit
License:	MIT
URL:		http://www.ellogon.org/petasis/index.php?option=com_content&task=view&id=24&Itemid=40
# Upstream uses php nonsense for downloads. Direct link looks like this:
# http://www.ellogon.org/petasis/index.php?option=com_docman&task=doc_download&gid=55&Itemid=37
Source0:	%{realname}%{version}%{betaver}.tar.gz
Patch0:		tcl-tileqt-0.4b1-use-system-tile-headers.patch
Patch1:		tcl-tileqt-0.4b1-tk86.patch
Patch2:		tcl-tileqt-configure-c99.patch
Provides:	%{realname} = %{version}-%{release}
Provides:	tk-%{realname} = %{version}-%{release}
BuildRequires: make
BuildRequires:	tcl-devel, tk-devel, qt-devel, libtool
Requires:	tcl(abi) = 8.6

%description
TileQt is a theme for the tile toolkit, which uses the Qt/KDE style engine to 
draw widgets. Thus, Tk applications that use the tile widget set look the same 
as KDE applications under GNU/Linux.

%prep
%setup -q -n %{realname}%{version}%{betaver}
%patch -P0 -p1 -b .use-system-tile-headers
%patch -P1 -p1 -b .tk86
%patch -P2 -p1
mv configure configure-qt3
cp -a configure-qt4 configure
sed -i 's|/usr/lib/|%{_libdir}/|g' configure

%build
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
install -d %{buildroot}%{tcl_sitearch}
mv %{buildroot}%{_libdir}/%{realname}%{version} %{buildroot}%{tcl_sitearch}/%{realname}%{version}
chmod -x %{buildroot}%{tcl_sitearch}/%{realname}%{version}/pkgIndex.tcl

%files
%license license.terms
%doc ChangeLog
%{tcl_sitearch}/%{realname}%{version}/

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-0.38.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-0.37.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-0.36.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-0.35.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Mar 17 2023 Florian Weimer <fweimer@redhat.com> - 0.4-0.34.b1
- Port configure script to C99

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-0.33.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-0.32.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-0.31.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-0.30.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-0.29.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-0.28.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-0.27.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-0.26.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-0.25.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-0.24.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-0.23.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-0.22.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-0.21.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-0.20.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-0.19.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Tom Callaway <spot@fedoraproject.org> - 0.4-0.18.b1
- modernize spec file

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-0.17.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-0.16.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-0.15.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 29 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 0.4-0.14.b1
- Changed requires to require tcl-8.6

* Wed May 21 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 0.4-0.13.b1
- Rebuilt for https://fedoraproject.org/wiki/Changes/f21tcl86

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-0.12.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-0.11.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-0.10.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-0.9.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.4-0.8.b1
- Rebuild for new libpng

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-0.7.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jun 29 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 0.4-0.6.b1
- fix code to build againt tk86

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-0.5.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-0.4.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Dec 23 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.4-0.3.b1
- build against tile bits in tk 8.5

* Wed Oct 15 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.4-0.2.b1
- use qt4 configure script

* Wed Jun 25 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.4-0.1.b1
- initial package for Fedora
