Name:		gxmms2
Summary: 	A graphical audio player
Version:	0.7.1
Release:	31%{?dist}
License:	GPL-2.0-only
# If we need to use a git checkout to support an xmms2 release...
# git clone git://git.xmms.se/xmms2/gxmms2.git
# tar cvfj gxmms2-20090811git.tar.bz2 gxmms2
# Source0:      %%{name}-20090811git.tar.bz2
Source0:	http://wejp.k.vu/projects/xmms2/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch0:		gxmms2-0.7.0-implicit-DSO-libX11.patch
Patch1:		gxmms2-0.7.1-xmms2-0.9.3.patch
Patch2:		gxmms2-0.7.1-stdio.patch
URL:		http://wejp.k.vu/projects/xmms2/
BuildRequires:	xmms2-devel >= 0.7, gtk2-devel, pango-devel, atk-devel
BuildRequires:	desktop-file-utils, gcc

%description
gxmms2 is a GTK2 based XMMS2 client, written in C. Its main window is small 
and simple. It includes a playlist editor and a file details dialog.

%package -n gkrellxmms2
Summary:	Gkrellm2 plugin client for XMMS2 
BuildRequires:	gkrellm-devel
BuildRequires: make
Requires:	gkrellm

%description -n gkrellxmms2
gkrellxmms2 is a gkrellm2 plugin for XMMS2. It has a title scroller with a 
position marker and five buttons for playback control. The position marker 
can be moved with the mouse to seek in the current track. The M button 
opens a menu with two items for opening a trackinfo dialog and the media 
library window.

%prep
%setup -q
%patch -P0 -p1 -b .DSO
%patch -P1 -p1 -b .093
%patch -P2 -p1 -b .stdio
sed -i 's|/lib/|/%{_lib}/|g' Makefile

%build
make %{?_smp_mflags} CC="gcc %{optflags}"

%install
make PREFIX=%{buildroot}%{_prefix} KRELLPREFIX=%{buildroot}%{_prefix} install

mkdir -p %{buildroot}/%{_datadir}/pixmaps
mv %{buildroot}%{_datadir}/gxmms2/gxmms2_mini.xpm %{buildroot}/%{_datadir}/pixmaps/gxmms2.xpm
# Don't need anything else in these dirs
rm -rf %{buildroot}%{_datadir}/gxmms2 %{buildroot}%{_datadir}/gkrellxmms2

mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE1}

%files
%doc CHANGELOG COPYING README
%{_bindir}/%{name}*
%{_datadir}/pixmaps/%{name}.xpm
%{_datadir}/applications/*.desktop

%files -n gkrellxmms2
%doc CHANGELOG COPYING README
%{_libdir}/gkrellm2/plugins/gkrellxmms2.so

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Sep 12 2023 Tom Callaway <spot@fedoraproject.org> - 0.7.1-27
- fix this ancient thing to build with xmms2 0.9.3

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Mar 25 2018 Tom Callaway <spot@fedoraproject.org> - 0.7.1-15
- rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.7.1-2
- Rebuild for new libpng

* Mon Dec  5 2011 Tom Callaway <spot@fedoraproject.org> - 0.7.1-1
- update to 0.7.1

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-9.20090811git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jun 30 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 0.7.0-8.20090811git
- fix compile against xmms2 0.7DrNo

* Wed Jun 30 2010 Adam Jackson <ajax@redhat.com> 0.7.0-7.20090811git
- Rebuild for new libxmmsclient

* Wed Feb 10 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 0.7.0-6.20090811git
- fix implicit DSO linking issue with libX11

* Tue Aug 11 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 0.7.0-5.20090811git
- update to git checkout to support xmms 0.6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Dec 24 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.7.0-2
- fix license tag

* Thu Dec  4 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.7.0-1
- Initial package for Fedora
