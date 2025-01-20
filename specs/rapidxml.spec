Name:           rapidxml
Version:        1.13
Release:        26%{?dist}
Summary:        Fast XML parser
License:        BSL-1.0 OR MIT
URL:            http://rapidxml.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}-with-tests.zip
Patch0:         %{name}-declarations.patch
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  dos2unix

%description
RapidXml is an attempt to create the fastest XML parser possible, while
retaining usability, portability and reasonable W3C compatibility. It is an
in-situ parser written in modern C++, with parsing speed approaching that of
strlen function executed on the same data.

%package devel
Summary:       Fast XML parser
Provides:      %{name}-static = %{version}-%{release}

%description devel
RapidXml is an attempt to create the fastest XML parser possible, while
retaining usability, portability and reasonable W3C compatibility. It is an
in-situ parser written in modern C++, with parsing speed approaching that of
strlen function executed on the same data.

%prep
%setup -qn %{name}-%{version}-with-tests
%patch -P0 -p1

dos2unix license.txt

# Rename it to .h (but keep .hpp for tests)
sed -i 's/.hpp/.h/g' manual.html
for HPP in *.hpp; do
  cp -p $HPP ${HPP%hpp}h
  sed -i 's/.hpp/.h/g' ${HPP%hpp}h
done

%build
cd tests
# -jX is useless here
make build-g++-debug
cd -

%install
for H in *.h; do
  install -Dpm0644 $H %{buildroot}%{_includedir}/$H
done

%check
cd tests
# -jX is useless here
make run-g++-debug
cd -

%files devel
%doc license.txt manual.html
%{_includedir}/*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Apr 09 2023 Iñaki Úcar <iucar@fedoraproject.org> - 1.13-21
- Adapt license tag to SPDX

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 30 2020 Iñaki Úcar <iucar@fedoraproject.org> 1.13-15
- https://fedoraproject.org/wiki/Changes/Remove_make_from_BuildRoot

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Apr 20 2013 Miro Hrončok <mhroncok@redhat.com> - 1.13-2
- devel subpackage now provides -static.

* Sat Feb 02 2013 Miro Hrončok <mhroncok@redhat.com> - 1.13-1
- Initial release
