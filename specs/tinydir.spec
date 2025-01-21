# This package builds a header-only lib, but has some testsuite to check
# the headers' function.  For this reason the main-pkg is build arched
# and produces a noarched subpkg, only.  There is no binary-compiled
# bits and therefore no debuginfo generated.
%global debug_package %{nil}

# Common summary and description.
%global common_sum  Portable and easy to integrate C directory and file reader
%global common_desc \
Lightweight, portable and easy to integrate C directory and file reader. \
TinyDir wraps dirent for POSIX and FindFirstFile for Windows.


Name:           tinydir
Version:        1.2.5
Release:        9%{?dist}
Summary:        %{common_sum}

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/cxong/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

# Testsuite
BuildRequires:  cmake3
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make

%description
%{common_desc}


%package devel
Summary:        %{common_sum} (header-only)
Provides:       %{name}-static == %{version}-%{release}

BuildArch:      noarch

%description devel
%{common_desc}


%prep
%autosetup -p 1


%build
# Make testsuite more verbose on failures.
export CTEST_OUTPUT_ON_FAILURE=1

for d in samples tests; do
  mkdir -p %{_target_platform}_${d}
  pushd %{_target_platform}_${d}
  # I'm intentionally not using the %%cmake-macro here.  This builds
  # no installed binaries, just the testsuite.  Building the tests
  # with system-flags enabled will lead to a bunch of errors during
  # compilation.
  cmake3 -DCMAKE_VERBOSE_MAKEFILE=ON ../${d}
  popd
  %make_build -C %{_target_platform}_${d}
done


%install
mkdir -p %{buildroot}%{_datadir}/pkgconfig %{buildroot}%{_includedir}

# Install headers.
install -pm 0644 %{name}.h %{buildroot}%{_includedir}

# Install pkg-config file.
cat << EOF > %{buildroot}%{_datadir}/pkgconfig/%{name}.pc
prefix=%{_prefix}
exec_prefix=\${prefix}

includedir=%{_includedir}

Name: %{name}
Version: %{version}
Description: %{common_sum}
EOF

# Clean-up for including samples in %%doc.
rm -f samples/{.gitignore,CMakeLists.txt}


%check
pushd %{_target_platform}_tests
ctest3
popd


%files devel
%license COPYING
%doc samples/ package.json README.md
%{_includedir}/%{name}.h
%{_datadir}/pkgconfig/%{name}.pc


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.2.5-8
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Nov 18 2021 Björn Esser <besser82@fedoraproject.org> - 1.2.5-1
- Update to 1.2.5
  Fixes rhbz#2024539

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Björn Esser <besser82@fedoraproject.org> - 1.2.3-1
- New upstream release (rhbz#1472803)

* Thu Mar 30 2017 Björn Esser <besser82@fedoraproject.org> - 1.2.2-1
- New upstream release (rhbz#1437283)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 28 2016 Björn Esser <bjoern.esser@gmail.com> - 1.2.1-1
- New upstream v1.2.1
- Remove Patch0, upstreamed

* Tue Dec 27 2016 Björn Esser <bjoern.esser@gmail.com> - 1.2-0.3.git20161112.683d230
- Initial rpm-release (#1408852)

* Tue Dec 27 2016 Björn Esser <bjoern.esser@gmail.com> - 1.2-0.2.git20161112.683d230
- Add pkg-config file

* Tue Dec 27 2016 Björn Esser <bjoern.esser@gmail.com> - 1.2-0.1.git20161112.683d230
- Initial package (#1408852)
