%global         srcname         ufo2ft
%global         forgeurl        https://github.com/googlefonts/ufo2ft
Version:        2.28.0
%global         tag             v%{version}
%forgemeta

Name:           python-%{srcname}
Release:        4%{?dist}
Summary:        A bridge from UFOs to FontTool objects

# The entire source is (SPDX) MIT, except:
#   - Lib/ufo2ft/filters/propagateAnchors.py is Apache-2.0
License:        MIT AND Apache-2.0
URL:            %forgeurl
Source0:        %{pypi_source %{srcname}}


BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(ufolib2)
BuildRequires:  python3dist(defcon)

BuildArch: noarch

# Use cu2qu in fonttools, relax test dependencies
# disable failing tests
# https://github.com/googlefonts/ufo2ft/issues/618
# https://bugzilla.redhat.com/show_bug.cgi?id=2098875
Patch01:  fonttoolscu2qu.patch

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
%forgeautosetup -N
%patch01 -p1 

%generate_buildrequires
%pyproject_buildrequires -x cffsubr,compreffor


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files ufo2ft

# tox seems to require exact dependencies
# which are not the ones in Fedora packages,
# so some tests are expected to fail

%check
# These require the “pathops” extra
k="${k-}${k+ and }not (IntegrationTest and test_removeOverlaps_pathops)"
k="${k-}${k+ and }not (IntegrationTest and test_removeOverlaps_CFF_pathops)"
k="${k-}${k+ and }not (TTFPreProcessorTest and test_custom_filters_as_argument)"
k="${k-}${k+ and }not (TTFInterpolatablePreProcessorTest and test_custom_filters_as_argument)"

%pytest -k "${k-}" tests


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst
 
%changelog
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

