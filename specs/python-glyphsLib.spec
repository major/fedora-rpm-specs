# Requires https://pypi.org/project/ufonormalizer/, not packaged
%bcond ufo_normalization 0
# Requires https://pypi.org/project/skia-pathops/, not packaged
%bcond colr 0

# If https://pypi.org/project/xmldiff/ were packaged, we could run more tests
%bcond xmldiff 0

%bcond check 1

Name:           python-glyphsLib
Version:        6.9.5
Release:        2%{?dist}
Summary:        A bridge from Glyphs source files to UFOs

# The entire package is Apache-2.0, except:
#   MIT:
#   - Lib/glyphsLib/data/ (Lib/glyphsLib/data/GlyphData_LICENSE)
#
# Additionally, many files in tests/data/ are OFL-1.1; these appear in the
# source RPM but do not contribute to the licenses of the binary RPMs. Note
# that these are not fonts per se, but font *sources*.
License:        Apache-2.0 AND MIT
URL:            https://github.com/googlefonts/glyphsLib
Source:         %{pypi_source glyphslib}

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
%license LICENSE
%license Lib/glyphsLib/data/GlyphData_LICENSE
%doc README.rst README.builder.md
%{_bindir}/glyphs2ufo
%{_bindir}/ufo2glyphs
%{_mandir}/man1/glyphs2ufo.1*
%{_mandir}/man1/ufo2glyphs.1*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Dec 06 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 6.9.5-1
- Update to 6.9.5 (close RHBZ#1881116)

* Fri Dec 06 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 5.3.2-1
- Update to 5.3.2 (the last 5.x release)
- Add generated man pages

* Fri Dec 06 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 5.1.11-16
- Update SPDX license expression and document license breakdown; package
  GlyphData_LICENSE as an additional license file
- Port to pyproject-rpm-macros and run most of the tests

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 5.1.11-15
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.11-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 5.1.11-13
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.11-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 5.1.11-9
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 5.1.11-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 5.1.11-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Athos Ribeiro <athoscr@fedoraproject.org> - 5.1.11-1
- Update version

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 14 2020 Athos Ribeiro <athoscr@fedoraproject.org> - 5.1.10-1
- Update version

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.0.0-5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 4.0.0-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.0.0-2
- Rebuilt for Python 3.8

* Sun Jul 28 2019 Athos Ribeiro <athoscr@fedoraproject.org> - 4.0.0-1
- Update version
- Skip test suite due to missing test dependencies (xmldiff, ufoNormalizer)
- Use sources from pypi
- Drop v2 patches
- Drop all Requires in favor of auto generated dependencies

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 12 2018 Miro Hrončok <mhroncok@redhat.com> - 2.2.1-6
- Subpackage python2-glyphsLib has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.2.1-4
- Rebuilt for Python 3.7

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.2.1-3
- Rebuilt for Python 3.7

* Wed Feb 21 2018 Athos Ribeiro <athoscr@fedoraproject.org> - 2.2.1-2
- Include new subdirectories

* Wed Feb 21 2018 Athos Ribeiro <athoscr@fedoraproject.org> - 2.2.1-1
- Update version
- Remove patch merged upstream

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 14 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 1.7.5-2
- Apply patch to remove shebangs from non-executable modules

* Thu Jul 13 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 1.7.5-1
- Update version
- Change package name to use upstream cammelcase

* Mon Apr 10 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 1.6.0-1
- Update version
- Add pythonX-mock BR

* Sun Mar 19 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 1.5.2-1
- Initial package
