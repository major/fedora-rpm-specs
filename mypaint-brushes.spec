%global mypaint_data_version 1.0

Name: mypaint-brushes
Version: 1.3.1
Release: 6%{?dist}
Summary: Brushes to be used with the MyPaint library

# According to Licenses.dep5 the files used for building/installing are GPLv2+
# but the shipped brush files are CC0
License: CC0
URL: https://github.com/mypaint/mypaint-brushes
Source0: https://github.com/mypaint/mypaint-brushes/releases/download/v%{version}/mypaint-brushes-%{version}.tar.xz

BuildArch: noarch
BuildRequires: make


%package devel
Summary: Files for developing with mypaint-brushes
Requires: pkgconfig
License: GPLv2+


%description
This package contains brush files for use with MyPaint and other programs.


%description devel
This package contains a pkgconfig file which makes it easier to develop
programs using these brush files.


%prep
%autosetup


%build
%configure
make %{?_smp_mflags}


%install
%make_install


%files
%doc AUTHORS NEWS README
%license COPYING
%dir %{_datadir}/mypaint-data
%dir %{_datadir}/mypaint-data/%{mypaint_data_version}
%{_datadir}/mypaint-data/%{mypaint_data_version}/brushes


%files devel
%license COPYING
%{_datadir}/pkgconfig/mypaint-brushes-%{mypaint_data_version}.pc


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Mar 05 2020 Kalev Lember <klember@redhat.com> - 1.3.1-1
- Update to 1.3.1

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Apr 04 2018 Nils Philippsen <nils@tiptoe.de> - 1.3.0-1
- initial release
