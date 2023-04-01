%global repo_name vcpkg-tool
%global repo_tag 2023-03-29

Name: vcpkg
Version: %(echo %{repo_tag} | sed 's/-/./g')
Release: 1%{?dist}

License: MIT
Summary: C++ Library Manager
URL: https://github.com/microsoft/%{repo_name}
Source0: %{url}/archive/%{repo_tag}/%{name}-%{version}.tar.gz
Source1: %{name}.sh

BuildRequires: catch-devel >= 2.13.0
BuildRequires: cmake
BuildRequires: cmrc-devel
BuildRequires: fmt-devel >= 9.1.0
BuildRequires: gcc-c++
BuildRequires: ninja-build

Requires: cmake%{?_isa}
Requires: gcc-c++%{?_isa}
Requires: git-core%{?_isa}
Requires: ninja-build%{?_isa}

Recommends: aria2%{?_isa}

%description
Vcpkg is a package manager for the different C and C++ libraries.

Vcpkg can collect usage data. The data collected by Microsoft is anonymous.

Fedora package has telemetry disabled by default. If you want to enable
telemetry, you should remove the %{_sysconfdir}/profile.d/%{name}.sh file
or unset the VCPKG_DISABLE_METRICS environment variable.

%prep
%autosetup -n %{repo_name}-%{repo_tag} -p1

# Fixing line endings...
sed -e "s,\r,," -i README.md

# Unbundling catch...
rm -rf include/catch2
ln -svf %{_includedir}/catch2/ include/

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON \
    -DBUILD_TESTING:BOOL=OFF \
    -DVCPKG_BASE_VERSION:STRING=%{repo_tag} \
    -DVCPKG_VERSION:STRING=%{repo_tag} \
    -DVCPKG_DEVELOPMENT_WARNINGS:BOOL=OFF \
    -DVCPKG_WARNINGS_AS_ERRORS:BOOL=OFF \
    -DVCPKG_DEPENDENCY_CMAKERC:BOOL=ON \
    -DVCPKG_DEPENDENCY_EXTERNAL_FMT:BOOL=ON \
    -DVCPKG_BUILD_TLS12_DOWNLOADER:BOOL=OFF \
    -DVCPKG_BUILD_FUZZING:BOOL=OFF \
    -DVCPKG_EMBED_GIT_SHA:BOOL=OFF \
    -DVCPKG_BUILD_BENCHMARKING:BOOL=OFF \
    -DVCPKG_ADD_SOURCELINK:BOOL=OFF
%cmake_build

%install
%cmake_install

# Installing environment options override...
install -D -m 0644 -p "%{SOURCE1}" "%{buildroot}%{_sysconfdir}/profile.d/%{name}.sh"

%files
%doc README.md
%license LICENSE.txt NOTICE.txt
%{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/profile.d/%{name}.sh

%changelog
* Thu Mar 30 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 2023.03.29-1
- Updated to version 2023.03.29.

* Thu Mar 23 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 2023.03.22-1
- Updated to version 2023.03.22.

* Tue Mar 14 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 2023.03.14-1
- Updated to version 2023.03.14.

* Thu Mar 02 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 2023.03.01-1
- Updated to version 2023.03.01.

* Wed Feb 15 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 2023.02.15-1
- Updated to version 2023.02.15.

* Mon Jan 30 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 2023.01.24-1
- Updated to version 2023.01.24.

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2022.12.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 21 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2022.12.14-1
- Updated to version 2022.12.14.

* Fri Nov 11 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2022.11.10-1
- Updated to version 2022.11.10.

* Sat Oct 22 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2022.10.17-1
- Updated to version 2022.10.17.

* Fri Oct 14 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2022.10.12-1
- Updated to version 2022.10.12.

* Fri Sep 02 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2022.09.01-1
- Updated to version 2022.09.01.

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2022.07.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jul 16 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2022.07.14-1
- Updated to version 2022.07.14.

* Sun Jul 10 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2022.06.15-2
- Rebuilt due to fmt library update.

* Fri Jun 17 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2022.06.15-1
- Updated to version 2022.06.15.

* Sat May 14 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2022.05.05-1
- Updated to version 2022.05.05.

* Sat Apr 02 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2022.03.30-1
- Updated to version 2022.03.30.

* Tue Mar 29 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2022.03.25-1
- Updated to version 2022.03.25.

* Sat Mar 05 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2022.03.03-1
- Updated to version 2022.03.03.

* Sat Feb 19 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2022.02.18-1
- Updated to version 2022.02.18.

* Tue Feb 15 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2022.02.11-1
- Updated to version 2022.02.11.

* Fri Feb 04 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2022.02.01-1
- Updated to version 2022.02.01.

* Tue Jan 25 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2022.01.19-1
- Updated to version 2022.01.19.

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2021.12.09-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 09 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 2021.12.09-1
- Updated to version 2021.12.09.

* Tue Nov 09 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 2021.11.02-1
- Updated to version 2021.11.02.

* Sat Oct 30 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 2021.10.25-1
- Updated to version 2021.10.25.

* Sun Sep 12 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 2021.09.10-1
- Updated to version 2021.09.10.

* Tue Aug 17 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 2021.08.12-1
- Updated to version 2021.08.12.

* Wed Aug 04 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 2021.08.03-1
- Updated to version 2021.08.03.

* Sun Jul 25 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 2021.07.21-1
- Initial SPEC release.
