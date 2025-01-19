# el6 compatibility
%{!?__global_ldflags: %global __global_ldflags -Wl,-z,relro}

%global make_flags \\\
        LDFLAGS="%{__global_ldflags} -Lsrc" \\\
        LIBDIR=%{_libdir} \\\
        HWINFO_VERSION=%{version}

Name:           hwinfo
Version:        23.2
Release:        4%{?dist}
Summary:        Hardware information tool

License:        GPL-1.0-or-later
URL:            https://github.com/openSUSE/hwinfo
Source0:        https://github.com/openSUSE/hwinfo/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  libx86emu-devel
BuildRequires:  libuuid-devel
BuildRequires:  gcc
BuildRequires:  flex
BuildRequires:  perl-interpreter
BuildRequires: make
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Obsoletes:      %{name} < 22.2-1


%description
hwinfo is to probe for the hardware present in the system. It can be used to
generate a system overview log which can be later used for support.


%package libs
Summary:        Libraries for hwinfo
Obsoletes:      %{name} < 22.2-1


%description libs
Libraries for using hwinfo, a hardware information tool, in other applications.


%package devel
Summary:        Development files for hwinfo
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}


%description devel
Header files and libraries for developing with libhd library from hwinfo, a
hardware information tool.


%prep
%autosetup


%build
# Parallel make disabled due to missing libhd.a dependency
make %{make_flags}


%install
%make_install %{make_flags}


%ldconfig_scriptlets libs


%files
%{_sbindir}/check_hd
%{_sbindir}/convert_hd
%{_sbindir}/getsysinfo
%{_sbindir}/hwinfo
%{_sbindir}/mk_isdnhwdb
%{_datadir}/hwinfo
%doc *.md MAINTAINER
%license COPYING


%files libs
%license COPYING
%{_libdir}/libhd.so.*


%files devel
%{_includedir}/hd.h
%{_libdir}/pkgconfig/hwinfo.pc
%{_libdir}/libhd.so


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 23.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 23.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 17 2024 Miroslav Suchý <msuchy@redhat.com> - 23.2-2
- convert license to SPDX

* Tue May 21 2024 Lubomir Rintel <lkundrak@v3.sk> - 23.2-1
- Update to 23.2

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 22.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 22.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 22.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon May 08 2023 Andrey Ponomarenko <andrewponomarenko@yandex.ru> - 22.2-1
- Update to 22.2

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 21.80-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 21.80-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Mar 28 2022 Andrey Ponomarenko <andrewponomarenko@yandex.ru> - 21.80-1
- Update to 21.80

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 21.68-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 21.68-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 21.68-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 21.68-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Mar 01 2020 Neal Gompa <ngompa13@gmail.com> - 21.68-1
- Rebase to 21.68
- Split libraries into their own subpackage

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 21.47-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 11 2019 Andrey Ponomarenko <andrewponomarenko@yandex.ru> - 21.47-9
- Bump release to rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 21.47-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 21.47-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 20 2018 Andrey Ponomarenko <andrewponomarenko@yandex.ru> - 21.47-6
- Fix missed __global_ldflags on el6

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 21.47-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 21.47-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 16 2017 Björn Esser <besser82@fedoraproject.org> - 21.47-3
- Properly apply build flags

* Fri Aug 25 2017 Lubomir Rintel <lkundrak@v3.sk> - 21.47-2
- Better align with packaging guidelines

* Tue Aug 01 2017 Lubomir Rintel <lkundrak@v3.sk> - 21.47-1
- Initial packaging
