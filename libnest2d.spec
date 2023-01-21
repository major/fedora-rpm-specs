# Copyright (c) 2020 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

Name:           libnest2d
%global commit  da4782500da4eb8cb6e38e5e3f10164ec5a59778
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Version:        0.4^20200805git%{shortcommit}
Release:        6%{?dist}
Summary:        Library for the 2D bin packaging problem
License:        LGPLv3
URL:            https://github.com/tamasmeszaros/libnest2d
Source:         %{url}/archive/%{commit}/libnest2d-%{shortcommit}.tar.gz

# Add disallowed areas
Patch0:         %{url}/pull/18.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  boost-devel
BuildRequires:  polyclipping-devel
BuildRequires:  pkgconfig(nlopt)

# This is a header only library
%global debug_package %{nil}

%description
A library and framework for the 2D bin packaging problem.


%package devel
Summary:        %{summary}
Provides:       %{name}-static = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       boost-devel
Requires:       polyclipping-devel
Requires:       pkgconfig(nlopt)

%description devel
A library and framework for the 2D bin packaging problem.


%prep
%autosetup -n %{name}-%{commit} -p1
sed -i -e "s/ lib\([^n]\)/ "%{_lib}"\1/" CMakeLists.txt


%build
%cmake -DLIBNEST2D_HEADER_ONLY=ON
%cmake_build


%install
%cmake_install


%files devel
%license LICENSE.txt
%doc README.md
%{_includedir}/libnest2d/
%{_libdir}/cmake/Libnest2D/


%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4^20200805gitda47825-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4^20200805gitda47825-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4^20200805gitda47825-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4^20200805gitda47825-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4^20200805gitda47825-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 28 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4^20200805gitda47825-1
- Initial package adapted from SUSE (by Stefan Brüns <stefan.bruens@rwth-aachen.de>)
