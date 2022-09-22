%global gittag v0.23
%global commit 83a0bd56de9cfce918a47bdf601a9ecdb5cd56de

Name:           superkb
Version:        0.23
Release:        5%{?dist}
Summary:        Graphical application launcher for Linux
License:        GPLv2
URL:            http://superkb.org/
Source0:        https://gitlab.com/alvarezp2000/%{name}/-/archive/%{gittag}/%{name}-v%{version}.tar.gz
Patch0:         patch-makeinstall.patch
Patch1:         patch-fix_ldlibs_m_position_on_invocation.patch
BuildRequires: make
BuildRequires:  cairo-devel
BuildRequires:  gcc
BuildRequires:  gdk-pixbuf2-xlib-devel
BuildRequires:  help2man
BuildRequires:  imlib2-devel
BuildRequires:  libXft-devel
BuildRequires:  libXinerama-devel
BuildRequires:  pango-devel
BuildRequires:  xorg-x11-proto-devel

%description
Graphical application launcher for Linux. It works by activating
upon a hot key press, usually Super_L or Super_R. On activation it shows a
keyboard on screen with the keys and its corresponding actions


%prep
%autosetup -n %{name}-%{gittag}


%build
make %{?_smp_mflags} PREFIX=%{_prefix} LIB_PREFIX=%{_libdir} FED_FLAGS="%{optflags} -Wno-return-type -Wno-unused-result -Wno-maybe-uninitialized -Wno-deprecated-declarations -Wno-unused-variable"


%install
make install DESTDIR=%{buildroot} PREFIX=%{_prefix} LIB_PREFIX=%{_libdir}


%files
%doc LICENSE
%{_bindir}/%{name}
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/drawkblibs-cairo.so
%{_libdir}/%{name}/drawkblibs-xlib.so
%{_libdir}/%{name}/puticon-gdkpixbuf.so
%{_libdir}/%{name}/puticon-imlib2.so
%attr(0644, root, root)  %{_mandir}/man1/superkb.1.*


%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov  4 22:28:41 CST 2020 Renich Bon Ciric <renich@woralelandia.com> - 0.23-1
- Updated to v0.23.
- This release includes some aesthetic fixes, compilation warning fixes and
  fixes to make the job easier for package maintainers.
- Re-generated the old patches that were still useful.
- Removed patches that weren't necessary anymore.
- Added patch to fix lib position on the compiler.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Mar 20 2015 Richard Hughes <richard@hughsie.com> - 0.22-7
- Rebuilt for gdk-pixbuf2-xlib split

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 03 2013 Ruben Guerra Marin <rugebiker@fedoraproject.org> 0.22-3
- Removed duplicated file superkb.1.gz

* Mon Jul 01 2013 Ruben Guerra Marin <rugebiker@fedoraproject.org> 0.22-2
- Fixed the SPEC to comply with the Fedora flags

* Sun Jun 23 2013 Ruben Guerra Marin <rugebiker@fedoraproject.org> 0.22-1
- Initial version of the package
