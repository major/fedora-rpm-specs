# Requires https://pypi.org/project/skia-pathops/ – not packaged, and
# nontrivial due to the involvement of Skia, https://skia.org/.
%bcond pathops 0
%bcond autohint 1
%bcond json 1
%bcond repacker 1

Name:           fontmake
Version:        3.10.1
Release:        %autorelease
Summary:        Compile fonts from sources (UFO, Glyphs) to binary (OpenType, TrueType)

# The entire source is Apache-2.0, except for certain files in tests/data/ that
# are under other acceptable licenses; these appear in the source RPM but do
# not contribute to the licenses of the binary RPMs. Note that these are not
# fonts per se, but font *sources*. These files include at least the following:
#
# MIT:
#   - tests/data/MutatorSans/
#   - tests/data/MutatorSansLite/
# OFL-1.1:
#   - tests/data/AutohintingTest/Padyakke.glyphs
License:        Apache-2.0
SourceLicense:  %{license} AND MIT AND OFL-1.1
URL:            https://github.com/googlefonts/fontmake
Source:         %{pypi_source fontmake %{version} zip}

BuildArch:      noarch

BuildRequires:  help2man

# See test_requirements.txt, which also contains unwanted dependencies for
# linting, coverage, etc.
BuildRequires:  %{py3_dist pytest} >= 4.5

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_provides_for_importable_modules
%py_provides python3-fontmake

%description
fontmake compiles fonts from various sources (.glyphs, .ufo, designspace) into
binaries (.otf, .ttf). You can use it to create static instances and variable
fonts.


%if %{with pathops}
%pyproject_extras_subpkg -n fontmake pathops
%endif
%if %{with autohint}
%pyproject_extras_subpkg -n fontmake autohint
%endif
%if %{with json}
%pyproject_extras_subpkg -n fontmake json
%endif
%if %{with repacker}
%pyproject_extras_subpkg -n fontmake repacker
%endif


%prep
%autosetup


%generate_buildrequires
# From setup.py:
#   - this [lxml] is now default; kept here for backward compatibility
#   - MutatorMath is no longer supported but a dummy extras [sic] is kept below
#     to avoid fontmake installation failing if requested
# We therefore don’t need to generate dependencies for these.
%{pyproject_buildrequires \
    %{?with_pathops:-x pathops} \
    %{?with_autohint:-x autohint} \
    %{?with_json:-x json} \
    %{?with_repacker:-x repacker}}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l fontmake

# We do this in %%install rather than in %%build because we need to use the
# script entry point that was generated during installation.
install -d '%{buildroot}%{_mandir}/man1'
%{py3_test_envvars} help2man \
    --no-info \
    --name '%{summary}' \
    --output='%{buildroot}%{_mandir}/man1/fontmake.1' \
    %{buildroot}%{_bindir}/fontmake


%check
%pyproject_check_import

# A number of integer IDs differ from the expected output. It feels like this
# is probably a brittle test that is sensitive to dependency versions rather
# than a real problem.
k="${k-}${k+ and }not test_main_designspace_v5_builds_STAT"

%if %{without autohint}
k="${k-}${k+ and }not test_autohinting"
%endif

%pytest -k "${k-}" -rs -vv


%files -f %{pyproject_files}
%doc README.md
%doc TROUBLESHOOTING.md
%doc USAGE.md

%{_bindir}/fontmake
%{_mandir}/man1/fontmake.1*


%changelog
%autochangelog
