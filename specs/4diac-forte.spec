# Force out of source build
%undefine __cmake_in_source_build

%global with_sysfs 1
%global with_opcua 0
%global with_paho 1
%global with_modbus 1

# LuaJIT is only available on i686, x86_64, and aarch64
%ifarch i686 x86_64 aarch64
%global with_lua 0
%global with_luajit 1
%else
%global with_lua 1
%global with_luajit 0
%endif

Name:     4diac-forte
Version:  2.0.1
Release:  11%{?dist}
Summary:  IEC 61499 runtime environment
License:  EPL-2.0
URL:      http://eclipse.org/4diac
Source0:  https://git.eclipse.org/c/4diac/org.eclipse.4diac.forte.git/snapshot/org.eclipse.4diac.forte-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: systemd
%{?systemd_requires}

%if 0%{?with_opcua}
BuildRequires: open62541-devel >= 1.0
%endif

%if 0%{?with_lua}
BuildRequires: lua-devel >= 5.1
%endif

%if 0%{?with_luajit}
BuildRequires: luajit-devel >= 2.1.0
%endif

%if 0%{?with_paho}
BuildRequires: paho-c-devel >= 1.3.9
%endif

%if 0%{?with_modbus}
BuildRequires: libmodbus-devel >= 3.1.6
%endif

%description
The 4DIAC runtime environment (4DIAC-RTE, FORTE) is a small portable
implementation of an IEC 61499 runtime environment targeting small
embedded control devices (16/32 Bit), implemented in C++. It supports
online-reconfiguration of its applications and the real-time capable
execution of all function block types provided by the IEC 61499 standard.

%prep
%setup -q -n org.eclipse.4diac.forte-%{version}

%build
%cmake -DFORTE_ARCHITECTURE=Posix \
       -DFORTE_COM_ETH=ON \
       -DFORTE_COM_FBDK=ON \
       -DFORTE_COM_LOCAL=ON \
%if 0%{?with_paho}
       -DFORTE_COM_PAHOMQTT=ON \
%endif
%if 0%{?with_modbus}
       -DFORTE_COM_MODBUS=ON \
%endif
%if 0%{?with_opcua}
       -DFORTE_COM_OPC_UA=ON -DFORTE_COM_OPC_UA_INCLUDE_DIR=%{_includedir} -DFORTE_COM_OPC_UA_LIB_DIR=%{_libdir} -DFORTE_COM_OPC_UA_LIB=libopen62541.so -DFORTE_COM_OPC_UA_MASTER_BRANCH=ON \
%endif
       -DFORTE_MODULE_CONVERT=ON \
       -DFORTE_MODULE_IEC61131=ON \
%if 0%{?with_sysfs}
       -DFORTE_MODULE_SysFs=ON \
%endif
       -DFORTE_MODULE_UTILS=ON \
       -DFORTE_MODULE_IEC61131=ON \
%if 0%{?with_lua}
       -DFORTE_USE_LUATYPES=Lua \
%endif
%if 0%{?with_luajit}
       -DFORTE_USE_LUATYPES=LuaJIT -DLUAJIT_INCLUDE_DIR=%{_includedir}/luajit-2.1 -DLUAJIT_LIBRARY=%{_libdir}/libluajit-5.1.so \
%endif
       -DFORTE_TESTS=OFF

%cmake_build

%install
mkdir -p %{buildroot}%{_unitdir}
install -p systemd/4diac-forte.service %{buildroot}%{_unitdir}

mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
install -p systemd/4diac-forte-sysconfig %{buildroot}%{_sysconfdir}/sysconfig/4diac-forte

%cmake_install

%post
%systemd_post 4diac-forte.service

%preun
%systemd_preun 4diac-forte.service

%postun
%systemd_postun_with_restart 4diac-forte.service

%files
%license epl-2.0.html
%{_bindir}/forte
%{_unitdir}/4diac-forte.service
%config(noreplace) %{_sysconfdir}/sysconfig/4diac-forte

%changelog
* Mon Jan 20 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 29 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 15 2022 Jens Reimann <ctron@dentrassi.de> - 2.0.1-1
- Update to version 2.0.1
- Enable MQTT support using Eclipse Paho
- Enable Modbus support
- Enable JIT for Lua (i686, x86_64, aarch66 only)
- Enable IEC-61131 module

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.12.0-5
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 24 2020 Jens Reimann <ctron@dentrassi.de> - 1.12.0-4
- Disable OPC UA as doesn't work with the current release of libopen62541

* Fri Jul 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 05 2020 Neal Gompa <ngompa13@gmail.com> - 1.12.0-1
- Update to release 1.12.0 to fix with CMake 3.17+

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct 07 2019 Jens Reimann <jreimann@redhat.com> - 1.11.0-1
- Update to release 1.11.0

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 12 2019 Peter Robinson <pbrobinson@fedoraproject.org> 1.9.0-4
- Build fixes and cleanup

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Apr 19 2018 Jens Reimann <jreimann@redhat.com> - 1.9.0-1.1
- Update to the final release 1.9.0
- Enable Lua integration
- Enable OPC UA integration

* Mon Feb 05 2018 Jens Reimann <jreimann@redhat.com> - 1.9.0.M3-0.1
- Initial version of the package
