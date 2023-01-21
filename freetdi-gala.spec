%global owner    freetdi
%global project  gala

Name:           %{owner}-%{project}
Version:        1
Release:        5%{?dist}
Summary:        C++ graph abstraction with low-level access

# The project as a whole is GPL-3.0-or-later.
# digraph.h and immutable.h are GPL-2.0-or-later.
License:        GPL-3.0-or-later AND GPL-2.0-or-later
URL:            https://github.com/%{owner}/%{project}
Source0:        %{url}/archive/%{version}/%{project}-%{version}.tar.gz
# Convert from the obsolete stx to tlx
# https://github.com/freetdi/gala/pull/3
Patch0:         %{name}-stx-to-tlx.patch
# Fix FTBFS on 32-bit platforms due to lack of __int128
Patch1:         %{name}-32bit.patch
# Implicit copy constructor with explicit assignment operator is deprecated
Patch2:         %{name}-deprecated.patch
# Remove tautological asserts
Patch3:         %{name}-always-true.patch
# The stdint header is no longer included transitively
Patch4:         %{name}-stdint.patch

BuildArch:      noarch
BuildRequires:  boost-devel
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(tlx)

%description
Gala is a C++ graph implementation inspired by boost/BGL, but with low
level access.  You choose the containers and data types and get full
access -- at your own risk.

%package        devel
Summary:        C++ graph abstraction with low-level access
Provides:       %{name}-static = %{version}-%{release}
Requires:       boost-devel%{?_isa}
Requires:       tlx-devel%{?_isa}

%description    devel
Gala is a C++ graph implementation inspired by boost/BGL, but with low
level access.  You choose the containers and data types and get full
access -- at your own risk.

%prep
%autosetup -p1 -n %{project}-%{version}

# Preserve timestamps
sed -i 's/INSTALL = install/& -p/' Makefile

# The tests build a binary named concepts, which g++ tries to include instead of
# the C++ header named concepts when building the other tests.
mv tests/concepts.cc tests/test-concepts.cc
sed -i 's/concepts/test-concepts/' tests/Makefile

%build
# The configure script is not autotools-based.  Do NOT use %%configure!
./configure --prefix=%{_prefix}

%install
%make_install

%check
make check LOCAL_CXXFLAGS="%{build_cxxflags} -DHAVE_TLX_CONTAINER_BTREE_SET_HPP %{build_ldflags}"

%files devel
%doc README
%{_includedir}/%{project}/

%changelog
* Thu Jan 19 2023 Jerry James <loganjerry@gmail.com> - 1-5
- Add -stdint patch to fix FBTFS

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug 16 2022 Jerry James <loganjerry@gmail.com> - 1-4
- Convert License tag to SPDX

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jul 13 2021 Jerry James <loganjerry@gmail.com> - 1-1
- Version 1
- Drop upstreamed patches: -graph and -is-set

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-5.20191212.ec2df02
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-4.20191212.ec2df02
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun  4 2020 Jerry James <loganjerry@gmail.com> - 0-3.20191212.ec2df02
- Add -graph, -deprecated, -always-true, and -is-set patches

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-2.20191212.ec2df02
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 17 2019 Jerry James <loganjerry@gmail.com> - 0-1.20191212.ec2df02
- Initial RPM
