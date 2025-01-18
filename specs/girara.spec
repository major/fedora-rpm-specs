Name:               girara
Version:            0.4.5
Release:            2%{?dist}
Summary:            Simple user interface library
License:            Zlib
URL:                https://pwmt.org/projects/%{name}/
Source0:            https://pwmt.org/projects/%{name}/download/%{name}-%{version}.tar.xz

#BuildRequires:      binutils
BuildRequires:      gcc
BuildRequires:      gettext
BuildRequires:      glib2-devel >= 2.72
BuildRequires:      gtk3-devel >= 3.24
BuildRequires:      intltool
BuildRequires:      meson >= 0.61
BuildRequires:      pango-devel >= 1.50
BuildRequires:      pkgconfig(json-glib-1.0)
# Tests
BuildRequires:      pkgconfig(check) >= 0.11
Buildrequires:      xorg-x11-server-Xvfb

# from Upstream: Mark girara_libnotify as deprecated
#BuildRequires:      libnotify-devel >= 0.7.0


%global girara_locales  lib%{name}-gtk3-4

%description
Girara is a library that implements a user interface that focuses on simplicity
and minimalism.

%package      devel
Summary:            Development files for %{name}
Requires:           %{name}%{?_isa} = %{version}-%{release}

%description  devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q

%build
%meson -Ddocs=disabled -Dtests=enabled
%meson_build

%install
%meson_install
%find_lang %{girara_locales}

%check
%meson_test


%files -f %{girara_locales}.lang
%license LICENSE
%doc AUTHORS README.md
%{_libdir}/libgirara-gtk3.so.4
%{_libdir}/libgirara-gtk3.so.4.0

%files devel
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%{_libdir}/pkgconfig/girara-gtk3.pc
%{_libdir}/libgirara-gtk3.so


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Dec 18 2024 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.4.5-1
- Update to 0.4.5 (fixes rhbz#2331281)
- version sonames in files

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed May 29 2024 Michael J Gruber <mjg@fedoraproject.org> - 0.4.4-2
- Rebuild for RPM 4.20 regression

* Thu May 09 2024 Michael J Gruber <mjg@fedoraproject.org> - 0.4.4-1
- feat: update to 0.4.4 (rhbz#2258262)

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Dec 08 2023 Michael J Gruber <mjg@fedoraproject.org> - 0.4.1-1
- feat: update to 0.4.1 (rhbz#2253671)

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 22 2023 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.4.0-1
- Update to 0.4.0

* Mon Jan 30 2023 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.3.9-1
- Update to 0.3.9
- https://pwmt.org/projects/girara/changelog/0.3.9/index.html

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec 02 2022 Alain Vigne <avigne@fedoraproject.org> - 0.3.8-2
- Re-enable tests

* Tue Nov 29 2022 Alain Vigne <avigne@fedoraproject.org> - 0.3.8-1
- 0.3.8 bump (rhbz#2148740)
- Switch to json-glib, where available
- Disable notify
- Tests are disabled
- SPDX license identifier

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Feb 15 2022 Alain Vigne <avigne@fedoraproject.org> - 0.3.7-1
- 0.3.7 bump
- Drop BR:doxygen as documentation is not generated nor installed

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Sep 16 2021 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.3.6-1
- Update to 0.3.6

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 10 2021 Björn Esser <besser82@fedoraproject.org> - 0.3.5-3
- Rebuild for versioned symbols in json-c

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Oct 31 2020 Petr Šabata <contyk@redhat.com> - 0.3.5-1
- 0.3.5 bump

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Apr 21 2020 Björn Esser <besser82@fedoraproject.org> - 0.3.4-2
- Rebuild (json-c)

* Wed Apr 15 2020 Petr Šabata <contyk@redhat.com> - 0.3.4-1
- 0.3.4 bump

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Petr Šabata <contyk@redhat.com> - 0.3.2-1
- 0.3.2 bump
- Enabling libnotify support
- Based on Ankur Sinha's PR, https://src.fedoraproject.org/rpms/girara/pull-request/1

* Fri Nov 16 2018 Petr Šabata <contyk@redhat.com> - 0.3.1-1
- 0.3.1 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri May 25 2018 Petr Šabata <contyk@redhat.com> - 0.3.0-1
- 0.3.0 bump

* Tue Apr 10 2018 Petr Šabata <contyk@redhat.com> - 0.2.9-1
- 0.2.9 bump
- Upstream switches to meson
- Dropping the ldconfig scriptlets as this is aimed at F28+

* Tue Mar 06 2018 Björn Esser <besser82@fedoraproject.org> - 0.2.7-7
- Rebuilt for libjson-c.so.4 (json-c v0.13.1)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 10 2017 Björn Esser <besser82@fedoraproject.org> - 0.2.7-5
- Rebuilt for libjson-c.so.3

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 15 2017 Petr Šabata <contyk@redhat.com> - 0.2.7-1
- 0.2.7 bump

* Tue Apr 19 2016 Petr Šabata <contyk@redhat.com> - 0.2.6-1
- 0.2.6 bump

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 21 2015 Petr Šabata <contyk@redhat.com> - 0.2.5-1
- 0.2.5 bump

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 09 2015 Petr Šabata <contyk@redhat.com> - 0.2.4-1
- 0.2.4 bump, soname changed to 2.0
- Fix the dep list, install LICENSE with the %%license macro

* Fri Oct 31 2014 Petr Šabata <contyk@redhat.com> - 0.2.3-2
- Release bump for the f21 override; needed for zathura 0.3.1
  The update previous update is blocked by f21 freeze and the override
  cannot be reenabled

* Fri Oct 17 2014 Petr Šabata <contyk@redhat.com> - 0.2.3-1
- 0.2.3 bump

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 26 2014 Petr Šabata <contyk@redhat.com> - 0.2.2-1
- 0.2.2 bump
- Introduce libnotify support

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Mar 23 2014 François Cami <fcami@fedoraproject.org> - 0.2.0-2
- Gratuitous release bump.

* Wed Mar 05 2014 François Cami <fcami@fedoraproject.org> - 0.2.0-1
- Update to 0.2.0 and switch to gtk3.

* Sat Dec 28 2013 François Cami <fcami@fedoraproject.org> - 0.1.9-1
- Update to latest upstream.
- Enforce building against gtk2 for now.

* Sat Aug 31 2013 François Cami <fcami@fedoraproject.org> - 0.1.7-1
- Update to latest upstream.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed May 29 2013 Petr Šabata <contyk@redhat.com> - 0.1.6-2
- Revision bump for f19 updates

* Tue May 21 2013 Petr Šabata <contyk@redhat.com> - 0.1.6-1
- 0.1.6 bump, 1.1 soname bump
- Fix bogus dates in changelog
- Use more macros

* Fri Feb 22 2013 Kevin Fenzi <kevin@scrye.com> 0.1.5-1
- Update to 0.1.5

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 27 2012 François Cami <fcami@fedoraproject.org> - 0.1.4-2
- remove static library [863049]

* Mon Nov 05 2012 Kevin Fenzi <kevin@scrye.com> 0.1.4-1
- Update to 0.1.4

* Tue Aug 21 2012 François Cami <fcami@fedoraproject.org> - 0.1.3-6
- really remove EL5-specific stuff (thanks to Mario B)

* Tue Aug 21 2012 François Cami <fcami@fedoraproject.org> - 0.1.3-5
- make -devel really depend on base package. (thanks to Mario B).
- remove el5 compatibility.

* Sun Aug 19 2012 François Cami <fcami@fedoraproject.org> - 0.1.3-4
- remove LICENSE from -devel; fix debuginfo (thanks to Mario B).

* Sun Aug 12 2012 François Cami <fcami@fedoraproject.org> - 0.1.3-3
- BuildRequires fixes suggested by Dennis Johnson.

* Sat Aug 11 2012 François Cami <fcami@fedoraproject.org> - 0.1.3-2
- fixes suggested by Mario Blättermann.

* Fri Aug 10 2012 François Cami <fcami@fedoraproject.org> - 0.1.3-1
- initial package, needed for zathura.

