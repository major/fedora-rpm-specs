# -*- rpm-spec -*-

%define with_mingw 0
%if 0%{?fedora}
    %define with_mingw 0%{!?_without_mingw:1}
%endif

Summary: osinfo database files
Name: osinfo-db
Version: 20221130
Release: 1%{?dist}
License: LGPLv2+
Source0: https://fedorahosted.org/releases/l/i/libosinfo/%{name}-%{version}.tar.xz
Source1: https://fedorahosted.org/releases/l/i/libosinfo/%{name}-%{version}.tar.xz.asc
URL: http://libosinfo.org/
BuildRequires: intltool
BuildRequires: osinfo-db-tools
BuildArch: noarch
Requires: hwdata

%if %{with_mingw}
BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw64-filesystem >= 95
%endif

%description
The osinfo database provides information about operating systems and
hypervisor platforms to facilitate the automated configuration and
provisioning of new virtual machines

%if %{with_mingw}
%package -n mingw32-osinfo-db
Summary: %{summary}

%description -n mingw32-osinfo-db
This package provides the osinfo database of information about
operating systems for use with virtualization provisioning tools

%package -n mingw64-osinfo-db
Summary: %{summary}

%description -n mingw64-osinfo-db
This package provides the osinfo database of information about
operating systems for use with virtualization provisioning tools

%endif

%install
osinfo-db-import --root %{buildroot} --dir %{_datadir}/osinfo %{SOURCE0}
%if 0%{?rhel}
# Remove the upstream virtio-win / spice-guest-tools drivers
find %{buildroot}/%{_datadir}/osinfo/os/microsoft.com/ -name "win-*.d" -type d -exec rm -rf {} +
%endif

%if %{with_mingw}
osinfo-db-import --root %{buildroot} --dir %{mingw32_datadir}/osinfo %{SOURCE0}
osinfo-db-import --root %{buildroot} --dir %{mingw64_datadir}/osinfo %{SOURCE0}
%endif

%files
%dir %{_datadir}/osinfo/
%{_datadir}/osinfo/VERSION
%{_datadir}/osinfo/LICENSE
%{_datadir}/osinfo/datamap
%{_datadir}/osinfo/device
%{_datadir}/osinfo/os
%{_datadir}/osinfo/platform
%{_datadir}/osinfo/install-script
%{_datadir}/osinfo/schema

%if %{with_mingw}
%files -n mingw32-osinfo-db
%dir %{mingw32_datadir}/osinfo
%doc %{mingw32_datadir}/osinfo/LICENSE
%{mingw32_datadir}/osinfo/VERSION
%{mingw32_datadir}/osinfo/datamap
%{mingw32_datadir}/osinfo/device
%{mingw32_datadir}/osinfo/os
%{mingw32_datadir}/osinfo/platform
%{mingw32_datadir}/osinfo/install-script
%{mingw32_datadir}/osinfo/schema

%files -n mingw64-osinfo-db
%dir %{mingw64_datadir}/osinfo
%doc %{mingw64_datadir}/osinfo/LICENSE
%{mingw64_datadir}/osinfo/VERSION
%{mingw64_datadir}/osinfo/datamap
%{mingw64_datadir}/osinfo/device
%{mingw64_datadir}/osinfo/os
%{mingw64_datadir}/osinfo/platform
%{mingw64_datadir}/osinfo/install-script
%{mingw64_datadir}/osinfo/schema
%endif

%changelog
* Wed Nov 30 2022 Victor Toso <victortoso@redhat.com> - 20221130-1
- Update to new release (v20221130)

* Tue Oct 18 2022 Victor Toso <victortoso@redhat.com> - 20221018-1
- Update to new release (v20221018)

* Tue Aug 30 2022 Victor Toso <victortoso@redhat.com> - 20220830-1
- Update to new release (v20220830)

* Fri Aug 26 2022 Victor Toso <victortoso@redhat.com> - 20220727-3
- Switch images/pxeboot in Fedora
  https://bugzilla.redhat.com/show_bug.cgi?id=2103835

* Tue Aug 23 2022 Daniel P. Berrangé <berrange@redhat.com> - 20220727-2
- Pull in mingw sub-packages

* Wed Jul 27 2022 Victor Toso <victortoso@redhat.com> - 20220727-1
- Update to new release (v20220727)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20220516-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 16 2022 Victor Toso <victortoso@redhat.com> - 20220516-1
- Update to new release (v20220516)

* Mon Feb 14 2022 Victor Toso <victortoso@redhat.com> - 20220214-1
- Update to new release (v20220214)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20211216-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 16 2021 Victor Toso <victortoso@redhat.com> - 20211216-1
- Update to new release (v20211216)

* Wed Oct 13 2021 Victor Toso <victortoso@redhat.com> - 20211013-1
- Update to new release (v20211013)

* Fri Sep 03 2021 Fabiano Fidêncio <fidencio@redhat.com> - 20210903-1
- Update to new release (v20210903)

* Mon Aug 09 2021 Fabiano Fidêncio <fidencio@redhat.com> - 20210809-1
- Update to new release (v20210806)

* Fri Aug 06 2021 Fabiano Fidêncio <fidencio@redhat.com> - 20210806-1
- Update to new release (v20210806)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20210621-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 21 2021 Fabiano Fidêncio <fidencio@redhat.com> - 20210621-1
- Update to new release (v20210621)

* Mon May 31 2021 Fabiano Fidêncio <fidencio@redhat.com> - 20210531-1
- Update to new release (v20210531)

* Mon Apr 26 2021 Fabiano Fidêncio <fidencio@redhat.com> - 20210426-1
- Update to new release (v20210426)

* Fri Mar 12 2021 Fabiano Fidêncio <fidencio@redhat.com> - 20210312-1
- Update to new release (v20210312)

* Mon Feb 15 2021 Fabiano Fidêncio <fidencio@redhat.com> - 20210215-1
- Don't distribute upstream virtio-win drivers on RHEL
- Update to new release (v20210215)

* Tue Feb 02 2021 Fabiano Fidêncio <fidencio@redhat.com> - 20210202-1
- Update to new release (v20210202)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20201218-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild
