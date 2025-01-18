%global real_name DICOMAnonymizer
%global forgeurl https://github.com/mmiv-center/%{real_name}
%global commit f0762643caab3d84e522b99cdec4b8d271b12039
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitdate 20210920


# debugsourcefiles.list is empty
%global debug_package %{nil}

Name:    dicomanonymizer
Version: 1

Release: 0.17.%{gitdate}git%{shortcommit}%{dist}
Summary: A multi-threaded anonymizer for DICOM files

%forgemeta

License: Unlicense and MIT
URL:     %{forgeurl}
Source:  %{forgesource}

# https://github.com/mmiv-center/DICOMAnonymizer/issues/3
Patch0: 0001-use-system-gdcm.patch
# https://github.com/mmiv-center/DICOMAnonymizer/issues/14
Patch1: 0002-timeval.patch

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: make
BuildRequires: gdcm-devel
BuildRequires: zlib-devel
BuildRequires: libxml2-devel
BuildRequires: libjpeg-turbo-devel
BuildRequires: libxslt-devel

%description
A multi-threaded anonymizer for DICOM files implementing most of DICOM PS 3.15
AnnexE. Entries such as uid entries are replaced with hash values. This ensures
that partial runs of a studies DICOM files can be merged afterwards. This
project is written in C++ using the gdcm library and multiple threads to
accelerate processing. Warning: The operation performed by this tool is a 'soft'
de-identification. Instead of a white list of allowed tags the tool keeps a list
of tags known to frequently contain personal identifying information (PII) and
replaces only those. On the command line you specify a patient identifier
(PatientID/PatientName). Only if you do not keep a mapping of the new and the
old identifier this is considered an anonymization. If such a list exists the
operation performed is a de-identification (permits a later re-identification).

%prep
%autosetup -n %{real_name}-%{commit}

%build
%cmake -DCMAKE_EXE_LINKER_FLAGS="%{optflags} -fPIE"
%cmake_build

%install
mkdir -p %{buildroot}%{_bindir}
install -pm 0755 %{_vpath_builddir}/anonymize %{buildroot}%{_bindir}/dicomanonymize

%files
%license LICENSE
%doc README.md
%{_bindir}/dicomanonymize

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1-0.17.20210920gitf076264
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1-0.16.20210920gitf076264
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1-0.15.20210920gitf076264
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1-0.14.20210920gitf076264
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1-0.13.20210920gitf076264
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1-0.12.20210920gitf076264
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 28 2022 Alessio <alciregi@fedoraproject.org> - 1-0.11.20210920gitf076264
- Update to latest upstream commit

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1-0.10.20191125gited06792
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1-0.9.20191125gited06792
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 29 2021 Alessio <alciregi@fedoraproject.org> - 1-0.8.20191125gited06792
- Using _vpath_builddir instead of _target_platform

* Thu Jul 29 2021 Alessio <alciregi@fedoraproject.org> - 1-0.7.20191125gited06792
- Using _vpath_builddir instead of _target_platform

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1-0.6.20191125gited06792
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1-0.5.20191125gited06792
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 11 2020 Alessio <alciregi@fedoraproject.org> - 1-0.1.20191125gited06792
- Using %cmake_build macro

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.20191125gited06792
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.20191125gited06792
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20191125gited06792
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 11 2019 Alessio <alciregi@fedoraproject.org> - 0-0.1.20191125gited06792
Initial commit
