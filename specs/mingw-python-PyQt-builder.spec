%{?mingw_package_header}

%global pkg_name PyQt-builder
%global pypi_name pyqt-builder

Name:           mingw-python-%{pkg_name}
Summary:        MinGW Python %{pkg_name}
Version:        1.17.0
Release:        3%{?dist}
BuildArch:      noarch

License:        BSD-2-Clause
Url:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        %{pypi_source pyqt_builder}
# Assorted mingw fixes
Patch0:         PyQt-builder_mingw.patch
# Drop setuptools scm dependency
Patch1:         pyqt_builder_nosetuptoolsscm.patch


BuildRequires:  mingw32-filesystem >= 102
BuildRequires:  mingw32-python3
BuildRequires:  mingw32-python3-build

BuildRequires:  mingw64-filesystem >= 102
BuildRequires:  mingw64-python3
BuildRequires:  mingw64-python3-build


%description
MinGW Python %{pkg_name}.


%package -n mingw32-python3-%{pkg_name}
Summary:       MinGW Python 3 %{pkg_name}
Requires:      mingw32-sip >= 6.0.0

%description -n mingw32-python3-%{pkg_name}
MinGW Python 3 %{pkg_name}.


%package -n mingw64-python3-%{pkg_name}
Summary:       MinGW Python 3 %{pkg_name}
Requires:      mingw64-sip >= 6.0.0

%description -n mingw64-python3-%{pkg_name}
MinGW Python 3 %{pkg_name}.


%prep
%autosetup -p1 -n pyqt_builder-%{version}
# Set version (see pyqt_builder_nosetuptoolsscm.patch)
sed -i 's|@version@|%version|' pyproject.toml
# Remove bundled egg-info
rm -rf PyQt_builder.egg-info
# Delete precompiled dlls
rm -rf pyqtbuild/bundle/dlls/


%build
%mingw32_py3_build_wheel
%mingw64_py3_build_wheel


%install
%mingw32_py3_install_wheel
%mingw64_py3_install_wheel


%files -n mingw32-python3-%{pkg_name}
%license LICENSE
%{mingw32_bindir}/pyqt-bundle
%{mingw32_bindir}/pyqt-qt-wheel
%{mingw32_python3_sitearch}/pyqtbuild/
%{mingw32_python3_sitearch}/PyQt_builder-%{version}.dist-info/

%files -n mingw64-python3-%{pkg_name}
%license LICENSE
%{mingw64_bindir}/pyqt-bundle
%{mingw64_bindir}/pyqt-qt-wheel
%{mingw64_python3_sitearch}/pyqtbuild/
%{mingw64_python3_sitearch}/PyQt_builder-%{version}.dist-info/


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Dec 10 2024 Sandro Mani <manisandro@gmail.com> - 1.17.0-2
- Fix pylib_lib in PyQt-builder_mingw.patch

* Sun Dec 08 2024 Sandro Mani <manisandro@gmail.com> - 1.17.0-1
- Update to 1.17.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jul 16 2024 Sandro Mani <manisandro@gmail.com> - 1.16.4-1
- Update to 1.16.4

* Wed May 01 2024 Sandro Mani <manisandro@gmail.com> - 1.16.2-1
- Update to 1.16.2

* Sat Feb 24 2024 Sandro Mani <manisandro@gmail.com> - 1.15.4-2
- Rebuild (sip)

* Tue Feb 06 2024 Sandro Mani <manisandro@gmail.com> - 1.15.4-1
- Update to 1.15.4

* Sat Jan 27 2024 Sandro Mani <manisandro@gmail.com> - 1.15.3-5
- Rebuild (sip)

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Oct 19 2023 Sandro Mani <manisandro@gmail.com> - 1.15.3-2
- Bump

* Thu Oct 19 2023 Sandro Mani <manisandro@gmail.com> - 1.15.3-1
- Update to 1.15.3

* Sat Aug 12 2023 Sandro Mani <manisandro@gmail.com> - 1.15.2-2
- Rebuild (sip)

* Sat Jul 29 2023 Sandro Mani <manisandro@gmail.com> - 1.15.2-1
- Update to 1.15.2

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Apr 26 2023 Sandro Mani <manisandro@gmail.com> - 1.15.0-1
- Update to 1.15.0

* Thu Feb 02 2023 Sandro Mani <manisandro@gmail.com> - 1.14.1-1
- Update to 1.14.1

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Oct 19 2022 Sandro Mani <manisandro@gmail.com> - 1.13.0-2
- Switch to python3-build

* Fri Jul 22 2022 Sandro Mani <manisandro@gmail.com> - 1.13.0-1
- Update to 1.13.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Feb 10 2022 Sandro Mani <manisandro@gmail.com> - 1.12.2-4
- Rebuild for new python dependency generator (take two)

* Thu Feb 10 2022 Sandro Mani <manisandro@gmail.com> - 1.12.2-3
- Rebuild for new python dependency generator

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Nov 01 2021 Sandro Mani <manisandro@gmail.com> - 1.12.2-1
- Update to 1.12.2

* Wed Oct 13 2021 Sandro Mani <manisandro@gmail.com> - 1.12.1-1
- Update to 1.12.1

* Tue Oct 05 2021 Sandro Mani <manisandro@gmail.com> - 1.11.0-2
- Restore lost hunk in PyQt-builder_mingw.patch

* Tue Oct 05 2021 Sandro Mani <manisandro@gmail.com> - 1.11.0-1
- Update to 1.11.0

* Thu Sep 23 2021 Sandro Mani <manisandro@gmail.com> - 1.10.3-2
- Disable bundling of pre-built dlls
- License is GPLv2 or GPLv3

* Tue Sep 14 2021 Sandro Mani <manisandro@gmail.com> - 1.10.3-1
- Initial package
