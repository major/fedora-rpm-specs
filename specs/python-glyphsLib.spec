# Requires https://pypi.org/project/ufonormalizer/, not packaged
%bcond ufo_normalization 0
# Requires https://pypi.org/project/skia-pathops/, not packaged
%bcond colr 0

# If https://pypi.org/project/xmldiff/ were packaged, we could run more tests
%bcond xmldiff 0

%bcond check 1

Name:           python-glyphsLib
Version:        6.12.5
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

BuildArch:      noarch

BuildRequires:  python3-devel
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

%prep
%autosetup -n glyphslib-%{version} -p1
# - Do not generate linting/coverage dependencies:
#   https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r \
%if %{without ufo_normalization}
    -e 's/^(ufo[Nn]ormalizer)\b/# &/' \
%endif
%if %{without colr}
    -e 's/^(skia-pathops)\b/# &/' \
%endif
%if %{without xmldiff}
    -e 's/^(xmldiff)\b/# &/' \
%endif
    -e 's/^(coverage|flake8.*|black)\b/# &/' \
    requirements-dev.in |
  tee requirements-dev-filtered.txt

%generate_buildrequires
%{pyproject_buildrequires \
    %{?with_ufo_normalization:-x ufo_normalization} \
    -x defcon \
    %{?with_colr:-x colr} \
    %{?with_check:requirements-dev-filtered.txt}}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l glyphsLib

install -d '%{buildroot}%{_mandir}/man1'
for bin in glyphs2ufo ufo2glyphs
do
  # We do this in %%install rather than in %%build because we need to use the
  # script entry point that was generated during installation.
  env PYTHONPATH='%{buildroot}%{python3_sitelib}' \
      PYTHONDONTWRITEBYTECODE=1 \
      help2man \
          --no-info \
          --name '%{summary}' \
          --output="%{buildroot}%{_mandir}/man1/${bin}.1" \
          "%{buildroot}%{_bindir}/${bin}"
done

# Mark GlyphData license files in-place rather than installing duplicates.
sed -r -i 's/^(.*GlyphData(_AGL)?_LICENSE)/%%license &/' %{pyproject_files}

%check
%pyproject_check_import
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
%pytest -v -rs ${ignore-}
%endif

%files -n python3-glyphsLib -f %{pyproject_files}
%doc README.rst README.builder.md
%{_bindir}/glyphs2ufo
%{_bindir}/ufo2glyphs
%{_mandir}/man1/glyphs2ufo.1*
%{_mandir}/man1/ufo2glyphs.1*

%changelog
%autochangelog
