%global POSTYEAR 2020
%global POSTMONTH 12
%global POSTNUM 1

Name:           libbtbb
Version:        %{POSTYEAR}.%{POSTMONTH}.R%{POSTNUM}
Release:        12%{?dist}
Summary:        A Bluetooth baseband decoding library
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            https://github.com/greatscottgadgets/libbtbb
Source0:        https://github.com/greatscottgadgets/libbtbb/archive/%{POSTYEAR}-%{POSTMONTH}-R%{POSTNUM}.tar.gz

BuildRequires:  cmake gcc-c++
BuildRequires: make

%description
This is the Bluetooth baseband decoding library, forked from the GR-Bluetooth
project. It can be used to extract Bluetooth packet and piconet information
from Ubertooth devices as well as GR-Bluetooth/USRP.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n %{name}-%{POSTYEAR}-%{POSTMONTH}-R%{POSTNUM}


%build
%cmake -DENABLE_PYTHON=OFF -B . -S .
%make_build


%install
%make_install


%ldconfig_scriptlets


%files
%license LICENSE
%{_libdir}/%{name}.so.*

%files devel
%{_includedir}/*
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2020.12.R1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 2020.12.R1-11
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2020.12.R1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2020.12.R1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2020.12.R1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2020.12.R1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2020.12.R1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2020.12.R1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2020.12.R1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020.12.R1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020.12.R1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 30 2020 Sergey Avseyev <sergey.avseyev@gmail.com> 2020.12.R1-1
- Update to 2020-12-R1

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2018.12.R1-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2018.12.R1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2018.12.R1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.12.R1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.12.R1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Sergey Avseyev <sergey.avseyev@gmail.com> - 2018.12.R1-2
- Add explicit curdir on CMake invocation

* Thu Dec 06 2018 Sergey Avseyev <sergey.avseyev@gmail.com> 2018.12.R1-1
- Update to 2018-12-R1

* Fri Aug 10 2018 Sergey Avseyev <sergey.avseyev@gmail.com> 2018.08.R1-1
- Update to 2018-08-R1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2018.06.R1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Sergey Avseyev <sergey.avseyev@gmail.com> 2018.06.R1-2
- Fix changelog in spec

* Wed Jun 27 2018 Sergey Avseyev <sergey.avseyev@gmail.com> 2018.06.R1-1
- Update to 2018-06-R1

* Tue Apr 17 2018 Sergey Avseyev <sergey.avseyev@gmail.com> 2017.03.R2-1
- Initial import
