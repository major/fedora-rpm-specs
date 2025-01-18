# For test builds, should be set to 0 for release builds.
%global alpha 0

Name:           flrig
Version:        2.0.05
Release:        5%{?dist}
Summary:        Transceiver control program

License:        GPL-3.0-or-later AND LGPL-3.0-or-later AND GPL-3.0-only
URL:            http://www.w1hkj.com/
%if %{alpha}
Source0:        http://www.w1hkj.com/alpha/%{name}/%{name}-%{version}.tar.gz
%else
Source0:        http://www.w1hkj.com/files/%{name}/%{name}-%{version}.tar.gz
%endif
Source100:      flrig.appdata.xml

Patch0:         flrig-headers.patch

BuildRequires:  gcc gcc-c++ make
BuildRequires:  fltk-devel >= 1.3.0
%if 0%{?rhel}
Provides:       bundled(xmlrpc)
%else
BuildRequires:  flxmlrpc-devel
%endif
BuildRequires:  desktop-file-utils
%if 0%{?fedora}
BuildRequires:  libappstream-glib
%endif
BuildRequires:  libudev-devel

# xdg-open is used in src/main.cxx
Requires:       xdg-utils



%description
Flrig is a transceiver control program designed to be used either stand alone or
as an adjunct to fldigi.  The supported transceivers all have some degree of
CAT.  The flrig user interface changes to accommodate the degree of CAT support
available for the transceiver in use. 


%prep
%autosetup -p1


%build
%if 0%{?fedora}
export CXXFLAGS="-std=c++17 $RPM_OPT_FLAGS"
%endif
%{?rhel:export LDFLAGS="-lfltk"}
%configure
%make_build


%install
%make_install

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%if 0%{?fedora}
mkdir -p %{buildroot}%{_datadir}/metainfo
install -pm 0644 %{SOURCE100} %{buildroot}%{_datadir}/metainfo/
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml
%endif


%files
%license COPYING
%doc AUTHORS ChangeLog README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.xpm
%{?fedora:%{_datadir}/metainfo/*.appdata.xml}


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.05-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.05-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.05-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.05-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Dec 31 2023 Richard Shaw <hobbes1069@gmail.com> - 2.0.05-1
- Update to 2.5.05.

* Fri Aug 25 2023 Richard Shaw <hobbes1069@gmail.com> - 2.0.03-1
- Update to 2.0.03.

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jul 08 2023 Richard Shaw <hobbes1069@gmail.com> - 2.0.02-1
- Update to 2.0.02.
- Update license format to SPDX identifier.

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Sep 06 2022 Richard Shaw <hobbes1069@gmail.com> - 1.4.7-1
- Update to 1.4.7.

* Thu Jul 28 2022 Richard Shaw <hobbes1069@gmail.com> - 1.4.6-1
- Update to 1.4.6.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Mar 26 2022 Richard Shaw <hobbes1069@gmail.com> - 1.4.5-1
- Update to 1.4.5.

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec 24 2021 Richard Shaw <hobbes1069@gmail.com> - 1.4.4-1
- Update to 1.4.4.

* Sun Nov 14 2021 Richard Shaw <hobbes1069@gmail.com> - 1.4.3-1
- Update to 1.4.3.

* Thu Aug 05 2021 Richard Shaw <hobbes1069@gmail.com> - 1.4.2-1
- Update to 1.4.2.

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jul 15 2021 Richard Shaw <hobbes1069@gmail.com> - 1.4.1-1
- Update to 1.4.1.

* Fri Jun 04 2021 Richard Shaw <hobbes1069@gmail.com> - 1.4.0-1
- Update to 1.4.0.

* Wed Feb 03 2021 Richard Shaw <hobbes1069@gmail.com> - 1.3.54-2
- Rebuild in hamlib side tag.

* Wed Feb 03 2021 Richard Shaw <hobbes1069@gmail.com> - 1.3.54-1
- Update to 1.3.54.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.53-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 10 2020 Richard Shaw <hobbes1069@gmail.com> - 1.3.53-1
- Update to 1.3.53.

* Mon Nov 30 2020 Richard Shaw <hobbes1069@gmail.com> - 1.3.52-1.1
- Rebuild with updates fixes patch.

* Fri Oct 30 2020 Richard Shaw <hobbes1069@gmail.com> - 1.3.52-1
- Update to 1.3.52.

* Tue Aug 18 2020 Jeff Law <law@redhat.com> - 1.3.51-3
- Force C++14 as this code is not C++17 ready

* Mon Jul 27 2020 Richard Shaw <hobbes1069@gmail.com> - 1.3.51-2
- Add patch for various fixes.

* Fri Jul 03 2020 Richard Shaw <hobbes1069@gmail.com> - 1.3.51-1
- Update to 1.3.51.

* Wed Apr 01 2020 Richard Shaw <hobbes1069@gmail.com> - 1.3.50-1
- Update to 1.3.50.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.49-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 13 2020 Richard Shaw <hobbes1069@gmail.com> - 1.3.49-1
- Update to 1.3.49.

* Sun Aug 18 2019 Richard Shaw <hobbes1069@gmail.com> - 1.3.48-1
- Update to 1.3.48.

* Tue Aug 06 2019 Richard Shaw <hobbes1069@gmail.com> - 1.3.47-1
- Update to 1.3.47.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.46-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 24 2019 Richard Shaw <hobbes1069@gmail.com> - 1.3.46-1
- Update to 1.3.46.

* Wed Jun 05 2019 Richard Shaw <hobbes1069@gmail.com> - 1.3.45-1
- Update to 1.3.45.

* Tue May 07 2019 Richard Shaw <hobbes1069@gmail.com> - 1.3.44-1
- Update to 1.3.44.

* Sun Apr 14 2019 Richard Shaw <hobbes1069@gmail.com> - 1.3.43-1
- Update to 1.3.43.

* Sat Feb 02 2019 Richard Shaw <hobbes1069@gmail.com> - 1.3.42-1
- Update to 1.3.42.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.41-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Dec 04 2018 Richard Shaw <hobbes1069@gmail.com> - 1.3.41-1
- Update to 1.3.41.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.39-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Richard Shaw <hobbes1069@gmail.com> - 1.3.39-1
- Update to 1.3.39.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.38-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 16 2018 Richard Shaw <hobbes1069@gmail.com> - 1.3.38-1
- Update to latest upstream release.

* Sun Dec 31 2017 Richard Shaw <hobbes1069@gmail.com> - 1.3.37-1
- Update to latest upstream release.

* Mon Nov 13 2017 Richard Shaw <hobbes1069@gmail.com> - 1.3.36-1
- Update to latest upstream release.

* Wed Sep 06 2017 Richard Shaw <hobbes1069@gmail.com> - 1.3.34-1
- Update to latest upstream release.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.33-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Sun Jul 30 2017 Florian Weimer <fweimer@redhat.com> - 1.3.33-3
- Rebuild with binutils fix for ppc64le (#1475636)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.33-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 24 2017 Richard Shaw <hobbes1069@gmail.com> - 1.3.33-1
- Update to latest upstream release.

* Sun Jul 09 2017 Richard Shaw <hobbes1069@gmail.com> - 1.3.32-1
- Update to latest upstream release.

* Tue Jun 06 2017 Richard Shaw <hobbes1069@gmail.com> - 1.3.31-1
- Update to latest upstream release

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sun Apr  2 2017 Richard Shaw <hobbes1069@gmail.com> - 1.3.30-1
- Update to latest upstream release.

* Wed Mar 29 2017 Richard Shaw <hobbes1069@gmail.com> - 1.3.29-1
- Update to latest upstream release.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 20 2017 Richard Shaw <hobbes1069@gmail.com> - 1.3.28-1
- Update to latest upstream release.

* Tue Nov 15 2016 Richard Shaw <hobbes1069@gmail.com> - 1.3.27-1
- Update to latest upstream release.

* Mon Jun 27 2016 Richard Shaw <hobbes1069@gmail.com> - 1.3.26-1
- Update to latest upstream release.

* Tue Apr 12 2016 Richard Shaw <hobbes1069@gmail.com> - 1.3.25-1
- Update to latest upstream release.

* Wed Feb 17 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.3.24-3
- Rename "ignore" into flrig_ignore to work-around symbol clash with std::ignore
  (F24FTBS, RHBZ#1307507)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 22 2016 Richard Shaw <hobbes1069@gmail.com> - 1.3.24-1
- Update to latest upstream release.

* Mon Nov 30 2015 Richard Shaw <hobbes1069@gmail.com> - 1.3.23-1
- Update to latest upstream release.

* Tue May  5 2015 Richard Shaw <hobbes1069@gmail.com> - 1.3.22-1
- Update to latest upstream release.
- Build with external xmlrpc library.
- Update spec to use license macro where appropriate.

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.3.21-2
- Rebuilt for GCC 5 C++11 ABI change

* Fri Mar 27 2015 Richard Shaw <hobbes1069@gmail.com> - 1.3.21-1
- Update to latest upstream release.

* Sun Mar 22 2015 Richard Shaw <hobbes1069@gmail.com> - 1.3.20-1
- Update to latest upstream release.

* Thu Feb 19 2015 Rex Dieter <rdieter@fedoraproject.org> 1.3.19-2
- rebuild (fltk)

* Fri Dec 26 2014 Richard Shaw <hobbes1069@gmail.com> - 1.3.19-1
- Update to latest upstream release.

* Sun Dec 07 2014 Richard Shaw <hobbes1069@gmail.com> - 1.3.18-1
- Update to latest upstream release.

* Thu Oct 16 2014 Richard Shaw <hobbes1069@gmail.com> - 1.3.17-1
- Update to latest upstream release.

* Thu Aug  7 2014 Richard Shaw <hobbes1069@gmail.com> - 1.3.16-2
- Add xdg-open to package requirements.

* Sun Jun  8 2014 Richard Shaw <hobbes1069@gmail.com> - 1.3.16-1
- Update to latest upstream release.

* Sun Feb  2 2014 Richard Shaw <hobbes1069@gmail.com> - 1.3.15-1
- Initial packaging.
