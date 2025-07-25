Name:           libzen
Version:        0.4.41
Release:        7%{?dist}
Summary:        Shared library for libmediainfo and medianfo*

License:        Zlib
URL:            https://github.com/MediaArea/ZenLib
Source0:        https://mediaarea.net/download/source/%{name}/%{version}/%{name}_%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  doxygen
BuildRequires:  cmake3
BuildRequires:  pkgconfig(zlib)

%description
Files shared library for libmediainfo and medianfo-*.

%package        doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description    doc
Documentation files.

%package        devel
Summary:        Include files and mandatory libraries for development
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Include files and mandatory libraries for development.

%prep
%autosetup -n ZenLib

#Correct documentation encoding and permissions
sed -i 's/.$//' *.txt
chmod 644 *.txt Source/Doc/Documentation.html

chmod 644 Source/ZenLib/*.h Source/ZenLib/*.cpp \
    Source/ZenLib/Format/Html/*.h Source/ZenLib/Format/Html/*.cpp \
    Source/ZenLib/Format/Http/*.h Source/ZenLib/Format/Http/*.cpp

%build
#Make documentation
pushd Source/Doc/
    doxygen -u Doxyfile
    doxygen Doxyfile
popd
cp Source/Doc/*.html ./

pushd Project/CMake
    %cmake3
    %cmake3_build
popd

%install
pushd Project/CMake
    %cmake3_install
popd

%files
%doc History.txt ReadMe.txt
%license License.txt
%{_libdir}/%{name}.so.*

%files doc
%doc Documentation.html
%doc Doc

%files devel
%{_includedir}/ZenLib
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/cmake/zenlib/


%changelog
* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.41-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.41-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.41-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.41-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.41-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.41-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Apr 17 2023 Vasiliy N. Glazov <vascom2@gmail.com> - 0.4.41-1
- Update to 0.4.41

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.40-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec 23 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 0.4.40-1
- Update to 0.4.40

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.39-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.39-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.39-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Mar 28 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 0.4.39-1
- Update to 0.4.39

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.38-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.38-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.38-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Apr 03 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 0.4.38-1
- Update to 0.4.38

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.37-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.37-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.37-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.37-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.37-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Sep 13 2017 Vasiliy N. Glazov <vascom2@gmail.com> - 0.4.37-1
- Update to 0.4.37

* Mon Aug 14 2017 Vasiliy N. Glazov <vascom2@gmail.com> - 0.4.36-1
- Update to 0.4.36

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.35-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.35-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Apr 06 2017 Vasiliy N. Glazov <vascom2@gmail.com> - 0.4.35-1
- Update to 0.4.35

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.34-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 05 2016 Vasiliy N. Glazov <vascom2@gmail.com> - 0.4.34-1
- Update to 0.4.34

* Wed Mar 02 2016 Vasiliy N. Glazov <vascom2@gmail.com> - 0.4.33-1
- Update to 0.4.33

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec 03 2015 Vasiliy N. Glazov <vascom2@gmail.com> - 0.4.32-1
- Update to 0.4.32

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.31-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 22 2015 Vasiliy N. Glazov <vascom2@gmail.com> - 0.4.31-2
- Correct lib version

* Thu Apr 09 2015 Vasiliy N. Glazov <vascom2@gmail.com> - 0.4.31-1
- update to 0.4.31

* Thu Jan 15 2015 Ivan Romanov <drizt@land.ru> - 0.4.30-4
- added patch to fix building MediaInfo

* Tue Dec 16 2014 Vasiliy N. Glazov <vascom2@gmail.com> 0.4.30-3
- Add BR pkgconfig(zlib)

* Sun Dec  7 2014 Ivan Romanov <drizt@land.ru> - 0.4.30-2
- use cmake

* Wed Nov 12 2014 Vasiliy N. Glazov <vascom2@gmail.com> 0.4.30-1
- update to 0.4.30

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.29-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Vasiliy N. Glazov <vascom2@gmail.com> 0.4.29-3
- Remove conflicted libzen-config from devel subpackage

* Fri Aug 02 2013 Vasiliy N. Glazov <vascom2@gmail.com> 0.4.29-2
- Corrected build flags
- Use more macros

* Fri May 31 2013 Vasiliy N. Glazov <vascom2@gmail.com> 0.4.29-1
- update to 0.4.29

* Tue Apr 23 2013 Vasiliy N. Glazov <vascom2@gmail.com> 0.4.28-7
- Corrected shebang
- Removed dos2unix from BR
- Correcting encoding for all files
- Corrected config and build

* Mon Apr 15 2013 Vasiliy N. Glazov <vascom2@gmail.com> 0.4.28-6
- Added doc subpackage
- Removed gcc-c++ from BR

* Mon Apr 08 2013 Vasiliy N. Glazov <vascom2@gmail.com> 0.4.28-5
- Corrected license
- Added comments
- Corrected make on smp

* Mon Apr 08 2013 Vasiliy N. Glazov <vascom2@gmail.com> 0.4.28-4
- Spec prepared for review again

* Mon Apr 08 2013 Vasiliy N. Glazov <vascom2@gmail.com> 0.4.28-3
- Spec prepared for review

* Mon Apr 08 2013 Vasiliy N. Glazov <vascom2@gmail.com> 0.4.28-2
- Clean spec

* Mon Sep 03 2012 Vasiliy N. Glazov <vascom2@gmail.com> 0.4.28-1
- Update to 0.4.28
- Drop patch

* Fri May 18 2012 Vasiliy N. Glazov <vascom2@gmail.com> 0.4.26-3
- Added libzen-config

* Thu May 17 2012 Vasiliy N. Glazov <vascom2@gmail.com> 0.4.26-2
- Corrected license
- removed *.a and *.la files

* Wed Apr 11 2012 Vasiliy N. Glazov <vascom2@gmail.com> 0.4.26-1
- Update to 0.4.26

* Tue Mar 20 2012 Vasiliy N. Glazov <vascom2@gmail.com> 0.4.25-1
- Update to 0.4.25

* Thu Feb 09 2012 Vasiliy N. Glazov <vascom2@gmail.com> 0.4.24-1
- Update to 0.4.24

* Tue Nov 22 2011 Vasiliy N. Glazov <vascom2@gmail.com> 0.4.23-2
- Added description in russian language

* Mon Nov 14 2011 Vasiliy N. Glazov <vascom2@gmail.com> 0.4.23-1
- Update to 0.4.23

* Tue Sep 27 2011 Vasiliy N. Glazov <vascom2@gmail.com> 0.4.22-1
- Update to 0.4.22

* Tue Aug 09 2011 Vasiliy N. Glazov <vascom2@gmail.com> 0.4.20-2
- Removed 0 from name

* Fri Aug 05 2011 Vasiliy N. Glazov <vascom2@gmail.com> 0.4.20-1
- Initial release
