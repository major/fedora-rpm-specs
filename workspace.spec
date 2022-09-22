Name:		workspace

Version:	1.3.1
Release:	11%{?dist}
Summary:	A tool to create scratch directories by users with an expiration date

License:	GPLv3
URL:		https://github.com/holgerBerger/hpc-workspace
Source0:	https://github.com/holgerBerger/hpc-workspace/archive/v%{version}/%{name}-%{version}.tar.gz

Patch0:	        ws_alloc_option.patch

#BuildRequires:	sed
BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	cmake
BuildRequires:	boost-devel
BuildRequires:	ncurses-devel
BuildRequires:	yaml-cpp-devel
BuildRequires:	python3-pyyaml

Requires:	python3-pyyaml


%description
A **workspace** is a directory, with an associated expiration date, created on
behalf of a user, to prevent disks from uncontrolled filling.
The project provides user and admin tools to manage those directories.


%prep
%setup -q -n hpc-%{name}-%{version}
# - remove the cmake_cxx_flags settings in the file CMakeLists.txt because this
#   override the build flags form the optflags macro and so allows the use of
#   the cmake macro in this spec file
sed -e '/^SET(CMAKE_CXX_FLAGS "-Wall -g")/d' -i CMakeLists.txt
%patch0


%build
%cmake
%cmake_build


%install
%cmake_install
install -p -m 755 contribs/ws_prepare %{buildroot}%{_sbindir}/ws_prepare


%files
%license LICENSE
%doc README.md admin-guide.md user-guide.md ws.conf ws.conf_full_sample
%{_bindir}/ws_extend
%{_bindir}/ws_find
%{_bindir}/ws_list
%{_bindir}/ws_register
%{_bindir}/ws_send_ical
# sbin/ws_restore is only for root
%{_sbindir}/ws_*
%{_mandir}/man1/ws_*

# this files need setuid
%defattr(4111,root,root)
%{_bindir}/ws_allocate
%{_bindir}/ws_release
%{_bindir}/ws_restore


%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 1.3.1-10
- Rebuilt for Boost 1.78

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Aug 07 2021 Jonathan Wakely <jwakely@redhat.com> - 1.3.1-8
- Rebuilt for Boost 1.76

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 1.3.1-5
- Rebuilt for Boost 1.75

* Wed Aug 12 2020 Gerd Pokorra <gp@zimt.uni-siegen.de> - 1.3.1-4
- Fix bug 1865626 with using new cmake macros 
  https://bugzilla.redhat.com/show_bug.cgi?id=1865626

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 14 2020 Gerd Pokorra <gp@zimt.uni-siegen.de> - 1.3.1-1
- update to version 1.3.1
- add patch ws_alloc_option.patch

* Wed Jun 03 2020 Gerd Pokorra <gp@zimt.uni-siegen.de> - 1.3.0-2
- Rebuilt for Boost 1.73 (BUG ID: 1843150)

* Tue Jun 02 2020 Gerd Pokorra <gp@zimt.uni-siegen.de> - 1.3.0-1
- update to version 1.3.0
- remove patch and work with sed

* Sat May 30 2020 Jonathan Wakely <jwakely@redhat.com> - 1.1.0-6
- Rebuilt for Boost 1.73

* Sat Mar 28 2020 Gerd Pokorra <gp@zimt.uni-siegen.de> - 1.1.0-5
- add a comment above the patch to explain it
- separate BRs one per line

* Mon Mar 23 2020 Gerd Pokorra <gp@zimt.uni-siegen.de> - 1.1.0-4
- wrap description

* Wed Mar 18 2020 Gerd Pokorra <gp@zimt.uni-siegen.de> - 1.1.0-3
- remove the CXXFLAGS settings in CMakeLists.txt

* Tue Mar 17 2020 Gerd Pokorra <gp@zimt.uni-siegen.de> - 1.1.0-2
- add use of _hardened_build

* Tue Mar 17 2020 Gerd Pokorra <gp@zimt.uni-siegen.de> - 1.1.0-1
- add patch for version number
- improved the source tag
- updated to the new upstream version
- initail spec file
