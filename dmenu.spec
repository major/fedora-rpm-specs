Name:           dmenu
Version:        5.1
Release:        2%{?dist}
Summary:        Generic menu for X
License:        MIT
URL:            http://tools.suckless.org/%{name}
Source0:        http://dl.suckless.org/tools/%{name}-%{version}.tar.gz
BuildRequires:  binutils
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  fontconfig-devel
BuildRequires:  libX11-devel
BuildRequires:  libXft-devel
BuildRequires:  libXinerama-devel
BuildRequires:  make
BuildRequires:  sed

%description
Dynamic menu is a generic menu for X, originally designed for dwm. It manages
huge amounts (up to 10.000 and more) of user defined menu items efficiently.

%prep
%autosetup

%build
%make_build \
  X11INC=%{_includedir} \
  X11LIB=%{_libdir} \
  CFLAGS='-std=c99 -pedantic -Wall $(INCS) $(CPPFLAGS) %{build_cflags}' \
  LDFLAGS='%{build_ldflags} $(LIBS)'

%install
%make_install PREFIX=%{_prefix}

%files
%doc LICENSE README
%{_bindir}/%{name}*
%{_bindir}/stest
%{_mandir}/man*/%{name}.*
%{_mandir}/man*/stest.*

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Feb 11 2022 Frantisek Sumsal <frantisek@sumsal.cz> - 5.1-1
- 5.1 bump
- Cleanup the prep/build phase to make it work correctly with package notes
(kudos to Zbigniew Jędrzejewski-Szmek for the patch)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Oct 31 2020 Petr Šabata <contyk@redhat.com> - 5.0-1
- 5.0 bump
- Memory leak fixes

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep 05 2019 Frantisek Sumsal <frantisek@sumsal.cz> - 4.9-3
- Fix dmenu crash in XmbLookupString() (BZ#1748043, BZ#1737739, BZ#1729601, BZ#1696199)
- Fix a focus issue in i3 (BZ#1695473)

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 06 2019 Petr Šabata <contyk@redhat.com> - 4.9-1
- 4.9 bump

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 09 2018 Petr Šabata <contyk@redhat.com> - 4.8-1
- 4.8 bump

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 03 2017 Petr Šabata <contyk@redhat.com> - 4.7-1
- 4.7 bump

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Petr Šabata <contyk@redhat.com> - 4.6-1
- 4.6 bump
- This release uses Xft for font rendering
- Dropping the ancient lsx provides/obsoletes

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5-8.20140425git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5-7.20140425git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5-6.20140425git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 25 2014 Christopher Meng <rpm@cicku.me> - 4.5-5.20140425git
- Fetch patches from upstream since 4.5 version.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jan 09 2012 Petr Šabata <contyk@redhat.com> - 4.5-1
- 4.5 bump
- Switching from lsx to stest

* Mon Sep 19 2011 Petr Sabata <contyk@redhat.com> - 4.4.1-1
- 4.4.1 bump

* Tue Aug 02 2011 Simon Wesp <cassmodiah@fedoraproject.org> - 4.4-2
- Rebuild against newest dependencies

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 4.4-1
- 4.4 bump
- This version integrates lsx, adding proper obsoletes/provides

* Mon Jun 13 2011 Petr Sabata <contyk@redhat.com> - 4.3.1-2
- dmenu no longer uses sselp at runtime, removing sselp dependency

* Thu May 19 2011 Petr Sabata <psabata@redhat.com> - 4.3.1-1
- 4.3.1 bugfix update

* Thu May 19 2011 Petr Sabata <psabata@redhat.com> - 4.3-1
- 4.3 released today
- Buildroot and defattr cleanup
- Use macros in URL and Source
- Use RPM_OPT_FLAGS in config.mk patch

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Nov 20 2010 Simon Wesp <cassmodiah@fedoraproject.org> - 4.2.1-1
- New upstrem version

* Mon Jun 28 2010 Simon Wesp <cassmodiah@fedoraproject.org> - 4.1.1-1
- New upstrem version

* Sat Dec 12 2009 Simon Wesp <cassmodiah@fedoraproject.org> - 4.0-2
- merged with the spec-file of Jan Blazek

* Thu Oct 15 2009 Simon Wesp <cassmodiah@fedoraproject.org> - 4.0-1
- Initial Package Build
