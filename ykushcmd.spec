Name:           ykushcmd
Version:        1.2.3
Release:        5%{?gitsnap:.%{gitsnap}}%{?dist}
Summary:        YKUSH Boards Control Application 
License:        ASL 2.0
URL:            https://github.com/Yepkit/ykush
Source0:        https://github.com/Yepkit/ykush/archive/%{version}/ykush-%{version}.tar.gz

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  hidapi-devel
BuildRequires:  libusbx-devel
BuildRequires:  systemd-devel

%description
Control application for Yepkit YKUSH Switchable USB Hub boards.


%prep
%autosetup -p1 -n ykush-%{version}


%build
make %{?_smp_mflags} CPP="%{__cxx} %{optflags} -I/usr/include/hidapi '-DDOCDIR=\"%{_pkgdocdir}\"'"


%install
mkdir -p %{buildroot}%{_bindir}
install bin/ykushcmd %{buildroot}%{_bindir}


%files
%license LICENSE.md
%doc README.md
%{_bindir}/ykushcmd


%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 04 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 1.2.3-1
- Update to 1.2.3

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Mar 10 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 1.2.2-1
- Update to 1.2.2

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-7.c585d24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6.c585d24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 24 2019 Peter Robinson <pbrobinson@fedoraproject.org> 1.1.0-5.c585d24
- Move to git snapshot to get support for new useful HW

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 16 2018 Lubomir Rintel <lkundrak@v3.sk> - 1.1.0-1
- Address review by Robert-André Mauchin (rh#1534545)
- Drop the superfluous executable bits
- Move to a released version 1.1.0

* Mon Jan 15 2018 Lubomir Rintel <lkundrak@v3.sk> - 1.0.0-1.20180108git01aff0b
- Initial packaging
