Name:           ski
Version:        1.3.2
Release:        36%{?dist}
Summary:        IA-64 user and system mode simulator

License:        GPLv2+
URL:            http://ski.sourceforge.net
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch1:         ski-1.3.2-asm-page.patch
Patch2:         ski-1.3.2-header.patch
Patch3:         ski-1.3.2-nohayes.patch
Patch4:         ski-1.3.2-uselib.patch
Patch5:         ski-1.3.2-ustat.patch
# https://gitweb.gentoo.org/repo/gentoo.git/tree/app-emulation/ski/files/ski-1.3.2-gcc-10.patch
Patch6:         ski-1.3.2-gcc-10.patch

ExcludeArch:    aarch64

BuildRequires: make
BuildRequires:  libglade2-devel ncurses-devel elfutils-libelf-devel libgnomeui-devel motif-devel
BuildRequires:  automake autoconf libtool gperf bison flex
BuildRequires:  libtool-ltdl-devel
BuildRequires:  gcc
Requires: %{name}-libs = %{version}-%{release}


%description
The Ski IA-64 user and system simulator originally developed by HP.


%package libs
Summary: Shared library for the ski simulator

%description libs
Shared library for the ski simulator


%package devel
Summary: Development files for the ski simulator
Requires: %{name}-libs = %{version}-%{release}

%description devel
The ski-devel package includes the static libraries and header files
for the support library for the Ski simulator.


%prep
%autosetup -p1


%build
./autogen.sh

%configure --with-x11 --with-gtk --enable-shared --disable-static

# Don't use rpath!
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

# fix linking
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool

make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_libdir}/*.la


%files
%license COPYING
%doc AUTHORS NEWS README TODO ChangeLog
%doc doc/ski-notes.html doc/manual/*.pdf
%config(noreplace) %{_sysconfdir}/X11/app-defaults/*
%{_bindir}/ski
%{_bindir}/bski*
%{_bindir}/gski
%{_bindir}/xski
%{_bindir}/ski-fake-xterm
%{_mandir}/man1/*
%{_datadir}/%{name}

%files libs
%license COPYING
%{_libdir}/libski-*.so.*

%files devel
%{_bindir}/ski-config
%{_includedir}/ski-1.3
%{_libdir}/libski.so


%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 03 2020 Dan Horák <dan[at]danny.cz> - 1.3.2-31
- fix build with gcc 10

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Sep  7 2016 Peter Robinson <pbrobinson@fedoraproject.org> 1.3.2-22
- Exclude aarch64

* Tue Feb 16 2016 Dan Horák <dan[at]danny.cz> - 1.3.2-21
- fix FTBFS (#1308134)
- spec cleanup

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 01 2015 Jon Ciesla <limburgher@gmail.com> - 1.3.2-19
- Move from lesstif to motif.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.3.2-11
- Rebuild for new libpng

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan  1 2011 Dan Horák <dan[at]danny.cz> 1.3.2-9
- updated the nohayes patch to completely remove TIOC[GS]HAYESESP

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov  1 2008 Dan Horak <dan[at]danny.cz> 1.3.2-6
- rename the ppc patch to nohayes and add other arches without TIOC[GS]HAYESESP

* Wed Apr 30 2008 Dan Horak <dan[at]danny.cz> 1.3.2-5
- fix attributes for files in subpackages

* Thu Apr 10 2008 Dan Horak <dan[at]danny.cz> 1.3.2-4
- fix build on ppc

* Wed Apr  9 2008 Dan Horak <dan[at]danny.cz> 1.3.2-3
- fix linking issues
- use -libs for the subpackage

* Sat Apr  5 2008 Dan Horak <dan[at]danny.cz> 1.3.2-2
- fix compile in rawhide (kernel >= 2.6.25-rc5)

* Tue Feb 19 2008 Dan Horak <dan[at]danny.cz> 1.3.2-1
- update to version 1.3.2
- remove patches integrated into upstream codebase
- create a lib subpackage to be multi-lib aware

* Sat Nov 10 2007 Dan Horak <dan[at]danny.cz> 1.2.6-2
- merge libski and libskiui

* Sat Oct  6 2007 Dan Horak <dan[at]danny.cz> 1.2.6-1
- initial Fedora version
