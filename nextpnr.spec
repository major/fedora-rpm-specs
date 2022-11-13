%global commit ac17c36bec5b0ae8d57b66f825acb6f21f2ca323
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global snapdate 20221109

Name:		nextpnr
Version:	1
Release:	14.%{snapdate}git%{shortcommit}%{?dist}
Summary:	FPGA place and route tool

License:	ISC and BSD and MIT and (MIT or Public Domain)
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
BuildRequires:	pybind11-devel
# NOTE: remember to update icestorm & trellis before rebuilding nextpnr!!!
BuildRequires:	icestorm >= 0-0.24
BuildRequires:	trellis-devel >= 1.2.1-12

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
%autosetup -n %{name}-%{commit}
cp 3rdparty/imgui/LICENSE.txt LICENSE-imgui.txt
cp 3rdparty/qtimgui/LICENSE LICENSE-qtimgui.txt
cp 3rdparty/python-console/LICENSE LICENSE-python-console.txt


%build
%cmake  -DARCH=all \
	-DICEBOX_DATADIR=%{_datadir}/icestorm \
	-DTRELLIS_LIBDIR=%{_libdir}/trellis \
	-DPYBIND11_INCLUDE_DIR="/usr/include/pybind11/" \
	-DBUILD_GUI=ON \
	-DUSE_OPENMP=ON
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
