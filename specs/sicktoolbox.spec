Name:           sicktoolbox
Version:        1.0.1
Release:        25%{?dist}
Summary:        The SICK LIDAR Toolbox

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://sicktoolbox.sourceforge.net
Source0:        http://downloads.sourceforge.net/%{name}/%{version}/%{name}-%{version}.tar.gz
# Add missing unistd.h to source files.
# Filed upstream at https://sourceforge.net/tracker/?func=detail&aid=3577232&group_id=219500&atid=1047068
Patch0:         %{name}-1.0.1-fixbuild.patch
# Fix c++14 incompatibilities
# Filed upstream at https://sourceforge.net/p/sicktoolbox/patches/5/
Patch1:         %{name}-1.0.1-g++14.patch

BuildRequires: make
BuildRequires:  gcc-c++

%description
The Sick LIDAR Toolbox is an open-source software package released under a
BSD Open-Source License that provides stable and easy-to-use C++ drivers
for Sick LMS 2xx and Sick LD laser range finders.

%package devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
Summary:        Development headers and libraries for %{name}

%description devel
Development headers and libraries for %{name}

%package doc
Requires:       %{name} = %{version}-%{release}
Summary:        Documentation for %{name}
BuildArch:      noarch

%description doc
Assorted documentation for %{name}.

%prep
%setup -q
%patch -P0 -p0
%patch -P1 -p1

%build
export CXXFLAGS="-std=c++14 $RPM_OPT_FLAGS"
%configure --disable-static --program-prefix=sick_
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
rm -rf %{buildroot}%{_libdir}/*.la

%ldconfig_scriptlets

%files
%license COPYING
%doc AUTHORS ChangeLog README THANKS NEWS
%{_bindir}/*_config
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%{_includedir}/sicklms-1.0
%{_includedir}/sickld-1.0

%files doc
%doc manuals/*.pdf

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0.1-24
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Jeff Law <law@redhat.com> - 1.0.1-14
- Force C++14 as this code is not C++17 ready

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 05 2016 Rich Mattes <richmattes@gmail.com> - 1.0.1-5
- Apply Ralf's patch to fix FTBFS (rhbz#1308128)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Sep 18 2015 Rich Mattes <richmattes@gmail.com> - 1.0.1-4
- Address last comments from package review

* Sat Sep 05 2015 Rich Mattes <richmattes@gmail.com> - 1.0.1-3
- Disabled static libraries
- Added "sick_" program prefix for binaries

* Sun Oct 14 2012 Rich Mattes <richmattes@gmail.com> - 1.0.1-2
- Split off -doc subpackage with pdf documentation
- Got rid of dependency on chrpath
- Added link to upstream tracker for fixbuild patch

* Tue Jun 05 2012 Rich Mattes <richmattes@gmail.com> - 1.0.1-1
- Initial package (rhbz#829097)
