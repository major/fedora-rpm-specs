Name:           python-cucumber-tag-expressions
Version:        9.0.0
Release:        %autorelease
Summary:        Provides a tag-expression parser and evaluation logic for cucumber/behave

License:        MIT
URL:            https://github.com/cucumber/tag-expressions
# The GitHub archive has test data files; the PyPI sdist does not.
Source:         %{url}/archive/v%{version}/tag-expressions-%{version}.tar.gz

# Downstream-only: loosen the lower bound on uv_build
#
# It was aggressively updated by upstream automation; we can use an older
# version until we catch up.
Patch:          0001-Downstream-only-loosen-the-lower-bound-on-uv_build.patch

BuildSystem:            pyproject
BuildOption(install):   -l cucumber_tag_expressions

BuildArch:      noarch

BuildRequires:  tomcli

# Test dependencies are intermixed with unwanted linting and coverage-analysis
# tools in the “dev” dependency group, so we enumerate them manually.
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
BuildRequires:  %{py3_dist pytest} >= 6.0.1
BuildRequires:  %{py3_dist pyyaml} >= 6.0.3

%global common_description %{expand:
Cucumber tag-expressions provide readable boolean expressions to select
features and scenarios marked with tags in Gherkin files in an easy way.}

%description %{common_description}


%package -n python3-cucumber-tag-expressions
Summary:        %{summary}

%description -n python3-cucumber-tag-expressions %{common_description}


%prep -a
# Python: Do not upper-bound (SemVer-bound) the version of uv_build; we must
# work with what we have, and compatibility across SemVer boundaries is quite
# good in practice.
sed -r -i 's/"(uv_build *>= *[^:]+), *<[^"]+"/"\1"/' python/pyproject.toml


%generate_buildrequires -p
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
cd python


%build -p
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
cd python


%install -p
install -t '%{buildroot}%{_pkgdocdir}/general' -p -m 0644 -D \
    ARCHITECTURE.md CHANGELOG.md README.md
install -t '%{buildroot}%{_pkgdocdir}' -p -m 0644 -D python/README.md


%check -a
%pytest python/tests -v


%files -n python3-cucumber-tag-expressions -f %{pyproject_files}
%doc %{_pkgdocdir}/


%changelog
%autochangelog
