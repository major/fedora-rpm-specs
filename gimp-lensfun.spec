Name:           gimp-lensfun
Version:        0.2.4
Release:        24%{?dist}
Summary:        Gimp plugin to correct lens distortion

License:        GPLv3+
URL:            http://seebk.github.io/GIMP-Lensfun/
Source0:        https://github.com/seebk/GIMP-Lensfun/archive/%{version}.tar.gz
Source1:        %{name}.metainfo.xml
Patch0:         %{name}-fix-exiv2-build-error.patch

BuildRequires:  gcc-c++
BuildRequires:  gimp-devel >= 2.0
BuildRequires:  exiv2-devel
BuildRequires:  lensfun-devel >= 0.3.2
BuildRequires: make


%description
GimpLensfun is a Gimp plugin to correct lens distortion using the lensfun
library and database.


%prep
%setup -q -n GIMP-Lensfun-%{version}
%patch0 -p1


%build
make %{?_smp_mflags} CXXFLAGS="%{optflags}"


%install
mkdir -p $RPM_BUILD_ROOT%{_libdir}/gimp/2.0/plug-ins
install -m 755 %{name} $RPM_BUILD_ROOT%{_libdir}/gimp/2.0/plug-ins
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/appdata


%files
%doc LICENSE.txt CHANGES.txt README.txt
%{_libdir}/gimp/2.0/plug-ins/%{name}
%{_datadir}/appdata/%{name}.metainfo.xml


%changelog
* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-16
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 01 2019 Graham White <graham_alton@hotmail.com> - 0.2.4-13
- Fix build error with exiv2

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Rex Dieter <rdieter@fedoraproject.org> - 0.2.4-10
- rebuild (exiv2)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 02 2017 Rex Dieter <rdieter@fedoraproject.org> - 0.2.4-5
- rebuild (exiv2)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Mar 11 2016 Graham White <graham_alton@hotmail.com> - 0.2.4-3
- Fix bug #1316721, thanks to Jiri Eischmann
- AppStream metadata file has been added to the package

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 11 2016 Graham White <graham_alton@hotmail.com> - 0.2.4-1
- new upstream release
- Lensfun version 0.3.2 is required
- basic support for non interactive mode
- avoid crash when camera or lens is not found in the database
- support for makers which are not in the pre-defined list

* Sun Jan 03 2016 Rex Dieter <rdieter@fedoraproject.org> 0.2.3-4
- rebuild (lensfun)

* Thu Jun 25 2015 Rex Dieter <rdieter@fedoraproject.org> 0.2.3-3
- rebuild (exiv2)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 16 2015 Graham White <graham_alton@hotmail.com> - 0.2.3-1
- rebuild for F22
- include upstream commit for newer lensfun patch
- clean up spec file for passing Fedora package review

* Thu May 23 2013 Graham White <graham_alton@hotmail.com> - 0.2.3-1
- version bump to 0.2.3
- add optflags macro to the build
- change URL and source to point to new web site

* Fri Feb 08 2013 Graham White <graham_alton@hotmail.com> - 0.2.2-1
- update version and build for F18

* Sat May 26 2012 Graham White <graham_alton@hotmail.com> - 0.2.1-1
- first build, for F17
