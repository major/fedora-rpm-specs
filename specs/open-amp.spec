Name:		open-amp
Version:	2024.10.0
Release:	2%{?dist}
Summary:	Open Asymmetric Multi Processing (OpenAMP) framework project
License:	BSD-3-Clause OR BSD-2-Clause
URL:		https://github.com/OpenAMP/open-amp/
Source0:	https://github.com/OpenAMP/open-amp/archive/v%{version}/%{name}-%{version}.tar.gz
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

BuildRequires:	cmake
BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	libmetal-devel
BuildRequires:	libsysfs-devel

%description
The OpenAMP framework provides software components that enable development of
software applications for Asymmetric Multiprocessing (AMP) systems.

%package libs
Summary:	Libaries for OpenAMP
%description libs
Libaries for OpenAMP baremetal, and RTOS environments.

%package devel
Summary:	Development files for OpenAMP
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
%description devel
Development file for OpenAMP
baremetal, and RTOS environments.


%prep
%autosetup


%build
%cmake -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
	-DCMAKE_INCLUDE_PATH=%{_includedir}/libmetal/ \
	-DCMAKE_LIBRARY_PATH=%{_libdir} \
	-DWITH_STATIC_LIB=OFF \
	-DWITH_APPS=ON ..
%cmake_build


%install
%cmake_install


%files
%license LICENSE.md
%doc README.md
%{_bindir}/linux_rpc_demo-shared
%{_bindir}/linux_rpc_demod-shared
%{_bindir}/matrix_multiply-shared
%{_bindir}/matrix_multiplyd-shared
%{_bindir}/msg-test-rpmsg-flood-ping-shared
%{_bindir}/msg-test-rpmsg-nocopy-echo-shared
%{_bindir}/msg-test-rpmsg-nocopy-ping-shared
%{_bindir}/msg-test-rpmsg-ping-shared
%{_bindir}/msg-test-rpmsg-update-shared
%{_bindir}/rpc_demod-shared
%{_bindir}/rpmsg-echo-ping-shared
%{_bindir}/rpmsg-echo-shared
%{_bindir}/rpmsg-nocopy-echo-shared
%{_bindir}/rpmsg-nocopy-ping-shared
%{_bindir}/rpmsg-sample-echo-shared
%{_bindir}/rpmsg-sample-ping-shared

%files libs
%{_libdir}/libopen_amp.so.1
%{_libdir}/libopen_amp.so.1.*

%files devel
%{_includedir}/openamp/
%{_libdir}/libopen_amp.so


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2024.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Nov 10 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 2024.10.0-1
- Update to 2024.10.0

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 2023.10.0-5
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2023.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2023.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2023.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Nov 03 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 2023.10.0-1
- Update to 2023.10.0

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2023.04.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue May 02 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 2023.04.0-1
- Update to 2023.04.0
- Split libraries out to sub package

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2020.10.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2020.10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2020.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov  2 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 2020.10.0-1
- Update to 2020.10.0

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2020.04.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2020.04.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 10 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 2020.04.0-1
- Update to 2020.04.0

* Thu Mar 05 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 2020.01.0-1
- Update to 2020.01.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2018.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Peter Robinson <pbrobinson@fedoraproject.org> 2018.10-1
- Update to 2018.10 release

* Sun Oct 14 2018 Peter Robinson <pbrobinson@fedoraproject.org> 2018.04-1
- Update to 2018.04 release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2017.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 20 2018 Jared Smith <jsmith@fedoraproject.org> - 2017.10-2
- Minor fixues for package review

* Fri Feb 16 2018 Jared K. Smith <jsmith@fedoraproject.org> - 2017.10-1
- Initial packaging
