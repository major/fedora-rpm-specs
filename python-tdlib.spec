# Get post-release fixes
%global gittag   e8ec9114377574f22ff4447cf29e66411b491b7e
%global shorttag %(cut -b -7 <<< %{gittag})
%global gitdate  20210929

Name:           python-tdlib
Version:        0.9.2
Release:        10.%{gitdate}.%{shorttag}%{?dist}
Summary:        Tree decomposition algorithms

# Project files are a mix of GPL-3.0-or-later and GPL-2.0-or-later.
# BSL-1.0: src/bucket_sorter.hpp, src/minimum_degree_ordering.hpp
License:        GPL-3.0-or-later AND GPL-2.0-or-later AND BSL-1.0
URL:            https://github.com/freetdi/tdlib
Source0:        %{url}/archive/%{gittag}/tdlib-%{shorttag}.tar.gz
# Fix a broken test to find the python header files
Patch0:         %{name}-python-includes.patch
# Fix FTBFS on 32-bit systems
Patch1:         %{name}-32bit.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  boost-devel
BuildRequires:  freetdi-gala-devel
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist cython}

%global _description %{expand:
This package provides tree decomposition algorithms.

A tree decomposition of a simple, loopless, undirected graph G is a tree
T with bags at its nodes containing vertices from G.  The usual
conditions apply.  By convention, a tree is an acyclic graph with exactly
one connected component.  The bagsize of T is the size of the biggest
bag, which is a notion for the (width of T)+1.}

%description %_description

%package -n    python3-tdlib
Summary:       Tree decomposition algorithms for python 3
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description -n python3-tdlib %_description

%package -n    python3-tdlib-devel
Summary:       Headers for python3-tdlib
BuildArch:     noarch
Requires:      python3-tdlib = %{version}-%{release}
Requires:      freetdi-gala-devel

%description -n python3-tdlib-devel
Headers for developing applications that use python3-tdlib.

%prep
%autosetup -p1 -n tdlib-%{gittag}

# Tell cython to generate python 3 code
sed -i 's/--cplus/-3 &/' cython.am

# Install into the arch-specific python directory
sed -i 's/pythondir/pyexecdir/' tdlib/Makefile.am

# Do not override Fedora build flags
sed -i 's/ -Os -march=native//' examples/Makefile.am

# Generate the configure script and Makefile.in files
autoreconf -fi .

%build
%configure --disable-static

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

%make_build

%install
%make_install
rm -f %{buildroot}%{python3_sitearch}/tdlib/*.la

%check
%py3_check_import tdlib

%files
%license COPYING GPL-2 GPL-3
%doc AUTHORS BUGS NEWS README THANKS TODO
%{_libexecdir}/treedec/

%files -n      python3-tdlib
%{python3_sitearch}/tdlib/

%files -n      python3-tdlib-devel
%{_includedir}/treedec/

%changelog
* Wed Jan 17 2024 Jonathan Wakely <jwakely@redhat.com> - 0.9.2-10.20210929.e8ec911
- Rebuilt for Boost 1.83

* Tue Jan 16 2024 Jerry James <loganjerry@gmail.com> - 0.9.2-9.20210929.e8ec911
- Stop building for 32-bit x86

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-9.20210929.e8ec911
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.9.2-8.20210929.e8ec911
- Rebuilt for Python 3.12

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 0.9.2-7.20210929.e8ec911
- Rebuilt for Boost 1.81

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-6.20210929.e8ec911
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 13 2022 Jerry James <loganjerry@gmail.com> - 0.9.2-5.20210929.%{shorttag}%{?dist}
- Convert License tag to SPDX

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-5.20210929.e8ec911
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.9.2-4.20210929.e8ec911
- Rebuilt for Python 3.11

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 0.9.2-3.20210929.e8ec911
- Rebuilt for Boost 1.78

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-2.20210929.e8ec911
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Oct  7 2021 Jerry James <loganjerry@gmail.com> - 0.9.2-1.20210929.e8ec911
- Version 0.9.2

* Tue Aug 17 2021 Jerry James <loganjerry@gmail.com> - 0.9.1-1.20210812.55906e9
- Version 0.9.1 plus bug fixes from git
- Drop upstreamed -gcc11 patch

* Sat Aug 07 2021 Jonathan Wakely <jwakely@redhat.com> - 0.9.0-12.20200404.4c6109e
- Rebuilt for Boost 1.76

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-11.20200404.4c6109e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.9.0-10.20200404.4c6109e
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-9.20200404.4c6109e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 0.9.0-8.20200404.4c6109e
- Rebuilt for Boost 1.75

* Fri Oct 16 2020 Jeff Law <law@redhat.com> - 0.9.0-7.20200404.4c6109e
- Fix missing #include for gcc-11

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-6.20200404.4c6109e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun  4 2020 Jerry James <loganjerry@gmail.com> - 0.9.0-5.20200404.4c6109e
- Update to latest git snapshot

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.0-4.20191218.6611c7c
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-3.20191218.6611c7c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan  7 2020 Jerry James <loganjerry@gmail.com> - 0.9.0-2.20191218.6611c7c
- Install into the arch-specific directory

* Thu Dec 19 2019 Jerry James <loganjerry@gmail.com> - 0.9.0-1.20191218.6611c7c
- Initial RPM
