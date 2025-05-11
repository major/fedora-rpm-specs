%bcond tests 1

Name:           python-ttfautohint-py
Version:        0.5.1
Release:        %autorelease
Summary:        Python wrapper for ttfautohint, a free auto-hinter for TrueType fonts

License:        MIT
# The entire source is MIT, except for test fonts that are not bundled in the
# binary RPMs and do not contribute to their licenses.
#
# OFL-1.1, tests/data/OFL.txt
#   - tests/data/NotoSansMono-Regular.ttf
SourceLicense:  %{license} AND OFL-1.1
URL:            https://github.com/fonttools/ttfautohint-py
# The PyPI sdist would work perfectly well here, but using the GitHub archive
# has an advantage: if upstream starts including sources included via git
# submodules in src/c/{freetype2,harfbuzz,ttfautohint}/ in the sdist and we
# don’t notice, we might accidentally include some questionably-licensed test
# fonts in the source RPM in the future. With the GitHub archive, we can be
# confident that nothing outside of the upstream source repository itself will
# appear in the source archive.
Source:         %{url}/archive/v%{version}/ttfautohint-py-%{version}.tar.gz

# python: ttfautohint: Python 3.12 support
# https://github.com/fonttools/ttfautohint-py/pull/22
#
# Eliminates use of the deprecated pkg_resources module, and (since
# pkg_resources was moved to setuptools) fixes an undeclared runtime dependency
# on setuptools.
Patch:         %{url}/pull/22.patch

BuildSystem:            pyproject
%if %{with tests}
BuildOption(generate_buildrequires): test-requirements-filtered.txt
%endif
BuildOption(install):   -l ttfautohint

BuildArch: noarch

BuildRequires:  ttfautohint-devel

%global common_description %{expand:
%{summary}.}

%description %{common_description}


%package -n python3-ttfautohint-py
Summary:        %{summary}

# The ttfautohint shared library is loaded at runtime using Python’s ctypes
# module, which in the end is using dlopen(). Since the shared library is not
# linked into an ELF file, the automatic dependency generator cannot help us
# here, and an explicit manual dependency is required.
Requires:       ttfautohint-libs

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_provides_for_importable_modules
%py_provides python3-ttfautohint

%description -n python3-ttfautohint-py %{common_description}


%prep -a
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r -s 's/^(coverage)\b/# &/' test-requirements.txt |
  tee test-requirements-filtered.txt


%generate_buildrequires -p
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'



%build -p
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'


%check -a
%if %{with tests}
%pytest -v
%endif


%files -n python3-ttfautohint-py -f %{pyproject_files}
%doc README.rst


%changelog
%autochangelog
