Name:             zathura-pdf-poppler
Version:          0.3.3
Release:          2%{?dist}
Summary:          PDF support for zathura via poppler
License:          Zlib
URL:              http://pwmt.org/projects/%{name}
Source0:          http://pwmt.org/projects/%{name}/download/%{name}-%{version}.tar.xz

#BuildRequires:    binutils
# Needed to validate the desktop file
BuildRequires:    desktop-file-utils
BuildRequires:    gcc
BuildRequires:    girara-devel
BuildRequires:    glib2-devel
# Needed to validate appdata
BuildRequires:    libappstream-glib
BuildRequires:    meson >= 0.61
BuildRequires:    poppler-glib-devel >= 21.12
BuildRequires:    zathura-devel >= 0.5.3

Requires:         zathura >= 0.5.3
# Old plugins used alternatives
Conflicts:        zathura-pdf-mupdf < 0.3.3

%description
The zathura-pdf-poppler plugin adds PDF support to zathura by using
the poppler rendering engine.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.metainfo.xml

# Clean the old alternatives link
%pre
[ -L %{_libdir}/zathura/pdf.so ] || rm -f %{_libdir}/zathura/pdf.so

%files
%license LICENSE
%doc AUTHORS
%{_libdir}/zathura/libpdf-poppler.so
%{_datadir}/applications/org.pwmt.zathura-pdf-poppler.desktop
%{_datadir}/metainfo/org.pwmt.zathura-pdf-poppler.metainfo.xml

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Aug 04 2024 Michael J Gruber <mjg@fedoraproject.org> - 0.3.3-1
- Update to 0.3.3

* Mon Dec 23 2024 Ankur Sinha <sanjay.ankur@gmail.com> - 0.3.2-5
- Rebuild for girara 0.4.5, mupdf 1.25.2

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri May 10 2024 Michael J Gruber <mjg@fedoraproject.org> - 0.3.2-3
- Rebuild against zathura 0.5.6

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 02 2024 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.3.2-1
- Update dep versions

* Sat Dec 09 2023 Michael J Gruber <mjg@fedoraproject.org> - 0.3.2-1
- Update to 0.3.2

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Dec 11 2022 Alain Vigne <avigne@fedoraproject.org> - 0.3.1-1
- Update to 0.3.1
- SPDX license identifier

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr 15 2020 Petr Šabata <contyk@redhat.com> - 0.3.0-1
- 0.3.0 bump

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 10 2018 Petr Šabata <contyk@redhat.com> - 0.2.9-1
- 0.2.9 bump

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Apr 04 2017 Petr Šabata <contyk@redhat.com> - 0.2.7-1
- 0.2.7 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 26 2016 Petr Šabata <contyk@redhat.com> - 0.2.6-1
- 0.2.6 bump

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jul 02 2015 Petr Šabata <contyk@redhat.com> - 0.2.5-8
- Install the desktop file correctly
- Don't package LICENSE twice

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Petr Šabata <contyk@redhat.com> - 0.2.5-6
- Rebuild for new girara

* Tue Jun 09 2015 Petr Šabata <contyk@redhat.com> - 0.2.5-5
- Fix the dep list, install LICENSE with the %%license macro
- Add support for alternatives

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar 06 2014 François Cami <fcami@fedoraproject.org> - 0.2.5-2
- Bump for rawhide

* Wed Mar 05 2014 François Cami <fcami@fedoraproject.org> - 0.2.5-1
- Update to 0.2.5

* Sat Dec 28 2013 François Cami <fcami@fedoraproject.org> - 0.2.4-1
- Update to latest upstream.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed May 29 2013 Petr Šabata <contyk@redhat.com> - 0.2.3-2
- Fix a debuginfo regression (#967954)

* Tue May 21 2013 Petr Šabata <contyk@redhat.com> - 0.2.3-1
- 0.2.3 bump

* Fri Mar 29 2013 Kevin Fenzi <kevin@scrye.com> 0.2.2-1
- Update to 0.2.2

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jan 12 2013 François Cami <fcami@fedoraproject.org> - 0.2.1-5
- force-require zathura.

* Sun Dec 02 2012 François Cami <fcami@fedoraproject.org> - 0.2.1-4
- really remove pre-EL6 stuff.

* Sun Dec 02 2012 François Cami <fcami@fedoraproject.org> - 0.2.1-3
- switch to using RPM_BUILD_ROOT exclusively.
- remove pre-EL6 stuff.

* Wed Nov 28 2012 François Cami <fcami@fedoraproject.org> - 0.2.1-2
- fix BR. Thanks to Dennis Johnson.

* Wed Nov 28 2012 François Cami <fcami@fedoraproject.org> - 0.2.1-1
- new upstream

* Sun Aug 19 2012 François Cami <fcami@fedoraproject.org> - 0.2.0-2
- minor build fixes.

* Fri Aug 10 2012 François Cami <fcami@fedoraproject.org> - 0.2.0-1
- Initial package.

