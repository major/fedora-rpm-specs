%global commit d810aac8676b9b4af0f4a1145bcfe9ac2a0b102e
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global snapdate 20241211

Name:		nextpnr
Version:	1
Release:	49.%{snapdate}git%{shortcommit}%{?dist}
Summary:	FPGA place and route tool

# Automatically converted from old format: ISC and BSD and MIT and (MIT or Public Domain) - review is highly recommended.
License:	ISC AND LicenseRef-Callaway-BSD AND LicenseRef-Callaway-MIT AND (LicenseRef-Callaway-MIT OR LicenseRef-Callaway-Public-Domain)
URL:		https://github.com/YosysHQ/nextpnr
Source0:	https://github.com/YosysHQ/nextpnr/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	make
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
BuildRequires:	libglvnd-devel
BuildRequires:	boost-filesystem
BuildRequires:	boost-thread
BuildRequires:	boost-program-options
BuildRequires:	boost-iostreams
BuildRequires:	qt5-qtconfiguration-devel
BuildRequires:	cmake(QtConfiguration)
BuildRequires:	boost-python3-devel
BuildRequires:	eigen3-devel
#BuildRequires:	pybind11-devel
# NOTE: remember to update icestorm & trellis before rebuilding nextpnr!!!
BuildRequires:	icestorm >= 0-0.36
BuildRequires:	trellis-devel >= 1.2.1-29

# License: ISC
Provides:	bundled(qtimgui)

# Qt5 enabled fork of QtPropertyBrowser
# License: BSD
Provides:	bundled(QtPropertyBrowser)

# License: MIT
Provides:	bundled(python-console)

# License: (MIT or Public Domain)
Provides:	bundled(imgui) = 1.66-wip


%description
nextpnr aims to be a vendor neutral, timing driven, FOSS FPGA place and
route tool.


%prep
%autosetup -p1 -n %{name}-%{commit}
cp 3rdparty/imgui/LICENSE.txt LICENSE-imgui.txt
cp 3rdparty/qtimgui/LICENSE LICENSE-qtimgui.txt
cp 3rdparty/python-console/LICENSE LICENSE-python-console.txt


%build
%cmake  -DARCH=all \
	-DICEBOX_DATADIR=%{_datadir}/icestorm \
	-DTRELLIS_LIBDIR=%{_libdir}/trellis \
	-DBUILD_GUI=ON \
	-DUSE_OPENMP=ON
#	-DPYBIND11_INCLUDE_DIR="/usr/include/pybind11/" \
%cmake_build
# prepare examples doc. directory:
mkdir -p examples/ice40
cp -r ice40/examples/* examples/ice40


%install
%cmake_install


%files
%{_bindir}/nextpnr-generic
%{_bindir}/nextpnr-ice40
%{_bindir}/nextpnr-ecp5
%doc README.md docs examples
%license COPYING
%license LICENSE-imgui.txt
%license LICENSE-qtimgui.txt
%license LICENSE-python-console.txt


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1-49.20241211gitd810aac
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Dec 11 2024 Gabriel Somlo <gsomlo@gmail.com> - 1-48.20241211gitd810aac
- Update to newer snapshot

* Fri Oct 11 2024 Gabriel Somlo <gsomlo@gmail.com> - 1-47.20241011gitcf42baa
- Update to newer snapshot

* Thu Sep 05 2024 Gabriel Somlo <gsomlo@gmail.com> - 1-46.20240905git4cf7afe
- Update to newer snapshot

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 1-45.20240808gite9e7dce
- convert license to SPDX

* Thu Aug 08 2024 Gabriel Somlo <gsomlo@gmail.com> - 1-44.20240808gite9e7dce
- Update to newer snapshot

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1-43.20240716giteb099a9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jul 16 2024 Gabriel Somlo <gsomlo@gmail.com> - 1-42.20240716giteb099a9
- Update to newer snapshot

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 1-41.20240524gitb7f91e5
- Rebuilt for Python 3.13

* Fri May 24 2024 Gabriel Somlo <gsomlo@gmail.com> - 1-40.20240524gitb7f91e5
- Update to newer snapshot

* Thu Apr 11 2024 Gabriel Somlo <gsomlo@gmail.com> - 1-39.20240411gitd3b53d8
- Update to newer snapshot

* Thu Mar 14 2024 Gabriel Somlo <gsomlo@gmail.com> - 1-38.20240314gitff96fc5
- Update to newer snapshot

* Sat Feb 10 2024 Gabriel Somlo <gsomlo@gmail.com> - 1-37.20240210gitcc273c1
- Update to newer snapshot

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1-36.20240118git4220ce1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1-35.20240118git4220ce1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Gabriel Somlo <gsomlo@gmail.com> - 1-34.20240118git4220ce1
- Update to newer snapshot

* Thu Jan 18 2024 Jonathan Wakely <jwakely@redhat.com> - 1-33.20240117git2afb1f6
- Rebuilt for Boost 1.83

* Wed Jan 17 2024 Gabriel Somlo <gsomlo@gmail.com> - 1-32.20240117git2afb1f6
- Update to newer snapshot

* Mon Dec 18 2023 Gabriel Somlo <gsomlo@gmail.com> - 1-31.20231218git535709a
- Update to newer snapshot
- fix Python 3.13 FTBFS (BZ #2250854)

* Wed Nov 08 2023 Gabriel Somlo <gsomlo@gmail.com> - 1-30.20231108git4c6003a
- Update to newer snapshot

* Fri Oct 06 2023 Gabriel Somlo <gsomlo@gmail.com> - 1-29.20231006git0eb9a9a
- Update to newer snapshot

* Tue Sep 12 2023 Gabriel Somlo <gsomlo@gmail.com> - 1-28.20230905git3e1e783
- Update to newer snapshot

* Sat Jul 29 2023 Gabriel Somlo <gsomlo@gmail.com> - 1-27.20230729git54b2045
- Update to newer snapshot

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1-26.20230607git119b47a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 1-25.20230607git119b47a
- Rebuilt for Python 3.12

* Wed Jun 07 2023 Gabriel Somlo <gsomlo@gmail.com> - 1-24.20230607git119b47a
- Update to newer snapshot

* Thu May 11 2023 Gabriel Somlo <gsomlo@gmail.com> - 1-23.20230511gite3529d3
- Update to newer snapshot

* Sun Apr 23 2023 Gabriel Somlo <gsomlo@gmail.com> - 1-22.20230423git051bdb1
- Update to newer snapshot

* Tue Mar 07 2023 Gabriel Somlo <gsomlo@gmail.com> - 1-21.20230307git132a98a
- Update to newer snapshot

* Sun Feb 26 2023 Gabriel Somlo <gsomlo@gmail.com> - 1-20.20230226git14050f9
- Update to newer snapshot
- Temp. use bundled pybind11 (https://github.com/pybind/pybind11/issues/4529)

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 1-19.20230215git78dabb7
- Rebuilt for Boost 1.81

* Wed Feb 15 2023 Gabriel Somlo <gsomlo@gmail.com> - 1-18.20230215git78dabb7
- Update to newer snapshot

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1-17.20230104gita46afc6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 04 2023 Gabriel Somlo <gsomlo@gmail.com> - 1-16.20230104gita46afc6
- Update to newer snapshot

* Fri Dec 09 2022 Gabriel Somlo <gsomlo@gmail.com> - 1-15.20221209gitb5d30c7
- Update to newer snapshot

* Wed Nov 09 2022 Gabriel Somlo <gsomlo@gmail.com> - 1-14.20221109gitac17c36
- Update to newer snapshot

* Thu Oct 06 2022 Gabriel Somlo <gsomlo@gmail.com> - 1-13.20221006git0d1ea9e
- Update to newer snapshot

* Mon Sep 12 2022 Gabriel Somlo <gsomlo@gmail.com> - 1-12.20220912gitf1349e1
- Update to newer snapshot

* Sun Aug 21 2022 Gabriel Somlo <gsomlo@gmail.com> - 1-11.20220821gitccf4367
- Update to newer snapshot

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1-10.20220705git86396c4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 05 2022 Gabriel Somlo <gsomlo@gmail.com> - 1-9.20220705git86396c4
- Update to newer snapshot (incl. fix for Python 3.11, BZ 2103645).

* Sat Jun 11 2022 Gabriel Somlo <gsomlo@gmail.com> - 1-8.20220611giteac864e
- Update to newer snapshot.

* Wed May 11 2022 Thomas Rodgers <trodgers@redhat.com> - 1-7.20220509git769a1f2
- Rebuilt for Boost 1.78

* Mon May 09 2022 Gabriel Somlo <gsomlo@gmail.com> - 1-6.20220509git769a1f2
- Update to newer snapshot.

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 1-5.20220407gitd5ec421
- Rebuilt for Boost 1.78

* Thu Apr 07 2022 Gabriel Somlo <gsomlo@gmail.com> - 1-4.20220407gitd5ec421
- Update to newer snapshot.

* Fri Mar 04 2022 Gabriel Somlo <gsomlo@gmail.com> - 1-3.20220304git2c6ca48
- Update to newer snapshot.

* Tue Feb 22 2022 Gabriel Somlo <gsomlo@gmail.com> - 1-2.20220222git4666ea7
- Update to newer snapshot.

* Thu Jan 27 2022 Gabriel Somlo <gsomlo@gmail.com> - 1-1.20220127git1301feb
- Update to newer snapshot.

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.29.20211209gitfd2d4a8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 09 2021 Gabriel Somlo <gsomlo@gmail.com> - 0-0.28.20211209gitfd2d4a8
- Update to newer snapshot.

* Sat Nov 06 2021 Gabriel Somlo <gsomlo@gmail.com> - 0-0.27.20211106git1615b0a
- Update to newer snapshot.

* Tue Sep 28 2021 Gabriel Somlo <gsomlo@gmail.com> - 0-0.26.20210928git9d8d3bd
- Update to newer snapshot.

* Sat Sep 04 2021 Gabriel Somlo <gsomlo@gmail.com> - 0-0.25.20210904gitfd6366f
- Update to newer snapshot.

* Sat Aug 07 2021 Jonathan Wakely <jwakely@redhat.com> - 0-0.24.20210523gite19d44e
- Rebuilt for Boost 1.76

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.23.20210523gite19d44e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0-0.22.20210523gite19d44e
- Rebuilt for Python 3.10

* Wed Jun 02 2021 Gabriel Somlo <gsomlo@gmail.com> - 0-0.21.20210523gite19d44e
- Enable GUI (BZ 1966568)

* Sun May 23 2021 Gabriel Somlo <gsomlo@gmail.com> - 0-0.20.20210523gite19d44e
- Update to newer snapshot.

* Sun Mar 07 2021 Gabriel Somlo <gsomlo@gmail.com> - 0-0.19.20210307gitf0e30ab
- Update to newer snapshot.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.18.20201124git8955230
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 0-0.17.20201124git8955230
- Rebuilt for Boost 1.75

* Tue Nov 24 2020 Gabriel Somlo <gsomlo@gmail.com> - 0-0.16.20201124git8955230
- Update to newer snapshot

* Thu Aug 06 2020 Gabriel Somlo <gsomlo@gmail.com> - 0-0.15.20200806gitb39a2a5
- Update to newer snapshot
- Update cmake build commands (fix FTBFS BZ 1864193)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.20200129git85f4452
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.20200129git85f4452
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 31 2020 Jonathan Wakely <jwakely@redhat.com> - 0-0.12.20200129git85f4452
- Rebuilt for Boost 1.73

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0-0.11.20200129git85f4452
- Rebuilt for Python 3.9

* Tue Feb 11 2020 Gabriel Somlo <gsomlo@gmail.com> - 0-0.10.20200129git85f4452
- Rebuilt for trellis dependency.

* Wed Jan 29 2020 Gabriel Somlo <gsomlo@gmail.com> - 0-0.9.20200129git85f4452
- Update to newer snapshot.
- Fix Python 3.9 build (BZ #1795549).

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.20190821gitc192ba2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Aug 21 2019 Gabriel Somlo <gsomlo@gmail.com> - 0-0.7.20190821gitc192ba2
- Update to newer snapshot
- Spec file: add 'snapdate' variable
- Fix python 3.8 build (BZ #1743893)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0-0.6.20190415gitdb7e850
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.20190415gitdb7e850
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 15 2019 Gabriel Somlo <gsomlo@gmail.com> - 0-0.4.20190415gitdb7e850
- Update to newer snapshot

* Mon Apr 01 2019 Gabriel Somlo <gsomlo@gmail.com> - 0-0.3.20190401gitd27ec2c
- Update to snapshot with fast HeAP-based analytical placer
- Package included ice40, ecp5 example projects as documentation

* Thu Mar 21 2019 Lubomir Rintel <lkundrak@v3.sk> - 0-0.2.20190319gitcadbf42
- Enable ecp5

* Tue Mar 19 2019 Lubomir Rintel <lkundrak@v3.sk> - 0-0.1.20190319gitcadbf42
- Initial packaging
