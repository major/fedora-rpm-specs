# For test builds, should be set to 0 for release builds.
%global alpha 0

Name:           flmsg
Version:        4.0.23
Release:        5%{?dist}
Summary:        Fast Light Message Amateur Radio Forms Manager

# Embedded mongoose is GPLv2
License:        GPL-3.0-or-later AND GPL-2.0-only
URL:            http://www.w1hkj.com/
%if %{alpha}
Source0:        http://www.w1hkj.com/alpha/%{name}/%{name}-%{version}.tar.gz
%else
Source0:        http://www.w1hkj.com/files/%{name}/%{name}-%{version}.tar.gz
%endif
Source100:      flmsg.appdata.xml

BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++ make
BuildRequires:  fltk-devel >= 1.3.0
%if 0%{?fedora}
BuildRequires:  flxmlrpc-devel >= 1.0
BuildRequires:  libappstream-glib
%endif

# While mongoose does make official releases, it is also designed as a copylib
# The copy in flmsg is heavily modified and will not work with any upstream 
# version.
# https://github.com/cesanta/mongoose
Provides:       bundled(mongoose)


%description
flmsg is a editor / file management tool for ics213 forms which form the
basis for emergency communications data transfers.


%prep
%autosetup -p1

%if 0%{?fedora}
# Remove bundled xmlrpc library.
rm -rf src/xmlrpcpp
%endif


%build
%configure
%make_build


%install
%make_install

%if 0%{?fedora}
mkdir -p %{buildroot}%{_datadir}/metainfo
install -pm 0644 %{SOURCE100} %{buildroot}%{_datadir}/metainfo/
%endif


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
%if 0%{?fedora}
appstream-util validate-relax --nonet \
    %{buildroot}%{_datadir}/metainfo/*.appdata.xml
%endif


%files
%license COPYING
%doc README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{?fedora:%{_datadir}/metainfo/*.xml}
%{_datadir}/pixmaps/%{name}.xpm


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.23-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.23-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Sep 28 2023 Richard Shaw <hobbes1069@gmail.com> - 4.0.23-1
- Update to 4.0.23.

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jun 25 2023 Richard Shaw <hobbes1069@gmail.com> - 4.0.22-1
- Update to 2.0.22.
- Update license tag to SPDX format.

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Richard Shaw <hobbes1069@gmail.com> - 4.0.20-1
- Update to 4.0.20.

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Aug 05 2021 Richard Shaw <hobbes1069@gmail.com> - 4.0.19-1
- Update to 4.0.19.

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct 07 2020 Richard Shaw <hobbes1069@gmail.com> - 4.0.17-1
- Update to 4.0.17.

* Tue Aug 18 2020 Jeff Law <law@redhat.com> - 4.0.16-4
- Force C++14 as this code is not C++17 ready

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Richard Shaw <hobbes1069@gmail.com> - 4.0.16-2
- Add patch for various memory leaks and one segfault.

* Fri Jun 26 2020 Richard Shaw <hobbes1069@gmail.com> - 4.0.16-1
- Update to 4.0.16.

* Mon Jun 01 2020 Richard Shaw <hobbes1069@gmail.com> - 4.0.14-1
- Update to 4.0.15.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 31 2019 Richard Shaw <hobbes1069@gmail.com> - 4.0.14-1
- Update to 4.0.14.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 24 2019 Richard Shaw <hobbes1069@gmail.com> - 4.0.11-1
- Update to 4.0.11.

* Sun Jun 30 2019 Richard Shaw <hobbes1069@gmail.com> - 4.0.10-1
- Update to 4.0.10.

* Thu Jan 31 2019 Richard Shaw <hobbes1069@gmail.com> - 4.0.8-1
- Update to 4.0.8.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Richard Shaw <hobbes1069@gmail.com> - 4.0.7-1
- Update to 4.0.7.

* Mon Mar 19 2018 Richard Shaw <hobbes1069@gmail.com> - 4.0.6-1
- Update to 4.0.6.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 17 2018 Richard Shaw <hobbes1069@gmail.com> - 4.0.5-1
- Update to latest upstream release.

* Wed Jan 10 2018 Richard Shaw <hobbes1069@gmail.com> - 4.0.4-1
- Update to latest upstream release.
- Add appdata file.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 24 2017 Richard Shaw <hobbes1069@gmail.com> - 4.0.3-1
- Update to latest upstream release.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov 15 2016 Richard Shaw <hobbes1069@gmail.com> - 4.0.0-1
- Update to latest upstream release.

* Mon Aug  8 2016 Richard Shaw <hobbes1069@gmail.com> - 3.00.02-1
- Update to latest upstream release.

* Mon Jun 27 2016 Richard Shaw <hobbes1069@gmail.com> - 3.00.01-1
- Update to latest upstream release.

* Wed Jun  8 2016 Richard Shaw <hobbes1069@gmail.com> - 3.00.00-1
- Update to latest upstream release.
- Update license tag to include GPLv2 (embedded mongoose server).

* Fri Apr  1 2016 Richard Shaw <hobbes1069@gmail.com> - 2.0.17-1
- Update to latest upstream release.

* Mon Jan  4 2016 Richard Shaw <hobbes1069@gmail.com> - 2.0.14-1
- Update to latest upstream release.

* Mon Dec 28 2015 Richard Shaw <hobbes1069@gmail.com> - 2.0.13-1
- Update to latest upstream release.

* Fri Oct  9 2015 Richard Shaw <hobbes1069@gmail.com> - 2.0.12-2
- Add virtual provides and comments for the bundled mongoose library.

* Sun Jul 26 2015 Richard Shaw <hobbes1069@gmail.com> - 2.0.12-1
- Update to latest upstream release.

* Tue May  5 2015 Richard Shaw <hobbes1069@gmail.com> - 2.0.10-1
- Update to latest upstream release.
- Build with external xmlrpc library.
- Use %%license macro where appropriate.

* Wed Mar 11 2015 Richard Shaw <hobbes1069@gmail.com> - 2.0.9-1
- Update to latest upstream release.

* Tue Jan 13 2015 Richard Shaw <hobbes1069@gmail.com> - 2.0.7-1
- Update to latest upstream release.

* Thu Oct 16 2014 Richard Shaw <hobbes1069@gmail.com> - 2.0.5-1
- Update to latest upstream release.

* Wed Mar  5 2014 Richard Shaw <hobbes1069@gmail.com> - 2.0.3-1
- Initial packaging.
