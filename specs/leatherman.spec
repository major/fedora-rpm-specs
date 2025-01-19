Name:           leatherman
Version:        1.12.13
Release:        3%{?dist}
Summary:        Collection of C++ and CMake utility libraries

# leatherman is ASL 2.0
# bundled rapidjson is MIT
License:        Apache-2.0 AND MIT
URL:            https://github.com/puppetlabs/leatherman
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# This unbundles boost-nowide and the boost libraries do not need
# to have the path to nowide added as it's included already
Patch0:         leatherman-1.12.4-shared_nowide.patch
Patch1:         system-catch.patch
Patch2:         %{name}-gcc11.patch

BuildRequires:  cmake >= 3.2.2
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  boost-devel >= 1.73
BuildRequires:  libcurl-devel
BuildRequires:  gettext
BuildRequires:  catch1-devel
Provides:       bundled(rapidjson) = 1.0.2

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
# Building against leatherman requires the boost nowide headers present
Requires:       boost-devel
# Strictly speaking, it is needed only if curl feature is activated
Requires:       libcurl-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1
# leatherman isn't compatible with rapidjson 1.1.0 yet so that has to be left bundled for now
# https://tickets.puppetlabs.com/browse/LTH-130
# catch is only used in testing so can be ignored

# Treating warnings as errors is pretty bad idea.
sed -i -e "s/\s*-Werror\s*//g" cmake/cflags.cmake

%build
%cmake . -B%{_target_platform} \
  -DLEATHERMAN_SHARED=ON \
  -DLEATHERMAN_DEBUG=ON \
  -DLEATHERMAN_CATCH_INCLUDE=%{_includedir}/catch \
  %{nil}
%make_build -C %{_target_platform}

%install
%make_install -C %{_target_platform}
%find_lang %{name}_logging
%find_lang %{name}_locale

%ldconfig_scriptlets

%files -f %{name}_logging.lang  -f %{name}_locale.lang
%license LICENSE
%{_libdir}/%{name}*.so.*

%files devel
%{_includedir}/%{name}
%{_libdir}/%{name}*.so
%dir %{_libdir}/cmake
%{_libdir}/cmake/%{name}/

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Apr 10 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.12.13-1
- 1.12.13

* Mon Feb 26 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.12.12-1
- 1.12.12

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Jonathan Wakely <jwakely@redhat.com> - 1.12.11-2
- Rebuilt for Boost 1.83

* Tue Oct 24 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.12.11-1
- 1.12.11

* Tue Oct 17 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.12.10-1
- 1.12.10

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Mar 04 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.12.9-4
- migrated to SPDX license

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 1.12.9-3
- Rebuilt for Boost 1.81

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Oct 17 2022 Gwyn Ciesla <gwync@protonmail.com> - 1.12.9-1
- 1.12.9

* Fri Jul 22 2022 Gwyn Ciesla <gwync@protonmail.com> - 1.12.8-1
- 1.12.8

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 1.12.7-3
- Rebuilt for Boost 1.78

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 19 2022 Gwyn Ciesla <gwync@protonmail.com> - 1.12.7-1
- 1.12.7

* Fri Aug 06 2021 Jonathan Wakely <jwakely@redhat.com> - 1.12.6-3
- Rebuilt for Boost 1.76

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jul 13 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.12.6-1
- 1.12.6

* Fri Jun 11 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.12.5-1
- 1.12.5

* Thu Mar 18 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.12.4-2
- Link leatherman_util against boost_nowide.

* Tue Mar 09 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.12.4-1
- 1.12.4

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 1.12.0-5
- Rebuilt for Boost 1.75

* Wed Nov 04 2020 Jeff Law <law@redhat.com> - 1.12.0-4
- Fix missing #includes for gcc-11

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 03 2020 Jonathan Wakely <jwakely@redhat.com> - 1.12.0-2
- Link libraries to libboost_nowide.so

* Wed Jun 03 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.12.0-1
- Update to 1.12.0

* Tue Jun 02 2020 Jonathan Wakely <jwakely@redhat.com> - 1.10.0-2
- Rebuilt and patched for Boost 1.73

* Tue Jan 28 2020 Adam Tkac <vonsch@gmail.com> - 1.10.1-1
- update to 1.10.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 24 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.6.1-1
- Update to 1.6.1

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 24 2019 Jonathan Wakely <jwakely@redhat.com> - 1.3.0-8
- Rebuilt for Boost 1.69

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 1.3.0-5
- Rebuilt for Boost 1.66

* Tue Nov 07 2017 James Hogarth <james.hogarth@gmail.com> - 1.3.0-4
- Restore catch to devel build (bz#1510392)
- Use make_build macro as per review

* Sun Oct 29 2017 Haïkel Guémar <hguemar@fedoraproject.org> - 1.3.0-3
- Merge with James spec + keep compatibility with CentOS SIGs

* Thu Oct 19 2017 James Hogarth <james.hogarth@gmail.com> - 1.3.0-2
- rebuilt

* Wed Oct 04 2017 James Hogarth <james.hogarth@gmail.com> - 1.3.0-1
- Upstream update
- unbundle nowide

* Thu Aug 31 2017 James Hogarth <james.hogarth@gmail.com> - 1.2.0-1
- Upstream update

* Sat Feb  4 2017 Haïkel Guémar <hguemar@fedoraproject.org> - 0.10.2-1
- Upstream 0.10.2
- Add Fedora support

* Thu Oct 27 2016 Haïkel Guémar <hguemar@fedoraproject.org> - 0.9.2-1
- Initial package on EL7

