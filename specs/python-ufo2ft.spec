%global         srcname         ufo2ft
%global         forgeurl        https://github.com/googlefonts/ufo2ft
Version:        3.6.8
%global         tag             v%{version}
%forgemeta

Name:           python-%{srcname}
Release:        1%{?dist}
Summary:        A bridge from UFOs to FontTool objects

# The entire source is (SPDX) MIT, except:
#   - Lib/ufo2ft/filters/propagateAnchors.py is Apache-2.0
License:        MIT AND Apache-2.0
URL:            %forgeurl
Source:         %{pypi_source %{srcname}}

BuildRequires:  python3-devel
BuildRequires:  python3dist(ufolib2)
BuildRequires:  python3dist(defcon)
BuildArch: noarch

%global _description %{expand:
ufo2ft (“UFO to FontTools”) is a fork of ufo2fdk whose goal is to generate
OpenType font binaries from UFOs (Unified Font Object) without the FDK
dependency.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description

# Cannot package “pathops” extra until python3dist(skia-pathops) is packaged
%pyproject_extras_subpkg -n python3-%{srcname} cffsubr compreffor

%prep
%autosetup -n %{srcname}-%{version} -p 1

%generate_buildrequires
%pyproject_buildrequires -x cffsubr,compreffor,test


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l ufo2ft

%check
# These require the “pathops” extra
k="${k-}${k+ and }not (IntegrationTest and test_removeOverlaps_pathops)"
k="${k-}${k+ and }not (IntegrationTest and test_removeOverlaps_CFF_pathops)"
k="${k-}${k+ and }not (TTFPreProcessorTest and test_custom_filters_as_argument)"
k="${k-}${k+ and }not (TTFInterpolatablePreProcessorTest and test_custom_filters_as_argument)"
# Test can fail when updates are not synchronized, but is not essential
# https://github.com/googlefonts/ufo2ft/issues/877
k="${k-}${k+ and }not (test_kern_zyyy_zinh)"

%pytest -k "${k-}" tests


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst
 
%changelog
* Wed Oct 15 2025 Benjamin A. Beasley <code@musicinmybrain.net> - 3.6.8-1
- Update to 3.6.8 (close RHBZ#2397679)

* Fri Sep 19 2025 Benjamin A. Beasley <code@musicinmybrain.net> - 3.6.5-1
- Update to 3.6.6 (close RHBZ#2396951)

* Fri Sep 19 2025 Python Maint <python-maint@redhat.com> - 3.6.4-3
- Rebuilt for Python 3.14.0rc3 bytecode

* Thu Sep 18 2025 Benjamin A. Beasley <code@musicinmybrain.net> - 3.6.4-2
- Update to 3.6.4 (close RHBZ#2396163)

* Tue Sep 09 2025 Benson Muite <fed500@fedoraproject.org> - 3.6.3-1
- Update to 3.6.3 (close RHBZ#2394037)

* Wed Aug 20 2025 Benjamin A. Beasley <code@musicinmybrain.net> - 3.6.0-3
- Patch tests for fonttools 4.59.1

* Fri Aug 15 2025 Python Maint <python-maint@redhat.com> - 3.6.0-2
- Rebuilt for Python 3.14.0rc2 bytecode

* Sat Jul 26 2025 Benjamin A. Beasley <code@musicinmybrain.net> - 3.6.0-1
- Update to 3.6.0 (close RHBZ#2383556)

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Wed Jul 09 2025 Benjamin A. Beasley <code@musicinmybrain.net> - 3.5.1-1
- Update to 3.5.1 (close RHBZ#2376167)
- Backport patch for current fonttools

* Mon Jun 16 2025 Benjamin A. Beasley <code@musicinmybrain.net> - 3.5.0-4
- Update to 3.5.0 (close RHBZ#2361673)
- Report and skip brittle integration tests failing with current fonttools;
  fixes RHBZ#2372184

* Sun Jun 15 2025 Python Maint <python-maint@redhat.com> - 3.4.2-3
- Rebuilt for Python 3.14

* Wed Mar 12 2025 Benson Muite <fed500@fedoraproject.org> - 3.4.2-1
- Upgrade to latest release

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Oct 12 2024 Benson Muite <benson_muite@emailplus.org> - 3.3.1-1
- Update to latest release

* Wed Oct 09 2024 Benson Muite <benson_muite@emailplus.org> - 3.3.0^20241007git0e2fa7-1
- Update to latest release

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.32.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 17 2024 Python Maint <python-maint@redhat.com> - 2.32.0-5
- Rebuilt for Python 3.13

* Wed Feb 21 2024 Benson Muite <benson_muite@emailplus.org> - 3.1.0-1
- Update to latest release

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.32.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.32.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.32.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 23 2023 Benson Muite <benson_muite@emailplus.org> - 2.32.0-1
- Upgrade to latest release
- Remove fonttoolscu2qu.patch as no longer needed

* Mon Jun 19 2023 Python Maint <python-maint@redhat.com> - 2.28.0-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.28.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Oct 15 2022 Benjamin A. Beasley <code@musicinmybrain.net> - 2.28.0-3
- Fix SPDX expression (and→AND)
- Drop obsolete python_provide macro
- Drop redundant explicit BR’s
- Package “cffsubr” and “compreffor” extras
- Skip/xfail fewer tests; move unrelated skips out of fonttoolscu2qu.patch

* Tue Aug 30 2022 Benson Muite <benson_muite@emailplus.org> - 2.28.0-2
- Update license information as indicated in review

* Sun Aug 28 2022 Benson Muite <benson_muite@emailplus.org> - 2.28.0-1
- Update version
- Add patch to relax dependency requirements

* Sun Jun 05 2022 Benson Muite <benson_muite@emailplus.org> - 2.27.0-1
- Version update
- Drop Python 2
- Update spec file format

* Wed Feb 21 2018 Athos Ribeiro <athoscr@fedoraproject.org> - 1.1.0-3
- Include new subdirectories

* Wed Feb 21 2018 Athos Ribeiro <athoscr@fedoraproject.org> - 1.1.0-2
- Add booleanOperations requirement

* Wed Feb 21 2018 Athos Ribeiro <athoscr@fedoraproject.org> - 1.1.0-1
- Version update

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 24 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 0.6.2-1
- Version update

* Mon Apr 10 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 0.4.2-1
- Version update
- Remove patch merged upstream. See https://github.com/googlei18n/ufo2ft/pull/121

* Thu Mar 23 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 0.4.0-1
- Initial package
