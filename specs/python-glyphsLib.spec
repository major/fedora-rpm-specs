# Requires https://pypi.org/project/ufonormalizer/, not packaged
%bcond ufo_normalization 0
# Requires https://pypi.org/project/skia-pathops/, not packaged
%bcond colr 0

# If https://pypi.org/project/xmldiff/ were packaged, we could run more tests
%bcond xmldiff 0

%bcond check 1

Name:           python-glyphsLib
Version:        6.14.0
Release:        %autorelease
Summary:        A bridge from Glyphs source files to UFOs

# The entire package is Apache-2.0, except:
#   MIT AND BSD-3-Clause:
#   - Lib/glyphsLib/data/ (Lib/glyphsLib/data/GlyphData_LICENSE,
#                          Lib/glyphsLib/data/GlyphData_AGL_LICENSE)
#
# Additionally, many files in tests/data/ are OFL-1.1; these appear in the
# source RPM but do not contribute to the licenses of the binary RPMs. Note
# that these are not fonts per se, but font *sources*.
License:        Apache-2.0 AND MIT AND BSD-3-Clause
URL:            https://github.com/googlefonts/glyphsLib
Source:         %{pypi_source glyphslib}

# Add additional license text for GlyphData
# https://github.com/googlefonts/glyphsLib/pull/1073
Patch:          %{url}/pull/1073.patch

BuildSystem:    pyproject
BuildOption(generate_buildrequires): %{shrink:
    %{?with_ufo_normalization:--extras ufo_normalization}
    --extras defcon
    %{?with_colr:--extras colr}
    %{?with_check:requirements-dev.in}
    }
BuildOption(install): --assert-license glyphsLib

BuildArch:      noarch

BuildRequires:  help2man

%global common_description %{expand:
This library provides a bridge from Glyphs source files (.glyphs) to UFOs
(Unified Font Object).}

%description %{common_description}

%package -n python3-glyphsLib
Summary:        %{summary}

%description -n python3-glyphsLib %{common_description}

%if %{with ufo_normalization}
%pyproject_extras_subpkg -n python3-glyphsLib ufo_normalization
%endif
%pyproject_extras_subpkg -n python3-glyphsLib defcon
%if %{with ufo_normalization}
%pyproject_extras_subpkg -n python3-glyphsLib colr
%endif

%prep -a
%if %{without ufo_normalization}
%pyproject_patch_dependency ufonormalizer:ignore
%endif
%if %{without colr}
%pyproject_patch_dependency skia-pathops:ignore
%endif
%if %{without xmldiff}
%pyproject_patch_dependency xmldiff:ignore
%endif
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
%pyproject_patch_dependency black:ignore
%pyproject_patch_dependency coverage:ignore
%pyproject_patch_dependency flake8-bugbear:ignore
%pyproject_patch_dependency flake8:ignore

%install -a
install --directory '%{buildroot}%{_mandir}/man1'
for bin in glyphs2ufo ufo2glyphs
do
  # We do this in %%install rather than in %%build because we need to use the
  # script entry point that was generated during installation.
  %{py3_test_envvars} help2man --no-info --name='%{summary}' \
      --output="%{buildroot}%{_mandir}/man1/${bin}.1" \
      "%{buildroot}%{_bindir}/${bin}"
done

# Mark GlyphData license files in-place rather than installing duplicates.
sed --regexp-extended --in-place \
    's/^(.*GlyphData(_AGL)?_LICENSE)/%%license &/' %{pyproject_files}

%check -a
%if %{with check}
%if %{without ufo_normalization}
ignore="${ignore-} --ignore=tests/builder/builder_test.py"
ignore="${ignore-} --ignore=tests/builder/instances_test.py"
ignore="${ignore-} --ignore=tests/builder/roundtrip_test.py"
ignore="${ignore-} --ignore=tests/test_helpers.py"
ignore="${ignore-} --ignore=tests/writer_test.py"
%endif
%if %{without xmldiff}
ignore="${ignore-} --ignore=tests/builder/designspace_gen_test.py"
ignore="${ignore-} --ignore=tests/builder/interpolation_test.py"
%endif
%pytest --verbose -rs ${ignore-}
%endif

%files -n python3-glyphsLib -f %{pyproject_files}
%doc README.rst README.builder.md
%{_bindir}/glyphs2ufo
%{_bindir}/ufo2glyphs
%{_mandir}/man1/glyphs2ufo.1*
%{_mandir}/man1/ufo2glyphs.1*

%changelog
%autochangelog
