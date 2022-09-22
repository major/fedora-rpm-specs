%{!?tcl_version: %global tcl_version %(echo 'puts $tcl_version' | tclsh)}
%{!?tcl_sitearch: %global tcl_sitearch %{_libdir}/tcl%{tcl_version}}

Name:           tkdnd
Version:        2.8
Release:        15%{?dist}
Summary:        Tk extension that adds native drag & drop capabilities

License:        BSD
URL:            http://tkdnd.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}%{version}-src.tar.gz

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  libXext-devel
BuildRequires:  libXft-devel
BuildRequires:  libXt-devel
BuildRequires:  tk-devel
Requires: tcl(abi) = 8.6

%description
Tk Drag & Drop: tkdnd is an extension that adds native drag & drop capabilities
to the tk toolkit. It can be used with any tk version equal or greater to 8.4.
Under unix the drag & drop protocol in use is the XDND protocol version 4
(also used by the QT toolkit, KDE & GNOME Desktops).

%prep
%setup -q -n %{name}%{version}

%build
%configure --enable-symbols
make %{?_smp_mflags}

%install
make libdir=%{tcl_sitearch} DESTDIR=%{buildroot} install \
        INSTALL_DATA="install -pm 644" INSTALL_LIBRARY="install -pm 755"
chmod +x %{buildroot}%{tcl_sitearch}/%{name}%{version}/lib%{name}%{version}.so


%files
%doc doc/*
%{_mandir}/mann/tkDND.n.gz
%{tcl_sitearch}/%{name}%{version}/


%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.8-6
- Escape macros in %%changelog

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov 08 2016 Filipe Rosset <rosset.filipe@gmail.com> - 2.8-2
- Spec clean up, silent rpmlint + rebuilt rhbz #1074039 and rhbz #1308188

* Sun Feb 28 2016 Sander Hoentjen <sander@hoentjen.eu> 2.8-1
- Update to latest upstream
- make .so executable to generate debuginfo correctly

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 2.6-3
- Changed requires to require tcl-8.6

* Wed May 21 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/f21tcl86

* Mon Mar 03 2014 Sander Hoentjen <sander@hoentjen.eu> - 2.6-1
- Update to latest upstream release

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0a2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0a2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0a2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0a2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0a2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0a2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0a2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Dec 03 2008 Sander Hoentjen <sander@hoentjen.eu> - 1.0a2-12
- Add missing requires on libXft

* Wed Dec 03 2008 Sander Hoentjen <sander@hoentjen.eu> - 1.0a2-11
- Add requires on tcl

* Tue Feb 12 2008 Sander Hoentjen <sander@hoentjen.eu> - 1.0a2-10
- Rebuilt for gcc-4.3

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 1.0a2-9
- Rebuild for selinux ppc32 issue.

* Tue Jul 03 2007 Sander Hoentjen <sander@hoentjen.eu> - 1.0a2-8
- Move to tcl_sitearch

* Mon Aug 28 2006 Sander Hoentjen <sander@hoentjen.eu> - 1.0a2-7
- FC6 Mass Rebuild

* Thu Jun 08 2006 Sander Hoentjen <sander@hoentjen.eu> - 1.0a2-6
- Removed the extra directory in %%'_doc by adding a wildcard
- Moved the "rm -rf $RPM_BUILD_ROOT" to the very first line in %%'_install

* Thu Jun 08 2006 Sander Hoentjen <sander@hoentjen.eu> - 1.0a2-5
- dropped sed magic, install files by hand instead

* Fri Jun 02 2006 Sander Hoentjen <sander@hoentjen.eu> - 1.0a2-4
- 64bit patch for tk headers too now

* Thu Jun 01 2006 Sander Hoentjen <sander@hoentjen.eu> - 1.0a2-3
- added 64bit patch
- sed magic instead of passing libdir to configure and rm libtkdnd.dll

* Wed May 31 2006 Sander Hoentjen <sander@hoentjen.eu> - 1.0a2-2
- fixed W: tkdnd unstripped-binary-or-object /usr/lib/tkdnd/libtkdnd.so (thanks Paul Howard)
- removed tcl-devel als buildreq since it is required by tk-devel

* Tue May 30 2006 Sander Hoentjen <sander@hoentjen.eu> - 1.0a2-1
- created
