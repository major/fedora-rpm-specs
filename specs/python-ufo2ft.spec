# Not packaged: python-skia-pathops
%bcond pathops 0

Name:           python-ufo2ft
Version:        3.7.0
Release:        %autorelease
Summary:        A bridge from UFOs to FontTool objects

# The entire source is (SPDX) MIT, except:
#   - Lib/ufo2ft/filters/propagateAnchors.py is Apache-2.0
License:        MIT AND Apache-2.0
URL:            https://github.com/googlefonts/ufo2ft
Source:         %{pypi_source ufo2ft}

BuildRequires:  python3-devel

BuildArch: noarch

%global _description %{expand:
ufo2ft (“UFO to FontTools”) is a fork of ufo2fdk whose goal is to generate
OpenType font binaries from UFOs (Unified Font Object) without the FDK
dependency.}

%description %_description


%package -n python3-ufo2ft
Summary:        %{summary}

%description -n python3-ufo2ft %_description


%pyproject_extras_subpkg -n python3-ufo2ft cffsubr compreffor
%if %{with pathops}
%pyproject_extras_subpkg -n python3-ufo2ft pathops
%endif


%prep
%autosetup -n ufo2ft-%{version} -p 1

# The file requirements.txt contains some additional test dependencies beyond
# those in the “test” extra, but pins exact versions. Remove the pins and use
# the result to generate BuildRequires.
sed -r -e 's/==[^;]+//' \
%if %{without pathops}
    -e 's/^skia-pathops\b/# &/' \
%endif
    requirements.txt |
  tee requirements-unpinned.txt


%generate_buildrequires
%{pyproject_buildrequires \
    -x cffsubr \
    -x compreffor \
    %{?with_pathops:-x pathops} \
    -x test \
    requirements-unpinned.txt}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l ufo2ft


%check
%if %{without pathops}
k="${k-}${k+ and }not (IntegrationTest and test_removeOverlaps_pathops)"
k="${k-}${k+ and }not (IntegrationTest and test_removeOverlaps_CFF_pathops)"
k="${k-}${k+ and }not (TTFPreProcessorTest and test_custom_filters_as_argument)"
k="${k-}${k+ and }not (TTFInterpolatablePreProcessorTest and test_custom_filters_as_argument)"
%endif
# Test can fail when updates are not synchronized, but is not essential
# https://github.com/googlefonts/ufo2ft/issues/877
k="${k-}${k+ and }not (test_kern_zyyy_zinh)"

%pytest -k "${k-}" tests -rs


%files -n python3-ufo2ft -f %{pyproject_files}
%doc README.rst
 

%changelog
%autochangelog
