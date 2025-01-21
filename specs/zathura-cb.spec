Name:             zathura-cb
Version:          0.1.10
Release:          11%{?dist}
Summary:          Comic book support for zathura
License:          Zlib
URL:              https://pwmt.org/projects/%{name}
Source0:          https://pwmt.org/projects/%{name}/download/%{name}-%{version}.tar.xz

#BuildRequires:    binutils
BuildRequires:    cairo-devel
# Needed to validate the desktop file
BuildRequires:    desktop-file-utils
BuildRequires:    gcc
BuildRequires:    girara-devel
# Needed to validate appdata
BuildRequires:    libappstream-glib
BuildRequires:    libarchive-devel
BuildRequires:    meson >= 0.43
BuildRequires:    zathura-devel >= 0.3.8

Requires:         zathura >= 0.3.8

%description
The zathura-cb plugin adds comic book archive support to zathura.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.metainfo.xml

%files
%license LICENSE
%doc AUTHORS
%{_libdir}/zathura/libcb.so
%{_datadir}/applications/org.pwmt.zathura-cb.desktop
%{_datadir}/metainfo/org.pwmt.zathura-cb.metainfo.xml


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Dec 23 2024 Ankur Sinha <sanjay.ankur@gmail.com> - 0.1.10-10
- Rebuild for girara 0.4.5, mupdf 1.25.2

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri May 10 2024 Michael J Gruber <mjg@fedoraproject.org> - 0.1.10-8
- Rebuild against zathura 0.5.6

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Dec 09 2023 Michael J Gruber <mjg@fedoraproject.org> - 0.1.10-6
- Rebuild against zathura 0.5.4

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 10 2023 Ankur Sinha <sanjay.ankur@gmail.com> - 0.1.10-3
- re-rebuild for zathura 0.5.2

* Sun Dec 11 2022 Alain Vigne <avigne@fedoraproject.org> - 0.1.10-2
- Rebuilt for zathura 0.5.2

* Sun Aug 28 2022 Alain Vigne <avigne@fedoraproject.org> - 0.1.10-1
- 0.1.10 bump
- Update URLs and SPDX license

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 10 2018 Petr Šabata <contyk@redhat.com> - 0.1.8-1
- 0.1.8 bump

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 15 2017 Petr Šabata <contyk@redhat.com> - 0.1.6-1
- 0.1.6 bump

* Fri Feb 26 2016 Petr Šabata <contyk@redhat.com> - 0.1.5-2
- Correct build dependencies

* Fri Feb 26 2016 Petr Šabata <contyk@redhat.com> - 0.1.5-1
- 0.1.5 bump

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jul 02 2015 Petr Šabata <contyk@redhat.com> - 0.1.4-5
- Install the desktop file again

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Petr Šabata <contyk@redhat.com> - 0.1.4-3
- Rebuild for new girara

* Tue Jun 09 2015 Petr Šabata <contyk@redhat.com> - 0.1.4-2
- Fix the dep list, install LICENSE with the %%license macro

* Wed Nov 12 2014 Petr Šabata <contyk@redhat.com> - 0.1.4-1
- 0.1.4 bugfix bump

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 23 2014 François Cami <fcami@fedoraproject.org> - 0.1.2-3
- Fix BuildRequires list.

* Tue Apr 22 2014 François Cami <fcami@fedoraproject.org> - 0.1.2-2
- Remove desktop file.

* Wed Mar 05 2014 François Cami <fcami@fedoraproject.org> - 0.1.2-1
- Initial package.
