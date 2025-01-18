#Blaze is a header only library
%global debug_package %{nil}

Name:           blaze
Version:        3.8.2
Release:        6%{?dist}
Summary:        An high-performance C++ math library for dense and sparse arithmetic
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://bitbucket.org/blaze-lib/blaze
Source0:        https://bitbucket.org/blaze-lib/blaze/downloads/%{name}-%{version}.tar.gz

BuildRequires: gcc-c++ >= 4.9
BuildRequires: cmake
BuildRequires: flexiblas-devel
BuildRequires: boost-devel
BuildRequires: make

%global blaze_desc \
Blaze is an open-source, high-performance C++ math library for dense and \
sparse arithmetic. With its state-of-the-art Smart Expression Template \
implementation Blaze combines the elegance and ease of use of a \
domain-specific language with HPC-grade performance, making it one of \
the most intuitive and fastest C++ math libraries available. \

%description 
%{blaze_desc}


%package devel
Summary:    Development headers for BLAZE
Provides:   blaze-static = %{version}-%{release}

Requires: flexiblas-devel
Requires: boost

%description devel
%{blaze_desc}

%prep
%autosetup

%build
pushd blaze
%{cmake} -DLIB=%{_lib} -DBLA_VENDOR=FlexiBLAS %{?cmake_opts:%{cmake_opts}} ..
cd %{__cmake_builddir}
%make_build
cd ..
popd

%install
pushd blaze
cd %{__cmake_builddir}
%make_install
cd ..
popd
rm -rf %{_includedir}/%{name}/CMakeFiles/3.12.2
rm -rf %{_includedir}/%{name}/CMakeFiles/FindOpenMP


%files devel
%doc INSTALL
%license LICENSE
%{_includedir}/%{name}
%{_datadir}/%{name}/cmake/*.cmake
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/cmake

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 3.8.2-5
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Aug 20 2023 Filipe Rosset <rosset.filipe@gmail.com> - 3.8.2-1
- Update to 3.8.2 fixes rhbz#2113122

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jul 13 2021 Björn Esser <besser82@fedoraproject.org> - 3.8-4
- Properly set BLA_VENDOR to FlexiBLAS for cmake >= 3.19

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Aug 27 2020 Iñaki Úcar <iucar@fedoraproject.org> - 3.8-2
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager
* Sat Aug 15  2020 Patrick Diehl  <patrickdiehl@lsu.edu> - 3.8-1
- Update to Blaze 3.8
* Mon Jul 27 2020 Patrick Diehl  <patrickdiehl@lsu.edu> - 3.7-3
- CMake fixes
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild
* Mon Feb 24 2020 Patrick Diehl <patrickdiehl@lsu.edu> - 3.7.1
- Initial Release of blaze 3.7
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-1
- Initial Release of blaze 3.6
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild
* Wed Feb 27 2019 Patrick Diehl <patrickdiehl@lsu.edu> - 3.5-1
- Initial Release of blaze 3.5
* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild
* Thu Nov 22 2018 Patrick Diehl <patrickdiehl@lsu.edu> - 3.4-1
- Initial Release of blaze 3.4





