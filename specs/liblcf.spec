Name: liblcf
Summary: Library to handle RPG Maker 2000/2003 game data

# liblcf itself is MIT, but it uses some example code
# from the BSD-licensed "inih" library, as well as
# some header-only C++ libraries, which are subject
# to the Boost License.
#
# BSD-licensed:
# - src/ini.cpp (removed before build)
# - src/ini.h   (removed before build)
# - src/inireader.cpp
# - src/inireader.h
#
# Boost:
# - src/lcf/third_party/span.h
# - src/lcf/third_party/string_view.h
License: MIT AND BSD-2-Clause AND BSL-1.0

Version: 0.8
Release: 8%{?dist}

URL: https://github.com/EasyRPG/liblcf
Source0: %{URL}/archive/%{version}/%{name}-%{version}.tar.gz

Patch0: 0000-unbundle-inih.patch

BuildRequires: cmake
BuildRequires: doxygen
BuildRequires: gcc-c++
BuildRequires: make

BuildRequires: expat-devel
BuildRequires: inih-devel
BuildRequires: libicu-devel

%description
%{name} is a library to handle RPG Maker 2000/2003 game data.
It can read and write LCF and XML files.

%{name} is part of the EasyRPG Project.


%package devel
Summary: Development files for %{name}
Requires: %{name}%{?isa} = %{version}-%{release}

Requires: inih-devel

%description devel
This package contains files required to develop applications using %{name}.


%package tools
Summary: Programs for handling RPG Maker 2000/2003 game data

%description tools
This package contains helper tools for working with
RPG Maker 2000/2003 data files:
- lcf2xml: converts RM2k data files to XML (and vice-versa)
- lcfstrings: extracts all strings from an RM2k data file


%package doc
Summary: Documentation for %{name}
BuildArch: noarch

%description doc
This package contains documentation (in HTML format) for %{name}.


%prep
%autosetup -p1

# Remove bundled inih library
rm src/ini.cpp src/lcf/ini.h


%build
%cmake \
	-DLIBLCF_UPDATE_MIMEDB=OFF \
	-DCMAKE_BUILD_TYPE=Release
%cmake_build
%cmake_build --target liblcf_doc


%install
%cmake_install

# liblcf bundles the "inih" library and exposes it as part of its API.
# Symlink liblcf's "ini.h" file to the un-bundled library's version.
ln -s %{_includedir}/ini.h %{buildroot}%{_includedir}/lcf/ini.h


%check
%cmake_build --target check


%files
%license COPYING
%{_libdir}/%{name}.so.*
%{_datadir}/mime/packages/%{name}*.xml


%files devel
%{_includedir}/lcf/
%{_libdir}/%{name}.so
%{_libdir}/cmake/%{name}/
%{_libdir}/pkgconfig/%{name}.pc


%files tools
%{_bindir}/lcf2xml
%{_bindir}/lcfstrings


%files doc
%license COPYING
%doc doc/*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 31 2024 Pete Walter <pwalter@fedoraproject.org> - 0.8-6
- Rebuild for ICU 74

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 František Zatloukal <fzatlouk@redhat.com> - 0.8-2
- Rebuilt for ICU 73.2

* Tue May 02 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.8-1
- Update to v0.8
- Convert License tag to SPDX

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 31 2022 Pete Walter <pwalter@fedoraproject.org> - 0.7.0-6
- Rebuild for ICU 72

* Mon Aug 01 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 0.7.0-5
- Rebuilt for ICU 71.1

* Fri Jul 22 2022 Artur Iwicki <fedora@svgames.pl> - 0.7.0-4
- Fix CMake-related FTBFS

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 02 2021 Artur Iwicki <fedora@svgames.pl> - 0.7.0-1
- Update to v0.7.0
- Add the -tools subpackage
- Drop Patch1 (fix SIGSTKSZ usage - issue fixed upsteam)

* Thu Jul 29 2021 Artur Iwicki <fedora@svgames.pl> - 0.6.2-7
- Add Patch1: fix SIGSTKSZ usage (fixes rhbz#1987651)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu May 20 2021 Pete Walter <pwalter@fedoraproject.org> - 0.6.2-5
- Rebuild for ICU 69

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Aug 02 2020 Artur Iwicki <fedora@svgames.pl> - 0.6.2-3
- Build and install documentation (in -doc subpackage)
- Build and run tests

* Sat Aug 01 2020 Artur Iwicki <fedora@svgames.pl> - 0.6.2-2
- Unbundle the inih library
- Disable the automatic mimedb update during install

* Fri Jul 31 2020 Artur Iwicki <fedora@svgames.pl> - 0.6.2-1
- Initial packaging
