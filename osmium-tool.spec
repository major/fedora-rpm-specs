%global catch_version 2.13.10
%global libosmium_version 2.17.0
%global protozero_version 1.6.3
%global rapidjson_version 1.1.0

Name:           osmium-tool
Version:        1.16.0
Release:        1%{?dist}
Summary:        Command line tool for working with OpenStreetMap data

License:        GPL-3.0-only
URL:            http://osmcode.org/osmium-tool/
Source0:        https://github.com/osmcode/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# Disable tests which break on big endian architectures
# https://github.com/osmcode/osmium-tool/issues/176
Patch0:         osmium-tool-bigendian.patch

BuildRequires:  cmake make gcc-c++ pandoc man-db

BuildRequires:  catch2-devel >= %{catch_version}
BuildRequires:  libosmium-devel >= %{libosmium_version}
BuildRequires:  libosmium-static >= %{libosmium_version}
BuildRequires:  protozero-devel >= %{protozero_version}
BuildRequires:  protozero-static >= %{protozero_version}
BuildRequires:  rapidjson-devel >= %{rapidjson_version}
BuildRequires:  rapidjson-static >= %{rapidjson_version}

%description
Command line tool for working with OpenStreetMap data
based on the Osmium library


%prep
%autosetup -p 1
sed -i -e "s/-O3 -g//" CMakeLists.txt
rm -rf include/rapidjson test/include/catch.hpp
ln -sf /usr/include/catch2/catch.hpp test/include


%build
%cmake
%cmake_build


%install
%cmake_install
mkdir -p %{buildroot}%{_datadir}/zsh/site-functions
install -p -m644 zsh_completion/* %{buildroot}%{_datadir}/zsh/site-functions


%check
%ctest


%files
%doc README.md CHANGELOG.md
%license LICENSE.txt
%{_bindir}/osmium
%{_mandir}/man1/osmium*.1.gz
%{_mandir}/man5/osmium*.5.gz
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_osmium


%changelog
* Fri Sep 22 2023 Tom Hughes <tom@compton.nu> - 1.16.0-1
- Update to 1.16.0 upstream release

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Mar 11 2023 Tom Hughes <tom@compton.nu> - 1.15.0-3
- Require catch2-devel instead of catch-devel

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 1.15.0-2
- Rebuilt for Boost 1.81

* Fri Jan 20 2023 Tom Hughes <tom@compton.nu> - 1.15.0-1
- Update to 1.15.0 upstream release

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 1.14.0-2
- Rebuilt for Boost 1.78

* Tue Feb  8 2022 Tom Hughes <tom@compton.nu> - 1.14.0-1
- Update to 1.14.0 upstream release

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Oct  6 2021 Tom Hughes <tom@compton.nu> - 1.13.2-1
- Update to 1.13.2 upstream release

* Sat Aug 07 2021 Jonathan Wakely <jwakely@redhat.com> - 1.13.1-5
- Rebuilt for Boost 1.76

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Mar 31 2021 Jonathan Wakely <jwakely@redhat.com> - 1.13.1-3
- Rebuilt for removed libstdc++ symbols (#1937698)

* Fri Feb 19 2021 Tom Hughes <tom@compton.nu> - 1.13.1-2
- Unbundle catch

* Mon Feb  1 2021 Tom Hughes <tom@compton.nu> - 1.13.1-1
- Update to 1.13.1 upstream release

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 1.13.0-2
- Rebuilt for Boost 1.75

* Fri Jan  8 2021 Tom Hughes <tom@compton.nu> - 1.13.0-1
- Update to 1.13.0 upstream release

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 28 2020 Tom Hughes <tom@compton.nu> - 1.12.1-1
- Update to 1.12.1 upstream release

* Thu May 28 2020 Jonathan Wakely <jwakely@redhat.com> - 1.12.0-2
- Rebuilt for Boost 1.73

* Tue Apr 21 2020 Tom Hughes <tom@compton.nu> - 1.12.0-1
- Update to 1.12.0 upstream release

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 20 2019 Tom Hughes <tom@compton.nu> - 1.11.1-1
- Update to 1.11.1 upstream release

* Tue Sep 17 2019 Tom Hughes <tom@compton.nu> - 1.11.0-1
- Update to 1.11.0 upstream release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 1.10.0-2
- Rebuilt for Boost 1.69

* Mon Dec 10 2018 Tom Hughes <tom@compton.nu> - 1.10.0-1
- Update to 1.10.0 upstream release

* Sat Sep 15 2018 Tom Hughes <tom@compton.nu> - 1.9.1-1
- Update to 1.9.1 upstream release

* Sun Aug 12 2018 Tom Hughes <tom@compton.nu> - 1.9.0-1
- Update to 1.9.0 upstream release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Apr  1 2018 Tom Hughes <tom@compton.nu> - 1.8.0-1
- Update to 1.8.0 upstream release

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 1.7.1-2
- Rebuilt for Boost 1.66

* Sat Aug 26 2017 Tom Hughes <tom@compton.nu> - 1.7.1-1
- Update to 1.7.1 upstream release

* Tue Aug 15 2017 Tom Hughes <tom@compton.nu> - 1.7.0-1
- Update to 1.7.0 upstream release

* Thu Aug 10 2017 Tom Hughes <tom@compton.nu> - 1.6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Jonathan Wakely <jwakely@redhat.com> - 1.6.1-5
- Rebuilt for s390x binutils bug

* Tue Jul 18 2017 Jonathan Wakely <jwakely@redhat.com> - 1.6.1-4
- Rebuilt for Boost 1.64

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri May  5 2017 Tom Hughes <tom@compton.nu> - 1.6.1-2
- Rebuild against libosmium 2.12.2

* Mon Apr 10 2017 Tom Hughes <tom@compton.nu> - 1.6.1-1
- Update to 1.6.1 upstream release

* Tue Mar  7 2017 Tom Hughes <tom@compton.nu> - 1.6.0-1
- Update to 1.6.0 upstream release

* Tue Feb 14 2017 Tom Hughes <tom@compton.nu> - 1.5.1-1
- Update to 1.5.1 upstream release

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 17 2017 Tom Hughes <tom@compton.nu> - 1.4.1-2
- Rebuild against libosmium 2.11.0

* Mon Nov 21 2016 Tom Hughes <tom@compton.nu> - 1.4.1-1
- Update to 1.4.1 upstream release
- Exclude ppc64le as libosmium tests fail

* Fri Sep 16 2016 Tom Hughes <tom@compton.nu> - 1.4.0-1
- Update to 1.4.0 upstream release

* Thu Sep 15 2016 Tom Hughes <tom@compton.nu> - 1.3.1-3
- Rebuild against libosmium 2.9.0
- Exclude aarch64 as libosmium tests fail

* Thu Aug  4 2016 Tom Hughes <tom@compton.nu> - 1.3.1-2
- Rebuild against libosmium 2.8.0

* Sat Jun 11 2016 Tom Hughes <tom@compton.nu> - 1.3.1-1
- Update to 1.3.1 upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 24 2016 Tom Hughes <tom@compton.nu> - 1.3.0-3
- Rebuild for boost 1.60.0

* Sun Nov 29 2015 Tom Hughes <tom@compton.nu> - 1.3.0-2
- Own %%{_datadir}/zsh

* Sun Nov 29 2015 Tom Hughes <tom@compton.nu> - 1.3.0-1
- Update to 1.3.0 upstream release

* Sun Sep  6 2015 Tom Hughes <tom@compton.nu> - 1.2.1-1
- Update to 1.2.1 upstream release

* Wed Jul 22 2015 Tom Hughes <tom@compton.nu> - 1.1.1-3
- Requre man-db for tests

* Thu Jul 16 2015 Tom Hughes <tom@compton.nu> - 1.1.1-2
- Use %%cmake

* Sun Jul 12 2015 Tom Hughes <tom@compton.nu> - 1.1.1-1
- Update to 1.1.1 upstream release

* Mon Jun  8 2015 Tom Hughes <tom@compton.nu> - 1.0.1-1
- Initial build
