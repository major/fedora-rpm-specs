# Setup _pkgdocdir if not defined already.
%{!?_pkgdocdir:%global _pkgdocdir %{_docdir}/%{name}-%{version}}

%global lc_name colpack
%global giturl  https://github.com/CSCsw/%{name}


Name:           ColPack
Version:        1.0.10
Release:        26%{?dist}
Summary:        Algorithms for specialized vertex coloring problems

License:        LGPL-3.0-or-later
URL:            http://cscapes.cs.purdue.edu
Source0:        %{giturl}/archive/v1.0.10.tar.gz#/%{name}-%{version}.tar.gz

Patch0:         ColPack-CVE-2024-55566.patch

BuildRequires:  chrpath
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make

Provides:       %{lc_name}               = %{version}-%{release}
Provides:       %{lc_name}%{?_isa}       = %{version}-%{release}

%description
ColPack is a package comprising of implementation of algorithms for
specialized vertex coloring problems that arise in sparse derivative
computation. It is written in an object-oriented fashion heavily using
the Standard Template Library (STL).  It is designed to be simple,
modular, extendable and efficient.


%package cli
Summary:        CLI-tool for %{name}

Requires:       %{name}%{?_isa}          = %{version}-%{release}

Provides:       %{lc_name}-cli           = %{version}-%{release}
Provides:       %{lc_name}-cli%{?_isa}   = %{version}-%{release}

%description cli
This package contains a cli-tool for %{name}


%package devel
Summary:        Development files for %{name}

Requires:       %{name}%{?_isa}          = %{version}-%{release}

Provides:       %{lc_name}-devel         = %{version}-%{release}
Provides:       %{lc_name}-devel%{?_isa} = %{version}-%{release}

%description devel
This package contains the development headers and library
for %{name}.


%package doc
Summary:        Documentation files for %{name}
Provides:       %{lc_name}-doc           = %{version}-%{release}

BuildArch:      noarch

%description doc
This package contains the documentation files and some brief examples
for %{name}.


%prep
%autosetup -p 1
autoreconf -fiv

# Preserve examples.
cp -pr SampleDrivers examples
find examples -depth -name '.git*' -print0 | xargs -0 rm -f


%build
%configure			\
	--enable-examples	\
	--enable-openmp		\
	--disable-silent-rules	\
	--disable-static
%make_build


%install
%make_install

# We don't want those libtool dumplings and static libs.
find %{buildroot} -depth -name '*.*a' -print0 | xargs -0 rm -f

# Move the cli-tool to %%{_bindir}
mkdir -p %{buildroot}%{_bindir}
mv -f .libs/%{name} %{buildroot}%{_bindir}

# Kill rpath from binaries.
chrpath --delete %{buildroot}%{_bindir}/%{name}

# Remove build examples.
rm -rf %{buildroot}%{_prefix}/examples

# Install documentation.
mkdir -p %{buildroot}%{_pkgdocdir}
cp -pr AUTHORS ChangeLog README.md examples %{buildroot}%{_pkgdocdir}


%check
%make_build check


%ldconfig_scriptlets


%files
%doc %dir %{_pkgdocdir}
%license COPYING*
%doc %{_pkgdocdir}/README.md
%{_libdir}/lib%{name}.so.*


%files cli
%{_bindir}/%{name}


%files devel
%doc %{_pkgdocdir}/ChangeLog
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so


%files doc
%license %{_datadir}/licenses/%{name}*
%doc %{_pkgdocdir}


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Dec 09 2024 Björn Esser <besser82@fedoraproject.org> - 1.0.10-25
- Fix CVE-2024-55566
  Fixes: rhbz#2331064

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 17 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0.10-23
- convert license to SPDX

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 05 2019 Björn Esser <besser82@fedoraproject.org> - 1.0.10-10
- Use autoreconf instead of a patch
- De-tabbify spec file
- Do not install COPYING* to %%{_pkgdocdir}
- Owning %%{_pkgdocdir} by main and doc package is enough

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Feb 17 2018 Björn Esser <besser82@fedoraproject.org> - 1.0.10-7
- Remove more cruft from spec file

* Sat Feb 17 2018 Björn Esser <besser82@fedoraproject.org> - 1.0.10-6
- Remove cruft from spec file

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 25 2016 Björn Esser <fedora@besser82.io> - 1.0.10-1
- new upstream release

* Wed Feb 24 2016 Björn Esser <fedora@besser82.io> - 1.0.9-8
- fix build with gcc 6 (#1307272)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.0.9-5
- Rebuilt for GCC 5 C++11 ABI change

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jun 18 2014 Björn Esser <bjoern.esser@gmail.com> - 1.0.9-3
- added Patch0 to fix build with openMP on GCC >= 4.9
- restructured spec
- preserve GPLv3-file

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Sep 05 2013 Björn Esser <bjoern.esser@gmail.com> - 1.0.9-1
- Initial rpm release (#1004760)
