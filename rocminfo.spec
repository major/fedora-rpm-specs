%global rocm_release 5.7
%global rocm_patch 0
%global rocm_version %{rocm_release}.%{rocm_patch}

Name:		rocminfo
Version:	%{rocm_version}
Release:	1%{?dist}
Summary:	ROCm system info utility

License:	NCSA
URL:		https://github.com/RadeonOpenCompute/rocminfo
Source0:	https://github.com/RadeonOpenCompute/rocminfo/archive/rocm-%{version}.tar.gz
Patch0:		0001-adjust-CMAKE_CXX_FLAGS.patch
Patch1:		0002-fix-buildtype-detection.patch

ExclusiveArch: x86_64 aarch64 ppc64le

BuildRequires: make
BuildRequires:	gcc-c++
BuildRequires:	cmake
BuildRequires:	rocm-runtime-devel >= %{rocm_release}.0
BuildRequires:	python3-devel

# rocminfo calls lsmod to check the kernel mode driver status
Requires:		kmod

%description
ROCm system info utility


%prep
%autosetup -n %{name}-rocm-%{version} -p1

%{__python3} %{_rpmconfigdir}/redhat/pathfix.py -i %{__python3} rocm_agent_enumerator

%build
%cmake -DROCM_DIR=/usr
%cmake_build

%install
%cmake_install

#FIXME:
chmod 755 %{buildroot}%{_bindir}/*

%files
%doc README.md
%license License.txt
%{_bindir}/rocm_agent_enumerator
%{_bindir}/rocminfo
#Duplicated files:
%exclude %{_docdir}/*/License.txt


%changelog
* Sun Sep 17 2023 Jeremy Newton <alexjnewt at hotmail dot com> - 5.7.0-1
- Update to 5.7

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 29 2023 Jeremy Newton <alexjnewt at hotmail dot com> - 5.6.0-1
- Update to 5.6

* Mon May 01 2023 Jeremy Newton <alexjnewt at hotmail dot com> - 5.5.0-1
- Update to 5.5

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Dec 18 2022 Jeremy Newton <alexjnewt at hotmail dot com> - 5.4.1-1
- Update to 5.4.1

* Mon Oct 17 2022 Jeremy Newton <alexjnewt at hotmail dot com> - 5.3.0-1
- Update to 5.3.0

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jul 03 2022 Jeremy Newton <alexjnewt at hotmail dot com> - 5.2.0-1
- Update to 5.2.0
- Fix cmake macro use

* Tue Apr 05 2022 Jeremy Newton <alexjnewt at hotmail dot com> - 5.1.0-2
- Enable ppc64le

* Thu Mar 31 2022 Jeremy Newton <alexjnewt at hotmail dot com> - 5.1.0-1
- Update to 5.1.0

* Sat Mar 12 2022 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0.0-2
- Add missing kmod requirement

* Wed Feb 16 2022 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0.0-1
- Update to ROCm version 5.0.0

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.0-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov 24 2020 Philipp Knechtges <philipp-dev@knechtges.com> - 3.9.0-0
- Version 3.9.0

* Tue Sep 22 2020 Jeff Law <law@redhat.com> - 1.0.0-7
- Use cmake_in_source_build to fix FTBFS due to recent cmake macro changes

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 16 2019 Tom Stellard <tstellar@redhat.com> - 1.0.0-1
- 1.0.0 Release

