%undefine __cmake_in_source_build

Name:           xtensor
Version:        0.24.2
Release:        5%{?dist}
Summary:        C++ tensors with broadcasting and lazy computing
License:        BSD
URL:            http://xtensor.readthedocs.io/

%global github  https://github.com/QuantStack/xtensor
Source0:        %{github}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gtest-devel
BuildRequires:  xtl-devel
BuildRequires:  xsimd-devel
BuildRequires:  python3-numpy
BuildRequires:  doctest-devel

# there is no actual arched content - this is a header only library
%global debug_package %{nil}

%global _description %{expand:
xtensor is a C++ library meant for numerical analysis with multi-dimensional
array expressions.

xtensor provides:
- an extensible expression system enabling lazy broadcasting.
- an API following the idioms of the C++ standard library.
- tools to manipulate array expressions and build upon xtensor.}


%description %_description

%package devel
Summary:        %{summary}
Provides:       %{name} = %{version}-%{release}
Provides:       %{name}-static = %{version}-%{release}
Requires:       xtl-devel
Requires:       xsimd-devel

%description devel %_description


%prep
%autosetup -p1

%ifarch s390x
find -name '*.npy' -exec %{__python3} -c "import numpy as np; np.save('{}', np.load('{}').byteswap().newbyteorder())" \;
%endif

%build
%cmake -DBUILD_TESTS=ON
%cmake_build

%install
%cmake_install

%check
%cmake_build --target xtest

%files devel
%doc README.md
%license LICENSE
%{_includedir}/%{name}.hpp
%{_includedir}/%{name}/
%{_libdir}/cmake/%{name}/
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Mon Jan 29 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 11 2022 sguelton@redhat.com - 0.24.2-1
- Upstream version bump

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Feb 15 2021 sguelton@redhat.com - 0.23.1-1
- Upstream version bump
- More generic use of %cmake_build

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Oct 06 2020 sguelton@redhat.com - 0.21.7-3
- Activate all architectures, fixing the remaining issues in the test suite

* Mon Oct 05 2020 sguelton@redhat.com - 0.21.7-2
- Fix UB in upstream testsuite, see https://github.com/xtensor-stack/xtensor/pull/2175
- Activates armv7hl

* Sat Oct 3 2020 sguelton@redhat.com - 0.21.7-1
- Upstream version bump

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 16 2020 sguelton@redhat.com - 0.21.2-1
- Upstream version bump

* Tue Sep 3 2019 sguelton@redhat.com - 0.20.8-1
- Initial package
