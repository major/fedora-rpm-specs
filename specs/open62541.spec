%bcond_without docs

Name:     open62541
Version:  1.4.8
Release:  2%{?dist}
Summary:  OPC UA implementation
License:  MPL-2.0
URL:      http://open62541.org
Source0:  https://github.com/open62541/open62541/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: cmake3
BuildRequires: gcc
BuildRequires: graphviz
BuildRequires: libbpf-devel
BuildRequires: make
BuildRequires: openssl-devel
BuildRequires: python3

%description
open62541 is a C-based library (linking with C++ projects is possible)
with all necessary tools to implement dedicated OPC UA clients and servers,
or to integrate OPC UA-based communication into existing applications.

%package  devel
Summary:  Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%if %{with docs}
%package   doc
Summary:   Documentation for %{name}
BuildArch: noarch
BuildRequires: python3dist(sphinx)
BuildRequires: python3dist(sphinx-rtd-theme)

%description doc
The %{name}-doc package contains documentation for %{name}.
%endif

%prep
%autosetup -n %{name}-%{version} -p1

%build
# The version is usually extracted from the git tag, which is not available in the tarball.
# Therefore we need to set it manually.
%cmake3 \
  -DOPEN62541_VERSION=v%{version} \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
  -DUA_ENABLE_DA=ON \
  -DUA_ENABLE_DISCOVERY=ON \
  -DUA_ENABLE_DISCOVERY_SEMAPHORE=ON \
  -DUA_ENABLE_ENCRYPTION_OPENSSL=ON \
  -DUA_ENABLE_JSON_ENCODING=ON \
  -DUA_ENABLE_METHODCALLS=ON \
  -DUA_ENABLE_PARSING=ON \
  -DUA_ENABLE_NODEMANAGEMENT=ON \
  -DUA_ENABLE_PUBSUB=ON \
  -DUA_ENABLE_PUBSUB_ETH_UADP=ON \
  -DUA_ENABLE_PUBSUB_FILE_CONFIG=ON \
  -DUA_ENABLE_PUBSUB_INFORMATIONMODEL=ON \
  -DUA_ENABLE_PUBSUB_MONITORING=ON \
  -DUA_ENABLE_SUBSCRIPTIONS=ON \
  -DUA_ENABLE_SUBSCRIPTIONS_EVENTS=ON \
  .

#  -DUA_BUILD_EXAMPLES=ON \

%cmake_build
%if %{with docs}
cd %{__cmake_builddir}
%make_build doc
%endif

%install
%cmake_install

%if %{with docs}
cd %{__cmake_builddir}
# Remove build files not belonging to docs
rm -rf doc/CMakeFiles doc/Makefile doc/*.cmake
cd -
%endif

%ldconfig_scriptlets

%files
%license LICENSE
%doc AUTHORS README.md
%{_libdir}/libopen62541.so.1*

%files devel
%license LICENSE LICENSE-CC0
%doc FEATURES.md
%{_libdir}/libopen62541.so
%{_libdir}/pkgconfig/open62541.pc
%{_includedir}/%{name}/
%{_libdir}/cmake/%{name}/
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/certs/
%{_datadir}/%{name}/generate_*
%{_datadir}/%{name}/nodeset_compiler/
%{_datadir}/%{name}/schema/

%if %{with docs}
%files doc
%doc %{__cmake_builddir}/doc/*
%doc examples/
%endif

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Dec 03 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 1.4.8-1
- Update to 1.4.8
- Minor build cleanups, add option to make docs optional

* Mon Oct 07 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 1.4.6-1
- Update to 1.4.6

* Thu Oct 03 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 1.4.5-1
- Update to 1.4.5

* Tue Aug 13 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 1.4.4-1
- Update to 1.4.4

* Tue Aug 13 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 1.3.12-1
- Update to 1.3.12

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Apr 13 2024 Miroslav Suchý <msuchy@redhat.com> - 1.3.10-3
- convert license to SPDX

* Fri Apr 12 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 1.3.10-2
- Don't build with AMALGAMATION=ON

* Fri Apr 12 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 1.3.10-1
- Update to 1.3.10
- Enable publish/subscribe UADP over Ethernet

* Tue Feb 20 2024 Marie Loise Nolden <loise@kde.org> - 1.3.9-1
- update to 1.3.9

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jan 24 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 1.3.4-2
- Enable features: Discovery serviice (LDS), JSON encoding, Discovery service,
  Methods, Subscriptions, PubSub, Event monitoring, Data Access

* Fri Jan 20 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 1.3.4-1
- Update to 1.3.4

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 10 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 1.2.5-1
- Update to 1.2.5

* Sun Feb 20 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 1.2.4-1
- Update to 1.2.4

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 15 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 1.2.2-1
- Update to 1.2.2 release

* Thu Jan 28 2021 Jens Reimann <jreimann@redhat.com> - 1.1.5-1
- Update to 1.1.5 release

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 21 2020 Jens Reimann <jreimann@redhat.com> - 1.1.2-1
- Update to 1.1.2 release

* Tue Jun 02 2020 Charalampos Stratakis <cstratak@redhat.com> - 1.0.1-2
- Fix macro typo

* Wed Feb  5 2020 Peter Robinson <pbrobinson@fedoraproject.org> 1.0.1-1
- Update to 1.0.1 release

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Oct 06 2019 Till Hofmann <thofmann@fedoraproject.org> - 1.0-2
- Add doc subpackage

* Sun Oct 06 2019 Till Hofmann <thofmann@fedoraproject.org> - 1.0-1
- Update to 1.0 release
- Explicitly set BuildType to RelWithDebInfo

* Sun Aug  4 2019 Peter Robinson <pbrobinson@fedoraproject.org> 0.3.1-1
- Update to 0.3.1 release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 13 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-4
- Use python3 on Fedora again

* Tue Feb 12 2019 Peter Robinson <pbrobinson@fedoraproject.org> 0.3.0-3
- Package fixes for el7

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 20 2018 Till Hofmann <thofmann@fedoraproject.org> - 0.3.0-1
- Update to 0.3.0 release

* Wed Aug 22 2018 Jens Reimann <jreimann@redhat.com> - 0.3-0.4.rc2
- Upgraded to 0.3.rc2

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-0.3.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Jens Reimann <jreimann@redhat.com> - 0.3-0.2.rc1
- Upgraded to 0.3.rc1, switch to cmake3

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 Jens Reimann <jreimann@redhat.com> - 0.2-1
- Initial version of the package

