Name:     FAudio
Version:  23.07
Release:  7%{?dist}
Summary:  FNA is a reimplementation of the Microsoft XNA Game Studio 4.0 Refresh libraries

License:  zlib
URL:      https://fna-xna.github.io/
Source0:  https://github.com/FNA-XNA/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: make

BuildRequires: SDL2-devel >= 2.24

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-SDL2 >= 2.24

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-SDL2 >= 2.24

%description
This is FAudio, an XAudio reimplementation that focuses solely on developing
fully accurate DirectX Audio runtime libraries for the FNA project, including
XAudio2, X3DAudio, XAPO, and XACT3.


%package -n libFAudio
Summary:  %{summary}


%description -n libFAudio
This is FAudio, an XAudio reimplementation that focuses solely on developing
fully accurate DirectX Audio runtime libraries for the FNA project, including
XAudio2, X3DAudio, XAPO, and XACT3.


%package -n libFAudio-devel
Summary:  Development files for the FAudio library
Requires: libFAudio%{?_isa} = %{version}-%{release}


%description -n libFAudio-devel
Development files for the FAudio library.


%package -n mingw32-%{name}
Summary:        %{summary}
BuildArch:      noarch


%description -n mingw32-%{name}
%{summary}.


%package -n mingw64-%{name}
Summary:        %{summary}
BuildArch:      noarch


%description -n mingw64-%{name}
%{summary}.


%{?mingw_debug_package}


%prep
%autosetup -p1
mkdir ../mingw-build
cp -rp . ../mingw-build


%build
%cmake
%cmake_build

pushd ../mingw-build
%mingw_cmake
%mingw_make %{?_smp_mflags}
popd


%install
%cmake_install

pushd ../mingw-build
%mingw_make_install
%mingw_debug_install_post
popd


%files -n libFAudio
%license LICENSE
%doc README
%{_libdir}/libFAudio.so.0*


%files -n libFAudio-devel
%{_libdir}/libFAudio.so
%{_libdir}/cmake/FAudio/
%{_libdir}/pkgconfig/FAudio.pc
%{_includedir}/F3DAudio.h
%{_includedir}/FACT.h
%{_includedir}/FACT3D.h
%{_includedir}/FAPO.h
%{_includedir}/FAPOBase.h
%{_includedir}/FAPOFX.h
%{_includedir}/FAudio.h
%{_includedir}/FAudioFX.h


%files -n mingw32-%{name}
%license LICENSE
%{mingw32_bindir}/FAudio.dll
%{mingw32_includedir}/F3DAudio.h
%{mingw32_includedir}/FACT.h
%{mingw32_includedir}/FACT3D.h
%{mingw32_includedir}/FAPO.h
%{mingw32_includedir}/FAPOBase.h
%{mingw32_includedir}/FAPOFX.h
%{mingw32_includedir}/FAudio.h
%{mingw32_includedir}/FAudioFX.h
%{mingw32_libdir}/cmake/%{name}/
%{mingw32_libdir}/libFAudio.dll.a
%{mingw32_libdir}/pkgconfig/%{name}.pc


%files -n mingw64-%{name}
%license LICENSE
%{mingw64_bindir}/FAudio.dll
%{mingw64_includedir}/F3DAudio.h
%{mingw64_includedir}/FACT.h
%{mingw64_includedir}/FACT3D.h
%{mingw64_includedir}/FAPO.h
%{mingw64_includedir}/FAPOBase.h
%{mingw64_includedir}/FAPOFX.h
%{mingw64_includedir}/FAudio.h
%{mingw64_includedir}/FAudioFX.h
%{mingw64_libdir}/cmake/%{name}/
%{mingw64_libdir}/libFAudio.dll.a
%{mingw64_libdir}/pkgconfig/%{name}.pc


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 23.07-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 23.07-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 23.07-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 23.07-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 23.07-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 23.07-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 10 2023 Michael Cronenworth <mike@cchtml.com> - 23.07-1
- Update to 23.07

* Mon Apr 03 2023 Michael Cronenworth <mike@cchtml.com> - 23.04-1
- Update to 23.04

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 22.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec 02 2022 Michael Cronenworth <mike@cchtml.com> - 22.12-1
- Update to 22.12

* Mon Oct 24 2022 Michael Cronenworth <mike@cchtml.com> - 22.10-1
- Update to 22.10

* Sun Sep 04 2022 Michael Cronenworth <mike@cchtml.com> - 22.09.01-1
- Update to 22.09.01

* Thu Sep 01 2022 Michael Cronenworth <mike@cchtml.com> - 22.09-1
- Update to 22.09

* Thu Aug 25 2022 Michael Cronenworth <mike@cchtml.com> - 22.08-2
- Include MinGW debuginfo packages

* Mon Aug 22 2022 Michael Cronenworth <mike@cchtml.com> - 22.08-1
- Update to 22.08
- Initial MinGW package

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 22.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 11 2022 Michael Cronenworth <mike@cchtml.com> - 22.03-1
- Update to 22.03

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 21.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Nov 10 2021 Michael Cronenworth <mike@cchtml.com> - 21.11-2
- Remove GStreamer

* Wed Nov 10 2021 Michael Cronenworth <mike@cchtml.com> - 21.11-1
- Update to 21.11

* Tue Sep 07 2021 Michael Cronenworth <mike@cchtml.com> - 21.09-1
- Update to 21.09

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 21.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 03 2021 Michael Cronenworth <mike@cchtml.com> - 21.06-1
- Update to 21.06

* Sat Mar 06 2021 Michael Cronenworth <mike@cchtml.com> - 21.03.05-1
- Update to 21.03.05

* Mon Mar 01 2021 Michael Cronenworth <mike@cchtml.com> - 21.03-1
- Update to 21.03

* Sun Feb 07 2021 Michael Cronenworth <mike@cchtml.com> - 21.02-1
- Update to 21.02

* Fri Jan 29 2021 Michael Cronenworth <mike@cchtml.com> - 21.01-1
- Update to 21.01

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 01 2020 Michael Cronenworth <mike@cchtml.com> - 20.12-1
- Update to 20.12

* Fri Oct 02 2020 Michael Cronenworth <mike@cchtml.com> - 20.10-1
- Update to 20.10

* Wed Sep 02 2020 Michael Cronenworth <mike@cchtml.com> - 20.09-1
- Update to 20.09

* Mon Aug 03 2020 Michael Cronenworth <mike@cchtml.com> - 20.08-1
- Update to 20.08
- Enable GStreamer backend

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20.07-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 15 2020 Michael Cronenworth <mike@cchtml.com> - 20.07-1
- Update to 20.07

* Mon Jun 01 2020 Michael Cronenworth <mike@cchtml.com> - 20.06-1
- Update to 20.06

* Thu Apr 02 2020 Michael Cronenworth <mike@cchtml.com> - 20.04-1
- Update to 20.04

* Mon Mar 02 2020 Michael Cronenworth <mike@cchtml.com> - 20.03-1
- Update to 20.03

* Mon Feb 03 2020 Michael Cronenworth <mike@cchtml.com> - 20.02-1
- Update to 20.02

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20.01-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 06 2020 Michael Cronenworth <mike@cchtml.com> - 20.01-1
- Update to 20.01

* Mon Dec 02 2019 Michael Cronenworth <mike@cchtml.com> - 19.12-1
- Update to 19.12

* Sat Nov 02 2019 Michael Cronenworth <mike@cchtml.com> - 19.11-1
- Update to 19.11

* Fri Sep 13 2019 Michael Cronenworth <mike@cchtml.com> - 19.09-1
- Update to 19.09

* Sun Aug 04 2019 Michael Cronenworth <mike@cchtml.com> - 19.08-1
- Update to 19.08

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 19.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 01 2019 Michael Cronenworth <mike@cchtml.com> - 19.03-1
- Update to 19.03

* Thu Feb 28 2019 Michael Cronenworth <mike@cchtml.com> - 19.02-1
- Initial spec file.

