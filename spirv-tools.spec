%undefine __cmake_in_source_build

%global sdkver 1.3.224.0

Name:           spirv-tools
Version:        2022.2
Release:        4%{?dist}
Summary:        API and commands for processing SPIR-V modules

License:        ASL 2.0
URL:            https://github.com/KhronosGroup/SPIRV-Tools
Source0:        %url/archive/sdk-%{sdkver}.tar.gz#/SPIRV-Tools-sdk-%{sdkver}.tar.gz

Patch0: fix-gcc12-build.patch

BuildRequires:  cmake3
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
%if 0%{?rhel} == 7
BuildRequires:  python36-devel
%else
BuildRequires:  python3-devel
%endif
BuildRequires:  python3-rpm-macros
BuildRequires:  spirv-headers-devel
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description
The package includes an assembler, binary module parser,
disassembler, and validator for SPIR-V..

%package        libs
Summary:        Library files for %{name}
Provides:       %{name}-libs%{?_isa} = %{version}

%description    libs
library files for %{name}

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
Development files for %{name}

%prep
%autosetup -p1 -n SPIRV-Tools-sdk-%{sdkver}

%build
%cmake3 -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_LIBDIR=%{_lib} \
        -DSPIRV-Headers_SOURCE_DIR=%{_prefix} \
        -DPYTHON_EXECUTABLE=%{__python3} \
        -DSPIRV_TOOLS_BUILD_STATIC=OFF \
        -GNinja
%cmake3_build

%install
%cmake3_install

%ldconfig_scriptlets libs

%files
%license LICENSE
%doc README.md CHANGES
%{_bindir}/spirv-as
%{_bindir}/spirv-cfg
%{_bindir}/spirv-dis
%{_bindir}/spirv-lesspipe.sh
%{_bindir}/spirv-link
%{_bindir}/spirv-lint
%{_bindir}/spirv-opt
%{_bindir}/spirv-reduce
%{_bindir}/spirv-val

%files libs
%{_libdir}/libSPIRV-Tools-diff.so
%{_libdir}/libSPIRV-Tools-link.so
%{_libdir}/libSPIRV-Tools-lint.so
%{_libdir}/libSPIRV-Tools-opt.so
%{_libdir}/libSPIRV-Tools.so
%{_libdir}/libSPIRV-Tools-reduce.so
%{_libdir}/libSPIRV-Tools-shared.so

%files devel
%{_includedir}/spirv-tools/
%{_libdir}/cmake/*
%{_libdir}/pkgconfig/SPIRV-Tools-shared.pc
%{_libdir}/pkgconfig/SPIRV-Tools.pc

%changelog
* Wed Aug 24 2022 Dave Airlie <airlied@redhat.com> - 2022.2-4
- Rebase to 1.3.224 SDK Version

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2022.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 17 2022 Dave Airlie <airlied@redhat.com> - 2022.2-2
- Rebase to 1.3.216 SDK Version

* Wed Apr 27 2022 Dave Airlie <airlied@redhat.com> - 2022.2-1.20220407.git7826e19
- Rebase to 1.3.211 SDK Version

* Wed Feb 16 2022 Dave Airlie <airlied@redhat.com> - 2022.1-1.20220202.git45dd184
- Rebase to 1.3.204 SDK Version

* Sat Jan 29 2022 Dave Jan Grulich <jgrulich@redhat.com> - 2021.4-5.20211110.git21e3f68
- Fix endianness of string literals

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2021.4-4.20211110.git21e3f68
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec 10 2021 Dave Airlie <airlied@redhat.com> - 2021.4-3.20211110.git21e3f68
- Retain compat with both ABIs

* Mon Dec 06 2021 Dave Airlie <airlied@redhat.com> - 2021.4-2.20211110.git21e3f68
- Restore previous ABI

* Tue Nov 23 2021 Dave Airlie <airlied@redhat.com> - 2021.4-1.20211110.git21e3f68
- Update to 1.2.198.0 SDK Version

* Tue Sep 07 2021 Dave Airlie <airlied@redhat.com> - 2021.3-1.20210825.git1fbed83
- Update to 1.2.189.0 SDK Version

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2021.2-2.20210619.git5dd2f76
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jul 07 2021 Dave Airlie <airlied@redhat.com> - 2021.2-1
- Update to 1.2.182.0 SDK Version

* Tue May 18 2021 Dave Airlie <airlied@redhat.com> - 2021.1-1
- Update to 1.2.176.1 SDK version

* Thu Jan 28 2021 Dave Airlie <airlied@redhat.com> - 2020.5-5
- Update to 1.2.162.0 SDK version

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020.5-4.20201031.gitf7da527
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Dec 04 2020 Jeff Law <law@redhat.com> - 2020.5-3.20201031.gitf7da5277
- Fix undesirable strncpy call to instead use memcpy to avoid
  gcc-11 diagnostic

* Mon Nov 02 2020 Dave Airlie <airlied@redhat.com> - 2020.5-2.20201031.gitf7da5277
- update to latest spirv-tools

* Tue Aug 04 2020 Dave Airlie <airlied@redhat.com> - 2029.5-1.20200803.git92a71657
- update to latest spirv-tools

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019.5-3.20200421.git67f4838
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr 22 2020 Dave Airlie <airlied@redhat.cvom> - 2019.5-2
- git snapshot for newer glslang/validation layers

* Wed Jan 29 2020 Dave Airlie <airlied@redhat.com> - 2019.5-1
- git snapshot for newer glslang/validation layers

* Tue Nov 12 2019 Dave Airlie <airlied@redhat.com> - 2019.4-1
- git snapshot for newer glslang/validation layers

* Thu Aug 01 2019 Dave Airlie <airlied@redhat.com> - 2019.4-0.1
- git snapshot to let newer vulkan validation layers build
- stats removed upstream

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2019.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 10 13:46:33 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 2019.3-1
- Release 2019.3

* Thu Mar 07 2019 Dave Airlie <airlied@redhat.com> - 2019.1-2
- Add patch to let vulkan-validation-layers build

* Mon Feb 04 2019 Dave Airlie <airlied@redhat.com> - 2019.1-1
- Update to 2019.1 release

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 23 2018 Leigh Scott <leigh123linux@googlemail.com> - 2018.4-1
- Update to 2018.4 release

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2018.3.0-0.3.20180407.git26a698c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 25 2018 Dave Airlie <airlied@redhat.com> - 2018.3.0-0.2.20180407.git26a698c
- Move to python3 and drop the simplejson buildreq.

* Tue Apr 24 2018 Leigh Scott <leigh123linux@googlemail.com> - 2018.3.0-0.1.20180407.git26a698c
- Bump version to 2018.3.0 to match .pc files

* Tue Apr 24 2018 Leigh Scott <leigh123linux@googlemail.com> - 2018.1-0.4.20180407.git26a698c
- Bump provides to 2018.3.0

* Tue Apr 24 2018 Leigh Scott <leigh123linux@googlemail.com> - 2018.1-0.3.20180407.git26a698c
- Update for vulkan 1.1.73.0

* Wed Feb 14 2018 Leigh Scott <leigh123linux@googlemail.com> - 2018.1-0.2.20180205.git9e19fc0
- Add isa to the provides

* Fri Feb 09 2018 Leigh Scott <leigh123linux@googlemail.com> - 2018.1-0.1.20180205.git9e19fc0
- Fix version
- Fix pkgconfig file
- Add version provides to -libs package

* Fri Feb 09 2018 Leigh Scott <leigh123linux@googlemail.com> - 2016.7-0.5.20180205.git9e19fc0
- Update for vulkan 1.0.68.0
- Try building as shared object
- Split libs into -libs subpackage

* Fri Feb 09 2018 Leigh Scott <leigh123linux@googlemail.com> - 2016.7-0.4.20171023.git5834719
- Use ninja to build

* Mon Jan 22 2018 Leigh Scott <leigh123linux@googlemail.com> - 2016.7-0.3.20171023.git5834719
- Add python prefix to fix the stupid Bodhi tests

* Wed Jan 03 2018 Leigh Scott <leigh123linux@googlemail.com> - 2016.7-0.2.20171023.git5834719
- Split binaries into main package

* Thu Jul 13 2017 Leigh Scott <leigh123linux@googlemail.com> - 2016.7-0.1.20171023.git5834719
- First build

